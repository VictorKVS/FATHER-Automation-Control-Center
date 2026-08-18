import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from chronology import REPORT, ChronologyError, build_archive, diagnostic_report, diagnose, load_data, mutate_for_diagnostic, query_event, validate_max, validate_med, validate_min, verify_diagnostic_report, write_diagnostic_report


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

    def test_clean_build(self):
        archive = build_archive()
        self.assertTrue(archive.exists())


if __name__ == "__main__":
    unittest.main()
