from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


HighestBand = Union[
    Literal[
        "critical",
        "high",
        "moderate",
        "low",
        "info",
    ],
    UnrecognizedStr,
]
