from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


WrittenProfileStatus = Union[
    Literal[
        "queued",
        "written",
        "failed",
    ],
    UnrecognizedStr,
]
r"""queued: the profile is being written. written: summary, statements and leads hold it. failed: it could not be written; error_code says why and no content is returned."""
