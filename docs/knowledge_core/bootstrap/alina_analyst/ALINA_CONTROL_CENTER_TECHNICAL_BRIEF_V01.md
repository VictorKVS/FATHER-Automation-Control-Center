# ALINA Control Center — Technical Brief / Website Project Specification v0.1

Status: REQUIREMENTS_BASELINE / NO IMPLEMENTATION
Upstream: C00, ALINA Control Center Analytical Passport v0.1
Visual basis: user-supplied references of luminous synthetic ALINA face/eyes, green holographic projection, and science-fiction command room.
Rule: this document specifies intent; formal notation and tests must precede implementation.

## 1. Product vision

The website presents ALINA as a live analytical presence inside a FATHER command workspace. The central area is a working table. ALINA is positioned behind or around it as a movable digital avatar. Contextual boards unfold around the table. Persistent but secondary domains occupy the side planes.

The site must combine:
- operational workspace;
- Knowledge Core navigation;
- provenance/evidence inspection;
- agent/specialist construction;
- experiments/tests/metrics;
- ALINA presence and state;
without turning the default screen into a generic dashboard.

## 2. Reference composition

```text
┌─────────────────────────────────────────────────────────────┐
│ LEFT DOMAIN PLANE                         RIGHT DOMAIN PLANE │
│ Knowledge / Sources                      Polygon / Metrics   │
│ Projects / Research                      Training / Settings │
│                                                             │
│      ┌────────┐       DEPLOYABLE BOARDS       ┌────────┐    │
│      │Evidence│                                │ Graph  │    │
│      └────────┘          [ ALINA ]             └────────┘    │
│                           avatar                            │
│                     ╔══════════════╗                        │
│                     ║ WORK TABLE   ║                        │
│                     ║ active task  ║                        │
│                     ╚══════════════╝                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 3. Avatar interaction requirements

ALINA avatar is a movable presentation object, not a fixed background.

Required position modes:
- CENTER_REAR — default behind work table;
- TOP_LEFT;
- TOP_RIGHT;
- BOTTOM_LEFT;
- BOTTOM_RIGHT;
- SIDE_DOCK_LEFT;
- SIDE_DOCK_RIGHT;
- FLOATING — constrained free placement if usability/performance tests approve it.

Required visibility/collapse modes:
- FULL_3D;
- HALF_BODY / COMPACT_3D;
- FACE;
- EYES;
- STATUS_ORB / MINIMAL_INDICATOR;
- HIDDEN_WITH_STATUS_AVAILABLE.

Core transitions:

```text
FULL_3D
  ↓
COMPACT
  ↓
FACE
  ↓
EYES
  ↓
STATUS
  ↓
HIDDEN

