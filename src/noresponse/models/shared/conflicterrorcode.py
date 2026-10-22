from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ConflictErrorCode = Union[
    Literal[
        "idempotency_key_reused",
        "key_rotation_in_progress",
        "too_many_integrations",
    ],
    UnrecognizedStr,
]
r"""Machine codes an HTTP 409 answer can carry."""
