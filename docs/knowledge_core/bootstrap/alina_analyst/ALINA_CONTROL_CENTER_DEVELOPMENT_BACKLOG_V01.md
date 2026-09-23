# ALINA Control Center — Development Backlog v0.1

Status: ACTIVE
Source: accepted Control Center Passport + Technical Brief requirements.
Rule: backlog entry does not authorize production code until analysis/notation/test gates pass.

| ID | Capability | Current maturity | Next gate |
|---|---|---|---|
| UI-001 | Spatial command-room notation | NOTATION_DRAFT | REVIEW -> NOTATED |
| UI-002 | ALINA avatar position/collapse/state machine | NOTATION_DRAFT | REVIEW -> NOTATED |
| UI-003 | Central work table + deployable boards | NOTATION_DRAFT | REVIEW -> NOTATED |
| UI-004 | Layered Agent Stack | NOTATION_DRAFT | REVIEW -> NOTATED |
| UI-005 | Knowledge Core + provenance interaction | NOTATION_DRAFT | REVIEW -> NOTATED |
| UI-006 | Full/focused/eyes/minimal wireframes | WIREFRAME_DRAFT | REVIEW -> WIREFRAME_BASELINE |
| UI-007 | Pre-implementation UI test specification | TEST_SPEC_DRAFT | REVIEW -> TEST_SPECIFIED |
| UI-008 | Performance/accessibility/fallback profiles | PROFILE_DRAFT | REVIEW -> PROFILE_BASELINE |
| UI-009 | A/B experiment plan | EXPERIMENT_PLAN_DRAFT | REVIEW -> EXPERIMENT_BASELINE |
| UI-010 | Production implementation plan | IMPLEMENTATION_PLAN_DRAFT | RECONNAISSANCE + DATA CONTRACT -> IMPLEMENTATION_READY |

## Definition of Implementation Ready

A capability is IMPLEMENTATION_READY only when:
1. purpose/boundaries/contracts are described;
2. notation matches the passport;
3. pre-implementation tests and expected outcomes exist;
4. metric/test context is valid;
5. dependencies/fallbacks are known;
6. significant decisions have FDR/trace;
7. review gate passes.

## Reference visual intent

The user-supplied images establish visual intent for:
- synthetic luminous ALINA face/eyes;
- volumetric/holographic ALINA presence;
- science-fiction command room;
- stacked/layered intelligence presentation.

They are design references, not assets to copy and not proof of system capabilities.

## Next work item

Start UI-001 and UI-002 together at the notation boundary because spatial zones and avatar movement/collapse constrain one another. Do not write production UI code yet.


## Delivery horizons

### MVP shell
Deliver a beautiful, comfortable, usable command-room workspace with a limited real vertical slice. Prefer simple replaceable implementations over prematurely building the full ALINA super-project.

### Super-project
Continue the full ALINA analytical/knowledge/specialist architecture under the existing evidence-first development process.

### Future shared capability
Extract the ALINA avatar contract into a FATHER Employee Avatar System so future specialists/agents can have distinct but predictable presences.


## MVP scope gate

MVP-00 is now defined in `MVP_00_CONTROL_CENTER_SCOPE_V01.md`. UI-003 onward must distinguish MUST WORK, DEMO/PLANNED and SUPER-PROJECT capabilities. The first implementation must include a narrow real Source -> Knowledge -> Evidence/Provenance vertical slice and must not be demo-only.


## M1 Runnable Baseline — 2026-09-23

Status: **VALIDATED_BASELINE**

Evidence: GitHub Actions run `35853674078` completed successfully. Install, all 14 tests, TypeScript compilation, and Vite production build passed. Build output: 19 modules transformed; index.html 0.41 kB (gzip 0.30 kB), CSS 2.76 kB (gzip 1.18 kB), JS 225.00 kB (gzip 70.73 kB); Vite build phase 165 ms. These metrics are specific to that CI run and are not workstation performance claims.

M1 scope remains DEMO-only and backend-independent. This baseline does not claim Knowledge Core connectivity, production readiness, final 3D ALINA rendering, or M2 completion.


## M1.1 Visual Architecture — 2026-09-23

Status: **PRE_IMPLEMENTATION_BASELINE**

Trigger: first local browser review of validated M1 exposed UI-GAP-001: the shell is technically valid but spatially too schematic for the target ALINA Control Center experience.

Pre-code artifacts now exist: M1.1 Visual Architecture Passport, M1.1 Spatial Scheme, and M1.1 Visual & Interaction Test Specification. Target hierarchy is Information Wall -> ALINA -> Work Table -> User. M1.1 must preserve M1 truth/fallback/state behavior and remain 2D/2.5D and renderer-replaceable; it does not authorize a final 3D engine or imply Knowledge Core connectivity.

Next gate: **REVIEW -> IMPLEMENTATION_READY**, then implement the visual composition and execute V01-V14 plus existing M1 regression tests.
