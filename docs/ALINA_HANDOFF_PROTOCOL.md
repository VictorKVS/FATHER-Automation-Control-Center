# ALINA Handoff Protocol

## Purpose

Transfer channel between local FATHER/ALINA production runs and GitHub for review by ChatGPT.

## Principles

1. FATHER_VAULT remains the local source repository for audit outputs and large machine data.
2. Normal Git stores compact control-plane artifacts: status, manifests, summaries, scripts, schemas, and review decisions.
3. Large machine handoffs are transferred as GitHub Actions artifacts rather than retained in normal Git history.
4. Publishing a handoff never authorizes deletion, movement, or modification of source documents.
5. Every substantive ALINA operation writes an ALINA journal entry.

## Required metadata

Each handoff identifies handoff/version, source run, timestamp, mode, record count where applicable, SHA-256, completion state, next stage, and known limitations.

## Lifecycle

```text
FATHER_VAULT
 -> validate output
 -> package payload
 -> calculate SHA-256
 -> write manifest/status/journal
 -> stage temporary handoff upload
 -> GitHub Actions artifact
 -> reviewer retrieval
 -> review decision
 -> next ALINA stage
```

## Safety gate

A handoff is data transfer only. It MUST NOT imply permission for physical cleanup.

```text
candidate
 -> canonical source identified
 -> destination copy created
 -> source/destination SHA-256 equal
 -> catalog registration confirmed
 -> explicit cleanup approval
 -> delete/move action may be considered
```

## V05 special rule

V05 is PARTIAL_COMPLETE and READ_ONLY / PLAN_ONLY. Its file-level migration decision is not sufficient for physical migration. V0.5.1 must classify context trees before V0.6 Safe Migration.

```text
FILE != DOCUMENTAL UNIT
file
 -> context tree
 -> COURSE / PROJECT / EXISTING_KB / LIBRARY / INBOX / LOOSE_SOURCE
 -> physical storage decision
```

## Artifact retention

GitHub Actions artifacts are transport packages, not the canonical archive. Canonical local audit data remains under FATHER_VAULT until a later storage policy explicitly changes that rule.
