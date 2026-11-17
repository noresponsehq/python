# SuggestedSearchKind

The kind of the value: one of the kinds the environment's enrichment setting names.

## Example Usage

```python
from noresponse.models.shared import SuggestedSearchKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SuggestedSearchKind = "username"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"username"`
- `"email"`
- `"phone"`
