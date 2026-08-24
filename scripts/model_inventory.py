from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

MODEL_EXTENSIONS = {
    ".gguf", ".ggml", ".safetensors", ".ckpt", ".pt", ".pth",
    ".onnx", ".engine", ".tflite", ".h5", ".pb", ".mlmodel",
}
CONDITIONAL_EXTENSIONS = {".bin"}
MIN_CONDITIONAL_MODEL_BYTES = 64 * 1024 * 1024

MODEL_PATH_MARKERS = (
    "model", "models", "checkpoint", "weights", "huggingface", "ollama",
    "lm studio", "lm-studio", "lmstudio", "comfyui", "stable-diffusion",
    "stable_diffusion", "forge", "lora", "controlnet", "vae", "unet",
    "clip", "whisper", "embedding",
)

SKIP_DIR_NAMES = {
    "$recycle.bin", "system volume information", "windows", "winsxs",
    "program files", "program files (x86)", "node_modules", ".git", ".svn",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".idea", ".vscode",
}

FAMILY_PATTERNS = (
    ("qwen", re.compile(r"qwen", re.I)),
    ("gigachat", re.compile(r"gigachat", re.I)),
    ("deepseek", re.compile(r"deepseek", re.I)),
    ("llama", re.compile(r"(?:llama|codellama)", re.I)),
    ("mistral", re.compile(r"(?:mistral|mixtral)", re.I)),
    ("gemma", re.compile(r"gemma", re.I)),
    ("phi", re.compile(r"\bphi[-_. ]?\d*", re.I)),
    ("bge", re.compile(r"\bbge(?:[-_. ]?m3)?", re.I)),
    ("e5", re.compile(r"\be5(?:[-_. ]|\b)", re.I)),
    ("gte", re.compile(r"\bgte(?:[-_. ]|\b)", re.I)),
    ("whisper", re.compile(r"whisper", re.I)),
    ("llava", re.compile(r"llava", re.I)),
    ("cogvlm", re.compile(r"cogvlm", re.I)),
    ("sdxl", re.compile(r"sdxl", re.I)),
    ("stable-diffusion", re.compile(r"stable[-_. ]?diffusion", re.I)),
    ("flux", re.compile(r"\bflux(?:[-_. ]|\b)", re.I)),
    ("controlnet", re.compile(r"controlnet", re.I)),
    ("clip", re.compile(r"(?:\bclip\b|siglip)", re.I)),
    ("nllb", re.compile(r"nllb", re.I)),
    ("madlad", re.compile(r"madlad", re.I)),
    ("opus-mt", re.compile(r"(?:opus[-_. ]?mt|helsinki[-_. ]?nlp)", re.I)),
)

