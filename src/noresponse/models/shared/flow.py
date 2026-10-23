from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Flow = Union[
    Literal[
        "signup",
        "login",
        "purchase",
    ],
    UnrecognizedStr,
]
r"""The customer event an assessment is made for: signup (a new account), login (a returning sign-in) or purchase (a payment or credit grant). The account's risk is reported with the decision for this flow."""
