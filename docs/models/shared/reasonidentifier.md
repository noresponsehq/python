# ReasonIdentifier

The submitted identifier or client context field a reason concerns; absent when it concerns the whole assessment. Client context is a claimed hint, not a device fingerprint.

## Example Usage

```python
from noresponse.models.shared import ReasonIdentifier

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ReasonIdentifier = "email"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"email"`
- `"username"`
- `"phone"`
- `"name"`
- `"ip"`
- `"context"`
