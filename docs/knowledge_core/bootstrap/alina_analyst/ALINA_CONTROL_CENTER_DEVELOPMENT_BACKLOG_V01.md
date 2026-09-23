# ALINA Control Center — Development Backlog v0.1

Status: ACTIVE
Source: accepted Control Center Passport + Technical Brief requirements.
Rule: backlog entry does not authorize production code until analysis/notation/test gates pass.

| ID | Capability | Current maturity | Next gate |
|---|---|---|---|
| UI-001 | Spatial command-room notation | NOTATION_DRAFT | REVIEW -> NOTATED |
| UI-002 | ALINA avatar position/collapse/state machine | NOTATION_DRAFT | REVIEW -> NOTATED |
| UI-003 | Central work table + deployable boards | PASSPORTED | NOTATED |
| UI-004 | Layered Agent Stack | PASSPORTED | NOTATED |
| UI-005 | Knowledge Core + provenance interaction | PASSPORTED | NOTATED |
| UI-006 | Full/focused/eyes/minimal wireframes | IDEA_CAPTURED | PASSPORTED/NOTATED |
| UI-007 | Pre-implementation UI test specification | IDEA_CAPTURED | TEST_SPECIFIED |
| UI-008 | Performance/accessibility/fallback profiles | IDEA_CAPTURED | TEST_SPECIFIED |
| UI-009 | A/B experiment plan | IDEA_CAPTURED | TEST_SPECIFIED |
| UI-010 | Production implementation plan | BLOCKED | UI-001..009 reviewed |

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
