from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


NotFoundErrorCode = Union[Literal["not_found",], UnrecognizedStr]
r"""Machine codes an HTTP 404 answer can carry."""
