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
        "synthetic",
    ],
    UnrecognizedStr,
]
r"""A platform a screening can cover. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""
