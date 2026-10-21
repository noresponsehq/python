from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


RateLimitErrorCode = Union[Literal["rate_limited",], UnrecognizedStr]
r"""Machine codes an HTTP 429 answer can carry."""
