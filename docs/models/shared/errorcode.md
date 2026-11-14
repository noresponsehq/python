# ErrorCode

Why a failed search found nothing: its sources did not answer, none could be asked, or it could not run before its attempts were spent.

## Example Usage

```python
from noresponse.models.shared import ErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ErrorCode = "not_answered"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"not_answered"`
- `"no_source"`
- `"worker_attempts_exhausted"`
