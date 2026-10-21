from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ConsistencyValue = Union[
    Literal[
        "match",
        "partial",
        "mismatch",
        "unknown",
    ],
    UnrecognizedStr,
]
r"""How a submitted identifier agrees with what the evidence holds for the other identifiers. unknown is a definite 'cannot tell' (for example a truncated or too-common breach result); absent means the comparison was not made."""