Any visible state -> move/dock to allowed screen position.
Any collapsed state -> restore prior position and working context.
```

The user must be able to move ALINA away from information she obscures. The system may suggest/reposition her when a task-critical board needs the same area, but automatic movement must not destroy user preference without an explicit layout policy.

## 4. Avatar state vs system state

Visual behavior may represent real ALINA states:
IDLE, LISTENING, ANALYZING, RESEARCHING, WAITING_FOR_EVIDENCE, GAP_DETECTED, TESTING, WARNING, COMPLETE.

The mapping must be documented. Animation alone is not evidence. Unknown telemetry is shown as unknown/unavailable.

## 5. Work table

The table is the primary focus surface. It can host one primary work context and linked secondary objects.

Candidate modes:
DOCUMENT;
GRAPH;
INVESTIGATION;
AGENT_FOUNDATION;
DESIGN;
COMPARE;
EXPERIMENT;
REVIEW;
CODE/ARTIFACT.

Mode is data/state, not a separate disconnected site.

## 6. Deployable boards

Boards are task-oriented projections. Minimum candidate board types:
SOURCE;
EVIDENCE;
KNOWLEDGE;
GRAPH;
TASK;
DECISION;
COMPETENCY;
IMPACT;
CURRENTNESS;
TEST;
METRICS;
COMPARE;
SPECIALIST_CONSULTATION.

Lifecycle:
CLOSED -> OPEN -> PINNED/MINIMIZED -> CLOSED.
Board state and origin object must be recoverable.

## 7. Side-domain candidates

Left/right grouping is provisional and must be validated:
Knowledge Base;
Sources/Library;
Projects/Workspaces;
Research;
Specialists/Agent Zoo;
Training/Learning;
Experiments/Polygon;
Metrics;
Dashboards;
History/Time Machine;
Gaps/Research Orders;
Notifications;
Settings;
System Health/Audit.

The architecture reserves these functions now while intentionally de-emphasizing them in the first visual focus.

## 8. Knowledge Base requirement

The website must expose canonical FATHER Knowledge Core projections rather than create a second knowledge truth store.

Minimum trace interaction:
RESULT -> DECISION -> KNOWLEDGE -> EVIDENCE -> FRAGMENT -> SOURCE VERSION -> ORIGINAL SOURCE.

Graph views and tabular/list views are complementary. The user can pull a knowledge object from a side domain onto the work table or a board.

## 9. Layout state contract — candidate

```text
WorkspaceLayoutState
- layout_version
- active_task_id
- active_object_id
- work_table_mode
- avatar_position_mode
- avatar_visibility_mode
- avatar_previous_position
- open_board_ids
- pinned_board_ids
- minimized_board_ids
- selected_object_ids
- selected_graph_node_ids
- collapse_level
- viewport_profile
- reduced_motion
- provenance_context_refs
```

Exact schema is deferred until notation/test review.

## 10. Visual language

Use supplied references as visual direction:
- deep dark command-room environment;
- cyan/blue luminous engineering accents;
- optional green holographic state/variant;
- translucent holographic boards;
- subtle graph/node geometry;
- ALINA's recognizable face/eyes preserved across collapse states;
- strong central depth around work table;
- readable typography and data density take priority over decoration.

Do not copy third-party UI assets or pseudo-scanner claims. Create original FATHER/ALINA visual assets inspired by the general language.

## 11. Resilience and accessibility

3D rendering is optional presentation capability. Core work remains available through fallback UI.

Required fallback concepts:
FULL_3D -> LIGHT_3D/WEBGL -> 2D AVATAR -> EYES/STATUS -> NO_AVATAR.

Support reduced motion. Avoid critical information encoded only through color, animation or avatar expression.

## 12. Website project artifact plan

Before implementation the project must contain:
1. this Technical Brief;
2. detailed component passports;
3. formal spatial/screen-state notation;
4. information architecture;
5. user/task flows;
6. visual wireframes;
7. avatar state/movement specification;
8. board state specification;
9. Knowledge Core interaction specification;
10. test specification;
11. workload/performance profiles;
12. accessibility/fallback tests;
13. A/B experiment plan for layout/avatar variants;
14. implementation plan;
15. release evidence.

## 13. Initial acceptance intentions

The final tests must prove, at minimum:
- avatar can be moved to supported corners/docks;
- avatar can collapse to EYES and minimal/hidden state;
- restoring avatar restores expected position/context;
- boards remain usable when avatar is moved/collapsed;
- central work context survives navigation and collapse where specified;
- Knowledge objects retain canonical IDs/provenance;
- 3D failure does not prevent Knowledge Core work;
- layout remains readable under representative desktop viewport profiles;
- real metrics are distinguishable from decorative visuals;
- state can be restored from a declared layout state representation.

## 14. Next artifact

Create formal spatial notation and low-fidelity visual wireframes from this specification. Do not begin production UI code until notation and pre-implementation test specification pass review.


## 15. Critical visual correction — ALINA is an embodied 3D analyst, not screen content

ALINA must be perceived as an independent full-bodied volumetric avatar located physically/visually in front of the information screens and behind/near the central work table. She is not a portrait rendered inside the central monitor and not a decorative dashboard background.

Target spatial model:

```text
BACK WALL / INFORMATION SCREENS
 documents | graphs | evidence | metrics
                ↓
        [ volumetric ALINA ]
        full-bodied analyst
        independent 3D layer
                ↓
          CENTRAL WORK TABLE
                ↓
               USER
