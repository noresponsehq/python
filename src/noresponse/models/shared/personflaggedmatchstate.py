from __future__ import annotations
from typing import Literal


PersonFlaggedMatchState = Literal[
    "confirmed",
    "probable",
    "possible",
    "none_found",
    "inaccessible",
]
r"""How sure the screening is that the accounts it read are the person's. A finding on a possible match is at most moderate, on a probable match at most high."""
