# FATHER Knowledge Formation Algorithms v0.1

This document turns the Knowledge Formation & Data Packaging Standard into executable-stage algorithms.

## A01 Source Intake

Input: discovered file/source.

```text
discover
 -> normalize locator
 -> fingerprint
 -> full SHA-256 when required
 -> identify exact duplicates
 -> identify logical document/version candidates
 -> classify context tree
 -> register physical locations
 -> preserve original
 -> emit Source Packet
```

Rules:
- FILE != DOCUMENTAL UNIT.
- Exact duplicate is a property, not permission to delete.
- Course/project/context inheritance is evaluated before physical storage action.
- Destructive cleanup requires a separate explicit gate.

Output: SOURCE_PACKET + audit event.

## A02 Document Understanding

```text
Source Packet
 -> parse format
 -> recover document structure
 -> identify chapters/sections/clauses
 -> extract text/tables/images/metadata
 -> create stable fragments
 -> quality checks
 -> Derived Packet
```

Extraction must retain locators back to the document version.

## A03 Knowledge Extraction

```text
fragment
 -> semantic segmentation
 -> candidate extraction
 -> semantic type classification
 -> atomicity check
 -> duplicate/near-duplicate check
 -> entity resolution
 -> evidence binding
 -> relation candidates
 -> contradiction candidates
 -> normalization
 -> validation queue
```

The extractor does not promote unsupported model output to FACT.

## A04 Entity Resolution

For every candidate entity or knowledge object:

```text
normalize label
 -> generate aliases
 -> retrieve existing candidates
 -> compare identity evidence
 -> SAME / RELATED / DIFFERENT / UNCERTAIN
 -> merge references only when identity gate passes
```

Uncertainty creates a review item; it must not force a merge.

## A05 Evidence Formation

```text
claim/knowledge candidate
 -> bind fragment
 -> bind document version
 -> bind publisher/authority/source
 -> evaluate source status/currentness
 -> record extraction method
 -> collect supporting/conflicting evidence
 -> assign evidence state
```

No fixed two-source rule is universal. Evidence requirements depend on claim class, authority and risk.

## A06 Relation Formation

```text
node A + node B
 -> candidate relation
 -> relation type
 -> evidence search
 -> scope/context
 -> contradiction check
 -> weight initialization
 -> edge validation
 -> versioned edge
```

No evidence means the edge remains candidate/hypothesis unless the relation is an explicit FATHER design decision.

## A07 Initial Weight Formation

For each weight dimension:

```text
collect evidence inputs
 -> identify calculation method/version
 -> calculate dimension value
 -> bind context
 -> bind evidence IDs
 -> persist weight event
```

Never let an LLM emit an unexplained final scalar as canonical weight.

## A08 Competency Formation

```text
profession
 -> discover real task classes
 -> decompose tasks
 -> infer required decisions
 -> map decisions to knowledge
 -> derive competencies
 -> map knowledge <-> competency <-> task
 -> assign contextual necessity/importance/risk weights
 -> evidence review
```

Question to enforce: "What decision does this knowledge enable?"

## A09 Learning Graph Formation

```text
target competencies
 + prerequisite graph
 + knowledge necessity
 + importance
 + risk_if_missing
 + difficulty
 + learner state
 + available constraints
 -> topological/prerequisite ordering
 -> modules
 -> practice
 -> checkpoints
 -> exams
 -> unseen tasks
 -> curriculum version
```

Curriculum is generated from competency/knowledge requirements, not from a copied table of contents.

## A10 Specialist Assembly

```text
profession blueprint
 -> resident K0 set
 -> retrieval K1/K2 policies
 -> tools/workflows
 -> cross-specialist interfaces
 -> training curriculum
 -> examination
 -> polygon
 -> release gate
```

The Specialist Knowledge Engineer discovers and justifies the profession model; it is not manually pre-filled with the answer.

## A11 Runtime Knowledge Sufficiency

```text
TASK
 -> task classification
 -> required competencies
 -> retrieve relevant graph neighborhood
 -> evidence retrieval
 -> sufficiency check
 -> sufficient? use
 -> insufficient? GAP
 -> research order
 -> ALINA/source discovery
 -> temporary research KB
 -> solve
 -> evaluate
 -> promote useful knowledge or archive one-off research
```

## A12 Polygon and Evaluation

```text
specialist/version
 -> representative tasks
 -> load tasks
 -> unseen transfer tasks
 -> A/B/n variants
 -> metrics
 -> failure analysis
 -> evidence pack
 -> independent evaluation
 -> pass/fail/retrain
```

Metrics are task-class specific; do not invent a universal quality score.

