from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


KeyKind = Union[
    Literal[
        "service",
        "personal",
    ],
    UnrecognizedStr,
]
