from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Stage = Union[
    Literal[
        "lookup",
        "lookup_typing",
        "platforms",
        "written",
        "late_platforms",
        "late_lookup",
        "ai_typing",
        "analysis",
        "rating",
    ],
    UnrecognizedStr,
]
r"""ai_typing and analysis appear only on searches recorded before the engine stopped analysing results."""
