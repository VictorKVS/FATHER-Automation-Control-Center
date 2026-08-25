from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path, PureWindowsPath

try:
    from scripts.model_dedup_wave1 import LinkAction, gib, norm, under, drive, verify_actions
except ModuleNotFoundError:  # direct execution: python scripts\model_dedup_wave2.py
    from model_dedup_wave1 import LinkAction, gib, norm, under, drive, verify_actions


SCHEMA = "father-model-hardlink-wave2.v0.1"

# Wave 2A is deliberately conservative: only old/archival image-generation trees
# under G:\1\Прежде\1_izobraznie\AI are eligible as hardlink targets.
# Current standalone ComfyUI and MindForge resource trees are protected.
WAVE2_TARGET_PREFIXES = (
    r"G:\1\Прежде\1_izobraznie\AI\ComfyUI\ComfyUI",
    r"G:\1\Прежде\1_izobraznie\AI\ComfyUI\models",
    r"G:\1\Прежде\1_izobraznie\AI\models\StableDiffusion",
    r"G:\1\Прежде\1_izobraznie\AI\stable-diffusion-webui-forge_old",
    r"G:\1\Прежде\1_izobraznie\AI\stable-diffusion-webui-OLD",
)

PREFERRED_CANONICAL_PREFIXES = (
    r"G:\1\Прежде\1_izobraznie\AI\models\checkpoints",
    r"G:\1\Прежде\1_izobraznie\AI\models\loras",
    r"G:\1\Прежде\1_izobraznie\MindForge_Studio\llm_baza\ai_models\sd\vae",
)

