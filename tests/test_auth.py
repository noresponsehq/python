"""Run the shared auth-context vectors through the Python adapters."""

import json
from pathlib import Path

import pytest

from noresponse import from_auth0, from_clerk, from_oidc, from_workos
from noresponse.auth import _MAP

FIXTURES = Path(__file__).parent / "fixtures"
VECTORS = json.loads((FIXTURES / "auth-context-vectors.json").read_text())["cases"]
MAPPERS = {"workos": from_workos, "clerk": from_clerk, "auth0": from_auth0}


def run(vector):
    mapper = MAPPERS.get(vector["provider"])
    if mapper:
        return mapper(vector["claims"], vector["overrides"])
    return from_oidc(vector["provider"], vector["claims"], vector["overrides"])


@pytest.mark.parametrize("vector", VECTORS, ids=[v["name"] for v in VECTORS])
def test_vector(vector):
    if vector.get("error"):
        with pytest.raises(ValueError):
            run(vector)
        return
    got = json.loads(run(vector).model_dump_json(exclude_none=True))
    assert got == vector["expect"]


def test_embedded_map_is_the_contract_map():
    table = json.loads((FIXTURES / "auth-context-claim-map.json").read_text())
    for key in ("description", "rules"):
        table.pop(key)
    for provider in table["providers"].values():
        provider.pop("notes", None)
    assert _MAP == table
