from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


SignalOutcome = Union[
    Literal[
        "found",
        "not_found",
        "inconclusive",
        "blocked",
        "unavailable",
    ],
    UnrecognizedStr,
]
r"""Per-signal outcome. A source that timed out, was blocked or errored reports blocked, unavailable or inconclusive with a reason and is listed in incomplete_sources; not_found is a definite absence."""
