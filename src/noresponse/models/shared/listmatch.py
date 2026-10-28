from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ListMatch = Union[
    Literal[
        "block",
        "allow",
    ],
    UnrecognizedStr,
]
r"""The action of the list entry that decided the account."""
