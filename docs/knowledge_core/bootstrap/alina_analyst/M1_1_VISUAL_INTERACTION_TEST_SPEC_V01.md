# ALINA Control Center M1.1 — Visual & Interaction Test Specification v0.1

Status: PRE_IMPLEMENTATION_TEST_BASELINE  
Trace: Entry 0044 / UI-GAP-001 / M1.1 Passport / M1.1 Spatial Scheme.

## Purpose

Define falsifiable acceptance checks before visual implementation. These tests supplement, not replace, the validated M1 T01-T10 suite.

| ID | Test | Expected result |
|---|---|---|
| V01 | Primary hierarchy | Information Wall, ALINA and Work Table are all present and represented as distinct semantic regions. |
| V02 | Work Table priority | Work Table exposes current object/title/status and remains the primary task surface. |
| V03 | Information Wall | Knowledge, Graph, Evidence and Activity/Status surfaces exist as a coordinated wall group. |
| V04 | ALINA presence | ALINA has a dedicated central presence region and is not represented only as a tiny toolbar icon. |
| V05 | Truth visibility | DEMO/PLANNED/UNAVAILABLE truth states remain visible and no fixture is silently presented as REAL. |
| V06 | Focus Mode | Focus Mode reduces peripheral presentation while retaining current object and truth status. |
| V07 | Renderer failure | STATUS_ONLY fallback preserves Work Table usability and system status. |
| V08 | Board lifecycle | Board open/close behavior survives the new composition. |
| V09 | Reduced motion | prefers-reduced-motion removes nonessential animation without hiding information. |
| V10 | Responsive containment | At desktop review viewport, primary regions do not overlap destructively or leave the Work Table off-screen. |
| V11 | Keyboard/control identity | Interactive controls retain accessible names and keyboard-operable native controls. |
| V12 | Public/demo hygiene | No secrets, PII, private documents or local absolute paths are introduced into public fixtures/UI. |
| V13 | Existing regression | Original M1 T01-T10 executable suite remains green. |
| V14 | Build gate | TypeScript compilation and Vite production build remain green. |

## Visual review protocol

Capture a full-page screenshot at the same general desktop class used for the M1 baseline. Compare BEFORE and AFTER against the passport rather than a subjective beauty score. Record observed hierarchy, empty-space use, ALINA prominence, Work Table prominence, wall coherence, truth-state clarity and any new interaction defects.

## Release rule

No M1.1 GREEN claim from appearance alone. Required: executable regression tests + production build + browser screenshot review. User visual judgment is recorded as qualitative evidence, not substituted for functional test evidence.
