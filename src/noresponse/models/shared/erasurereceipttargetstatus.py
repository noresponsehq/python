from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ErasureReceiptTargetStatus = Union[
    Literal[
        "pending",
        "completed",
    ],
    UnrecognizedStr,
]
