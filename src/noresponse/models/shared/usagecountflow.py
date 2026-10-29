from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


UsageCountFlow = Union[
    Literal[
        "account_creation",
        "login",
        "purchase",
    ],
    UnrecognizedStr,
]
r"""assessments only."""
