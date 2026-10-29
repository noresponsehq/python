# MemberDeniedAction

## Example Usage

```python
from noresponse.models.shared import MemberDeniedAction

# Open enum: unrecognized values are captured as UnrecognizedStr
value: MemberDeniedAction = "evidence.read"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"evidence.read"`
- `"exports.read"`
- `"policy.publish"`
