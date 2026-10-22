"""Run the shared issued-credential vectors through the hash helper."""

import json
from pathlib import Path

import pytest

from noresponse import hash_issued_credential

CASES = json.loads((Path(__file__).parent / "fixtures" / "issued-credential-vectors.json").read_text(encoding="utf-8"))["cases"]


@pytest.mark.parametrize("case", CASES, ids=[c["sha256"][:8] for c in CASES])
def test_vector(case):
    assert hash_issued_credential(case["key"]) == case["sha256"]


def test_empty_key_is_refused():
    with pytest.raises(ValueError):
        hash_issued_credential("")
