from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


GroupType = Union[
    Literal[
        "event",
        "organisation",
        "place",
        "custom",
    ],
    UnrecognizedStr,
]
r"""What the group's people share: an event, an organisation, a place or another attribute."""
