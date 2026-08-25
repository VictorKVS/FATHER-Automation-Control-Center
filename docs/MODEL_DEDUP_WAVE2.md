# FATHER Model Dedup — Wave 2A Image Models

Wave 2A is a conservative, read-only planning and verification stage for exact SHA-256 duplicate image-generation assets.

## Scope

Eligible target trees are limited to old/archival image stacks under `G:\1\Прежде\1_izobraznie\AI`:

- nested old ComfyUI trees;
- `AI\models\StableDiffusion` duplicate library;
- `stable-diffusion-webui-forge_old`;
- `stable-diffusion-webui-OLD`.

Current standalone `G:\1\Прежде\1_izobraznie\ComfyUI` and MindForge resource model trees are explicitly protected from targeting in Wave 2A.

## Safety invariants

1. Exact SHA-256 groups only.
2. Never consolidate by file name, size, family, or logical similarity alone.
3. PLAN and VERIFY are read-only.
4. No APPLY mode exists in this Wave 2A tool.
5. Canonical survivor and target must both be on `G:` before a future hardlink operation can even be proposed.
6. Existing model paths are intended to remain unchanged in any later apply stage.
7. Runtime-owned C: stores and active OSINT paths are outside this wave.

## Commands

```cmd
RUN_MODEL_DEDUP_WAVE2_PLAN.cmd
RUN_MODEL_DEDUP_WAVE2_VERIFY.cmd
```

Generated reports:

```text
reports\model_inventory\consolidation_wave2\wave2_hardlink_plan.md
reports\model_inventory\consolidation_wave2\wave2_hardlink_plan.json
```

A future APPLY stage must be implemented separately only after the generated plan is reviewed and verification reports zero blocked actions.
