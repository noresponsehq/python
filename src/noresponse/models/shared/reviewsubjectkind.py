from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ReviewSubjectKind = Union[
    Literal[
        "account",
        "assessment",
        "issued_credential",
    ],
    UnrecognizedStr,
]
