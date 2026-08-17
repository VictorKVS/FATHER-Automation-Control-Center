import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.automations = json.loads((ROOT / "registry/automations.json").read_text(encoding="utf-8"))
        cls.factories = json.loads((ROOT / "registry/factories.json").read_text(encoding="utf-8"))

    def test_capacity_and_unique_streams(self):
        streams = self.automations["streams"]
        self.assertEqual(len(streams), self.automations["capacity"])
        self.assertEqual(len({item["stream_id"] for item in streams}), len(streams))
        self.assertLessEqual(sum(item["status"] == "active" for item in streams), self.automations["capacity"])

    def test_one_security_and_three_book_streams(self):
        active = [item for item in self.automations["streams"] if item["status"] == "active"]
        self.assertEqual(sum(item["factory_id"] == "SEC-KB-FACTORY" for item in active), 1)
        self.assertEqual(sum(item["factory_id"] == "BOOK-KB-FACTORY" for item in active), 3)

    def test_active_factories_exist(self):
        factory_ids = {item["factory_id"] for item in self.factories["factories"]}
        for stream in self.automations["streams"]:
            if stream["status"] == "active":
                self.assertIn(stream["factory_id"], factory_ids)

    def test_no_invented_actual_runtime(self):
        for stream in self.automations["streams"]:
            value = stream["actual_runtime_hours"]
            self.assertTrue(value is None or value >= 0)

    def test_event_ids_are_unique(self):
        with (ROOT / "registry/stream_events.csv").open(encoding="utf-8", newline="") as file:
            events = list(csv.DictReader(file))
        self.assertEqual(len({event["event_id"] for event in events}), len(events))

if __name__ == "__main__":
    unittest.main()
