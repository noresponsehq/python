from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class PublicationTypedDict(TypedDict):
    r"""Immutable publication provenance remains in policy history after evaluation evidence expires. SHA-256 values identify the frozen manifest, evaluator semantic input, cohort, and canonical result separately."""

    manifest_sha256: str
    input_sha256: str
    cohort_sha256: str
    result_sha256: str
    evaluator_sha256: str
    evaluation_id: str
    build_version: str
    captured_at: str
    published_at: str
    evaluator_version: Literal["identity-threshold-evaluator-v2"]


class Publication(BaseModel):
    r"""Immutable publication provenance remains in policy history after evaluation evidence expires. SHA-256 values identify the frozen manifest, evaluator semantic input, cohort, and canonical result separately."""

    manifest_sha256: str

    input_sha256: str

    cohort_sha256: str

    result_sha256: str

    evaluator_sha256: str

    evaluation_id: str

    build_version: str

    captured_at: str

    published_at: str

    evaluator_version: Annotated[
        Annotated[
            Literal["identity-threshold-evaluator-v2"],
            AfterValidator(validate_const("identity-threshold-evaluator-v2")),
        ],
        pydantic.Field(alias="evaluator_version"),
    ] = "identity-threshold-evaluator-v2"


try:
    Publication.model_rebuild()
except NameError:
    pass
