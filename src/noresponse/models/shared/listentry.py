from __future__ import annotations
from .keyenvironment import KeyEnvironment
from .listentryaction import ListEntryAction
from .listentrykind import ListEntryKind
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ListEntryTypedDict(TypedDict):
    r"""One entry of an environment's list: an exact email or an email domain that decides an account whatever its score. An account matches when one of its admitted assessments sent the email, or an email of the domain. A block entry decides block for every flow and an allow entry decides allow; when both match, block wins. The account's risk carries the list_match reason with the entry's id, and its score stays the one the assessment's facts give. A held flow still waits for its investigation."""

    id: str
    r"""The entry's id: lst_ and a ULID."""
    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""
    kind: ListEntryKind
    r"""email matches one address, whatever the case of its local part. email_domain matches every address of the registrable domain and of its subdomains."""
    value: str
    r"""The value the entry matches, in canonical form: an email lower-cased whole, or a domain lower-cased and taken to its registrable domain (mail.example.co.uk is stored as example.co.uk)."""
    action: ListEntryAction
    r"""block decides block for the accounts the entry matches; allow decides allow. Block wins when both match."""
    created_at: str
    created_by: str
    r"""The external user id of the member who added the entry through the console, or the prefix (nrk_<environment>_<key id>) of the management key that added it."""
    note: NotRequired[str]
    r"""Why the entry exists, for the people who manage the list. It is shown with the entry and decides nothing."""
    expires_at: NotRequired[str]
    r"""Optional expiry. An expired entry stops matching immediately; bounded maintenance removes it and propagates account risk changes."""


class ListEntry(BaseModel):
    r"""One entry of an environment's list: an exact email or an email domain that decides an account whatever its score. An account matches when one of its admitted assessments sent the email, or an email of the domain. A block entry decides block for every flow and an allow entry decides allow; when both match, block wins. The account's risk carries the list_match reason with the entry's id, and its score stays the one the assessment's facts give. A held flow still waits for its investigation."""

    id: str
    r"""The entry's id: lst_ and a ULID."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""

    kind: ListEntryKind
    r"""email matches one address, whatever the case of its local part. email_domain matches every address of the registrable domain and of its subdomains."""

    value: str
    r"""The value the entry matches, in canonical form: an email lower-cased whole, or a domain lower-cased and taken to its registrable domain (mail.example.co.uk is stored as example.co.uk)."""

    action: ListEntryAction
    r"""block decides block for the accounts the entry matches; allow decides allow. Block wins when both match."""

    created_at: str

    created_by: str
    r"""The external user id of the member who added the entry through the console, or the prefix (nrk_<environment>_<key id>) of the management key that added it."""

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
