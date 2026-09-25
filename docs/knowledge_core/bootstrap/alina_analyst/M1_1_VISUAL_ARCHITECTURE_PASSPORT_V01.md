# ALINA Control Center M1.1 — Visual Architecture Passport v0.1

Status: PRE_IMPLEMENTATION_BASELINE  
Scope: visual/spatial composition only; preserve validated M1 behavior.  
Trace: Entry 0044 / UI-GAP-001.

## 1. Problem

The first locally rendered M1 is technically valid but visually schematic. It does not yet communicate the intended analytical command-room hierarchy or make ALINA, the information wall and the Work Table read as one coherent workspace.

## 2. Objective

Produce the first visually convincing ALINA Control Center using a replaceable 2D/2.5D implementation before committing to a heavy 3D engine.

The required perceptual hierarchy is:

BACK WALL / INFORMATION SCREENS -> ALINA -> WORK TABLE -> USER.

## 3. Non-goals

M1.1 does not add a real Knowledge Core backend, production telemetry, final 3D avatar, production deployment, or new claims of REAL data. It must not disguise DEMO/PLANNED data as operational truth.

## 4. Functional zones

1. Command/Status Bar — product identity, current context, truth/system state and view controls.
2. Source Rail — Sources, Knowledge, Projects and Agents navigation with clear active state.
3. Information Wall — coordinated Knowledge, Graph, Evidence and Activity surfaces.
4. ALINA Presence — central analytical presence, visually stronger than ordinary panels but not blocking working information.
5. Work Table — primary current-decision surface for document, knowledge object, graph, compare or review modes.
6. Context/Agent Stack — specialists/agents and task context, visually subordinate to the Work Table.
7. System Strip — provenance, jobs, alerts and system/fallback state.

## 5. Spatial rules

- Avoid large purposeless empty regions.
- Information Wall belongs behind ALINA, not as an unrelated floating card.
- ALINA occupies a meaningful central layer; M1.1 may use an original CSS/SVG/2D representation behind AvatarRendererAdapter.
- Work Table must read as the primary interactive surface closest to the user.
- Side rails frame the workspace rather than compete with it.
- Depth must be conveyed by scale, overlap, perspective, blur/glow restraint and hierarchy, not decorative noise.
- Layout must remain usable when ALINA degrades to STATUS_ONLY or HIDDEN.

## 6. Truth and data rules

All existing M1 truth semantics remain mandatory: DEMO, PLANNED, UNAVAILABLE, STALE and UNKNOWN remain explicit. Visual richness must never imply backend connectivity that does not exist.

## 7. Interaction rules

Focus Mode reduces peripheral surfaces and emphasizes Work Table/current object. ALINA presence can collapse without moving canonical task state. Boards remain open/closeable. Reduced-motion users receive the same information hierarchy without animation dependency.

## 8. Replaceability

Visual implementation must preserve component boundaries. Avatar rendering remains behind an adapter. Information-wall panels consume presentation models rather than directly querying a future database. No final 3D engine is selected by this passport.

## 9. Acceptance gate

M1.1 may proceed to implementation only after the spatial notation and pre-implementation visual/interaction test specification exist. Implementation is accepted only if existing M1 tests remain green and M1.1 tests demonstrate the intended hierarchy, fallback behavior, responsive containment and truth-state visibility.

## 10. Expected result

A user opening the page should immediately understand: what system this is, what ALINA is working with, what the current work object is, where evidence/knowledge/agents live, and which information is DEMO versus connected/real. The page should read as one analytical workspace rather than a collection of bordered rectangles.
