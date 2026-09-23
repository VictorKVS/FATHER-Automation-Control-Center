# C02 — ALINA Analyst Source & Evidence Register v0.1

Status: DISCOVERY_IN_PROGRESS
Task: SF-BOOTSTRAP-0001
Target: ALINA Analyst

## Purpose

Register authoritative source families used to derive ALINA requirements. Discovery sources may suggest candidates; promotion requires traceable evidence and currentness status.

| ID | Authority / source | Capability family | Evidence use | Currentness note | State |
|---|---|---|---|---|---|
| SRC-ALINA-001 | ODNI ICD 203 Analytic Standards | analytic tradecraft | source quality, uncertainty, alternatives, logic, change in judgments | official ODNI source; recheck required by Currency policy | ACCEPTED_SOURCE |
| SRC-ALINA-002 | CIA Structured Analytic Techniques primer | analytic methods | method registry; assumptions, information quality, competing hypotheses, challenge techniques | official CIA source; recheck required | ACCEPTED_SOURCE |
| SRC-ALINA-003 | W3C PROV-O / PROV family | provenance | entities/activities/agents, derivation/version/provenance modeling | W3C Recommendation family | ACCEPTED_SOURCE |
| SRC-ALINA-004 | ISO 30401:2018 Knowledge management systems | knowledge management | establishing, implementing, maintaining, reviewing and improving KM systems | published; ISO reports amendments and replacement draft in progress in 2026 | ACCEPTED_WITH_CURRENCY_WATCH |
| SRC-ALINA-005 | ISO/DIS 30401 Edition 2 | knowledge management currentness | future replacement candidate for ISO 30401:2018 | DRAFT / under development; must not be treated as current standard | WATCH_ONLY |
| SRC-ALINA-006 | OMG Ontology Definition Metamodel (ODM) | ontology/knowledge representation | ontology definition, conceptual knowledge, taxonomy, interchange and inference interfaces | official OMG specification family | ACCEPTED_SOURCE |
| SRC-ALINA-007 | Cochrane Handbook v6.5/6.5.1 | evidence synthesis | explicit review questions, eligibility, systematic search/selection, data collection, bias, synthesis, interpretation, updating | official handbook; chapter versions vary and must be versioned | ACCEPTED_SOURCE |
| SRC-ALINA-008 | NIST AI RMF / AIRC | AI evaluation/governance | AI lifecycle risk management; testing, evaluation, verification and validation (TEVV) | AI RMF 1.0 is being revised in 2026 | ACCEPTED_WITH_CURRENCY_WATCH |
| SRC-ALINA-009 | NIST AI 600-1 GenAI Profile | generative AI evaluation/risk | GenAI-specific risks/actions across lifecycle | published 2024; NIST page updated 2026 | ACCEPTED_SOURCE |

## Evidence-backed implications discovered in this pass

### Knowledge management
ISO 30401 supports treating knowledge management as a maintained and continually improved management system, not a one-time ingestion job. For FATHER this supports candidate requirements around review/improvement cycles, but the standard does not by itself define ALINA's complete technical KB architecture.

### Ontology / semantic engineering
OMG ODM supports formal ontology/taxonomy/conceptual knowledge representation and interchange between heterogeneous systems. This supports an ALINA capability family for explicit conceptual/ontology modeling; it does not prove that every FATHER relation must use ODM directly.

### Evidence synthesis
Cochrane provides a strong model for explicit questions/scope, pre-specified inclusion criteria, systematic searching/selection, transparent data collection, bias assessment, synthesis and interpretation. These methods originate in systematic reviews (especially healthcare evidence), so FATHER must adapt rather than blindly generalize them to every domain.

### AI evaluation
NIST AIRC explicitly supports testing, evaluation, verification and validation of AI, while AI RMF/GenAI Profile frame risk management across AI lifecycle. This supports independent evaluation/TEVV as a capability family for ALINA/Agent Factory. It does not supply our entire specialist examination design.

## Candidate requirement impact

- ALINA-SR-003 provenance: strengthened by W3C PROV.
- ALINA-SR-005 gaps/insufficient evidence: strengthened conceptually by systematic evidence methods; exact FATHER gap policy remains design-specific.
- ALINA-SR-006 currentness: strengthened by living/update-oriented evidence practice and by current ISO/NIST revision states; FATHER currency state machine remains design-specific.
- ALINA-SR-007 relations/knowledge representation: partially strengthened by OMG ODM.
- ALINA-SR-011 independent evaluation: strengthened by NIST TEVV framing.
- New candidate family: systematic evidence acquisition/synthesis with explicit scope, selection rules, bias controls and reproducible reporting.
- New candidate family: knowledge-management review/improvement lifecycle.

## Remaining priority gaps

1. Competency modeling and instructional design.
2. Decision science / decision quality.
3. Information/data quality and metadata/catalog standards.
4. Regulatory/legal research methodology.
5. Knowledge graph engineering implementation patterns and evaluation.
6. LLM/agent evaluation benchmarks beyond risk-governance framing.

No requirement is promoted to VALIDATED solely by this register.
