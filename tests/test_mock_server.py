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
            flow="signup",
            identifiers={"email": "new.user@example.com"},
        )
    assert res.id.startswith("asm_")
    assert res.detail.account_id == "acct_7f3a9c"


def test_get_returns_the_documented_assessment():
    with client() as sdk:
        res = sdk.assessments.get("asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM")
    assert res.id.startswith("asm_") and res.detail.assessment_id == res.id


def test_accounts_return_the_documented_account_and_page():
    with client() as sdk:
        account = sdk.accounts.get("acct_7f3a9c")
        page = sdk.accounts.list_assessments("acct_7f3a9c", limit=20)
    assert account.id == "acct_7f3a9c" and account.assessment_id.startswith("asm_")
    assert account.decisions_by_flow.signup == account.risk.decision
    assert page.account_id == "acct_7f3a9c"
    with client() as sdk:
        deletion = sdk.accounts.delete("acct_7f3a9c")
    assert deletion.id == "acct_7f3a9c" and deletion.deleted is True
    with client() as sdk:
        removed = sdk.assessments.delete("asm_01JA2Z8K6Q4V7W9XBCDEFGHJKM")
    assert removed.id.startswith("asm_") and removed.deleted is True and removed.account.id == "acct_7f3a9c"


def test_async_create():
    async def create():
        async with client() as sdk:
            return await sdk.assessments.create_async(
                idempotency_key="mock-server-smoke-0002",
                account_id="acct_7f3a9c",
                flow="signup",
                identifiers={"email": "new.user@example.com"},
            )

    assert asyncio.run(create()).id.startswith("asm_")
