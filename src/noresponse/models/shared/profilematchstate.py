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
r"""How sure the screening is that a profile is the person's, from the likelihood its record scores. Confirmed reaches the join bar of 0.9. Probable reaches 0.85, which takes a shared value beyond the one that found the account. Possible is the rest."""
