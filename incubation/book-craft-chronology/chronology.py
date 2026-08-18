from __future__ import annotations

import argparse
import copy
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "chronology.json"
REPORT = ROOT / "reports" / "chronology-diagnostics.json"


class ChronologyError(ValueError):
    pass


def issue(code: str, event_id: str | None, relation: str, expected, actual) -> dict:
    return {
        "code": code,
        "event": event_id,
        "relation": relation,
        "expected": expected,
        "actual": actual,
    }


def load_data() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


def validate_min(data: dict) -> None:
    events = data.get("events", [])
    if len(events) != 3:
        raise ChronologyError("exactly three demonstration events are required")
    ids = [event["id"] for event in events]
    if len(ids) != len(set(ids)):
        raise ChronologyError("event IDs must be unique")
    if data.get("provenance", {}).get("automatic_extraction") is not False:
        raise ChronologyError("manual seed must not claim automatic extraction")
    for event in events:
        if not all(key in event for key in ("sequence", "time", "location", "actors")):
            raise ChronologyError(f"incomplete event: {event.get('id')}")


def diagnose(data: dict) -> list[dict]:
    validate_min(data)
    events = sorted(data["events"], key=lambda event: event["sequence"])
    problems: list[dict] = []
    if [event["sequence"] for event in events] != [1, 2, 3]:
        broken = next(
            (event for expected, event in enumerate(data["events"], 1) if event["sequence"] != expected),
            data["events"][0],
        )
        expected = data["events"].index(broken) + 1
        problems.append(issue("CHR-ORDER-001", broken["id"], "event.sequence", expected, broken["sequence"]))
    if [event["time"] for event in events] != sorted(event["time"] for event in events):
        problems.append(issue("CHR-TIME-001", None, "event_time", "monotonic", [event["time"] for event in events]))

    positions: dict[str, str] = {}
    owners: dict[str, str] = {}
    informed: set[tuple[str, str]] = set()
    for event in events:
        movement = event.get("movement")
        if movement:
            actor = movement["actor"]
            previous = positions.get(actor)
            if movement["from"] != previous:
                problems.append(issue("CHR-MOVE-001", event["id"], "movement.from", previous, movement["from"]))
            if movement["to"] != event["location"]:
                problems.append(issue("CHR-MOVE-002", event["id"], "movement.to", event["location"], movement["to"]))
            positions[actor] = movement["to"]
        for actor in event["actors"]:
            if actor in positions and positions[actor] != event["location"]:
                problems.append(issue("CHR-LOC-001", event["id"], f"actor_location.{actor}", event["location"], positions[actor]))

        transfer = event.get("ownership")
        if transfer:
            item = transfer["item"]
            if owners.get(item) != transfer["from"]:
                problems.append(issue("CHR-OWNER-001", event["id"], f"ownership.from.{item}", owners.get(item), transfer["from"]))
            owners[item] = transfer["to"]

        info = event.get("information")
        if info:
            informed.add((info["learned_by"], info["fact"]))

    if owners.get("ITEM-BRASS-KEY") != "CHAR-B":
        problems.append(issue("CHR-OWNER-002", "EVT-003", "ownership.final.ITEM-BRASS-KEY", "CHAR-B", owners.get("ITEM-BRASS-KEY")))
    if ("CHAR-A", "INFO-MEETING-PLACE") not in informed or ("CHAR-B", "INFO-MEETING-PLACE") not in informed:
        problems.append(issue("CHR-INFO-001", "EVT-003", "information.acquisition.INFO-MEETING-PLACE", ["CHAR-A", "CHAR-B"], sorted(actor for actor, fact in informed if fact == "INFO-MEETING-PLACE")))
    return problems


def validate_med(data: dict) -> None:
    problems = diagnose(data)
    if problems:
        raise ChronologyError(json.dumps(problems[0], ensure_ascii=False, sort_keys=True))


def validate_max(data: dict) -> None:
    validate_med(data)
    mutations = []
    wrong_order = copy.deepcopy(data)
    wrong_order["events"][1]["sequence"] = 3
    mutations.append(wrong_order)
    wrong_move = copy.deepcopy(data)
    wrong_move["events"][1]["movement"]["from"] = "LOC-IMPOSSIBLE"
    mutations.append(wrong_move)
    wrong_owner = copy.deepcopy(data)
    wrong_owner["events"][2]["ownership"]["from"] = "CHAR-B"
    mutations.append(wrong_owner)
    missing_info = copy.deepcopy(data)
    missing_info["events"][2]["information"] = None
    mutations.append(missing_info)
    for index, mutation in enumerate(mutations, 1):
        try:
            validate_med(mutation)
        except ChronologyError:
            continue
        raise ChronologyError(f"negative mutation {index} was not rejected")


