# ALINA Work Journal — Knowledge Core Bootstrap

## Entry 0001

- operation: BOOTSTRAP_SPECIALIST_TASK_CREATED
- target: ALINA Analyst
- task_id: SF-BOOTSTRAP-0001
- result: READY_FOR_DISCOVERY
- changed: Added the first reference-specialist build task for Specialist Factory.
- decision: Start validation of FATHER from the analytical specialist itself, before mass document ingestion and before downstream Lawyer/InfoSec/System Analyst specialists.
- quality rule: Do not pre-fill ALINA's profession model; Specialist Knowledge Engineer must discover and evidence it.
- next_action: C01 Profession Discovery for ALINA Analyst.
- improvement: Add executable schemas/state machine after the first controlled discovery pass.
- priority: P0

## Entry 0002

- operation: SPECIALIST_REQUIREMENT_ALGORITHM_ADDED_AND_APPLIED
- target: ALINA Analyst
- algorithm: A19 Specialist Requirement Derivation
- result: CANDIDATE_BASELINE_CREATED
- changed: Added evidence-driven derivation and ALINA-SR-001..012.
- evidence_state: PROPOSED_FROM_FATHER_DESIGN; external profession evidence pending C01/C02.
- quality_rule: requirement must trace why it exists, task/decision/competency, evidence and test.
- currentness_rule: upstream source/task/risk/architecture changes trigger impact review.
- next_action: run C01/C02 discovery against external professional, academic and standards sources; enrich/reject/add requirements.
- improvement: add machine-readable specialist_requirement schema after first evidence-backed discovery pass.
- priority: P0

## Entry 0003 — ALINA Development Journal becomes a reusable Factory template

- operation: DEVELOPMENT_PROCESS_DECISION
- target: ALINA Analyst
- result: ACCEPTED
- decision: Keep a detailed development journal for ALINA from bootstrap through independent release; later analyze it and convert the successful process into a reusable template for creating future FATHER agents/specialists.
- principle: ALINA is the reference bootstrap case. The journal must capture not only successful artifacts but also mistakes, rejected hypotheses, architecture changes, evidence gaps, repeated work and reasons for decisions.
- reuse_goal: derive FATHER Agent Foundation Template / Specialist Factory playbook from observed ALINA development rather than designing the final template only in advance.
- mandatory_per_action: timestamp; stage; operation; input; assumptions; source/evidence used; artifact/result; decision; errors/gaps; what changed; what should improve; how to improve; priority; metrics when available; next action.
- traceability: every material journal entry should reference affected requirement/task/competency/knowledge/source/artifact/commit IDs when available.
- quality_rule: journal is append-only history; later conclusions may supersede earlier conclusions but must not erase them.
- analysis_plan: after ALINA reaches major gates, perform retrospective analysis to identify invariant steps, optional steps, failed approaches, bottlenecks, quality gates, automation candidates and profession-specific exceptions.
- template_output: AGENT_FOUNDATION_TEMPLATE + BUILD_PLAYBOOK + QUALITY_GATES + JOURNAL_TEMPLATE + METRICS_BASELINE.
- next_action: continue C01/C02 ALINA discovery while logging each substantive operation under this contract.
- priority: P0

## Entry 0004 — C01 Profession Discovery started

- operation: EVIDENCE_BACKED_PROFESSION_DISCOVERY
- target: ALINA Analyst
- result: PARTIAL_C01_CREATED
- sources_checked: ODNI ICD 203; CIA Structured Analytic Techniques primer; W3C PROV-O/PROV Overview.
- discovered: analytic tradecraft/source-quality/uncertainty/alternatives and structured provenance/derivation/versioning have primary-source support.
- decision: treat ALINA as a composite FATHER meta-analytical role; do not pretend a single external profession exactly matches it.
- changed: created C01_PROFESSION_DISCOVERY_V01.md and identified first capability families plus evidence gaps.
- gaps: knowledge engineering; ontology engineering; evidence synthesis; competency/instructional engineering; AI/agent evaluation; decision science; data quality/cataloging; regulatory research.
- what_to_improve: broaden source map before promoting candidate requirements to EVIDENCED/VALIDATED.
- how_to_improve: research primary standards, professional bodies and academic frameworks for each gap; register evidence in C02.
- next_action: create C02 Source & Evidence Register and continue evidence discovery.
- priority: P0

## Entry 0005 — C02 Source & Evidence Register v0.1

- operation: SOURCE_AND_EVIDENCE_DISCOVERY
- target: ALINA Analyst
- result: C02_V01_CREATED
- sources_added: ISO 30401:2018; ISO/DIS 30401; OMG ODM; Cochrane Handbook; NIST AI RMF/AIRC; NIST AI 600-1; retained ODNI/CIA/W3C sources from C01.
- important_currency_finding: ISO 30401:2018 is published but has amendments and a replacement draft in progress; NIST AI RMF 1.0 is under revision. This validates the need to store source currentness separately from source authority.
- capability_updates: knowledge-management lifecycle; ontology/semantic representation; systematic evidence synthesis; AI TEVV/evaluation.
- caution: domain-specific methods (e.g. Cochrane healthcare review methodology) are evidence sources for method principles, not universal rules for all FATHER domains.
- changed: created C02_SOURCE_EVIDENCE_REGISTER_V01.md; linked sources to candidate ALINA requirements.
- remaining_gaps: competency/instructional engineering; decision science; data/metadata quality; regulatory research; graph engineering evaluation; LLM/agent benchmarks.
- next_action: evidence pass on competency formation + decision science, then update ALINA requirements and C03 Task Graph.
- priority: P0

## Entry 0006 — Development journal causal-trace rule

- operation: JOURNAL_GOVERNANCE_UPDATE
- target: ALINA Analyst / future Agent Foundation Template
- result: ACCEPTED
- why_now: the ALINA bootstrap is moving from source discovery into requirement, task, decision, competency and knowledge formation. Decisions made now will constrain later graphs, curriculum, runtime and evaluation.
- decision: every substantive development step must record not only WHAT was done, but WHY it was done, WHY it is needed, WHAT it changes, and HOW it constrains or enables the next planned steps.
- mandatory_causal_fields: problem_or_trigger; objective; action; rationale; evidence_or_assumption; artifact_changed; immediate_effect; downstream_effect; dependencies_created; risks_or_gaps; validation_needed; next_steps_enabled; next_steps_blocked; supersedes_or_is_superseded_by; metrics_if_available.
- forward_trace_rule: each important decision must identify the downstream artifacts it is expected to influence (Task Graph, Decision Graph, Competency Graph, Knowledge Requirements, Methods, Tools, Curriculum, Exam, Polygon, Runtime, Agent Foundation).
- backward_trace_rule: later artifacts must be able to point back to the journal decision/evidence that caused them.
- planning_rule: before starting the next stage, write its expected purpose, inputs, outputs, quality gate and effect on following stages; after execution, compare expected vs actual.
- no_rewrite_rule: journal remains append-only. Wrong decisions are marked superseded/rejected with reason; they are not erased.
- template_goal: this causal development history will later be mined to produce the reusable FATHER Agent Build Playbook and Agent Foundation Template.
- immediate_effect: C03 and later artifacts must be built with explicit causal links to C01/C02 evidence and A19 requirements.
- next_steps_enabled: define the staged ALINA build plan; then execute Competency Engineering + Decision Science evidence pass; then derive C03 Task Graph rather than invent it directly.
- priority: P0


