from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Country = Union[
    Literal[
        "consistent",
        "mismatch",
        "unknown",
    ],
    UnrecognizedStr,
]
r"""IP country, phone country, breach countries and policy_context.region together."""
