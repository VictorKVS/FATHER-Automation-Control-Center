import copy
import hashlib
import json
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from chronology import ARCHIVE_PAYLOAD, MANIFEST, RELEASE, REPORT, ZIP_DATE_TIME, ZIP_MODE, ChronologyError, archive_manifest, build_archive, diagnostic_report, diagnose, load_data, mutate_for_diagnostic, query_event, release_checksum, validate_max, validate_med, validate_min, verify_archive, verify_archive_manifest, verify_diagnostic_report, verify_release_checksum, write_archive_manifest, write_diagnostic_report, write_release_checksum


class ChronologyTests(unittest.TestCase):
    def setUp(self):
        self.data = load_data()

    def test_min(self):
        validate_min(self.data)
        self.assertEqual(3, len(self.data["events"]))

    def test_med(self):
        validate_med(self.data)

    def test_max_negative_mutations(self):
        validate_max(self.data)

    def test_interactive_query(self):
        result = json.loads(query_event(self.data, "EVT-003"))
        self.assertEqual("00:26", result["time"])
        self.assertEqual("CHAR-B", result["ownership"]["to"])
        self.assertEqual("manual_demo_seed", result["source"])

    def test_rejects_fourth_event(self):
        invalid = copy.deepcopy(self.data)
        invalid["events"].append(copy.deepcopy(invalid["events"][-1]))
        invalid["events"][-1]["id"] = "EVT-004"
        with self.assertRaises(ChronologyError):
            validate_min(invalid)

    def test_diagnostic_names_movement_event(self):
        problems = diagnose(mutate_for_diagnostic(self.data, "movement"))
        self.assertEqual("CHR-MOVE-001", problems[0]["code"])
        self.assertEqual("EVT-002", problems[0]["event"])
        self.assertEqual("LOC-NEVSKY-ENTRY", problems[0]["expected"])

    def test_diagnostic_names_order_event(self):
        problems = diagnose(mutate_for_diagnostic(self.data, "order"))
        self.assertEqual("CHR-ORDER-001", problems[0]["code"])
        self.assertEqual("EVT-002", problems[0]["event"])
        self.assertEqual(2, problems[0]["expected"])
        self.assertEqual(3, problems[0]["actual"])

    def test_diagnostic_names_ownership_event(self):
        problems = diagnose(mutate_for_diagnostic(self.data, "ownership"))
        self.assertEqual("CHR-OWNER-001", problems[0]["code"])
        self.assertEqual("EVT-003", problems[0]["event"])

    def test_diagnostic_names_information_event(self):
        problems = diagnose(mutate_for_diagnostic(self.data, "information"))
        self.assertEqual("CHR-INFO-001", problems[0]["code"])
        self.assertEqual("EVT-003", problems[0]["event"])

    def test_clean_seed_has_no_diagnostics(self):
        self.assertEqual([], diagnose(self.data))

    def test_diagnostic_report_is_deterministic(self):
        first = diagnostic_report(self.data)
        second = diagnostic_report(copy.deepcopy(self.data))
        self.assertEqual(first, second)
        self.assertEqual("GREEN", first["status"])
        self.assertEqual(3, first["event_count"])
        self.assertFalse(first["source"]["automatic_extraction"])

    def test_committed_report_matches_generator(self):
        write_diagnostic_report(self.data)
        committed = json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(diagnostic_report(self.data), committed)

    def test_verifies_current_report(self):
        write_diagnostic_report(self.data)
        self.assertEqual(REPORT, verify_diagnostic_report(self.data))

    def test_rejects_stale_report_digest(self):
        report = diagnostic_report(self.data)
        report["source"]["sha256"] = "0" * 64
        path = ROOT / "build" / "stale-report.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(report), encoding="utf-8")
        with self.assertRaisesRegex(ChronologyError, "CHR-REPORT-003"):
            verify_diagnostic_report(self.data, path)

    def test_rejects_tampered_report_events(self):
        report = diagnostic_report(self.data)
        report["event_ids"][-1] = "EVT-004"
        path = ROOT / "build" / "tampered-report.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(report), encoding="utf-8")
        with self.assertRaisesRegex(ChronologyError, "CHR-REPORT-004"):
            verify_diagnostic_report(self.data, path)

    def test_rejects_malformed_report(self):
        path = ROOT / "build" / "malformed-report.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text("not-json", encoding="utf-8")
        with self.assertRaisesRegex(ChronologyError, "CHR-REPORT-001"):
            verify_diagnostic_report(self.data, path)

    def test_archive_manifest_is_deterministic(self):
        self.assertEqual(archive_manifest(), archive_manifest())
        self.assertEqual(6, archive_manifest()["payload_file_count"])
        self.assertEqual(list(ARCHIVE_PAYLOAD), [entry["path"] for entry in archive_manifest()["files"]])

    def test_verifies_current_archive_manifest(self):
        write_diagnostic_report(self.data)
        write_archive_manifest()
        self.assertEqual(MANIFEST, verify_archive_manifest())

    def test_rejects_tampered_archive_manifest(self):
        manifest = archive_manifest()
        manifest["files"][0]["sha256"] = "0" * 64
        path = ROOT / "build" / "tampered-manifest.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaisesRegex(ChronologyError, "CHR-MANIFEST-002"):
            verify_archive_manifest(path)

    def test_verifies_built_archive_contents(self):
        archive = build_archive()
        self.assertEqual(archive, verify_archive(archive))

    def test_build_is_byte_reproducible(self):
        first = build_archive().read_bytes()
        second = build_archive().read_bytes()
        self.assertEqual(first, second)
        self.assertEqual(hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest())

    def test_build_has_canonical_zip_metadata(self):
        archive = build_archive()
        with zipfile.ZipFile(archive) as built:
            for member in built.infolist():
                self.assertEqual(ZIP_DATE_TIME, member.date_time)
                self.assertEqual(3, member.create_system)
                self.assertEqual(ZIP_MODE, member.external_attr >> 16)

    def test_release_checksum_is_deterministic(self):
        archive = build_archive()
        self.assertEqual(release_checksum(archive), release_checksum(archive))
        self.assertEqual(7, release_checksum(archive)["member_count"])

    def test_verifies_external_release_checksum(self):
        archive = build_archive()
        write_release_checksum(archive)
        self.assertEqual(archive, verify_release_checksum(RELEASE, archive))

    def test_verifies_renamed_archive_copy_against_release(self):
        archive = build_archive()
        write_release_checksum(archive)
        renamed = ROOT / "build" / "downloaded-from-drive.zip"
        renamed.write_bytes(archive.read_bytes())
        self.assertEqual(renamed, verify_release_checksum(RELEASE, renamed))

    def test_rejects_tampered_external_release_checksum(self):
        archive = build_archive()
        release = release_checksum(archive)
        release["sha256"] = "0" * 64
        path = ROOT / "build" / "tampered-release.json"
        path.write_text(json.dumps(release), encoding="utf-8")
        with self.assertRaisesRegex(ChronologyError, "CHR-RELEASE-002"):
            verify_release_checksum(path, archive)

    def test_rejects_archive_not_matching_external_release(self):
        archive = build_archive()
        write_release_checksum(archive)
        path = ROOT / "build" / "changed-after-release.zip"
        path.write_bytes(archive.read_bytes() + b"changed")
        with self.assertRaisesRegex(ChronologyError, "CHR-RELEASE-002"):
            verify_release_checksum(RELEASE, path)

    def test_rejects_archive_with_extra_member(self):
        source = build_archive()
        path = ROOT / "build" / "extra-member.zip"
        with zipfile.ZipFile(source) as original, zipfile.ZipFile(path, "w") as modified:
            for member in original.namelist():
                modified.writestr(member, original.read(member))
            modified.writestr("unexpected.txt", "not allowed")
        with self.assertRaisesRegex(ChronologyError, "CHR-ARCHIVE-002"):
            verify_archive(path)

    def test_rejects_archive_with_tampered_payload(self):
        source = build_archive()
        path = ROOT / "build" / "tampered-payload.zip"
        with zipfile.ZipFile(source) as original, zipfile.ZipFile(path, "w") as modified:
            for member in original.namelist():
                content = original.read(member)
                if member == "README.md":
                    content += b"tampered"
                modified.writestr(member, content)
        with self.assertRaisesRegex(ChronologyError, "CHR-ARCHIVE-004"):
            verify_archive(path)

    def test_clean_build(self):
        archive = build_archive()
        self.assertTrue(archive.exists())
        with zipfile.ZipFile(archive) as built:
            self.assertEqual(
                [*ARCHIVE_PAYLOAD, "reports/archive-manifest.json"],
                built.namelist(),
            )


if __name__ == "__main__":
    unittest.main()
