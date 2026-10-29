from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Source = Union[
    Literal[
        "requests",
        "webhook_attempts",
    ],
    UnrecognizedStr,
]
