# ALINA P3.1 — Reference Animation Benchmark v0.1

## Purpose
Select the fastest evidence-backed animation path for ALINA without building a humanoid animation engine from zero.

## Failure that triggered this benchmark
The P3 visual polygon proved that root locomotion and turning work, but the hand-authored procedural skeleton mutator can break avatar integrity. Therefore P3 remains unaccepted until the avatar can complete IDLE -> WALK -> ARRIVAL/IDLE -> PRESENT without skeletal corruption.

## Architecture boundary
Presence Controller -> Locomotion Controller -> AnimationIntent -> Animation Runtime -> VRM.

Locomotion owns world-space position/orientation. Animation owns skeletal motion. Animation clips must not silently become the source of world-space navigation.

## Candidates

### A. Official @pixiv/three-vrm + @pixiv/three-vrm-animation — PRIMARY
Use the already integrated VRM runtime, VRMA loader, createVRMAnimationClip and THREE.AnimationMixer. This is the smallest architectural change and keeps the runtime close to the official VRM implementation.

### B. norio/vrm-game-starter — REFERENCE / ADAPT
Study its shared animation library retargeting, idle/walk/run contracts, character controller separation and Foot IK. Reuse source mechanisms only after license/provenance review. Bundled assets are independently licensed and are not implicitly approved for FATHER redistribution.

### C. Mixamo -> VRM retargeting — SECONDARY INPUT PATH
The official three-vrm examples demonstrate loading a Mixamo animation onto VRM. Treat Mixamo/other animation files as acquisition inputs subject to the FATHER asset gate, not as runtime network dependencies.

## Decision
Use A as the production spine. Study/adapt B for proven retargeting/controller/IK techniques. Keep C as an asset acquisition/retargeting route. Do not continue procedural gait as the primary path.

## P3 minimal motion set
1. IDLE_NEUTRAL
2. WALK_FORWARD
3. ARRIVAL -> IDLE_NEUTRAL
4. PRESENT_NEUTRAL

No large motion library is required to close P3.

## Acceptance gates
- G1 VRM body remains structurally intact while root locomotion runs with skeletal animation disabled.
- G2 IDLE clip preserves body integrity for >= 10 seconds.
- G3 WALK clip loops while Locomotion Controller moves root toward INFORMATION_WALL.
- G4 arrival cross-fades WALK -> IDLE/PRESENT without teleport or detached limbs.
- G5 no unreviewed runtime asset download.
- G6 every accepted animation asset has source, license/status and SHA-256.
- G7 automated tests remain green and a local browser/GPU visual polygon provides final evidence.

## Current implementation action
The primary AlinaScene runtime no longer calls proceduralPose. The next visual polygon is intentionally a skeleton-integrity isolation test: the avatar may slide/turn without a walk cycle, but its body must remain intact.

## Promotion rule
Only after G1 passes do we bind the clip-based animation runtime behind AnimationIntent. P4 workspace interaction remains blocked until P3 visual acceptance.
