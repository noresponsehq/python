# FindingCategory

What a finding is about: a direct threat to the principal or the event, intent to harm without a named target, fixation on the principal, a grievance against the host, research into the venue, route or security, weapons tied to any of these, disruption or protest planning toward this event, violent extremist content or identification, prior harassment or stalking of staff or principals, or posting the principal's addresses or movements.

## Example Usage

```python
from noresponse.models.shared import FindingCategory

# Open enum: unrecognized values are captured as UnrecognizedStr
value: FindingCategory = "direct_threat"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"direct_threat"`
- `"harm_intent"`
- `"fixation"`
- `"grievance"`
- `"security_research"`
- `"weapons"`
- `"disruption"`
- `"violent_extremism"`
- `"harassment"`
- `"movement_exposure"`
