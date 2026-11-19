from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ScreeningSpendLineRole = Union[
    Literal[
        "resolver",
        "collector",
        "analyser",
    ],
    UnrecognizedStr,
]
r"""What the implementation did. analyser appears only on spend recorded before the engine stopped analysing posts."""
