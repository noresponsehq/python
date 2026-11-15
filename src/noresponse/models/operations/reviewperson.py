from __future__ import annotations
from noresponse.models.shared import (
    person as shared_person,
    personreviewrequest as shared_personreviewrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ReviewPersonRequestTypedDict(TypedDict):
    group_id: str
    person_id: str
    body: shared_personreviewrequest.PersonReviewRequestTypedDict


class ReviewPersonRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_personreviewrequest.PersonReviewRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class ReviewPersonResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_person.PersonTypedDict


class ReviewPersonResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_person.Person
