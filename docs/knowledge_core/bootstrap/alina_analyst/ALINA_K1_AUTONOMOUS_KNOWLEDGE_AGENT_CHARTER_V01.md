# ALINA K1 — Autonomous Knowledge Agent Charter v0.1

## Mission
ALINA is the reference FATHER agent and the machine for transforming raw information into evidence-backed, reusable knowledge and verified agent competence.

Token reduction is a consequence of this architecture, not ALINA's primary mission.

## Primary transformation
SOURCE -> EVIDENCE -> KNOWLEDGE -> COMPETENCE -> TASK RESULT -> EVALUATION -> GAP -> IMPROVEMENT.

## What ALINA must produce
ALINA must not stop at extracted text, summaries, chunks or embeddings. For accepted source material she must be able to produce structured Knowledge Units containing, where supported by evidence:
- concepts and definitions;
- facts and claims;
- principles and requirements;
- rules and constraints;
- methods and algorithms;
- applicability conditions and exceptions;
- failure modes and anti-patterns;
- examples;
- validation criteria;
- relationships to other knowledge;
- provenance/evidence;
- confidence/status;
- specialist/competency applicability;
- candidate tests.

## Knowledge layers
### L0 SOURCE
Immutable source identity and provenance: original location/reference, source metadata, version/date where available, hash, license/status where relevant.

### L1 EVIDENCE / EXTRACTED
Recoverable source-derived structure: pages/sections/chunks/tables/images/code fragments and precise provenance back to L0.

### L2 KNOWLEDGE
Normalized Knowledge Units, concepts, relations, methods, algorithms, conflicts, alternatives, evidence links and Knowledge Graph structures.

### L3 COMPETENCE
Agent-specific capability state: which knowledge/skills are required, which are available, which have been demonstrated in tests, and which gaps remain.

## ALINA internal systems
1. Identity & Constitution — mission, authority, constraints and stable policies.
2. Cognitive Core — task decomposition, planning, reasoning, verification and uncertainty handling.
3. Knowledge Core — L0-L3 model, graph, retrieval, provenance and contradiction handling.
4. Memory — task/work/project/long-term memory separated from canonical knowledge.
5. Tool Intelligence — tool selection, constraints, cost/risk awareness and result verification.
6. Self-Evaluation — requirements/result/evidence/uncertainty/test review.
7. Learning Engine — classify failures into knowledge, retrieval, reasoning, tool, policy or execution gaps and close them through controlled improvement.
8. Agent Architect — derive specialist requirements, knowledge foundation, tools, prompts/policies, tests and improvement loops for downstream agents.

## Existing components are tools, not ALINA itself
The existing alina-knowledge-worker extraction/search pipeline is treated as a Document Processor / Library Worker under ALINA. It is not the complete ALINA agent and must not define the final Knowledge Core schema by itself.

The ALINA 3D body and Control Center are the human interaction/presence layer. They continue as a parallel ALINA BODY track and do not block K1 knowledge-agent development.

## Existing library audit
Do not start by rescanning all disks. The previously produced library/model inventory is an input candidate. K1 must first locate and validate the existing inventory artifacts, determine their schema/completeness/freshness, and import or adapt them into a Master Source Registry without silently treating stale inventory as current truth.

## K1 MVP — first proving loop
The first bounded proving loop uses MAKAR as the downstream specialist:
1. accept a validated subset of the existing source inventory relevant to frontend / UI / WebGL / Three.js / VRM / 3D / game engineering;
2. register sources and deduplicate identities;
3. extract evidence while preserving provenance;
4. create evidence-backed Knowledge Units;
5. build relations/graph and retrieval surfaces;
6. derive Makar competency requirements;
7. assemble Makar's knowledge/retrieval/tool/prompt package from shared FATHER knowledge rather than copying an isolated private library;
8. give Makar a previously unseen practical task;
9. evaluate result and evidence;
10. classify gaps;
11. improve knowledge/agent configuration;
12. rerun the test and compare.

## Acceptance criteria
K1 is not accepted merely because ingestion, embeddings or RAG search work.

K1 MVP is accepted only when a bounded source set can complete an auditable SOURCE -> KNOWLEDGE -> COMPETENCE loop and the downstream specialist can be evaluated against a practical task with traceable evidence and explicit gap/improvement state.

## Immediate implementation sequence
K1.0 — inventory/artifact discovery and AS-IS audit.
K1.1 — canonical Master Source Registry contract.
K1.2 — L0/L1 evidence contract and adapter for existing extraction pipeline.
K1.3 — Knowledge Unit schema and validator.
K1.4 — first evidence-to-Knowledge-Unit transformation on a small controlled corpus.
K1.5 — relation/conflict/provenance graph.
K1.6 — Makar competency projection.
K1.7 — retrieval package + practical exam.
K1.8 — gap classification and improvement loop.
K1.9 — metrics and repeatability gate.

## Metrics
Track at minimum: sources discovered/accepted/rejected; duplicates; extraction success/failure; Knowledge Units produced/accepted/rejected; provenance coverage; unresolved contradictions; retrieval evidence quality; competency coverage; exam pass/fail by criterion; gap categories; rework rate; processing throughput; and token/cost reduction only as a secondary efficiency metric.

## Non-goals for K1 MVP
- perfect 3D animation;
- large gesture/emotion library;
- autonomous ingestion of the entire computer before schema validation;
- treating summaries or vector embeddings as canonical knowledge;
- duplicating the same source/knowledge physically into every agent;
- claiming autonomous learning without an auditable promotion/test gate.
