from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


KeyStatus = Union[
    Literal[
        "active",
        "expired",
        "revoked",
    ],
    UnrecognizedStr,
]
r"""active: the key authenticates. expired: a rotation's overlap window has ended (expires_at). revoked: the key was revoked (revoked_at) and answers 401."""
