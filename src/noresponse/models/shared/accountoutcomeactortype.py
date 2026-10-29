from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AccountOutcomeActorType = Union[
    Literal[
        "api_key",
        "user",
    ],
    UnrecognizedStr,
]
