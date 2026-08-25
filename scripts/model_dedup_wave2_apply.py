from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

try:
    from scripts.model_dedup_wave1 import apply_one, gib, verify_actions
    from scripts.model_dedup_wave2 import build_actions, load_dedup_plan
except ModuleNotFoundError:  # direct execution: python scripts\model_dedup_wave2_apply.py
    from model_dedup_wave1 import apply_one, gib, verify_actions
    from model_dedup_wave2 import build_actions, load_dedup_plan


SCHEMA = "father-model-hardlink-wave2-apply.v0.1"
CONFIRM_PHRASE = "APPLY_WAVE2_HARDLINKS"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def free_bytes_g() -> int:
    return int(shutil.disk_usage("G:\\").free)


def write_report(
    actions,
    output: Path,
    source_plan: Path,
    status: str,
    free_before: int | None,
    free_after: int | None,
) -> None:
    output.mkdir(parents=True, exist_ok=True)
    expected = sum(action.expected_reclaim_bytes for action in actions)
    delta = None if free_before is None or free_after is None else free_after - free_before
    counters = {
        "actions": len(actions),
        "groups": len({action.group_id for action in actions}),
        "expected_reclaim_bytes": expected,
        "expected_reclaim_gib": gib(expected),
        "hardlinked_actions": sum(action.status == "HARDLINKED" for action in actions),
        "already_linked_actions": sum(action.status == "ALREADY_LINKED" for action in actions),
        "blocked_actions": sum(action.status == "BLOCKED" for action in actions),
        "verified_actions": sum(action.status == "VERIFIED" for action in actions),
        "free_before_bytes": free_before,
        "free_after_bytes": free_after,
        "observed_free_space_delta_bytes": delta,
        "observed_free_space_delta_gib": None if delta is None else gib(delta),
    }
    payload = {
        "schema_version": SCHEMA,
        "generated_at": utc_now(),
        "status": status,
        "source_plan": str(source_plan),
        "strategy": "NTFS_HARDLINK_PRESERVE_PATH",
        "confirmation_required": CONFIRM_PHRASE,
        "counters": counters,
        "actions": [asdict(action) for action in actions],
    }
    (output / "wave2_apply_report.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# FATHER Model Dedup — Wave 2A Apply Report",
        "",
        f"- status: **{status}**",
        f"- groups: **{counters['groups']}**",
        f"- target paths: **{counters['actions']}**",
        f"- expected reclaim: **{counters['expected_reclaim_gib']} GiB**",
        f"- hardlinked this run: **{counters['hardlinked_actions']}**",
        f"- already linked: **{counters['already_linked_actions']}**",
        f"- blocked: **{counters['blocked_actions']}**",
        f"- observed G: free-space delta: **{counters['observed_free_space_delta_gib']} GiB**",
        "",
        "| Group | GiB | Status | Canonical survivor | Preserved target path |",
        "|---|---:|---|---|---|",
    ]
    for action in actions:
        lines.append(
            f"| {action.group_id} | {gib(action.size_bytes)} | {action.status} | "
            f"`{action.canonical}` | `{action.target}` |"
        )
    (output / "wave2_apply_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply verified Wave 2A image-model dedup using path-preserving NTFS hardlinks."
    )
    parser.add_argument(
        "--plan",
        default="reports/model_inventory/generated/model_dedup_plan.json",
    )
    parser.add_argument(
        "--output",
        default="reports/model_inventory/consolidation_wave2",
    )
    parser.add_argument("--confirm", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_plan = Path(args.plan)
    output = Path(args.output)

    print("FATHER Model Dedup Wave 2A APPLY — exact SHA duplicates only")
    print(f"source_plan={source_plan.absolute()}")

    if args.confirm != CONFIRM_PHRASE:
        print("status=BLOCKED")
        print(f"reason=CONFIRMATION_REQUIRED:{CONFIRM_PHRASE}")
        return 2
    if not source_plan.is_file():
        print("status=BLOCKED")
        print("reason=DEDUP_PLAN_NOT_FOUND")
        return 3

    try:
        payload = load_dedup_plan(source_plan)
        actions = build_actions(payload)
    except Exception as exc:
        print("status=BLOCKED")
        print(f"reason={type(exc).__name__}: {exc}")
        return 4

    print(f"groups={len({action.group_id for action in actions})}")
    print(f"targets={len(actions)}")
    print(f"expected_reclaim_gib={gib(sum(action.expected_reclaim_bytes for action in actions))}")

    if not actions:
        write_report(actions, output, source_plan, "NO_WAVE2_ACTIONS", None, None)
        print("status=NO_WAVE2_ACTIONS")
        return 0

    print("preflight=VERIFY_ALL_SHA256_BEFORE_FIRST_MUTATION")
    try:
        ok, actions = verify_actions(actions)
    except KeyboardInterrupt:
        write_report(actions, output, source_plan, "INTERRUPTED_DURING_PREFLIGHT", None, None)
        print("status=INTERRUPTED")
        return 130
    except Exception as exc:
        write_report(actions, output, source_plan, "BLOCKED_PREFLIGHT_EXCEPTION", None, None)
        print("status=BLOCKED")
        print(f"reason={type(exc).__name__}: {exc}")
        return 5

    blocked = [action for action in actions if action.status == "BLOCKED"]
    if not ok or blocked:
        write_report(actions, output, source_plan, "BLOCKED_PREFLIGHT", None, None)
        print("status=BLOCKED")
        print(f"blocked={len(blocked)}")
        return 6

    mutable = [action for action in actions if action.status == "VERIFIED"]
    already = [action for action in actions if action.status == "ALREADY_LINKED"]
    print(f"verified={len(mutable)}")
    print(f"already_linked={len(already)}")

    free_before = free_bytes_g()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    try:
        total = len(mutable)
        for index, action in enumerate(mutable, 1):
            print(f"hardlink [{index}/{total}] {gib(action.size_bytes)} GiB  {action.target}")
            apply_one(action, stamp)
    except KeyboardInterrupt:
        free_after = free_bytes_g()
        write_report(actions, output, source_plan, "INTERRUPTED_PARTIAL", free_before, free_after)
        print("status=INTERRUPTED_PARTIAL")
        print(f"output={output.absolute()}")
        return 130
    except Exception as exc:
        free_after = free_bytes_g()
        write_report(actions, output, source_plan, "BLOCKED_PARTIAL", free_before, free_after)
        print("status=BLOCKED_PARTIAL")
        print(f"reason={type(exc).__name__}: {exc}")
        print(f"output={output.absolute()}")
        return 7

    free_after = free_bytes_g()
    write_report(actions, output, source_plan, "WAVE2_HARDLINKS_APPLIED", free_before, free_after)
    print(f"free_before_gib={gib(free_before)}")
    print(f"free_after_gib={gib(free_after)}")
    print(f"observed_reclaim_gib={gib(free_after - free_before)}")
    print(f"output={output.absolute()}")
    print("status=WAVE2_HARDLINKS_APPLIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
