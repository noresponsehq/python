from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


HandlePlatform = Union[
    Literal[
        "instagram",
        "x",
        "bluesky",
        "youtube",
        "tiktok",
        "facebook",
        "threads",
        "reddit",
        "telegram",
        "linkedin",
    ],
    UnrecognizedStr,
]
