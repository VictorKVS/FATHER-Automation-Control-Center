# FATHER Human Agent Studio — Acceptance & Test Plan v0.1

Status: PRE-IMPLEMENTATION TEST BASELINE

## Test philosophy

Tests prove observable capabilities, not document existence. ALINA #001 is the first end-to-end polygon.

## T1 Contracts
- HA-001 HumanAgentPackage validates required identities/profiles/versions.
- HA-002 body/persona/profession/task remain separate references.
- HA-003 adapters reject unsupported contract versions.
- HA-004 asset without provenance/license status is not promotable to approved production asset.

## T2 Presence/runtime
- HA-010 ALINA loads through AvatarRendererAdapter.
- HA-011 ALINA can move between two defined scene anchors.
- HA-012 behavior state maps to visible presentation state.
- HA-013 hide/show preserves task/dialogue state.
- HA-014 renderer failure falls back without destroying workspace state.
- HA-015 reduced-motion mode preserves essential information.

## T3 Character changes
- HA-020 swapping approved avatar/body asset does not change professional identity.
- HA-021 wardrobe change does not mutate knowledge/task state.
- HA-022 package records changed asset/version and provenance.

## T4 Conversation
- HA-030 FLOW completes reversible routine choices without unnecessary questions.
- HA-031 high-impact ambiguity produces a concise clarification.
- HA-032 DETAIL changes only selected dimensions unless dependencies require more.
- HA-033 LOCK survives unrelated subsequent changes.
- HA-034 explicit unlock/supersession is versioned.

## T5 Visual references
- HA-040 image reference can be scoped to an intended aspect/region.
- HA-041 multiple references can have separate aspects/weights/exclusions.
- HA-042 Visual Intent is inspectable before/after execution.
- HA-043 conflicting references are detected rather than silently merged.
- HA-044 changing one reference produces a bounded delta where possible.

## T6 Production compiler
- HA-050 scene intent produces actors/actions/anchors/timing/behavior/assets/tool plan/validation.
- HA-051 generated prompts retain target tool, source intent, version and expected output.
- HA-052 failed tool execution does not erase production intent.
- HA-053 rerun/regeneration history is preserved.

## T7 Voice/face
- HA-060 speech remains available as text.
- HA-061 voice provider can be replaced through adapter.
- HA-062 lip-sync failure degrades gracefully.
- HA-063 animation cannot claim backend work that did not occur.

## T8 Regression/performance
- HA-070 existing ALINA Control Center tests pass.
- HA-071 production build passes.
- HA-072 frame/render/runtime metrics are captured before setting budgets.
- HA-073 fallback activates when measured capability/profile requires it.

## T9 End-to-end acceptance scenario

Input:
- natural-language request for ALINA scene;
- one or more visual references;
- one requested locked characteristic.

Expected:
1. system derives Visual/Scenario Intent;
2. asks only material clarification if required;
3. compiles action/tool plan;
4. executes available adapters;
5. ALINA performs/presents the result;
6. user gives one natural-language correction;
7. system updates bounded affected artifacts;
8. locked characteristic remains;
9. result, prompts/actions, assets, versions and provenance are inspectable;
10. regression tests/build remain green.

## Release evidence

A gate can be marked PASS only with:
- test run identifier;
- commit/version;
- relevant metrics where applicable;
- known gaps;
- visual evidence for visual behavior;
- provenance/license evidence for external assets.
