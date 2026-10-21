from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


BadRequestErrorCode = Union[
    Literal[
        "invalid_request",
        "invalid_idempotency_key",
        "invalid_cursor",
    ],
    UnrecognizedStr,
]
r"""Machine codes an HTTP 400 answer can carry."""
