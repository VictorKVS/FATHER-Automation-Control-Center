# UI-008 — Workload, Performance & Accessibility Profiles v0.1

Status: PROFILE_DRAFT
Scope: MVP-00
Upstream: UI-007 Pre-Implementation Test Specification
Implementation: BLOCKED until review + target runtime confirmation

## 1. Purpose

Define representative operating contexts in which ALINA Control Center MVP must remain useful, readable and responsive. These profiles provide valid context for UI-007 measurements; they do not invent universal performance thresholds.

## 2. Primary target

MVP is desktop-first for sustained analytical work.

Primary interaction assumptions:
- keyboard + mouse;
- large desktop browser viewport;
- long document/knowledge sessions;
- several related boards, not a wall of dashboards;
- ALINA may render in rich or degraded mode;
- canonical backend may be local/LAN/remote depending on deployment.

Mobile is not a release-blocking full-workspace target for MVP. A safe informational/degraded view may be added later.

## 3. Viewport profiles

VP-A STANDARD_DESKTOP
- target class: approximately 1920x1080 logical workspace class;
- expected: full room composition, central table, ALINA, limited boards.

VP-B COMPACT_DESKTOP
- target class: approximately 1366x768 / similar laptop workspace;
- expected: reduced side domains, tighter board policy, avatar auto-suggestion/collapse where needed.

VP-C WIDE_DESKTOP
- target class: ultrawide/high-resolution desktop;
- expected: more peripheral room available, but no automatic increase in information density merely because space exists.

VP-D DEGRADED_SMALL
- below supported comfortable workspace;
- expected: focus/single-context layout, reduced visual layers, explicit limitation where appropriate.

Exact breakpoints are implementation/test decisions, not fixed by this profile document.

## 4. Workload profiles

W0 IDLE_ROOM
Control Center open, no active object.

W1 DOCUMENT_FOCUS
One real document/knowledge object on Work Table; ALINA EYES/MINIMAL; zero or one board.

W2 NORMAL_ANALYSIS
One primary object + two active boards + ALINA compact/full as space permits.

W3 PROVENANCE_TRACE
Primary object + sequential Knowledge/Evidence/Fragment/Source drill-down.

W4 AGENT_INSPECTION
ALINA Agent Stack expanded + one focused layer + related board.

W5 BUSY_WORKSPACE
Primary object + several requested boards, some pinned/minimized; used to test organization/overload behavior.

W6 DEGRADED_RENDER
Same useful task with no rich 3D.

W7 BACKEND_DEGRADED
UI state present while canonical backend is slow/unavailable/stale.

W8 RESTORE
Reload/reopen a previously populated workspace.

## 5. Render capability profiles

R-A RICH
Hardware/browser supports intended rich rendering.

R-B LIGHT
Reduced 3D/WebGL/Canvas complexity.

R-C TWO_D
2D avatar/presence and ordinary UI surfaces.

R-D STATUS_ONLY
No avatar imagery required; status/presence indicator only.

Rule: analytical functionality must not depend on R-A.

## 6. Accessibility profiles

A0 DEFAULT.

A1 REDUCED_MOTION
- remove/shorten nonessential movement;
- replace spatial animation with state-preserving transitions;
- no meaning encoded only in motion.

A2 KEYBOARD_ORIENTED
- primary workflow reachable without precision dragging where supported;
- visible focus;
- deterministic order;
- alternatives for drag/dock operations.

A3 LOW_VISUAL_EFFECT
- reduced glow/transparency/depth effects;
- maintain hierarchy/readability.

A4 COLOR_INDEPENDENT_STATUS
- REAL/DEMO/PLANNED/UNAVAILABLE, warning, gap and currentness states have text/icon/shape cues, not color alone.

A5 AVATAR_OFF
- user can work without rendered avatar;
- ALINA functionality/status remains reachable through non-avatar UI.

## 7. Representative browser/runtime matrix

MVP target should validate at least:
- current Chromium-family desktop browser on Windows;
- one secondary modern desktop browser if practical;
- reduced-render path independent of advanced 3D capability.

Exact versions are captured at test execution time rather than frozen here.

## 8. Performance metric candidates

Record under explicit TEST_CONTEXT:
- initial shell usable time;
- active-object open latency;
- board open/close/pin response;
- provenance navigation response;
- workspace restore time;
- avatar collapse/reposition response;
- frame/render stability for rich modes;
- CPU/GPU/memory footprint where meaningful;
- backend wait/error handling;
- long-session memory growth.

No pass/fail numbers are set until representative hardware and an implementation prototype exist.

## 9. Responsiveness principle

For direct manipulation, perceived response should be immediate enough that the user does not question whether the action registered. If an operation depends on backend/research work, UI must acknowledge the action and expose truthful progress/state rather than freeze.

Quantitative latency budgets are established empirically in the implementation benchmark.

## 10. Long-session profile

LONG_SESSION:
- representative document/analysis task;
- repeated board open/close;
- provenance drill-down;
- focus mode;
- avatar collapse/restore;
- context switches;
- idle periods;
- backend calls.

Observe:
- memory/resource growth;
- visual fatigue/friction;
- lost context;
- accidental board/avatar obstruction;
- navigation repetition;
- state drift;
- stale-status clarity.

## 11. Failure injection profiles

F1 avatar renderer fails.
F2 Knowledge Core/backend unavailable.
F3 slow backend.
F4 canonical object becomes stale/superseded.
F5 board data unavailable.
F6 workspace state partially corrupt/incompatible version.
F7 unsupported rich-render capability.

Expected: degrade explicitly, preserve recoverable context where safe, never replace missing REAL data with silent DEMO.

## 12. MVP hardware policy

Do not design only for a high-end GPU workstation.

The MVP must have a useful non-rich path on ordinary desktop/laptop hardware. Rich avatar/room rendering is an enhancement layer.

Before benchmarks, record the user's actual development workstation as one target profile and add at least one lower-capability profile or throttled/degraded equivalent.

## 13. Data/load profiles

D0 DEMO_FIXTURE — explicit fixtures only.
D1 REAL_VERTICAL_SLICE — one real canonical Source->Knowledge->Evidence path.
D2 SMALL_WORKSPACE — limited objects/relations.
D3 GROWING_WORKSPACE — enough objects to reveal navigation/render scaling issues.

Large production-scale Knowledge Core performance is outside UI MVP acceptance unless it directly affects the selected vertical slice.

## 14. Valid comparison rule

A/B or version comparison is valid only when:
- same workload profile;
- compatible viewport;
- same or recorded render capability;
- same data/fixture version;
- comparable backend state;
- same metric definition;
- sufficient repeated observations;
- no hidden change in another component invalidates attribution.

## 15. Exit gate

UI-008 may become PROFILE_BASELINE when:
- primary target environment is confirmed;
- viewport/workload/accessibility/render profiles are accepted;
- at least one development workstation context is recorded;
- UI-007 tests map to these profiles;
- no unsupported performance threshold is presented as fact.

## 16. Next step

UI-009 defines A/B experiment hypotheses for layout, ALINA presence and board behavior. Separately, the real MVP vertical-slice data contract must be identified before UI-010 Implementation Plan can unlock production code.
