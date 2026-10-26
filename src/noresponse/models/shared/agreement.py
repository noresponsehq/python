from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Agreement = Union[
    Literal[
        "match",
        "partial",
        "mismatch",
    ],
    UnrecognizedStr,
]
