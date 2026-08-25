from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path, PureWindowsPath


SCHEMA = "father-model-hardlink-wave1.v0.1"
CONFIRM_PHRASE = "APPLY_WAVE1_HARDLINKS"

# Wave 1 is intentionally narrow. It touches only old project/archive model trees
# on G:. Runtime-owned C: stores, Ollama, ComfyUI image trees and active project
# paths are not targets in this pass.
WAVE1_TARGET_PREFIXES = (
    r"G:\1\Прежде\KNOWLEDGE_CORE",
    r"G:\1\Прежде\MF-KNOWLEDGE-BRAIN",
    r"G:\1\Прежде\Sokrat",
)

# When an already active G: copy belongs to the same exact SHA group, prefer it
# as the canonical inode and convert only archive copies into links to it.
PREFERRED_CANONICAL_PREFIXES = (
    r"G:\1\OSINT_deepseek\data\models",
)

# Explicitly never target these locations in Wave 1.
PROTECTED_TARGET_PREFIXES = (
    r"C:\",
    r"G:\1\OSINT_deepseek",
    r"G:\1\FATHER-Automation-Control-Center",
    r"G:\1\OTUS",
)


@dataclass
class LinkAction:
    group_id: str
    sha256: str
    size_bytes: int
    canonical: str
    target: str
    expected_reclaim_bytes: int
    status: str = "PLANNED"
    detail: str = ""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def norm(path: str) -> str:
    return str(PureWindowsPath(path)).casefold()


def under(path: str, prefix: str) -> bool:
    p = norm(path)
    root = norm(prefix).rstrip("\\")
    return p == root or p.startswith(root + "\\")


def drive(path: str) -> str:
    return PureWindowsPath(path).drive.casefold()


