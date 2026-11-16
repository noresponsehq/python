# WrittenProfileErrorCode

Present only when status is failed. no_writer: no profile writer serves this environment. refused: the model refused. not_written: the answer was not a profile, or no statement survived grounding. uncited_statement: a statement or lead cited a record the person does not hold. not_answered: the writer did not answer. worker_attempts_exhausted: the worker stopped retrying.

## Example Usage

```python
from noresponse.models.shared import WrittenProfileErrorCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: WrittenProfileErrorCode = "no_writer"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"no_writer"`
- `"refused"`
- `"not_written"`
- `"uncited_statement"`
- `"not_answered"`
- `"worker_attempts_exhausted"`
