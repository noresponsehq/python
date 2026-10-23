from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AccountDecision = Union[
    Literal[
        "allow",
        "step_up",
        "review",
        "block",
    ],
    UnrecognizedStr,
]
r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""
