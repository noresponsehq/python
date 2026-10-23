# Depth

How long the synchronous answer waits for sources. quick waits only for the fast sources, those that answer within 500 ms of ingress (or deadline_ms when lower); full waits for the whole budget, up to 3000 ms. Sources still running at the cut continue asynchronously and update the assessment either way.

## Example Usage

```python
from noresponse.models.shared import Depth

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Depth = "quick"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"quick"`
- `"full"`
