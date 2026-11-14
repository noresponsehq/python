from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


PersonRole = Union[
    Literal[
        "guest",
        "crew",
        "vendor",
        "press",
    ],
    UnrecognizedStr,
]
r"""The person's role in the group: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: a person without one has no role, not guest. A later row naming the same person replaces it, and a change of role alone keeps the person's screening results."""
