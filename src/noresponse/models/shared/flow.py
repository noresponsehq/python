from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Flow = Union[
    Literal[
        "account_creation",
        "login",
        "purchase",
    ],
    UnrecognizedStr,
]
r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
