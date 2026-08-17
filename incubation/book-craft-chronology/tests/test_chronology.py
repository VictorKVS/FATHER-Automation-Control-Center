import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from chronology import ChronologyError, build_archive, load_data, query_event, validate_max, validate_med, validate_min


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

    def test_clean_build(self):
        archive = build_archive()
        self.assertTrue(archive.exists())


if __name__ == "__main__":
    unittest.main()