## Entry 0007 — Target result established before further construction

- operation: TARGET_RESULT_AND_CREATION_THEORY_DEFINED
- target: ALINA Analyst
- trigger: continuing from sources directly into Task/Competency graphs risked building detailed artifacts without a fixed observable end-state.
- objective: establish what ALINA must ultimately produce and select complementary creation theories before deriving further internal structure.
- action: created ALINA_TARGET_RESULT_AND_CREATION_THEORY_V01.md.
- rationale: dependency-first invention, systems lifecycle engineering, contradiction solving, build/evaluate design science, evidence provenance and continuous evolution solve different parts of the problem; no single method is treated as universal.
- evidence_basis: Ryan North dependency/technology-tree framing; ISO/IEC/IEEE 15288 lifecycle framework; Altshuller/TRIZ contradiction-oriented problem solving; Design Science build/evaluate literature.
- immediate_effect: ALINA's primary product is now defined as an Agent Foundation Package, not a prompt or runnable chatbot.
- downstream_effect: insert C00 Target Result / Problem / Context / Acceptance before C03; all later graphs and curricula must derive from that target.
- dependencies_created: success criteria and independent evaluation must be defined before implementation/model/fine-tuning choices.
- risk: sources have different scopes and evidentiary strength; they must remain complementary methods, not be falsely merged into one established scientific theory.
- validation_needed: use ALINA to build at least one unfamiliar agent foundation and test traceability, completeness, unseen-task performance and change regression.
- next_steps_enabled: create C00 for ALINA herself; then derive C03 Task Graph from C00+C01+C02 rather than intuition.
- next_steps_blocked: premature model selection, prompt engineering, fine-tuning and detailed curriculum.
- priority: P0


## Entry 0008 — Modular experimental architecture becomes a cross-cutting requirement

- operation: ARCHITECTURE_PRINCIPLE_ADDED
- target: ALINA Analyst + future Agent Factory + Control Center
- trigger: Agent Foundation was defined as a package of artifacts, but without a universal rule guaranteeing that every stage can be measured, experimentally compared and replaced later.
- objective: prevent monolithic ALINA/agent implementations and preserve continuous technological evolution.
- action: added Principle of Modular Experimental Architecture, component contract, Experiment Router, local/end-to-end metrics, replacement/rollback rules and Control Center projection.
- rationale: future algorithms/models/tools will improve; FATHER must replace one block without rewriting unrelated blocks and must prove that the replacement is actually better in the relevant context.
- immediate_effect: every major future block is treated as versioned callable component/object with explicit input/output contract, metrics, experiment hooks and lifecycle.
- downstream_effect: C00-C15 artifacts must identify component boundaries and measurable outputs; C03/C04 graphs become executable/observable graph candidates; C12/C13 must support component-level and end-to-end A/B/n evaluation; Control Center must expose every component's position, state, metrics and experiments.
- dependencies_created: common contracts, experiment routing, metric registry, compatibility/version policy, impact analysis and telemetry/event model.
- risk: over-fragmentation and metric gaming. Components should be split at meaningful responsibility/contract boundaries; local metrics must be checked against end-to-end outcomes.
- validation_needed: during ALINA bootstrap replace at least one component implementation with an alternative and demonstrate A/B comparison, compatibility, regression check and rollback.
- next_steps_enabled: C00 acceptance criteria can now include modularity/replaceability/observability; C03 can identify callable stages rather than only prose tasks.
- priority: P0


## Entry 0009 — Metrics require a valid test context

- operation: COMPONENT_METRIC_VALIDITY_RULE_ADDED
- target: ALINA modular architecture / Agent Factory / Control Center
- trigger: a component can appear competitive because of a metric measured under irrelevant or non-comparable inputs/load. Naked metric values can therefore drive false promotion decisions.
- objective: ensure every block is tested under a declared use case and workload before its metrics are used for A/B/n decisions.
- action: added mandatory Test Context and Passport Question Set to every component; metric results now bind value to component version, workload, dataset, environment, method, timestamp and run ID.
- rationale: metric validity is conditional. Performance/quality/cost values from different operating regimes are not automatically comparable.
- immediate_effect: component passport must answer whether the test/metric makes sense under the stated inputs and load.
- downstream_effect: Experiment Router requires a comparability gate; Polygon must generate representative workload profiles; Metric Registry must store definitions and validity scopes; Control Center must display metric context beside metric values; promotion/rollback decisions must reference test runs.
- dependencies_created: Test Context object, Metric Definition object, Test Run object, Comparability Gate and representative workload profiles.
- risks: excessive test dimensions can make experiments expensive; insufficient dimensions can make results misleading. Start with decision-relevant context and expand from observed failures.
- validation_needed: run the same component under at least two materially different workload profiles and demonstrate that FATHER does not incorrectly generalize one result to the other.
- next_steps_enabled: C00 can define ALINA operating envelopes; C03 tasks can attach workload classes; C12/C13 can derive tests from those classes.
- priority: P0


## Entry 0010 — ALINA declared transparent, predictable, adaptable and extensible foundation

- operation: FOUNDATION_QUALITY_AND_DECISION_GOVERNANCE_BASELINE
- target: ALINA Analyst
- trigger: modularity, A/B testing and context-valid metrics were defined, but the foundational non-functional qualities and formal treatment of design decisions were not yet stated as one mandatory baseline.
- objective: ensure ALINA remains understandable and evolvable as future agents, models, methods and knowledge domains are added.
- action: declared mandatory foundation qualities and introduced FATHER Decision Record (FDR) for every significant decision.
- why: ALINA will become upstream infrastructure for many agents. Opaque or irreversible choices made here would multiply downstream technical debt and make future evidence, replacement and impact analysis unreliable.
- immediate_effect: significant decisions now require both chronological Journal trace and an addressable normative FDR object.
- downstream_effect: C00 acceptance criteria must include transparency/predictability/adaptability/extensibility; C03-C10 objects must expose contracts and dependencies; C12/C13 must test these properties where measurable; Control Center must render FDR, version, impact and supersession links.
- design_distinction: Journal = what happened and why over time. FDR = current/superseded formal decision and its normative rationale/conditions.
- risks: excessive bureaucracy for trivial choices. FDR is required for significant decisions; trivial D0 choices remain lightweight under decision-significance rules.
- validation_needed: demonstrate end-to-end trace from one released behavior to component -> FDR -> journal -> evidence/test, then replace the component and preserve history.
- next_steps_enabled: freeze C00 acceptance baseline and begin C03 with governance-ready component/task objects.
- priority: P0


## Entry 0011 — Analysis-first implementation gate

- operation: DEVELOPMENT_ORDER_FIXED
- target: all significant ALINA/FATHER blocks
- trigger: modular architecture still permits premature coding unless the required order of analytical artifacts is explicit.
- objective: make implementation the consequence of analysis, not the place where requirements and architecture are discovered accidentally.
- decision: mandatory order is Analytical Passport -> Scheme/Notation -> Test Specification -> Review Gate -> Program/Instruction -> Test Run -> Evidence/Metrics -> Release decision.
- why: the passport explains what/why/how and boundaries; the scheme exposes flows/interfaces/internal structure; pre-implementation tests make expected behavior falsifiable; only then is code or an operational instruction justified.
- immediate_effect: production implementation is BLOCKED when passport, scheme or meaningful test specification is absent for a significant block.
- downstream_effect: C03-C10 must produce implementation-ready analytical objects; C12/C13 reuse predeclared tests and workload contexts; Control Center can show maturity stage of each block; Factory can automate promotion gates.
- change_effect: material changes must update analysis artifacts first; emergency fixes require retrospective documentation and regression evidence.
- risk: documentation overhead. Mitigation: depth scales with decision significance D0-D4; trivial D0 operations remain lightweight.
- validation_needed: apply this sequence to the first executable ALINA component and verify code can be derived without inventing unstated requirements during implementation.
- next_steps_enabled: C00 can define the artifact maturity gates; first ALINA component will become the reference implementation of this rule.
- priority: P0


