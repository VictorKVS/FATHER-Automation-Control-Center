# ALINA BACKEND BOOTSTRAP PASSPORT v0.1

Status: PRE-IMPLEMENTATION BASELINE  
Scope: FATHER Backend / ALINA Analyst  
Primary principle: ALINA FIRST

## 1. Purpose

ALINA Analyst is the first FATHER meta-specialist. Her purpose is to transform a target, context and source material into evidence-backed, versioned, traceable and testable knowledge, detect what is missing or contradictory, and use that knowledge to create the foundation of future agents and specialists.

ALINA is not the canonical source of truth. FATHER Knowledge Core is the canonical knowledge substrate; ALINA is an analytical actor operating on it.

## 2. Primary outcome

Given a target agent/specialist and operating context, ALINA shall be able to produce an Agent Knowledge Foundation whose material claims and requirements are traceable to evidence, whose gaps are explicit, and whose quality can be evaluated independently.

## 3. Bootstrap strategy

ALINA is built before mass specialist generation.

Specialist Knowledge Engineer provides the reference methodology for knowledge formation. During bootstrap, human architects may define and review this methodology, but the target state is for ALINA to execute it reproducibly.

ALINA MUST NOT certify herself. Promotion requires independent Examiner/Polygon evidence.

Makar Agent v0.1 is the first compact applied validation case for ALINA/FATHER contracts.

## 4. Inputs

ALINA may receive:
- target and desired outcome;
- context and constraints;
- source documents and source metadata;
- existing Knowledge Core objects;
- research orders;
- task and evaluation results;
- specialist/agent requirements;
- prior gaps, contradictions and supersession events.

Unknown or unavailable inputs remain explicit; they are not silently invented.

## 5. Outputs

ALINA shall be capable of producing versioned artifacts including:
- source registration and source-version records;
- fragments/chunks with stable provenance;
- Evidence objects;
- typed Knowledge Objects;
- typed and evidenced Relations;
- contradiction and uncertainty records;
- GAP records and Research Orders;
- retrieval/evidence packs;
- analytical conclusions separated from source-backed facts;
- Agent Knowledge Foundation artifacts;
- evaluation inputs and improvement proposals;
- append-only audit/journal events.

## 6. Knowledge semantics

ALINA MUST preserve distinctions between at least:
FACT != CLAIM != DEFINITION != REQUIREMENT != METHOD != ALGORITHM != DECISION != INFERENCE != HYPOTHESIS.

Document != requirement.
Chunk != knowledge.
Embedding != knowledge.
RAG != Knowledge Core.
Model output != evidence.

Contradictions are preserved and analyzed, not erased by selecting a convenient statement.

## 7. Provenance invariant

For any material grounded conclusion, FATHER must be able to reconstruct:

RESULT / DECISION
<- KNOWLEDGE
<- EVIDENCE
<- FRAGMENT
<- DOCUMENT VERSION
<- DOCUMENT
<- ORIGINAL SOURCE

If provenance cannot be reconstructed, the relevant claim remains unverified or becomes a GAP.

## 8. Internal capability stages

ALINA backend is developed through these capabilities:

1. Target & Context Intake
2. Source Registration
3. Version & Integrity Control
4. Fragmentation / Structural Extraction
5. Evidence Formation
6. Knowledge Object Formation
7. Relation / Graph Formation
8. Validation / Contradiction Analysis
9. Retrieval Planning and RAG
10. Evidence Pack Assembly
11. Analytical Reasoning
12. GAP Detection
13. Research Order Formation
14. Agent Knowledge Foundation Builder
15. Evaluation / Polygon Handoff
16. Learning & Improvement Proposal

Each capability must expose auditable inputs, outputs, status and failure modes.

## 9. First executable vertical slice

The first backend slice SHALL prove one complete path:

SOURCE
-> DOCUMENT
-> DOCUMENT_VERSION
-> FRAGMENT
-> EVIDENCE
-> KNOWLEDGE_OBJECT
-> RETRIEVAL
-> GROUNDED_USE
-> REVERSE_PROVENANCE_TO_SOURCE

The first applied consumer is Makar Agent v0.1.

The slice is successful only when a piece of educational source material can be registered, transformed into a typed knowledge object, retrieved for a Makar task, used in a grounded response/check, and traced back to the exact source evidence.

## 10. Makar boundary

Makar uses shared FATHER knowledge/evidence/retrieval contracts.

Canonical educational knowledge and learner-specific state are separate.

Canonical:
- mathematical/linguistic concepts;
- methods and algorithms;
- task patterns;
- evidence/source provenance.

Learner-specific:
- attempts;
- mistakes;
- mastered/learning/gap states;
- hints used;
- difficulty history;
- progress/evaluation events.

Learner state MUST NOT silently mutate canonical knowledge.

## 11. Storage responsibility

Target canonical operational store: PostgreSQL with pgvector used as a retrieval index where appropriate.

Original source files remain immutable in FATHER_VAULT or an equivalent controlled source store.

Git stores reviewed schemas, migrations, algorithms, policies, contracts and sanitized fixtures; it is not the production Knowledge Core database.

Graph and vector indexes are projections/indexes and can be rebuilt from canonical records.

## 12. Failure modes

ALINA must explicitly fail or degrade when:
- source is unavailable or integrity is unknown;
- evidence does not support the proposed knowledge;
- currentness is unknown where currentness matters;
- sources contradict;
- retrieval has insufficient support;
- requested agent capability has no evidenced competency/knowledge basis;
- model output cannot be distinguished from source-backed knowledge;
- evaluation evidence is insufficient.

Failure must create a GAP, Research Order, REVIEW_REQUIRED state, or other explicit non-success state.

## 13. Quality gates

Before implementation of a capability:
NEED/PROBLEM -> PASSPORT -> SCHEME/NOTATION -> TEST SPECIFICATION -> REVIEW.

Before release:
IMPLEMENTATION -> TEST EXECUTION -> EVIDENCE/METRICS -> INDEPENDENT EVALUATION where applicable -> RELEASE/REWORK.

Universal rules:
- no artifact = stage not complete;
- no provenance = claim unverified;
- no independent evaluation = competence unconfirmed;
- no regression = improvement not released.

## 14. Bootstrap acceptance criteria

ALINA bootstrap is not complete merely because an LLM can answer questions.

Minimum evidence of progress:
- the vertical slice runs end-to-end;
- knowledge types remain distinct;
- provenance is reversible;
- unsupported statements are not promoted to canonical knowledge;
- gaps and contradictions are explicit;
- Makar can consume shared knowledge through RAG without owning a duplicate truth store;
- evaluation results can feed improvement without overwriting source evidence;
- ALINA can begin constructing her own Agent Knowledge Foundation under independent review.

## 15. Next required artifact

Create ALINA Backend Flow / Notation v0.1 describing the data/control flow, object boundaries, state transitions and the Makar validation path.

No backend implementation is authorized by this passport alone; the notation and test specification gates remain required.
