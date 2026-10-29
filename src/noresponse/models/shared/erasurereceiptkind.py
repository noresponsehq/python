from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ErasureReceiptKind = Union[
    Literal[
        "assessment",
        "account",
        "workspace",
    ],
    UnrecognizedStr,
]
