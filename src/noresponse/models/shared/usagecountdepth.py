from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


UsageCountDepth = Union[
    Literal[
        "quick",
        "full",
    ],
    UnrecognizedStr,
]
r"""assessments only."""
