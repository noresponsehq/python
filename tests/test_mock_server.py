"""Smoke test of the generated client against the mock server.

Skipped unless NORESPONSE_MOCK_URL names a running mock server
(`generate_sdks.py mockserver --serve`). The mock server answers with the
examples in the SDK document, so this proves the client's wiring (URL, auth
header, request encoding, response parsing) and nothing about the live API.
"""
import asyncio
import os

import pytest

from noresponse import NoResponse

MOCK_URL = os.environ.get("NORESPONSE_MOCK_URL")
pytestmark = pytest.mark.skipif(not MOCK_URL, reason="set NORESPONSE_MOCK_URL to a running mock server")


def client() -> NoResponse:
    return NoResponse(api_key="nrk_mock_" + "k" * 20, server_url=MOCK_URL)


def test_create_returns_the_documented_assessment():
    with client() as sdk:
        res = sdk.assessments.create(
            idempotency_key="mock-server-smoke-0001",
            account_id="acct_7f3a9c",
            identifiers={"email": "new.user@example.com"},
        )
    assert res.result.assessment_id.startswith("asm_")
    assert res.result.account_id == "acct_7f3a9c"


def test_get_returns_the_documented_assessment():
    with client() as sdk:
        res = sdk.assessments.get("asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM")
    assert res.result.assessment_id.startswith("asm_")


def test_async_create():
    async def create():
        async with client() as sdk:
            return await sdk.assessments.create_async(
                idempotency_key="mock-server-smoke-0002",
                account_id="acct_7f3a9c",
                identifiers={"email": "new.user@example.com"},
            )

    assert asyncio.run(create()).result.assessment_id.startswith("asm_")
