# UI-006 — ALINA Control Center MVP Low-Fidelity Wireframes v0.1

Status: WIREFRAME_DRAFT
Scope: MVP-00
Upstream: UI-001..UI-005
Implementation: BLOCKED until UI-007 Test Specification

## 1. Purpose

Combine the approved interaction models into one end-to-end user-facing MVP layout before visual polish or production code.

This document defines information hierarchy and interaction placement, not final colors, typography, animation, 3D assets or pixel geometry.

## 2. Screen A — Default / Welcome Workspace

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ FATHER                         CONTROL CENTER                  status / user  │
├──────────────┬───────────────────────────────────────────────┬───────────────┤
│ KNOWLEDGE    │        BACK INFORMATION / CONTEXT FIELD       │ AGENTS        │
│ SOURCES      │                                               │ PROJECTS      │
│ PROJECTS     │              ┌───────────────┐                │ POLYGON*      │
│ RESEARCH*    │              │     ALINA     │                │ METRICS*      │
│              │              │   FULL/FACE   │                │ TRAINING*     │
│              │              └───────────────┘                │ SETTINGS      │
│              │                                               │               │
│              │      [ optional deployable board zone ]       │               │
│              │                                               │               │
│              │        ╔════════════════════════════╗         │               │
│              │        ║       WORK TABLE           ║         │               │
│              │        ║  Select/open active object ║         │               │
│              │        ╚════════════════════════════╝         │               │
├──────────────┴───────────────────────────────────────────────┴───────────────┤
│ current task / provenance hint / REAL|DEMO|PLANNED status                   │
└──────────────────────────────────────────────────────────────────────────────┘

* may be PLANNED/DEMO in MVP.
```

Default rule: the center is intentionally quiet. Do not populate empty space with decorative dashboards.

## 3. Screen B — Real Document / Knowledge Work

```text
┌──────────────┬───────────────────────────────────────────────────────────────┐
│ domains      │                      ALINA [EYES]                             │
│              │                                                               │
│              │ [KNOWLEDGE]                         [EVIDENCE]                 │
│              │  K-17                                 E-4                     │
│              │  relation summary                     support/status           │
│              │       \                               /                        │
│              │        \                             /                         │
│              │         ╔════════════════════════════╗                         │
│              │         ║ WORK TABLE: DOCUMENT DV-3 ║                         │
│              │         ║ title / fragment / context ║                         │
│              │         ║ primary reading/work area  ║                         │
│              │         ╚════════════════════════════╝                         │
│              │                                                               │
│              │ provenance: Document -> Version -> Fragment -> Evidence        │
└──────────────┴───────────────────────────────────────────────────────────────┘
```

When reading/working, ALINA collapses by preference or layout need. The document dominates.

## 4. Screen C — Provenance Drill-Down

```text
                [K-17 KNOWLEDGE]
                       │
                       ▼
                 [E-4 EVIDENCE]
                       │
                       ▼
                [F-22 FRAGMENT]
                       │
                       ▼
              [DV-3 DOC VERSION]
                       │
                       ▼
                [SOURCE OBJECT]

       ╔══════════════════════════════╗
       ║ WORK TABLE retains context   ║
       ║ Back returns exact prior step║
       ╚══════════════════════════════╝
```

Only the currently inspected branch expands. The whole provenance graph is not shown by default.

## 5. Screen D — Agent Stack

```text
┌──────────────────────┐      ┌──────────────────────────────────────────────┐
│ ALINA                │      │ selected layer board                         │
│ ┌──────────────────┐ │      │ L3 KNOWLEDGE                                │
│ │ L8 Outcomes      │ │      │ objects / currentness / gaps                │
│ │ L7 Decisions     │ │ ───► │ evidence links                              │
│ │ L6 Actions       │ │      └──────────────────────────────────────────────┘
│ │ L5 Methods       │ │
│ │ L4 Competencies  │ │             ╔════════════════════════════╗
│ │ L3 Knowledge  ◄──┼─┼────────────►║ WORK TABLE                 ║
│ │ L2 Evidence      │ │             ║ promoted layer/object      ║
│ │ L1 Input         │ │             ╚════════════════════════════╝
│ │ L0 Runtime       │ │
│ └──────────────────┘ │
└──────────────────────┘
```

MVP can show PLANNED layers, but at least one layer path must link to real structured Knowledge/Evidence/Source data.

## 6. Screen E — Focus / Long Session Mode

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ task / object                                               ALINA [EYES]     │
│                                                                              │
│                    ╔════════════════════════════════════╗                    │
│                    ║                                    ║                    │
│                    ║           WORK TABLE               ║                    │
│                    ║      maximum readable space        ║                    │
│                    ║                                    ║                    │
│                    ╚════════════════════════════════════╝                    │
│                                                                              │
│ [pinned board]                                         [provenance/status]   │
└──────────────────────────────────────────────────────────────────────────────┘
```

