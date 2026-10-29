from __future__ import annotations
from noresponse.models.shared import (
    keyenvironment as shared_keyenvironment,
    priority as shared_priority,
    reviewlist as shared_reviewlist,
    reviewstatus as shared_reviewstatus,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Awaitable, Callable, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListReviewsRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    limit: NotRequired[int]
    cursor: NotRequired[str]
    status: NotRequired[shared_reviewstatus.ReviewStatus]
    priority: NotRequired[shared_priority.Priority]
    assignee: NotRequired[str]
    unassigned: NotRequired[bool]
    assignee_principal_id: NotRequired[str]
    r"""Filter by immutable member ID. Mutually exclusive with assignee and unassigned=true."""
    account_id: NotRequired[str]
    r"""Only reviews of this exact account in the authenticated workspace and environment. Applied before pagination and bound into the cursor."""


class ListReviewsRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 50

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    status: Annotated[
        Optional[shared_reviewstatus.ReviewStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    priority: Annotated[
        Optional[shared_priority.Priority],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    assignee: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    unassigned: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    assignee_principal_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by immutable member ID. Mutually exclusive with assignee and unassigned=true."""

    account_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Only reviews of this exact account in the authenticated workspace and environment. Applied before pagination and bound into the cursor."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "limit",
                "cursor",
                "status",
                "priority",
                "assignee",
                "unassigned",
                "assignee_principal_id",
                "account_id",
            ]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListReviewsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_reviewlist.ReviewListTypedDict


class ListReviewsResponse(BaseModel):
    next: Union[
        Callable[[], Optional[ListReviewsResponse]],
        Callable[[], Awaitable[Optional[ListReviewsResponse]]],
    ]

    headers: Dict[str, List[str]]

    result: shared_reviewlist.ReviewList
