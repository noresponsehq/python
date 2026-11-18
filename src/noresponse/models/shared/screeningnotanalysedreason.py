from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


ScreeningNotAnalysedReason = Union[
    Literal[
        "video",
        "image_unavailable",
        "image_unsupported",
        "image_limit",
        "refused",
        "unfinished",
        "unverified",
        "unspecified",
        "analysis_off",
    ],
    UnrecognizedStr,
]
r"""Why an item read was not analysed. video: a video with no cover frame the analyser could read, whose caption alone is read. image_unavailable: the image could not be fetched from the platform. image_unsupported: not a JPEG, PNG, GIF or WebP image, or too large to send. image_limit: past the most images one person's analysis reads. refused: the model declined to read it. unfinished: the model cut its batch short or answered outside the schema, or the request was rejected. unverified: a finding cited it with words it does not contain or an image it did not describe. unspecified: the analyser gave no reason. analysis_off: no analyser is switched on, so the investigation found, read and typed everything without AI and analysed nothing."""
