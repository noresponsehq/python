# Bucket

The period each count covers, in UTC; a week starts on Monday.

## Example Usage

```python
from noresponse.models.shared import Bucket

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Bucket = "hour"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"hour"`
- `"day"`
- `"week"`
