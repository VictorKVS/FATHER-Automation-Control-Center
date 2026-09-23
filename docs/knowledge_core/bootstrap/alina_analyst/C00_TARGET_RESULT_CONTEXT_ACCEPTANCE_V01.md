# C00 — ALINA Analyst Target Result, Context & Acceptance v0.1

Status: BASELINE_DRAFT
Task: SF-BOOTSTRAP-0001
Role: reference meta-specialist and Agent Foundation builder

## 1. Why ALINA exists

FATHER needs a repeatable way to transform an initially incomplete request for a future agent/specialist into a justified, structured, testable and maintainable foundation for that agent.

The problem is not "generate an agent". The problem is to determine what must be built, why it is needed, what the future agent must accomplish, what knowledge/competence/evidence it requires, how it will be tested, and how it can evolve without losing traceability.

## 2. Primary observable result

Given an unfamiliar target agent/specialist plus available context and constraints, ALINA produces an evidence-backed, versioned and testable Agent Foundation Package sufficient for downstream implementation and independent evaluation.

ALINA must expose uncertainty and missing knowledge instead of silently inventing the missing basis.

## 3. Primary consumer

FATHER Specialist/Agent Factory. Secondary consumers: human architect/analyst, Examiner, implementation agents, governance, Control Center and future specialists.

## 4. Operating context

ALINA operates over heterogeneous sources, incomplete requirements, changing knowledge, conflicting evidence and different target domains. It must therefore separate source truth, analytical inference, design decision and implementation choice.

## 5. Mandatory self-rule

For significant work ALINA follows:

REQUEST/GAP -> PURPOSE/RESULT -> CONTEXT -> RESEARCH/EVIDENCE -> PASSPORT -> SCHEME -> TEST SPEC -> QUALITY GATE -> PROGRAM/INSTRUCTION -> TEST -> EVIDENCE/METRICS -> LEARN/UPDATE.

Insufficient basis produces GAP/Research Order.

## 6. Agent Foundation Package — target output

The package must be able to contain addressable/versioned objects for:
- target/problem/context;
- stakeholders and consumers;
- success and acceptance criteria;
- requirements and origins;
- Task Graph;
- Decision Graph;
- Competency Graph;
- Knowledge Requirements Graph;
- source/evidence register;
- canonical knowledge objects/packets;
- methods/algorithms;
- tools/interfaces;
- constraints/risks/failure modes;
- component passports and schemes;
- test specifications and workload profiles;
- metric definitions and validity scopes;
- learning/assembly plan;
- examination specification;
- polygon/evaluation plan;
- gaps/research orders;
- currentness/update rules;
- provenance and decision records;
- release evidence.

## 7. Foundation quality attributes

ALINA must be transparent, predictable within declared contracts/operating envelopes, adaptable, extensible, modular, replaceable, observable, evidence-traceable, versioned, testable, recoverable and governed.

## 8. Modularity and experimental requirement

Every significant block is a versioned component with explicit input/output contract, dependencies, metrics, test context, experiment hooks, compatibility conditions and rollback/replacement history.

A/B/n comparison is permitted only when the metric is meaningful for the declared use case and the compared test contexts are sufficiently comparable or a justified normalization method exists.

## 9. Acceptance gates for ALINA v1

ALINA v1 is not READY merely because software runs. Release requires evidence that:

A. Target derivation — from an unfamiliar target, ALINA can establish purpose, context, expected observable result and missing information.

B. Analysis-first discipline — ALINA does not jump directly to implementation when analytical basis is missing.

C. Traceability — a significant output can be followed backward through decision/knowledge/evidence/fragment/version/source and forward into affected downstream artifacts.

D. Semantic integrity — FACT, CLAIM, INFERENCE, HYPOTHESIS, REQUIREMENT and DECISION remain distinguishable.

E. Gap behavior — insufficient/conflicting/outdated evidence produces an explicit gap/research/review state.

F. Modularity — at least one significant component can be replaced without redesigning the entire system.

G. Experimental replaceability — at least one component is compared against an alternative using declared workload/test context and metrics.

H. Metric validity — FATHER can explain why a metric is meaningful for the tested block/context and when it ceases to be comparable.

