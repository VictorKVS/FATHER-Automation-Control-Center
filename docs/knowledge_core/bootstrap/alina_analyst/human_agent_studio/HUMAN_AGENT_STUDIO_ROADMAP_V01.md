# FATHER Human Agent Studio — Development Roadmap v0.1

Status: EXECUTION ROADMAP

## Gate 0 — Documentation baseline
Deliver README, Technical Specification, Architecture, Roadmap and Acceptance/Test Plan. Record journal entry. No implementation before gate is complete.

## Gate 1 — ALINA 3D runtime
Continue existing P1-P7 chain:
- verify P1 world CI;
- P2 HumanAgentProfile + AvatarRendererAdapter + temporary provenance-cleared avatar;
- P3 locomotion/turn/look;
- P4 workspace/fullscreen transition;
- P5 fallback/reduced motion/hide-show continuity;
- P6 voice-preparation contracts;
- P7 prototype visual/performance review.

Exit: ALINA #001 demonstrably inhabits the Control Center without coupling brain to body.

## Gate 2 — Studio Core
Implement versioned HumanAgentPackage schemas, manifests, asset provenance, adapter registry and package validation.

Exit: ALINA #001 can be reconstructed from package references.

## Gate 3 — Character Studio MVP
Body/face/hair/material/wardrobe profile editing, presets, preview and asset swapping. Prefer mature reusable components; no premature custom body engine.

Exit: visible ALINA presentation can be changed without professional-state changes.

## Gate 4 — Motion & Behavior
Semantic action library, animation graph, retargeting, gaze, gestures, IK where justified, behavior-state mapping.

Exit: scenario actions drive visible behavior reproducibly.

## Gate 5 — Face + Voice
Voice profile, replaceable TTS/STT, viseme/lip-sync, expressions, blink/gaze and synchronized speaking behavior.

Exit: ALINA can speak with synchronized presentation while text remains available.

## Gate 6 — Live Collaboration
Implement FLOW/DETAIL/LOCK, assumption ledger, selective clarification and delta-update planning.

Exit: a user can refine ALINA by ordinary conversation without manually editing prompts.

## Gate 7 — Visual Reference Intelligence
Reference Board, image/region input, structured Visual Intent, weighting/exclusions, comparison and provenance.

Exit: reference image + natural-language request produces an inspectable intent package and a controlled Studio change.

## Gate 8 — Scenario Production Compiler
Scenario → scenes → beats → actions → assets → prompts/tool instructions → validation → preview.

Exit: a short natural-language scene can be compiled and executed through available adapters.

## Gate 9 — Scene / World Studio
Environment, objects, lights, cameras, anchors and interaction points.

## Gate 10 — Web Experience Studio
Visual intent → design decisions → components/spatial UI → preview/test loop.

## Gate 11 — Game Experience Lab
Add runtime adapters and learning polygons for controller, camera, collision, physics, navigation, NPC/game AI, VFX and action mechanics. Evaluate Godot/Unreal rather than rebuilding mature engine infrastructure by default.

## Gate 12 — Specialist Factory
Build/evaluate Interactive 3D / Human Agent & Game Experience Engineer from evidence-backed knowledge, documentation, books, competitor research and FATHER polygon telemetry.

Exit: specialist can produce Human Agent #002 with materially less manual specification than ALINA #001.

## Continuous rules

Every gate:
PASSPORT/REQUIREMENTS → SCHEME → TEST SPEC → IMPLEMENTATION → TEST RUN → EVIDENCE/METRICS → RELEASE/REWORK.

Every substantive action is journaled.

No production performance claim without telemetry.
No external asset without provenance/license state.
No specialist competence claim without independent evaluation.
