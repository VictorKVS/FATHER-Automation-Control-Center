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

## Application of A19 — ALINA Analyst requirement baseline v0

This is a candidate baseline, not a certified final profession model. Requirements derived only from FATHER's accepted bootstrap mission are FATHER_SPECIFIC/TASK_DERIVED; external professional requirements remain pending C01/C02 evidence discovery.

| ID | Candidate requirement | Origin | Derived from | Validation |
|---|---|---|---|---|
| ALINA-SR-001 | Decompose an unknown source into stable traceable structural fragments without losing source/version locators. | R3, R5 | bootstrap reference test + provenance constraint | unseen-source polygon + provenance audit |
| ALINA-SR-002 | Extract candidates while keeping FACT, CLAIM, INFERENCE, HYPOTHESIS, REQUIREMENT and DECISION distinct. | R3, R5 | minimal constraints + reference test | labeled unseen corpus + Examiner |
| ALINA-SR-003 | Bind significant knowledge assertions to evidence, fragment, document version and original source. | R3, R4, R5 | provenance/evidence constraints | reverse-trace audit |
| ALINA-SR-004 | Preserve contradictions and expose unresolved conflicts instead of silently reconciling them. | R3, R4, R5 | bootstrap constraint | conflicting-source test |
| ALINA-SR-005 | Detect insufficient knowledge/evidence and emit explicit gaps/unknowns. | R3, R4, R5 | gap constraints | incomplete-evidence unseen test |
| ALINA-SR-006 | Expose source/version currentness; never imply currentness without evidence. | R3, R4, R5 | Knowledge Currency principle | stale/changed-source test |
| ALINA-SR-007 | Form evidence-backed relations and retain context/method for weights. | R3, R5 | graph reference test | graph reconstruction test |
| ALINA-SR-008 | Produce canonical Knowledge Packets reusable by FATHER, not only prose summaries. | R3, R5 | mission + reference test | schema/traceability acceptance |
| ALINA-SR-009 | Explain significant outputs through an auditable reverse chain to original evidence. | R3, R4, R5 | Examiner trace requirement | sampled trace audit |
| ALINA-SR-010 | Operate through defined interfaces with Source Intake, Knowledge Miner, Knowledge Core, Specialist Factory, Examiner and other specialists. | R5 | discovery question 9 | integration contract test |
| ALINA-SR-011 | Submit competence to independent examination and unseen-task testing; no self-certification. | R4, R5 | release rule | independent Examiner + polygon |
| ALINA-SR-012 | Trigger impact review when upstream source/version changes affect downstream knowledge/requirements. | R3, R4, R5 | currency/impact architecture | controlled change regression |

Current evidence state: ALINA-SR-001..012 are PROPOSED from accepted FATHER design/bootstrap evidence and are not yet external-profession-validated. C01/C02 must determine external support, FATHER-only requirements and missing requirements.

Immediate derivation backlog for each candidate: TASK -> DECISION -> ACTION -> EXPECTED RESULT -> COMPETENCY -> KNOWLEDGE -> METHOD -> TOOL -> EVIDENCE -> FAILURE MODE -> TEST.

No candidate becomes VALIDATED merely because it appears in this bootstrap document.
