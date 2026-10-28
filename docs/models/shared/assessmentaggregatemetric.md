# AssessmentAggregateMetric

## Example Usage

```python
from noresponse.models.shared import AssessmentAggregateMetric

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AssessmentAggregateMetric = "count"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"count"`
- `"score_histogram"`
- `"score_outcomes"`
- `"late_flips"`
