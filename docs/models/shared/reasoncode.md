# ReasonCode

A stable reason code. New codes may appear; ignore any you do not know.

## Example Usage

```python
from noresponse.models.shared import ReasonCode

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ReasonCode = "no_digital_footprint"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"no_digital_footprint"`
- `"voip_number"`
- `"disposable_email"`
- `"new_email"`
- `"spam_reports"`
- `"fraud_flag"`
- `"identity_mismatch"`
- `"country_mismatch"`
- `"proxy_ip"`
- `"seen_before"`
- `"shared_ip"`
- `"many_recent_accounts"`
- `"established_accounts"`
- `"aged_identity"`
- `"breach_name_match"`
- `"breach_cooccurrence"`
- `"breach_name_mismatch"`
- `"breach_phone_mismatch"`
- `"recent_password_exposure"`
- `"credential_list_exposure"`
- `"abuse_ecosystem_member"`
- `"no_breach_history"`
- `"automation_fast_submit"`
- `"client_clock_skew"`
- `"bot_or_automation"`
- `"auth_email_verified"`
- `"auth_phone_verified"`
- `"auth_mfa_recent"`
- `"auth_new_session"`
- `"auth_new_account"`
- `"auth_impersonated"`
- `"context_timezone_mismatch"`
- `"context_locale_mismatch"`
- `"context_line_country_mismatch"`
- `"prior_abuse_link"`
- `"test_scenario"`
- `"shared_api_key"`
- `"list_match"`
- `"young_email_domain"`
- `"email_domain_no_mx"`
- `"email_domain_nonexistent"`
- `"forum_sanctioned"`
- `"prior_payment_abuse"`
- `"ip_history_match"`
- `"identity_attribute_conflict"`
- `"impossible_identity_age"`
- `"breach_shared_ip"`
- `"nationality_mismatch"`
- `"minor_identity"`
