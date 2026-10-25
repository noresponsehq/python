# KeyStatus

active: the key authenticates. expired: a rotation's overlap window has ended (expires_at). revoked: the key was revoked (revoked_at) and answers 401.

## Example Usage

```python
from noresponse.models.shared import KeyStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: KeyStatus = "active"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"active"`
- `"expired"`
- `"revoked"`
