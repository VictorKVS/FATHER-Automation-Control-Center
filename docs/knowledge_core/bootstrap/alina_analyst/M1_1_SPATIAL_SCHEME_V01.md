# ALINA Control Center M1.1 — Spatial Scheme v0.1

Status: NOTATION_BASELINE  
Trace: Entry 0044 / UI-GAP-001 / M1.1 Visual Architecture Passport.

## 1. Primary depth notation

\`\`\`text
BACK WALL / INFORMATION SCREENS
Sources | Knowledge | Graph | Evidence | Activity
                 ↓
          ALINA PRESENCE
      analytical focal layer
                 ↓
          CENTRAL WORK TABLE
 document | object | graph | compare | review
                 ↓
                USER
\`\`\`

## 2. Desktop composition

\`\`\`text
┌──────────────────── COMMAND / STATUS BAR ────────────────────┐
│                                                              │
│ SOURCE      ┌──────── INFORMATION WALL ────────┐   AGENT     │
│ RAIL        │ KNOWLEDGE | GRAPH | EVIDENCE     │   STACK     │
│             │          ACTIVITY / STATUS        │             │
│             └──────────────┬────────────────────┘             │
│                            │                                  │
│                       ┌────▼────┐                             │
│                       │  ALINA  │                             │
│                       │PRESENCE │                             │
│                       └────┬────┘                             │
│                            │                                  │
│             ╔══════════════▼══════════════╗                   │
│             ║         WORK TABLE          ║                   │
│             ║ current decision / object   ║                   │
│             ╚═════════════════════════════╝                   │
│                                                              │
├──── PROVENANCE | JOBS | ALERTS | SYSTEM / FALLBACK ──────────┤
└──────────────────────────────────────────────────────────────┘
\`\`\`

## 3. Layer model

Z0 background atmosphere; Z1 information wall; Z2 ALINA; Z3 Work Table; Z4 rails/controls/status. Layering communicates function, not merely decoration.

## 4. State transformations

FULL: wall + ALINA + Work Table + side context.  
FOCUS: Work Table dominates; wall/rails attenuate; truth status remains visible.  
COMPACT: ALINA collapses but context remains.  
STATUS_ONLY: avatar renderer unavailable; status indicator replaces presence; Work Table remains usable.  
REDUCED_MOTION: same spatial hierarchy with no motion-dependent meaning.

## 5. Data flow notation

\`\`\`text
FatherObject refs ─┐
BoardState refs ───┼─> Presentation Model ─> Information Wall / Work Table
WorkspaceState ────┘                    └─> ALINA presentation state

Canonical truth is NOT copied into presentation state.
\`\`\`

## 6. M1.1 constraints

No real backend invented. No final 3D dependency. No hidden truth-status badges. No essential information encoded only by glow/color/animation. No layout where avatar failure destroys task usability.
