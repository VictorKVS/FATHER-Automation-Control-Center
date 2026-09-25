# FATHER Knowledge Packet Contract v0.1

This is the machine-facing logical contract. It is technology-neutral and will be mapped to normalized PostgreSQL tables and JSON Schema.

## Required identity

```yaml
knowledge_id: stable-id
knowledge_type: CONCEPT|DEFINITION|FACT|CLAIM|INFERENCE|HYPOTHESIS|REQUIREMENT|METHOD|ALGORITHM|PATTERN|ANTI_PATTERN|PROCEDURE|RULE|TOOL|METRIC|LIMITATION|EXAMPLE|DECISION|FAILURE_MODE
version: integer
state: DISCOVERED|SOURCED|EXTRACTED|NORMALIZED|EVIDENCED|LINKED|VALIDATED|APPLIED|TRANSFERRED|RETIRED|SUPERSEDED
title: string
```

## Provenance

```yaml
provenance:
  source_id: stable-id
  document_id: stable-id
  document_version_id: stable-id
  fragment_id: stable-id
  locator: page/section/offset/etc
  extraction_method: method+version
```

## Semantics

```yaml
semantics:
  what: text|null
  why: text|null
  when: text|null
  when_not: text|null
  limitations: []
  examples: []
```

Null means unknown/not applicable; it must not be silently synthesized.

## Relations

```yaml
relations:
  - edge_id: stable-id
    relation_type: controlled-vocabulary
    target_id: stable-id
    scope: context|null
    status: CANDIDATE|VALIDATED|REJECTED|SUPERSEDED
    evidence_ids: []
    weight_ids: []
```

## Weight event

```yaml
weight_event:
  weight_id: stable-id
  edge_or_binding_id: stable-id
  dimension: evidence_strength|source_authority|confidence|applicability|relevance|necessity|importance|frequency_of_use|prerequisite_strength|practical_success|recency|risk_if_missing
  value: number
  scale: declared-scale
  context: structured-context
  method: method-id+version
  evidence_ids: []
  experiment_ids: []
  calculated_at: timestamp
  previous_weight_id: stable-id|null
  reason_for_change: text
```

A value without dimension, scale, method, context and provenance is invalid.

## Competency binding

```yaml
competency_binding:
  specialist_role_id: stable-id
  competency_id: stable-id
  task_class_ids: []
  knowledge_id: stable-id
  residency: K0|K1|K2|K3
  weight_ids: []
```

## Evidence state

Evidence should distinguish source-backed material from FATHER analysis/design:

```text
SOURCE_BACKED
ANALYTICAL_INFERENCE
FATHER_DESIGN_DECISION
UNVERIFIED
CONTRADICTED
OUTDATED
```

## Persistence rule

The packet is an interchange/logical representation. Canonical PostgreSQL storage should normalize identity, source/version/fragment, evidence, nodes, edges, weight events, competencies, tasks, evaluations and audit history.