```

The interaction metaphor is face-to-face collaboration with a human analyst: ALINA can address the user, turn toward a relevant board, indicate an object, move/dock to another permitted position, and reduce her visual presence when the workspace requires maximum information density.

Her avatar layer and the information-display layer are separate components. Screens remain usable without the avatar; ALINA remains conceptually present even when collapsed to face/eyes/status.

Future visualizations must preserve depth ordering: screens/background -> ALINA volumetric presence -> work table -> user viewpoint. A composition that embeds ALINA inside a monitor fails this requirement.


## 16. Agent layered intelligence visualization

Agent/specialist information must support a layered vertical representation inspired by the supplied stacked intelligence/process references. This is a semantic projection of the Agent Foundation, not a decorative infographic and not a second data model.

### Core interaction

Each agent can be viewed as a stack of addressable layers. The user can inspect the whole stack, expand/collapse a layer, isolate it, compare it with the same layer of another agent, and trace a layer to canonical knowledge/evidence/tests.

Candidate generic stack (subject to Specialist Factory evidence and profession-specific variation):

```text
L8  OUTCOMES / STRATEGIC CAPABILITY
L7  DECISIONS / REASONING / SYNTHESIS
L6  ACTIONS / WORKFLOWS / COLLABORATION
L5  METHODS / ALGORITHMS / TOOLS
L4  COMPETENCIES / TASK CLASSES
L3  KNOWLEDGE / RULES / CONSTRAINTS
L2  EVIDENCE / SOURCES / PROVENANCE
L1  INPUT / CONTEXT / SIGNALS
L0  RUNTIME / MODEL / MEMORY / INTERFACES
```

This is a visualization baseline, not a claim that every profession has exactly nine fixed layers. The Factory may add, merge or specialize layers while preserving traceable contracts.

### Layer card/passport

Every displayed layer should be able to expose:
- layer_id/type/version/status;
- purpose and responsibility;
- inputs/outputs;
- tasks/decisions/competencies represented;
- knowledge/evidence coverage;
- methods/tools/components;
- tests and latest validated result;
- metrics with test context;
- gaps/contradictions/currentness;
- dependencies up/down the stack;
- change/impact history.

### Visual behavior

Default: compact vertical stack beside/above the work table. Selecting a layer expands it into a working board. Multiple layers may be exploded into a pipeline/graph view. Layers may show readiness/coverage/currentness states, but visual encoding must map to real canonical states rather than invented scores.

Candidate interactions:
STACK -> LAYER -> OBJECTS -> EVIDENCE / TESTS -> IMPACT.
STACK A + STACK B -> SAME LAYER -> COMPARE, when contracts/context make comparison valid.

### Relationship to progressive disclosure

The entire agent can collapse from full stack to compact spine/icon. A single active layer can remain expanded while the rest collapse. This allows deep agent information without permanently occupying the main workspace.


## 17. Development backlog baseline — accepted visual/interaction concepts

The following concepts are accepted into the website project backlog and must be carried through notation, tests and implementation planning:

- embodied full-bodied ALINA volumetric analyst, independent of display screens;
- depth order: information screens -> ALINA -> work table -> user;
- movable/dockable avatar with corner/side positions;
- progressive avatar collapse: full -> compact -> face -> eyes -> status -> hidden;
- central task-oriented work table;
- deployable holographic boards that bring information to the table;
- side-domain planes for currently secondary functions;
- Knowledge Core navigation with reverse provenance trace;
- layered Agent Stack visualization with drill-down and comparison;
- progressive disclosure for boards, agent stacks and avatar;
- real-state/real-metric rule: no decorative telemetry presented as operational truth;
- fallback/reduced-motion/non-3D modes;
- workspace state preservation and restoration;
- modular/versioned/A-B-testable presentation components.

### Development maturity states

Every accepted UI capability moves through:

```text
IDEA_CAPTURED
-> PASSPORTED
-> NOTATED
-> TEST_SPECIFIED
-> IMPLEMENTATION_READY
-> IMPLEMENTED
-> TESTED
-> VALIDATED
-> RELEASED
```

No capability is marked IMPLEMENTATION_READY solely because a concept image exists.

### Immediate development queue

UI-001 Spatial notation: command room zones, depth layers, movement paths, deployable-board flows.
UI-002 Avatar state machine: position, visibility/collapse, real analytical state, fallback.
UI-003 Work-table/board state model.
UI-004 Agent Stack notation and layer contract.
UI-005 Knowledge Core interaction/provenance flow.
UI-006 Low-fidelity wireframes for full/focused/eyes/minimal states.
UI-007 Pre-implementation test specification.
UI-008 Performance/accessibility/fallback workload profiles.
UI-009 A/B experiment plan for avatar/layout/board variants.
UI-010 Implementation plan only after UI-001..UI-009 gates are reviewed.
