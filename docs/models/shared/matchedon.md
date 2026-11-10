# MatchedOn

## Example Usage

```python
from noresponse.models.shared import MatchedOn

# Open enum: unrecognized values are captured as UnrecognizedStr
value: MatchedOn = "email"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"email"`
- `"phone"`
- `"external_id"`
