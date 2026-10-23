# WebhookDeliveryAttemptStatus

delivered when the endpoint answered 2xx; failed otherwise, with failure naming why.

## Example Usage

```python
from noresponse.models.shared import WebhookDeliveryAttemptStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: WebhookDeliveryAttemptStatus = "delivered"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"delivered"`
- `"failed"`
