from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


PolicyEvaluationStatus = Union[
    Literal[
        "queued",
        "running",
        "completed",
        "failed",
        "cancelled",
    ],
    UnrecognizedStr,
]
