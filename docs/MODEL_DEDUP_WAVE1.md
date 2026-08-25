# FATHER Model Dedup — Wave 1

## Goal

Reduce physical storage used by byte-identical model copies while preserving every existing Windows path used by old projects.

Wave 1 does **not** delete model paths. It replaces eligible exact duplicates on the same NTFS volume with hardlinks to one canonical inode.

## Evidence boundary

Eligibility requires an existing `model_dedup_plan.json` produced by the inventory scanner. Only `exact_duplicate_groups` with a SHA-256 are considered. Logical similarity, equal names, equal sizes, model family, quantization or folder naming are never sufficient.

## Scope

Wave 1 target allowlist:

- `G:\1\Прежде\KNOWLEDGE_CORE`
- `G:\1\Прежде\MF-KNOWLEDGE-BRAIN`
- `G:\1\Прежде\Sokrat`

Preferred canonical path when the same exact SHA already exists there:

- `G:\1\OSINT_deepseek\data\models`

Explicitly protected from becoming targets:

- all `C:\` paths;
- active `G:\1\OSINT_deepseek` paths;
- the FATHER control-center repo;
- OTUS.

Runtime-owned Ollama, ComfyUI and SD WebUI stores are outside Wave 1.

## Three gates

### 1. PLAN — read only

```powershell
.\RUN_MODEL_DEDUP_WAVE1_PLAN.cmd
```

Expected outputs:

- `reports/model_inventory/consolidation_wave1/wave1_hardlink_plan.md`
- `reports/model_inventory/consolidation_wave1/wave1_hardlink_plan.json`

No file is changed.

### 2. VERIFY — read only

```powershell
.\RUN_MODEL_DEDUP_WAVE1_VERIFY.cmd
```

The verifier recomputes SHA-256 for the selected target and canonical files, checks current size, same-volume eligibility, missing paths and already-linked files. Any mismatch blocks the entire apply stage.

No file is changed.

### 3. APPLY — explicit destructive metadata operation

There is deliberately no one-click APPLY launcher. After PLAN and VERIFY are reviewed, run:

```powershell
python .\scripts\model_dedup_wave1.py --mode apply --confirm APPLY_WAVE1_HARDLINKS
```

Before the first change the tool runs the complete verification gate again. For each target it:

1. renames the duplicate to a temporary sibling backup;
2. creates an NTFS hardlink at the original path pointing to the canonical file;
3. proves both paths resolve to the same file object;
4. removes the temporary duplicate allocation;
5. rolls back the original path if hardlink creation or verification fails.

The original path remains present after a successful operation.

## Important semantics

A hardlink is not a shortcut. Both paths refer to the same bytes on the same filesystem. Removing one hardlink later does not remove the data while another link remains. Modifying bytes through one hardlink would affect every link, so consolidated model files must be treated as immutable weights.

Hardlinks cannot span `C:` and `G:`. Consequently Wave 1 keeps at least one physical copy per volume. Cross-volume runtime consolidation is a later migration stage.

## Fail-closed rules

Apply is refused when:

- the current SHA differs from the inventory SHA;
- a canonical or target path disappeared;
- size changed;
- canonical and target are on different volumes;
- a target escapes the Wave 1 allowlist;
- any preflight action is blocked;
- the explicit confirmation phrase is absent.

## Current production baseline

The latest inventory measured 166 artifacts / 136 packages / 563.589 GiB, with 108 SHA-identified artifacts, 23 exact duplicate groups and 305.279 GiB theoretical duplicate saving across all volumes.

Wave 1 intentionally captures only a conservative same-volume subset. Its exact expected reclaim is generated from the current local dedup plan at runtime; do not hard-code a historical number as an acceptance condition.
