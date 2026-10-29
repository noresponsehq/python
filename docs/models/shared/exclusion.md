# Exclusion

## Example Usage

```python
from noresponse.models.shared import Exclusion

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Exclusion = "expired_or_erased_records"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"expired_or_erased_records"`
- `"secrets_and_credential_digests"`
- `"private_source_and_work_payloads"`
- `"cross_customer_data"`
- `"legacy_outcome_notes"`
- `"uncaptured_historical_decisions"`
- `"investigator_reviews_require_review_export"`
