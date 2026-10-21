# PermissionDeniedErrorCode

Machine codes an HTTP 403 answer can carry.

## Example Usage

```python
from noresponse.models.shared import PermissionDeniedErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PermissionDeniedErrorCode = "tenant_forbidden"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"tenant_forbidden"`
