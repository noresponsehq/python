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
    r"""Distinct observed accounts with retained assessments. Typed identifier searches use stable opaque account order, independent of newly submitted assessments; ordinary and legacy email searches use newest-seen order. One repeatable-read database snapshot supplies each page's rows and totals. Pages do not share a snapshot: new matching accounts may appear on a later page or before the cursor and be missed until a fresh search; retention, erasure and changed membership can remove results. Current account decisions are read separately and may advance during a page. Cursors bind the workspace/environment, operation and filters, expire, and cannot cross scopes. Erasure and retention always take precedence over pagination."""

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
    r"""Distinct observed accounts with retained assessments. Typed identifier searches use stable opaque account order, independent of newly submitted assessments; ordinary and legacy email searches use newest-seen order. One repeatable-read database snapshot supplies each page's rows and totals. Pages do not share a snapshot: new matching accounts may appear on a later page or before the cursor and be missed until a fresh search; retention, erasure and changed membership can remove results. Current account decisions are read separately and may advance during a page. Cursors bind the workspace/environment, operation and filters, expire, and cannot cross scopes. Erasure and retention always take precedence over pagination."""

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
