from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ListChangeState = Union[
    Literal[
        "propagating",
        "completed",
    ],
    UnrecognizedStr,
]
