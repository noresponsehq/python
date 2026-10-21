# BreachSelector

The submitted identifier a breach table matched on: email or username. Phone and name are not breach selectors.

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
