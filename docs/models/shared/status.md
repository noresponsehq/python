# Status

Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered.

## Example Usage

```python
from noresponse.models.shared import Status

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Status = "complete"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"complete"`
- `"partial"`
- `"pending"`
