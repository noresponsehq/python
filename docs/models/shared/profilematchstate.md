# ProfileMatchState

How sure the screening is that a profile is the person's, from the likelihood its record scores. Confirmed reaches the join bar of 0.9. Probable reaches 0.85, which takes a shared value beyond the one that found the account. Possible is the rest.

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
