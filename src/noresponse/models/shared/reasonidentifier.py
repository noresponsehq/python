from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ReasonIdentifier = Union[
    Literal[
        "email",
        "username",
        "phone",
        "name",
        "ip",
        "context",
    ],
    UnrecognizedStr,
]
r"""The submitted identifier or client context field a reason concerns; absent when it concerns the whole assessment. Client context is a claimed hint, not a device fingerprint."""
