from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Match = Union[
    Literal[
        "exact",
        "canonical",
        "mailbox",
    ],
    UnrecognizedStr,
]
r"""exact compares the original submitted value; canonical uses identifier-specific normalisation; mailbox explicitly selects the email alias rules used by lists."""
