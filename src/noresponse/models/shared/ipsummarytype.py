from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


IPSummaryType = Union[
    Literal[
        "residential",
        "hosting",
        "vpn",
        "proxy",
        "tor",
        "mobile",
        "unknown",
    ],
    UnrecognizedStr,
]
r"""The address's network type."""
