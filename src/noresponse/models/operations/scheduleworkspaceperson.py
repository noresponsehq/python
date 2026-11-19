from __future__ import annotations
from noresponse.models.shared import (
    personschedule as shared_personschedule,
    personschedulerequest as shared_personschedulerequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ScheduleWorkspacePersonRequestTypedDict(TypedDict):
    person_id: str
    body: shared_personschedulerequest.PersonScheduleRequestTypedDict


class ScheduleWorkspacePersonRequest(BaseModel):
    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_personschedulerequest.PersonScheduleRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class ScheduleWorkspacePersonResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_personschedule.PersonScheduleTypedDict


class ScheduleWorkspacePersonResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_personschedule.PersonSchedule
