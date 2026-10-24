from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


EnforcementProvider = Union[
    Literal[
        "clerk",
        "workos",
        "auth0",
        "custom",
    ],
    UnrecognizedStr,
]
r"""The identity provider the action ran in; custom for the workspace's own user store."""
