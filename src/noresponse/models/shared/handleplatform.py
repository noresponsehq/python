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
        "github",
        "scratch",
        "dailymotion",
        "substack",
        "duolingo",
        "dockerhub",
        "wikipedia",
        "internetarchive",
        "spotify",
        "patreon",
        "wordpress",
        "okru",
        "flickr",
        "synthetic",
    ],
    UnrecognizedStr,
]
r"""A platform a screening can cover. github and scratch through flickr are each one read of the public profile a handle names, with no posts. synthetic is the deterministic connector's own platform, for exercising the product end to end with no network."""
