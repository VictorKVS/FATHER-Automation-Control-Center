# ALINA 3D PRESENCE PROTOTYPE PASSPORT v0.1

Status: PRE_IMPLEMENTATION_BASELINE
Scope: ALINA Control Center / replaceable 3D presence layer
Parent principle: Workspace First, ALINA Everywhere, Avatar Optional

## 1. Problem

The M1 shell proved UI contracts but the visual ALINA presence is schematic. The target experience is a game-like embodied analyst that can move, speak and present information while dense engineering workspaces remain primary and can occupy the full screen.

## 2. Objective

Prove a replaceable browser 3D presence layer in which ALINA can inhabit a small control-room scene, move between a Work Table and Information Wall, reflect real presentation states, and yield the screen to Knowledge/Graph/Evidence/RAG workspaces without breaking dialogue or task continuity.

## 3. Non-goals

- final photorealistic digital human;
- production voice provider;
- production lip-sync;
- final environment/art direction;
- autonomous navigation in arbitrary worlds;
- coupling ALINA reasoning to the renderer;
- replacing canonical FATHER state with scene state.

## 4. Prototype scene

Minimum scene:
- one room;
- one humanoid ALINA avatar;
- Work Table anchor;
- Information Wall anchor;
- Knowledge, Graph and Evidence panel anchors;
- user camera;
- full-screen workspace overlay;
- non-avatar status/dialogue channel.

## 5. Presence modes

FULL_BODY — avatar visible in scene.
COMPACT — reduced visual presence.
VOICE_ONLY — no avatar rendering; voice/text/session continue.
HIDDEN — workspace only; text/task state remain.
STATUS_ONLY — minimal execution/status indicator.

Presence mode is presentation state, not ALINA cognitive state.

## 6. Behavioral states

IDLE
LISTENING
THINKING
WALKING
PRESENTING
SPEAKING
WARNING
WAITING

A behavior state may influence animation, pose, gaze and camera suggestions but MUST NOT fabricate backend execution or telemetry.

## 7. First interactions

- spawn ALINA at Work Table;
- idle animation;
- command move_to_information_wall;
- walk/turn to target;
- present Knowledge/Graph/Evidence panel;
- expand selected panel to full-screen workspace;
- hide avatar while retaining dialogue/status;
- restore scene and ALINA context;
- reduced-motion fallback.

## 8. Architecture boundary

ALINA Backend / FATHER state
-> Presentation Model
-> Presence Controller
-> AvatarRendererAdapter
-> 3D engine/avatar

Workspace panels consume Presentation Model directly and never depend on avatar internals.

Renderer failure must degrade to STATUS_ONLY or workspace-only mode.

## 9. Technology direction

Prototype direction: existing React/Vite shell + isolated Three.js/R3F-compatible 3D layer + VRM-capable avatar adapter.

Reference inspiration may be taken from game/avatar projects, but code/assets are reused only after license-level review. No third-party character asset is canonical.

## 10. Truth and safety

- scene animation cannot claim work that backend has not reported;
- DEMO/PLANNED/UNAVAILABLE/UNKNOWN truth states remain visible;
- no secret, PII, private learner data or local absolute path in public fixtures;
- essential information cannot exist only in animation/audio/color.

## 11. Performance/fallback

The 3D layer is optional. Performance degradation must allow transition FULL_BODY -> COMPACT -> STATUS_ONLY/HIDDEN without loss of task operation.

No numeric performance threshold is invented in v0.1; baseline measurements will be collected from the first executable prototype before setting budgets.

## 12. Acceptance gate

Before implementation:
Passport -> Scene/State Notation -> Test Specification -> Review.

Prototype release requires:
- deterministic state transitions for test fixtures;
- avatar can move between two anchors;
- full-screen panel transition works;
- avatar can be hidden without losing dialogue/task state;
- renderer failure fallback works;
- original M1 truth/state tests remain green;
- build passes;
- screenshot/video/manual review records the spatial result.

## 13. Next artifact

ALINA_3D_SCENE_AND_STATE_NOTATION_V01.md
