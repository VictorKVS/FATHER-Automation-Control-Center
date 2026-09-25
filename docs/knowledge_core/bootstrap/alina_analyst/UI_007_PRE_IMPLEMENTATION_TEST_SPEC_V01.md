# UI-007 — ALINA Control Center Pre-Implementation Test Specification v0.1

Status: TEST_SPEC_DRAFT
Scope: MVP-00
Upstream: MVP-00; UI-001..UI-006
Production implementation: BLOCKED until this specification is reviewed and required data contracts are identified

## 1. Purpose

Define what must be true before the MVP UI is considered implementation-ready. Tests are designed before production code so the implementation is built against observable behavior rather than visual intuition alone.

## 2. Test-context rule

No metric is valid without its context.

Every measured run records where applicable:
- viewport/profile;
- device/browser/runtime;
- render mode;
- reduced-motion setting;
- connected/demo backend mode;
- dataset/fixture version;
- active object type;
- number of visible/open boards;
- avatar presence/position;
- cold/warm/cache state;
- network/backend condition;
- repetitions/sample size;
- metric definition;
- invalidation conditions.

A result outside its declared context must not be generalized automatically.

## 3. Acceptance classes

P0 — release-blocking MVP behavior.
P1 — important usability/resilience behavior.
P2 — improvement/experiment candidate.

## 4. T-001 Enter Control Center [P0]

Precondition: application available.
Action: open Control Center.
Expected:
- central Work Table is visually identifiable;
- ALINA presence is independent from screens;
- primary navigation is available;
- REAL/DEMO/PLANNED areas can be distinguished when present;
- no fake operational metrics are shown.

Evidence: screenshot/state snapshot + UI state record.

## 5. T-002 Open real canonical object [P0]

Precondition: real vertical-slice object exists.
Action: open source/document object.
Expected:
- Work Table primary_context references canonical object ID;
- title/type/version/status match backend contract;
- UI does not create a second truth object;
- object status is REAL.

Evidence: UI state + backend/canonical reference comparison.

## 6. T-003 Board origin and lifecycle [P0]

Action: from primary object open Knowledge/Evidence board; pin; minimize; restore; close.
Expected:
- board retains object_ref, origin and relation_to_primary;
- state transitions follow UI-003;
- closing board does not mutate canonical data;
- restore returns same referenced object/version.

## 7. T-004 Promote board / deterministic return [P0]

Action: promote a related board to Work Table, then Back.
Expected:
- previous primary context is preserved;
- promoted object becomes primary;
- Back restores exact previous primary context and relevant board state;
- incompatible boards are marked stale/context-changed rather than silently reinterpreted.

## 8. T-005 Reverse provenance [P0]

Path:
Knowledge -> Evidence -> Fragment -> Document Version -> Original Source -> Back.

Expected:
- canonical IDs remain traceable;
- semantic types remain unchanged;
- missing stage is explicit;
- historical version is preserved;
- Back returns through the actual visited context.

## 9. T-006 Missing evidence [P0]

Fixture: knowledge object with no valid evidence relation.
Expected:
- GAP/MISSING/UNAVAILABLE is shown;
- no citation/source/fragment is fabricated;
- user can create/follow future Research Order path only if capability exists, otherwise PLANNED.

## 10. T-007 Contradictory evidence [P0]

Fixture: supporting and contradicting evidence.
Expected:
- both branches visible on demand;
- UI does not auto-resolve for cleanliness;
- resolution state is explicit/UNKNOWN where unresolved.

## 11. T-008 REAL vs DEMO boundary [P0]

Fixture: real object and demo/planned module in same workspace.
Expected:
- statuses remain distinguishable through navigation/promotion;
- DEMO board cannot become visually indistinguishable from REAL after promotion;
- demo IDs/data never masquerade as canonical production objects.

## 12. T-009 Avatar collapse and restore [P0]

Actions:
FULL -> COMPACT/FACE -> EYES -> STATUS/HIDDEN -> restore.
Expected:
- analytical task continues;
- primary context unchanged;
- prior user position/presence preference recoverable;
- hidden avatar does not remove status access required by the UI.

## 13. T-010 Avatar reposition / board collision [P1]

Scenario: board occupies avatar region.
Expected:
- critical content remains readable;
- user preference is retained when possible;
- automatic move/collapse follows explicit policy and can be overridden;
- task state is unchanged.

## 14. T-011 Avatar render failure [P0]

Inject/render capability failure.
Expected fallback:
FULL_3D -> LIGHT_3D/2D -> STATIC/EYES/STATUS -> NO_AVATAR.
Core Work Table/Boards/Knowledge navigation remain usable.
Failure is observable; analytical state is not falsely changed.

## 15. T-012 Reduced motion [P1]

Enable reduced motion.
Expected:
- all essential transitions remain understandable and usable;
- no required information is encoded only in animation;
- task/provenance flow remains equivalent.

## 16. T-013 Workspace reload/restore [P0]

