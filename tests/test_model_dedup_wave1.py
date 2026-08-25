from scripts.model_dedup_wave1 import build_actions


def group(group_id, sha, size, paths):
    return {
        "group_id": group_id,
        "sha256": sha,
        "size_bytes_each": size,
        "paths": paths,
    }


def test_prefers_active_osint_g_copy_as_canonical():
    payload = {
        "exact_duplicate_groups": [
            group(
                "DUP-X",
                "a" * 64,
                100,
                [
                    r"C:\Users\1\.lmstudio\models\x.gguf",
                    r"G:\1\OSINT_deepseek\data\models\x.gguf",
                    r"G:\1\Прежде\KNOWLEDGE_CORE\models\x.gguf",
                    r"G:\1\Прежде\MF-KNOWLEDGE-BRAIN\models\x.gguf",
                ],
            )
        ]
    }
    actions = build_actions(payload)
    assert len(actions) == 2
    assert all(a.canonical == r"G:\1\OSINT_deepseek\data\models\x.gguf" for a in actions)
    assert all(r"\Прежде\" in a.target for a in actions)


def test_keeps_one_g_archive_copy_when_only_c_survivor_is_outside_wave():
    payload = {
        "exact_duplicate_groups": [
            group(
                "DUP-Y",
                "b" * 64,
                200,
                [
                    r"C:\Users\1\.lmstudio\models\y.gguf",
                    r"G:\1\Прежде\KNOWLEDGE_CORE\models\y.gguf",
                    r"G:\1\Прежде\MF-KNOWLEDGE-BRAIN\models\y.gguf",
                ],
            )
        ]
    }
    actions = build_actions(payload)
    assert len(actions) == 1
    assert actions[0].canonical == r"G:\1\Прежде\KNOWLEDGE_CORE\models\y.gguf"
    assert actions[0].target == r"G:\1\Прежде\MF-KNOWLEDGE-BRAIN\models\y.gguf"


def test_does_not_target_active_or_c_drive_paths():
    payload = {
        "exact_duplicate_groups": [
            group(
                "DUP-Z",
                "c" * 64,
                300,
                [
                    r"C:\Users\1\.lmstudio\models\z.gguf",
                    r"G:\1\OSINT_deepseek\data\models\z.gguf",
                ],
            )
        ]
    }
    assert build_actions(payload) == []


def test_different_sha_groups_are_never_combined_by_name():
    payload = {
        "exact_duplicate_groups": [
            group(
                "DUP-A",
                "d" * 64,
                400,
                [
                    r"G:\1\OSINT_deepseek\data\models\same-name.gguf",
                ],
            ),
            group(
                "DUP-B",
                "e" * 64,
                400,
                [
                    r"G:\1\Прежде\KNOWLEDGE_CORE\models\same-name.gguf",
                    r"G:\1\Прежде\MF-KNOWLEDGE-BRAIN\models\same-name.gguf",
                ],
            ),
        ]
    }
    actions = build_actions(payload)
    assert len(actions) == 1
    assert actions[0].group_id == "DUP-B"
    assert actions[0].canonical != r"G:\1\OSINT_deepseek\data\models\same-name.gguf"
