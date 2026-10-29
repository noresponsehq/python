from __future__ import annotations
from .filter_ import Filter, FilterTypedDict
from .ownertype import OwnerType
from noresponse.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class ReviewViewTypedDict(TypedDict):
    id: str
    name: str
    owner: str
    owner_type: OwnerType
    r"""The credential namespace of the creator. An external user ID equal to an API-key label does not grant ownership of that key's private view."""
    shared: bool
    version: int
    filter_: FilterTypedDict
    created_at: str
    updated_at: str
    owner_principal_id: str
    r"""Immutable member ID or API key ID, interpreted with owner_type. Ownership survives changes to an external user identity."""


class ReviewView(BaseModel):
    id: str

    name: str

    owner: str

    owner_type: OwnerType
    r"""The credential namespace of the creator. An external user ID equal to an API-key label does not grant ownership of that key's private view."""

    shared: bool

    version: int

    filter_: Annotated[Filter, pydantic.Field(alias="filter")]

    created_at: str

    updated_at: str

    owner_principal_id: str
    r"""Immutable member ID or API key ID, interpreted with owner_type. Ownership survives changes to an external user identity."""


try:
    ReviewView.model_rebuild()
except NameError:
    pass
