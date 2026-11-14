# PersonRole

The person's role in the group: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: a person without one has no role, not guest. A later row naming the same person replaces it, and a change of role alone keeps the person's screening results.

## Example Usage

```python
from noresponse.models.shared import PersonRole

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PersonRole = "guest"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"guest"`
- `"crew"`
- `"vendor"`
- `"press"`
