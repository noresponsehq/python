from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ErasureReceiptTargetName = Union[
    Literal[
        "serving",
        "outbox",
        "cache",
        "downstream_projection",
    ],
    UnrecognizedStr,
]
