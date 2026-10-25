# BreachSelector

The submitted email or username whose own search matched the table. A submitted full name is searched as well, and what it finds feeds the identity's reasons rather than this list.

## Example Usage

```python
from noresponse.models.shared import BreachSelector

# Open enum: unrecognized values are captured as UnrecognizedStr
value: BreachSelector = "email"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"email"`
- `"username"`
- `"ip"`
