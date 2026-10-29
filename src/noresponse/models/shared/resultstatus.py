from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ResultStatus = Union[
    Literal[
        "no_change",
        "proposal_requires_review",
    ],
    UnrecognizedStr,
]
