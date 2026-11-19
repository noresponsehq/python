from __future__ import annotations
from .personchangekind import PersonChangeKind
from .significance import Significance
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PersonChangeTypedDict(TypedDict):
    id: str
    kind: PersonChangeKind
    r"""account_added and account_removed: an account or profile appeared or disappeared. breach_added and breach_removed: a breach record appeared or disappeared. identifier_added and identifier_removed: an email, phone, username, name or account id on an account the person already held. field_changed: another field on such an account. finding_added: a new finding. posts_added: new posts, counted in count."""
    significance: Significance
    r"""One rule ranks every change: identity changes (accounts, breaches, identifiers) are high, profile fields and findings are medium, new posts are low."""
    source: str
    r"""The connector, site or platform the change came from."""
    investigation_id: str
    r"""The investigation that found the change."""
    previous_investigation_id: str
    r"""The earlier investigation it was compared with."""
    created_at: str
    reviewed_at: Nullable[str]
    field: NotRequired[str]
    before: NotRequired[str]
    after: NotRequired[str]
    count: NotRequired[int]
    reviewed_by: NotRequired[str]


class PersonChange(BaseModel):
    id: str

    kind: PersonChangeKind
    r"""account_added and account_removed: an account or profile appeared or disappeared. breach_added and breach_removed: a breach record appeared or disappeared. identifier_added and identifier_removed: an email, phone, username, name or account id on an account the person already held. field_changed: another field on such an account. finding_added: a new finding. posts_added: new posts, counted in count."""

    significance: Significance
    r"""One rule ranks every change: identity changes (accounts, breaches, identifiers) are high, profile fields and findings are medium, new posts are low."""

    source: str
    r"""The connector, site or platform the change came from."""

    investigation_id: str
    r"""The investigation that found the change."""

    previous_investigation_id: str
    r"""The earlier investigation it was compared with."""

    created_at: str

    reviewed_at: Nullable[str]

    field: Optional[str] = None

    before: Optional[str] = None

    after: Optional[str] = None

    count: Optional[int] = None

    reviewed_by: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["field", "before", "after", "count", "reviewed_by"])
        nullable_fields = set(["reviewed_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
