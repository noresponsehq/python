from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


OwnerType = Union[
    Literal[
        "user",
        "api_key",
    ],
    UnrecognizedStr,
]
r"""The credential namespace of the creator. An external user ID equal to an API-key label does not grant ownership of that key's private view."""
