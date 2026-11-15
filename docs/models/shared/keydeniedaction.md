# KeyDeniedAction

## Example Usage

```python
from noresponse.models.shared import KeyDeniedAction

# Open enum: unrecognized values are captured as UnrecognizedStr
value: KeyDeniedAction = "evidence.read"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"evidence.read"`
- `"exports.read"`
- `"policy.publish"`
