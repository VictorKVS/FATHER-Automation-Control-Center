# FATHER Human Agent Studio — Research Synthesis v0.1

Status: RESEARCH BASELINE / PRODUCT DIRECTION
Date: 2026-09-24

## Product decision

Do not build a monolithic avatar editor. Build a reusable Human Agent Studio and a corresponding specialist discipline that can create:
- web interfaces and spatial web experiences;
- parametric digital humans and stylized characters;
- clothing, rigs, animation, facial performance, voice and presence;
- interactive agents and NPCs;
- game-ready characters and scenes;
- later, complete interactive/game experiences including locomotion, physics, VFX and action mechanics.

The current ALINA 3D prototype is the first integration polygon, not a throwaway demo.

## Competitive synthesis

### M3 CharacterStudio
Use as primary open architectural reference for browser character assembly: point-and-click composition, local VRM/textures, color customization, GLB/VRM export, screenshots, programmable animation, avatar optimization, batch export, Three.js/WebGL. Important pattern: program and asset packs are separated.

### MakeHuman / MB-Lab
Use as references for parametric body-generation concepts and Blender/DCC workflow. MakeHuman demonstrates mature separation between application code and graphical assets; asset licensing must be tracked separately. MB-Lab is useful as a Blender-native morphology/skeleton/morph reference, not as a direct web runtime dependency.

### MetaHuman
Use as quality/UX benchmark, not as the canonical FATHER dependency. Key ideas: preset-to-sculpt workflow, parametric body measurements, face/body/hair/clothing/material editing, rig-ready output, animation preview, parametric clothing and DCC round-trip. Keep FATHER formats/provider layer independent.

### VRM ecosystem
Adopt VRM as a primary interoperable humanoid runtime format for the web path, while retaining GLB/glTF support. Use @pixiv/three-vrm behind an adapter, not as domain truth.

### VRoid AI Companion / ReactFiberAvatarTalk / Open VRM Companion / Khavee SDK
Extract patterns: avatar renderer isolation, animation retargeting, viseme/blendshape lip sync, gaze/blink/idle, swappable voice/LLM backends, explicit conversational states, RAG integration. Do not couple the Human Agent model to any one LLM/TTS/STT provider.

### NVIDIA ACE Audio2Face
Use as a future high-quality facial-animation adapter candidate. Its streaming audio-to-blendshape architecture validates separating speech generation from facial animation.

### Godot TPS demos
Use as reference/polygon for later game mechanics: third-person controller, movement, camera, aim/shoot mechanics, effects and game-loop integration. Keep these capabilities downstream from the reusable character/behavior core.

## Chosen architecture

HUMAN AGENT STUDIO
1. Character Definition
   - BodyProfile: stature, proportions, morphology parameters, age presentation, body presets.
   - FaceProfile: morphs/blendshapes, eyes, skin, hair.
   - WardrobeProfile: garment slots, fitting rules, materials, accessories.
2. Rig & Motion
   - HumanoidRigContract.
   - Retargeting.
   - AnimationGraph: idle/listen/think/walk/run/turn/sit/talk/present/react.
   - IK, gaze, hand/foot targets.
3. Face & Speech
   - Expression/FACS-like semantic layer.
   - Viseme layer.
   - blink/gaze/micro-motion.
   - VoiceProfile and replaceable TTS/STT/audio adapters.
4. Personality & Interaction
   - communication style, initiative, formality, warmth, humor and boundaries as behavioral configuration;
   - conversation turn-taking, interruption policy, listening/attention cues;
   - profession-specific interaction overlays.
5. Professional Agent
   - FATHER knowledge/evidence/RAG/skills remain external to the body renderer;
   - HumanAgentProfile binds specialist role to embodiment/presence without making appearance a source of professional truth.
6. Runtime
   - Web runtime: React + Three.js/R3F + VRM/GLB adapters.
   - DCC pipeline: Blender-first open pipeline.
   - Game runtime adapters: Godot and/or Unreal explored after reusable contracts stabilize.
