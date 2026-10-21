from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


IncompleteReason = Union[
    Literal[
        "timed_out",
        "rate_limited",
        "blocked",
        "source_error",
        "unavailable",
        "deferred",
    ],
    UnrecognizedStr,
]
r"""Why a lane did not settle. deferred means the lane is asynchronous and still running; a continuation settles it. timed_out means the lane missed its deadline. insufficient_evidence is a settled inconclusive signal rather than an incomplete lane."""
