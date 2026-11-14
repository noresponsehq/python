# RecordRole

Which common field a value is, where many sources share it: a join date and a birth date are both dates, with the roles joined and born. A platform account's field and a breach row's column with the same meaning carry the same kind and role. A linked_account field is named by its network. Absent for a field only its source returns. Each role's description names the kinds its values have.

## Example Usage

```python
from noresponse.models.shared import RecordRole

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RecordRole = "account_id"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"account_id"`
- `"account_status"`
- `"account_type"`
- `"alternate_phone"`
- `"balance"`
- `"banned"`
- `"bio"`
- `"born"`
- `"bot"`
- `"caller_category"`
- `"cover_picture"`
- `"deleted"`
- `"deleted_on"`
- `"department"`
- `"display_name"`
- `"email_verified"`
- `"expires"`
- `"first_name"`
- `"followers"`
- `"following"`
- `"friends"`
- `"full_address"`
- `"full_name"`
- `"handle"`
- `"headline"`
- `"interests"`
- `"job_title"`
- `"joined"`
- `"last_active"`
- `"last_ip"`
- `"last_name"`
- `"last_post"`
- `"last_updated"`
- `"level"`
- `"likes_given"`
- `"likes_received"`
- `"line_type"`
- `"linked_account"`
- `"location"`
- `"marked_spam"`
- `"middle_name"`
- `"nationality"`
- `"organisation"`
- `"other_ip"`
- `"paid"`
- `"password_changed"`
- `"picture"`
- `"points"`
- `"posts"`
- `"private"`
- `"profile_link"`
- `"profile_views"`
- `"rating"`
- `"referrals"`
- `"referrer"`
- `"report_count"`
- `"reputation"`
- `"reputation_label"`
- `"residence"`
- `"salutation"`
- `"school"`
- `"signature"`
- `"signup_ip"`
- `"site_role"`
- `"spam_score"`
- `"street"`
- `"verified"`
- `"warnings"`
- `"website"`
