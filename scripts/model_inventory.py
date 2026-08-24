from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

MODEL_EXTENSIONS = {
    ".gguf",
    ".ggml",
    ".safetensors",
    ".ckpt",
    ".pt",
    ".pth",
    ".onnx",
    ".engine",
    ".tflite",
    ".h5",
    ".pb",
    ".mlmodel",
}

CONDITIONAL_EXTENSIONS = {".bin"}
MIN_CONDITIONAL_MODEL_BYTES = 64 * 1024 * 1024

MODEL_PATH_MARKERS = (
    "model",
    "models",
    "checkpoint",
    "checkpoints",
    "weights",
    "huggingface",
    "transformers",
    "ollama",
    "lm studio",
    "lm-studio",
    "comfyui",
    "stable-diffusion",
    "stable_diffusion",
    "forge",
    "loras",
    "lora",
    "controlnet",
    "vae",
    "unet",
    "clip",
    "whisper",
    "embeddings",
)

SKIP_DIR_NAMES = {
    "$recycle.bin",
    "system volume information",
    "windows",
    "winsxs",
    "program files",
    "program files (x86)",
    "programdata\\microsoft",
    "node_modules",
    ".git",
    ".svn",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".idea",
    ".vscode",
}

FAMILY_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("qwen", re.compile(r"\bqwen(?:2(?:\.5)?|3)?\b", re.I)),
    ("gigachat", re.compile(r"\bgigachat\b", re.I)),
    ("deepseek", re.compile(r"\bdeepseek\b", re.I)),
    ("llama", re.compile(r"\b(?:llama|codellama)\b", re.I)),
    ("mistral", re.compile(r"\b(?:mistral|mixtral)\b", re.I)),
    ("gemma", re.compile(r"\bgemma\b", re.I)),
    ("phi", re.compile(r"\bphi[-_. ]?\d*\b", re.I)),
    ("bge", re.compile(r"\bbge(?:[-_. ]?m3)?\b", re.I)),
    ("e5", re.compile(r"\be5(?:[-_. ]|\b)", re.I)),
    ("gte", re.compile(r"\bgte(?:[-_. ]|\b)", re.I)),
    ("whisper", re.compile(r"\bwhisper\b", re.I)),
    ("llava", re.compile(r"\bllava\b", re.I)),
    ("cogvlm", re.compile(r"\bcogvlm\b", re.I)),
    ("sdxl", re.compile(r"\bsdxl\b", re.I)),
    ("stable-diffusion", re.compile(r"\bstable[-_. ]?diffusion\b|\bsd[-_. ]?[12](?:\.\d)?\b", re.I)),
    ("flux", re.compile(r"\bflux(?:[-_. ]|\b)", re.I)),
    ("controlnet", re.compile(r"\bcontrolnet\b", re.I)),
    ("clip", re.compile(r"\b(?:clip|siglip)\b", re.I)),
    ("nllb", re.compile(r"\bnllb\b", re.I)),
    ("madlad", re.compile(r"\bmadlad\b", re.I)),
    ("opus-mt", re.compile(r"\bopus[-_. ]?mt\b|\bhelsinki[-_. ]?nlp\b", re.I)),
)

QUANT_PATTERNS = (
    re.compile(r"\bQ[2-8](?:_[A-Z0-9]+)+\b", re.I),
    re.compile(r"\bQ[2-8]\b", re.I),
    re.compile(r"\b(?:IQ[1-4](?:_[A-Z0-9]+)*)\b", re.I),
    re.compile(r"\b(?:F16|F32|FP16|FP32|BF16|INT8|INT4|NF4)\b", re.I),
)

PARAM_RE = re.compile(r"(?<!\d)(\d+(?:\.\d+)?)\s*[bB](?![A-Za-z])")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_id(*parts: str) -> str:
    return hashlib.sha256("\x1f".join(parts).encode("utf-8", errors="replace")).hexdigest()[:24]