## Entry 0012 — Bootstrap cost accepted to create a reusable development template

- operation: BOOTSTRAP_INVESTMENT_DECISION
- target: ALINA Analyst / FATHER Agent Factory
- trigger: analysis-first development, passports, notation, pre-implementation tests, metrics and decision records increase the time required for the first ALINA build.
- objective: intentionally invest more time in the reference build so the resulting process becomes a reusable development template for subsequent agents and components.
- decision: optimize the ALINA bootstrap for reproducibility, traceability and reuse rather than minimum calendar time to first code.
- why: the first build pays the discovery cost of defining artifacts, gates, contracts, tests and decision rules. Subsequent builds should reuse those assets and automate repeatable steps instead of rediscovering the process.
- expected_payoff: lower redesign/rework; faster later specialist builds; comparable components; reusable tests; clearer handoff to coding agents; safer replacement/evolution; measurable Factory throughput.
- immediate_effect: do not bypass analytical gates merely to produce executable ALINA earlier.
- downstream_effect: after ALINA bootstrap, perform a retrospective and extract AGENT_FOUNDATION_TEMPLATE, COMPONENT_PASSPORT_TEMPLATE, FDR_TEMPLATE, TEST_SPEC_TEMPLATE, BUILD_PLAYBOOK, QUALITY_GATES, METRICS_BASELINE and AUTOMATION_CANDIDATES.
- metrics_to_collect: elapsed time by stage; active work time where observable; rework count; returns to prior stages; defects/gaps found before code vs after code; artifact reuse; test reuse; number of manual decisions; automation candidates; later build cycle-time comparison.
- quality_rule: extra time is justified only if it produces reusable knowledge/artifacts or reduces measurable downstream uncertainty/rework; ceremony with no demonstrated value becomes a candidate for simplification.
- validation_needed: compare the first later specialist/agent build using the template against the ALINA bootstrap baseline.
- next_steps_enabled: proceed deliberately with C00 as the first full reference artifact under the new development order.
- priority: P0


## Entry 0013 — Development discipline becomes an ALINA operating rule

- operation: SELF_RULE_PROMOTION
- target: ALINA Analyst behavior
- trigger: the analysis-first sequence was defined as a development rule for building ALINA, but ALINA must later reproduce the same disciplined process when building foundations for other agents/components.
- objective: convert the bootstrap lesson into an inherited behavioral rule of ALINA and future Factory outputs.
- decision: ALINA must not jump from idea/request directly to program/instruction for significant work. She first establishes purpose/result/context/evidence, then Passport, Scheme, Test Specification and quality gate, and only then implementation instructions.
- why: otherwise the Factory would reproduce the same premature-coding failure mode at scale.
- immediate_effect: this rule becomes part of ALINA's own competency/behavior requirements, not merely project documentation.
- downstream_effect: add it to C00 acceptance criteria, C03 tasks, C04 decisions, C05 competencies, C06 knowledge requirements, C11 curriculum and C12/C13 examination/polygon scenarios.
- inheritance_rule: future agents/components produced through ALINA inherit this discipline for significant decisions unless a documented FATHER exception exists.
- gap_behavior: insufficient knowledge/evidence creates GAP/Research Order; ALINA must not silently fill the missing design basis.
- validation_needed: give ALINA an underspecified future-agent request and verify that she requests/derives missing analytical artifacts instead of immediately generating implementation.
- priority: P0


## Entry 0014 — C00 foundation baseline started from desired result

- operation: C00_TARGET_RESULT_BASELINE
- target: ALINA Analyst
- trigger: foundational principles are now sufficient to stop adding abstract rules and begin the reference build from first principles.
- objective: define the observable result and acceptance boundary before deriving tasks, decisions, competencies, knowledge or implementation.
- why_this_first: all later artifacts must be consequences of the desired result; otherwise Task/Competency/Knowledge graphs risk becoming inventories without a proof of necessity.
- action: created C00_TARGET_RESULT_CONTEXT_ACCEPTANCE_V01.md.
- artifact_scope: why ALINA exists; target observable result; consumers; operating context; self-rule; Agent Foundation output; quality attributes; modular/A-B requirements; v1 acceptance gates; non-goals; first reference validation scenario; downstream derivation rules.
- immediate_effect: C03 now has a concrete source of required observable behaviors instead of being invented from intuition.
- downstream_effect: C03 tasks must map to C00 acceptance gates; C04 decisions map to C03; A19 requirements map to tasks/decisions/risks; later competency/knowledge/test artifacts inherit this trace.
- deliberate_limit: this is BASELINE_DRAFT, not final truth. C01/C02 and later evidence may force revision; such revision must be versioned and journaled.
- testability_effect: ALINA v1 READY is separated from merely RUNNING. Acceptance requires traceability, gap behavior, semantic integrity, modular replacement/A-B, metric validity, independent unseen-task evaluation, change regression, observability and history preservation.
- next_action: review C00 for missing first-principles acceptance conditions, then derive C03 Task Graph one task at a time with explicit C00 trace links.
- priority: P0


## Entry 0015 — C03 derivation begins with T00 Target Result & Context

- operation: TASK_GRAPH_DERIVATION_T00
- target: ALINA Analyst
- trigger: C00 now defines observable result and v1 acceptance gates; the next step is to derive behavior from those outcomes without jumping to implementation.
- objective: identify the first indispensable operational task of ALINA.
- derivation: C00 Acceptance A/B/E/L -> need to establish target/result/context, preserve original input, expose unknowns and avoid premature implementation -> T00 Establish Target Result and Operating Context.
- why_first: every later task depends on knowing what result is sought and under which conditions. If T00 is wrong, later requirements/knowledge/tests can optimize the wrong target.
- action: created C03_TASK_GRAPH_V01.md with only T00 in detailed form rather than generating the entire task inventory at once.
- T00_output: versioned Target Context Package containing problem, purpose, stakeholders, observable result, context, constraints, operating envelope, facts, assumptions, open questions, contradictions, initial acceptance criteria, gaps and provenance.
- boundaries: T00 does not design implementation, choose a model/provider, invent missing knowledge or construct later graphs.
- scheme_effect: first input/internal/output flow candidate documented; formal notation choice remains to be reviewed before implementation.
- test_effect: test intent recorded now; full Test Specification will be produced before any T00 implementation.
- downstream_effect: T00 output becomes upstream input for Decision/Requirement derivation, workload/test context, later tasks and impact analysis.
- risk: over-asking for clarification can block autonomous research; under-asking can encode false assumptions. A later C04 decision rule must distinguish CLARIFY vs RESEARCH vs EXPLICIT_ASSUMPTION vs BLOCK.
- next_step: review T00 passport/scheme for completeness, then derive the next task from C00 rather than coding T00.
- priority: P0


## Entry 0016 — ALINA web presence, 3D avatar and extreme-collapse requirement

