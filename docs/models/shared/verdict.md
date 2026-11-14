# Verdict

A reviewer's overrule (POST .../people/{person_id}/records), which decides joined whatever the likelihood and sticks for as long as a lookup finds the same record. Absent when nobody overruled it.

## Example Usage

```python
from noresponse.models.shared import Verdict

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Verdict = "joined"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"joined"`
- `"rejected"`
