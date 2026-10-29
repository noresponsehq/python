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
r"""The period each count covers: an hour, or a day or a week (from Monday) in time_zone. Hour buckets are whole UTC hours in any time zone."""
