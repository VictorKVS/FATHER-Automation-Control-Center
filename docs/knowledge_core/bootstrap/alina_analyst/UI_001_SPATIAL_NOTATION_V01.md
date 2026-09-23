# UI-001 — ALINA Control Center Spatial Notation v0.1

Status: NOTATION_DRAFT
Upstream: ALINA Control Center Passport v0.1; Technical Brief v0.1
Implementation: BLOCKED until notation review + test specification

## 1. Purpose

Define the spatial grammar of the Control Center before visual implementation. This notation describes zones, depth order, object movement and information flow. It is not a pixel-perfect screen design.

## 2. Coordinate/depth model

User viewpoint is the reference origin.

```text
Z4  BACK WALL / INFORMATION FIELD
    persistent screens, space/context background, global status

Z3  ALINA PRESENCE FIELD
    independent volumetric avatar, movable/dockable

Z2  DEPLOYABLE BOARD FIELD
    source/evidence/graph/task/test/comparison boards

Z1  CENTRAL WORK TABLE
    active task/object, primary manipulation surface

Z0  USER VIEWPOINT / INPUT
    keyboard/mouse/touch/voice as supported
```

Default depth relationship:
BACK WALL -> ALINA/BOARDS -> WORK TABLE -> USER.
ALINA must never be semantically embedded inside a monitor.

## 3. Horizontal zones

```text
┌──────────────────────────────────────────────────────────────┐
│ LEFT DOMAIN       BACK / GLOBAL FIELD       RIGHT DOMAIN     │
│ Sources           persistent context         Polygon          │
│ Knowledge                                  Metrics            │
│ Projects            [ ALINA ]              Training           │
│ Research        [board] [board]            Settings           │
│                                                              │
│                 ╔══════════════╗                              │
│                 ║  WORK TABLE  ║                              │
│                 ║ active task  ║                              │
│                 ╚══════════════╝                              │
└──────────────────────────────────────────────────────────────┘
                         USER
```

Left/right domain allocation is provisional. The invariant is SIDE DOMAIN vs ACTIVE CENTER, not which named item permanently belongs left or right.

## 4. Core spatial objects

ROOM — container for layout state.
WORK_TABLE — one primary active context.
ALINA_AVATAR — independent presentation/presence object.
DOMAIN_ENTRY — persistent navigation/availability object.
BOARD — temporary or pinned task-relevant projection.
AGENT_STACK — layered specialist/agent projection.
STATUS_FIELD — real system/task state projection.

## 5. Object movement notation

```text
DOMAIN_ENTRY
   │ select
   ▼
OBJECT_REFERENCE
   │ deploy
   ▼
BOARD ───── pin/minimize/close ─────► BOARD_STATE
   │ promote
   ▼
WORK_TABLE
   │ inspect relation
   ├────────► another BOARD
   │
   └────────► provenance / impact trace
```

Canonical data does not move or duplicate because the visual object moves. UI movement changes projection/context only.

## 6. ALINA occupancy rule

ALINA has an occupancy region. Boards and the work table have protected readable regions.

If a new critical board conflicts with ALINA:
1. retain user layout if still readable;
2. suggest/recommend another avatar position;
3. apply automatic reposition only under an explicit layout policy;
4. allow immediate user override;
5. never move/collapse ALINA in a way that loses task state.

## 7. Spatial states

S0 FULL_ROOM — side domains + ALINA + work table + active boards.
S1 FOCUS — work table + required boards + reduced side domains.
S2 ALINA_COMPACT — work context retained, avatar reduced.
S3 EYES — only ALINA eyes/status presence plus work context.
S4 MINIMAL — status indicator only.
S5 PRESENTATION_HIDDEN — avatar hidden; analytical UI remains operational.

## 8. Agent Stack placement

An Agent Stack normally enters from a side domain as a compact vertical object.

```text
AGENTS DOMAIN
    ↓
[compact stack]
    ↓ select layer
[layer board] ─────► WORK TABLE
    ↓
knowledge / evidence / tests / metrics
```

The full stack may remain adjacent while one layer is promoted to the work table.

## 9. Context preservation invariant

For every spatial transition:
- active_task_id is preserved unless user changes task;
- active_object_id is preserved or explicitly replaced;
- provenance context remains recoverable;
- board origin is known;
- avatar state is independent from analytical state;
- collapse does not equal task termination.

## 10. Failure/degraded notation

```text
3D unavailable
   ↓
LIGHT_3D
   ↓
2D/FACE
   ↓
EYES/STATUS
   ↓
NO_AVATAR
   ↓
CORE WORKSPACE STILL AVAILABLE
```

Knowledge Core/data failure is a different failure class and must show explicit degraded/unknown state rather than being masked by avatar fallback.

## 11. Notation review questions

- Are Z0-Z4 sufficient to express intended depth?
- Can boards coexist with a full avatar without hiding critical information?
- Is the work table always visually dominant for an active task?
- Can every side-domain object reach the table through a consistent interaction?
- Can the avatar be moved/collapsed without changing analytical state?
- Does Agent Stack fit this grammar without special-case navigation?
- Which transitions require animation, and which must also work with reduced motion?

## 12. Gate

UI-001 may move from NOTATION_DRAFT to NOTATED only after these invariants and transitions are reviewed. Next, UI-002 defines the avatar state machine in detail; then UI-007 specifies tests before production implementation.
