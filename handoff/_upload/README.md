# Handoff transport area

`handoff/_upload/` is a temporary transport area for ALINA handoff payloads.

Large payloads should not be retained on the default branch. The publishing workflow converts staged payloads into GitHub Actions artifacts. After successful publication and verification, temporary tracked payloads should be removed in a separate commit.

Canonical audit data remains in `FATHER_VAULT`.
