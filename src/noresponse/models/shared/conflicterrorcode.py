from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ConflictErrorCode = Union[
    Literal[
        "idempotency_key_reused",
        "key_rotation_in_progress",
        "webhook_endpoint_limit_reached",
        "webhook_endpoint_unverified",
        "too_many_integrations",
        "risk_version_ahead",
        "key_limit_reached",
        "self_revocation",
        "outcome_conflict",
        "credential_conflict",
        "binding_conflict",
        "list_entry_exists",
        "list_limit_reached",
        "list_entry_too_broad",
    ],
    UnrecognizedStr,
]
r"""Machine codes an HTTP 409 answer can carry."""
