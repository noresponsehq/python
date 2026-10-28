from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Delay = Union[
    Literal[
        "under_10s",
        "under_1m",
        "under_10m",
        "under_1h",
        "under_1d",
        "over_1d",
    ],
    UnrecognizedStr,
]
r"""How long after the assessment's creation the change was made."""
