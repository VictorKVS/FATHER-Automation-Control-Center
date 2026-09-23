# M1-CP-001 — Control Center Shell & Contracts Passport v0.1

Status: PRE_IMPLEMENTATION_BASELINE
Depends on: FDR-UI-001, MVP-00, UI-001..010

## Why
M1 must prove the Control Center interaction model before real Knowledge Core integration.

## Responsibility
Render the command-room shell, ALINA presentation slot, one primary Work Table, deployable Boards, truth-status badges, Focus/Minimal modes, and restorable presentation state.

## Must not
- invent canonical Knowledge Core data;
- expose private/local data;
- imply DEMO objects are REAL;
- couple ALINA analytics to avatar rendering;
- require 3D or backend availability.

## Inputs
Sanitized FatherObject references, DemoWorkspace fixture, user interaction events, viewport/reduced-motion settings.

## Outputs
Visible workspace; WorkspaceState; board lifecycle events; avatar presentation state; explicit data-status presentation.

## Core contracts

### FatherObject
- id
- type
- title
- version
- dataStatus: REAL | DEMO | PLANNED | UNAVAILABLE | STALE | UNKNOWN
- provenanceRefs[]
- relationRefs[]

### WorkspaceState
- version
- activeObjectRef
- workTableMode
- openBoardIds[]
- pinnedBoardIds[]
- minimizedBoardIds[]
- focusMode
- avatarPresence
- avatarPosition
- renderMode

### BoardState
- id
- type
- objectRef
- state: OPEN | PINNED | MINIMIZED | CLOSED
- relationToPrimary
- dataStatus

## Internal blocks
ControlCenterShell -> AlinaPresence + WorkTable + BoardManager + StatusTruthBadge + WorkspaceStateController.

## Failure behavior
Bad/missing fixture -> explicit ERROR/UNAVAILABLE state.
Avatar renderer failure -> fallback presentation; Work Table remains usable.
Unknown status -> UNKNOWN, never inferred REAL.
Restore mismatch -> safe baseline + visible stale/restore warning.

## Security
Fixtures sanitized; no secrets, PII, absolute local paths or private document payloads.

## Replaceability
Visual renderer, board renderer and persistence adapter are replaceable behind contracts.

## Quality gate
Implementation may begin only after M1 tests below exist as specification.
