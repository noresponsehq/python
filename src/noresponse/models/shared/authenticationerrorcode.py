from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


AuthenticationErrorCode = Union[Literal["unauthorized",], UnrecognizedStr]
r"""Machine codes an HTTP 401 answer can carry."""