7. Studio
   - character/body editor;
   - face editor;
   - wardrobe/material editor;
   - animation/behavior editor;
   - voice/conversation editor;
   - scene/presence editor;
   - test polygon;
   - export/package manager.

## Canonical package

HumanAgentPackage
- manifest + version;
- CharacterProfile;
- BodyProfile;
- FaceProfile;
- WardrobeProfile;
- RigProfile;
- AnimationProfile;
- VoiceProfile;
- PersonalityProfile;
- InteractionProfile;
- ProfessionBinding;
- AssetManifest with origin/license/hash;
- RuntimeCompatibility;
- TestProfile;
- provenance and change history.

The package references assets; it does not make binary assets canonical knowledge.

## Specialist direction

Create a broad FATHER specialist tentatively named **Interactive 3D / Human Agent & Game Experience Engineer**.

Competency branches:
- frontend/UI/UX and spatial web;
- Three.js/WebGL/WebGPU/R3F;
- 3D math, rendering, materials, lighting and optimization;
- Blender/DCC, modeling, topology, UV, texturing and baking;
- humanoid anatomy/proportion for technical character construction;
- rigging, skinning, morph targets, retargeting, IK/FK;
- animation state machines, procedural animation and motion systems;
- facial animation, visemes, lip sync, gaze and expressive behavior;
- audio/voice integration;
- HCI/conversational embodiment;
- game architecture, scene graphs, input, camera and physics;
- NPC/game AI, navigation and behavior;
- VFX and action mechanics;
- asset pipeline, LOD, compression, export and licensing;
- testing, profiling, accessibility and fallback;
- safety/content controls appropriate to the target application.

This specialist should be capable of both authoring assets/experiences and deciding when an existing engine/library/asset is technically and legally preferable to rebuilding it.

## Knowledge curriculum seeds

Priority references to acquire/read into the Knowledge Core:
- Real-Time Rendering, 4th Edition — rendering foundations and reference bibliography.
- Hands-On C++ Game Animation Programming — animation tracks, skinning, IK, glTF and optimization.
- Mastering C++ Game Animation Programming (2025) — modern character animation, collision/camera, NPC behavior and tooling.
- Game Programming in C++ — graphics, physics, AI, audio, cameras and animation as an integrated game-programming foundation.
- Practical Game AI Programming — animation behavior, navigation, planning, awareness and crowd behavior.
- Current official Three.js/R3F, VRM, Blender, Godot and Unreal/MetaHuman documentation should complement books where APIs evolve faster than print.

## Build-vs-reuse policy

REUSE when:
- a mature engine solves commodity infrastructure better;
- licensing is compatible;
- adapter isolation is possible;
- replacement remains feasible.

BUILD when:
- capability is core FATHER IP;
- existing solutions prevent provider/runtime independence;
- provenance/testing/knowledge integration cannot be achieved cleanly;
- the work is deliberately used as a learning polygon for the specialist.

HYBRID is the default: reuse rendering/physics/DCC primitives while FATHER owns the semantic character package, professional binding, behavior orchestration, evidence-aware agent integration, tests and Studio workflow.

## Product evolution

Phase A — ALINA web embodiment: current P1-P7.
Phase B — reusable HumanAgentPackage + renderer adapters.
Phase C — Character/Voice/Behavior Studio editors.
Phase D — specialist factory knowledge/competency/polygon.
Phase E — scene/gameplay lab: locomotion, interaction, physics, VFX and NPCs.
Phase F — game-production adapter(s), with action systems and richer simulations as downstream modules.

No requirement to implement all game mechanics inside the browser Control Center. The Studio produces portable definitions/assets; specialized runtimes execute them.

## Immediate consequence for ALINA P2

P2 must not hard-code ALINA's body into the Control Center. Introduce AvatarRendererAdapter + HumanAgentProfile boundary first. A temporary licensed/test avatar may be swapped later without changing ALINA knowledge, dialogue, task state or workspace.
