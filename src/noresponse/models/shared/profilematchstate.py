from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ProfileMatchState = Union[
    Literal[
        "confirmed",
        "probable",
        "possible",
    ],
    UnrecognizedStr,
]
r"""How sure the screening is that a profile is the person's, from its evidence: confirmed is a handle on the person row, or two or more hard identifiers (email, phone, a supplied handle, or a fact an existing source returned); probable is one identifier beyond the name; possible is the name alone."""
