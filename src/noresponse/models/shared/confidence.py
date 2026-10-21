from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Confidence = Union[
    Literal[
        "low",
        "medium",
        "high",
        "unavailable",
    ],
    UnrecognizedStr,
]
r"""Ordinal confidence in the recommendation under the current policy: low, medium, high or unavailable."""
