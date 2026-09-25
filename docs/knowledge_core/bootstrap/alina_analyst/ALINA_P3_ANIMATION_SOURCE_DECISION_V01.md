# ALINA P3 Animation Source Decision v0.1

## Decision
Use the Google XRBlocks VRM avatar demo as an implementation/reference benchmark, but do **not** copy its animation binaries into FATHER at this stage.

## Evidence reviewed
1. Google XRBlocks `demos/vrm-avatar/README.md` states that its demo retargets CC0 Mesh2Motion GLB animations, crossfades idle/walk, walks to a selected floor point, then returns to idle.
2. Its `main.js` resolves T-pose/idle/walk from a separate `xrblocks/proprietary-assets` repository/CDN.
3. The XRBlocks source repository itself is Apache-2.0, but that does not by itself establish redistribution terms for binaries hosted in the separately named proprietary-assets repository.
4. Pixiv three-vrm official examples demonstrate both direct Three.js humanoid animation and VRMA playback/retargeting.

## FATHER interpretation
The reference proves that the architecture we need is practical: VRM + idle/walk clips + retargeting + AnimationMixer/crossfade + locomotion. It does **not** satisfy FATHER's binary provenance gate for those specific external files.

## Result
- REUSE: architecture patterns and source-code concepts subject to their source licenses.
- DO NOT IMPORT YET: XRBlocks animation binaries.
- KEEP: FATHER's fail-closed local asset manifest.
- NEXT: either obtain an animation with explicit redistribution terms from its authoritative source, or generate/author a FATHER-owned neutral idle/walk pair and export it as VRMA.

## Why this matters
A repository README saying an upstream animation is CC0 is useful evidence, but FATHER's standard requires the actual promoted artifact to have traceable source, license and hash. A separate repository named proprietary-assets creates enough ambiguity to stop automatic redistribution.
