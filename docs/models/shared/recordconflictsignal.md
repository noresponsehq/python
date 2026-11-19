# RecordConflictSignal

anchors_disagree: records found by two of the identifiers you gave clash with each other, so those identifiers may belong to different people.

## Example Usage

```python
from noresponse.models.shared import RecordConflictSignal

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RecordConflictSignal = "anchors_disagree"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"anchors_disagree"`
