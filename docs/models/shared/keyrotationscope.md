# KeyRotationScope

## Example Usage

```python
from noresponse.models.shared import KeyRotationScope

# Open enum: unrecognized values are captured as UnrecognizedStr
value: KeyRotationScope = "assess"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"assess"`
- `"history"`
- `"delete"`
- `"webhooks"`
- `"detailed"`
- `"integrations"`
- `"management"`
