from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Decision = Union[
    Literal[
        "allow",
        "step_up",
        "review",
        "block",
    ],
    UnrecognizedStr,
]
r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""
