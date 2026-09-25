# UI-010 — ALINA Control Center MVP Implementation Plan v0.1

Status: IMPLEMENTATION_PLAN_DRAFT
Scope: Beautiful Working MVP
Upstream: MVP-00; UI-001..UI-009
Production code gate: CONDITIONAL — real vertical-slice contract must be confirmed before data-connected implementation

## 1. Objective

Turn the approved Control Center architecture into the smallest real, attractive, replaceable MVP that proves:
USER <-> ALINA <-> WORK TABLE <-> BOARDS <-> CANONICAL FATHER OBJECTS.

Do not implement the full ALINA super-project in this phase.

## 2. Delivery strategy

Build in vertical increments that remain runnable:
P0 shell -> P1 workspace state -> P2 ALINA presentation -> P3 boards -> P4 real Knowledge vertical slice -> P5 Agent Stack -> P6 provenance -> P7 restore/fallback -> P8 polish -> P9 tests/evidence.

Each increment must preserve the contracts established in UI-001..009.

## 3. Frontend component boundaries

Candidate component tree:

```text
ControlCenterApp
├── ControlCenterShell
│   ├── HeaderStatus
│   ├── LeftDomainRail
│   ├── RightDomainRail
│   └── WorkspaceStage
├── AlinaPresence
│   ├── AvatarRendererAdapter
│   ├── AvatarStateController
│   └── AvatarFallback
├── WorkTable
│   └── ActiveObjectRenderer
├── BoardManager
│   ├── DeployableBoard
│   ├── BoardDock
│   └── BoardOverflow
├── AgentStack
│   ├── StackCompact
│   ├── StackExpanded
│   └── AgentLayerCard
├── ProvenanceNavigator
│   ├── EvidenceSummary
│   ├── FragmentView
│   ├── VersionView
│   └── SourceView
├── FocusMode
├── WorkspaceStateController
└── StatusTruthBadge
```

Component names are implementation candidates, not immutable public APIs.

## 4. Core frontend state

Separate domain/canonical references from presentation state.

```text
CanonicalRefs
- activeTaskId
- activeObjectRef
- activeObjectType
- objectVersionRef
- provenanceRefs

WorkspacePresentation
- workTableMode
- openBoardIds
- pinnedBoardIds
- minimizedBoardIds
- boardPositions
- focusMode
- avatarPresence
- avatarPosition
- renderMode
- sideRailState
- experimentVariantRefs
```

Never persist a copied canonical truth object merely to restore layout; persist references plus safe presentation state.

## 5. Data-access boundary

Frontend must depend on a stable adapter/service contract rather than direct database assumptions.

Candidate read operations:
- getObject(ref)
- getDocument(ref)
- getDocumentVersion(ref)
- getFragment(ref)
- getKnowledgeObject(ref)
- getEvidenceForKnowledge(ref)
- getSourceForEvidence(ref)
- getRelations(ref)
- getAgentFoundationSummary(agentRef)
- getAgentLayer(agentRef, layerId)

Candidate UI-state operations:
- loadWorkspaceState(workspaceId)
- saveWorkspaceState(workspaceState)

Exact transport may be REST/FastAPI or another existing FATHER interface; choose after repository/backend inspection.

## 6. Real vertical-slice contract — mandatory gate

Before implementing connected views, confirm or define canonical representations for:

```text
Source/Document
    ↓
DocumentVersion
    ↓
Fragment
    ↓
Evidence
    ↓
KnowledgeObject
```

Minimum cross-object fields:
- canonical ID;
- type;
- version/status;
- relation IDs;
- provenance/source reference;
- currentness where available;
- semantic type where applicable;
- REAL/DEMO boundary.

If current repository schemas differ, create an adapter. Do not redesign canonical Knowledge Core from the UI inward without impact analysis.

## 7. Fixture/demo contract

Create a separate explicit fixture namespace for PLANNED/DEMO screens.

Rules:
- fixture IDs cannot collide with canonical IDs;
- fixture objects carry data_status=DEMO;
- UI badges derive from data status;
- demo objects cannot be silently promoted into canonical persistence;
- the same component contract should allow later replacement by real data.

## 8. Suggested implementation phases

### Phase 0 — Repository reconnaissance
Inspect current frontend/backend/package structure, existing design system, routes, API clients, state management and Knowledge Core schemas. Produce an impact note before changing architecture.

