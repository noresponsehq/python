from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


InvestigationStatus = Union[
    Literal[
        "queued",
        "running",
        "completed",
        "partial",
        "failed",
        "cancelled",
        "unknown",
    ],
    UnrecognizedStr,
]