- operation: UI_REQUIREMENT_CAPTURE
- target: ALINA Control Center
- trigger: visual references define ALINA as a luminous synthetic female avatar/3D projection and require the Knowledge Base to be available immediately through a polished website with extreme progressive collapse.
- objective: capture the visual/interaction intent now without violating the analysis-first rule by prematurely coding the site.
- decision: ALINA Control Center is a projection over canonical FATHER Knowledge Core, not a separate truth store. ALINA has a replaceable 3D visual-presence component and progressive disclosure from full workspace to minimal live indicator.
- reference_effect: supplied images are treated as visual-language references, not evidence of biometric/AI-scanner capabilities.
- collapse_rule: presentation may collapse aggressively while analytical/task/provenance state remains recoverable.
- resilience_rule: 3D rendering must never be required for analytical correctness; fallback/reduced-motion/lightweight modes are mandatory design considerations.
- knowledge_ui_effect: site must expose navigable Knowledge/Evidence/Source/Decision/Task/Competency/Learning/Regulatory/Impact projections and reverse trace where data exists.
- next_artifact: before website code, create ALINA Control Center analytical passport, then notation/screen-state scheme, then test specification, then implementation.
- priority: P0


## Entry 0017 — Control Center spatial model: ALINA behind central work table

- operation: CONTROL_CENTER_PASSPORT
- trigger: new visual reference and user direction establish the spatial metaphor: central work table, ALINA behind it, deployable boards around it, secondary folders/settings/domains on side planes.
- objective: convert the visual idea into an analytical UI passport before formal notation or code.
- decision: center is task workspace, not default dashboard; ALINA is visible operator/presence behind it; task-relevant information is brought to deployable boards; side domains remain reachable but visually de-emphasized until promoted by task context.
- candidate_side_domains: Knowledge Base, Sources/Library, Projects, Specialists/Agent Zoo, Training, Experiments/Polygon, Metrics, Dashboards, History, Gaps/Research Orders, Notifications, Settings, System Health/Audit.
- important_limit: candidate groups are not frozen navigation; Task Graph and usability tests may regroup them.
- context_rule: selecting side information should normally bring it into the current workspace instead of forcing navigation away from the active task.
- dashboard_rule: metrics/dashboards are secondary by default and become central only for a metrics/health/experiment task.
- state_rule: open/pinned boards, active object/task, collapse level and relevant context must be representable/restorable.
- next_gate: derive formal spatial/screen-state notation from the passport, then write tests, then implement.
- priority: P0


## Entry 0018 — Website technical brief: movable/collapsible ALINA avatar

- operation: WEBSITE_TZ_BASELINE
- trigger: user requires ALINA avatar to be movable to screen corners/docks or collapsed as far as eyes, and all visual concepts to enter the website project as a technical specification with visualization.
- objective: preserve the design intent as implementable requirements before notation/tests/code.
- action: created ALINA_CONTROL_CENTER_TECHNICAL_BRIEF_V01.md.
- avatar_requirement: position modes include center-rear, four corners, side docks and candidate constrained floating placement; visibility modes include full 3D, compact, face, eyes, minimal status and hidden-with-status.
- workspace_requirement: ALINA must move away from task-critical information; collapse/movement must preserve recoverable work context.
- visual_basis: user-supplied references are recorded as design direction only; future assets must be original and must not present decorative scanner telemetry as real capability.
- project_effect: technical brief, component passports, formal notation, wireframes, state specs, tests, performance/accessibility/fallback tests and A/B plan become required website artifacts before production implementation.
- next_gate: spatial/screen-state notation plus low-fidelity wireframes.
- priority: P0


## Entry 0019 — Correct avatar model: embodied 3D analyst in front of screens

- operation: VISUAL_MODEL_CORRECTION
- trigger: first visualization incorrectly made ALINA read as central screen content.
- correction: ALINA is an independent full-bodied volumetric avatar/analyst in front of information screens and behind/near the central work table, creating a face-to-face human-analyst interaction metaphor.
- component_boundary: avatar/presence layer is separate from information-display layer.
- depth_order: background screens -> volumetric ALINA -> work table -> user viewpoint.
- failure_condition: any design that embeds ALINA as a portrait/background inside a monitor fails the intended interaction model.
- downstream_effect: spatial notation, wireframes, avatar movement/state tests and future concept art must use the corrected depth model.
- priority: P0


## Entry 0020 — Agents represented as layered intelligence stacks

- operation: AGENT_LAYER_VISUALIZATION_REQUIREMENT
- trigger: user supplied stacked intelligence/process references and proposed presenting agent information by layers.
- objective: make an agent's internal foundation understandable at a glance while retaining drill-down to canonical objects.
- decision: add a vertical layered Agent Stack projection. Candidate baseline runs from runtime/input/evidence/knowledge/competence/methods/actions/decisions to outcomes, but layer count and specialization remain configurable by Factory evidence.
- anti-pattern: do not freeze a decorative universal nine-layer taxonomy merely because the reference image uses a stack.
- traceability_rule: each layer is a projection of canonical tasks/decisions/competencies/knowledge/evidence/components/tests, with IDs/versions/status and reverse trace.
- interaction_rule: whole-stack view, layer expand/isolate, compact collapse, exploded graph/pipeline view, and context-valid same-layer comparison across agents.
- next_gate: include Agent Stack in spatial notation and later test whether the layer model improves navigation/comprehension without hiding cross-layer relations.
- priority: P1


## Entry 0021 — Control Center concepts accepted into active development

- operation: UI_BACKLOG_ACTIVATION
- trigger: user approved the accumulated Control Center, embodied ALINA and Agent Stack concepts and requested they be entered into the project and development.
- action: updated Technical Brief with accepted concept baseline and maturity pipeline; created ALINA_CONTROL_CENTER_DEVELOPMENT_BACKLOG_V01.md.
- development_rule: accepted means scheduled for governed development, not permission to skip notation/tests and immediately code.
- active_items: UI-001 spatial notation; UI-002 avatar state/movement; UI-003 work table/boards; UI-004 Agent Stack; UI-005 Knowledge/provenance flow; UI-006 wireframes; UI-007 tests; UI-008 workload/accessibility/fallback; UI-009 A/B plan; UI-010 implementation plan blocked behind prior gates.
- immediate_next: UI-001 + UI-002 notation, because room geometry and avatar movement/collapse are coupled.
- expected_reuse: these artifacts become part of the future FATHER UI development template.
- priority: P0


## Entry 0022 — UI-001 spatial notation drafted

- operation: UI_SPATIAL_NOTATION
- target: ALINA Control Center
- trigger: approved step-by-step progression from passport to notation.
- objective: formalize room depth, zones, object movement and context invariants before avatar state details or code.
- artifact: UI_001_SPATIAL_NOTATION_V01.md.
- key_model: Z4 back information field; Z3 ALINA presence; Z2 deployable boards; Z1 central work table; Z0 user viewpoint/input.
- invariant: ALINA is an independent volumetric presence, never semantically embedded in a monitor; UI movement moves projections, not canonical data.
- interaction_model: side domain -> object reference -> board -> optional promotion to work table -> provenance/impact trace.
- context_rule: collapse/movement preserves active task/object/provenance and does not terminate analytical work.
- degraded_rule: 3D fallback is independent from Knowledge Core availability.
- backlog_effect: UI-001 advanced from PASSPORTED to NOTATION_DRAFT; production implementation remains blocked.
- next_step: review UI-001 invariants, then draft UI-002 Avatar State Machine.
- priority: P0


