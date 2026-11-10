from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Access = Union[
    Literal[
        "public",
        "private",
        "locked",
    ],
    UnrecognizedStr,
]
r"""public profiles were read; a private or locked one exists but could not be read."""
