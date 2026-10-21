# AuthenticationErrorCode

Machine codes an HTTP 401 answer can carry.

## Example Usage

```python
from noresponse.models.shared import AuthenticationErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuthenticationErrorCode = "unauthorized"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"unauthorized"`
