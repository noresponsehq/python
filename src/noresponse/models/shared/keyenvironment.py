from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


KeyEnvironment = Union[
    Literal[
        "live",
        "test",
    ],
    UnrecognizedStr,
]
r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""
