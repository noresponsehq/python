# WebhookTestRequestEvent

endpoint.verification sends a fresh challenge now, in this call, and the endpoint is verified if it echoes it. assessment.updated queues an event whose data is a fixed example assessment, with test true, delivered and retried like any other; the endpoint must be verified.

## Example Usage

```python
from noresponse.models.shared import WebhookTestRequestEvent

# Open enum: unrecognized values are captured as UnrecognizedStr
value: WebhookTestRequestEvent = "endpoint.verification"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"endpoint.verification"`
- `"assessment.updated"`
