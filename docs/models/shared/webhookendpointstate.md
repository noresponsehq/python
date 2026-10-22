# WebhookEndpointState

unverified until the endpoint echoes an endpoint.verification challenge (send one with POST /v1/webhooks/{endpoint_id}/test); verified receives assessment.updated events; disabled after 72 hours of continuous delivery failure, and verified again by the same challenge.

## Example Usage

```python
from noresponse.models.shared import WebhookEndpointState

# Open enum: unrecognized values are captured as UnrecognizedStr
value: WebhookEndpointState = "unverified"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"unverified"`
- `"verified"`
- `"disabled"`
