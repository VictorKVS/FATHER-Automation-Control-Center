# ALINA Control Center

Beautiful Working MVP for the FATHER human-facing analytical workspace.

Status: M1 SCAFFOLDING.

This application boundary is intentionally separate from the existing automation-control scripts and from the future canonical Knowledge Core runtime.

## M1 rules
- sanitized DEMO fixtures only until a real Knowledge Core adapter is approved;
- DEMO/PLANNED/UNKNOWN must never be presented as REAL;
- canonical object references are separate from workspace presentation state;
- ALINA visual rendering is replaceable and must not be required for analytical workspace operation;
- no secrets, personal data, private documents or absolute local paths in this public repository.

## Contracts
See `contracts/`. They are framework-independent and precede the frontend implementation.

## Next
Scaffold the React/Vite frontend against these contracts and implement M1 tests T01-T10.
