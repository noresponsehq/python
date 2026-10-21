from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Freshness = Union[
    Literal[
        "fresh",
        "stale",
        "unknown",
    ],
    UnrecognizedStr,
]
r"""Freshness class of the evidence behind a signal. unknown whenever no evidence was obtained."""
