# C03 — ALINA Analyst Task Graph v0.1

Status: DERIVATION_IN_PROGRESS
Derived from: C00 Target Result & Acceptance, C01 Profession Discovery, C02 Source & Evidence Register
Rule: tasks are derived from required observable results; they are not an arbitrary feature list.

## 1. Derivation method

For each C00 acceptance condition ask:

1. What observable result must exist?
2. What task must ALINA perform to produce it?
3. What input does that task require?
4. What output must it produce?
5. Which downstream task consumes that output?
6. What failure/gap state must be explicit?
7. How can the task later be tested?

This document begins with the first root task only. Later tasks are added step-by-step after review.

---

# T00 — Establish Target Result and Operating Context

## Why this task exists

C00 requires ALINA to work from the desired observable result rather than immediately producing implementation. Therefore the first operational task of ALINA is to establish what is being created, why, for whom, under what conditions and how success will be recognized.

Without T00, all downstream requirements, competencies, knowledge, tests and implementation choices can be internally consistent yet solve the wrong problem.

## Trigger

A request, idea, identified gap, proposed specialist/agent/component, or change request enters ALINA.

## Inputs

- original request/problem statement;
- requester/stakeholder information when available;
- known context;
- known constraints;
- existing FATHER artifacts when applicable;
- explicit evidence/source references when supplied.

Inputs may be incomplete or contradictory.

## Internal analytical stages

T00.1 Preserve original request as immutable/request-versioned input.

T00.2 Identify requested target object:
agent, specialist, component, workflow, knowledge capability or other significant artifact.

T00.3 Identify intended consumers/stakeholders.

T00.4 Extract stated desired outcomes.

T00.5 Separate stated facts, assumptions, preferences, constraints and unresolved questions.

T00.6 Define observable result candidates.

T00.7 Identify operating context and expected workload envelope where known.

T00.8 Identify success/acceptance criteria already stated.

T00.9 Detect missing, ambiguous or conflicting information.

T00.10 Decide whether the basis is sufficient to proceed, requires research, requires stakeholder clarification, or requires explicit assumption with review.

T00.11 Produce versioned Target Context Package.

## Output — Target Context Package

Minimum logical objects:

- target_id;
- request_version;
- problem_statement;
- purpose;
- target_object_type;
- stakeholders/consumers;
- desired_outcomes;
- observable_result;
- context;
- constraints;
- operating_envelope;
- known facts;
- assumptions;
- open_questions;
- contradictions;
- initial success criteria;
- gaps/research orders;
- provenance links;
- status;
- version.

## Status model

RECEIVED
-> ANALYZING
-> SUFFICIENT_FOR_NEXT_STAGE

Alternative states:
NEEDS_CLARIFICATION
NEEDS_RESEARCH
CONTRADICTORY_INPUT
BLOCKED
SUPERSEDED

## Boundaries

T00 does NOT:
- design the final implementation;
- select a permanent model/provider;
- invent missing professional knowledge;
- declare unsupported assumptions as facts;
- build the complete Task/Decision/Competency graphs.

Its job is to establish the target and operating frame that makes those later activities meaningful.

## First scheme candidate

```text
REQUEST / IDEA / GAP
        |
        v
[Preserve Original Input]
        |
        v
[Identify Target + Stakeholders]
        |
        v
[Extract Outcomes + Constraints]
        |
        v
[Separate Facts / Assumptions / Unknowns]
        |
        v
[Define Observable Result]
        |
        v
[Define Context / Operating Envelope]
        |
        v
[Check Sufficiency / Contradictions]
   +----+---------+---------+
   |              |         |
   v              v         v
READY         RESEARCH   CLARIFY/BLOCK
   |              |         |
   +--------------+---------+
                  |
                  v
        TARGET CONTEXT PACKAGE
                  |
                  v
          downstream C03 tasks
```

## Test intent — not yet full Test Specification

Later pre-implementation tests must verify at least:
- ALINA does not lose the original request;
- separates explicit input from its own inference;
- identifies missing critical context;
- does not proceed silently through material contradiction;
- can express an observable target result;
- can create a gap/research order when basis is insufficient;
- preserves version/provenance;
- produces an output consumable by the next task.

## Trace to C00

Primary:
- Acceptance A — Target derivation.
- Acceptance B — Analysis-first discipline.
- Acceptance E — Gap behavior.
- Acceptance L — History preservation.

Supporting:
- Acceptance C — Traceability.
- Acceptance H — Metric validity, because workload/context begins here.
- Acceptance J — Change resilience, because request/context is versioned.

## Downstream influence

T00 output becomes an input to:
- further Task Graph derivation;
- Decision Graph;
- A19 Requirement Derivation;
- operating/workload profiles;
- test-context design;
- acceptance tests;
- impact analysis when target/context changes.

If T00 changes materially, downstream artifacts must be marked for impact review rather than silently updated.
