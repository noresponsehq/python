from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


SourceID = Union[
    Literal[
        "github",
        "phone",
        "breach",
        "rdap",
        "mx",
        "ipintel",
        "adobe",
        "nvidia",
        "wix",
        "life360",
        "zapier",
        "google",
    ],
    UnrecognizedStr,
]
r"""A NoResponse source: github (GitHub accounts), phone (the phone lookup), breach (breach exposure), rdap (the email domain's registration), mx (the email domain's mail servers), ipintel (IP intelligence) or an email account source that searches one platform for an account by email address (adobe, nvidia, wix, life360, zapier, google). google runs only for Gmail addresses."""
