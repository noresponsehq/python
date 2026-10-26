from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


FootprintFamily = Union[
    Literal[
        "account_presence",
        "auth_provider",
        "breach",
        "breach_abuse",
        "code_hosting",
    ],
    UnrecognizedStr,
]
r"""The source-neutral kind of evidence: account_presence (an account found on a site), auth_provider (the account at your auth provider), breach (breach and credential tables), breach_abuse (abuse and fraud communities' tables) and code_hosting (a code hosting profile)."""
