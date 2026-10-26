from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RiskDetailsEventKind = Union[
    Literal[
        "created",
        "last_active",
        "breached",
    ],
    UnrecognizedStr,
]
