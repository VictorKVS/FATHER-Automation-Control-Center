# MVP-00 — ALINA Control Center Scope v0.1

Status: SCOPE_BASELINE
Product horizon: Beautiful Working MVP
Super-project: ALINA remains separate long-horizon development
Implementation: BLOCKED until notation + tests

## 1. MVP purpose

Create a beautiful, comfortable and useful daily FATHER workspace before the full ALINA super-project is complete.

The MVP must prove the interaction model:
USER <-> ALINA <-> WORK TABLE <-> BOARDS <-> CANONICAL FATHER OBJECTS.

It must feel like a coherent analytical workplace, not a collection of admin pages.

## 2. MVP success scenario

A user opens FATHER and:
1. enters the Control Center;
2. sees ALINA as an independent presence in the room;
3. sees the central work table as the primary focus;
4. opens one real FATHER object;
5. receives related information on deployable boards without losing the active context;
6. can move/collapse ALINA when she obstructs work;
7. can inspect the object's available provenance/evidence chain;
8. can switch to another object and return;
9. can restore the working layout/context;
10. can clearly distinguish real connected data from demo/placeholder areas.

If this end-to-end scenario is pleasant and reliable, the MVP has demonstrated the shell.

## 3. MUST WORK in MVP

### M1 Control Center shell
- command-room visual composition;
- central work table;
- side-domain placeholders/navigation;
- deployable-board region;
- responsive desktop layout within declared viewport profiles.

### M2 ALINA presence
- recognizable ALINA visual presence;
- independent from information screens;
- at least CENTER_REAR plus corner/dock placement;
- collapse at least FULL/FACE-or-COMPACT/EYES/MINIMAL;
- state restoration;
- non-3D/lightweight fallback.

Full photorealistic volumetric 3D is not required for MVP if a simpler implementation preserves the intended interaction and is replaceable.

### M3 Work Table
- one primary active object/context;
- open/replace/return behavior;
- context/state representation.

### M4 Deployable boards
At least a small real set:
- Source/Evidence board;
- Knowledge/Graph-or-Relations board;
- Agent/Layer board or Project board.
Boards can open, close, pin/minimize as selected for MVP tests.

### M5 Real vertical slice
At least one real canonical object chain:
SOURCE/DOCUMENT
-> FRAGMENT or VERSION
-> KNOWLEDGE OBJECT
-> EVIDENCE/PROVENANCE
-> visible Control Center projection.

The MVP must not be demo-only.

### M6 Knowledge navigation
User can inspect the real chain available for the vertical slice and return to the active work context.

### M7 Agent representation
At least one ALINA/agent information stack is rendered from structured data, even if many future layers are placeholders.

### M8 Workspace state
Preserve enough state to restore:
- active object;
- avatar visibility/position;
- open/pinned boards selected for MVP;
- collapse/focus state.

### M9 Truthful status
Connected real data, demo data, unavailable data and planned features must be visually distinguishable.

## 4. MAY BE VISUAL/DEMO in MVP

These may appear as designed shells with explicit DEMO/PLANNED status:
- Training/Learning;
- advanced Metrics/Dashboards;
- full Polygon;
- full Agent Zoo;
- Time Machine;
- advanced Impact Graph;
- multi-specialist collaboration;
- rich avatar gestures;
- voice interaction;
- sophisticated 3D room navigation;
- full regulatory graph.

Demo elements cannot emit fake operational claims.

## 5. OUT OF MVP / SUPER-PROJECT

Not required to release the shell:
- full Specialist Factory;
- autonomous profession discovery;
- complete Evidence/Decision/Competency engines;
- production-grade autonomous research;
- fine-tuning pipeline;
- all FATHER employee avatars;
- advanced multi-agent orchestration;
- full A/B platform implementation;
- complete learning/evolution engine;
- all Knowledge Core domains.

Their interfaces/space may be reserved but they do not block MVP.

## 6. UX acceptance intent

MVP must optimize for long-session comfort:
- central focus is obvious;
- secondary controls do not dominate;
- important text/data remains readable;
- avatar is pleasant but never obstructive;
- common actions require low navigation effort;
- user can always understand where they are and what object is active;
- visual effects do not create noticeable interaction friction;
- reduced-motion/fallback remains usable.

Quantitative thresholds are deferred to UI-007 after workload/context definition.

## 7. MVP visual hierarchy

```text
PRIMARY:
  WORK TABLE + ACTIVE OBJECT

SECONDARY:
  ALINA + TASK-RELEVANT BOARDS

TERTIARY:
  PROVENANCE / STATUS / RELATED OBJECTS

BACKGROUND:
  SIDE DOMAINS / FUTURE MODULES
```

A background module can become PRIMARY when explicitly selected.

## 8. MVP data principle

Use canonical FATHER IDs and data contracts wherever a real backend object exists.

If backend functionality does not yet exist:
- use explicit fixture/demo data;
- label it;
- keep the UI contract compatible with later real data;
- never create a parallel source of truth merely to make the screen look complete.

## 9. MVP implementation strategy

Prefer the simplest replaceable implementation that proves the interaction:
- 2D/Canvas/WebGL/limited 3D can stand in for final volumetric rendering;
- a limited real graph can stand in for the future full graph engine;
- a small canonical vertical slice can stand in for the complete Knowledge Core.

Do not fake depth of capability; prove the architecture through a narrow real path.

## 10. Exit gate

MVP can move toward implementation only after:
- UI-001 spatial notation reviewed;
- UI-002 avatar state notation reviewed;
- UI-003 Work Table/Board model completed;
- MVP wireframe completed;
- UI-007 tests for the MVP path specified;
- data contract for the real vertical slice identified;
- explicit demo/real boundary documented.

## 11. Immediate next step

Derive UI-003 Work Table + Board state model specifically against this MVP scope, avoiding features that belong only to the super-project.
