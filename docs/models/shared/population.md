# Population

first_answers uses anonymous counters that can include erased detail. retained_first_answers computes exact intersections over retained first answers within 31 days. Requests exceeding the 100000-record work budget are refused.

## Example Usage

```python
from noresponse.models.shared import Population

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Population = "first_answers"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"first_answers"`
- `"retained_first_answers"`
