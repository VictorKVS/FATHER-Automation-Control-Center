from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from model_inventory import (
    build_artifact,
    candidate_file,
    compute_hashes,
    exact_duplicate_groups,
    logical_variant_groups,
)


def test_exact_duplicates_require_sha256(tmp_path: Path) -> None:
    a = tmp_path / "Qwen2.5-7B-Q4_K_M.gguf"
    b = tmp_path / "copy" / "Qwen2.5-7B-Q4_K_M.gguf"
    b.parent.mkdir()
    payload = b"same-model-bytes" * 100
    a.write_bytes(payload)
    b.write_bytes(payload)

    artifacts = [build_artifact(a), build_artifact(b)]
    compute_hashes(artifacts, "duplicates")
    groups = exact_duplicate_groups(artifacts)

    assert len(groups) == 1
    assert groups[0]["copies"] == 2
    assert groups[0]["potential_saving_bytes"] == len(payload)
    assert all(row.duplicate_group for row in artifacts)


def test_different_quantizations_are_not_physical_duplicates(tmp_path: Path) -> None:
    q4 = tmp_path / "Qwen2.5-7B-Q4_K_M.gguf"
    q8 = tmp_path / "Qwen2.5-7B-Q8_0.gguf"
    q4.write_bytes(b"q4" * 100)
    q8.write_bytes(b"q8" * 150)

    artifacts = [build_artifact(q4), build_artifact(q8)]
    compute_hashes(artifacts, "duplicates")

    assert exact_duplicate_groups(artifacts) == []
    assert artifacts[0].quantization != artifacts[1].quantization


def test_large_bin_needs_model_context(tmp_path: Path) -> None:
    plain = tmp_path / "archive.bin"
    model_dir = tmp_path / "models"
    model_dir.mkdir()
    model = model_dir / "weights.bin"

    threshold_size = 64 * 1024 * 1024
    assert candidate_file(plain, threshold_size) is False
    assert candidate_file(model, threshold_size) is True


def test_logical_variants_never_become_delete_instruction(tmp_path: Path) -> None:
    a = tmp_path / "Qwen2.5-7B-Q4_K_M.gguf"
    b = tmp_path / "Qwen2.5-7B-Q8_0.gguf"
    a.write_bytes(b"a")
    b.write_bytes(b"b")

    groups = logical_variant_groups([build_artifact(a), build_artifact(b)])
    for group in groups:
        assert group["action"] == "KEEP_VARIANTS_UNTIL_BENCHMARK"
        assert "not proof" in group["note"].casefold()
