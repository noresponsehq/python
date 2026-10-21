from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


FailureReason = Union[
    Literal[
        "timed_out",
        "rate_limited",
        "blocked",
        "source_error",
        "unavailable",
        "deferred",
        "insufficient_evidence",
    ],
    UnrecognizedStr,
]
r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""
