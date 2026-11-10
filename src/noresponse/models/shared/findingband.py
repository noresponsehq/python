from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


FindingBand = Union[
    Literal[
        "critical",
        "high",
        "moderate",
        "low",
        "info",
    ],
    UnrecognizedStr,
]
r"""How severe a finding is, most severe first."""
