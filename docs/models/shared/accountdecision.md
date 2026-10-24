# AccountDecision

block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. held only for a flow whose admission is held (settings flows.<flow>.admission), when the account's current assessment was made for that flow and its investigation has not completed (status partial): the final decision arrives as account.risk_changed when the investigation completes, decided by its score, or when the hold's deadline (hold_seconds after the assessment was created) passes first, as the flow's on_expiry action or the decision the evidence so far gives, whichever is stricter. Your application applies it.

## Example Usage

```python
from noresponse.models.shared import AccountDecision

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AccountDecision = "allow"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"allow"`
- `"step_up"`
- `"review"`
- `"block"`
- `"held"`
