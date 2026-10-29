# Metric

assessments: assessments admitted. webhook_deliveries: events sent to endpoints, one per event per endpoint. key_usage_events: key-usage events accepted.

## Example Usage

```python
from noresponse.models.shared import Metric

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Metric = "assessments"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"assessments"`
- `"webhook_deliveries"`
- `"key_usage_events"`
