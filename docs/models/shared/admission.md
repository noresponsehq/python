# Admission

immediate (the default): an assessment of this flow is decided from the evidence its answer has, and later evidence may change the decision. held: while the account's current assessment of this flow has not completed, the account's decision for the flow is held, and the final decision arrives as account.risk_changed when the investigation completes or hold_seconds pass, whichever is first. Each flow has its own admission.

## Example Usage

```python
from noresponse.models.shared import Admission

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Admission = "immediate"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"immediate"`
- `"held"`