## A13 Dynamic Weight Update

```text
previous weight event
 + new experiment/usage/evidence
 -> validate comparability
 -> calculate new contextual dimension
 -> persist new weight event
 -> preserve previous event
 -> impact analysis
 -> regression check
```

Historical evidence and old weights are never overwritten.

## A14 Gap Loop

```text
failure/unknown/contradiction/outdated knowledge
 -> classify GAP
 -> prioritize by risk/impact
 -> research plan
 -> source acquisition
 -> evidence
 -> new/updated knowledge
 -> graph update
 -> curriculum/runtime update
 -> retrain/retest
 -> close or retain gap
```

Gap classes include knowledge, evidence, competency, interaction and currency gaps.

## A15 Knowledge Currency

```text
START SPECIALIST
 -> SYNC KNOWLEDGE
 -> CHECK UPDATES
 -> PROCESS CHANGES
 -> IMPACT ANALYSIS
 -> UPDATE WORKING MODEL
 -> REGRESSION/HEALTH CHECK
 -> READY
 -> WORK
```

Emergency updates use an accelerated path but retain provenance, impact analysis and audit.

## A16 Decision Trace

For significant decisions:

```text
TASK
 -> requirements/constraints
 -> alternatives
 -> selected method/algorithm/pattern
 -> rationale/trade-offs
 -> implementation/action
 -> measurement
 -> evidence
 -> learning
```

Reverse trace must be possible from decision to original evidence.

## A17 Specialist Factory Quality Loop

Evaluate the Specialist Knowledge Engineer by the quality of specialists it builds:

```text
SKE vN
 -> build specialist vN
 -> polygon/evaluation
 -> metrics/gaps
 -> improve SKE/Factory
 -> build specialist vN+1
 -> compare under controlled evaluation
```

Do not equate self-reflection with validation.

## A18 Knowledge Evolution Loop

```text
DISCOVER
 -> SOURCE
 -> EVIDENCE
 -> KNOWLEDGE
 -> GRAPH
 -> COMPETENCY
 -> SPECIALIST
 -> TASK
 -> DECISION
 -> ACTION
 -> POLYGON
 -> METRICS
 -> A/B
 -> LEARN
 -> UPDATE WEIGHTS
 -> GAP?
 -> RESEARCH
 -> NEW KNOWLEDGE
 -> repeat
```

This is the canonical Knowledge -> Competence -> Experiment -> Evidence loop.

## A19 Specialist Requirement Derivation

Purpose: derive specialist requirements from evidenced work rather than inventing a syllabus or list of knowledge.

TARGET / CONTEXT -> normative obligations and constraints -> professional role evidence -> real task classes -> risks and responsibility -> FATHER-specific operating requirements -> TASKS -> DECISIONS -> ACTIONS -> EXPECTED RESULTS -> COMPETENCIES -> KNOWLEDGE / METHODS / TOOLS -> SPECIALIST REQUIREMENTS -> TRAINING -> EXAM / POLYGON.

Requirement origin classes:
- R1 NORMATIVE — applicable binding requirements.
- R2 PROFESSIONAL — professional/educational standards, body of knowledge or evidenced professional practice.
- R3 TASK_DERIVED — necessary for an evidenced real task or decision.
- R4 RISK_DERIVED — necessary because omission/error creates material risk.
- R5 FATHER_SPECIFIC — necessary for operation inside FATHER.

Each requirement is a versioned first-class object. Where applicable it records target specialist, origin class, must_be_able_to, derived_from task/decision/risk/normative object, required knowledge, methods, tools, evidence, criticality, risk_if_missing, validation method, currentness and lifecycle state.

Lifecycle: PROPOSED -> EVIDENCED -> VALIDATED -> ACTIVE; rejected candidates become REJECTED; active requirements may enter REVIEW_REQUIRED and then remain ACTIVE or become SUPERSEDED/RETIRED.

Mandatory gate: WHY REQUIRED? -> WHICH TASK? -> WHICH DECISION/ACTION? -> WHICH COMPETENCY? -> WHICH EVIDENCE/SOURCE? -> HOW TESTED?

If this chain cannot be established, the requirement cannot enter the reference specialist baseline as validated.

Reverse trace: SPECIALIST REQUIREMENT <- COMPETENCY <- DECISION <- TASK <- PROFESSION/NORMATIVE/RISK/FATHER CONTEXT <- EVIDENCE <- SOURCE VERSION.

Currentness applies to specialist requirements. Changes in upstream source, task model, technology, risk model or FATHER architecture trigger impact review rather than silent mutation.

Output: SPECIALIST_REQUIREMENT objects + evidence links + validation plan + audit event.
