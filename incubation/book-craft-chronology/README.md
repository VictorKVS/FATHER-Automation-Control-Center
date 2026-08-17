# BOOK·CRAFT chronology MVP seed

Bounded chronology slice for the synthetic world **«Невский после полуночи»**.

Scope is intentionally fixed to exactly three manually authored demonstration events. The data proves only explicit static relationships; no automatic extraction, RAG, graph database, or story expansion is implemented.

Run:

```bash
python -m unittest discover -s tests -v
python chronology.py check --level all
python chronology.py query --event EVT-003
python chronology.py build
```

The build writes `build/book-craft-chronology-clean.zip`. Generated output is not committed.