def sha256_file(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def human_gib(value: int) -> float:
    return round(value / (1024 ** 3), 3)


def normalize_for_identity(value: str) -> str:
    text = Path(value).stem.casefold()
    text = re.sub(r"sha256[-_:]?[0-9a-f]{32,64}", " ", text)
    text = re.sub(r"\bq[2-8](?:_[a-z0-9]+)+\b", " ", text)
    text = re.sub(r"\b(?:iq[1-4](?:_[a-z0-9]+)*|f16|f32|fp16|fp32|bf16|int8|int4|nf4)\b", " ", text)
    text = re.sub(r"\b(?:gguf|ggml|safetensors|onnx|checkpoint|model|weights)\b", " ", text)
    text = re.sub(r"[_\-.]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def infer_family(path_text: str) -> str | None:
    for family, pattern in FAMILY_PATTERNS:
        if pattern.search(path_text):
            return family
    return None


def infer_quant(path_text: str) -> str | None:
    for pattern in QUANT_PATTERNS:
        match = pattern.search(path_text)
        if match:
            return match.group(0).upper()
    return None


def infer_parameters(path_text: str) -> str | None:
    matches = PARAM_RE.findall(path_text)
    if not matches:
        return None
    # Prefer the largest plausible parameter count mentioned in the path/name.
    values = sorted((float(value), value) for value in matches if 0 < float(value) <= 1000)
    if not values:
        return None
    value = values[-1][1]
    return f"{value}B"


def infer_store(path: Path) -> str:
    text = str(path).casefold().replace("/", "\\")
    if "\\.ollama\\models\\" in text or "\\ollama\\models\\" in text:
        return "OLLAMA"
    if "\\.cache\\huggingface\\" in text or "\\huggingface\\hub\\" in text or "models--" in text:
        return "HUGGINGFACE_CACHE"
    if "\\lm studio\\" in text or "\\lm-studio\\" in text or "\\lmstudio\\" in text:
        return "LM_STUDIO"
    if "\\comfyui\\" in text:
        return "COMFYUI"
    if "stable-diffusion-webui" in text or "stable_diffusion_webui" in text or "\\forge\\" in text:
        return "SD_WEBUI"
    return "FILESYSTEM"


def infer_capabilities(path_text: str, family: str | None) -> list[str]:
    text = path_text.casefold()
    caps: set[str] = set()

    if family in {"bge", "e5", "gte"} or "embedding" in text:
        caps.update({"embedding", "retrieval"})
    if family == "whisper" or "whisper" in text:
        caps.update({"speech_to_text", "audio"})
    if family in {"llava", "cogvlm"} or any(token in text for token in ("vision", "qwen-vl", "internvl")):
        caps.update({"vision", "image_understanding"})
    if family in {"sdxl", "stable-diffusion", "flux", "controlnet"} or any(
        token in text for token in ("lora", "vae", "unet", "diffusion", "animatediff")
    ):
        caps.update({"image_generation"})
    if family in {"nllb", "madlad", "opus-mt"} or "translation" in text:
        caps.update({"translation"})
    if any(token in text for token in ("coder", "code", "deepseek-coder", "codellama")):
        caps.update({"code", "text_generation"})
    if family in {"qwen", "gigachat", "deepseek", "llama", "mistral", "gemma", "phi"}:
        caps.add("text_generation")
    if any(token in text for token in ("instruct", "chat")) and "text_generation" in caps:
        caps.add("instruction_following")
    if any(token in text for token in ("reranker", "rerank")):
        caps.add("reranking")
    if any(token in text for token in ("ocr", "docling", "layout")):
        caps.add("document_understanding")

    return sorted(caps or {"unknown"})


def is_ollama_blob(path: Path) -> bool:
    return path.parent.name.casefold() == "blobs" and path.name.casefold().startswith("sha256-")


def is_candidate_model_file(path: Path, size_bytes: int) -> bool:
    suffix = path.suffix.casefold()
    if suffix in MODEL_EXTENSIONS:
        return True
    if is_ollama_blob(path):
        return True
    if suffix in CONDITIONAL_EXTENSIONS:
        text = str(path).casefold()
        return size_bytes >= MIN_CONDITIONAL_MODEL_BYTES and any(marker in text for marker in MODEL_PATH_MARKERS)
    return False


def should_skip_dir(path: str, name: str) -> bool:
    folded = name.casefold()
    full = os.path.join(path, name).casefold().replace("/", "\\")
    if folded in SKIP_DIR_NAMES:
        return True
    return any(marker in full for marker in ("\\windows\\", "\\winsxs\\", "\\node_modules\\", "\\.git\\"))


def iter_candidate_files(roots: Iterable[Path]) -> Iterable[Path]:
    seen_paths: set[str] = set()
    for root in roots:
        if not root.exists():
            continue
        if root.is_file():
            try:
                size = root.stat().st_size
            except OSError:
                continue
            if is_candidate_model_file(root, size):
                resolved = str(root.resolve()).casefold()
                if resolved not in seen_paths:
                    seen_paths.add(resolved)
                    yield root
            continue

        for current, dirnames, filenames in os.walk(root, topdown=True, onerror=lambda _exc: None):
            dirnames[:] = [name for name in dirnames if not should_skip_dir(current, name)]
            current_path = Path(current)
            for filename in filenames:
                path = current_path / filename
                try:
                    size = path.stat().st_size
                except OSError:
                    continue
                if not is_candidate_model_file(path, size):
                    continue
                try:
                    resolved = str(path.resolve()).casefold()
                except OSError:
                    resolved = str(path.absolute()).casefold()
                if resolved in seen_paths:
                    continue
                seen_paths.add(resolved)
                yield path


def infer_package_root(path: Path, store: str) -> str:
    parts = list(path.parts)
    lower = [part.casefold() for part in parts]

    if store == "OLLAMA":
        if "blobs" in lower:
            idx = lower.index("blobs")
            return str(Path(*parts[:idx]))
        if "manifests" in lower:
            idx = lower.index("manifests")
            return str(Path(*parts[:idx]))

    if store == "HUGGINGFACE_CACHE":
        for idx, part in enumerate(parts):
            if part.startswith("models--"):
                # Keep snapshot identity when available so revisions are not silently merged.
                if idx + 3 < len(parts) and parts[idx + 1].casefold() == "snapshots":
                    return str(Path(*parts[: idx + 3]))
                return str(Path(*parts[: idx + 1]))

    # Sharded safetensors/onnx packages generally sit together with config/index files.
    if path.suffix.casefold() in {".safetensors", ".onnx", ".bin"}:
        parent = path.parent
        sibling_names = {child.name.casefold() for child in parent.iterdir()} if parent.exists() else set()
        if any(name in sibling_names for name in ("config.json", "model.safetensors.index.json", "pytorch_model.bin.index.json")):
            return str(parent)

    return str(path)


def fixed_drives_windows() -> list[Path]:
    if os.name != "nt":
        return []
    try:
        import ctypes

        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        roots: list[Path] = []
        for letter_index in range(26):
            if not bitmask & (1 << letter_index):
                continue
            letter = chr(ord("A") + letter_index)
            root = f"{letter}:\\"
            drive_type = ctypes.windll.kernel32.GetDriveTypeW(root)
            # DRIVE_FIXED=3; include removable/external DRIVE_REMOVABLE=2 as model disks are often external.
            if drive_type in (2, 3):
                roots.append(Path(root))
        return roots
    except Exception:
        return []


@dataclass(slots=True)
class ModelArtifact:
    artifact_id: str
    path: str
    file_name: str
    size_bytes: int
    size_gib: float
    modified_at: str
    store: str
    format: str
    family: str | None
    parameters: str | None
    quantization: str | None
    capabilities: list[str]
    package_root: str
    package_id: str
    logical_model_key: str
    sha256: str | None = None
    hash_source: str | None = None
    exact_duplicate_group: str | None = None
    exact_duplicate_group_size: int = 1

    def to_dict(self) -> dict:
        return asdict(self)


def build_artifact(path: Path) -> ModelArtifact:
    stat = path.stat()
    path_text = str(path)
    store = infer_store(path)
    family = infer_family(path_text)
    package_root = infer_package_root(path, store)
    quant = infer_quant(path_text)
    params = infer_parameters(path_text)
    format_name = "OLLAMA_BLOB" if is_ollama_blob(path) else path.suffix.casefold().lstrip(".").upper()

    sha = None
    hash_source = None
    if is_ollama_blob(path):
        candidate = path.name[len("sha256-") :].lower()
        if re.fullmatch(r"[0-9a-f]{64}", candidate):
            sha = candidate
            hash_source = "OLLAMA_CONTENT_ADDRESS"

    identity_name = normalize_for_identity(path.name)
    logical_parts = [family or "unknown", params or "unknown", identity_name]
    logical_key = "::".join(logical_parts)

    return ModelArtifact(
        artifact_id=f"ART-{stable_id(str(path.absolute()), str(stat.st_size), str(stat.st_mtime_ns))}",
        path=str(path.absolute()),
        file_name=path.name,
        size_bytes=stat.st_size,
        size_gib=human_gib(stat.st_size),
        modified_at=datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
        store=store,
        format=format_name,
        family=family,
        parameters=params,
        quantization=quant,
        capabilities=infer_capabilities(path_text, family),
        package_root=package_root,
        package_id=f"PKG-{stable_id(package_root)}",
        logical_model_key=logical_key,
        sha256=sha,
        hash_source=hash_source,
    )


def hash_duplicate_candidates(artifacts: list[ModelArtifact], hash_mode: str) -> None:
    if hash_mode == "none":
        return

    by_size: dict[int, list[ModelArtifact]] = defaultdict(list)
    for artifact in artifacts:
        by_size[artifact.size_bytes].append(artifact)

    for size, rows in by_size.items():
        should_hash = hash_mode == "all" or len(rows) > 1
        if not should_hash or size <= 0:
            continue
        for artifact in rows:
            if artifact.sha256:
                continue
            try:
                artifact.sha256 = sha256_file(Path(artifact.path))
                artifact.hash_source = "COMPUTED_SHA256"
            except (OSError, PermissionError):
                continue


def assign_exact_duplicate_groups(artifacts: list[ModelArtifact]) -> list[dict]:
    by_sha: dict[str, list[ModelArtifact]] = defaultdict(list)
    for artifact in artifacts:
        if artifact.sha256:
            by_sha[artifact.sha256].append(artifact)

    groups: list[dict] = []
    for sha, rows in sorted(by_sha.items()):
        if len(rows) < 2:
            continue
        group_id = f"DUP-{sha[:16].upper()}"
        for artifact in rows:
            artifact.exact_duplicate_group = group_id
            artifact.exact_duplicate_group_size = len(rows)

        # Do not delete automatically. Prefer a non-cache, non-temp path only as a review candidate.
        def canonical_rank(row: ModelArtifact) -> tuple[int, int, str]:
            path = row.path.casefold()
            cache_penalty = int(any(token in path for token in ("\\cache\\", "\\temp\\", "\\tmp\\")))
            return (cache_penalty, len(row.path), row.path.casefold())

        canonical = sorted(rows, key=canonical_rank)[0]
        groups.append(
            {
                "group_id": group_id,
                "sha256": sha,
                "copies": len(rows),
                "size_bytes_each": rows[0].size_bytes,
                "potential_saving_bytes": rows[0].size_bytes * (len(rows) - 1),
                "canonical_candidate": canonical.path,
                "paths": [row.path for row in rows],
                "action": "REVIEW_EXACT_DUPLICATE",
            }
        )
    return groups


def logical_groups(artifacts: list[ModelArtifact]) -> list[dict]:
    package_representatives: dict[str, list[ModelArtifact]] = defaultdict(list)
    for artifact in artifacts:
        package_representatives[artifact.package_id].append(artifact)

    package_rows: list[dict] = []
    for package_id, members in package_representatives.items():
        families = sorted({row.family for row in members if row.family})
        params = sorted({row.parameters for row in members if row.parameters})
        quants = sorted({row.quantization for row in members if row.quantization})
        caps = sorted({cap for row in members for cap in row.capabilities})
        stores = sorted({row.store for row in members})
        formats = sorted({row.format for row in members})
        package_rows.append(
            {
                "package_id": package_id,
                "package_root": members[0].package_root,
                "artifact_count": len(members),
                "total_bytes": sum(row.size_bytes for row in members),
                "families": families,
                "parameters": params,
                "quantizations": quants,
                "capabilities": caps,
                "stores": stores,
                "formats": formats,
                "identity_hints": sorted({row.logical_model_key for row in members}),
            }
        )

    by_identity: dict[str, list[dict]] = defaultdict(list)
    for row in package_rows:
        family = row["families"][0] if len(row["families"]) == 1 else "unknown"
        params = row["parameters"][0] if len(row["parameters"]) == 1 else "unknown"
        # identity_hints intentionally ignore quantization, so variants can be grouped but not deleted.
        hint = min(row["identity_hints"], key=len) if row["identity_hints"] else row["package_root"].casefold()
        identity = f"{family}::{params}::{hint}"
        by_identity[identity].append(row)

    result = []
    for identity, rows in sorted(by_identity.items()):
        if len(rows) < 2:
            continue
        result.append(
            {
                "logical_group_id": f"LOG-{stable_id(identity)}",
                "identity": identity,
                "packages": rows,
                "action": "KEEP_VARIANTS_UNTIL_BENCHMARK",
                "note": "Logical similarity is not proof of byte duplication; do not delete by this group alone.",
            }
        )
    return result


def write_outputs(artifacts: list[ModelArtifact], roots: list[Path], output_dir: Path, hash_mode: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    exact_groups = assign_exact_duplicate_groups(artifacts)
    logical = logical_groups(artifacts)

    total_bytes = sum(row.size_bytes for row in artifacts)
    saving_bytes = sum(group["potential_saving_bytes"] for group in exact_groups)
    package_count = len({row.package_id for row in artifacts})
    hashed_count = sum(1 for row in artifacts if row.sha256)

    payload = {
        "schema_version": "father-model-inventory.v0.1",
        "generated_at": utc_now(),
        "read_only": True,
        "roots": [str(root) for root in roots],
        "hash_mode": hash_mode,
        "counters": {
            "artifacts": len(artifacts),
            "packages": package_count,
            "total_bytes": total_bytes,
            "total_gib": human_gib(total_bytes),
            "hashed_artifacts": hashed_count,
            "exact_duplicate_groups": len(exact_groups),
            "potential_exact_duplicate_saving_bytes": saving_bytes,
            "potential_exact_duplicate_saving_gib": human_gib(saving_bytes),
            "logical_variant_groups": len(logical),
        },
        "stores": dict(Counter(row.store for row in artifacts)),
        "formats": dict(Counter(row.format for row in artifacts)),
        "families": dict(Counter(row.family or "UNKNOWN" for row in artifacts)),
        "capabilities": dict(Counter(cap for row in artifacts for cap in row.capabilities)),
        "artifacts": [row.to_dict() for row in artifacts],
        "exact_duplicate_groups": exact_groups,
        "logical_variant_groups": logical,
    }

    json_path = output_dir / "model_inventory.json"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    csv_path = output_dir / "model_inventory.csv"
    fields = list(ModelArtifact.__dataclass_fields__.keys())
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for artifact in artifacts:
            row = artifact.to_dict()
            row["capabilities"] = ";".join(artifact.capabilities)
            writer.writerow(row)

    dedup_path = output_dir / "model_dedup_plan.json"
    dedup_path.write_text(
        json.dumps(
            {
                "schema_version": "father-model-dedup-plan.v0.1",
                "generated_at": utc_now(),
                "read_only": True,
                "automatic_delete_allowed": False,
                "exact_duplicate_groups": exact_groups,
                "logical_variant_groups": logical,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    md = [
        "# FATHER Local Model Inventory",
        "",
        "> Read-only inventory. No files were moved, deleted, linked, or modified.",
        "",
        f"Generated: `{payload['generated_at']}`",
        "",
        "## Counters",
        "",
        f"- artifacts: **{len(artifacts)}**",
        f"- packages: **{package_count}**",
        f"- total size: **{human_gib(total_bytes)} GiB**",
        f"- artifacts with SHA-256: **{hashed_count}**",
        f"- exact duplicate groups: **{len(exact_groups)}**",
        f"- potential exact-duplicate saving: **{human_gib(saving_bytes)} GiB**",
        f"- logical variant groups: **{len(logical)}**",
        "",
        "## Stores",
        "",
    ]
    for key, value in sorted(payload["stores"].items(), key=lambda item: (-item[1], item[0])):
        md.append(f"- `{key}`: {value}")

    md.extend(["", "## Largest artifacts", "", "| # | GiB | Store | Format | Family | Params | Quant | Capabilities | Path |", "|---:|---:|---|---|---|---|---|---|---|"])
    for idx, artifact in enumerate(sorted(artifacts, key=lambda row: row.size_bytes, reverse=True)[:100], start=1):
        md.append(
            f"| {idx} | {artifact.size_gib} | {artifact.store} | {artifact.format} | "
            f"{artifact.family or ''} | {artifact.parameters or ''} | {artifact.quantization or ''} | "
            f"{', '.join(artifact.capabilities)} | `{artifact.path.replace('|', '\\|')}` |"
        )

    md.extend(["", "## Exact duplicate candidates", ""])
    if not exact_groups:
        md.append("No exact duplicate group was proven by SHA-256 in this pass.")
    else:
        for group in exact_groups:
            md.extend(
                [
                    f"### {group['group_id']} — {group['copies']} copies, potential saving {human_gib(group['potential_saving_bytes'])} GiB",
                    "",
                    f"SHA-256: `{group['sha256']}`",
                    "",
                    f"Canonical candidate (review only): `{group['canonical_candidate']}`",
                    "",
                ]
            )
            for path in group["paths"]:
                md.append(f"- `{path}`")
            md.append("")

    md.extend(["## Logical variants", "", "These are **not** deletion candidates. They are candidates for later benchmark/role consolidation.", ""])
    for group in logical[:50]:
        md.append(f"- `{group['logical_group_id']}` — {len(group['packages'])} packages — `{group['identity']}`")

    (output_dir / "model_inventory.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only inventory of local AI/ML model artifacts.")
    parser.add_argument("roots", nargs="*", help="Roots to scan. On Windows, defaults to fixed/removable drives if omitted.")
    parser.add_argument("--output", default="reports/model_inventory/generated", help="Output directory.")
    parser.add_argument(
        "--hash",
        choices=("none", "duplicates", "all"),
        default="duplicates",
        help="SHA-256 policy: none, same-size duplicate candidates (default), or all artifacts.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    roots = [Path(value) for value in args.roots]
    if not roots:
        roots = fixed_drives_windows()
        if not roots:
            roots = [Path.home()]

    print("FATHER Model Inventory — READ ONLY")
    print("roots=" + ";".join(str(root) for root in roots))
    print(f"hash_mode={args.hash}")

    artifacts: list[ModelArtifact] = []
    for index, path in enumerate(iter_candidate_files(roots), start=1):
        try:
            artifact = build_artifact(path)
        except (OSError, PermissionError, ValueError):
            continue
        artifacts.append(artifact)
        print(f"[{index}] {artifact.size_gib:>7} GiB  {artifact.store:<18} {artifact.path}")

    if not artifacts:
        print("No model artifacts found.")
        return 2

    print("Computing SHA-256 according to policy...")
    hash_duplicate_candidates(artifacts, args.hash)

    output_dir = Path(args.output)
    write_outputs(artifacts, roots, output_dir, args.hash)

    exact_groups = {row.exact_duplicate_group for row in artifacts if row.exact_duplicate_group}
    total_bytes = sum(row.size_bytes for row in artifacts)
    print()
    print("status=MODEL_INVENTORY_READY")
    print(f"artifacts={len(artifacts)}")
    print(f"packages={len({row.package_id for row in artifacts})}")
    print(f"total_gib={human_gib(total_bytes)}")
    print(f"hashed={sum(1 for row in artifacts if row.sha256)}")
    print(f"exact_duplicate_groups={len(exact_groups)}")
    print(f"output={output_dir.absolute()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