QUANT_PATTERNS = (
    re.compile(r"\bQ[2-8](?:_[A-Z0-9]+)+\b", re.I),
    re.compile(r"\bQ[2-8]\b", re.I),
    re.compile(r"\bIQ[1-4](?:_[A-Z0-9]+)*\b", re.I),
    re.compile(r"\b(?:F16|F32|FP16|FP32|BF16|INT8|INT4|NF4)\b", re.I),
)
PARAM_RE = re.compile(r"(?<!\d)(\d+(?:\.\d+)?)\s*[bB](?![A-Za-z])")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_id(*parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8", errors="replace")
    return hashlib.sha256(payload).hexdigest()[:24]


def sha256_file(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def gib(value: int) -> float:
    return round(value / (1024 ** 3), 3)


def md_escape(value: str) -> str:
    return value.replace("|", "\\|")


def infer_family(text: str) -> str | None:
    for family, pattern in FAMILY_PATTERNS:
        if pattern.search(text):
            return family
    return None


def infer_quant(text: str) -> str | None:
    for pattern in QUANT_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(0).upper()
    return None


def infer_parameters(text: str) -> str | None:
    values = []
    for raw in PARAM_RE.findall(text):
        value = float(raw)
        if 0 < value <= 1000:
            values.append((value, raw))
    if not values:
        return None
    return f"{sorted(values)[-1][1]}B"


def infer_store(path: Path) -> str:
    text = str(path).casefold().replace("/", "\\")
    if "\\.ollama\\models\\" in text or "\\ollama\\models\\" in text:
        return "OLLAMA"
    if "\\.cache\\huggingface\\" in text or "\\huggingface\\hub\\" in text or "models--" in text:
        return "HUGGINGFACE_CACHE"
    if any(token in text for token in ("\\lm studio\\", "\\lm-studio\\", "\\lmstudio\\")):
        return "LM_STUDIO"
    if "\\comfyui\\" in text:
        return "COMFYUI"
    if any(token in text for token in ("stable-diffusion-webui", "stable_diffusion_webui", "\\forge\\")):
        return "SD_WEBUI"
    return "FILESYSTEM"


def infer_capabilities(text: str, family: str | None) -> list[str]:
    folded = text.casefold()
    caps: set[str] = set()
    if family in {"bge", "e5", "gte"} or "embedding" in folded:
        caps.update({"embedding", "retrieval"})
    if family == "whisper" or "whisper" in folded:
        caps.update({"speech_to_text", "audio"})
    if family in {"llava", "cogvlm"} or any(x in folded for x in ("vision", "qwen-vl", "internvl")):
        caps.update({"vision", "image_understanding"})
    if family in {"sdxl", "stable-diffusion", "flux", "controlnet"} or any(
        x in folded for x in ("lora", "vae", "unet", "diffusion", "animatediff")
    ):
        caps.add("image_generation")
    if family in {"nllb", "madlad", "opus-mt"} or "translation" in folded:
        caps.add("translation")
    if any(x in folded for x in ("coder", "codellama", "deepseek-coder")):
        caps.update({"code", "text_generation"})
    if family in {"qwen", "gigachat", "deepseek", "llama", "mistral", "gemma", "phi"}:
        caps.add("text_generation")
    if "text_generation" in caps and any(x in folded for x in ("instruct", "chat")):
        caps.add("instruction_following")
    if any(x in folded for x in ("reranker", "rerank")):
        caps.add("reranking")
    if any(x in folded for x in ("ocr", "docling", "layout")):
        caps.add("document_understanding")
    return sorted(caps or {"unknown"})


def is_ollama_blob(path: Path) -> bool:
    return path.parent.name.casefold() == "blobs" and path.name.casefold().startswith("sha256-")


def candidate_file(path: Path, size_bytes: int) -> bool:
    suffix = path.suffix.casefold()
    if suffix in MODEL_EXTENSIONS or is_ollama_blob(path):
        return True
    if suffix in CONDITIONAL_EXTENSIONS and size_bytes >= MIN_CONDITIONAL_MODEL_BYTES:
        folded = str(path).casefold()
        return any(marker in folded for marker in MODEL_PATH_MARKERS)
    return False


def should_skip_dir(parent: str, name: str) -> bool:
    folded = name.casefold()
    if folded in SKIP_DIR_NAMES:
        return True
    full = os.path.join(parent, name).casefold().replace("/", "\\")
    return any(token in full for token in ("\\windows\\", "\\winsxs\\", "\\node_modules\\", "\\.git\\"))


def iter_model_files(roots: Iterable[Path]) -> Iterable[Path]:
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
            base = Path(current)
            for name in files:
                path = base / name
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


def normalize_identity(name: str) -> str:
    text = Path(name).stem.casefold()
    text = re.sub(r"sha256[-_:]?[0-9a-f]{32,64}", " ", text)
    text = re.sub(r"\bq[2-8](?:_[a-z0-9]+)+\b", " ", text)
    text = re.sub(r"\b(?:iq[1-4](?:_[a-z0-9]+)*|f16|f32|fp16|fp32|bf16|int8|int4|nf4)\b", " ", text)
    text = re.sub(r"[_\-.]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def package_root(path: Path, store: str) -> str:
    parts = list(path.parts)
    lower = [part.casefold() for part in parts]
    if store == "HUGGINGFACE_CACHE":
        for idx, part in enumerate(parts):
            if part.startswith("models--"):
                if idx + 3 < len(parts) and parts[idx + 1].casefold() == "snapshots":
                    return str(Path(*parts[: idx + 3]))
                return str(Path(*parts[: idx + 1]))
    if store == "OLLAMA":
        if "blobs" in lower:
            return str(Path(*parts[: lower.index("blobs")]))
        if "manifests" in lower:
            return str(Path(*parts[: lower.index("manifests")]))
    if path.suffix.casefold() in {".safetensors", ".onnx", ".bin"}:
        parent = path.parent
        try:
            names = {child.name.casefold() for child in parent.iterdir()}
        except OSError:
            names = set()
        if names.intersection({"config.json", "model.safetensors.index.json", "pytorch_model.bin.index.json"}):
            return str(parent)
    return str(path)


def windows_model_scan_roots() -> list[Path]:
    if os.name != "nt":
        return [Path.home()]
    roots: list[Path] = []
    try:
        import ctypes

        mask = ctypes.windll.kernel32.GetLogicalDrives()
        for idx in range(26):
            if not mask & (1 << idx):
                continue
            drive = f"{chr(ord('A') + idx)}:\\"
            drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive)
            if drive_type in (2, 3):
                roots.append(Path(drive))
    except Exception:
        pass
    return roots or [Path.home()]


@dataclass(slots=True)
class Artifact:
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
    logical_key: str
    sha256: str | None = None
    hash_source: str | None = None
    duplicate_group: str | None = None
    duplicate_group_size: int = 1


def build_artifact(path: Path) -> Artifact:
    stat = path.stat()
    text = str(path)
    store = infer_store(path)
    family = infer_family(text)
    root = package_root(path, store)
    sha = None
    hash_source = None
    if is_ollama_blob(path):
        candidate = path.name.removeprefix("sha256-").casefold()
        if re.fullmatch(r"[0-9a-f]{64}", candidate):
            sha = candidate
            hash_source = "OLLAMA_CONTENT_ADDRESS"
    identity = normalize_identity(path.name)
    return Artifact(
        artifact_id=f"ART-{stable_id(str(path.absolute()), str(stat.st_size), str(stat.st_mtime_ns))}",
        path=str(path.absolute()),
        file_name=path.name,
        size_bytes=stat.st_size,
        size_gib=gib(stat.st_size),
        modified_at=datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
        store=store,
        format="OLLAMA_BLOB" if is_ollama_blob(path) else path.suffix.casefold().lstrip(".").upper(),
        family=family,
        parameters=infer_parameters(text),
        quantization=infer_quant(text),
        capabilities=infer_capabilities(text, family),
        package_root=root,
        package_id=f"PKG-{stable_id(root)}",
        logical_key=f"{family or 'unknown'}::{infer_parameters(text) or 'unknown'}::{identity}",
        sha256=sha,
        hash_source=hash_source,
    )


def compute_hashes(artifacts: list[Artifact], mode: str) -> None:
    if mode == "none":
        return
    by_size: dict[int, list[Artifact]] = defaultdict(list)
    for artifact in artifacts:
        by_size[artifact.size_bytes].append(artifact)
    for rows in by_size.values():
        if mode != "all" and len(rows) < 2:
            continue
        for artifact in rows:
            if artifact.sha256:
                continue
            try:
                artifact.sha256 = sha256_file(Path(artifact.path))
                artifact.hash_source = "COMPUTED_SHA256"
            except OSError:
                continue


def exact_duplicate_groups(artifacts: list[Artifact]) -> list[dict]:
    by_sha: dict[str, list[Artifact]] = defaultdict(list)
    for artifact in artifacts:
        if artifact.sha256:
            by_sha[artifact.sha256].append(artifact)
    groups = []
    for sha, rows in sorted(by_sha.items()):
        if len(rows) < 2:
            continue
        group_id = f"DUP-{sha[:16].upper()}"
        for row in rows:
            row.duplicate_group = group_id
            row.duplicate_group_size = len(rows)
        canonical = sorted(
            rows,
            key=lambda row: (
                int(any(token in row.path.casefold() for token in ("\\temp\\", "\\tmp\\", "\\cache\\"))),
                len(row.path),
                row.path.casefold(),
            ),
        )[0]
        groups.append({
            "group_id": group_id,
            "sha256": sha,
            "copies": len(rows),
            "size_bytes_each": rows[0].size_bytes,
            "potential_saving_bytes": rows[0].size_bytes * (len(rows) - 1),
            "canonical_candidate": canonical.path,
            "paths": [row.path for row in rows],
            "action": "REVIEW_EXACT_DUPLICATE",
        })
    return groups


def logical_variant_groups(artifacts: list[Artifact]) -> list[dict]:
    packages: dict[str, list[Artifact]] = defaultdict(list)
    for artifact in artifacts:
        packages[artifact.package_id].append(artifact)

    package_rows = []
    for package_id, members in packages.items():
        families = sorted({m.family for m in members if m.family})
        params = sorted({m.parameters for m in members if m.parameters})
        keys = sorted({m.logical_key for m in members})
        package_rows.append({
            "package_id": package_id,
            "package_root": members[0].package_root,
            "artifact_count": len(members),
            "total_bytes": sum(m.size_bytes for m in members),
            "families": families,
            "parameters": params,
            "quantizations": sorted({m.quantization for m in members if m.quantization}),
            "capabilities": sorted({cap for m in members for cap in m.capabilities}),
            "stores": sorted({m.store for m in members}),
            "formats": sorted({m.format for m in members}),
            "logical_keys": keys,
        })

    by_identity: dict[str, list[dict]] = defaultdict(list)
    for row in package_rows:
        family = row["families"][0] if len(row["families"]) == 1 else "unknown"
        params = row["parameters"][0] if len(row["parameters"]) == 1 else "unknown"
        hint = min(row["logical_keys"], key=len) if row["logical_keys"] else row["package_root"].casefold()
        by_identity[f"{family}::{params}::{hint}"].append(row)

    result = []
    for identity, rows in sorted(by_identity.items()):
        if len(rows) < 2:
            continue
        result.append({
            "logical_group_id": f"LOG-{stable_id(identity)}",
            "identity": identity,
            "packages": rows,
            "action": "KEEP_VARIANTS_UNTIL_BENCHMARK",
            "note": "Logical similarity is not proof of byte duplication.",
        })
    return result


def write_outputs(artifacts: list[Artifact], roots: list[Path], output: Path, hash_mode: str) -> None:
    output.mkdir(parents=True, exist_ok=True)
    exact = exact_duplicate_groups(artifacts)
    logical = logical_variant_groups(artifacts)
    total_bytes = sum(a.size_bytes for a in artifacts)
    saving = sum(row["potential_saving_bytes"] for row in exact)

    payload = {
        "schema_version": "father-model-inventory.v0.1",
        "generated_at": utc_now(),
        "read_only": True,
        "roots": [str(root) for root in roots],
        "hash_mode": hash_mode,
        "counters": {
            "artifacts": len(artifacts),
            "packages": len({a.package_id for a in artifacts}),
            "total_bytes": total_bytes,
            "total_gib": gib(total_bytes),
            "hashed_artifacts": sum(1 for a in artifacts if a.sha256),
            "exact_duplicate_groups": len(exact),
            "potential_exact_duplicate_saving_bytes": saving,
            "potential_exact_duplicate_saving_gib": gib(saving),
            "logical_variant_groups": len(logical),
        },
        "stores": dict(Counter(a.store for a in artifacts)),
        "formats": dict(Counter(a.format for a in artifacts)),
        "families": dict(Counter(a.family or "UNKNOWN" for a in artifacts)),
        "capabilities": dict(Counter(cap for a in artifacts for cap in a.capabilities)),
        "artifacts": [asdict(a) for a in artifacts],
        "exact_duplicate_groups": exact,
        "logical_variant_groups": logical,
    }

    (output / "model_inventory.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "model_dedup_plan.json").write_text(json.dumps({
        "schema_version": "father-model-dedup-plan.v0.1",
        "read_only": True,
        "automatic_delete_allowed": False,
        "exact_duplicate_groups": exact,
        "logical_variant_groups": logical,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    fields = list(Artifact.__dataclass_fields__.keys())
    with (output / "model_inventory.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for artifact in artifacts:
            row = asdict(artifact)
            row["capabilities"] = ";".join(artifact.capabilities)
            writer.writerow(row)

    lines = [
        "# FATHER Local Model Inventory", "",
        "> READ ONLY: no model file was moved, deleted, linked or modified.", "",
        f"- artifacts: **{len(artifacts)}**",
        f"- packages: **{len({a.package_id for a in artifacts})}**",
        f"- total size: **{gib(total_bytes)} GiB**",
        f"- SHA-256 available: **{sum(1 for a in artifacts if a.sha256)}**",
        f"- exact duplicate groups: **{len(exact)}**",
        f"- potential exact duplicate saving: **{gib(saving)} GiB**",
        f"- logical variant groups: **{len(logical)}**", "",
        "## Largest artifacts", "",
        "| # | GiB | Store | Format | Family | Params | Quant | Capabilities | Path |",
        "|---:|---:|---|---|---|---|---|---|---|",
    ]
    for idx, artifact in enumerate(sorted(artifacts, key=lambda a: a.size_bytes, reverse=True)[:100], 1):
        path_text = md_escape(artifact.path)
        caps = ", ".join(artifact.capabilities)
        lines.append(
            f"| {idx} | {artifact.size_gib} | {artifact.store} | {artifact.format} | "
            f"{artifact.family or ''} | {artifact.parameters or ''} | {artifact.quantization or ''} | {caps} | `{path_text}` |"
        )

    lines.extend(["", "## Exact duplicate candidates", ""])
    if not exact:
        lines.append("No exact duplicate group was proven by SHA-256 in this pass.")
    for group in exact:
        lines.extend([
            f"### {group['group_id']} — {group['copies']} copies",
            f"Potential saving: **{gib(group['potential_saving_bytes'])} GiB**",
            f"SHA-256: `{group['sha256']}`",
            f"Canonical candidate for review: `{group['canonical_candidate']}`",
        ])
        lines.extend(f"- `{path}`" for path in group["paths"])
        lines.append("")

    lines.extend(["## Logical variants", "", "Not deletion candidates; benchmark before consolidation.", ""])
    for group in logical[:50]:
        lines.append(f"- `{group['logical_group_id']}` — {len(group['packages'])} packages — `{group['identity']}`")

    (output / "model_inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only inventory of local AI/ML models.")
    parser.add_argument("roots", nargs="*", help="Roots to scan. If omitted on Windows, scans fixed/removable drives.")
    parser.add_argument("--output", default="reports/model_inventory/generated")
    parser.add_argument("--hash", choices=("none", "duplicates", "all"), default="duplicates")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    roots = [Path(value) for value in args.roots] or windows_model_scan_roots()
    print("FATHER Model Inventory — READ ONLY")
    print("roots=" + ";".join(str(root) for root in roots))
    print(f"hash_mode={args.hash}")

    artifacts: list[Artifact] = []
    for idx, path in enumerate(iter_model_files(roots), 1):
        try:
            artifact = build_artifact(path)
        except (OSError, PermissionError, ValueError):
            continue
        artifacts.append(artifact)
        print(f"[{idx}] {artifact.size_gib:>7} GiB  {artifact.store:<18} {artifact.path}")

    if not artifacts:
        print("status=NO_MODELS_FOUND")
        return 2

    print("Computing SHA-256 according to policy...")
    compute_hashes(artifacts, args.hash)
    output = Path(args.output)
    write_outputs(artifacts, roots, output, args.hash)

    duplicate_groups = {a.duplicate_group for a in artifacts if a.duplicate_group}
    print()
    print("status=MODEL_INVENTORY_READY")
    print(f"artifacts={len(artifacts)}")
    print(f"packages={len({a.package_id for a in artifacts})}")
    print(f"total_gib={gib(sum(a.size_bytes for a in artifacts))}")
    print(f"hashed={sum(1 for a in artifacts if a.sha256)}")
    print(f"exact_duplicate_groups={len(duplicate_groups)}")
    print(f"output={output.absolute()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
