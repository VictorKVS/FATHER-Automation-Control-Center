# UI-009 — ALINA Control Center A/B Experiment Plan v0.1

Status: EXPERIMENT_PLAN_DRAFT
Scope: MVP-00
Upstream: UI-006 Wireframes; UI-007 Tests; UI-008 Test Context Profiles
Implementation: experiments are hooks/specifications; full experimentation platform is outside MVP

## 1. Purpose

Define which uncertain UX choices should be tested rather than frozen by taste. The goal is not to maximize visual spectacle; it is to find configurations that improve comfortable, understandable, low-friction analytical work.

## 2. Experiment rule

Every experiment must declare:
HYPOTHESIS -> VARIANTS -> TEST_CONTEXT -> TASK -> METRICS/OBSERVATIONS -> GUARDRAILS -> RESULT -> DECISION.

A local visual win cannot be promoted if it causes unacceptable downstream regression.

## 3. EXP-001 ALINA default presence

Question: what default ALINA presence best balances companionship/identity with unobstructed work?

A: FULL/large presence on entry.
B: COMPACT/FACE presence on entry.
C: context-adaptive presence with deterministic rules.

Contexts: W0 Idle Room, W1 Document Focus, W2 Normal Analysis.

Observe:
- time until first useful action;
- obstruction/reposition events;
- voluntary collapse/expand actions;
- user preference/comfort;
- task completion friction.

Guardrail: ALINA must remain recognizable and status-accessible.

## 4. EXP-002 ALINA default position

A: CENTER_REAR.
B: SIDE_DOCK_RIGHT.
C: context-adaptive CENTER_REAR -> side dock in Focus.

Observe: content obstruction, eye travel, manual moves, perceived presence, ability to identify current state.

## 5. EXP-003 Board density

A: maximum 2 visible related boards.
B: maximum 3 visible related boards.
C: adaptive visible count with overflow stack/minimize.

Do not assume more boards means more productivity.

Observe: context loss, board hunting, overlap, Work Table readable area, unnecessary close/minimize actions.

## 6. EXP-004 Provenance disclosure depth

A: compact provenance indicator -> click for evidence.
B: evidence summary always visible.
C: provenance rail visible in analysis modes only.

Observe: trust inspection frequency, visual clutter, time to source, accidental loss of focus.

Guardrail: provenance must always remain reachable.

## 7. EXP-005 Agent Stack default form

A: compact vertical spine.
B: small labeled layer cards.
C: identity card + active layer only, expand on demand.

Observe: comprehension of specialist structure, time to desired layer, space cost, visual competition with Work Table.

## 8. EXP-006 Focus Mode ALINA presence

A: EYES.
B: STATUS only.
C: HIDDEN with summon control.

Observe during representative long-session task:
- distraction/obstruction;
- sense of system availability;
- summon frequency;
- preference;
- task/context continuity.

## 9. EXP-007 Visual intensity

A: restrained luminous geometry.
B: richer glow/depth effects.
C: low-effects technical mode.

Observe: readability, fatigue, perceived polish, visual distraction, render/resource cost.

Guardrails: text/data readability and accessibility cannot regress.

## 10. EXP-008 Board opening behavior

A: board appears nearest relation origin.
B: fixed board slots.
C: adaptive placement respecting protected Work Table/ALINA regions.

Observe: predictability, collisions, manual reposition, spatial memory.

## 11. EXP-009 Return/back model

A: browser-like context history.
B: visible breadcrumb/context trail.
C: hybrid history + compact breadcrumb.

Observe: successful return to prior object, navigation errors, user understanding of current context.

## 12. EXP-010 Future specialist presence

Not MVP release-blocking.

A: specialist appears as avatar + board.
B: avatar appears only while directly interacting.
C: board first, avatar on explicit summon.

Use later when Lawyer/InfoSec/etc have real implementations. Do not test with fake capability claims.

## 13. Metrics and observations

Prefer task-specific evidence:
- task completion success;
- navigation count;
- backtracking/errors;
- obstruction events;
- manual layout corrections;
- time to evidence/source;
- state recovery success;
- resource/render measurements;
- qualitative comfort and preference.

No universal UX score.

## 14. Experiment eligibility gate

Run comparison only if:
- variants satisfy same required contract;
- task/workload is representative;
- REAL/DEMO state is equivalent between variants;
- test context is recorded;
- metric definitions are fixed before run;
- sample/observations are sufficient for the decision being made;
- accessibility/fallback guardrails are checked.

For single-user early MVP, repeated within-subject trials are acceptable as exploratory evidence, but must not be presented as population-level proof.

## 15. Promotion states

PROPOSED
-> READY_FOR_TRIAL
-> RUNNING
-> INCONCLUSIVE | REJECTED | PROMOTION_CANDIDATE
-> REGRESSION_CHECK
-> ACCEPTED
-> SUPERSEDED.

Every accepted change records context and evidence. A later context may justify another variant.

## 16. MVP minimum experiment hooks

The implementation should make these choices configurable without architectural rewrite:
- avatar presence default;
- avatar default position;
- board visible-count/placement policy;
- provenance disclosure mode;
- Agent Stack default form;
- Focus Mode avatar behavior;
- visual-effects level.

A full experiment service/dashboard is not required in MVP.

## 17. Exit gate

UI-009 is sufficient for implementation planning when:
- major uncertain UX choices have explicit hypotheses/variants;
- metrics are context-bound;
- guardrails protect readability/truth/accessibility;
- configuration hooks are identified;
- no experiment result is invented before implementation/testing.

## 18. Next step

UI-010 Implementation Plan may now be drafted, but production code remains gated on identifying/defining the real vertical-slice data contract:
Source/Document -> Version/Fragment -> Evidence -> Knowledge Object.
