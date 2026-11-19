from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


LastError = Union[
    Literal[
        "screening_cap_exceeded",
        "screening_unavailable",
        "person_not_found",
        "idempotency_key_reused",
    ],
    UnrecognizedStr,
]
