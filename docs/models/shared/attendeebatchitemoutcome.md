# AttendeeBatchItemOutcome

unchanged: the row matched an attendee with the same details.

## Example Usage

```python
from noresponse.models.shared import AttendeeBatchItemOutcome

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AttendeeBatchItemOutcome = "created"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"created"`
- `"updated"`
- `"unchanged"`
