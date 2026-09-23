# UI-004 — FATHER Agent Stack Model v0.1

Status: NOTATION_DRAFT
Scope: MVP-00 + reusable future employee/agent framework
Upstream: UI-003 Work Table & Boards; Agent Foundation Package; FATHER Knowledge Core
Implementation: BLOCKED until review + UI-007 tests

## 1. Purpose

Represent a FATHER specialist/agent as an understandable layered intelligence stack rather than a black-box avatar or a flat capability list.

The Stack is a projection of canonical Agent Foundation objects. It is not a second knowledge model.

## 2. Design objective

At a glance the user should be able to answer:
- Who is this specialist?
- What is the specialist for?
- What can it do?
- What does it know?
- Why can its output be trusted?
- Which tools/methods does it use?
- What is currently weak, stale, missing or untested?
- What is implementation/runtime versus professional knowledge?

## 3. Baseline layers

```text
L8  OUTCOMES / STRATEGIC CAPABILITY
L7  DECISIONS / REASONING / SYNTHESIS
L6  ACTIONS / WORKFLOWS / COLLABORATION
L5  METHODS / ALGORITHMS / TOOLS
L4  COMPETENCIES / TASK CLASSES
L3  KNOWLEDGE / RULES / CONSTRAINTS
L2  EVIDENCE / SOURCES / PROVENANCE
L1  INPUT / CONTEXT / SIGNALS
L0  RUNTIME / MODEL / MEMORY / INTERFACES
```

This is the baseline visual grammar, not an immutable universal taxonomy. A specialist may specialize/merge/add layers through governed versioned design decisions while preserving interfaces.

## 4. Layer contract

Each layer exposes:
- layer_id;
- layer_type;
- specialist_id;
- version;
- lifecycle/status;
- purpose;
- responsibility/boundary;
- input_refs;
- output_refs;
- task_refs;
- decision_refs;
- competency_refs;
- knowledge_refs;
- evidence_refs;
- method/tool/component refs;
- test/evaluation refs;
- latest validated result;
- metrics with test_context refs;
- gap/contradiction/currentness refs;
- upstream/downstream dependencies;
- change/impact refs;
- data_status: REAL | DEMO | PLANNED | UNAVAILABLE.

No percentage/score may be shown unless its definition, test context and source are available.

## 5. Stack visual states

STACK_COMPACT — thin recognizable tower/spine beside the workspace.
STACK_EXPANDED — all layers visible as readable cards.
LAYER_FOCUSED — one layer expands while others compress.
STACK_EXPLODED — layers separated to show dependency/data flow.
STACK_COMPARE — compatible layers from two specialists shown together.
STACK_MINIMAL — identity + status + active layer only.

MVP requires COMPACT, EXPANDED and LAYER_FOCUSED. Other states may be PLANNED.

## 6. Interaction with Boards and Work Table

```text
AGENT DOMAIN
    ↓
STACK_COMPACT
    ↓ expand
STACK_EXPANDED
    ↓ select L3 Knowledge
AGENT_LAYER BOARD
    ↓ promote
WORK TABLE: L3 KNOWLEDGE
    ├── related Knowledge Board
    ├── Evidence Board
    ├── Source Board
    └── Competency/Task Board
```

Layer inspection uses UI-003 Board grammar. The Stack itself does not need a parallel navigation system.

## 7. Drill-down

```text
SPECIALIST
   ↓
LAYER
   ↓
OBJECT
   ↓
RELATION
   ↓
EVIDENCE
   ↓
FRAGMENT / VERSION
   ↓
SOURCE
```

Reverse path is available where relationships exist:
SOURCE -> EVIDENCE -> KNOWLEDGE -> COMPETENCY -> TASK/DECISION -> SPECIALIST CAPABILITY.

## 8. Active-work projection

The Stack may highlight which layers are participating in the current task, but only from real task/runtime events.

Example:
INPUT active -> KNOWLEDGE consulted -> METHOD invoked -> DECISION formed -> OUTCOME produced.

This is trace visualization, not simulated thinking and not hidden chain-of-thought disclosure.

## 9. Knowledge residency projection

Where supported, a layer may expose:
K0 REQUIRED NOW / RESIDENT;
K1 LIKELY NEEDED / READY;
K2 POTENTIALLY USEFUL / DISCOVERABLE;
K3 UNKNOWN / GAP.

Residency is separate from truth/evidence strength.

## 10. Health and readiness

Avoid a single magical "intelligence score".

Instead show typed states where real data exists:
- evidence coverage;
- currentness;
- validation state;
- known gaps;
- test status;
- runtime availability;
- tool availability;
- unresolved contradictions.

UNKNOWN is a valid state.

## 11. Specialist identity and avatar relationship

Avatar answers WHO IS PRESENT.
Agent Stack answers HOW THIS SPECIALIST IS CONSTRUCTED / WHAT SUPPORTS ITS CAPABILITY.

They share specialist_id but are separate components. Changing avatar appearance must not change the Stack or specialist knowledge.

This contract is reusable for future FATHER employees: Lawyer, InfoSec, Architect, Programmer, OSINT, Researcher, etc.

## 12. ALINA reference stack for MVP

For MVP, ALINA is the reference stack.

Minimum real/structured representation:
- identity/role;
- L0 runtime/interface summary;
- L3 knowledge domain summary;
- L4 task/competency summary;
- L2 evidence/provenance link for at least the real vertical slice;
- explicit DEMO/PLANNED status for unimplemented layers.

The MVP does not need all L0-L8 backed by production engines.

## 13. Comparison rule

Two stacks/layers may be visually compared only when:
- compared objects have compatible contracts;
- metric definitions match;
- test contexts are comparable;
- versions/status are visible;
- missing data remains missing rather than normalized into invented values.

## 14. Progressive disclosure

Default:
identity + compact stack + current task/status.

On demand:
layer -> objects -> relations -> evidence -> source.

Principle:
FATHER shows what is needed for the current decision, not everything the system knows.

## 15. Failure/degraded behavior

If a layer backend is unavailable:
- retain stack geometry/identity;
- mark layer UNAVAILABLE/UNKNOWN;
- do not substitute demo data unless explicitly switched to DEMO mode;
- preserve links to last validated artifacts only when their version/status is clear.

## 16. MVP acceptance gate

UI-004 is ready for test-specification stage when:
- Stack is derived from structured data;
- layer/object drill-down uses Board grammar;
- avatar and Stack are separate;
- REAL/DEMO/PLANNED/UNAVAILABLE are explicit;
- at least one layer links to real Knowledge/Evidence/Source objects;
- no unsupported intelligence/readiness score exists;
- collapsed/expanded/focused states preserve active context.

## 17. Next step

UI-005 defines the Knowledge/Evidence/Provenance navigation contract. Then UI-006 combines the room, ALINA, Work Table, Boards and Agent Stack into low-fidelity MVP wireframes.
