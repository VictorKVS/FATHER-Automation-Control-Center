# ALINA 3D SCENE AND STATE NOTATION v0.1

Status: PRE_IMPLEMENTATION_NOTATION

## 1. System flow

FATHER / ALINA Runtime
        |
        v
Presentation Model
        |
        +-----------------------> Workspace Controller
        |                              |
        v                              v
Presence Controller              Full-screen Panels
        |
        v
AvatarRendererAdapter
        |
        v
3D Scene / VRM Avatar

No reverse path may promote renderer-local state into canonical Knowledge Core truth.

## 2. Scene graph

SCENE
|- Environment
|  |- Room
|  |- InformationWall
|  |  |- KnowledgeAnchor
|  |  |- GraphAnchor
|  |  '- EvidenceAnchor
|  '- WorkTable
|- ALINA
|  |- AvatarRoot
|  |- AnimationController
|  |- GazeTarget
|  '- InteractionTarget
'- CameraRig

## 3. Spatial anchors

A0 WORK_TABLE
A1 INFORMATION_WALL
A2 KNOWLEDGE_PANEL
A3 GRAPH_PANEL
A4 EVIDENCE_PANEL

Prototype navigation is anchor-based. Arbitrary autonomous path planning is out of scope.

## 4. Presence state machine

FULL_BODY -> COMPACT -> VOICE_ONLY -> HIDDEN
     \---------------------------> STATUS_ONLY

Any state may transition to STATUS_ONLY on renderer failure.
User may request show/hide independently of backend task state.

## 5. Behavior state machine

IDLE
 -> LISTENING
 -> THINKING
 -> WALKING
 -> PRESENTING
 -> SPEAKING
 -> WAITING

WARNING is an interruptible presentation state and must reference a real reported warning/GAP when connected to backend data.

## 6. Command vocabulary

SHOW_ALINA(mode)
HIDE_ALINA
MOVE_TO(anchor_id)
LOOK_AT(target_id)
PRESENT(panel_id)
OPEN_FULLSCREEN(panel_id)
CLOSE_FULLSCREEN
SET_BEHAVIOR(state)
SPEAK(message_ref)
SET_STATUS(status_ref)

Commands reference presentation/task objects; they do not contain canonical knowledge bodies.

## 7. Full-screen transition

Scene + FULL_BODY
 -> PRESENT(panel)
 -> OPEN_FULLSCREEN(panel)
 -> avatar mode becomes COMPACT/VOICE_ONLY/HIDDEN according to workspace policy
 -> workspace becomes primary
 -> dialogue/status persist
 -> CLOSE_FULLSCREEN
 -> restore previous scene/presence context

## 8. Makar example

ALINA task state: building Makar foundation
 -> GAP detected by backend
 -> Presentation Model exposes GAP
 -> SET_BEHAVIOR(WARNING)
 -> MOVE_TO(EVIDENCE_PANEL)
 -> PRESENT(EVIDENCE_PANEL)
 -> user opens full screen
 -> avatar may hide
 -> ALINA dialogue continues
 -> evidence workspace shows source-backed details.

## 9. Fallback

3D renderer unavailable
 -> Presence Controller marks renderer unavailable
 -> STATUS_ONLY or HIDDEN
 -> Work Table / panels remain operational
 -> dialogue remains operational
 -> no canonical task state is lost.

## 10. Next gate

Create executable test specification covering state, navigation, full-screen transitions, fallback, accessibility, truth-state preservation and regression.
