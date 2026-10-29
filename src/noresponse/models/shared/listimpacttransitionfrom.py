from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ListImpactTransitionFrom = Union[
    Literal[
        "none",
        "allow",
        "block",
    ],
    UnrecognizedStr,
]
