from __future__ import annotations
from .handle import Handle, HandleTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class WorkspacePersonTypedDict(TypedDict):
    id: str
    created_at: str
    updated_at: str
    expires_at: str
    r"""The time the workspace retention policy removes this person, their evidence and investigation history. Shortening workspace retention can move this time earlier."""
    external_id: NotRequired[str]
    r"""Your reference for this person within the workspace environment. Only an explicit reference or person_id can reuse an existing person."""
    name: NotRequired[str]
    email: NotRequired[str]
    r"""The person's email."""
    phone: NotRequired[str]
    r"""The person's phone in E.164 form."""
    company: NotRequired[str]
    r"""Where the person works."""
    city: NotRequired[str]
    r"""Where the person lives."""
    username: NotRequired[str]
    r"""A username the person uses, with no platform. A search looks it up on every platform that finds accounts by username."""
    handles: NotRequired[List[HandleTypedDict]]
    r"""Accounts the person is known to hold, at most 20."""


class WorkspacePerson(BaseModel):
    id: str

    created_at: str

    updated_at: str

    expires_at: str
    r"""The time the workspace retention policy removes this person, their evidence and investigation history. Shortening workspace retention can move this time earlier."""

    external_id: Optional[str] = None
    r"""Your reference for this person within the workspace environment. Only an explicit reference or person_id can reuse an existing person."""

    name: Optional[str] = None

    email: Optional[str] = None
    r"""The person's email."""

    phone: Optional[str] = None
    r"""The person's phone in E.164 form."""

    company: Optional[str] = None
    r"""Where the person works."""

    city: Optional[str] = None
    r"""Where the person lives."""

    username: Optional[str] = None
    r"""A username the person uses, with no platform. A search looks it up on every platform that finds accounts by username."""

    handles: Optional[List[Handle]] = None
    r"""Accounts the person is known to hold, at most 20."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "external_id",
                "name",
                "email",
                "phone",
                "company",
                "city",
                "username",
                "handles",
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