## Entry 0023 — UI-002 ALINA Avatar State Machine drafted

- operation: AVATAR_STATE_MACHINE_NOTATION
- target: ALINA Control Center
- trigger: UI-001 established room geometry and avatar independence; next required step is formal avatar behavior.
- objective: prevent visual presence, location, analytical state and rendering capability from becoming one opaque UI state.
- decision: model avatar state as orthogonal dimensions PRESENCE × POSITION × ANALYTICAL_STATE × INTERACTION_STATE × RENDER_MODE.
- presence: FULL_3D -> COMPACT_3D -> FACE -> EYES -> STATUS -> HIDDEN.
- position: center-rear, four corners, side docks, candidate constrained floating.
- analytical_states: idle/listening/analyzing/researching/waiting/gap/testing/warning/complete/degraded/error, sourced from real runtime state.
- render_fallback: full -> light 3D -> 2D -> static -> status -> no avatar, without changing Knowledge Core truth/task state.
- invariants: collapse does not stop work; movement does not move data; fallback does not alter truth; avatar failure cannot block core workspace; automatic layout changes remain recoverable.
- backlog_effect: UI-002 advanced to NOTATION_DRAFT; implementation remains blocked.
- next_step: UI-003 Work Table + Deployable Board state model.
- priority: P0


## Entry 0024 — Product split: pleasant MVP now, ALINA super-project long term

- operation: DELIVERY_HORIZON_DECISION
- trigger: user clarified that the immediate site is an MVP/beautiful shell optimized for comfortable daily work, while ALINA herself is a super-project developed deeply over time; future FATHER employees are expected to gain avatars too.
- decision: separate delivery into Horizon A Beautiful Working MVP and Horizon B ALINA Super-Project.
- MVP_goal: visually strong, convenient, pleasant working environment with central table, ALINA presence, navigation shells and a small real vertical slice; do not wait for every deep ALINA engine before obtaining a useful workspace.
- architecture_rule: MVP components remain replaceable and must not block the full architecture.
- UX_rule: comfort, clarity, low friction and aesthetic quality are explicit acceptance concerns, later validated by usability tests rather than subjective decoration alone.
- future_rule: ALINA avatar becomes reference implementation for a reusable FATHER Employee Avatar System shared by future specialists/agents.
- anti_overbuild: do not require full 3D/agent intelligence/metrics/training implementation merely to release the MVP shell; placeholders/demo states must be explicitly identified.
- downstream_effect: backlog and tests must distinguish MVP acceptance from super-project acceptance.
- next_step: before continuing UI-003 detail, define MVP scope/vertical slice so the website can become usable without coupling its release to the full ALINA roadmap.
- priority: P0


## Entry 0025 — MVP-00 Control Center scope frozen as baseline

- operation: MVP_SCOPE_BASELINE
- trigger: product split requires a precise boundary between a beautiful usable shell and the long-horizon ALINA super-project.
- objective: prevent both overbuilding and a fake demo-only MVP.
- action: created MVP_00_CONTROL_CENTER_SCOPE_V01.md and bound the UI backlog to it.
- must_work: command-room shell; ALINA presence/move/collapse/fallback; central Work Table; limited deployable boards; one real canonical Source->Knowledge->Evidence/Provenance vertical slice; knowledge navigation; one structured Agent Stack; workspace-state restoration; truthful real/demo/unavailable status.
- may_demo: Training, advanced Metrics/Dashboards, full Polygon/Zoo/Time Machine/Impact, rich gestures/voice/advanced 3D, provided they are explicitly marked.
- out_of_mvp: full Specialist Factory and deep ALINA engines/orchestration/evolution do not block shell release.
- UX_goal: pleasant low-friction long-session workspace is an explicit acceptance concern.
- anti_fake_rule: MVP must contain at least one narrow real end-to-end data path and cannot consist solely of mock screens.
- next_step: UI-003 Work Table + Board model constrained to MVP scope.
- priority: P0


## Entry 0026 — UI-003 Work Table and Board model drafted

- operation: WORKSPACE_INTERACTION_NOTATION
- target: Beautiful Working MVP
- trigger: MVP-00 fixed the real vertical slice; next step is to define the daily interaction grammar before wireframes/code.
- objective: make the central table the single primary context and use Boards as traceable related projections without page-hopping or data duplication.
- decision: MVP has one PRIMARY_CONTEXT; Boards carry object_ref/origin/relation/status and move through OPEN/PINNED/MINIMIZED/PRIMARY/CLOSED states.
- navigation_rule: promoting a Board preserves previous primary context for deterministic return; incompatible pinned boards become stale/context-changed rather than silently reinterpreted.
- truth_rule: every Board declares REAL/DEMO/PLANNED/UNAVAILABLE.
- vertical_slice: Document/Source -> Knowledge Board -> Evidence Board -> Source/Version -> promote/inspect -> return to prior context.
- agent_integration: Agent Stack and Agent Layer use the same Board grammar, avoiding a special parallel UI architecture.
- cognitive_load_rule: exact simultaneous visible-board count is deferred to usability testing; do not hard-code a visually impressive but unusable wall of panels.
- backlog_effect: UI-003 advanced to NOTATION_DRAFT; implementation remains blocked.
- next_step: UI-004 Agent Stack/layer contract.
- priority: P0


## Entry 0027 — UI-004 layered Agent Stack drafted

- operation: AGENT_STACK_NOTATION
- trigger: UI-003 established a universal Board/Work Table grammar; next step is to make agents understandable without creating a separate UI architecture.
- objective: represent each FATHER employee/agent as a layered, inspectable, evidence-linked specialist rather than a black box or decorative avatar.
- decision: baseline L0-L8 stack = Runtime; Input/Context; Evidence; Knowledge; Competencies/Tasks; Methods/Tools; Actions/Workflows; Decisions/Reasoning; Outcomes.
- architecture_rule: Stack is a projection of Agent Foundation canonical objects, not a second source of truth.
- interaction_rule: Stack -> Layer -> Board -> Work Table -> Evidence/Source, reusing UI-003.
- identity_rule: Avatar answers who is present; Stack answers what supports specialist capability. They share specialist_id but remain replaceable independent components.
- transparency_rule: no magical intelligence score; show typed evidence/currentness/validation/gap/test/runtime states and UNKNOWN when appropriate.
- privacy_reasoning_rule: active-work visualization may show task/runtime events and object traces, not hidden chain-of-thought.
- MVP_rule: ALINA reference stack needs only a small structured real subset plus explicit DEMO/PLANNED layers; full L0-L8 engines do not block MVP.
- future_reuse: same contract supports Lawyer, InfoSec, Architect, Programmer, OSINT, Researcher and other FATHER employees.
- next_step: UI-005 Knowledge/Evidence/Provenance navigation contract.
- priority: P0


## Entry 0028 — UI-005 Knowledge/Evidence/Provenance navigation drafted

