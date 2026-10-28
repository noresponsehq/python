# AggregateDimension

decision, recommendation and band: the first answer's. flow: the assessment's. list_match: the action of the list entry that decided the account when it was first answered. reason: a reason the first answer fired, with its impact band. lane: an evidence lane the first answer listed in incomplete_sources. country and asn: the submitted IP's, from the IP data.

## Example Usage

```python
from noresponse.models.shared import AggregateDimension

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AggregateDimension = "decision"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"decision"`
- `"flow"`
- `"recommendation"`
- `"band"`
- `"reason"`
- `"lane"`
- `"country"`
- `"asn"`
- `"list_match"`
