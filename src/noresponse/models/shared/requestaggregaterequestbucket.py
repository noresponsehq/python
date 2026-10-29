from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RequestAggregateRequestBucket = Union[
    Literal[
        "hour",
        "day",
    ],
    UnrecognizedStr,
]
