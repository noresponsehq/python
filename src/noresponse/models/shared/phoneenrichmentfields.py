from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Any, List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


class AlternateNameTypedDict(TypedDict):
    pass


class AlternateName(BaseModel):
    pass


AlternateNameUnionTypedDict = TypeAliasType(
    "AlternateNameUnionTypedDict",
    Union[AlternateNameTypedDict, str, float, bool, List[Any]],
)


AlternateNameUnion = TypeAliasType(
    "AlternateNameUnion", Union[AlternateName, str, float, bool, List[Any]]
)


class NameCandidateTypedDict(TypedDict):
    pass


class NameCandidate(BaseModel):
    pass


NameCandidateUnionTypedDict = TypeAliasType(
    "NameCandidateUnionTypedDict",
    Union[NameCandidateTypedDict, str, float, bool, List[Any]],
)


NameCandidateUnion = TypeAliasType(
    "NameCandidateUnion", Union[NameCandidate, str, float, bool, List[Any]]
)


class TimezoneTypedDict(TypedDict):
    pass


class Timezone(BaseModel):
    pass


TimezoneUnionTypedDict = TypeAliasType(
    "TimezoneUnionTypedDict", Union[TimezoneTypedDict, str, float, bool, List[Any]]
)


TimezoneUnion = TypeAliasType(
    "TimezoneUnion", Union[Timezone, str, float, bool, List[Any]]
)


class EmailTypedDict(TypedDict):
    pass


class Email(BaseModel):
    pass


EmailUnionTypedDict = TypeAliasType(
    "EmailUnionTypedDict", Union[EmailTypedDict, str, float, bool, List[Any]]
)


EmailUnion = TypeAliasType("EmailUnion", Union[Email, str, float, bool, List[Any]])


class WebsiteTypedDict(TypedDict):
    pass


class Website(BaseModel):
    pass


WebsiteUnionTypedDict = TypeAliasType(
    "WebsiteUnionTypedDict", Union[WebsiteTypedDict, str, float, bool, List[Any]]
)


WebsiteUnion = TypeAliasType(
    "WebsiteUnion", Union[Website, str, float, bool, List[Any]]
)


class LocationTypedDict(TypedDict):
    pass


class Location(BaseModel):
    pass


LocationUnionTypedDict = TypeAliasType(
    "LocationUnionTypedDict", Union[LocationTypedDict, str, float, bool, List[Any]]
)


LocationUnion = TypeAliasType(
    "LocationUnion", Union[Location, str, float, bool, List[Any]]
)


class SocialProfileTypedDict(TypedDict):
    pass


class SocialProfile(BaseModel):
    pass


SocialProfileUnionTypedDict = TypeAliasType(
    "SocialProfileUnionTypedDict",
    Union[SocialProfileTypedDict, str, float, bool, List[Any]],
)


SocialProfileUnion = TypeAliasType(
    "SocialProfileUnion", Union[SocialProfile, str, float, bool, List[Any]]
)


class PhoneEnrichmentFieldsTypedDict(TypedDict):
    phone: NotRequired[str]
    name: NotRequired[str]
    carrier: NotRequired[str]
    line_type: NotRequired[str]
    entity_type: NotRequired[str]
    country_code: NotRequired[str]
    country: NotRequired[str]
    state: NotRequired[str]
    city: NotRequired[str]
    location: NotRequired[str]
    national_format: NotRequired[str]
    job_title: NotRequired[str]
    company_name: NotRequired[str]
    email: NotRequired[str]
    website: NotRequired[str]
    first_call_at: NotRequired[str]
    last_call_at: NotRequired[str]
    matched_name: NotRequired[str]
    alternate_names: NotRequired[List[AlternateNameUnionTypedDict]]
    name_candidates: NotRequired[List[NameCandidateUnionTypedDict]]
    timezones: NotRequired[List[TimezoneUnionTypedDict]]
    emails: NotRequired[List[EmailUnionTypedDict]]
    websites: NotRequired[List[WebsiteUnionTypedDict]]
    locations: NotRequired[List[LocationUnionTypedDict]]
    social_profiles: NotRequired[List[SocialProfileUnionTypedDict]]
    report_count: NotRequired[int]
    tag_count: NotRequired[int]
    total_calls: NotRequired[int]
    calls_60_days: NotRequired[int]
    reports_60_days: NotRequired[int]
    searches_60_days: NotRequired[int]
    comment_count: NotRequired[int]
    names_count: NotRequired[int]
    spam_report_count: NotRequired[int]


class PhoneEnrichmentFields(BaseModel):
    phone: Optional[str] = None

    name: Optional[str] = None

    carrier: Optional[str] = None

    line_type: Optional[str] = None

    entity_type: Optional[str] = None

    country_code: Optional[str] = None

    country: Optional[str] = None

    state: Optional[str] = None

    city: Optional[str] = None

    location: Optional[str] = None

    national_format: Optional[str] = None

    job_title: Optional[str] = None

    company_name: Optional[str] = None

    email: Optional[str] = None

    website: Optional[str] = None

    first_call_at: Optional[str] = None

    last_call_at: Optional[str] = None

    matched_name: Optional[str] = None

    alternate_names: Optional[List[AlternateNameUnion]] = None

    name_candidates: Optional[List[NameCandidateUnion]] = None

    timezones: Optional[List[TimezoneUnion]] = None

    emails: Optional[List[EmailUnion]] = None

    websites: Optional[List[WebsiteUnion]] = None

    locations: Optional[List[LocationUnion]] = None

    social_profiles: Optional[List[SocialProfileUnion]] = None

    report_count: Optional[int] = None

    tag_count: Optional[int] = None

    total_calls: Optional[int] = None

    calls_60_days: Optional[int] = None

    reports_60_days: Optional[int] = None

    searches_60_days: Optional[int] = None

    comment_count: Optional[int] = None

    names_count: Optional[int] = None

    spam_report_count: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "phone",
                "name",
                "carrier",
                "line_type",
                "entity_type",
                "country_code",
                "country",
                "state",
                "city",
                "location",
                "national_format",
                "job_title",
                "company_name",
                "email",
                "website",
                "first_call_at",
                "last_call_at",
                "matched_name",
                "alternate_names",
                "name_candidates",
                "timezones",
                "emails",
                "websites",
                "locations",
                "social_profiles",
                "report_count",
                "tag_count",
                "total_calls",
                "calls_60_days",
                "reports_60_days",
                "searches_60_days",
                "comment_count",
                "names_count",
                "spam_report_count",
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
