from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Transport = Union[
    Literal[
        "backend",
        "browser",
        "provider_hook",
    ],
    UnrecognizedStr,
]
r"""Where the context was derived: backend (also when the request named no transport), browser, or provider_hook for a hosted provider hook."""
