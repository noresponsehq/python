from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


HookPoint = Union[
    Literal[
        "pre_registration",
        "post_registration",
        "pre_login",
        "post_login",
        "token_issuance",
    ],
    UnrecognizedStr,
]
r"""The provider event a provider_hook context was sent for; absent for any other transport."""
