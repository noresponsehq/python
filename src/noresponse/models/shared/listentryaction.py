from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ListEntryAction = Union[
    Literal[
        "block",
        "allow",
    ],
    UnrecognizedStr,
]
r"""block decides block for the accounts the entry matches; allow decides allow. Block wins when both match."""
