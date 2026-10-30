from __future__ import annotations
from .linkedaccount import LinkedAccount, LinkedAccountTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LinkedAccountPageTypedDict(TypedDict):
    r"""Other accounts in this workspace and environment whose retained assessments submitted an email, phone or customer-namespace username that one of account_id's retained assessments also submitted. Matching uses the identifier search rules: exact, canonical and, for email, mailbox. Only customer-submitted identifiers link accounts; source-discovered identifiers do not. Expired, retention-shortened, deleted and erased assessments link nothing. A shared identifier is not verified ownership. Accounts use stable opaque order, the page and total share one database snapshot, and later pages are live. Cursors bind the workspace, environment, operation and account_id, and expire."""

    account_id: str
    r"""The account whose submitted identifiers were compared. It is excluded from items."""
    items: List[LinkedAccountTypedDict]
    total: int
    r"""Distinct linked accounts, exact below 10000 and capped at 10000."""
    total_capped: bool
    r"""True when at least 10000 accounts are linked."""
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    next_cursor: NotRequired[str]
    r"""Opaque, expiring cursor bound to this environment, operation and account_id. Absent on the last page."""


class LinkedAccountPage(BaseModel):
    r"""Other accounts in this workspace and environment whose retained assessments submitted an email, phone or customer-namespace username that one of account_id's retained assessments also submitted. Matching uses the identifier search rules: exact, canonical and, for email, mailbox. Only customer-submitted identifiers link accounts; source-discovered identifiers do not. Expired, retention-shortened, deleted and erased assessments link nothing. A shared identifier is not verified ownership. Accounts use stable opaque order, the page and total share one database snapshot, and later pages are live. Cursors bind the workspace, environment, operation and account_id, and expire."""

    account_id: str
    r"""The account whose submitted identifiers were compared. It is excluded from items."""

    items: List[LinkedAccount]

    total: int
    r"""Distinct linked accounts, exact below 10000 and capped at 10000."""

    total_capped: bool
    r"""True when at least 10000 accounts are linked."""

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    next_cursor: Optional[str] = None
    r"""Opaque, expiring cursor bound to this environment, operation and account_id. Absent on the last page."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_cursor"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    LinkedAccountPage.model_rebuild()
except NameError:
    pass
