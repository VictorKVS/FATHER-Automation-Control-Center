# ALINA 3D — EXECUTION CHAIN v0.1

Status: EXECUTION BASELINE
Decision owner: Viktor
Execution mode: one approval for the chain; intermediate technical decisions are delegated unless a stop condition is reached.

## Goal

Reach a working browser prototype in which a game-like ALINA inhabits the Control Center, can move between Work Table and Information Wall, present a panel, yield the screen to a full-screen workspace, and continue dialogue when visually hidden.

## Execution chain

1. P1 WORLD
   - add isolated 3D dependencies;
   - create Canvas/scene/camera/lights/floor/room;
   - implement canonical scene anchors A0-A4;
   - add debug geometry for spatial validation.
   Gate: tests + build + readable camera composition.

2. P2 BODY
   - integrate AvatarRendererAdapter;
   - load a temporary license-cleared humanoid/VRM or use a neutral placeholder if asset review blocks;
   - bind body root to Presence Controller state.
   Gate: avatar can be shown/hidden without affecting workspace/task state.

3. P3 LOCOMOTION
   - map MOVE_TO to physical target;
   - idle/walk/turn;
   - arrival tolerance and completion event;
   - LOOK_AT/PRESENT orientation.
   Gate: deterministic A0 -> A1 -> panel presentation demo.

4. P4 WORKSPACE TRANSITION
   - connect Knowledge/Graph/Evidence scene panels;
   - OPEN_FULLSCREEN/CLOSE_FULLSCREEN;
   - preserve scene, selected object, dialogue and task context;
   - avatar auto-reduces/hides by policy.
   Gate: 3D -> full-screen panel -> same 3D context round trip.

5. P5 PRESENCE FALLBACK
   - renderer failure fallback;
   - reduced-motion behavior;
   - FULL_BODY/COMPACT/VOICE_ONLY/HIDDEN/STATUS_ONLY;
   - no essential information only in animation/audio.
   Gate: workspace remains usable with 3D disabled.

6. P6 VOICE PREP
   - define audio/viseme adapter boundary;
   - do not lock to a production voice provider;
   - connect SPEAK state to presentation behavior using mock audio/event timing first.
   Gate: speech channel can be replaced independently of avatar/backend.

7. P7 PROTOTYPE REVIEW
   - automated tests;
   - production build;
   - screenshots/video/manual spatial review;
   - collect baseline performance rather than invent thresholds;
   - register visual/performance gaps.
   Gate: PROTOTYPE_ACCEPTED or REWORK.

## Delegated intermediate decisions

May proceed without separate user approval:
- file/component names;
- internal TypeScript types;
- scene coordinates and camera values;
- test fixture values;
- temporary debug geometry;
- minor refactors required by tests;
- dependency wiring consistent with this chain;
- fixes for CI/build/test failures;
- documentation/journal updates.

## Stop conditions requiring user review

Stop and surface a decision if any of the following occurs:
- architecture must violate Workspace First / Avatar Optional;
- canonical FATHER/ALINA state would need to live inside the renderer;
- repository boundary must materially change;
- license of a desired permanent avatar/environment asset is unclear or restrictive;
- a paid/external provider must be selected;
- permanent ALINA appearance/voice/persona choice is required;
- security/privacy boundary changes;
- significant replacement of the existing Control Center is proposed;
- measured prototype results show the selected web-3D approach is not viable.

## Continuous controls

For every stage:
Passport/notation/test baseline already governs the prototype.
Implementation -> automated tests -> build -> journal -> next stage.
Failures become explicit GAPs and are fixed before claiming PASS.
No fake telemetry. No unreviewed third-party assets. No PII/secrets in public fixtures.
