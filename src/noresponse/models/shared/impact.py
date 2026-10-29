from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Impact = Union[
    Literal[
        "none",
        "low",
        "medium",
        "high",
    ],
    UnrecognizedStr,
]
r"""The selected reason's served impact band. Requires reason."""
