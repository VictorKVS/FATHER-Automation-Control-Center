# UI-005 — Knowledge / Evidence / Provenance Navigation v0.1

Status: NOTATION_DRAFT
Scope: MVP-00
Upstream: Knowledge Formation Standard; UI-003 Work Table & Boards; UI-004 Agent Stack
Implementation: BLOCKED until review + UI-007 tests

## 1. Purpose

Define the user's traceable navigation from a visible FATHER knowledge/agent result back to the evidence and original source that supports it, while preserving the active workspace context.

The interface must make trust inspectable without forcing the user to leave the Control Center.

## 2. Canonical trace

Forward formation:
```text
ORIGINAL SOURCE
 -> DOCUMENT
 -> DOCUMENT VERSION
 -> FRAGMENT
 -> EVIDENCE
 -> KNOWLEDGE OBJECT
 -> RELATION / DECISION RULE
 -> TASK / DECISION / SPECIALIST OUTPUT
```

Reverse inspection:
```text
VISIBLE RESULT
 <- DECISION / RELATION
 <- KNOWLEDGE OBJECT
 <- EVIDENCE
 <- FRAGMENT
 <- DOCUMENT VERSION
 <- ORIGINAL SOURCE
```

Not every MVP object will contain every stage. Missing stages must be explicit rather than fabricated.

## 3. User interaction path

Example:
```text
WORK TABLE: Knowledge K-17
   ↓ Why / Evidence
EVIDENCE BOARD: E-4
   ↓ Show exact support
FRAGMENT BOARD: F-22
   ↓ Document context
SOURCE/VERSION BOARD: DV-3
   ↓ Original
SOURCE OBJECT
   ↓ Back
DV-3 -> F-22 -> E-4 -> K-17
```

The user must be able to return to the exact prior workspace context.

## 4. Provenance object card

Where data exists, expose:
- canonical object ID;
- object type;
- source/document identity;
- document version;
- fragment locator/page/section/paragraph where applicable;
- evidence relation type;
- extraction/formation method;
- created/observed timestamp;
- currentness/status;
- supersedes/superseded_by;
- confidence only when methodologically defined;
- contradiction/gap references;
- processing lineage;
- data status REAL | DEMO | PLANNED | UNAVAILABLE.

Do not display unsupported precision.

## 5. Evidence semantics

UI must preserve semantic distinction between:
FACT;
CLAIM;
INFERENCE;
HYPOTHESIS;
REQUIREMENT;
DECISION.

Visual treatment may differ, but semantic type comes from canonical data. The UI must not silently convert a CLAIM into a FACT or an INFERENCE into EVIDENCE.

## 6. Evidence strength vs currentness

These are independent dimensions.

A source/evidence item may be authoritative but old, or current but weak for a particular claim. The UI must not compress them into one trust color/score.

Currentness candidates:
CURRENT_VERIFIED;
CURRENT_PENDING_RECHECK;
CHANGE_DETECTED;
OUTDATED;
SUPERSEDED;
REPEALED;
SOURCE_UNAVAILABLE;
CURRENTNESS_UNKNOWN.

Only display states available from the canonical backend.

## 7. Contradictions

If knowledge objects or evidence conflict:
```text
KNOWLEDGE K-17
   ├── SUPPORTS <- E-4
   └── CONTRADICTED_BY <- E-9
```

The UI opens both evidence branches. It does not resolve the conflict merely for visual cleanliness.

Possible states:
UNRESOLVED;
REVIEW_REQUIRED;
RESOLVED_BY_DECISION;
SUPERSEDED_CONTEXT.

## 8. Missing evidence / gaps

If the trace cannot be completed:
```text
RESULT
  ↓
KNOWLEDGE
  ↓
EVIDENCE = MISSING
  ↓
GAP / RESEARCH ORDER
```

The user should see "evidence unavailable / gap" rather than an empty-looking success state.

## 9. Source version navigation

A document is not equal to a version.

```text
DOCUMENT
  ├── VERSION v1
  ├── VERSION v2
  └── VERSION v3 [current if verified]
```

When a newer version exists, historical knowledge remains linked to the version from which it was derived. The UI may offer impact/currentness navigation without silently relinking old knowledge.

## 10. Agent Stack integration

From any Agent Stack layer:
```text
SPECIALIST
 -> LAYER
 -> KNOWLEDGE / METHOD / COMPETENCY
 -> EVIDENCE
 -> SOURCE
```

This lets the user inspect why a specialist has a capability or why a particular output references specific knowledge.

Avatar appearance is never evidence.

## 11. MVP visual grammar

Use progressive disclosure:
1. normal work view shows compact provenance indicator;
2. first expansion shows evidence summary/status;
3. second expansion shows exact fragment/version/source;
4. deeper graph/impact/history views are on demand.

Do not permanently fill the room with provenance panels.

## 12. Real vertical slice acceptance

MVP must implement at least one real chain using canonical IDs:
SOURCE/DOCUMENT -> VERSION/FRAGMENT -> EVIDENCE -> KNOWLEDGE OBJECT -> UI.

The user must be able to navigate the reverse path and return to the original Work Table context.

## 13. Demo boundary

If some trace stages are not yet implemented:
- label them PLANNED/UNAVAILABLE;
- do not synthesize fake fragment IDs, citations, timestamps or currentness;
- demo fixtures are allowed only under explicit DEMO state.

## 14. Failure cases for UI-007

Test later:
- evidence missing;
- source unavailable;
- source version superseded;
- conflicting evidence;
- unknown currentness;
- stale board after source update;
- broken relation;
- canonical object permission denied;
- user follows a deep trace then returns;
- backend unavailable during trace;
- DEMO and REAL objects shown in same workspace.

## 15. Quality gate

UI-005 is ready for wireframing when:
- reverse provenance path is deterministic;
- semantic types remain distinct;
- currentness is independent from evidence strength;
- contradictions/gaps are visible;
- document/version distinction is preserved;
- no missing link is silently fabricated;
- Work Table context survives drill-down and return;
- one real vertical slice is identifiable.

## 16. Next step

UI-006 creates the first low-fidelity end-to-end MVP wireframe combining:
room + ALINA + Work Table + Boards + Agent Stack + Knowledge/Evidence/Source navigation.