PROTECTED_TARGET_PREFIXES = (
    "C:\\",
    r"G:\1\Прежде\1_izobraznie\ComfyUI",
    r"G:\1\Прежде\1_izobraznie\MindForge_Studio\resources\models",
    r"G:\1\OSINT_deepseek",
    r"G:\1\FATHER-Automation-Control-Center",
    r"G:\1\OTUS",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_dedup_plan(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    groups = payload.get("exact_duplicate_groups")
    if not isinstance(groups, list):
        raise ValueError("dedup plan has no exact_duplicate_groups list")
    return payload


def is_target(path: str) -> bool:
    return any(under(path, prefix) for prefix in WAVE2_TARGET_PREFIXES)


def is_protected(path: str) -> bool:
    return any(under(path, prefix) for prefix in PROTECTED_TARGET_PREFIXES)


def choose_canonical(g_paths: list[str], selected: list[str]) -> str | None:
    # Prefer a stable model-library copy that is outside the Wave 2 target set.
    for prefix in PREFERRED_CANONICAL_PREFIXES:
        for path in g_paths:
            if under(path, prefix) and not is_target(path):
                return path

    # Otherwise use any non-target G: path in the same exact SHA group.
    for path in g_paths:
        if not is_target(path):
            return path

    # Last resort: retain the first selected path as physical canonical and only
    # link the remaining selected paths to it. This still preserves all paths.
    return selected[0] if selected else None


def build_actions(payload: dict) -> list[LinkAction]:
    actions: list[LinkAction] = []
    for group in payload["exact_duplicate_groups"]:
        sha = str(group.get("sha256") or "").casefold()
        if len(sha) != 64:
            continue
        size = int(group.get("size_bytes_each") or 0)
        if size <= 0:
            continue

        all_paths = [str(value) for value in group.get("paths", [])]
        g_paths = [path for path in all_paths if drive(path) == "g:"]
        selected = [path for path in g_paths if is_target(path)]
        if not selected or len(g_paths) < 2:
            continue

        canonical = choose_canonical(g_paths, selected)
        if not canonical or drive(canonical) != "g:":
            continue
        if is_protected(canonical) and is_target(canonical):
            raise RuntimeError(f"protected canonical also selected as target: {canonical}")

        for target in selected:
            if norm(target) == norm(canonical):
                continue
            if is_protected(target):
                raise RuntimeError(f"protected path selected as target: {target}")
            if not is_target(target):
                raise RuntimeError(f"target escaped Wave 2 allowlist: {target}")
            if drive(target) != drive(canonical):
                raise RuntimeError(f"cross-volume hardlink requested: {target} -> {canonical}")
            actions.append(
                LinkAction(
                    group_id=str(group.get("group_id") or ""),
                    sha256=sha,
                    size_bytes=size,
                    canonical=canonical,
                    target=target,
                    expected_reclaim_bytes=size,
                )
            )
    return actions


def write_reports(actions: list[LinkAction], output: Path, mode: str, source_plan: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    expected = sum(action.expected_reclaim_bytes for action in actions)
    counters = {
        "actions": len(actions),
        "groups": len({action.group_id for action in actions}),
        "expected_reclaim_bytes": expected,
        "expected_reclaim_gib": gib(expected),
        "verified_actions": sum(action.status == "VERIFIED" for action in actions),
        "already_linked_actions": sum(action.status == "ALREADY_LINKED" for action in actions),
        "blocked_actions": sum(action.status == "BLOCKED" for action in actions),
    }
    payload = {
        "schema_version": SCHEMA,
        "generated_at": utc_now(),
        "mode": mode,
        "source_plan": str(source_plan),
        "strategy": "NTFS_HARDLINK_PRESERVE_PATH",
        "read_only": True,
        "apply_supported": False,
        "wave2_target_prefixes": list(WAVE2_TARGET_PREFIXES),
        "preferred_canonical_prefixes": list(PREFERRED_CANONICAL_PREFIXES),
        "protected_target_prefixes": list(PROTECTED_TARGET_PREFIXES),
        "counters": counters,
        "actions": [asdict(action) for action in actions],
    }
    (output / "wave2_hardlink_plan.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# FATHER Model Dedup — Wave 2A Image Plan",
        "",
        "> READ ONLY. No file is moved, deleted or linked by this tool.",
        "> Only exact SHA-256 duplicate groups are eligible.",
        "> Current standalone ComfyUI and MindForge resource trees remain protected.",
        "",
        f"- mode: **{mode}**",
        f"- exact groups selected: **{counters['groups']}**",
        f"- target paths selected: **{counters['actions']}**",
        f"- expected physical reclaim if later applied: **{counters['expected_reclaim_gib']} GiB**",
        f"- verified: **{counters['verified_actions']}**",
        f"- already linked: **{counters['already_linked_actions']}**",
        f"- blocked: **{counters['blocked_actions']}**",
        "",
        "| Group | GiB | Status | Canonical survivor | Preserved target path |",
        "|---|---:|---|---|---|",
    ]
    for action in actions:
        lines.append(
            f"| {action.group_id} | {gib(action.size_bytes)} | {action.status} | "
            f"`{action.canonical}` | `{action.target}` |"
        )
    (output / "wave2_hardlink_plan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="FATHER Wave 2A read-only image-model exact-duplicate planner."
    )
    parser.add_argument(
        "--plan",
        default="reports/model_inventory/generated/model_dedup_plan.json",
        help="model_dedup_plan.json produced by model_inventory_v2.py",
    )
    parser.add_argument(
        "--output",
        default="reports/model_inventory/consolidation_wave2",
        help="directory for Wave 2A reports",
    )
    parser.add_argument("--mode", choices=("plan", "verify"), default="plan")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_plan = Path(args.plan)
    output = Path(args.output)
    print("FATHER Model Dedup Wave 2A — image models, READ ONLY")
    print(f"mode={args.mode}")
    print(f"source_plan={source_plan.absolute()}")

    if not source_plan.is_file():
        print("status=BLOCKED")
        print("reason=DEDUP_PLAN_NOT_FOUND")
        return 2

    try:
        payload = load_dedup_plan(source_plan)
        actions = build_actions(payload)
    except Exception as exc:
        print("status=BLOCKED")
        print(f"reason={type(exc).__name__}: {exc}")
        return 3

    print(f"groups={len({action.group_id for action in actions})}")
    print(f"targets={len(actions)}")
    print(f"expected_reclaim_gib={gib(sum(action.expected_reclaim_bytes for action in actions))}")

    if not actions:
        write_reports(actions, output, args.mode, source_plan)
        print(f"output={output.absolute()}")
        print("status=NO_WAVE2_ACTIONS")
        return 0

    if args.mode == "verify":
        try:
            ok, actions = verify_actions(actions)
        except KeyboardInterrupt:
            write_reports(actions, output, "verify_INTERRUPTED", source_plan)
            print("status=INTERRUPTED")
            return 130
        except Exception as exc:
            write_reports(actions, output, "verify_FAILED", source_plan)
            print("status=BLOCKED")
            print(f"reason={type(exc).__name__}: {exc}")
            return 5
        write_reports(actions, output, args.mode, source_plan)
        print(f"output={output.absolute()}")
        if not ok:
            print("status=BLOCKED")
            return 4
        print("status=WAVE2_VERIFIED")
        return 0

    write_reports(actions, output, args.mode, source_plan)
    print(f"output={output.absolute()}")
    print("status=WAVE2_PLAN_READY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
