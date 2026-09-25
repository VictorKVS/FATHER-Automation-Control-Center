# ALINA 3D PRESENCE — EXECUTABLE TEST SPECIFICATION v0.1

Status: PRE_IMPLEMENTATION_TEST_BASELINE
Depends on:
- ALINA_3D_PRESENCE_PROTOTYPE_PASSPORT_V01.md
- ALINA_3D_SCENE_AND_STATE_NOTATION_V01.md

## 1. Purpose

Define acceptance tests before implementation of the first game-like ALINA 3D presence prototype. Tests protect the architectural rule that the avatar is a replaceable presentation channel and cannot become the owner of ALINA task/knowledge truth.

## 2. Test layers

T1 CONTRACT — commands, presence modes, behavior states, anchors.
T2 STATE — deterministic Presence Controller transitions.
T3 SCENE — avatar spawn, movement, orientation and presentation targets.
T4 WORKSPACE — full-screen panel takeover and restoration.
T5 FALLBACK — renderer failure and avatar-disabled operation.
T6 ACCESSIBILITY — reduced motion and non-audio/non-animation information path.
T7 TRUTH — visual state cannot invent backend work/status.
T8 REGRESSION — existing M1 contracts/tests/build remain green.
T9 VISUAL REVIEW — spatial composition is manually evidenced after executable prototype exists.

## 3. Fixtures

Mock Presentation Model:
- task_id: demo-makar-001
- current_object: Makar Agent Foundation
- backend_status: WORKING
- truth_state: DEMO
- gap_count: 1
- gap_ref: GAP-DEMO-001
- active_panel: null
- dialogue_text: "I found a demo knowledge gap."
- renderer_available: true

No fixture may contain real PII, secrets, private learner history or local absolute paths.

## 4. Acceptance cases

### 3D-001 Initial scene
GIVEN renderer available and default presence FULL_BODY
WHEN scene starts
THEN ALINA is bound to WORK_TABLE anchor
AND behavior is IDLE
AND workspace remains usable.

### 3D-002 Move to wall
GIVEN ALINA at WORK_TABLE
WHEN MOVE_TO(INFORMATION_WALL)
THEN state becomes WALKING during transition
AND avatar reaches the target tolerance defined by implementation fixture
AND returns to a non-walking state
AND canonical backend/task state is unchanged.

### 3D-003 Present evidence
GIVEN demo GAP is present
WHEN PRESENT(EVIDENCE_PANEL)
THEN ALINA targets the Evidence panel
AND presentation state references GAP-DEMO-001
AND no new GAP/evidence object is fabricated by renderer code.

### 3D-004 Full-screen takeover
GIVEN Evidence panel is being presented
WHEN OPEN_FULLSCREEN(EVIDENCE_PANEL)
THEN Evidence workspace becomes primary
AND presence may become COMPACT, VOICE_ONLY or HIDDEN according to policy
AND dialogue/task/status remain available
AND CLOSE_FULLSCREEN restores prior scene context.

### 3D-005 Explicit hide/show
GIVEN any non-failed scene
WHEN HIDE_ALINA
THEN avatar is not required for workspace operation
AND task/dialogue state remains intact.
WHEN SHOW_ALINA(FULL_BODY)
THEN renderer restores avatar presentation without creating a new ALINA task/session.

### 3D-006 Renderer failure
GIVEN renderer becomes unavailable
WHEN Presence Controller receives renderer failure
THEN presence degrades to STATUS_ONLY or HIDDEN
AND workspace/dialogue remain operational
AND no canonical task data is lost.

### 3D-007 Reduced motion
GIVEN reduced-motion preference
WHEN a movement/presentation command is issued
THEN essential state change is available without requiring animated locomotion
AND information is conveyed through text/status/workspace.

### 3D-008 Truth preservation
GIVEN backend_status is WAITING
WHEN avatar animation attempts THINKING/WORKING presentation
THEN UI must not represent unreported backend work as factual execution.
Presentation-only animation must be distinguishable from backend execution status.

### 3D-009 Unknown/unavailable data
GIVEN a metric is absent
WHEN a panel is shown
THEN it renders UNKNOWN/UNAVAILABLE according to contract
AND does not synthesize a numeric value.

### 3D-010 State restoration
GIVEN ALINA at INFORMATION_WALL and full-screen Graph panel open
WHEN full-screen is closed
THEN previous anchor, selected panel and permitted presence mode are restored deterministically.

### 3D-011 Command validation
Invalid anchor, panel, presence mode or behavior state must fail safely and produce a diagnosable UI/test error; it must not silently map to another semantic state.

### 3D-012 M1 regression
Existing M1 frontend unit/contract tests must pass after 3D integration.

### 3D-013 Build
Production frontend build must pass.

### 3D-014 Visual evidence
After automated gates pass, capture at minimum:
1. ALINA at Work Table;
2. ALINA presenting Information Wall;
3. full-screen Evidence/Graph workspace with avatar absent or reduced.
Manual review records clipping, occlusion, camera readability and spatial hierarchy issues.

## 5. Implementation order after review gate

P0 — typed contracts/state machine without 3D asset.
P1 — empty 3D scene + camera + anchors.
P2 — temporary licensed/test humanoid adapter.
P3 — idle/walk/turn between A0/A1.
P4 — panel presentation/full-screen transition.
P5 — hide/show/fallback/reduced motion.
P6 — visual evidence and baseline metrics.
P7 — only then evaluate lip-sync/voice and permanent ALINA asset.

## 6. Release decision

PASS only if T1-T8 automated gates pass, build passes, and T9 visual review has no blocking spatial defect.

Otherwise status is REWORK with explicit failing test/GAP. No aesthetic success can override truth/fallback/regression failures.
