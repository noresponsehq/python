from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Identifier = Union[
    Literal[
        "email",
        "username",
    ],
    UnrecognizedStr,
]
