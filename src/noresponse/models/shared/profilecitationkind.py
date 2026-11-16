from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ProfileCitationKind = Union[
    Literal[
        "record",
        "post",
        "check",
    ],
    UnrecognizedStr,
]
r"""record: a record in lookup.records or profiles[].record. post: an item in posts. check: an item in lookup.checks."""
