from __future__ import annotations
from .keyenvironment import KeyEnvironment
from .settingsflows import SettingsFlows, SettingsFlowsTypedDict
from .sourceid import SourceID
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class SettingsTypedDict(TypedDict):
    r"""One environment's settings: how long its assessments are kept, and for each flow the risk thresholds that decide it and the depth a request that names none is served at, the sources it refuses, and the daily cap on screening spend. Live and test each have their own. A flow without thresholds of its own uses account_creation's (inherits_account_creation). Every change is recorded in the audit log as settings.updated, with who made it."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""
    retention_days: int
    r"""Days an assessment is kept after it is created, 1 to 365 (default 365). Shortening hides older assessments at once."""
    policy_version: int
    r"""The monotonic settings configuration epoch, including retention changes. Zero while defaults apply. Historical assessments keep their frozen policy version; the active version reaches new assessments within a minute."""
    flows: SettingsFlowsTypedDict
    refused_sources: List[SourceID]
    r"""The sources this environment refuses, sorted; empty, the default, refuses none. An assessment leaves a refused source out: its coverage is missing (an identifier with no other source lists coverage-unavailable as unavailable) rather than not_found, and a stored result of a refused source is not reused."""
    screening_daily_cap: Nullable[int]
    r"""The most the environment's screenings may spend in one UTC day, in minor units of USD (cents), 0 to 100000000; null is no cap. Default 50000. A screening whose estimated_spend exceeds the cap less the day's recorded spend and what open screenings may still spend answers 409 screening_cap_exceeded."""
    updated_by: NotRequired[str]
    r"""Who last changed the policy: the member's external user id for a change made through the console, the prefix (nrk_<environment>_<key id>) of the management key that made it, or NoResponse. Absent while the defaults apply."""
    updated_at: NotRequired[str]
    r"""When the policy last changed. Absent while the defaults apply."""


class Settings(BaseModel):
    r"""One environment's settings: how long its assessments are kept, and for each flow the risk thresholds that decide it and the depth a request that names none is served at, the sources it refuses, and the daily cap on screening spend. Live and test each have their own. A flow without thresholds of its own uses account_creation's (inherits_account_creation). Every change is recorded in the audit log as settings.updated, with who made it."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""

    retention_days: int
    r"""Days an assessment is kept after it is created, 1 to 365 (default 365). Shortening hides older assessments at once."""

    policy_version: int
    r"""The monotonic settings configuration epoch, including retention changes. Zero while defaults apply. Historical assessments keep their frozen policy version; the active version reaches new assessments within a minute."""

    flows: SettingsFlows

    refused_sources: List[SourceID]
    r"""The sources this environment refuses, sorted; empty, the default, refuses none. An assessment leaves a refused source out: its coverage is missing (an identifier with no other source lists coverage-unavailable as unavailable) rather than not_found, and a stored result of a refused source is not reused."""

    screening_daily_cap: Nullable[int]
    r"""The most the environment's screenings may spend in one UTC day, in minor units of USD (cents), 0 to 100000000; null is no cap. Default 50000. A screening whose estimated_spend exceeds the cap less the day's recorded spend and what open screenings may still spend answers 409 screening_cap_exceeded."""

    updated_by: Optional[str] = None
    r"""Who last changed the policy: the member's external user id for a change made through the console, the prefix (nrk_<environment>_<key id>) of the management key that made it, or NoResponse. Absent while the defaults apply."""

    updated_at: Optional[str] = None
    r"""When the policy last changed. Absent while the defaults apply."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["updated_by", "updated_at"])
        nullable_fields = set(["screening_daily_cap"])
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
