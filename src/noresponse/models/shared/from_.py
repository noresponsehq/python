from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


From = Union[
    Literal[
        "allow",
        "step_up",
        "review",
        "block",
        "held",
    ],
    UnrecognizedStr,
]
