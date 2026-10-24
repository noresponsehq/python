"""The shared late enforcement vectors through handle_risk_change, plus what the
vectors cannot say in JSON: verification and the custom provider."""

import hashlib
import hmac
import json
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import parse_qsl, urlsplit

import httpx
import pytest

from noresponse import (
    AccountStateAnswer,
    FlowPolicy,
    NoResponse,
    ProviderActionError,
    WebhookVerificationError,
    custom_provider,
    enforce_account,
    handle_risk_change,
    identity_provider,
)

VECTORS = json.loads((Path(__file__).parent / "fixtures" / "late-results-vectors.json").read_text())
SECRETS = {VECTORS["key_id"]: VECTORS["secret_utf8"]}


def sign(event):
    raw = json.dumps(event).encode("utf-8")
    stamp = str(VECTORS["now"])
    digest = hmac.new(VECTORS["secret_utf8"].encode(), stamp.encode() + b"." + raw, hashlib.sha256).hexdigest()
    headers = {
        "NR-Webhook-Id": event["id"],
        "NR-Webhook-Timestamp": stamp,
        "NR-Webhook-Key-Id": VECTORS["key_id"],
        "NR-Webhook-Signature": "v1=" + digest,
    }
    return raw, headers


def normalize(method, url):
    """Method, path and query as an order-free set of decoded pairs."""
    parts = urlsplit(str(url))
    query = sorted(f"{k}={v}" for k, v in parse_qsl(parts.query, keep_blank_values=True))
    return f"{method} {parts.scheme}://{parts.netloc}{parts.path}?{'&'.join(query)}"


class Transcript:
    """An httpx transport that serves the case's exchanges in order and fails on anything else."""

    def __init__(self, exchanges):
        self.exchanges = exchanges
        self.next = 0

    def __call__(self, request):
        got = normalize(request.method, request.url)
        assert self.next < len(self.exchanges), f"unexpected request {got}"
        expected = self.exchanges[self.next]
        assert got == normalize(expected["request"]["method"], expected["request"]["url"]), f"request {self.next}"
        if "body" in expected["request"]:
            assert json.loads(request.content) == expected["request"]["body"], f"body of request {self.next}"
        self.next += 1
        response = expected["response"]
        body = response.get("body")
        content = b"" if body is None or response["status"] == 204 else json.dumps(body).encode()
        return httpx.Response(response["status"], headers=response.get("headers", {}), content=content)

    def done(self):
        assert self.next == len(self.exchanges), "every exchange was requested"


def client_for(transcript):
    http = httpx.Client(transport=httpx.MockTransport(transcript))
    return NoResponse(VECTORS["api_key"], server_url=VECTORS["api_base_url"], client=http), http


@pytest.mark.parametrize("vector", VECTORS["cases"], ids=[c["name"] for c in VECTORS["cases"]])
def test_vector(vector):
    transcript = Transcript(vector["exchanges"])
    client, http = client_for(transcript)
    provider = identity_provider(vector["provider"], token=VECTORS["provider_token"], domain=vector.get("domain"), http=http)
    raw, headers = sign(vector["event"])

    def get_account_state(account):
        assert account.id == vector["event"]["data"]["account"]["id"]
        state = vector["state"]
        if state is None:
            return None
        return AccountStateAnswer(state["state"], state.get("user_id"), state.get("enforced_risk_version"))

    flows = {flow: FlowPolicy(**policy) for flow, policy in (vector.get("flows") or {}).items()}
    if vector["error"]:
        with pytest.raises(ProviderActionError) as caught:
            handle_risk_change(client, raw, headers, SECRETS, provider=provider, get_account_state=get_account_state,
                               flows=flows, now=VECTORS["now"])
        transcript.done()
        assert {"provider": caught.value.provider, "status": caught.value.status, "code": caught.value.code} == vector["error"]
        return
    result = handle_risk_change(client, raw, headers, SECRETS, provider=provider, get_account_state=get_account_state,
                                flows=flows, now=VECTORS["now"])
    transcript.done()
    assert result.skipped == vector["result"]["skipped"]
    enforcements = [
        {"flow": e.flow, "action": e.action, "status": e.status, **({"error_code": e.error_code} if e.error_code else {})}
        for e in result.enforcements
    ]
    assert enforcements == vector["result"]["enforcements"]


def test_a_delivery_that_fails_verification_reads_and_acts_on_nothing():
    transcript = Transcript([])
    client, _ = client_for(transcript)
    raw, headers = sign(VECTORS["cases"][0]["event"])
    with pytest.raises(WebhookVerificationError):
        handle_risk_change(client, raw + b" ", headers, SECRETS, provider=custom_provider({}),
                           get_account_state=lambda account: pytest.fail("not called"), now=VECTORS["now"])
    transcript.done()


def test_a_custom_provider_runs_your_functions_and_a_missing_one_fails_the_action():
    decisions = SimpleNamespace(account_creation="block", login="block", purchase="block")
    account = SimpleNamespace(id="acct_7f3a9c", risk_version=9, decisions_by_flow=decisions)
    recorded = []
    client = SimpleNamespace(accounts=SimpleNamespace(record_enforcement=lambda account_id, **body: recorded.append(body)))
    ran = []
    # A return value that is not a list of actions (True here) is no extra action.
    provider = custom_provider({"restrict": lambda user_id: ran.append(("restrict", user_id)) or True})
    with pytest.raises(ValueError):
        enforce_account(client, account, provider=provider, get_account_state=lambda a: AccountStateAnswer("active", "u_1"))
    assert ran == [("restrict", "u_1")]
    assert [(b["action"], b["status"], b["error_code"], b["provider"]) for b in recorded] == [
        ("restrict", "applied", None, "custom"),
        ("revoke_sessions", "failed", "custom.error", "custom"),
    ]


def test_identity_provider_needs_its_credentials():
    with pytest.raises(ValueError):
        identity_provider("clerk", token="")
    with pytest.raises(ValueError):
        identity_provider("auth0", token="t")
    with pytest.raises(ValueError):
        identity_provider("okta", token="t")
