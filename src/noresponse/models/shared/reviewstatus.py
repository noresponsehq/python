from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ReviewStatus = Union[
    Literal[
        "open",
        "in_progress",
        "resolved",
    ],
    UnrecognizedStr,
]
