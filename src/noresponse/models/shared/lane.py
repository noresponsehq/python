from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Lane = Union[
    Literal[
        "accounts",
        "phone",
        "breach",
        "ip",
    ],
    UnrecognizedStr,
]
r"""An evidence lane: accounts (account presence for email and username), phone, breach and ip."""
