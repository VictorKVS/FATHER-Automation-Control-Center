# ENG-001 — Repository Reconnaissance for ALINA Control Center MVP v0.1

Status: COMPLETE_FOR_CURRENT_REPOSITORY_SNAPSHOT
Branch inspected: feature/father-knowledge-formation-standard-v01
Purpose: satisfy UI-010 Phase 0 before production UI code.

## 1. Result

The current FATHER-Automation-Control-Center repository is not yet a web application repository.

It currently contains:
- Python automation/control scripts;
- Python unit tests;
- machine-readable registries (JSON/CSV);
- generated/hand-authored reports;
- Knowledge Core / ALINA architecture documents;
- GitHub Actions workflows;
- storage handoff artifacts.

No existing web frontend application, frontend package manifest, web routes/components, browser state manager, backend API service, database migrations, PostgreSQL schema, or canonical Knowledge Core runtime implementation was found in the inspected tree.

Therefore there is no existing frontend framework to preserve or extend in this repository.

## 2. Current executable stack observed

Repository README identifies:
- Python scripts such as build_dashboard.py and estimate_capacity.py;
- unittest-based tests;
- JSON/CSV registries as machine-readable operational data.

The tree also contains model inventory/dedup Python scripts and their tests.

This is useful operational tooling, but it is not the planned Control Center application runtime.

## 3. Existing web/frontend findings

Observed:
- no package.json;
- no pnpm/yarn/npm lockfile;
- no src/app/pages/components frontend tree;
- no Vite/Next/React application structure;
- no static web application directory identified;
- no browser routes identified.

Conclusion: M1 needs a new web application boundary rather than modifications to an existing frontend.

## 4. Existing backend/API findings

Observed:
- no FastAPI/Flask/Django service structure identified;
- no API routes/controllers identified;
- no OpenAPI contract identified;
- no service layer exposing Knowledge Core objects.

Conclusion: UI-010 candidate operations such as getObject/getEvidence/getRelations are design contracts only, not existing endpoints.

## 5. Existing Knowledge Core runtime findings

The repository contains detailed Knowledge Core standards and bootstrap design artifacts, but the inspected tree does not contain a confirmed runtime schema for:
Source/Document -> DocumentVersion -> Fragment -> Evidence -> KnowledgeObject.

No PostgreSQL migration/schema directory was identified.

Conclusion: B2 from UI-010 remains active. A real vertical slice cannot yet be truthfully connected from this repository alone.

## 6. Reusable assets

Directly reusable now:
- Knowledge formation/packaging standards;
- Knowledge Packet contract;
- regulatory/currentness design;
- ALINA C00-C03 bootstrap artifacts;
- MVP-00 and UI-001..010 specifications;
- operational registry principles: unknown values remain unknown, evidence before maturity claims;
- GitHub CI pattern and Python test discipline.

Potentially reusable later through adapters:
- registry JSON/CSV data for a FATHER operations board;
- generated status/capacity reports.

These operational registries must not be mistaken for the canonical Knowledge Core.

## 7. Architecture conflict check

No existing web framework conflict exists because no web application was found.

Primary architecture risk is different: creating UI code inside the automation-control root could mix three responsibilities:
1. automation/stream control;
2. Knowledge Core runtime;
3. human-facing Control Center.

Recommendation: create an explicit application boundary.

## 8. Proposed repository boundary

For the current repository, the minimal safe structure is:

```text
apps/
  alina-control-center/
    README.md
    frontend/
    contracts/
    fixtures/
    tests/

docs/
  knowledge_core/
    ...existing design source...

scripts/
registry/
reports/
tests/
...existing automation-control assets...
```

Do not create backend/database folders until the Knowledge Core runtime ownership decision is made.

If FATHER later adopts a monorepo, backend packages can be added under explicit services/packages boundaries.

## 9. M1 exact file plan

M1 is scaffolding only and may use DEMO fixtures.

Proposed first files:

```text
apps/alina-control-center/
├── README.md
├── contracts/
│   ├── workspace-state.schema.json
│   └── father-object.schema.json
├── fixtures/
│   └── demo-workspace.json
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   │   ├── ControlCenterShell
│   │   │   ├── AlinaPresence
│   │   │   ├── WorkTable
│   │   │   ├── BoardManager
│   │   │   └── StatusTruthBadge
│   │   └── state/
│   └── tests/
└── tests/
    └── contract/
```

Exact framework-generated filenames depend on the framework decision.

## 10. Framework decision required before M1 code

Because there is no existing frontend stack, framework selection is now a real FATHER Design Decision.

Decision criteria:
- fast desktop MVP development;
- component/state model;
- testability;
- future 2D/3D adapter compatibility;
- accessibility;
- maintainability;
- developer familiarity;
- avoid unnecessary infrastructure.

Candidate baseline to evaluate: TypeScript + React + Vite for the shell, with rich 3D deferred behind an adapter.

This is a candidate, not yet a released decision.

## 11. Data-contract decision

Before M2 real-data work, identify where canonical Knowledge Core runtime will live:
A. in this repository as explicit backend/service packages;
B. in a dedicated Knowledge Core repository/service;
C. in an existing external FATHER service connected by adapter.

Until decided, M1 must use explicit DEMO fixtures and contract interfaces only.

## 12. Security/public-repository constraint

The repository is currently public in the working context. Do not commit:
- local absolute paths;
- private source documents;
- personal data;
- secrets/tokens;
- production database dumps;
- sensitive Knowledge Core payloads.

Only sanitized contracts/fixtures may be used for M1.

## 13. Blocker status after reconnaissance

B1 repository structure not inspected -> RESOLVED.
B2 real Knowledge schema/API unconfirmed -> OPEN P0 for M2.
B3 target workstation/runtime context -> OPEN for benchmark baseline.
B4 design drafts review -> OPEN, but no discovered P0 contradiction blocks safe M1 scaffolding.

## 14. Next gate

Before generating frontend production files:
1. create FDR for frontend/framework choice;
2. define M1 component passports/contract schemas;
3. define M1 tests from UI-007 subset;
4. then scaffold the runnable M1 application.

This preserves the FATHER rule:
analysis -> passport/contract -> tests -> implementation.
