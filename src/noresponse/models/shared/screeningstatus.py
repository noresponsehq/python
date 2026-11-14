from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ScreeningStatus = Union[
    Literal[
        "queued",
        "running",
        "completed",
        "partial",
        "failed",
        "cancelled",
    ],
    UnrecognizedStr,
]
r"""partial finished with some people or platforms not covered; people_failed and people_partial count them."""
