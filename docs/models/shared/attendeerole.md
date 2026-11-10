# AttendeeRole

The attendee's role at the event: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: an attendee without one has no role, not guest. A later row naming the same attendee replaces it, and a change of role alone keeps the attendee's screening results.

## Example Usage

```python
from noresponse.models.shared import AttendeeRole

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AttendeeRole = "guest"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"guest"`
- `"crew"`
- `"vendor"`
- `"press"`
