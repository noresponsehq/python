# GroupType

What the group's people share: an event, an organisation, a place or another attribute.

## Example Usage

```python
from noresponse.models.shared import GroupType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: GroupType = "event"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"event"`
- `"organisation"`
- `"place"`
- `"custom"`
