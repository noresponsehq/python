from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AccountType = Union[
    Literal[
        "personal",
        "business",
    ],
    UnrecognizedStr,
]
r"""personal, or business: an account a company or school manages."""
