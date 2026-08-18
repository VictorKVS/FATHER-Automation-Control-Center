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
DRY_RUN_REPORT = ROOT / "reports" / "repair-dry-run.json"
MANIFEST = ROOT / "reports" / "archive-manifest.json"
ARCHIVE = ROOT / "build" / "book-craft-chronology-clean.zip"
RELEASE = ROOT / "reports" / "archive-release.json"
ZIP_DATE_TIME = (1980, 1, 1, 0, 0, 0)
ZIP_MODE = 0o100644
ARCHIVE_PAYLOAD = (
    "README.md",
    "MATURITY_ROADMAP.md",
    "chronology.py",
    "data/chronology.json",
    "reports/chronology-diagnostics.json",
    "reports/repair-dry-run.json",
    "tests/test_chronology.py",
)


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


def archive_manifest() -> dict:
    files = []
    for relative in ARCHIVE_PAYLOAD:
        content = (ROOT / relative).read_bytes()
        files.append({
            "path": relative,
            "bytes": len(content),
            "sha256": hashlib.sha256(content).hexdigest(),
        })
    return {
        "schema_version": "book-craft-clean-archive-manifest/1.0",
        "algorithm": "sha256",
        "payload_file_count": len(files),
        "files": files,
    }


def write_archive_manifest() -> Path:
    MANIFEST.parent.mkdir(exist_ok=True)
    MANIFEST.write_text(
        json.dumps(archive_manifest(), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return MANIFEST


def verify_archive_manifest(manifest_path: Path = MANIFEST) -> Path:
    expected = archive_manifest()
    try:
        actual = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ChronologyError(json.dumps(issue(
            "CHR-MANIFEST-001", None, "manifest.read", "valid JSON manifest", str(error)
        ), ensure_ascii=False, sort_keys=True)) from error
    if actual != expected:
        raise ChronologyError(json.dumps(issue(
            "CHR-MANIFEST-002", None, "manifest.content", expected, actual
        ), ensure_ascii=False, sort_keys=True))
    return manifest_path


def verify_archive(archive_path: Path = ARCHIVE) -> Path:
    expected_members = [*ARCHIVE_PAYLOAD, "reports/archive-manifest.json"]
    try:
        with zipfile.ZipFile(archive_path) as archive:
            members = archive.namelist()
            if len(members) != len(expected_members) or set(members) != set(expected_members):
                raise ChronologyError(json.dumps(issue(
                    "CHR-ARCHIVE-002", None, "archive.members",
                    sorted(expected_members), sorted(members),
                ), ensure_ascii=False, sort_keys=True))

            manifest = json.loads(archive.read("reports/archive-manifest.json").decode("utf-8"))
            entries = manifest.get("files") if isinstance(manifest, dict) else None
            if not isinstance(entries, list) or not all(isinstance(entry, dict) for entry in entries):
                raise ChronologyError(json.dumps(issue(
                    "CHR-ARCHIVE-003", None, "archive.manifest", "valid file entries", entries
                ), ensure_ascii=False, sort_keys=True))

            expected_descriptor = {
                "schema_version": "book-craft-clean-archive-manifest/1.0",
                "algorithm": "sha256",
                "payload_file_count": len(ARCHIVE_PAYLOAD),
                "paths": list(ARCHIVE_PAYLOAD),
            }
            actual_descriptor = {
                "schema_version": manifest.get("schema_version"),
                "algorithm": manifest.get("algorithm"),
                "payload_file_count": manifest.get("payload_file_count"),
                "paths": [entry.get("path") for entry in entries],
            }
            if actual_descriptor != expected_descriptor:
                raise ChronologyError(json.dumps(issue(
                    "CHR-ARCHIVE-003", None, "archive.manifest",
                    expected_descriptor, actual_descriptor,
                ), ensure_ascii=False, sort_keys=True))

            for entry in entries:
                content = archive.read(entry["path"])
                expected_file = {
                    "path": entry["path"],
                    "bytes": entry.get("bytes"),
                    "sha256": entry.get("sha256"),
                }
                actual_file = {
                    "path": entry["path"],
                    "bytes": len(content),
                    "sha256": hashlib.sha256(content).hexdigest(),
                }
                if actual_file != expected_file:
                    raise ChronologyError(json.dumps(issue(
                        "CHR-ARCHIVE-004", None, f"archive.payload.{entry['path']}",
                        expected_file, actual_file,
                    ), ensure_ascii=False, sort_keys=True))
    except ChronologyError:
        raise
    except (OSError, KeyError, UnicodeDecodeError, json.JSONDecodeError, zipfile.BadZipFile) as error:
        raise ChronologyError(json.dumps(issue(
            "CHR-ARCHIVE-001", None, "archive.read", "valid clean ZIP", str(error)
        ), ensure_ascii=False, sort_keys=True)) from error
    return archive_path


def release_checksum(archive_path: Path = ARCHIVE) -> dict:
    verify_archive(archive_path)
    content = archive_path.read_bytes()
    return {
        "schema_version": "book-craft-chronology-release/1.0",
        "artifact": ARCHIVE.name,
        "algorithm": "sha256",
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "member_count": len(ARCHIVE_PAYLOAD) + 1,
    }


def write_release_checksum(archive_path: Path = ARCHIVE) -> Path:
    RELEASE.parent.mkdir(exist_ok=True)
    RELEASE.write_text(
        json.dumps(release_checksum(archive_path), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return RELEASE


def verify_release_checksum(
    release_path: Path = RELEASE,
    archive_path: Path = ARCHIVE,
) -> Path:
    expected = release_checksum(archive_path)
    try:
        actual = json.loads(release_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ChronologyError(json.dumps(issue(
            "CHR-RELEASE-001", None, "release.read", "valid JSON release checksum", str(error)
        ), ensure_ascii=False, sort_keys=True)) from error
    if actual != expected:
        raise ChronologyError(json.dumps(issue(
            "CHR-RELEASE-002", None, "release.content", expected, actual
        ), ensure_ascii=False, sort_keys=True))
    return archive_path


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


def repair_preview(data: dict, mutation: str) -> dict:
    if mutation != "movement":
        raise ChronologyError("M2.1 supports movement preview only")
    target = mutate_for_diagnostic(data, mutation)
    problems = diagnose(target)
    conflict = problems[0]
    return {
        "schema_version": "book-craft-chronology-repair-preview/1.0",
        "status": "PREVIEW_ONLY",
        "source": diagnostic_report(data)["source"],
        "fixture": mutation,
        "conflict": conflict,
        "proposal": {
            "event": conflict["event"],
            "path": conflict["relation"],
            "operation": "replace",
            "from": conflict["actual"],
            "to": conflict["expected"],
        },
        "automatic_apply": False,
        "source_data_written": False,
        "required_validation": ["MIN", "MED", "MAX"],
    }


def review_repair(data: dict, mutation: str, decision: str) -> dict:
    if decision not in ("approve", "reject"):
        raise ChronologyError("M2.2 decision must be approve or reject")
    preview = repair_preview(data, mutation)
    canonical_proposal = json.dumps(
        preview["proposal"], ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return {
        "schema_version": "book-craft-chronology-repair-review/1.0",
        "status": "REVIEW_APPROVED" if decision == "approve" else "REVIEW_REJECTED",
        "source": preview["source"],
        "fixture": mutation,
        "decision": decision,
        "decision_origin": "explicit_cli_argument",
        "reviewer_identity_verified": False,
        "proposal_sha256": hashlib.sha256(canonical_proposal).hexdigest(),
        "proposal": preview["proposal"],
        "automatic_apply": False,
        "source_data_written": False,
        "required_validation": preview["required_validation"],
    }


def validation_matrix(data: dict) -> dict:
    results = {}
    for name, validator in (("MIN", validate_min), ("MED", validate_med), ("MAX", validate_max)):
        try:
            validator(data)
        except ChronologyError as error:
            results[name] = {"status": "RED", "error": str(error)}
        else:
            results[name] = {"status": "GREEN"}
    return results


def dry_run_repair(data: dict, mutation: str, decision: str) -> dict:
    source_snapshot = copy.deepcopy(data)
    review = review_repair(data, mutation, decision)
    target = mutate_for_diagnostic(data, mutation)
    before = {
        "issues": diagnose(target),
        "validation": validation_matrix(target),
    }
    result = {
        "schema_version": "book-craft-chronology-repair-dry-run/1.0",
        "status": "DRY_RUN_SKIPPED" if decision == "reject" else "DRY_RUN_PENDING",
        "source": review["source"],
        "fixture": mutation,
        "review": {
            "decision": review["decision"],
            "proposal_sha256": review["proposal_sha256"],
            "reviewer_identity_verified": review["reviewer_identity_verified"],
        },
        "proposal": review["proposal"],
        "before": before,
        "after": None,
        "transient_copy_applied": False,
        "automatic_apply": False,
        "canonical_data_written": False,
    }
    if decision == "approve":
        proposal = review["proposal"]
        event = next(event for event in target["events"] if event["id"] == proposal["event"])
        if event["movement"]["from"] != proposal["from"]:
            raise ChronologyError("M2.3 proposal no longer matches the transient fixture")
        event["movement"]["from"] = proposal["to"]
        after = {
            "issues": diagnose(target),
            "validation": validation_matrix(target),
        }
        result["after"] = after
        result["transient_copy_applied"] = True
        result["status"] = "DRY_RUN_GREEN" if (
            not after["issues"]
            and all(gate["status"] == "GREEN" for gate in after["validation"].values())
        ) else "DRY_RUN_RED"
    if data != source_snapshot:
        raise ChronologyError("M2.3 dry-run changed canonical source data")
    return result


def write_repair_dry_run_report(data: dict) -> Path:
    DRY_RUN_REPORT.parent.mkdir(exist_ok=True)
    DRY_RUN_REPORT.write_text(
        json.dumps(
            dry_run_repair(data, "movement", "approve"),
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )
    return DRY_RUN_REPORT


def build_archive() -> Path:
    data = load_data()
    validate_max(data)
    write_diagnostic_report(data)
    verify_diagnostic_report(data)
    write_repair_dry_run_report(data)
    write_archive_manifest()
    verify_archive_manifest()
    output = ARCHIVE
    output.parent.mkdir(exist_ok=True)
    allowed = (*ARCHIVE_PAYLOAD, "reports/archive-manifest.json")
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in allowed:
            member = zipfile.ZipInfo(relative, date_time=ZIP_DATE_TIME)
            member.compress_type = zipfile.ZIP_DEFLATED
            member.create_system = 3
            member.external_attr = ZIP_MODE << 16
            archive.writestr(
                member,
                (ROOT / relative).read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
    verify_archive(output)
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
    repair = sub.add_parser("plan-repair")
    repair.add_argument("--mutation", choices=("movement",), required=True)
    review = sub.add_parser("review-repair")
    review.add_argument("--mutation", choices=("movement",), required=True)
    review.add_argument("--decision", choices=("approve", "reject"), required=True)
    dry_run = sub.add_parser("dry-run-repair")
    dry_run.add_argument("--mutation", choices=("movement",), required=True)
    dry_run.add_argument("--decision", choices=("approve", "reject"), required=True)
    sub.add_parser("dry-run-report")
    sub.add_parser("report")
    verify = sub.add_parser("verify-report")
    verify.add_argument("--path", type=Path, default=REPORT)
    sub.add_parser("manifest")
    verify_manifest = sub.add_parser("verify-manifest")
    verify_manifest.add_argument("--path", type=Path, default=MANIFEST)
    verify_zip = sub.add_parser("verify-archive")
    verify_zip.add_argument("--path", type=Path, default=ARCHIVE)
    sub.add_parser("release")
    verify_release = sub.add_parser("verify-release")
    verify_release.add_argument("--release-path", type=Path, default=RELEASE)
    verify_release.add_argument("--archive-path", type=Path, default=ARCHIVE)
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
    elif args.command == "plan-repair":
        print(json.dumps(repair_preview(data, args.mutation), ensure_ascii=False, indent=2, sort_keys=True))
    elif args.command == "review-repair":
        print(json.dumps(review_repair(data, args.mutation, args.decision), ensure_ascii=False, indent=2, sort_keys=True))
    elif args.command == "dry-run-repair":
        print(json.dumps(dry_run_repair(data, args.mutation, args.decision), ensure_ascii=False, indent=2, sort_keys=True))
    elif args.command == "dry-run-report":
        print(write_repair_dry_run_report(data))
    elif args.command == "report":
        print(write_diagnostic_report(data))
    elif args.command == "verify-report":
        print(f"GREEN REPORT VERIFIED {verify_diagnostic_report(data, args.path)}")
    elif args.command == "manifest":
        print(write_archive_manifest())
    elif args.command == "verify-manifest":
        print(f"GREEN MANIFEST VERIFIED {verify_archive_manifest(args.path)}")
    elif args.command == "verify-archive":
        print(f"GREEN ARCHIVE VERIFIED {verify_archive(args.path)}")
    elif args.command == "release":
        print(write_release_checksum())
    elif args.command == "verify-release":
        print(f"GREEN RELEASE VERIFIED {verify_release_checksum(args.release_path, args.archive_path)}")
    else:
        print(build_archive())


if __name__ == "__main__":
    main()
