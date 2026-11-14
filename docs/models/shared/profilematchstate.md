# ProfileMatchState

How sure the screening is that a profile is the person's, from its evidence: confirmed is a handle on the person row, or two or more hard identifiers (email, phone, a supplied handle, or a fact an existing source returned); probable is one identifier beyond the name; possible is the name alone.

## Example Usage

```python
from noresponse.models.shared import ProfileMatchState

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ProfileMatchState = "confirmed"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"confirmed"`
- `"probable"`
- `"possible"`
