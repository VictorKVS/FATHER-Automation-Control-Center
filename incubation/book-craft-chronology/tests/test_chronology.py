import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from chronology import ChronologyError, build_archive, diagnose, load_data, mutate_for_diagnostic, query_event, validate_max, validate_med, validate_min


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

    def test_clean_build(self):
        archive = build_archive()
        self.assertTrue(archive.exists())


if __name__ == "__main__":
    unittest.main()
