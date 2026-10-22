from __future__ import annotations
from noresponse.models.shared import integration as shared_integration
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class CreateIntegrationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_integration.IntegrationTypedDict


class CreateIntegrationResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_integration.Integration
