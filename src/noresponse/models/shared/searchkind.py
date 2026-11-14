from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


SearchKind = Union[
    Literal[
        "email",
        "phone",
        "username",
        "person_name",
        "password",
        "hash",
        "ip",
    ],
    UnrecognizedStr,
]
r"""The kind of the value searched."""
