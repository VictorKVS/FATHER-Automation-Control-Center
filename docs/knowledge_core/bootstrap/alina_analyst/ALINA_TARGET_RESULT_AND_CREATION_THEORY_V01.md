# ALINA Target Result & Creation Theory v0.1

Status: DESIGN_BASELINE
Task: SF-BOOTSTRAP-0001
Purpose: define the target result before continuing ALINA construction.

## 1. Target result

ALINA is successful when, given a target future agent/specialist and its context, she can reproducibly produce an evidence-backed Agent Foundation Package that another Factory component can use to assemble, train/configure, evaluate and maintain the agent.

ALINA is not merely a chatbot, summarizer, prompt generator or document reader.

## 2. Required output of ALINA

For target agent X, ALINA must produce:

1. Target / Problem Definition
2. Context & Stakeholder Model
3. Success / Acceptance Criteria
4. Requirement Set with origin and evidence
5. Task Graph
6. Decision Graph
7. Competency Graph
8. Knowledge Requirements Graph
9. Source & Evidence Plan
10. Knowledge Foundation / Knowledge Packets
11. Method & Algorithm Register
12. Tool & Interface Map
13. Constraints / Risks / Failure Modes
14. Learning / Assembly Plan
15. Examination Specification
16. Polygon / Evaluation Plan
17. Gap Register
18. Currency / Update Policy
19. Provenance & Decision Trace
20. Release Evidence Pack

This package is the primary artifact. A runnable LLM agent is a downstream implementation artifact.

## 3. Combined creation theory

FATHER will not depend on one universal invention theory. ALINA uses a controlled composition of complementary methods.

### Layer A — First-principles / dependency reconstruction

Inspired by the dependency-tree framing visible in Ryan North's *How to Invent Everything*: determine what foundational capabilities must exist before higher capabilities can be built.

Use in FATHER:
TARGET CAPABILITY -> prerequisites -> prerequisite prerequisites -> minimal viable foundation -> build order.

### Layer B — Systems engineering lifecycle

Use systems-engineering lifecycle thinking to define stakeholders, needs, requirements, architecture, verification, validation, operation, maintenance and retirement. The process is iterative and recursive.

Use in FATHER:
NEED -> REQUIREMENTS -> ARCHITECTURE -> IMPLEMENTATION -> VERIFICATION -> VALIDATION -> OPERATION -> UPDATE/RETIRE.

### Layer C — TRIZ / contradiction-driven invention

When requirements conflict or obvious solutions fail:
problem -> contradiction -> resources -> ideal result -> solution principles -> candidate solutions -> evaluation.

TRIZ is a problem-solving layer, not a substitute for evidence, domain knowledge or lifecycle engineering.

### Layer D — Design Science build/evaluate loop

Treat the Agent Foundation and agent implementation as purposeful artifacts:
problem/context -> requirements -> build artifact -> demonstrate -> evaluate -> learn -> redesign.

Evaluation must be planned from the target result, not appended after construction.

### Layer E — Evidence / provenance

Every significant requirement, knowledge object and design decision must preserve:
SOURCE -> EVIDENCE -> REQUIREMENT/KNOWLEDGE -> DESIGN DECISION -> ARTIFACT -> EVALUATION.

### Layer F — Evolution

A released agent is not final:
source/environment/task change -> impact analysis -> gap -> research -> changed foundation -> regression -> new release.

## 4. Canonical ALINA creation loop

```text
DEFINE DESIRED RESULT
        ↓
DEFINE CONTEXT / SUCCESS / CONSTRAINTS
        ↓
DECOMPOSE CAPABILITY
        ↓
BUILD DEPENDENCY TREE
        ↓
DISCOVER TASKS
        ↓
DISCOVER DECISIONS
        ↓
DERIVE REQUIREMENTS
        ↓
FIND CONTRADICTIONS / RISKS
        ↓
DERIVE COMPETENCIES
        ↓
DERIVE KNOWLEDGE / METHODS / TOOLS
        ↓
SOURCE & EVIDENCE RESEARCH
        ↓
BUILD AGENT FOUNDATION
        ↓
ASSEMBLE PROTOTYPE
        ↓
VERIFY AGAINST REQUIREMENTS
        ↓
VALIDATE ON REAL/UNSEEN TASKS
        ↓
POLYGON / A-B / METRICS
        ↓
GAPS?
   YES ─┘  └─ NO
   ↓          ↓
RESEARCH    RELEASE
   ↓          ↓
REDESIGN   WATCH / EVOLVE
   └──────────↺
```

