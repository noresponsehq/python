from __future__ import annotations
from noresponse.models.shared import (
    recordverdict as shared_recordverdict,
    recordverdictrequest as shared_recordverdictrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class JudgeRecordRequestTypedDict(TypedDict):
    group_id: str
    person_id: str
    body: shared_recordverdictrequest.RecordVerdictRequestTypedDict


class JudgeRecordRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_recordverdictrequest.RecordVerdictRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class JudgeRecordResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_recordverdict.RecordVerdictTypedDict


class JudgeRecordResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_recordverdict.RecordVerdict
