from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import model_inventory_v2 as inv


def test_venv_and_site_packages_are_skipped() -> None:
    assert inv.should_skip_dir(r"G:\work", "venv")
    assert inv.should_skip_dir(r"G:\work\venv\Lib", "site-packages")


def test_small_framework_fixture_is_not_model() -> None:
    path = Path(r"G:\work\onnx\backend\test\data\node\x\model.onnx")
    assert not inv.candidate_file(path, 32_000)


def test_large_onnx_outside_runtime_noise_remains_candidate() -> None:
    path = Path(r"G:\models\vision\detector.onnx")
    assert inv.candidate_file(path, 100 * 1024 * 1024)


def test_tiny_python_pth_is_not_model() -> None:
    path = Path(r"G:\work\distutils-precedence.pth")
    assert not inv.candidate_file(path, 200)
