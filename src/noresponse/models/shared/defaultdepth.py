from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


DefaultDepth = Union[
    Literal[
        "quick",
        "full",
    ],
    UnrecognizedStr,
]
r"""The depth a request for this flow that names none is served at. Defaults: full for account_creation and purchase, quick for login."""