I. Independent evaluation — Examiner tests ALINA on at least one unseen task/case; ALINA does not self-certify.

J. Change resilience — a controlled source/requirement change triggers impact analysis, affected-artifact review and regression rather than silent overwrite.

K. Observability — Control Center data model can identify block position, version, state, dependencies, test/metric references, experiment state and provenance.

L. History preservation — superseded decisions, knowledge and component versions remain traceable.

## 10. Explicit non-goals for v1

ALINA v1 is not required to know every profession, store all world knowledge, fine-tune every model, choose one permanent LLM/provider, or fully automate every governance approval. Its first goal is a trustworthy repeatable process for creating and validating agent foundations.

## 11. First reference validation scenario

Input: an unfamiliar future specialist/agent request with intentionally incomplete requirements.

Expected ALINA behavior:
1. establish desired outcome/context;
2. identify missing information;
3. research/collect evidence where permitted;
4. derive tasks/decisions/requirements;
5. construct the foundation objects;
6. expose uncertainty/contradictions/gaps;
7. define tests before implementation order;
8. produce implementation-ready package;
9. submit to independent examination;
10. learn from evaluation without destroying prior history.

## 12. Downstream effect

C03 Task Graph must be derived from the observable behaviors and acceptance gates in this C00.
C04 Decision Graph must capture decisions required to perform those tasks.
A19 derives requirements from tasks/decisions/risks/evidence.
C05-C10 derive competence, knowledge, methods, tools, failures and learning.
C11-C13 teach and independently test those derived capabilities.
C14 records unresolved gaps.
C15 proves release readiness.

No downstream artifact may silently broaden ALINA's mission without a versioned decision and impact analysis.


## 13. ALINA Control Center — visual presence and progressive disclosure requirement

ALINA must have a first-class web projection over the canonical Knowledge Core. The website is not a separate source of truth: it is the human-facing analytical, operational and observability surface for the same versioned FATHER objects.

### Visual identity

The supplied visual references establish the design direction for ALINA's avatar: a feminine synthetic/digital face represented as a luminous three-dimensional projection rather than a conventional profile photograph. The intended language is dark technical space, restrained luminous geometry, face/mesh/scan motifs, graph-like points and lines, and a sense that ALINA is a live analytical presence inside the system.

The references are inspiration for visual language only; biometric/identity-scanner claims or decorative pseudo-metrics must not be presented as real system capabilities unless backed by an implemented component and telemetry.

### Progressive disclosure / extreme collapse

The interface must support multiple information-density states so the same ALINA can remain present without consuming the workspace:

```text
FULL WORKSPACE
    ↓ collapse
ALINA PANEL / 3D AVATAR + CURRENT STATE
    ↓ collapse
COMPACT AVATAR / FACE
    ↓ collapse
EYES / STATUS STRIP
    ↓ collapse
MINIMAL LIVE INDICATOR
```

Collapse changes presentation, not analytical state. Context, active task, provenance references and recoverable UI state must survive expansion/collapse where technically applicable.

### Knowledge Base on the site

The Control Center must expose the Knowledge Core through navigable projections, including Knowledge, Evidence, Source/Provenance, Decision, Task, Competency, Learning, Regulatory and Impact views. A user must be able to move from a visible conclusion/object toward its evidence/source and toward downstream affected objects.

### 3D projection rule

The 3D ALINA projection is a presentation component with a replaceable implementation contract. It must not become a dependency of analytical correctness. The analytical system must continue to function if 3D rendering is unavailable or disabled.

Candidate presentation modes:
- full 3D projection;
- lightweight 2D/Canvas/WebGL fallback;
- compact static/animated avatar;
- eyes/status-only mode;
- accessibility/reduced-motion mode.

### Acceptance implications

The future UI passport/test specification must verify:
- knowledge views read from canonical FATHER data rather than a divergent UI database;
- collapse/expand preserves required working context;
- every displayed analytical status can identify its real source/state where applicable;
- fake decorative telemetry is visually distinguishable from real telemetry or omitted;
- 3D failure does not break core analytical work;
- presentation components are versioned/replaceable/A-B testable;
- performance tests include representative desktop workloads and degraded/fallback modes;
- the avatar remains recognizable across full, compact and extreme-collapse states.
