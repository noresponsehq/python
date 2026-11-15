from __future__ import annotations
from .handle import Handle, HandleTypedDict
from .personrole import PersonRole
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PersonIdentityTypedDict(TypedDict):
    external_id: NotRequired[str]
    r"""Your reference for this person within the workspace environment. Only an explicit reference or person_id can reuse an existing person."""
    name: NotRequired[str]
    r"""The person's full name."""
    email: NotRequired[str]
    r"""The person's email."""
    phone: NotRequired[str]
    r"""The person's phone in E.164 form."""
    company: NotRequired[str]
    r"""Where the person works."""
    city: NotRequired[str]
    r"""Where the person lives."""
    handles: NotRequired[List[HandleTypedDict]]
    person_id: NotRequired[str]
    role: NotRequired[PersonRole]
    r"""The person's role in the group: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: a person without one has no role, not guest. A later row naming the same person replaces it, and a change of role alone keeps the person's screening results."""


class PersonIdentity(BaseModel):
    external_id: Optional[str] = None
    r"""Your reference for this person within the workspace environment. Only an explicit reference or person_id can reuse an existing person."""

    name: Optional[str] = None
    r"""The person's full name."""

    email: Optional[str] = None
    r"""The person's email."""

    phone: Optional[str] = None
    r"""The person's phone in E.164 form."""

    company: Optional[str] = None
    r"""Where the person works."""

    city: Optional[str] = None
    r"""Where the person lives."""

    handles: Optional[List[Handle]] = None

    person_id: Optional[str] = None

    role: Optional[PersonRole] = None
    r"""The person's role in the group: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: a person without one has no role, not guest. A later row naming the same person replaces it, and a change of role alone keeps the person's screening results."""

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
                "handles",
                "person_id",
                "role",
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
