# Outcome

What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins.

## Example Usage

```python
from noresponse.models.shared import Outcome

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Outcome = "confirmed_abuse"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"confirmed_abuse"`
- `"account_takeover"`
- `"chargeback"`
- `"false_positive"`
- `"legitimate"`
- `"unknown"`
