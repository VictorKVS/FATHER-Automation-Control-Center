# FATHER Knowledge Formation & Data Packaging Standard v0.1

Status: DRAFT FOR IMPLEMENTATION

## 1. Purpose

This standard defines how FATHER converts sources into traceable knowledge, relations, weights, competencies, learning programs, specialists, experiments and updated knowledge.

The canonical reasoning chain is:

```text
SOURCE -> EVIDENCE -> KNOWLEDGE -> GRAPH -> WEIGHTS
       -> COMPETENCY -> CURRICULUM -> SPECIALIST
       -> ACTION -> EXPERIMENT -> METRIC -> LEARNING
       -> KNOWLEDGE EVOLUTION -> repeat
```

A chunk is not knowledge. A file is not a knowledge object. An LLM answer is not evidence.

## 2. Core invariants

1. SOURCE IS IMMUTABLE.
2. CATALOG IS AUTHORITATIVE FOR SOURCE IDENTITY AND STATE.
3. KNOWLEDGE IS VERSIONED.
4. PROVENANCE IS MANDATORY.
5. FACT != CLAIM != INFERENCE != HYPOTHESIS != REQUIREMENT != DECISION.
6. No material knowledge assertion may lose its path back to evidence and source.
7. Contradictions are preserved, not silently averaged away.
8. Graph edges are first-class versioned objects.
9. A weight is contextual evidence about a relation, not truth.
10. Weight history is append-only.
11. Specialist views reuse canonical knowledge; they do not duplicate source truth.
12. RAG is an access mechanism, not the knowledge base.
13. Embeddings are indexes, not canonical knowledge.
14. Practical results may change weights but never rewrite historical evidence.
15. No artifact means the stage is not complete.
16. No provenance means the claim is unverified.
17. No independent evaluation means competence is unconfirmed.
18. No regression check means an improvement is not released.

## 3. Knowledge states

```text
DISCOVERED
 -> SOURCED
 -> EXTRACTED
 -> NORMALIZED
 -> EVIDENCED
 -> LINKED
 -> VALIDATED
 -> APPLIED
 -> TRANSFERRED
 -> RETIRED/SUPERSEDED
```

State transitions must be audited.

## 4. Knowledge object taxonomy

Canonical semantic types include:

- CONCEPT
- DEFINITION
- FACT
- CLAIM
- INFERENCE
- HYPOTHESIS
- REQUIREMENT
- METHOD
- ALGORITHM
- PATTERN
- ANTI_PATTERN
- PROCEDURE
- RULE
- TOOL
- METRIC
- LIMITATION
- EXAMPLE
- DECISION
- FAILURE_MODE

## 5. Three packaging levels

### L0 Source Packet
Represents what was obtained: source, document, version, structure, fragments, extraction metadata and provenance.

### L1 Knowledge Packet
Represents what was established or extracted from source material.

### L2 Application Packet
Represents how knowledge is used: task classes, decision rules, alternatives, constraints, trade-offs, metrics and failure modes.

Never collapse these three levels.

## 6. Logical Knowledge Packet

```text
KNOWLEDGE_PACKET
├── identity
│   ├── knowledge_id
│   ├── type
│   ├── title
│   └── version
├── semantics
│   ├── what
│   ├── why
│   ├── when
│   ├── when_not
│   ├── limitations
│   └── examples
├── provenance
│   ├── source_id
│   ├── document_version_id
│   ├── fragment_id
│   ├── locator
│   └── extraction_method
├── evidence
│   ├── evidence_ids
│   ├── authority
│   ├── strength
│   ├── currentness
│   └── contradictions
├── relations
│   ├── requires
│   ├── supports
│   ├── contradicts
│   ├── alternative_to
│   ├── supersedes
│   └── used_for
├── application
│   ├── task_classes
│   ├── decision_rules
│   ├── constraints
│   ├── alternatives
│   └── tradeoffs
├── competence
│   ├── competency_ids
│   ├── prerequisite_level
│   └── specialist_roles
├── weights
│   └── typed contextual weight vector
└── lifecycle
    ├── state
    ├── created_at
    ├── validated_at
    ├── last_used_at
    └── next_review_at
```

This is a logical contract. PostgreSQL should normalize it rather than store the entire system as one opaque JSON document.

## 7. Atomicity rule

A knowledge node should represent one independently evidenceable and usable unit of meaning.

Each applicable knowledge object should answer:

```text
WHAT
WHY
WHEN
WHEN_NOT
REQUIRES
ALTERNATIVES
TRADE_OFFS
METRICS
EVIDENCE
EXAMPLE
FAILURE
```

Missing fields are allowed only when they are genuinely inapplicable or explicitly unknown.

## 8. Provenance chain

Every significant decision should permit reverse traversal:

```text
DECISION
 <- DECISION_RULE
 <- KNOWLEDGE
 <- EVIDENCE
 <- FRAGMENT
 <- DOCUMENT_VERSION
 <- DOCUMENT
 <- ORIGINAL_SOURCE
```

A broken chain changes verification state; it must not be hidden.

## 9. Graph model

Canonical relation vocabulary starts with:

```text
IS_A
PART_OF
REQUIRES
DEPENDS_ON
USED_FOR
IMPLEMENTS
SUPPORTS
CONTRADICTS
ALTERNATIVE_TO
SUPERSEDES
DERIVED_FROM
EVIDENCED_BY
APPLIES_TO
PROHIBITS
RECOMMENDS
IMPROVES
DEGRADES
MEASURED_BY
REQUIRED_FOR_COMPETENCY
USED_IN_TASK
```

Every edge contains at least from_node, relation_type, to_node, evidence, scope, status, version and weight references.

## 10. Weight model

Never use an unexplained scalar such as `weight=0.83`.

A weight is:

```text
(value, dimension, context, method, evidence, timestamp, version)
```

Initial dimensions include:

- evidence_strength
- source_authority
- confidence
- applicability
- relevance
- necessity
- importance
- frequency_of_use
- prerequisite_strength
- practical_success
- recency
- risk_if_missing

Practical evaluation may add task_coverage, failure_rate, transfer_success, benchmark_gain and regression_risk.

Weights are contextual. The same knowledge may have different necessity or importance for different specialist roles.

## 11. Knowledge residency

```text
K0 RESIDENT      always-needed specialist knowledge
K1 READY         frequently retrieved knowledge
K2 DISCOVERABLE  rare knowledge found on demand
K3 UNKNOWN       identified gap requiring research
```

Do not push the entire knowledge graph into an LLM context or model weights.

## 12. Canonical storage roles

- FATHER_VAULT: immutable originals and derived artifacts.
- PostgreSQL: canonical operational catalog, knowledge, evidence, graph, competency and lifecycle state.
- pgvector: semantic retrieval index.
- Git: reviewed schemas, algorithms, policies, migrations, manifests and sanitized projections.
- LLM: reasoning mechanism, not carrier of canonical professional truth.

A specialized graph engine may be added only when measured requirements justify it.
