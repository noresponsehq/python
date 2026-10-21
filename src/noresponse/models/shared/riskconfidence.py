from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RiskConfidence = Union[
    Literal[
        "low",
        "medium",
        "high",
    ],
    UnrecognizedStr,
]
r"""How much of the planned evidence answered; it says nothing about risk."""
