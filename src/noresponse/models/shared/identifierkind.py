from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


IdentifierKind = Union[
    Literal[
        "email",
        "username",
        "phone",
        "ip",
    ],
    UnrecognizedStr,
]
r"""Which submitted identifier a signal concerns. ip is a selector of breach_exposure only."""