- operation: PROVENANCE_NAVIGATION_NOTATION
- trigger: UI-004 made specialists inspectable by layers; next requirement is a deterministic trust path from visible result back to canonical evidence/source.
- objective: let the user inspect why a result/knowledge object exists without leaving the Control Center or losing active context.
- canonical_trace: Original Source -> Document -> Version -> Fragment -> Evidence -> Knowledge -> Relation/Decision -> Output; reverse inspection follows the same lineage backward.
- semantic_rule: FACT/CLAIM/INFERENCE/HYPOTHESIS/REQUIREMENT/DECISION remain distinct in UI.
- currentness_rule: evidence strength and currentness are separate; no combined magical trust score.
- contradiction_rule: conflicting evidence branches remain visible; UI does not resolve them for visual cleanliness.
- gap_rule: missing evidence becomes explicit GAP/RESEARCH state, never fabricated provenance.
- version_rule: historical knowledge remains linked to its actual document version; newer versions trigger impact/currentness paths rather than silent relinking.
- UX_rule: progressive disclosure keeps provenance compact during ordinary work and expands exact fragment/version/source on demand.
- MVP_gate: at least one real canonical Source/Version/Fragment/Evidence/Knowledge chain must support reverse navigation and context return.
- backlog_effect: UI-005 advanced to NOTATION_DRAFT.
- next_step: UI-006 low-fidelity end-to-end MVP wireframes.
- priority: P0


## Entry 0029 — UI-006 first end-to-end MVP wireframes drafted

- operation: MVP_WIREFRAME_COMPOSITION
- trigger: UI-001..UI-005 now define room, avatar, workspace objects, Agent Stack and provenance navigation; first complete user-facing composition is required before tests/code.
- objective: test information hierarchy and daily-work comfort conceptually before visual polish.
- screens: A default/welcome; B document/knowledge work; C provenance drill-down; D Agent Stack; E long-session focus; F minimal/avatar-hidden; G future team-presence concept.
- primary_rule: Work Table dominates ordinary work; task boards are secondary; ALINA remains present but must not obstruct; provenance/status is progressively disclosed.
- comfort_rule: Focus Mode deliberately removes visual noise for long reading/coding/analysis sessions.
- future_team_rule: additional employee avatars appear on demand because a task needs them, not as a permanent crowd.
- degradation_rule: workspace remains usable with avatar hidden/unavailable.
- visual_rule: dark technical room, restrained luminous geometry, readability above glow; no game-HUD wall of panels.
- backlog_effect: UI-006 advanced to WIREFRAME_DRAFT; production code remains blocked.
- next_step: UI-007 Pre-Implementation Test Specification.
- priority: P0


## Entry 0030 — UI-007 pre-implementation test specification drafted

- operation: PRE_IMPLEMENTATION_TEST_DESIGN
- trigger: UI-006 produced the first complete MVP wireframe; FATHER analysis-first rule requires tests before production implementation.
- objective: convert visual/interaction intentions into observable acceptance behavior and prevent implementation from being judged only by appearance.
- artifact: UI_007_PRE_IMPLEMENTATION_TEST_SPEC_V01.md.
- coverage: 23 tests spanning entry, real canonical object, board lifecycle, deterministic return, provenance, missing/contradictory evidence, REAL/DEMO boundary, avatar collapse/reposition/failure, reduced motion, workspace restore, Agent Stack drill-down, Focus Mode, overload, backend outage, source-version change, avatar independence, accessibility, golden path, pleasant-work pilot and performance contexts.
- metric_rule: no metric is comparable outside a declared TEST_CONTEXT; performance thresholds remain unset until target environments are identified.
- human_factor_rule: pleasantness is tested through representative work and observations, not a fabricated universal score.
- release_rule: P0 test specifications + real vertical-slice data contract + explicit demo contract + representative environment profiles are required before implementation-ready status.
- backlog_effect: UI-007 advanced to TEST_SPEC_DRAFT; implementation remains blocked.
- next_step: UI-008 workload/performance/accessibility profiles and representative target environments; locate/define the real vertical-slice data contract.
- priority: P0


## Entry 0031 — UI-008 workload/performance/accessibility profiles drafted

- operation: TEST_CONTEXT_PROFILE_DESIGN
- trigger: UI-007 requires valid operating contexts before performance/usability metrics can be interpreted.
- objective: define desktop-first viewport, workload, render, accessibility, long-session and failure contexts without inventing benchmark thresholds.
- target: sustained desktop analytical work; mobile full-workspace support is not release-blocking for MVP.
- workload_profiles: idle, document focus, normal analysis, provenance trace, Agent Stack inspection, busy workspace, degraded render, degraded backend, restore.
- render_rule: rich 3D is optional enhancement; analytical work must survive LIGHT/2D/STATUS_ONLY paths.
- accessibility: reduced motion, keyboard-oriented operation, low visual effects, color-independent status, avatar-off mode.
- performance_rule: capture latency/render/resource/restore/long-session metrics under TEST_CONTEXT; thresholds wait for actual prototype and representative hardware.
- hardware_rule: do not optimize only for high-end GPU; record actual development workstation and at least one lower-capability/degraded profile.
- comparison_rule: A/B comparisons require comparable workload, viewport, render/data/backend context and metric definitions.
- backlog_effect: UI-008 advanced to PROFILE_DRAFT.
- next_step: UI-009 A/B experiment hypotheses; identify real vertical-slice data contract before UI-010 implementation plan.
- priority: P0


## Entry 0032 — UI-009 A/B experiment plan drafted

- operation: UX_EXPERIMENT_DESIGN
- trigger: UI-008 defined valid contexts; uncertain visual/interaction choices should now become testable hypotheses instead of permanent taste-based decisions.
- objective: preserve replaceability and learn which UI variants improve comfortable analytical work.
- experiments: default ALINA presence; default position; board density; provenance disclosure; Agent Stack form; Focus Mode presence; visual intensity; board placement; Back model; future specialist presence.
- experiment_contract: HYPOTHESIS -> VARIANTS -> TEST_CONTEXT -> TASK -> METRICS/OBSERVATIONS -> GUARDRAILS -> RESULT -> DECISION.
- guardrail: local visual improvement cannot be promoted if readability, truth/status clarity, accessibility, provenance reachability or downstream task performance regress.
- MVP_rule: implement configuration hooks, not a full experimentation platform.
- evidence_rule: single-user repeated trials are exploratory evidence and must not be presented as population-level proof.
- backlog_effect: UI-009 advanced to EXPERIMENT_PLAN_DRAFT.
- next_step: UI-010 Implementation Plan, with production code still gated on the real Source/Version/Fragment/Evidence/Knowledge data contract.
- priority: P0


## Entry 0033 — UI-010 MVP implementation plan drafted

- operation: IMPLEMENTATION_PLANNING
- trigger: UI-001..009 now cover spatial model, avatar, workspace, Agent Stack, provenance, wireframes, tests, workload contexts and experiment hooks.
- objective: convert design artifacts into an incremental engineering plan without prematurely implementing the full ALINA super-project.
- architecture: ControlCenterShell + AlinaPresence + WorkTable + BoardManager + AgentStack + ProvenanceNavigator + FocusMode + WorkspaceStateController + StatusTruthBadge.
- state_rule: canonical references are separated from presentation/layout state; workspace restoration must not create a copied source of truth.
- data_boundary: frontend consumes a stable adapter/service contract; exact REST/FastAPI/other transport follows repository reconnaissance.
- phases: reconnaissance -> runnable shell -> workspace state -> ALINA presentation -> real Knowledge vertical slice -> provenance -> Agent Stack -> restore/degraded -> polish -> tests/evidence.
- milestones: M1 runnable visual/interaction scaffolding with explicit DEMO/PLANNED; M2 completion candidate adds real vertical slice, provenance, real Agent layer, restore/fallback and P0 test evidence.
- blockers: repository structure not inspected; real Knowledge schema/API unconfirmed; target workstation context not recorded; draft artifacts need review for P0 contradictions.
- anti_overbuild: rich 3D and new frameworks are not prerequisites; use simplest replaceable implementation that proves the interaction.
- next_step: repository reconnaissance and exact M1 file/change plan before first production component.
- priority: P0


