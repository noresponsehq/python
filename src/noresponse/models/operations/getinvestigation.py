from __future__ import annotations
from noresponse.models.shared import investigationreport as shared_investigationreport
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetInvestigationRequestTypedDict(TypedDict):
    investigation_id: str


class GetInvestigationRequest(BaseModel):
    investigation_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetInvestigationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_investigationreport.InvestigationReportTypedDict


class GetInvestigationResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_investigationreport.InvestigationReport
