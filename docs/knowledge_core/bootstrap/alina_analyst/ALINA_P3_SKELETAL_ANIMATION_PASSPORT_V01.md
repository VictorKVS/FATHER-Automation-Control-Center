# ALINA P3 Skeletal Animation Passport v0.1

## NEED / PROBLEM
P3 locomotion semantics are validated, but translating a VRM scene without skeletal animation leaves the temporary humanoid rigid. A production path must separate locomotion intent from pose/clip playback and must not make animation state the source of truth.

## PURPOSE
Define the boundary that converts ALINA BehaviorState into visible humanoid motion while preserving Presence Controller and locomotion state as canonical runtime intent.

## INPUT
- BehaviorState: IDLE, WALKING, PRESENTING and later LISTENING/THINKING/SPEAKING/WARNING/WAITING.
- VRM humanoid loaded by the renderer adapter.
- animation asset plus license/provenance record.
- reduced-motion policy.

## OUTPUT
- normalized AnimationIntent;
- selected animation clip;
- playback transition/crossfade;
- visible pose consistent with behavior;
- fallback when a clip cannot be loaded.

## NOTATION
Presence Controller -> Locomotion Controller -> Animation Intent Mapper -> Animation Adapter -> VRM humanoid
                                      |                              |
                                      +-> reduced-motion             +-> clip/procedural fallback

## RULES
1. WALKING must only be displayed while locomotion moving=true.
2. IDLE must not create positional movement.
3. PRESENTING may use a neutral standing pose before gesture clips exist.
4. Missing/unlicensed assets must fall back safely; they must never be silently fetched at runtime.
5. Animation assets require provenance, license, source and hash before repository/runtime promotion.
6. Reduced motion disables nonessential expressive motion but preserves state legibility.
7. The temporary Seed-san asset remains TEST_ONLY and is not a permanent ALINA identity.

## IMPLEMENTATION STRATEGY
Phase A: introduce typed AnimationIntent and pure mapping tests.
Phase B: introduce VRM animation adapter/mixer boundary.
Phase C: add an explicitly reviewed idle/walk asset or a procedural pose fallback.
Phase D: visual polygon checks for feet, root motion, orientation, clipping, arrival and crossfade.
Phase E: bind backend Presence Controller commands; remove temporary click trigger.

## QUALITY GATE
No clip is promoted merely because it looks acceptable. Gate requires:
- mapping tests green;
- license/provenance recorded;
- no fake locomotion;
- no runtime dependency on an uncontrolled external asset host;
- visual review on the actual ALINA polygon;
- fallback verified.

## CURRENT GAP
No reviewed skeletal idle/walk asset is committed yet. Therefore this passport deliberately does not claim that T-pose is solved.
