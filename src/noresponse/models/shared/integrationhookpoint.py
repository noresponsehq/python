from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


IntegrationHookPoint = Union[
    Literal[
        "pre_registration",
        "post_login",
    ],
    UnrecognizedStr,
]
r"""pre_registration runs before the user exists; post_login runs after a successful sign-in."""
