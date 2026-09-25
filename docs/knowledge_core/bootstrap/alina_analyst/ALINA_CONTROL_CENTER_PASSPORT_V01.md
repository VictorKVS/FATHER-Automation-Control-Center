# ALINA Control Center — Analytical Passport v0.1

Status: CONCEPT_BASELINE / PRE-NOTATION
Rule: passport before formal notation, tests before implementation.

## 1. Purpose

ALINA Control Center is the human-facing workspace of ALINA over the canonical FATHER Knowledge Core. It must make complex analytical work spatially understandable while keeping secondary functions available without competing with the current task.

The central metaphor is a command/analytical room: ALINA is visually present behind a central working table; task-specific boards/panels unfold around and above that table; persistent navigation and secondary domains live on the side planes.

## 2. Primary spatial composition

### CENTER — Focus / Work Table

The center is reserved for the current work object. The working table is the visual anchor and the highest-priority interaction zone.

It may host:
- current document/source;
- graph fragment;
- investigation;
- Agent Foundation artifact;
- task/decision;
- comparison;
- experiment;
- code/design artifact;
- review package.

The table is not a decorative dashboard. It represents the active working context.

### BEHIND CENTER — ALINA Presence

ALINA appears behind the work table as a synthetic 3D/digital projection. She is the visible analytical operator of the workspace.

Her presentation may reflect real states such as idle, analyzing, waiting for evidence, gap detected, testing, warning, completed. Visual state must be bound to real system state; decorative animation must not masquerade as telemetry.

### AROUND CENTER — Deployable Boards

Boards appear only when the current task needs them. Candidate board roles:
- source/evidence;
- knowledge/graph;
- task/decision;
- comparison/A-B;
- document/detail;
- impact/currentness;
- test/result;
- specialist consultation.

Boards can open, pin, minimize, stack or return to their originating side section while preserving context.

### SIDES — Persistent but De-emphasized Domains

Side planes contain functions that must remain reachable but should not dominate the active task.

Candidate groups:
- Knowledge Base;
- Sources / Library;
- Projects / Workspaces;
- Specialists / Agent Zoo;
- Training / Learning;
- Experiments / Polygon;
- Metrics;
- Dashboards;
- History / Time Machine;
- Gaps / Research Orders;
- Notifications;
- Settings / Configuration;
- System / Health / Audit.

These are information architecture candidates, not a frozen menu. Their final grouping must be derived from tasks and validated by use.

## 3. Attention hierarchy

Priority 1: active work on central table.
Priority 2: ALINA state and task-critical boards.
Priority 3: evidence/provenance/status required for trust.
Priority 4: navigation to adjacent domains.
Priority 5: training, metrics, dashboards, settings and administration unless the current task explicitly promotes one of them.

A secondary domain can temporarily become Priority 1 when selected; hierarchy follows task context, not a permanent visual ranking.

## 4. Interaction principle — bring information to the table

The user should not repeatedly leave the active workspace to inspect related information. Selecting a source, graph node, metric, specialist or setting should normally open the relevant object as a board/card/panel around the same work table.

Concept:

```text
SIDE DOMAIN -> SELECT OBJECT -> DEPLOY BOARD -> WORK/COMPARE -> PIN/SAVE/CLOSE
                                      |
                                      v
                              CENTRAL CONTEXT
```

## 5. Progressive disclosure

FULL COMMAND ROOM
-> central work table + ALINA + active boards + side domains
-> focused workspace
-> ALINA panel
-> compact avatar
-> eyes/status strip
-> minimal live indicator.

Collapse must preserve recoverable task/context state.

## 6. Knowledge Base relationship

The site is a projection over canonical FATHER data. Knowledge Base is a major side domain, but knowledge objects can be pulled onto the central table and related boards without duplicating canonical truth.

Required reverse navigation where data exists:
visible result -> decision -> knowledge -> evidence -> fragment -> source version -> original source.

## 7. Visual direction

Reference direction: dark science-fiction command space, cyan/blue luminous technical accents, holographic/translucent boards, restrained graph/network motifs, central depth, ALINA as a synthetic projected presence.

The visual metaphor must serve information hierarchy. It must not reduce readability, accessibility or performance.

## 8. Explicit separation: workspace vs dashboard

The default center is a WORKSPACE, not a wall of metrics.

Metrics/dashboards stay available on side planes and can be promoted into the center when the user is analyzing system performance, experiments or production health.

This prevents the primary analytical surface from becoming a generic admin dashboard.

## 9. State preservation

The workspace state should be representable as data:
- active_task_id;
- active_object_id;
- central_table_mode;
- open_board_ids;
- pinned_board_ids;
- selected_graph_nodes;
- current_specialist/context;
- collapse_level;
- relevant provenance references;
- layout/version where needed.

The exact persistence implementation is deferred.

## 10. Failure/fallback considerations

- 3D ALINA unavailable -> 2D/lightweight presence.
- heavy board rendering unavailable -> simplified panels.
- animation/reduced-motion preference -> static transitions.
- Knowledge Core unavailable -> explicit degraded/read-only/offline state as applicable; never fake fresh data.
- telemetry unavailable -> UNKNOWN/UNAVAILABLE, not decorative numbers.

## 11. Open questions for later analysis

- exact side-domain grouping;
- number of simultaneously visible boards before cognitive overload;
- desktop resolution envelope and multi-monitor behavior;
- keyboard/voice interaction;
- 3D engine choice;
- whether work table needs free spatial placement or constrained docking;
- accessibility requirements;
- mobile/tablet projection;
- persistence granularity;
- user-configurable layouts versus governed defaults.

These remain open intentionally and must be answered through task analysis and tests, not aesthetic preference alone.

## 12. Next gate

This passport is the analytical description. The next artifact is a formal screen/spatial-state notation derived from it. After notation review, create test specifications for hierarchy, context preservation, fallback, performance and usability. No production UI implementation before those gates.
