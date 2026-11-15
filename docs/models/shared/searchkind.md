# SearchKind

The kind of the value searched. A domain search finds the leaked rows of every email address at the domain.

## Example Usage

```python
from noresponse.models.shared import SearchKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SearchKind = "email"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"email"`
- `"phone"`
- `"username"`
- `"person_name"`
- `"password"`
- `"hash"`
- `"ip"`
- `"domain"`
