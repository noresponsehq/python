from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


IdentifierSearchKind = Union[
    Literal[
        "email",
        "phone",
        "username",
    ],
    UnrecognizedStr,
]