### Phase 1 — Static runnable shell
Implement room composition, rails, Work Table placeholder, board zones and explicit DEMO/PLANNED labels. No fake backend claims.

### Phase 2 — Workspace state
Implement Work Table primary context, Board lifecycle, Back/history, Focus Mode and local/session persistence as appropriate.

### Phase 3 — ALINA presentation
Implement simplest replaceable ALINA renderer that meets MVP intent. Start with lightweight presentation; renderer behind adapter. Implement move/dock/collapse and avatar-off/fallback.

### Phase 4 — Real Knowledge vertical slice
Connect one canonical Source/Document -> Version/Fragment -> Evidence -> Knowledge object chain.

### Phase 5 — Provenance navigation
Implement reverse drill-down and deterministic return.

### Phase 6 — Agent Stack
Render ALINA structured stack from data; connect at least one layer to the real Knowledge/Evidence chain; mark remaining layers DEMO/PLANNED.

### Phase 7 — Restore/degraded states
Reload/restore, stale/unavailable states, backend outage behavior, reduced motion and no-avatar path.

### Phase 8 — Visual polish
High-fidelity visual system, depth, restrained glow, typography, transitions and ALINA identity. Polish must not break accessibility/readability/performance guardrails.

### Phase 9 — Tests and evidence
Execute UI-007 P0 path first, then P1 profiles. Capture test contexts, defects and release evidence.

## 9. Technology selection rule

Do not select a new framework merely because it is fashionable.

Prefer existing repository stack where suitable. Add dependencies only when they solve a tested requirement. Rich 3D libraries are optional until a lightweight prototype proves value within the target runtime profile.

## 10. Visual asset rule

Create original FATHER/ALINA assets. User/reference images are inspiration for composition and mood, not assets to copy.

Avatar assets/models are versioned and replaceable behind AvatarRendererAdapter.

## 11. Configuration / experiment hooks

MVP configuration should expose:
- avatar default presence;
- avatar default position;
- render/effects level;
- board placement policy;
- visible-board policy;
- provenance disclosure mode;
- Agent Stack default mode;
- Focus Mode avatar behavior.

No full experiment backend required.

## 12. Error/degraded-state policy

Frontend explicitly distinguishes:
LOADING;
REAL;
DEMO;
PLANNED;
UNAVAILABLE;
STALE;
ERROR;
UNKNOWN.

Do not turn backend failure into a generic success-looking screen.

## 13. Security/privacy baseline

Before connecting real data:
- do not expose local filesystem paths or secrets in public frontend;
- treat source/document content according to its access classification;
- log IDs/events needed for debugging without leaking sensitive source content;
- keep public GitHub artifacts sanitized;
- authentication/authorization boundaries follow the backend, not avatar/UI state.

## 14. Definition of first runnable milestone

MILESTONE M1:
- app opens to Control Center;
- room/rails/table visible;
- ALINA placeholder/presence visible;
- focus/minimal modes switch;
- one demo Board opens/closes;
- statuses clearly DEMO/PLANNED;
- no canonical data connected yet.

M1 is visual/interaction scaffolding, not MVP completion.

## 15. Definition of MVP completion candidate

MILESTONE M2:
- M1 plus real vertical slice;
- deterministic provenance/back path;
- structured ALINA Agent Stack with one real layer;
- avatar move/collapse/fallback;
- workspace restore;
- Focus Mode;
- REAL/DEMO separation;
- required UI-007 P0 tests executed with evidence;
- no release-blocking defects.

## 16. Immediate implementation blockers

B1 repository/frontend structure not yet inspected for this plan.
B2 real Knowledge vertical-slice schema/API not yet confirmed.
B3 target development workstation/runtime context not yet recorded.
B4 UI-001..009 are drafts requiring review during implementation planning; unresolved P0 contradictions must become GAP/FDR.

These blockers prevent blind production coding, not repository reconnaissance or creation of a safe implementation branch.

## 17. First engineering action

Perform repository reconnaissance and produce:
- current project tree relevant to web UI;
- package/runtime stack;
- existing routes/components;
- backend/API interfaces;
- Knowledge Core schema/artifacts;
- reusable components;
- conflicts with this plan;
- proposed minimal change set;
- exact M1 file plan.

Only after that should the first production component be created.
