from __future__ import annotations
from .listentryrequest import ListEntryRequest, ListEntryRequestTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ListPreviewRequestTypedDict(TypedDict):
    r"""Choose an addition or a removal. The preview performs no list, account, audit, outcome or outbox write."""

    add: NotRequired[ListEntryRequestTypedDict]
    r"""POST /v1/workspaces/{workspace_id}/lists/{environment} body. Adds one entry to the environment's list and, in the same change, re-decides every account it matches: each sends account.risk_changed when a decision changes. Needs the admin or owner role, or a management key of the environment."""
    remove: NotRequired[str]


class ListPreviewRequest(BaseModel):
    r"""Choose an addition or a removal. The preview performs no list, account, audit, outcome or outbox write."""

    add: Optional[ListEntryRequest] = None
    r"""POST /v1/workspaces/{workspace_id}/lists/{environment} body. Adds one entry to the environment's list and, in the same change, re-decides every account it matches: each sends account.risk_changed when a decision changes. Needs the admin or owner role, or a management key of the environment."""

    remove: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["add", "remove"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
