from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


SuggestedSearchKind = Union[
    Literal[
        "username",
        "email",
        "phone",
    ],
    UnrecognizedStr,
]
r"""The kind of the value: one of the kinds the environment's enrichment setting names."""
