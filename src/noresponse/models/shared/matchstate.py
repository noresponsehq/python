from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


MatchState = Union[
    Literal[
        "unscreened",
        "confirmed",
        "probable",
        "possible",
        "none_found",
        "inaccessible",
    ],
    UnrecognizedStr,
]
r"""How sure the latest screening is that it found the person's accounts. unscreened until a screening reaches the person, and after one that had no profile to check (no_profile_to_check)."""