def query_event(data: dict, event_id: str) -> str:
    validate_med(data)
    event = next((event for event in data["events"] if event["id"] == event_id), None)
    if not event:
        raise ChronologyError(f"unknown event: {event_id}")
    owner = event.get("ownership")
    info = event.get("information")
    return json.dumps({
        "event": event["id"], "time": event["time"], "where": event["location"],
        "who": event["actors"], "ownership": owner, "information": info,
        "source": "manual_demo_seed"
    }, ensure_ascii=False, indent=2)


def diagnostic_report(data: dict) -> dict:
    problems = diagnose(data)
    canonical_source = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "schema_version": "book-craft-chronology-diagnostics/1.0",
        "world_id": data["world_id"],
        "source": {
            "mode": data["provenance"]["mode"],
            "automatic_extraction": data["provenance"]["automatic_extraction"],
            "sha256": hashlib.sha256(canonical_source).hexdigest(),
        },
        "event_count": len(data["events"]),
        "event_ids": [event["id"] for event in data["events"]],
        "checks": ["event_order", "event_time", "location_movement", "ownership", "information_acquisition"],
        "status": "CONFLICT" if problems else "GREEN",
        "issue_count": len(problems),
        "issues": problems,
    }


def write_diagnostic_report(data: dict) -> Path:
    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(json.dumps(diagnostic_report(data), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return REPORT


def verify_diagnostic_report(data: dict, report_path: Path = REPORT) -> Path:
    expected = diagnostic_report(data)
    try:
        actual = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ChronologyError(json.dumps(issue(
            "CHR-REPORT-001", None, "report.read", "valid JSON report", str(error)
        ), ensure_ascii=False, sort_keys=True)) from error

    comparisons = (
        ("CHR-REPORT-002", "report.schema_version", expected["schema_version"], actual.get("schema_version")),
        ("CHR-REPORT-003", "report.source", expected["source"], actual.get("source")),
        ("CHR-REPORT-004", "report.events", {
            "event_count": expected["event_count"], "event_ids": expected["event_ids"]
        }, {
            "event_count": actual.get("event_count"), "event_ids": actual.get("event_ids")
        }),
    )
    for code, relation, expected_value, actual_value in comparisons:
        if actual_value != expected_value:
            raise ChronologyError(json.dumps(issue(
                code, None, relation, expected_value, actual_value
            ), ensure_ascii=False, sort_keys=True))
    if actual != expected:
        raise ChronologyError(json.dumps(issue(
            "CHR-REPORT-005", None, "report.content", expected, actual
        ), ensure_ascii=False, sort_keys=True))
    return report_path


def mutate_for_diagnostic(data: dict, mutation: str) -> dict:
    mutated = copy.deepcopy(data)
    if mutation == "order":
        mutated["events"][1]["sequence"] = 3
    elif mutation == "movement":
        mutated["events"][1]["movement"]["from"] = "LOC-IMPOSSIBLE"
    elif mutation == "ownership":
        mutated["events"][2]["ownership"]["from"] = "CHAR-B"
    elif mutation == "information":
        mutated["events"][2]["information"] = None
    return mutated


def build_archive() -> Path:
    data = load_data()
    validate_max(data)
    write_diagnostic_report(data)
    verify_diagnostic_report(data)
    output = ROOT / "build" / "book-craft-chronology-clean.zip"
    output.parent.mkdir(exist_ok=True)
    allowed = ["README.md", "MATURITY_ROADMAP.md", "chronology.py", "data/chronology.json", "reports/chronology-diagnostics.json", "tests/test_chronology.py"]
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in allowed:
            archive.write(ROOT / relative, relative)
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    check.add_argument("--level", choices=("min", "med", "max", "all"), default="all")
    query = sub.add_parser("query")
    query.add_argument("--event", required=True)
    diagnostic = sub.add_parser("diagnose")
    diagnostic.add_argument("--mutation", choices=("order", "movement", "ownership", "information"))
    sub.add_parser("report")
    verify = sub.add_parser("verify-report")
    verify.add_argument("--path", type=Path, default=REPORT)
    sub.add_parser("build")
    args = parser.parse_args()
    data = load_data()
    if args.command == "check":
        checks = {"min": validate_min, "med": validate_med, "max": validate_max}
        selected = checks.values() if args.level == "all" else [checks[args.level]]
        for check_fn in selected:
            check_fn(data)
        print(f"GREEN {args.level.upper()}")
    elif args.command == "query":
        print(query_event(data, args.event))
    elif args.command == "diagnose":
        target = mutate_for_diagnostic(data, args.mutation) if args.mutation else data
        problems = diagnose(target)
        print(json.dumps({"status": "CONFLICT" if problems else "GREEN", "issues": problems}, ensure_ascii=False, indent=2))
    elif args.command == "report":
        print(write_diagnostic_report(data))
    elif args.command == "verify-report":
        print(f"GREEN REPORT VERIFIED {verify_diagnostic_report(data, args.path)}")
    else:
        print(build_archive())


if __name__ == "__main__":
    main()
