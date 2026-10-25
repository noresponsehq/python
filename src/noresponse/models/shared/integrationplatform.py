from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


IntegrationPlatform = Union[
    Literal[
        "workos",
        "auth0",
        "supabase",
    ],
    UnrecognizedStr,
]
r"""The authentication provider that calls the endpoint."""
