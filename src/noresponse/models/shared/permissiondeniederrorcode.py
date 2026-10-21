from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


PermissionDeniedErrorCode = Union[Literal["tenant_forbidden",], UnrecognizedStr]
r"""Machine codes an HTTP 403 answer can carry."""
