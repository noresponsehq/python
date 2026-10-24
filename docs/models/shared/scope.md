# Scope

## Example Usage

```python
from noresponse.models.shared import Scope

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Scope = "assess"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"assess"`
- `"history"`
- `"delete"`
- `"webhooks"`
- `"detailed"`
- `"integrations"`
