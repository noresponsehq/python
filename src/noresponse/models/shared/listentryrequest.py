from __future__ import annotations
from .listentryaction import ListEntryAction
from .listentrykind import ListEntryKind
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ListEntryRequestTypedDict(TypedDict):
    r"""POST /v1/workspaces/{workspace_id}/lists/{environment} body. Adds one entry to the environment's list and, in the same change, re-decides every account it matches: each sends account.risk_changed when a decision changes. Needs the admin or owner role, or a management key of the environment."""

    kind: ListEntryKind
    r"""email matches one address, whatever the case of its local part. email_domain matches every address of the registrable domain and of its subdomains."""
    value: str
    r"""An email address for kind email, written as in an assessment request; an LDH domain (A-label for an internationalised one) such as example.com for kind email_domain, which must sit below a public suffix (co.uk alone is refused with 400). NoResponse stores it in canonical form and answers that form."""
    action: ListEntryAction
    r"""block decides block for the accounts the entry matches; allow decides allow. Block wins when both match."""
    note: NotRequired[str]
    r"""Why the entry exists, for the people who manage the list. It is shown with the entry and decides nothing."""
    expires_at: NotRequired[str]
    r"""Optional expiry. An expired entry stops matching immediately; bounded maintenance removes it and propagates account risk changes."""


class ListEntryRequest(BaseModel):
    r"""POST /v1/workspaces/{workspace_id}/lists/{environment} body. Adds one entry to the environment's list and, in the same change, re-decides every account it matches: each sends account.risk_changed when a decision changes. Needs the admin or owner role, or a management key of the environment."""

    kind: ListEntryKind
    r"""email matches one address, whatever the case of its local part. email_domain matches every address of the registrable domain and of its subdomains."""

    value: str
    r"""An email address for kind email, written as in an assessment request; an LDH domain (A-label for an internationalised one) such as example.com for kind email_domain, which must sit below a public suffix (co.uk alone is refused with 400). NoResponse stores it in canonical form and answers that form."""

    action: ListEntryAction
    r"""block decides block for the accounts the entry matches; allow decides allow. Block wins when both match."""

    note: Optional[str] = None
    r"""Why the entry exists, for the people who manage the list. It is shown with the entry and decides nothing."""

    expires_at: Optional[str] = None
    r"""Optional expiry. An expired entry stops matching immediately; bounded maintenance removes it and propagates account risk changes."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["note", "expires_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
