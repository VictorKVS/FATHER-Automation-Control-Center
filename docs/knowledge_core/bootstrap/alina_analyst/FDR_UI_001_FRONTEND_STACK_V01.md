# FDR-UI-001 — Frontend Stack for ALINA Control Center MVP

Status: ACCEPTED_FOR_M1
Decision class: D2
Scope: Beautiful Working MVP only
Date: 2026-09-23

## Problem
ENG-001 found no existing web frontend stack. M1 needs a new explicit web boundary without committing the ALINA super-project to a heavy permanent rendering/runtime architecture.

## Desired outcome
A small, fast, testable desktop-first frontend that supports component contracts, explicit state, DEMO/REAL separation, accessibility, future 2D/3D renderer adapters, and later replacement without rewriting canonical Knowledge Core.

## Constraints
- existing repository is primarily Python automation/control and documentation;
- no existing frontend framework must be preserved;
- M1 is an interaction shell, not the final ALINA runtime;
- 3D is optional for M1 and must remain behind an adapter;
- public repository must use sanitized fixtures only;
- analysis/passport/tests precede production implementation.

## Alternatives considered

### A — TypeScript + React + Vite
Strengths: small application boundary; mature component model; explicit TypeScript contracts; fast local development; straightforward test tooling; suitable for adapter-based 2D/3D integration.
Risks: adds Node toolchain to a Python-oriented repository; state discipline must be designed rather than delegated to framework magic.

### B — Next.js
Strengths: full application framework, routing/server features.
Why not M1: server rendering/full-stack conventions are not required by the first milestone and would add architecture before the backend boundary is known.

### C — Vanilla TypeScript/Web Components
Strengths: minimal framework dependency.
Why not M1: more custom UI/state composition work for a component-heavy interactive workspace; less useful leverage for rapid MVP iteration.

### D — Python-rendered UI/dashboard
Strengths: aligns with existing Python stack.
Why not M1: Control Center requires a rich interactive spatial client and replaceable avatar/board components; a Python dashboard would couple the new product UX to the automation repository's current execution style.

## Decision
Use **TypeScript + React + Vite** for M1 frontend.

This decision does NOT select:
- final 3D engine;
- final backend/API framework;
- canonical Knowledge Core database;
- final global state library;
- final design system.

Prefer React local/context state initially. Add a state library only when measured complexity justifies it.

## Component boundary
The frontend lives under:
`apps/alina-control-center/frontend/`

Contracts and sanitized fixtures remain adjacent but framework-independent:
`apps/alina-control-center/contracts/`
`apps/alina-control-center/fixtures/`

## 3D rule
No mandatory Three.js/react-three-fiber dependency in initial scaffold. `AlinaPresence` uses a renderer adapter. First runnable M1 may use an original lightweight 2D/CSS/SVG presentation while preserving the future volumetric contract.

## Validation
The decision is valid for M1 if:
1. shell runs locally;
2. component boundaries from UI-010 can be represented without architectural hacks;
3. WorkspaceState is explicit and restorable;
4. UI-007 P0 interaction tests can be automated;
5. reduced-motion/no-avatar path remains functional;
6. build does not require Knowledge Core backend.

## Reversal triggers
Revisit if:
- required 3D/rendering workflow proves incompatible;
- measured bundle/runtime constraints fail UI-008 targets;
- repository ownership changes to an established frontend stack;
- M2 backend integration exposes a material contract mismatch.

## Provenance
Derived from ENG-001 repository reconnaissance and UI-001..010 requirements. This is a FATHER design decision, not an externally sourced universal technology claim.
