# EnforcementAction

What the workspace did in its identity provider: revoke_sessions (signed the account out everywhere), restrict (limited what the account can do), unrestrict (lifted an earlier restriction), fail_onboarding (stopped an account that was still onboarding), reject_activation (refused to activate a provisional account), activate (let a held onboarding or provisional account in) or none (decided to take no action).

## Example Usage

```python
from noresponse.models.shared import EnforcementAction

# Open enum: unrecognized values are captured as UnrecognizedStr
value: EnforcementAction = "revoke_sessions"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"revoke_sessions"`
- `"restrict"`
- `"unrestrict"`
- `"fail_onboarding"`
- `"reject_activation"`
- `"activate"`
- `"none"`