## Entry 0034 — ENG-001 repository reconnaissance completed

- operation: REPOSITORY_RECONNAISSANCE
- trigger: UI-010 requires inspection of actual repository structure before production components are created.
- inspected: current branch recursive tree + repository README.
- finding: repository is currently Python automation/control + registries/reports/tests + Knowledge Core/ALINA design documentation; no existing web frontend, package manifest, browser routes/components, web API service or confirmed PostgreSQL Knowledge Core runtime schema was found.
- consequence: there is no frontend framework to preserve; M1 needs a new explicit application boundary.
- proposed_boundary: apps/alina-control-center/{frontend,contracts,fixtures,tests}; backend/database ownership intentionally deferred.
- reusable_assets: Knowledge standards/contracts, ALINA UI specs, registry evidence principles, CI/test discipline; operational registries are not canonical Knowledge Core.
- blocker_update: B1 RESOLVED; B2 remains OPEN P0 for M2; B3 remains OPEN for benchmark baseline; B4 remains review work but no discovered P0 contradiction blocks safe M1 scaffolding.
- framework_candidate: TypeScript + React + Vite, subject to FATHER Design Decision; rich 3D deferred behind adapter.
- security_rule: public repo receives sanitized contracts/fixtures only; no local paths, secrets, private documents, personal data or production dumps.
- next_step: FDR frontend/framework choice + M1 component/contract passport + pre-code tests, then scaffold runnable M1.
- priority: P0


## Entry 0035 — M1 implementation gate completed before code

- operation: DESIGN_DECISION_AND_PRECODE_GATE
- trigger: ENG-001 resolved repository structure and showed no existing frontend stack.
- decision: FDR-UI-001 accepts TypeScript + React + Vite for M1 only; final 3D engine, backend, database, state library and design system remain undecided.
- rationale: small explicit component boundary, typed contracts, rapid desktop MVP iteration, future renderer adapter; avoid unnecessary full-stack framework commitment.
- passport: M1-CP-001 defines Control Center Shell responsibility, inputs/outputs, contracts, failure behavior, security and replaceability.
- tests_before_code: M1-TEST-001 defines T01-T10 startup, truth status, board lifecycle, focus, avatar collapse/fallback, restore, reduced motion, invalid fixture and public-fixture hygiene.
- architecture_rule: canonical object references remain separate from presentation state; DEMO never silently becomes REAL.
- implementation_gate: PASSED_FOR_SCAFFOLDING; validation remains pending until tests are implemented/executed.
- next_step: create framework-independent JSON contracts + sanitized demo fixture, then scaffold React/Vite M1 and implement T01-T10.
- priority: P0


## Entry 0036 — M1 framework-independent contracts and sanitized fixture created

- operation: CONTRACT_FIRST_SCAFFOLDING
- trigger: Entry 0035 passed the pre-code design gate and required contracts/fixture before React implementation.
- artifacts: apps/alina-control-center boundary; FatherObject JSON Schema; BoardState JSON Schema; WorkspaceState JSON Schema; DemoWorkspace aggregate schema; sanitized demo-workspace fixture; app README.
- contract_rule: canonical object identity/status/provenance references remain distinct from WorkspaceState presentation data.
- truth_rule: fixture root is DEMO; objects independently carry DEMO/PLANNED status; no object is marked REAL.
- security_check_by_design: fixture contains no personal data, secrets, private documents or absolute local paths.
- implementation_effect: frontend can now consume framework-independent contracts without inventing a Knowledge Core schema.
- limitation: JSON Schema validation has not yet been executed in CI; references/contract behavior remain to be covered by M1 executable tests.
- next_step: create React/Vite M1 scaffold and implement the first executable tests against these contracts/fixture.
- priority: P0


## Entry 0037 — First executable React/Vite M1 scaffold created

- operation: FIRST_EXECUTABLE_FRONTEND_SCAFFOLD
- trigger: contract-first artifacts and pre-code T01-T10 specification were completed in Entry 0036/0035.
- implementation: created TypeScript + React + Vite frontend under apps/alina-control-center/frontend.
- implemented_components: Control Center shell composition; side domain rails; Work Table; lightweight replaceable ALINA 2D presence; Knowledge board; truth-status badges; Focus Mode; ALINA presence cycling; reduced-motion CSS baseline.
- data_source: sanitized in-code DEMO workspace mirrors the framework-independent fixture; Knowledge Core explicitly NOT CONNECTED.
- truth_behavior: DEMO and PLANNED labels are visible; no fixture object is presented as REAL.
- visual_rule: dark technical command-room baseline with restrained luminous geometry; this is M1 scaffolding, not final visual design.
- tests_created: executable Vitest/Testing Library coverage for T01 startup, T02 truth visibility, T03 board close/reopen, T04 Focus toggle, T05 ALINA presence transition.
- tests_not_yet_executed: dependencies have not been installed/run by GitHub connector; T06-T10 remain to implement.
- known_gap: demo data is currently duplicated between JSON fixture and TypeScript module; next refactor should consume/validate one canonical fixture source to prevent drift.
- known_gap: WorkspaceState is not yet serialized/restored; board lifecycle is only partial; avatar failure injection not yet implemented.
- security: no secrets, private documents, personal data or local absolute paths added.
- next_step: remove fixture duplication, implement T06-T10 + state restore/fallback, add CI/frontend validation, then execute build/tests on a runtime.
- priority: P0


## Entry 0038 — M1 duplicate fixture gap removed; T06-T10 implementation completed

- operation: GAP_REPAIR_AND_TEST_COMPLETION
- trigger: Entry 0037 identified duplicated DEMO data and missing T06-T10/state restore/fallback behavior.
- gap_repair: demoData.ts no longer contains a second copy of the fixture; it is now a typed adapter over apps/alina-control-center/fixtures/demo-workspace.json.
- state_change: added workspaceState.ts with versioned local-storage key, safe defaults, serialization and corrupt-state fallback. Persisted data contains presentation state only, not canonical FATHER object copies.
- avatar_failure_behavior: App accepts renderer availability; renderer failure degrades to STATUS ONLY while Work Table remains usable.
- invalid_state_behavior: corrupt persisted state falls back to safe default instead of inventing workspace truth.
- tests_added_or_extended: T06 avatar renderer failure; T07 presentation restore/no canonical duplication; T08 reduced-motion contract; T09 corrupt-state fallback; T10 public-fixture hygiene. T01-T05 retained.
- security_test: fixture test rejects obvious absolute Windows paths, secret-like fields and selected PII-like fields.
- expected_effect: all M1 T01-T10 now have executable test representations.
- limitation: tests/build still have NOT been executed in a Node runtime; code presence is not test evidence.
- remaining_gap: JSON Schema validation is not yet executable in the frontend test suite; schema/fixture conformance should be added before calling contracts validated.
- remaining_gap: T09 currently validates corrupt persisted state, while malformed aggregate fixture injection still needs a dedicated adapter-level test if required by the original wording.
- next_step: add schema validation/CI and execute npm install + build + test on an actual runtime; record exact versions, failures, timings and fixes.
- priority: P0


## Entry 0039 — Contract validation and M1 CI added; lockfile assumption corrected

