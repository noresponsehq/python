from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Topic = Union[
    Literal[
        "identity",
        "location",
        "movement",
        "timeline",
        "interests",
        "relationships",
        "work",
        "education",
        "accounts",
        "credentials",
        "devices",
        "absence",
    ],
    UnrecognizedStr,
]