def sha256_file(path: Path, chunk_size: int = 16 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def gib(value: int) -> float:
    return round(value / (1024 ** 3), 3)


def load_dedup_plan(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload.get("exact_duplicate_groups"), list):
        raise ValueError("dedup plan has no exact_duplicate_groups list")
    if payload.get("automatic_delete_allowed") is True:
        # This tool never relies on automatic deletion policy.
        print("warning=source_plan_allows_auto_delete_but_wave1_still_requires_explicit_confirmation")
    return payload


def choose_canonical(g_paths: list[str], selected: list[str]) -> str:
    # First choice: an active G: model path already in the same SHA group.
    for path in g_paths:
        if any(under(path, prefix) for prefix in PREFERRED_CANONICAL_PREFIXES):
            return path
    # Otherwise keep the first archival copy as the physical G: inode.
    return selected[0]


def build_actions(payload: dict) -> list[LinkAction]:
    actions: list[LinkAction] = []
    for group in payload["exact_duplicate_groups"]:
        sha = str(group.get("sha256") or "").casefold()
        if len(sha) != 64:
            continue
        size = int(group.get("size_bytes_each") or 0)
        all_paths = [str(p) for p in group.get("paths", [])]
        g_paths = [p for p in all_paths if drive(p) == "g:"]
        selected = [
            p for p in g_paths
            if any(under(p, prefix) for prefix in WAVE1_TARGET_PREFIXES)
        ]
        if not selected or len(g_paths) < 2:
            continue

        canonical = choose_canonical(g_paths, selected)
        if drive(canonical) != "g:":
            continue

        for target in selected:
            if norm(target) == norm(canonical):
                continue
            if any(under(target, prefix) for prefix in PROTECTED_TARGET_PREFIXES):
                raise RuntimeError(f"protected path selected as target: {target}")
            if not any(under(target, prefix) for prefix in WAVE1_TARGET_PREFIXES):
                raise RuntimeError(f"target escaped Wave 1 allowlist: {target}")
            if drive(target) != drive(canonical):
                raise RuntimeError(f"cross-volume hardlink requested: {target} -> {canonical}")
            actions.append(LinkAction(
                group_id=str(group.get("group_id") or ""),
                sha256=sha,
                size_bytes=size,
                canonical=canonical,
                target=target,
                expected_reclaim_bytes=size,
            ))
    return actions


def same_file(a: Path, b: Path) -> bool:
    try:
        return os.path.samefile(a, b)
    except (OSError, FileNotFoundError):
        return False


def verify_actions(actions: list[LinkAction]) -> tuple[bool, list[LinkAction]]:
    hash_cache: dict[str, str] = {}
    ok = True
    total = len(actions)

    for idx, action in enumerate(actions, 1):
        canonical = Path(action.canonical)
        target = Path(action.target)
        print(f"verify [{idx}/{total}] {gib(action.size_bytes)} GiB  {action.target}")

        if not canonical.is_file():
            action.status = "BLOCKED"
            action.detail = "CANONICAL_MISSING"
            ok = False
            continue
        if not target.is_file():
            action.status = "BLOCKED"
            action.detail = "TARGET_MISSING"
            ok = False
            continue
        if canonical.stat().st_size != action.size_bytes or target.stat().st_size != action.size_bytes:
            action.status = "BLOCKED"
            action.detail = "SIZE_CHANGED"
            ok = False
            continue

        if same_file(canonical, target):
            action.status = "ALREADY_LINKED"
            action.detail = "canonical_and_target_are_same_inode"
            continue

        canonical_key = str(canonical).casefold()
        actual_canonical = hash_cache.get(canonical_key)
        if actual_canonical is None:
            actual_canonical = sha256_file(canonical)
            hash_cache[canonical_key] = actual_canonical
        if actual_canonical.casefold() != action.sha256:
            action.status = "BLOCKED"
            action.detail = "CANONICAL_SHA_CHANGED"
            ok = False
            continue

        actual_target = sha256_file(target)
        if actual_target.casefold() != action.sha256:
            action.status = "BLOCKED"
            action.detail = "TARGET_SHA_CHANGED"
            ok = False
            continue

        action.status = "VERIFIED"
        action.detail = "exact_sha_and_same_volume_confirmed"

    return ok, actions


def apply_one(action: LinkAction, stamp: str) -> None:
    canonical = Path(action.canonical)
    target = Path(action.target)

    if same_file(canonical, target):
        action.status = "ALREADY_LINKED"
        action.detail = "no_change_needed"
        return

    backup = target.with_name(target.name + f".father-dedup-backup-{stamp}")
    if backup.exists():
        raise RuntimeError(f"backup collision: {backup}")

    # Transaction-like local replacement:
    # 1. rename the duplicate bytes to a temporary sibling;
    # 2. create an NTFS hardlink at the original path;
    # 3. prove the link resolves to the canonical inode;
    # 4. delete the temporary duplicate bytes.
    os.replace(target, backup)
    try:
        os.link(canonical, target)
        if not same_file(canonical, target):
            raise RuntimeError("hardlink verification failed: paths are not same inode")
        backup.unlink()
        action.status = "HARDLINKED"
        action.detail = "original_path_preserved_duplicate_allocation_released"
    except Exception:
        try:
            if target.exists():
                target.unlink()
        finally:
            if backup.exists():
                os.replace(backup, target)
        raise


def apply_actions(actions: list[LinkAction], confirm: str) -> list[LinkAction]:
    if confirm != CONFIRM_PHRASE:
        raise RuntimeError(
            f"apply refused: pass --confirm {CONFIRM_PHRASE} after reviewing verification output"
        )

    # Full preflight must be green before the first filesystem mutation.
    ok, actions = verify_actions(actions)
    blocked = [a for a in actions if a.status == "BLOCKED"]
    if not ok or blocked:
        raise RuntimeError(f"apply refused: {len(blocked)} action(s) blocked during preflight")

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    mutable = [a for a in actions if a.status == "VERIFIED"]
    total = len(mutable)
    for idx, action in enumerate(mutable, 1):
        print(f"hardlink [{idx}/{total}] {gib(action.size_bytes)} GiB  {action.target}")
        apply_one(action, stamp)
    return actions


def write_reports(actions: list[LinkAction], output: Path, mode: str, source_plan: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    expected = sum(a.expected_reclaim_bytes for a in actions)
    realized = sum(a.expected_reclaim_bytes for a in actions if a.status == "HARDLINKED")
    already = sum(a.expected_reclaim_bytes for a in actions if a.status == "ALREADY_LINKED")
    counters = {
        "actions": len(actions),
        "groups": len({a.group_id for a in actions}),
        "expected_reclaim_bytes": expected,
        "expected_reclaim_gib": gib(expected),
        "hardlinked_actions": sum(a.status == "HARDLINKED" for a in actions),
        "already_linked_actions": sum(a.status == "ALREADY_LINKED" for a in actions),
        "blocked_actions": sum(a.status == "BLOCKED" for a in actions),
        "verified_actions": sum(a.status == "VERIFIED" for a in actions),
        "realized_reclaim_estimate_bytes": realized,
        "realized_reclaim_estimate_gib": gib(realized),
        "already_consolidated_bytes": already,
    }
    payload = {
        "schema_version": SCHEMA,
        "generated_at": utc_now(),
        "mode": mode,
        "source_plan": str(source_plan),
        "strategy": "NTFS_HARDLINK_PRESERVE_PATH",
        "automatic_delete": False,
        "wave1_target_prefixes": list(WAVE1_TARGET_PREFIXES),
        "preferred_canonical_prefixes": list(PREFERRED_CANONICAL_PREFIXES),
        "counters": counters,
        "actions": [asdict(a) for a in actions],
    }
    (output / "wave1_hardlink_plan.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# FATHER Model Dedup — Wave 1 Hardlink Plan",
        "",
        "> Paths are preserved. Only exact SHA-256 duplicates on G: are eligible.",
        "> Default modes are read-only. Apply requires an explicit confirmation phrase.",
        "",
        f"- mode: **{mode}**",
        f"- exact groups in Wave 1: **{counters['groups']}**",
        f"- target paths: **{counters['actions']}**",
        f"- expected physical reclaim: **{counters['expected_reclaim_gib']} GiB**",
        f"- verified: **{counters['verified_actions']}**",
        f"- blocked: **{counters['blocked_actions']}**",
        f"- hardlinked in this run: **{counters['hardlinked_actions']}**",
        "",
        "| Group | GiB | Status | Canonical | Preserved target path |",
        "|---|---:|---|---|---|",
    ]
    for action in actions:
        lines.append(
            f"| {action.group_id} | {gib(action.size_bytes)} | {action.status} | "
            f"`{action.canonical}` | `{action.target}` |"
        )
    (output / "wave1_hardlink_plan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="FATHER Wave 1 exact-duplicate consolidation using NTFS hardlinks."
    )
    parser.add_argument(
        "--plan",
        default="reports/model_inventory/generated/model_dedup_plan.json",
        help="model_dedup_plan.json produced by the inventory scanner",
    )
    parser.add_argument(
        "--output",
        default="reports/model_inventory/consolidation_wave1",
        help="directory for Wave 1 reports",
    )
    parser.add_argument("--mode", choices=("plan", "verify", "apply"), default="plan")
    parser.add_argument("--confirm", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_plan = Path(args.plan)
    output = Path(args.output)
    print("FATHER Model Dedup Wave 1 — exact SHA duplicates, path-preserving hardlinks")
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

    expected = sum(a.expected_reclaim_bytes for a in actions)
    print(f"groups={len({a.group_id for a in actions})}")
    print(f"targets={len(actions)}")
    print(f"expected_reclaim_gib={gib(expected)}")

    if not actions:
        write_reports(actions, output, args.mode, source_plan)
        print("status=NO_WAVE1_ACTIONS")
        return 0

    try:
        if args.mode == "verify":
            ok, actions = verify_actions(actions)
            write_reports(actions, output, args.mode, source_plan)
            print(f"output={output.absolute()}")
            if not ok:
                print("status=BLOCKED")
                return 4
            print("status=WAVE1_VERIFIED")
            return 0
        if args.mode == "apply":
            actions = apply_actions(actions, args.confirm)
            write_reports(actions, output, args.mode, source_plan)
            print(f"output={output.absolute()}")
            print("status=WAVE1_HARDLINKS_APPLIED")
            return 0

        write_reports(actions, output, args.mode, source_plan)
        print(f"output={output.absolute()}")
        print("status=WAVE1_PLAN_READY")
        return 0
    except KeyboardInterrupt:
        write_reports(actions, output, args.mode + "_INTERRUPTED", source_plan)
        print("status=INTERRUPTED")
        print(f"output={output.absolute()}")
        return 130
    except Exception as exc:
        write_reports(actions, output, args.mode + "_FAILED", source_plan)
        print("status=BLOCKED")
        print(f"reason={type(exc).__name__}: {exc}")
        print(f"output={output.absolute()}")
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
