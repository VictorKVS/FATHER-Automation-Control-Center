import sys
import unittest
from pathlib import Path

# Keep direct execution (`python tests/test_model_dedup_wave2.py`) deterministic.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.model_dedup_wave2 import build_actions


def group(group_id, sha, size, paths):
    return {
        "group_id": group_id,
        "sha256": sha,
        "size_bytes_each": size,
        "paths": paths,
    }


class Wave2SelectionTests(unittest.TestCase):
    def test_prefers_stable_ai_checkpoint_as_canonical(self):
        payload = {
            "exact_duplicate_groups": [
                group(
                    "DUP-IMG",
                    "a" * 64,
                    100,
                    [
                        r"C:\Users\1\.lmstudio\models\x.safetensors",
                        r"G:\1\Прежде\1_izobraznie\AI\models\checkpoints\x.safetensors",
                        r"G:\1\Прежде\1_izobraznie\AI\models\StableDiffusion\x.safetensors",
                        r"G:\1\Прежде\1_izobraznie\AI\stable-diffusion-webui-OLD\models\Stable-diffusion\x.safetensors",
                    ],
                )
            ]
        }
        actions = build_actions(payload)
        self.assertEqual(len(actions), 2)
        self.assertTrue(
            all(
                action.canonical
                == r"G:\1\Прежде\1_izobraznie\AI\models\checkpoints\x.safetensors"
                for action in actions
            )
        )

    def test_current_standalone_comfyui_is_not_a_target(self):
        payload = {
            "exact_duplicate_groups": [
                group(
                    "DUP-CURRENT",
                    "b" * 64,
                    200,
                    [
                        r"G:\1\Прежде\1_izobraznie\ComfyUI\models\checkpoints\x.safetensors",
                        r"G:\1\Прежде\1_izobraznie\MindForge_Studio\resources\models\checkpoints\x.safetensors",
                    ],
                )
            ]
        }
        self.assertEqual(build_actions(payload), [])

    def test_old_runtime_paths_are_targets_but_paths_are_preserved(self):
        payload = {
            "exact_duplicate_groups": [
                group(
                    "DUP-OLD",
                    "c" * 64,
                    300,
                    [
                        r"G:\1\Прежде\1_izobraznie\AI\models\loras\lora.safetensors",
                        r"G:\1\Прежде\1_izobraznie\AI\ComfyUI\ComfyUI\models\loras\lora.safetensors",
                        r"G:\1\Прежде\1_izobraznie\AI\stable-diffusion-webui-OLD\models\Lora\lora.safetensors",
                    ],
                )
            ]
        }
        actions = build_actions(payload)
        self.assertEqual(len(actions), 2)
        self.assertTrue(
            all(
                "stable-diffusion-webui-OLD" in action.target
                or "AI\\ComfyUI" in action.target
                for action in actions
            )
        )

    def test_same_name_different_sha_is_never_combined(self):
        payload = {
            "exact_duplicate_groups": [
                group(
                    "DUP-A",
                    "d" * 64,
                    400,
                    [r"G:\1\Прежде\1_izobraznie\AI\models\checkpoints\same.safetensors"],
                ),
                group(
                    "DUP-B",
                    "e" * 64,
                    400,
                    [
                        r"G:\1\Прежде\1_izobraznie\AI\models\checkpoints\same.safetensors",
                        r"G:\1\Прежде\1_izobraznie\AI\stable-diffusion-webui-OLD\models\Stable-diffusion\same.safetensors",
                    ],
                ),
            ]
        }
        actions = build_actions(payload)
        self.assertEqual(len(actions), 1)
        self.assertEqual(actions[0].group_id, "DUP-B")


if __name__ == "__main__":
    unittest.main()
