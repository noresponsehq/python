from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AttendeeBatchItemOutcome = Union[
    Literal[
        "created",
        "updated",
        "unchanged",
    ],
    UnrecognizedStr,
]
r"""unchanged: the row matched an attendee with the same details."""
