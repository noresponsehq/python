# PersonBatchItemOutcome

unchanged: the row matched a person with the same details.

## Example Usage

```python
from noresponse.models.shared import PersonBatchItemOutcome

# Open enum: unrecognized values are captured as UnrecognizedStr
value: PersonBatchItemOutcome = "created"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"created"`
- `"updated"`
- `"unchanged"`