## 5. Starting question

Before ALINA creates any agent, she must answer:

"What observable result must this agent produce, in what context, for whom, under which constraints, with what evidence, and how will we know independently that it works?"

If this is unresolved, detailed curriculum, prompt, model selection and fine-tuning are premature.

## 6. Bootstrap application to ALINA herself

Target: ALINA Analyst.

Observable result:
Given an unfamiliar target specialist/agent, ALINA creates a traceable Agent Foundation Package whose requirements and knowledge can be followed back to evidence, whose dependencies are explicit, whose gaps are visible, and whose fitness can be tested independently on unseen tasks.

Bootstrap acceptance requires at least:
- one unfamiliar target agent case;
- complete foundation package;
- reverse provenance sample;
- explicit contradictions/gaps;
- independent Examiner;
- unseen-task polygon;
- regression after at least one controlled source/requirement change.

## 7. Effect on existing build plan

C01/C02 remain evidence discovery inputs, but C03 must no longer begin as an isolated Task Graph.

Before C03 create C00 Target Result / Problem / Context / Acceptance artifact. Then:
C00 -> C03 Task Graph -> C04 Decision Graph -> A19 Requirement derivation -> C05 Competency Graph -> C06 Knowledge Requirements -> C07 Methods -> C08 Tools -> C09 Failures -> C10 Learning -> C11 Curriculum -> C12 Exam -> C13 Polygon -> C14 Gaps -> C15 Release Evidence Pack.

This ordering is provisional and must be tested during ALINA bootstrap.


## 8. Principle of Modular Experimental Architecture

Every material part of ALINA and every future Agent Foundation is designed as a replaceable, versioned block/object/callable component with an explicit contract. The architecture must allow a component to be evaluated, A/B/n tested, shadow-tested, replaced by a better future implementation, rolled back, and traced without rebuilding the whole chain.

Canonical component contract:

```text
COMPONENT
├── component_id / type / version
├── purpose
├── position_in_pipeline
├── input_contract
├── output_contract
├── dependencies
├── implementation
├── configuration
├── evidence / provenance
├── metrics
├── quality gates
├── experiment hooks
├── alternatives
├── compatibility contract
├── failure / fallback policy
├── cost / latency / resource telemetry
├── lifecycle state
└── replacement / rollback history
```

A/B/n testing is a cross-cutting capability, not a final-stage feature. Every replaceable component should be routable through an Experiment Layer when meaningful:

```text
INPUT
  ↓
COMPONENT INTERFACE
  ↓
EXPERIMENT ROUTER
 ├── A: implementation v1
 ├── B: implementation v2
 └── N: candidate implementation
  ↓
COMMON OUTPUT CONTRACT
  ↓
EVALUATOR
  ↓
METRICS + EVIDENCE + DECISION
  ↓
PROMOTE / RETAIN / ROLLBACK / CONTINUE TEST
```

Metrics are local to a component and also propagate to end-to-end outcome metrics. No single universal score is assumed. Each component defines task-appropriate quality, latency, cost, resource, reliability, safety and traceability measures where applicable.

Replacement rule: downstream consumers depend on the component contract, not on one implementation. A future better model, algorithm, retriever, graph engine, evaluator, source connector or reasoning method may replace the current implementation if compatibility and regression gates pass.

## 9. Pipeline-as-Graph and Control Center Projection

The development and runtime chain must be represented as a graph of callable components. Each component has a visible place in ALINA Control Center.

The site must support, progressively:
- pipeline/graph view showing component position and dependencies;
- component card with contract, version, status, owner and evidence;
- live calls/events and input/output references;
- local and downstream metrics;
- A/B/n experiment state and comparison;
- version history and replacement candidates;
- health/failure/fallback state;
- provenance and decision trace;
- impact view showing what would be affected by replacement;
- drill-down from end result back through components to evidence/source.

Thus the same architecture is simultaneously executable, measurable, experimentally replaceable and observable.

## 10. Effect on Agent Foundation Package

The previously defined Agent Foundation Package remains the logical output, but every section must be decomposable into versioned objects/components and linked through explicit interfaces. Task Graph, Decision Graph, Competency Graph, Knowledge Requirements, evidence, methods, tools, evaluation and currency are not static report chapters; they become addressable graph objects that can evolve independently under compatibility and impact controls.
