# BOOK·CRAFT chronology MVP seed

Bounded chronology slice for the synthetic world **«Невский после полуночи»**.

Scope is intentionally fixed to exactly three manually authored demonstration events. The data proves only explicit static relationships; no automatic extraction, RAG, graph database, or story expansion is implemented.

Run:

```bash
python -m unittest discover -s tests -v
python chronology.py check --level all
python chronology.py query --event EVT-003
python chronology.py diagnose --mutation movement
python chronology.py plan-repair --mutation movement
python chronology.py review-repair --mutation movement --decision approve
python chronology.py review-repair --mutation movement --decision reject
python chronology.py report
python chronology.py verify-report
python chronology.py manifest
python chronology.py verify-manifest
python chronology.py build
python chronology.py verify-archive
python chronology.py release
python chronology.py verify-release
```

The build writes `build/book-craft-chronology-clean.zip`. Generated output is not committed.

`diagnose` returns stable conflict codes, the exact event, relation, expected value, and actual value. Mutations are test-only and never alter the three-event seed.

`plan-repair --mutation movement` produces a deterministic preview for the controlled `EVT-002` movement fixture. It names the exact replacement and MIN/MED/MAX acceptance requirement but never writes or automatically changes chronology data.

`review-repair` records an explicit `approve` or `reject` CLI decision bound to the preview proposal by SHA-256. Reviewer identity is not authenticated, and neither decision applies the proposal or writes chronology data.

`report` writes deterministic `reports/chronology-diagnostics.json` with the checked event IDs, check set, result, and SHA-256 of canonical static input. It contains no timestamp, model output, or protected text.

`verify-report` independently recomputes the expected report and rejects missing, malformed, stale, or tampered content. This is an integrity and consistency check for the manual seed, not automatic extraction or cryptographic authenticity.

`manifest` writes deterministic `reports/archive-manifest.json` with the byte size and SHA-256 of all six payload files. `verify-manifest` rejects stale or tampered payload metadata; the manifest itself is the seventh archive entry and is intentionally not self-hashed.

`verify-archive` reads the finished ZIP without extracting it, rejects missing or additional members, and compares every embedded payload byte-for-byte through its size and SHA-256 in the embedded manifest.

Clean ZIP output is reproducible: member order, timestamp (`1980-01-01 00:00:00`), Unix file mode (`0644`), and compression level are fixed. Unchanged inputs therefore produce a byte-identical archive and SHA-256 on consecutive builds in the same toolchain.

`release` writes `reports/archive-release.json` outside the ZIP with its byte size and SHA-256. `verify-release` checks a supplied archive against this separately versioned anchor. Build deliberately does not rewrite the release record automatically.
