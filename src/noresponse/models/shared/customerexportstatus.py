from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


CustomerExportStatus = Union[
    Literal[
        "queued",
        "running",
        "completed",
        "failed",
        "cancelled",
        "expired",
    ],
    UnrecognizedStr,
]
