from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Conclusion = Union[
    Literal[
        "benign",
        "abuse",
        "inconclusive",
    ],
    UnrecognizedStr,
]
