from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AttendeeRole = Union[
    Literal[
        "guest",
        "crew",
        "vendor",
        "press",
    ],
    UnrecognizedStr,
]
r"""The attendee's role at the event: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: an attendee without one has no role, not guest. A later row naming the same attendee replaces it, and a change of role alone keeps the attendee's screening results."""
