# Chronology maturity roadmap

- M0 — three-event manual seed and stable references.
- M1 — deterministic validation of order, location/movement, ownership, and information acquisition.
- M2 — conflict explanations and bounded editing workflow.
- M3 — optional extraction experiments, only after a separate approval and provenance contract.

This increment closes **M1.1**: all four relationship types are validated over the fixed three-event seed, including negative mutation checks. It does not claim M1 complete.

**M1.2 complete:** a deterministic diagnostic report identifies the broken event and relation for order, movement, ownership, and information conflicts. Editing remains out of scope.

**M1.3 complete:** the clean seed produces a byte-stable diagnostics artifact with canonical input digest for independent control-stream verification.

**M1.4 complete:** `verify-report` recomputes the canonical input digest and exact three-event report, rejecting missing, malformed, stale, or tampered artifacts before a clean build is archived.

**M1.5 complete:** the clean archive carries a deterministic manifest with the byte size and SHA-256 of every payload file; build verifies it before packaging.

**M1.6 complete:** `verify-archive` reopens the produced ZIP, enforces the exact seven-member allowlist, and verifies every embedded payload against the embedded manifest.

**M1.7 complete:** clean builds use canonical ZIP timestamps, file modes, member order, and compression settings; two consecutive builds are required to be byte-identical.

**M1.8 complete:** `archive-release.json` anchors the reproducible ZIP size and SHA-256 outside the ZIP; `verify-release` compares any supplied archive with that separately versioned record.

**M2.1 complete:** `plan-repair --mutation movement` returns a deterministic preview for the `EVT-002` movement conflict, including the exact replacement and required validation, without writing or automatically applying data.

**M2.2 complete:** `review-repair` records an explicit `approve` or `reject` decision bound to the movement proposal by SHA-256. It does not authenticate reviewer identity, apply the proposal, or write chronology data.

**M2.3 complete:** `dry-run-repair` applies an approved movement proposal only to a transient fixture copy and reports diagnostics plus MIN/MED/MAX before and after. Rejected proposals are skipped; canonical data is never written.

**M2.4 complete:** `dry-run-report` persists a deterministic, timestamp-free approved dry-run bound to both the canonical source SHA-256 and proposal SHA-256. The report is included in the clean archive without writing canonical data.

**M2.5 complete:** `verify-dry-run-report` independently recomputes the approved dry-run and rejects malformed, stale, proposal-tampered, or otherwise changed report content before build packaging.

**M2.6 complete — M2 DONE/FROZEN:** `check-m2` is the single end-to-end gate for preview, approve/reject review, approved/skipped dry-run, report verification, and MIN/MED/MAX. It preserves the three-event manual seed and explicitly leaves M3 automatic extraction unauthorized.
