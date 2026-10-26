from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Direction = Union[
    Literal[
        "raises",
        "lowers",
        "neutral",
    ],
    UnrecognizedStr,
]
