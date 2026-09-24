# FATHER Human Agent Studio — Architecture v0.1

Status: PRE-IMPLEMENTATION BASELINE

## System boundary

FATHER KNOWLEDGE CORE / ALINA BRAIN
→ Presentation Model
→ Human Agent Orchestrator
→ HumanAgentProfile
→ Production / Presence Controllers
→ Adapter Layer
→ Web / DCC / Voice / Generation / Game runtimes

The renderer never owns canonical professional knowledge or task truth.

## Logical architecture

```text
USER
 ├─ conversation
 ├─ image/screenshot/sketch
 ├─ selected region
 └─ later: video/time range
          │
          ▼
SCENARIO WRITER ──► MULTIMODAL INTENT
                         │
                         ▼
        3D / HUMAN AGENT / GAME ENGINEER
                         │
                         ▼
                PRODUCTION COMPILER
          ┌──────────────┼───────────────┐
          ▼              ▼               ▼
     HumanAgent       ScenePlan       Prompt/ToolPlan
          │              │               │
          └──────────────┼───────────────┘
                         ▼
                    ADAPTER LAYER
       ┌─────────┬───────┼────────┬─────────┐
       ▼         ▼       ▼        ▼         ▼
     WEB/3D    BLENDER  VOICE   GEN-AI   GAME RUNTIME
       │
       ▼
   PREVIEW / RESULT
       │
       ▼
 USER DELTA FEEDBACK
       │
       └────────► VERSION / VALIDATION LOOP
```

## HumanAgentPackage

```text
HumanAgentPackage
├─ manifest
├─ identity_ref
├─ CharacterProfile
│  ├─ BodyProfile
│  ├─ FaceProfile
│  └─ WardrobeProfile
├─ RigProfile
├─ AnimationProfile
├─ VoiceProfile
├─ PersonalityProfile
├─ InteractionProfile
├─ ProfessionBinding
├─ AssetManifest[]
├─ RuntimeCompatibility[]
├─ TestProfile
└─ provenance/change_history
```

## Separation invariants

BODY != PERSONA != PROFESSIONAL KNOWLEDGE != TASK STATE.

PROMPT != SOURCE OF TRUTH.

RENDERER STATE != BACKEND EXECUTION STATE.

REFERENCE IMAGE != REQUIREMENT until interpreted and accepted as Visual Intent.

EXTERNAL ASSET != TRUSTED until provenance/license state is recorded.

## Visual Reference Intelligence

ReferenceAsset
→ region/selection
→ feature extraction/description
→ aspect classification
→ VisualIntentItem[]
→ weights/exclusions
→ conflict detection
→ accepted intent
→ production requirements.

VisualIntentItem types initially:
UI_PATTERN, TYPOGRAPHY, COMPOSITION, GEOMETRY, MATERIAL, LIGHTING, COLOR_RELATION, OBJECT_FORM, CHARACTER_STYLE, WARDROBE, MOTION_REFERENCE, MOOD.

## Conversation model

LIVE mode is the human-facing default.
Inspector is a projection over the same versioned production state.

FLOW → infer reversible details.
DETAIL → expose/discuss selected dimension.
LOCK → convert approved choice to a constraint.
A later user instruction may explicitly unlock/supersede it.

## Runtime adapters

Initial:
- AvatarRendererAdapter
- AssetLoaderAdapter
- AnimationAdapter
- VoiceAdapter
- LipSyncAdapter

Later:
- ImageGenerationAdapter
- VideoReferenceAdapter
- DCCAdapter
- PhysicsAdapter
- GameRuntimeAdapter.

Adapters translate FATHER semantics; they do not redefine them.

## ALINA #001

ALINA is the first integration instance:
ALINA Brain/Knowledge/Task
→ ALINA HumanAgentProfile
→ Presence Controller
→ AvatarRendererAdapter
→ Web 3D body
while Workspaces consume Presentation Model independently.

This preserves Workspace First / ALINA Everywhere / Avatar Optional.
