# IncompleteReason

Why a lane did not settle. deferred means the lane is asynchronous and still running; a continuation settles it. timed_out means the lane missed its deadline. insufficient_evidence is a settled inconclusive signal rather than an incomplete lane.

## Example Usage

```python
from noresponse.models.shared import IncompleteReason

# Open enum: unrecognized values are captured as UnrecognizedStr
value: IncompleteReason = "timed_out"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"timed_out"`
- `"rate_limited"`
- `"blocked"`
- `"source_error"`
- `"unavailable"`
- `"deferred"`
