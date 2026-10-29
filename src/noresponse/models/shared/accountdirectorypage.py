from __future__ import annotations
from .accountdirectorypageitem import (
    AccountDirectoryPageItem,
    AccountDirectoryPageItemTypedDict,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountDirectoryPageTypedDict(TypedDict):
    r"""Accounts observed in retained assessments, newest seen first, with each account once per page and across pages. Counts and keyset pagination are computed over distinct accounts in one database snapshot per page. Live data can change between pages."""

    items: List[AccountDirectoryPageItemTypedDict]
    total: int
    r"""Distinct accounts matching the filters, exact below 10000 and capped at 10000."""
    total_capped: bool
    r"""True when at least 10000 accounts match."""
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    next_cursor: NotRequired[str]
    r"""Opaque, expiring cursor bound to this environment, operation and every filter. Keep the filters unchanged."""


class AccountDirectoryPage(BaseModel):
    r"""Accounts observed in retained assessments, newest seen first, with each account once per page and across pages. Counts and keyset pagination are computed over distinct accounts in one database snapshot per page. Live data can change between pages."""

    items: List[AccountDirectoryPageItem]

    total: int
    r"""Distinct accounts matching the filters, exact below 10000 and capped at 10000."""

    total_capped: bool
    r"""True when at least 10000 accounts match."""

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    next_cursor: Optional[str] = None
    r"""Opaque, expiring cursor bound to this environment, operation and every filter. Keep the filters unchanged."""

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
    AccountDirectoryPage.model_rebuild()
except NameError:
    pass
