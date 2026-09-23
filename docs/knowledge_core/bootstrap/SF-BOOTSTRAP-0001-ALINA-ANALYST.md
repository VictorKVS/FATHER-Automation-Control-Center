# SF-BOOTSTRAP-0001 — Build ALINA Analyst

Status: READY_FOR_DISCOVERY
Builder: Specialist Knowledge Engineer
Target: ALINA Analyst
Role class: FATHER bootstrap/reference specialist

## Mission

Build and independently validate the first analytical specialist that can transform source material into traceable evidence and canonical knowledge for FATHER.

This task intentionally does NOT predefine ALINA's final competency model, curriculum, source list, or professional methods. The Specialist Knowledge Engineer must discover, evidence, justify and version them.

## Minimal input

- Target name: ALINA Analyst
- System context: FATHER Knowledge Core / Specialist Factory
- Purpose: analyze sources and transform them into evidence-backed, structured, reusable knowledge.
- Constraints:
  - provenance mandatory;
  - FACT, CLAIM, INFERENCE, HYPOTHESIS, REQUIREMENT and DECISION remain distinct;
  - contradictions must be preserved;
  - significant assertions require evidence;
  - no self-certification;
  - specialist must expose unknowns and knowledge gaps;
  - source truth is not stored only in model weights.

## Required discovery questions

The builder must establish with evidence:

1. What real task classes define an analytical specialist suitable for FATHER?
2. What decisions must ALINA make in each task class?
3. Which competencies enable those decisions?
4. Which knowledge is required, useful, optional, or discoverable on demand?
5. Which analytical methods and procedures are appropriate, and under what conditions?
6. What source/evidence standards are required?
7. What tools are needed?
8. What common analytical failure modes and biases must be controlled?
9. What interfaces are required with Source Intake, Knowledge Miner, Knowledge Core, Specialist Factory, Examiner and other specialists?
10. How can competence be tested on unseen material rather than by self-description?

## Mandatory outputs

```text
C01 Profession Dossier
C02 Source & Evidence Register
C03 Task Graph
C04 Decision Graph
C05 Competency Graph
C06 Knowledge Requirements Graph
C07 Method / Algorithm Register
C08 Tool & Interface Map
C09 Failure / Limitation Register
C10 Learning Graph
C11 Curriculum
C12 Examination Specification
C13 Polygon Specification
C14 Gap Register
C15 Release Evidence Pack
```

Every output must be versioned and traceable.

## Bootstrap acceptance

ALINA Analyst is not released merely because it can summarize documents.

The reference test is:

```text
UNKNOWN SOURCE
 -> structure
 -> evidence extraction
 -> knowledge candidates
 -> semantic typing
 -> provenance
 -> relations
 -> contradictions
 -> weights with explicit method/context
 -> gaps/unknowns
 -> Knowledge Packet
 -> independent evaluation
```

The Examiner must be able to trace a sampled result backwards:

```text
OUTPUT
 <- DECISION/KNOWLEDGE
 <- EVIDENCE
 <- FRAGMENT
 <- DOCUMENT VERSION
 <- ORIGINAL SOURCE
```

## Failure rule

If ALINA fails, do not manually patch the answer into ALINA's knowledge base.

Classify the failure as one or more of:

- PROFESSION_MODEL_GAP
- TASK_MODEL_GAP
- COMPETENCY_GAP
- KNOWLEDGE_GAP
- EVIDENCE_GAP
- METHOD_GAP
- TOOLING_GAP
- INTERACTION_GAP
- CURRENCY_GAP
- EVALUATION_GAP
- FACTORY_ALGORITHM_GAP

Fix the responsible layer, rebuild/retrain/reconfigure, and repeat the same controlled test.

## Release rule

No independent examination + no unseen-task polygon + no provenance audit + no regression check = NOT RELEASED.
