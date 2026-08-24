from __future__ import annotations

import argparse
import os
from collections import defaultdict
from pathlib import Path

import model_inventory as base

# Python/runtime payloads are not user model stores. Scanning them produced
# thousands of ONNX backend fixtures during the first real disk pass.
SKIP_DIR_NAMES = {
    "venv", ".venv", "env", ".env", "site-packages", "dist-packages",
    "tests", "test", "__pycache__", ".pytest_cache", ".mypy_cache",
    "node_modules", ".git", ".svn", ".idea", ".vscode",
    "$recycle.bin", "system volume information", "windows", "winsxs",
}

NOISE_PATH_TOKENS = (
    "\\lib\\site-packages\\",
    "\\site-packages\\",
    "\\dist-packages\\",
    "\\onnx\\backend\\test\\",
    "\\onnxruntime\\datasets\\",
    "\\tests\\data\\",
    "\\test\\data\\",
)

# Small framework fixtures with these generic extensions are usually code/test
# assets, not standalone model weights. Large real artifacts remain eligible.
MIN_BYTES_BY_SUFFIX = {
    ".onnx": 8 * 1024 * 1024,
    ".pt": 8 * 1024 * 1024,
    ".pth": 8 * 1024 * 1024,
    ".pb": 8 * 1024 * 1024,
    ".h5": 8 * 1024 * 1024,
    ".tflite": 4 * 1024 * 1024,
}

DEFAULT_MIN_HASH_BYTES = 64 * 1024 * 1024


def should_skip_dir(parent: str, name: str) -> bool:
    folded = name.casefold()
    if folded in SKIP_DIR_NAMES:
        return True
    full = os.path.join(parent, name).casefold().replace("/", "\\")
    if any(token in full for token in NOISE_PATH_TOKENS):
        return True
    return base.should_skip_dir(parent, name)


def candidate_file(path: Path, size_bytes: int) -> bool:
    full = str(path).casefold().replace("/", "\\")
    if any(token in full for token in NOISE_PATH_TOKENS):
        return False
    minimum = MIN_BYTES_BY_SUFFIX.get(path.suffix.casefold())
    if minimum is not None and size_bytes < minimum:
        return False
    return base.candidate_file(path, size_bytes)


def iter_model_files(roots: list[Path]):
    seen: set[str] = set()
    for root in roots:
        if not root.exists():
            continue
        if root.is_file():
            try:
                size = root.stat().st_size
            except OSError:
                continue
            if candidate_file(root, size):
                yield root
            continue

        for current, dirs, files in os.walk(root, topdown=True, onerror=lambda _exc: None):
            dirs[:] = [name for name in dirs if not should_skip_dir(current, name)]
            parent = Path(current)
            for name in files:
                path = parent / name
                try:
                    size = path.stat().st_size
                except OSError:
                    continue
                if not candidate_file(path, size):
                    continue
                try:
                    key = str(path.resolve()).casefold()
                except OSError:
                    key = str(path.absolute()).casefold()
                if key in seen:
                    continue
                seen.add(key)
                yield path


def compute_hashes(artifacts: list[base.Artifact], mode: str, min_hash_bytes: int) -> None:
    if mode == "none":
        return

    by_size: dict[int, list[base.Artifact]] = defaultdict(list)
    for artifact in artifacts:
        by_size[artifact.size_bytes].append(artifact)

    queue: list[base.Artifact] = []
    for size, rows in by_size.items():
        if size < min_hash_bytes:
            continue
        if mode != "all" and len(rows) < 2:
            continue
        queue.extend(row for row in rows if not row.sha256)

    total = len(queue)
    print(f"hash_candidates={total}")
    for index, artifact in enumerate(queue, 1):
        print(f"hash [{index}/{total}] {artifact.size_gib} GiB  {artifact.path}")
        try:
            artifact.sha256 = base.sha256_file(Path(artifact.path))
            artifact.hash_source = "COMPUTED_SHA256"
        except (OSError, PermissionError) as exc:
            print(f"hash_skip={artifact.path} reason={type(exc).__name__}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Noise-resistant read-only inventory of local AI/ML models.")
    parser.add_argument("roots", nargs="*", help="Roots to scan; omitted = local fixed/removable drives on Windows.")
    parser.add_argument("--output", default="reports/model_inventory/generated")
    parser.add_argument("--hash", choices=("none", "duplicates", "all"), default="duplicates")
    parser.add_argument("--min-hash-mib", type=int, default=64)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    roots = [Path(value) for value in args.roots] or base.windows_model_scan_roots()
    output = Path(args.output)

    print("FATHER Model Inventory v2 — READ ONLY")
    print("roots=" + ";".join(str(root) for root in roots))
    print(f"hash_mode={args.hash}")
    print(f"min_hash_mib={args.min_hash_mib}")
    print("noise_filters=venv,site-packages,dist-packages,tests,onnx-backend-fixtures")

    artifacts: list[base.Artifact] = []
    for index, path in enumerate(iter_model_files(roots), 1):
        try:
            artifact = base.build_artifact(path)
        except (OSError, PermissionError, ValueError):
            continue
        artifacts.append(artifact)
        # Keep the console useful; the generated inventory contains every artifact.
        if artifact.size_bytes >= 16 * 1024 * 1024 or base.is_ollama_blob(Path(artifact.path)):
            print(f"[{index}] {artifact.size_gib:>7} GiB  {artifact.store:<18} {artifact.path}")

    if not artifacts:
        print("status=NO_MODELS_FOUND")
        return 2

    # Critical reliability change: persist discovery BEFORE expensive hashing.
    base.write_outputs(artifacts, roots, output, "discovery_pre_hash")
    print(f"discovery_saved={output.absolute()}")
    print(f"discovered_artifacts={len(artifacts)}")

    try:
        print("Computing SHA-256 for meaningful duplicate candidates only...")
        compute_hashes(artifacts, args.hash, max(0, args.min_hash_mib) * 1024 * 1024)
    except KeyboardInterrupt:
        base.write_outputs(artifacts, roots, output, "partial_interrupted")
        print()
        print("status=MODEL_INVENTORY_PARTIAL")
        print("reason=HASHING_INTERRUPTED")
        print(f"artifacts={len(artifacts)}")
        print(f"hashed={sum(1 for item in artifacts if item.sha256)}")
        print(f"output={output.absolute()}")
        return 130

    base.write_outputs(artifacts, roots, output, args.hash)
    duplicate_groups = {item.duplicate_group for item in artifacts if item.duplicate_group}
    print()
    print("status=MODEL_INVENTORY_READY")
    print(f"artifacts={len(artifacts)}")
    print(f"packages={len({item.package_id for item in artifacts})}")
    print(f"total_gib={base.gib(sum(item.size_bytes for item in artifacts))}")
    print(f"hashed={sum(1 for item in artifacts if item.sha256)}")
    print(f"exact_duplicate_groups={len(duplicate_groups)}")
    print(f"output={output.absolute()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