- operation: VALIDATION_AUTOMATION_PREPARATION
- trigger: Entry 0038 left JSON Schema conformance and actual runtime execution as open P0 gaps.
- package_change: frontend dependencies normalized; React remains runtime dependency; Vite/plugin/TypeScript/test tooling moved to devDependencies; Ajv added for executable JSON Schema checks.
- test_runtime: Vitest configured for jsdom with jest-dom setup.
- contract_validation: schemaValidation.test.ts validates every FatherObject, BoardState and WorkspaceState from the canonical sanitized fixture and asserts that the aggregate fixture is DEMO with no REAL object.
- ci_added: .github/workflows/alina-control-center-m1.yml runs install -> test -> build on Node 22 for relevant branch/path changes.
- error_caught_during_action: initial CI draft used npm ci + npm cache while no package-lock.json exists yet. This would make the first workflow invalid.
- correction: workflow immediately changed to npm install and cache assumption removed until a lockfile is generated and committed from a real runtime.
- lesson: CI prerequisites are themselves contracts; do not assume generated artifacts exist.
- evidence_status: CI definition exists, but no successful workflow run is claimed yet. Build/tests remain UNVERIFIED until GitHub Actions or local runtime returns results.
- next_step: inspect workflow run triggered by these commits; if no run exists or it fails, obtain logs, classify GAP, fix and rerun. After first successful install generate/commit lockfile and switch CI to npm ci for reproducibility.
- priority: P0


## Entry 0040 — First M1 CI failure diagnosed and repaired

- operation: CI_FAILURE_ANALYSIS_AND_REPAIR
- evidence: GitHub Actions run 35851126862 completed FAILURE; Install succeeded; Test failed; Build was skipped.
- observed_failure_1: React Testing Library DOM was not cleaned between tests, causing repeated mounted apps and ambiguous queries such as multiple Focus Mode / ALINA buttons / WORK TABLE nodes.
- repair_1: testSetup.ts now runs cleanup() after each test.
- observed_failure_2: default Ajv instance did not include JSON Schema draft 2020-12 meta-schema; FatherObject/BoardState/WorkspaceState compilation failed with 'no schema with key or ref https://json-schema.org/draft/2020-12/schema'.
- repair_2: schema tests now use Ajv2020 from ajv/dist/2020.
- observed_failure_3: Vite ?raw CSS import returned an empty value in this Vitest context, so T08 could not prove reduced-motion source presence.
- repair_3: T08 now reads styles.css directly through node:fs/fileURLToPath; @types/node added for TypeScript build compatibility.
- runner_observation: GitHub emitted a warning that actions/checkout@v4 and setup-node@v4 target deprecated Node 20 internally and are forced to Node 24 by the runner. The job's configured application Node remains a separate concern. This warning is recorded but is not the test failure cause.
- causality: three independent test-infrastructure defects prevented product tests from completing; no evidence yet indicates the Control Center UI itself failed its intended interaction contract.
- validation_status: REPAIR_COMMITTED, RETEST_REQUIRED. No GREEN claim until a new workflow run succeeds.
- next_step: inspect the workflow run triggered by these repairs; if failure persists, fetch exact logs and repeat GAP -> FIX -> RETEST.
- priority: P0


## Entry 0041 — Second M1 CI narrowed to one failing accessibility test

- operation: CI_RETEST_ANALYSIS_AND_TARGETED_REPAIR
- evidence: GitHub Actions run 35852539550 completed FAILURE after Entry 0040 repairs.
- positive_evidence: npm install succeeded; 3 of 4 test files passed; 13 of 14 tests passed; fixture hygiene passed; all 4 JSON Schema conformance tests passed; all 8 App/state tests passed.
- remaining_failure: only T08 reduced-motion source test failed with ERR_INVALID_URL_SCHEME because import.meta.url was transformed by the Vitest/Vite runtime and was not a file: URL. This is a test-path implementation defect, not evidence that reduced-motion CSS is absent.
- repair: reducedMotion.test.ts now resolves src/styles.css from process.cwd(), which is fixed by CI working-directory to apps/alina-control-center/frontend.
- measured_test_run: 14 total tests; 13 passed; 1 failed; Vitest duration 2.49 s. These values describe run 35852539550 only.
- dependency_observation: npm installed 112 packages, audited 113, reported 0 vulnerabilities in that run.
- validation_status: NEAR_GREEN, RETEST_REQUIRED. Build remains unexecuted because the failing test stopped the job.
- next_step: inspect new CI run; if tests pass, analyze TypeScript/Vite build independently and fix any build-only gaps before M1 baseline release.
- priority: P0


## Entry 0042 — All M1 tests GREEN; first build-only gaps identified and repaired

- operation: TEST_GATE_PASSED_BUILD_GATE_REPAIR
- evidence: GitHub Actions run 35853497939.
- test_result: 4/4 test files passed; 14/14 tests passed; Vitest duration 2.62 s.
- contract_result: JSON Schema conformance, fixture hygiene, UI/state behavior and reduced-motion source checks all passed in this run.
- build_result: FAILED during tsc -b before Vite bundling.
- build_gap_1: TS2882 for side-effect import ./styles.css because Vite client module declarations were absent.
- repair_1: added src/vite-env.d.ts referencing vite/client.
- build_gap_2: node:fs, node:path and process were unresolved because @types/node was installed but tsconfig.app.json restricted types to vitest/globals only.
- repair_2: added node to compilerOptions.types.
- interpretation: test gate is now evidenced GREEN for run 35853497939; M1 release gate remains blocked until build is GREEN.
- telemetry: npm install 112 packages / audit 113 / 0 vulnerabilities; tests 14/14 PASS; test duration 2.62 s. Values are specific to this CI run.
- next_step: retest CI and inspect build; if Vite bundling succeeds, capture output/bundle metrics and establish first M1 runnable baseline. If not, classify next build GAP and continue.
- priority: P0


## Entry 0043 — First Runnable M1 Baseline validated GREEN

- operation: M1_BASELINE_VALIDATION
- evidence: GitHub Actions run 35853674078 completed SUCCESS.
- environment: application test/build runtime Node v22.23.2, npm 10.9.8; GitHub runner also emitted separate deprecation warnings for Node 20-targeting action internals.
- install: PASS; 112 packages added, 113 audited, 0 vulnerabilities reported by npm in this run.
- tests: PASS; 4/4 test files, 14/14 tests, Vitest duration 2.69 s.
- build: PASS; tsc -b and Vite production build succeeded.
- build_output: Vite 8.3.0; 19 modules transformed; dist/index.html 0.41 kB / gzip 0.30 kB; CSS 2.76 kB / gzip 1.18 kB; JS 225.00 kB / gzip 70.73 kB; Vite build phase 165 ms.
- release_interpretation: first technically runnable and CI-validated M1 baseline established for the DEMO-only ALINA Control Center shell.
- explicitly_not_claimed: no real Knowledge Core backend, no production deployment, no final 3D avatar, no M2 vertical slice, no user usability validation, no workstation benchmark.
- process_evidence: the M1 loop produced failures, classified gaps, committed repairs, reran validation and reached GREEN without suppressing failed history.
- next_phase: VISUAL_AND_INTERACTION_REVIEW of the runnable baseline, then lockfile/reproducibility hardening and M2 real Knowledge vertical-slice preparation under the same passport -> notation -> tests -> implementation rule.
- priority: P0 COMPLETE for M1 runnable baseline; visual review remains P1 and M2 remains P0 next milestone.
