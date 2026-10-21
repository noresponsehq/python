from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Band = Union[
    Literal[
        "low",
        "medium",
        "high",
        "critical",
    ],
    UnrecognizedStr,
]
r"""low 0-29, medium 30-59, high 60-84, critical 85-100."""
