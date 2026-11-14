from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


PersonBatchItemOutcome = Union[
    Literal[
        "created",
        "updated",
        "unchanged",
    ],
    UnrecognizedStr,
]
r"""unchanged: the row matched a person with the same details."""
