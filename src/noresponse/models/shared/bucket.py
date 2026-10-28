from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Bucket = Union[
    Literal[
        "hour",
        "day",
        "week",
    ],
    UnrecognizedStr,
]
r"""The period each count covers, in UTC; a week starts on Monday."""