This is the key comfort mode. Side domains and nonessential boards recede. ALINA remains present without occupying the reading area.

## 7. Screen F — Minimal / ALINA Hidden

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ FATHER | active task                                      ● ALINA available │
│                                                                              │
│                    ╔════════════════════════════════════╗                    │
│                    ║           WORK TABLE               ║                    │
│                    ╚════════════════════════════════════╝                    │
│                                                                              │
│ optional board                                                     status    │
└──────────────────────────────────────────────────────────────────────────────┘
```

The Control Center remains fully usable when the avatar is hidden or render capability is unavailable.

## 8. Screen G — Future Team Presence (not required for MVP)

```text
             [ ALINA ]
                │
       ╔══════════════════╗
       ║    WORK TABLE    ║
       ╚══════════════════╝
          /            \
 [LAWYER avatar]   [INFOSEC avatar]
       │                  │
 [legal board]      [security board]
```

Future employees appear because the task needs them, not as a permanent crowd. Their avatars share the FATHER Employee Avatar contract.

## 9. Interaction hierarchy

Priority during ordinary work:
P1 active Work Table object;
P2 task-relevant board(s);
P3 ALINA presence/state;
P4 provenance/status;
P5 navigation/future modules.

When the user explicitly opens Agent Stack or provenance analysis, that object becomes P1.

## 10. MVP navigation skeleton

```text
WELCOME
  ↓ open source/document
DOCUMENT WORK
  ↓ inspect knowledge
KNOWLEDGE BOARD
  ↓ why/evidence
EVIDENCE BOARD
  ↓ exact support
FRAGMENT / VERSION / SOURCE
  ↓ back
DOCUMENT WORK
  ↓ inspect ALINA
AGENT STACK
  ↓ select layer
LAYER BOARD
  ↓ return
DOCUMENT WORK
  ↓ focus
FOCUS MODE
```

## 11. Visual-design constraints for later high fidelity

- dark technical room, not a game HUD;
- restrained luminous geometry;
- ALINA recognizable across FULL/FACE/EYES states;
- text/data readability outranks glow/effects;
- depth supports hierarchy, not decoration;
- avoid permanent wall of panels;
- visual motion must have reduced-motion equivalent;
- REAL/DEMO/PLANNED/UNAVAILABLE legible but not visually dominant;
- future specialist avatars use coherent FATHER grammar while retaining individual identity.

## 12. Wireframe review questions

1. Is the Work Table unmistakably primary?
2. Is ALINA present but non-obstructive?
3. Can the user understand where a Board came from?
4. Can provenance be inspected without leaving the workspace?
5. Can the UI become quiet enough for long reading/coding/analysis?
6. Does Agent Stack fit naturally rather than becoming a separate mini-app?
7. Is future team presence possible without redesigning the whole room?
8. Are demo/planned functions clearly distinguishable?
9. Does the interface remain useful with no avatar rendering?
10. Does every major visual object correspond to a real contract/state?

## 13. Gate

Do not proceed to production UI code from this wireframe alone.

Next artifact: UI-007 Pre-Implementation Test Specification. It must test the end-to-end MVP flow, state restoration, truth/demo boundaries, avatar fallback, board behavior, provenance return path, long-session focus and representative viewport/performance contexts.