Prepare:
active real object + avatar state + pinned/minimized boards + focus state.
Reload/reopen.
Expected:
- declared persistent state restores;
- unavailable/stale object is shown explicitly if backend changed;
- system does not silently substitute another version/object.

## 17. T-014 Agent Stack structured drill-down [P0]

Action:
ALINA Stack -> L3 Knowledge (or selected real layer) -> object -> Evidence -> Source.
Expected:
- Stack is rendered from structured data;
- avatar and Stack are independent;
- at least one real layer path reaches canonical data;
- PLANNED layers remain explicitly PLANNED.

## 18. T-015 Focus Mode [P0]

Action: enter long-session Focus Mode on document/code/analysis object.
Expected:
- Work Table receives dominant readable area;
- side domains/nonessential boards recede;
- ALINA can remain EYES/MINIMAL/HIDDEN;
- essential status/provenance access remains available;
- leaving Focus restores prior layout.

Usability duration thresholds are not invented here; pilot session protocol will define them.

## 19. T-016 Board overload behavior [P1]

Request boards beyond comfortable visible capacity.
Expected:
- UI stacks/minimizes/organizes rather than indefinitely shrinking primary content;
- Work Table remains primary;
- no hard maximum is claimed until usability evidence establishes it.

## 20. T-017 Backend temporary outage [P0]

During active real-object work, make canonical backend unavailable.
Expected:
- existing screen state is not relabeled as current truth;
- affected data marked unavailable/stale as appropriate;
- DEMO data is not substituted automatically;
- avatar shell failure state does not conceal backend failure.

## 21. T-018 Source/version change during session [P1]

Scenario: source gains a newer version/currentness transition.
Expected:
- historical object remains linked to original version;
- UI surfaces change/currentness state;
- no silent provenance rewrite;
- impact/recheck may be PLANNED if backend not implemented.

## 22. T-019 Agent avatar independence [P1]

Change avatar visual asset/theme/version.
Expected:
- specialist_id and Agent Stack canonical refs unchanged;
- professional knowledge/capability does not change due to avatar appearance;
- fallback avatar remains able to identify specialist.

## 23. T-020 Accessibility without visual effects [P1]

Scenario: reduced motion + low/no 3D + keyboard-oriented navigation where supported.
Expected:
- primary workflow remains reachable;
- focus is visible;
- statuses not encoded only by color;
- provenance drill-down and Back remain usable.

## 24. T-021 MVP end-to-end golden path [P0]

```text
OPEN CONTROL CENTER
-> OPEN REAL DOCUMENT
-> OPEN KNOWLEDGE BOARD
-> OPEN EVIDENCE
-> OPEN FRAGMENT/VERSION/SOURCE
-> RETURN TO DOCUMENT
-> OPEN ALINA AGENT STACK
-> INSPECT REAL LAYER
-> RETURN
-> ENTER FOCUS MODE
-> COLLAPSE ALINA
-> RELOAD/RESTORE WORKSPACE
```

Pass requires the same canonical object lineage and user context to survive the path without REAL/DEMO confusion.

## 25. T-022 Pleasant-work pilot [P1]

This is a human usability test, not a synthetic benchmark.

Protocol to define before execution:
- representative task;
- representative session length;
- interruptions/context switches;
- user-reported obstruction/friction;
- unnecessary navigation count;
- moments where avatar/boards obscure content;
- ability to recover context;
- qualitative comfort/aesthetic feedback.

Do not invent a universal "pleasantness score". Store observations and task-specific metrics.

## 26. T-023 Performance context profiles [P1]

Profiles to specify before implementation benchmark:
A normal workspace;
B document + 2 boards + compact ALINA;
C Agent Stack expanded;
D Focus Mode;
E degraded/no-3D mode.

Candidate metrics: interaction latency, frame/render stability where applicable, memory/CPU/GPU use, initial load, state restore time. Thresholds require target hardware/browser context and are not set yet.

## 27. Test evidence contract

Each executed test should produce:
- test_id;
- implementation/component versions;
- test_context_id;
- input/fixture refs;
- expected result;
- actual result;
- PASS/FAIL/BLOCKED;
- evidence refs/screenshots/logs;
- defects/gaps;
- timestamp;
- reviewer where applicable.

## 28. Implementation-ready gate

MVP production implementation may start when:
1. P0 tests are accepted as specifications;
2. the real vertical-slice backend/data contract is identified;
3. fixture/demo contract is separate from real data;
4. UI state model is implementable from UI-001..006;
5. unresolved P0 ambiguity is converted to explicit GAP/decision;
6. representative viewport/runtime profiles are chosen;
7. first implementation plan maps components to tests.

## 29. Next step

UI-008 defines workload/performance/accessibility profiles and identifies representative target environments. In parallel, the real vertical-slice data contract must be located/defined. Then UI-009 defines A/B experiments; after those gates UI-010 can become the implementation plan.
