from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Failure = Union[
    Literal[
        "invalid_url",
        "resolve_failed",
        "address_refused",
        "timeout",
        "connection_failed",
        "redirect",
        "non_2xx",
    ],
    UnrecognizedStr,
]
r"""Why the attempt failed: the URL is no longer valid, the host did not resolve, it resolved to an address that is not public, no answer within 5 seconds, the connection failed, a 3xx (redirects are not followed) or another non-2xx status. Absent for a delivered attempt."""
