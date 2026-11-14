from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


PersonDecision = Union[
    Literal[
        "cleared",
        "watch",
        "escalated",
    ],
    UnrecognizedStr,
]
