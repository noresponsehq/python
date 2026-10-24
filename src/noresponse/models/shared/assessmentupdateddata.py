from __future__ import annotations
from .assessment import Assessment, AssessmentTypedDict
from .assessmentexpired import AssessmentExpired, AssessmentExpiredTypedDict
from noresponse.utils import get_discriminator
from pydantic import Discriminator, Tag
from typing import Union
from typing_extensions import Annotated, TypeAliasType


AssessmentUpdatedDataTypedDict = TypeAliasType(
    "AssessmentUpdatedDataTypedDict",
    Union[AssessmentExpiredTypedDict, AssessmentTypedDict],
)
r"""The assessment, or the minimal notice that it expired."""


AssessmentUpdatedData = Annotated[
    Union[
        Annotated[Assessment, Tag("complete")],
        Annotated[Assessment, Tag("partial")],
        Annotated[Assessment, Tag("pending")],
        Annotated[AssessmentExpired, Tag("expired")],
    ],
    Discriminator(lambda m: get_discriminator(m, "status", "status")),
]
r"""The assessment, or the minimal notice that it expired."""
