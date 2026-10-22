from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ResponseMode = Union[
    Literal[
        "standard",
        "detailed",
    ],
    UnrecognizedStr,
]
r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""
