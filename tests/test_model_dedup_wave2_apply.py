import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import model_dedup_wave2_apply as apply2


class Wave2ApplySafetyTests(unittest.TestCase):
    def test_confirmation_phrase_is_explicit_and_wave_specific(self):
        self.assertEqual(apply2.CONFIRM_PHRASE, "APPLY_WAVE2_HARDLINKS")

    def test_main_refuses_without_confirmation_before_touching_plan(self):
        old_argv = sys.argv
        try:
            sys.argv = ["model_dedup_wave2_apply.py"]
            self.assertEqual(apply2.main(), 2)
        finally:
            sys.argv = old_argv


if __name__ == "__main__":
    unittest.main()
