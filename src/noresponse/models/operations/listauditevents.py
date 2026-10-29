from __future__ import annotations
from noresponse.models.shared import (
    auditeventlist as shared_auditeventlist,
    customerexportrequestfilteroutcome as shared_customerexportrequestfilteroutcome,
    environment as shared_environment,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Awaitable, Callable, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListAuditEventsRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    limit: NotRequired[int]
    r"""Events per page."""
    cursor: NotRequired[str]
    r"""next_cursor from the previous page, unchanged; keep every filter unchanged."""
    environment: NotRequired[shared_environment.Environment]
    r"""Affected scope. API keys can request only their own environment. Omit to read the scopes the caller is allowed."""
    action: NotRequired[str]
    r"""Exact action, such as key.created or account.deleted."""
    actor: NotRequired[str]
    r"""Exact external user id, public API key id or console credential id."""
    target_type: NotRequired[str]
    r"""Exact target kind, such as key, member, setting or workspace."""
    target_id: NotRequired[str]
    r"""Public target identifier. Audit targets exclude subject identifiers."""
    outcome: NotRequired[
        shared_customerexportrequestfilteroutcome.CustomerExportRequestFilterOutcome
    ]
    r"""Exact outcome."""
    since: NotRequired[str]
    r"""Inclusive creation timestamp in RFC3339 format."""
    until: NotRequired[str]
    r"""Exclusive creation timestamp in RFC3339 format; must follow since when both are supplied."""


class ListAuditEventsRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Events per page."""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""next_cursor from the previous page, unchanged; keep every filter unchanged."""

    environment: Annotated[
        Optional[shared_environment.Environment],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Affected scope. API keys can request only their own environment. Omit to read the scopes the caller is allowed."""

    action: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Exact action, such as key.created or account.deleted."""

    actor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Exact external user id, public API key id or console credential id."""

    target_type: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Exact target kind, such as key, member, setting or workspace."""

    target_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Public target identifier. Audit targets exclude subject identifiers."""

    outcome: Annotated[
        Optional[
            shared_customerexportrequestfilteroutcome.CustomerExportRequestFilterOutcome
        ],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Exact outcome."""

    since: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Inclusive creation timestamp in RFC3339 format."""

    until: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Exclusive creation timestamp in RFC3339 format; must follow since when both are supplied."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "limit",
                "cursor",
                "environment",
                "action",
                "actor",
                "target_type",
                "target_id",
                "outcome",
                "since",
                "until",
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


class ListAuditEventsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_auditeventlist.AuditEventListTypedDict


class ListAuditEventsResponse(BaseModel):
    next: Union[
        Callable[[], Optional[ListAuditEventsResponse]],
        Callable[[], Awaitable[Optional[ListAuditEventsResponse]]],
    ]

    headers: Dict[str, List[str]]

    result: shared_auditeventlist.AuditEventList
