# IdentifierKind

Which submitted identifier a signal concerns. ip is a selector of breach_exposure only.

## Example Usage

```python
from noresponse.models.shared import IdentifierKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: IdentifierKind = "email"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"email"`
- `"username"`
- `"phone"`
- `"ip"`
