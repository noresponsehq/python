from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ScreeningPlatformCoverageStatus = Union[
    Literal[
        "covered",
        "none_found",
        "inaccessible",
        "failed",
        "unavailable",
    ],
    UnrecognizedStr,
]
r"""covered read at least one profile; none_found looked and found no account; inaccessible found accounts that are private or locked; failed could not finish looking; unavailable has no resolver or collector enabled."""
