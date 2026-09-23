# UI-003 — Work Table & Deployable Boards Model v0.1

Status: NOTATION_DRAFT
Scope: MVP-00
Upstream: UI-001 Spatial Notation; UI-002 Avatar State Machine; MVP-00 Scope
Implementation: BLOCKED until test specification and review

## 1. Purpose

Define how the user works with real FATHER objects without leaving the main Control Center. The central Work Table owns the primary active context; Boards bring related information to that context.

## 2. Core rule

The user should not navigate away from the active task merely to inspect related information.

```text
FIND / SELECT OBJECT
        ↓
OPEN BOARD
        ↓
INSPECT / PIN / COMPARE
        ↓
PROMOTE TO WORK TABLE if primary
        ↓
FOLLOW RELATION / PROVENANCE
        ↓
OPEN RELATED BOARD
        ↓
SAVE / MINIMIZE / CLOSE
        ↓
RETURN WITHOUT LOSING CONTEXT
```

## 3. Work Table contract

The Work Table has exactly one PRIMARY_CONTEXT in MVP.

Candidate fields:
- workspace_id;
- active_task_id;
- primary_object_ref;
- primary_object_type;
- mode;
- title/summary;
- source/provenance refs;
- dirty/unsaved UI state where applicable;
- related_board_ids;
- previous_primary_context_ref;
- focus_state;
- version.

MVP modes:
DOCUMENT;
KNOWLEDGE_OBJECT;
AGENT_STACK_OR_LAYER;
PROJECT_OBJECT;
COMPARE;
REVIEW.

Modes are projections over canonical objects, not independent copies.

## 4. Board contract

A Board is a temporary/pinned projection of one object or relation set.

Candidate fields:
- board_id;
- board_type;
- object_ref;
- canonical_object_id where applicable;
- origin;
- relation_to_primary;
- state;
- position_slot;
- pinned;
- minimized;
- provenance_refs;
- data_status: REAL | DEMO | PLANNED | UNAVAILABLE;
- version.

MVP board types:
SOURCE_EVIDENCE;
KNOWLEDGE_RELATIONS;
AGENT_LAYER;
PROJECT_CONTEXT;
DETAIL;
COMPARE_CANDIDATE.

## 5. Board lifecycle

```text
CLOSED
  ↓ open
OPEN
  ├── pin ───────► PINNED
  ├── minimize ──► MINIMIZED
  ├── promote ───► PRIMARY_ON_TABLE
  └── close ─────► CLOSED

PINNED/MINIMIZED
  ├── restore ───► OPEN
  └── close ─────► CLOSED

PRIMARY_ON_TABLE
  ├── replace primary -> previous context enters history
  └── demote -> OPEN/PINNED
```

## 6. Primary-context replacement

When a board is promoted:
1. preserve current primary-context reference;
2. promote selected object;
3. keep previous context in local navigation history;
4. retain relevant pinned boards where contracts still apply;
5. mark incompatible boards stale/context-changed rather than silently reinterpreting them.

This creates predictable Back/Return behavior.

## 7. Relationship opening

Selecting a relation never requires duplicating canonical data.

Example:

```text
WORK TABLE: Knowledge K-17
   ├── evidence ──► Board E-4
   ├── source ────► Board S-2
   ├── related ───► Board K-18
   └── agent use ─► Board AgentLayer-A3
```

Each board knows why it was opened through relation_to_primary/origin.

## 8. Comparison

MVP comparison is deliberately limited.

Two compatible objects may be placed into COMPARE mode when a comparison contract exists. The UI must not imply comparability merely because two cards can be shown side by side.

For metrics, test context validity rules apply.

## 9. Board capacity and cognitive load

Do not hard-code a large simultaneous board count before testing.

MVP concept:
- 1 primary Work Table context;
- small number of visible active boards;
- additional boards minimized/stacked;
- pinned boards survive context changes only when still meaningful.

Exact visible-board threshold is a UI-007 usability-test parameter.

## 10. Interaction with ALINA

ALINA is not a Board.

ALINA may:
- point/turn toward an active board;
- explain a board/object;
- request a board;
- suggest pin/compare/promote;
- move/collapse when a board requires her occupied region.

ALINA cannot visually override canonical object state.

## 11. Agent Stack integration

```text
AGENT STACK BOARD
      ↓ choose layer
AGENT LAYER BOARD
      ↓ promote
WORK TABLE: AGENT LAYER
      ├── Knowledge board
      ├── Evidence board
      ├── Tests board (later/full)
      └── Gaps board (later/full)
```

MVP requires at least one structured stack/layer path; deeper Factory functions may be DEMO/PLANNED.

## 12. Knowledge vertical slice

Required real MVP path:

```text
WORK TABLE: DOCUMENT/SOURCE
      ↓ select fragment/knowledge
KNOWLEDGE BOARD
      ↓ evidence
EVIDENCE BOARD
      ↓ source/version
SOURCE BOARD
      ↓ promote/inspect
WORK TABLE
      ↓ back
previous context restored
```

Every real board on this path must carry canonical IDs/provenance available from the backend.

## 13. Truth/status rule

Every Board declares:
REAL — backed by connected canonical data;
DEMO — fixture/example data;
PLANNED — capability shell only;
UNAVAILABLE — expected real capability/data currently unavailable.

Status must be visible enough to prevent confusion without dominating the workspace.

## 14. State restoration

MVP restoration target:
- primary context;
- previous-context navigation reference;
- open/pinned/minimized boards selected for persistence;
- board/object references;
- avatar state from UI-002;
- focus/collapse state.

If a canonical object/version no longer exists or is inaccessible, restore the layout with an explicit stale/unavailable state rather than substituting another object.

## 15. Failure cases to test later

- board object becomes unavailable;
- source version superseded during session;
- board opened from stale relation;
- user promotes a DEMO board;
- comparison objects incompatible;
- too many boards requested;
- avatar/board collision;
- reload during active work;
- canonical backend temporarily unavailable;
- restore points to changed object version.

## 16. MVP quality gate

UI-003 is acceptable for test-specification stage when:
- primary context is unambiguous;
- every board has origin/object/status;
- promote/demote/back behavior is deterministic;
- canonical data is not duplicated by UI movement;
- REAL/DEMO/PLANNED/UNAVAILABLE are distinguishable;
- restoration and stale states are explicit;
- Agent Stack and Knowledge vertical slice fit the same board grammar.

## 17. Next step

UI-004 formalizes the Agent Stack/layer model against this Board contract. Then UI-005 formalizes Knowledge/Provenance navigation. UI-006 wireframes can combine UI-001..005; UI-007 specifies tests before implementation.
