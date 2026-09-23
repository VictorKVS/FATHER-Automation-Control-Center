# FATHER Regulatory Knowledge Foundation & ALINA Control Center v0.1

Status: DEVELOPMENT FOUNDATION

## 1. Architectural decision

The regulatory/legal knowledge hierarchy is a first-class foundation of FATHER Knowledge Core and a first-class projection in ALINA Control Center.

It is not a folder taxonomy. Documents, versions, fragments, requirements, applicability decisions, controls, responsible roles and competencies are graph objects with provenance.

## 2. Regulatory knowledge layers

```text
L1 GENERAL LEGAL FOUNDATION
  constitutional/general legal norms
  federal laws
  decrees
  government regulations
  general technical regulations
  general standards/GOST
        |
L2 INDUSTRY SELECTION
  healthcare / construction / finance / industry /
  education / communications / energy / transport / IT / ...
        |
L3 INDUSTRY REGULATORY FOUNDATION
  industry laws
  industry regulations
  technical regulations
  industry standards/GOST
  codes/rules/classifiers/methodological documents
        |
L4 REGULATORS AND SUPERVISION
  authority
  mandate
  regulated objects
  applicability domain
        |
L5 DEPARTMENTAL / REGULATOR ACTS
  orders
  directives
  regulations
  instructions
  regulator requirements
  methodological documents
  clarifications (kept distinct from binding acts)
        |
L6 ORGANIZATION / LOCAL ACTS
  local orders
  policies
  staffing
  organization structure
  job descriptions
  procedures
  internal standards
```

## 3. Requirement chain

```text
LAW / STANDARD / ORDER
 -> REQUIREMENT
 -> APPLICABILITY
 -> OBLIGATION / PROHIBITION / PERMISSION
 -> CONTROL
 -> EVIDENCE OF COMPLIANCE
 -> RESPONSIBLE ROLE
 -> COMPETENCY
 -> SPECIALIST
```

Reverse traversal must answer why a local control, duty or specialist competence exists.

## 4. Legal status and time

Document/version status is explicit:

```text
DRAFT
PUBLISHED
ACTIVE
AMENDED
SUSPENDED
REPEALED
SUPERSEDED
UNKNOWN
```

Required temporal fields include publication, effective-from/effective-to and version relations. Historical versions are never overwritten.

Legal force, territorial scope, industry/domain scope and applicability to a concrete object are separate dimensions. Hierarchical rank alone does not prove applicability.

## 5. Regulatory graph relations

The controlled vocabulary is extended with:

```text
CONTAINS
ESTABLISHES
AMENDS
REPEALS
SUPERSEDES
APPLIES_TO
REGULATED_BY
ISSUED_BY
IMPLEMENTS
DERIVED_FROM
REQUIRES_CONTROL
EVIDENCED_BY
ASSIGNED_TO_ROLE
REQUIRES_COMPETENCY
```

## 6. ALINA Control Center projections

The site must expose the same canonical data through multiple projections:

```text
KNOWLEDGE GRAPH     what ALINA knows
REGULATORY GRAPH    why requirements exist and where they apply
EVIDENCE GRAPH      why knowledge is trusted
TASK GRAPH          what work ALINA understands
COMPETENCY GRAPH    what specialists can do
DECISION GRAPH      how decisions are justified
LEARNING GRAPH      how competence is formed
IMPACT GRAPH        what changes when a source/version changes
```

These are views/projections, not independent truth stores.

## 7. Regulatory UI

The Regulatory Graph view must support:

- navigation from general legal foundation to industry, regulator, departmental and local levels;
- filtering by industry, regulator, organization, status and effective date;
- current/historical version timeline;
- requirement extraction and applicability state;
- reverse trace from local order/control/role to originating requirement and source;
- impact analysis for amendments/repeals;
- contradiction and unresolved-applicability indicators;
- evidence/provenance panel for every significant node/edge;
- specialist/competency impact panel.

## 8. Node interaction contract

Selecting a regulatory or knowledge node should expose:

```text
IDENTITY
STATUS / CURRENTNESS
WHAT IT ESTABLISHES
APPLICABILITY
SOURCE + VERSION + LOCATOR
EVIDENCE
RELATIONS
WEIGHTS + HISTORY
CONTRADICTIONS
CONTROLS
RESPONSIBLE ROLES
COMPETENCIES
SPECIALISTS
IMPACT
AUDIT HISTORY
```

## 9. Change propagation

```text
NEW/CHANGED SOURCE VERSION
 -> legal/currentness validation
 -> affected fragments
 -> affected requirements/knowledge
 -> affected graph edges/weights
 -> applicability re-evaluation
 -> controls
 -> roles/competencies
 -> specialists
 -> curricula
 -> active projects/decisions
 -> regression/review queue
```

A changed regulation must not silently mutate downstream knowledge.

## 10. Separation of responsibilities

FATHER Knowledge Core is canonical operational truth.
ALINA Analyst performs evidence-backed analysis.
Specialist Knowledge Engineer builds profession/competency models.
ALINA Control Center visualizes, explains and controls the process.
Git stores reviewed schemas, algorithms, policies and sanitized projections, not the canonical live knowledge database.
