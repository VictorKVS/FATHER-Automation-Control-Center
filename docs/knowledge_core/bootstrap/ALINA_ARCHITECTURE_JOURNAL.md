# ALINA Architecture Journal

## Entry 0001 — Regulatory foundation and site projection

- operation: ARCHITECTURE_DECISION
- scope: FATHER Knowledge Core + ALINA Control Center
- result: ACCEPTED_FOR_V0.1
- decision: Regulatory/legal hierarchy becomes a first-class Knowledge Graph projection and a foundation for specialist formation.
- layers: general legal foundation -> industry -> industry regulation -> regulators -> departmental acts -> local organizational acts.
- key_chain: source -> requirement -> applicability -> obligation/prohibition/permission -> control -> compliance evidence -> responsible role -> competency -> specialist.
- site_change: add Regulatory Graph and Impact Graph projections with version timeline, provenance, applicability and downstream impact.
- safety: no automatic claim of applicability based only on document hierarchy; historical versions preserved.
- next_action: map this contract to PostgreSQL entities and UI information architecture.
- priority: P0

## Entry 0002 — Principle of Currency

- operation: ARCHITECTURE_DECISION
- scope: FATHER Regulatory Knowledge + ALINA Control Center
- result: ACCEPTED_FOR_V0.1
- decision: Currentness is mandatory evidence-backed metadata, never an implicit/permanent property.
- rule: NO CURRENTNESS EVIDENCE -> NO CLAIM OF CURRENTNESS.
- behavior: official-source checks, version/hash comparison, immutable history, semantic/requirement diff, applicability re-evaluation and downstream impact review.
- UI: Currency / Update Radar required.
- audit: every verification and currentness transition is an auditable event.
- next_action: implement Source Registry + Watch + Applicability contracts and map currentness fields to PostgreSQL.
- priority: P0
