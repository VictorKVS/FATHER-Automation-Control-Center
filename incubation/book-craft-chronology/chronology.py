from __future__ import annotations

import argparse
import copy
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "chronology.json"


class ChronologyError(ValueError):
    pass


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


def validate_med(data: dict) -> None:
    validate_min(data)
    events = sorted(data["events"], key=lambda event: event["sequence"])
    if [event["sequence"] for event in events] != [1, 2, 3]:
        raise ChronologyError("sequence must be contiguous: 1, 2, 3")
    if [event["time"] for event in events] != sorted(event["time"] for event in events):
        raise ChronologyError("event time must be monotonic")

    positions: dict[str, str] = {}
    owners: dict[str, str] = {}
    informed: set[tuple[str, str]] = set()
    for event in events:
        movement = event.get("movement")
        if movement:
            actor = movement["actor"]
            previous = positions.get(actor)
            if movement["from"] != previous:
                raise ChronologyError(f"movement discontinuity at {event['id']}")
            if movement["to"] != event["location"]:
                raise ChronologyError(f"movement destination mismatch at {event['id']}")
            positions[actor] = movement["to"]
        for actor in event["actors"]:
            if actor in positions and positions[actor] != event["location"]:
                raise ChronologyError(f"actor location conflict at {event['id']}")

        transfer = event.get("ownership")
        if transfer:
            item = transfer["item"]
            if owners.get(item) != transfer["from"]:
                raise ChronologyError(f"ownership discontinuity at {event['id']}")
            owners[item] = transfer["to"]

        info = event.get("information")
        if info:
            informed.add((info["learned_by"], info["fact"]))

    if owners.get("ITEM-BRASS-KEY") != "CHAR-B":
        raise ChronologyError("final ownership is not demonstrated")
    if ("CHAR-A", "INFO-MEETING-PLACE") not in informed or ("CHAR-B", "INFO-MEETING-PLACE") not in informed:
        raise ChronologyError("information acquisition chain is incomplete")


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


def build_archive() -> Path:
    validate_max(load_data())
    output = ROOT / "build" / "book-craft-chronology-clean.zip"
    output.parent.mkdir(exist_ok=True)
    allowed = ["README.md", "MATURITY_ROADMAP.md", "chronology.py", "data/chronology.json", "tests/test_chronology.py"]
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
    else:
        print(build_archive())


if __name__ == "__main__":
    main()
