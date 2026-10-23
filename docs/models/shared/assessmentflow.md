# AssessmentFlow

The customer event an assessment is made for: signup (a new account), login (a returning sign-in) or purchase (a payment or credit grant). The account's risk is reported with the decision for this flow.

## Example Usage

```python
from noresponse.models.shared import AssessmentFlow
value: AssessmentFlow = "signup"
```


## Values

- `"signup"`
- `"login"`
- `"purchase"`
