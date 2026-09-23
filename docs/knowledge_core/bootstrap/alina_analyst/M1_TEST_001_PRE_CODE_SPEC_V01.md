# M1-TEST-001 — Pre-code Test Specification v0.1

Status: TEST_SPECIFIED
Scope: first runnable ALINA Control Center shell

## T01 Startup
Given sanitized demo fixture, app opens without backend and renders shell, ALINA presence, Work Table and domain rails.
Acceptance: no blank/fatal screen.

## T02 Truth status
Given DEMO/PLANNED/UNKNOWN objects, each is visibly represented with its actual status.
Acceptance: none is rendered as REAL.

## T03 Board lifecycle
Open one board, pin/minimize/restore/close it.
Acceptance: transitions follow UI-003 and active Work Table object is not lost.

## T04 Focus mode
Enter and exit Focus Mode.
Acceptance: active object/context survives and secondary UI de-emphasizes.

## T05 Avatar collapse
FULL/COMPACT presentation -> EYES/STATUS -> restore.
Acceptance: analytical/workspace state is unchanged.

## T06 Avatar failure
Simulate renderer unavailable.
Acceptance: fallback status/presence appears and Work Table remains usable.

## T07 Workspace restore
Change board/avatar/focus state, serialize, restore.
Acceptance: valid presentation state returns; canonical truth is referenced, not duplicated.

## T08 Reduced motion
Enable reduced-motion profile.
Acceptance: critical state remains understandable without motion.

## T09 Invalid fixture
Load malformed/missing object reference.
Acceptance: explicit ERROR/UNAVAILABLE, no invented content.

## T10 Public-fixture hygiene
Contract test scans committed fixture for forbidden absolute local paths and obvious secret fields.
Acceptance: zero findings.

## Implementation gate
T01-T10 are the required initial test targets. Production scaffold may now be created, but M1 is not VALIDATED until the tests are implemented and executed.
