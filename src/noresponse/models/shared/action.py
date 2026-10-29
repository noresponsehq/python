from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Action = Union[
    Literal[
        "allow",
        "block",
    ],
    UnrecognizedStr,
]
