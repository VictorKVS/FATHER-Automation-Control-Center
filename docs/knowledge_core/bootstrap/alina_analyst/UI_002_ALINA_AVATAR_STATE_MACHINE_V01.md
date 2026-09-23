# UI-002 — ALINA Avatar State Machine v0.1

Status: NOTATION_DRAFT
Upstream: UI-001 Spatial Notation; Control Center Technical Brief
Implementation: BLOCKED until test specification and review

## 1. Purpose

Define ALINA's visual presence as a stateful, movable, replaceable UI component without coupling analytical correctness to 3D rendering.

The avatar has independent state dimensions. A visual state must not be confused with an analytical state.

## 2. State dimensions

ALINA_AVATAR_STATE =
PRESENCE_MODE × POSITION_MODE × ANALYTICAL_STATE × INTERACTION_STATE × RENDER_MODE.

This avoids one giant state list and allows combinations to be tested explicitly.

## 3. Presence mode

P0 FULL_3D — full-bodied volumetric analyst.
P1 COMPACT_3D — reduced volumetric presence.
P2 FACE — face/head presence.
P3 EYES — recognizable eyes/status strip.
P4 STATUS — minimal live indicator.
P5 HIDDEN — avatar not visible; status remains accessible elsewhere.

Normal collapse:
FULL_3D -> COMPACT_3D -> FACE -> EYES -> STATUS -> HIDDEN.
Expansion is reversible unless a capability/failure constraint prevents the requested render mode.

## 4. Position mode

A0 CENTER_REAR — default behind/near central table.
A1 TOP_LEFT
A2 TOP_RIGHT
A3 BOTTOM_LEFT
A4 BOTTOM_RIGHT
A5 SIDE_DOCK_LEFT
A6 SIDE_DOCK_RIGHT
A7 FLOATING_CONSTRAINED — candidate; enabled only after usability tests.

Position and presence are orthogonal: EYES may be TOP_RIGHT while FULL_3D may be CENTER_REAR.

## 5. Analytical state

S0 IDLE
S1 LISTENING
S2 ANALYZING
S3 RESEARCHING
S4 WAITING_FOR_EVIDENCE
S5 GAP_DETECTED
S6 TESTING
S7 WARNING
S8 COMPLETE
S9 DEGRADED
S10 ERROR

These states must originate from real runtime/workflow state. Visual treatment is downstream of state, never its source of truth.

## 6. Interaction state

I0 PASSIVE
I1 ADDRESSING_USER
I2 INDICATING_OBJECT
I3 FOLLOWING_BOARD
I4 REPOSITION_REQUESTED
I5 USER_DRAGGING
I6 DOCKING
I7 COLLAPSING
I8 EXPANDING

Future gesture/gaze/voice states require separate evidence, privacy and accessibility analysis.

## 7. Render mode

R0 FULL_RENDER
R1 LIGHT_3D
R2 TWO_D
R3 STATIC
R4 STATUS_ONLY
R5 NO_AVATAR

Fallback:
FULL_RENDER -> LIGHT_3D -> TWO_D -> STATIC -> STATUS_ONLY -> NO_AVATAR.
Fallback changes presentation capability, not the underlying analytical task state.

## 8. Transition rules

User may request position or presence changes at any time unless a modal safety/critical interaction explicitly blocks it.

Critical board collision:
BOARD_REQUEST -> OCCUPANCY_CHECK -> no conflict: deploy.
Conflict -> preserve readable layout if possible -> suggest avatar move/collapse -> user/policy decision -> deploy.

Render failure:
render_error -> downgrade render mode -> preserve presence intent as closely as possible -> log degradation -> continue core workspace.

Task state change:
runtime event -> analytical state update -> mapped visual cue -> UI event log.
No invented percentage/telemetry may be generated from avatar animation.

## 9. Memory / restoration

Candidate persistent state:
- preferred_position_mode;
- last_visible_presence_mode;
- previous_position_before_auto_layout;
- reduced_motion;
- avatar_enabled;
- render_capability;
- last_user_override;
- layout_policy_version.

On restore, user preference wins unless incompatible with current viewport/capability; any automatic fallback must be explainable.

## 10. Minimal state diagram

```text
                 +----------------------+
                 |      FULL_3D         |
                 +----------+-----------+
                            |
                         collapse
                            v
 COMPACT_3D -> FACE -> EYES -> STATUS -> HIDDEN
      ^         ^       ^       ^          |
      +---------+-------+-------+----------+
                     expand

POSITION is independent:
CENTER_REAR <-> CORNERS <-> SIDE_DOCKS <-> FLOATING*

ANALYTICAL STATE is independent:
IDLE -> LISTENING -> ANALYZING/RESEARCHING/TESTING
                    -> WAITING/GAP/WARNING
                    -> COMPLETE/DEGRADED/ERROR

RENDER capability is independent:
FULL -> LIGHT -> 2D -> STATIC -> STATUS -> NONE
```

* FLOATING requires later usability approval.

## 11. Invariants

1. Hiding/collapsing avatar never terminates the analytical task.
2. Moving avatar never moves canonical data.
3. Render fallback never changes Knowledge Core truth.
4. Analytical state cannot be inferred solely from animation.
5. Real state has canonical/runtime source and timestamp/event reference where applicable.
6. User can recover from automatic layout change.
7. Avatar must not permanently obscure task-critical content.
8. Reduced-motion path must remain functionally equivalent.
9. Failure of avatar component must not block core Control Center.
10. State transitions are observable enough for debugging and tests.

## 12. Pre-test questions

Before implementation tests must define:
- every allowed/forbidden transition;
- restoration after reload/session restore;
- board collision scenarios;
- viewport constraints;
- reduced-motion behavior;
- render failure injection;
- stale/unknown analytical state;
- latency budget for collapse/move;
- state-event audit requirements;
- whether voice/gesture interaction belongs in v1 or later.

## 13. Next gate

Review the state dimensions and invariants. Then UI-003 defines Work Table + Board state model. UI-007 will convert UI-001/UI-002 requirements into executable test specifications before implementation.
