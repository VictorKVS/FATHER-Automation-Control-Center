# BOOK·CRAFT chronology MVP seed

Bounded chronology slice for the synthetic world **«Невский после полуночи»**.

Scope is intentionally fixed to exactly three manually authored demonstration events. The data proves only explicit static relationships; no automatic extraction, RAG, graph database, or story expansion is implemented.

Run:

```bash
python -m unittest discover -s tests -v
python chronology.py check --level all
python chronology.py query --event EVT-003
python chronology.py diagnose --mutation movement
python chronology.py report
python chronology.py verify-report
python chronology.py build
```

The build writes `build/book-craft-chronology-clean.zip`. Generated output is not committed.

`diagnose` returns stable conflict codes, the exact event, relation, expected value, and actual value. Mutations are test-only and never alter the three-event seed.

`report` writes deterministic `reports/chronology-diagnostics.json` with the checked event IDs, check set, result, and SHA-256 of canonical static input. It contains no timestamp, model output, or protected text.

`verify-report` independently recomputes the expected report and rejects missing, malformed, stale, or tampered content. This is an integrity and consistency check for the manual seed, not automatic extraction or cryptographic authenticity.
