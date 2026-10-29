from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class CustomerExportActionRequestTypedDict(TypedDict):
    r"""Send an empty JSON object to cancel or retry a customer export."""


class CustomerExportActionRequest(BaseModel):
    r"""Send an empty JSON object to cancel or retry a customer export."""
