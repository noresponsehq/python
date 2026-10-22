"""Hash an API key your signup gate issued. Hand-written; not generated."""

from __future__ import annotations

import hashlib


def hash_issued_credential(key: str) -> str:
    """SHA-256 of an issued API key, as 64 lower-case hex characters.

    The key never leaves your backend: send only this hash, as
    ``issued_credential.sha256`` on the assessment request. The key is hashed as
    its UTF-8 bytes exactly as given, with no trimming or normalisation. An empty
    key raises ``ValueError``.
    """
    if not isinstance(key, str) or key == "":
        raise ValueError("issued key must be a non-empty string")
    return hashlib.sha256(key.encode("utf-8")).hexdigest()
