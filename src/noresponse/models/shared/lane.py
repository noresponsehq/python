from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Lane = Union[
    Literal[
        "accounts",
        "phone",
        "breach",
        "domain",
        "ip",
    ],
    UnrecognizedStr,
]
r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""
