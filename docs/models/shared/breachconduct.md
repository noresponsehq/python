# BreachConduct

What a breach table's rows record against the identifier: chargeback, one or more chargebacks; declined_payment, one or more declined payments; forum_sanction, a forum ban, warning or infraction. A category and not a value: the schema has no member for one.

## Example Usage

```python
from noresponse.models.shared import BreachConduct

# Open enum: unrecognized values are captured as UnrecognizedStr
value: BreachConduct = "chargeback"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"chargeback"`
- `"declined_payment"`
- `"forum_sanction"`
