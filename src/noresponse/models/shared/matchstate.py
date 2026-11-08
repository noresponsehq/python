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
r"""How sure the latest screening is that it found the attendee's accounts. unscreened until a screening reaches the attendee."""
