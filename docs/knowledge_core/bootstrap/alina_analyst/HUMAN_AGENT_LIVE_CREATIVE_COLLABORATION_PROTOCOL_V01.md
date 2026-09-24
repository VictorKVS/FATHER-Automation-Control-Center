# FATHER Human Agent — Live Creative Collaboration Protocol v0.1

Status: PRODUCT / INTERACTION BASELINE
Date: 2026-09-24

## Intent

The user should collaborate with the Scenario Writer and Interactive 3D / Human Agent & Game Experience Engineer through natural conversation, not by manually filling large technical forms or authoring production prompts.

The system converts creative intent into structured production actions, prompts, constraints, assets, tests and tool calls. Manual work is minimized; productive creative discussion is maximized.

## Core interaction principle

CONVERSATION FIRST -> STRUCTURE INTERNALLY -> EXECUTE THROUGH TOOLS -> SHOW RESULT -> DISCUSS ONLY WHAT MATTERS.

The user may speak in ordinary language:
- "Make the room darker and more serious."
- "She should walk to the board, pause, look at me and explain the graph."
- "This character feels too robotic."
- "Make this sequence more dynamic."
- "I want a game scene with this character."

The system must translate this into technical production state without requiring the user to know renderer, rig, animation, prompt or engine terminology.

## Collaboration roles

### Scenario Writer
Owns narrative intent:
- scene purpose;
- characters;
- sequence of events;
- dialogue;
- emotional beats;
- environment and staging;
- interaction branches;
- continuity;
- desired audience experience.

### Interactive 3D / Human Agent & Game Experience Engineer
Owns executable realization:
- decomposes scene into shots/actions/states;
- determines required characters/assets/animations/cameras/lights/audio/VFX/interactions;
- generates and refines production prompts;
- chooses reuse/build strategy;
- selects tools/runtime/adapters;
- creates technical constraints;
- validates feasibility;
- runs tests and proposes alternatives;
- returns visible result and only the decisions that require human judgment.

### ALINA / Orchestrator
Maintains task context, provenance, decisions, unresolved questions and artifact graph; routes work between specialists and tools.

## Default conversation loop

USER INTENT
-> Scenario Writer interprets creative meaning
-> Engineer compiles Production Plan internally
-> missing information classified
-> safe/reversible details inferred using project defaults
-> only high-impact ambiguity is asked
-> prompts/actions generated
-> tools execute
-> preview/result shown
-> user reacts naturally
-> delta compiled
-> affected artifacts regenerated only
-> validation
-> next preview

## Question policy

Do NOT interrogate the user for every parameter.

Ask a question only when the answer materially changes:
1. story/meaning;
2. permanent character identity;
3. visual identity that is costly to reverse;
4. legal/license/privacy/safety boundary;
5. target platform/performance class;
6. expensive/irreversible production work;
7. two or more plausible variants would produce substantially different results.

Everything else uses documented defaults and remains editable.

Question depth modes:
- FLOW: default; minimal questions, rapid production.
- DETAIL: temporarily activated for meticulous discussion of one object/scene/behavior.
- LOCK: approved characteristic becomes a versioned constraint until explicitly changed.

After DETAIL, automatically return to FLOW.

## Prompt compilation

Prompts are generated artifacts, not the primary user interface.

Creative Intent
-> Scene Specification
-> Action Timeline
-> Character/Behavior Requirements
-> Asset Requirements
-> Runtime Constraints
-> Tool-specific Prompt/Instruction
-> Generation/Execution
-> Validation
-> Artifact + provenance

Every generated prompt should retain:
- source intent reference;
- target tool/model/runtime;
- version;
- positive constraints;
- negative constraints where relevant;
- dependencies;
- expected output;
- validation rule;
- regeneration history.

## Scenario action representation

Each action should minimally contain:
- actor;
- intent;
- start condition;
- action;
- target;
- spatial anchor;
- timing/beat;
- emotion/interaction state;
- dialogue/audio reference when applicable;
- animation/gesture/gaze requirements;
- camera relevance;
- environment/VFX relevance;
- end condition;
- dependencies;
- fallback;
- validation criteria.

Example:
ALINA / explain evidence / after graph opens / walk-to / EvidenceWall / A4 / pause-before-speech / PRESENTING / dialogue:D17 / look-at-wall->user / medium-shot / panel-glow / explanation-complete / graph-loaded / status-only fallback / reaches anchor and preserves dialogue context.

## Productivity rules

- Prefer editing deltas over regenerating whole scenes.
- Reuse approved CharacterProfile, SceneProfile, WardrobeProfile and animation assets.
- Maintain continuity automatically.
- Cache/reuse tool outputs where license and provenance permit.
- Surface alternatives only when they matter.
- Technical errors are fixed internally when possible.
- User-facing conversation uses creative language; technical trace remains available on demand.
- Every automated assumption is inspectable and reversible.

## Studio consequence

Human Agent Studio needs two simultaneous interfaces:
1. LIVE MODE — conversational co-creation, previews, short decisions.
2. INSPECTOR MODE — exact parameters, graphs, prompts, assets, provenance, versions and tests.

LIVE MODE is the default. INSPECTOR/DETAIL is entered when precision is needed.

## Target UX

The desired experience is not "fill in a character editor" and not "write perfect prompts."

It is:
"I talk to a capable creative/technical specialist. It understands the scenario, asks only important questions, performs the technical work, shows me the result, and we refine it together."

## Acceptance criteria

- A scene can be created from ordinary-language intent without manual prompt engineering.
- Routine technical parameters do not require user confirmation.
- High-impact ambiguity triggers a concise question.
- User can request meticulous DETAIL discussion for any selected element.
- Returning from DETAIL to FLOW preserves all approved constraints.
- User corrections produce delta updates rather than unnecessary full regeneration.
- Generated prompts/actions remain inspectable and versioned.
- Scenario Writer and Engineer responsibilities remain distinguishable.
- Result can be traced from visible artifact back to scenario intent and generated production instructions.
