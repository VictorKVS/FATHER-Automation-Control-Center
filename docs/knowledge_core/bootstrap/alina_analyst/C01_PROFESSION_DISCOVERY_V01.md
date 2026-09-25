# C01 — ALINA Analyst Profession Discovery v0.1

Status: DISCOVERY_STARTED
Task: SF-BOOTSTRAP-0001
Builder: Specialist Knowledge Engineer
Target: ALINA Analyst

## Scope

This is the first evidence-backed discovery pass. ALINA is a FATHER meta-analytical specialist that must create the knowledge foundation for future agents/specialists. This document does not claim that an external profession named "ALINA Analyst" exists. It decomposes the target role into externally evidenced professional capability families plus FATHER-specific requirements.

## Evidence class 1 — rigorous analysis / analytic tradecraft

ODNI ICD 203 establishes analytic standards for production and evaluation of analytic products and emphasizes rigor, integrity, source quality/credibility, uncertainty, distinction between underlying information and analyst assumptions/judgments, alternatives, relevance, logical argumentation, changes in judgments, accuracy and effective visual information.

Source: https://www.dni.gov/files/documents/ICD/ICD-203.pdf

CIA's Structured Analytic Techniques primer addresses analysis under incomplete/ambiguous information and includes methods such as Key Assumptions Check, Quality of Information Check, Analysis of Competing Hypotheses, Devil's Advocacy, Team A/Team B, Red Team Analysis and Alternative Futures Analysis.

Source: https://www.cia.gov/resources/csi/books-monographs/a-tradecraft-primer/

### Candidate implications for ALINA

- ALINA must explicitly assess source/information quality.
- ALINA must separate source information from analytical assumptions/judgments.
- ALINA must expose uncertainty.
- ALINA must consider alternatives when the task warrants it.
- ALINA must preserve and explain changes in analytical judgments.
- ALINA needs a method registry rather than one generic "reasoning" procedure.

These are evidence-backed candidate requirements, not yet validated ALINA competencies.

## Evidence class 2 — provenance / derivation / versioning

W3C PROV provides a domain-agnostic model for representing provenance and interchange across systems. Its model supports entities, activities, agents, derivation, versioning and provenance relationships. This directly supports FATHER's requirement for reverse traceability from knowledge/decision to source and process.

Sources:
- https://www.w3.org/TR/prov-o/
- https://www.w3.org/TR/prov-overview/

### Candidate implications for ALINA

- Provenance should be modeled as structured data, not prose-only citations.
- Knowledge creation activities and derived entities should be traceable.
- Versioning and derivation should survive transformation between source, evidence and knowledge.
- FATHER may map its provenance contract to W3C PROV concepts where useful, while retaining domain-specific extensions.

## First discovered capability families

1. Source and information quality assessment.
2. Evidence/provenance formation.
3. Separation of information, assumptions, judgments and uncertainty.
4. Structured analytical methods and alternative hypotheses.
5. Logical argumentation and decision trace.
6. Change-of-judgment/currentness trace.
7. Knowledge transformation and canonical packaging (FATHER-specific; external evidence discovery continues).
8. Graph/ontology/semantic knowledge engineering (research pending).
9. Competency/learning engineering for future agents (research pending).
10. Independent evaluation and unseen-task testing (research pending).

## Open evidence gaps

- Knowledge engineering / ontology engineering professional foundations.
- Evidence synthesis and systematic review methods.
- Knowledge management and information science.
- Competency modeling / instructional design.
- Agent evaluation and LLM/AI evaluation standards.
- Decision science and decision-support methodology.
- Data quality / metadata / cataloging standards.
- Regulatory research methodology.
- Software/system interfaces needed for executable ALINA.

## C01 status

PARTIAL. Two capability families now have primary-source support; the profession model is intentionally incomplete.

Next: C02 Source & Evidence Register, followed by research passes for knowledge engineering, evidence synthesis, competency engineering and AI evaluation.
