from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Significance = Union[
    Literal[
        "high",
        "medium",
        "low",
    ],
    UnrecognizedStr,
]
r"""One rule ranks every change: identity changes (accounts, breaches, identifiers) are high, profile fields are medium, new posts are low."""
