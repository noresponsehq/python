from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Band = Union[
    Literal[
        "low",
        "medium",
        "high",
        "critical",
    ],
    UnrecognizedStr,
]
