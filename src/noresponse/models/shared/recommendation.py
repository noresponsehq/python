from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Recommendation = Union[
    Literal[
        "allow",
        "step_up",
        "review",
    ],
    UnrecognizedStr,
]
r"""The recommended action: allow, step_up or review. Your application applies it."""
