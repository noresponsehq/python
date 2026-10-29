# Changelog

## 9.4.1

* `sdk.accounts.search()`: **Added**

## 9.4.0

* `sdk.assessments.create()`:  `response.detail.risk.details.breach_names[]` **Changed**
* `sdk.assessments.get()`:  `response.detail.risk.details.breach_names[]` **Changed**
* `sdk.assessments.query()`:  `response.items[].risk.details.breach_names[]` **Changed**
* `sdk.assessments.search()`:  `response.items[].detail.risk.details.breach_names[]` **Changed**
* `sdk.assessments.retrieve_version()`:  `response.detail.risk.details.breach_names[]` **Changed**
* `sdk.accounts.list_assessments()`:  `response.items[].risk.details.breach_names[]` **Changed**
* `sdk.accounts.export()`:  `response.assessments[].detail.risk.details.breach_names[]` **Changed**

## 9.3.0

* `sdk.assessments.aggregate()`: 
  *  `request.time_zone` **Added**
  *  `response.time_zone` **Added**

## 9.2.0

* `sdk.assessments.search()`: 
  *  `request` **Changed**
  *  `response` **Changed**

## 9.1.0

* `sdk.usage.get()`:  `response.console_lookups` **Added**

## 9.0.0

* `sdk.accounts.list_outcomes()`: 
  *  `response.items[].actor` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed**
* `sdk.accounts.record_outcome()`: 
  *  `response.actor` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed**
* `sdk.accounts.export()`: 
  *  `response` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed**
* `sdk.keys.create()`: 
  *  `request` **Changed**
  *  `response` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed**
* `sdk.accounts.list_enforcements()`: **Added**
* `sdk.accounts.list_decisions()`: **Added**
* `sdk.webhook_endpoints.aggregate()`: **Added**
* `sdk.members.list()`: **Added**
* `sdk.members.remove()`: **Added**
* `sdk.members.update()`: **Added**
* `sdk.audit.list()`: **Added**
* `sdk.audit.get_retention()`: **Added**
* `sdk.audit.update_retention()`: **Added**
* `sdk.audit.list_streams()`: **Added**
* `sdk.audit.configure_stream()`: **Added**
* `sdk.audit.remove_stream()`: **Added**
* `sdk.audit.replay_stream()`: **Added**
* `sdk.usage.get()`: **Added**
* `sdk.invites.list()`: **Added**
* `sdk.invites.create()`: **Added**
* `sdk.invites.revoke()`: **Added**
* `sdk.invites.resend()`: **Added**
* `sdk.settings.list_history()`: **Added**
* `sdk.settings.restore()`: **Added**
* `sdk.settings.preview()`: **Added**
* `sdk.requests.aggregate()`: **Added**
* `sdk.lists.preview()`: **Added**
* `sdk.lists.change()`: **Added**
* `sdk.lists.get_change()`: **Added**
* `sdk.reviews.list()`: **Added**
* `sdk.reviews.create()`: **Added**
* `sdk.reviews.get()`: **Added**
* `sdk.reviews.update()`: **Added**
* `sdk.reviews.resolve()`: **Added**
* `sdk.reviews.list_comments()`: **Added**
* `sdk.reviews.comment()`: **Added**
* `sdk.reviews.list_resolutions()`: **Added**
* `sdk.reviews.list_views()`: **Added**
* `sdk.reviews.create_view()`: **Added**
* `sdk.reviews.delete_view()`: **Added**
* `sdk.reviews.update_view()`: **Added**
* `sdk.reviews.export()`: **Added**
* `sdk.reviews.list_subjects()`: **Added**
* `sdk.reviews.add_subject()`: **Added**
* `sdk.reviews.delete_subject()`: **Added**
* `sdk.erasures.get()`: **Added**
* `sdk.exports.list()`: **Added**
* `sdk.exports.create()`: **Added**
* `sdk.exports.get()`: **Added**
* `sdk.exports.cancel()`: **Added**
* `sdk.exports.retry()`: **Added**
* `sdk.exports.download_chunk()`: **Added**
* `sdk.evaluations.list()`: **Added**
* `sdk.evaluations.create()`: **Added**
* `sdk.evaluations.get()`: **Added**
* `sdk.evaluations.get_result()`: **Added**
* `sdk.evaluations.cancel()`: **Added**
* `sdk.evaluations.publish()`: **Added**
* `sdk.operations.summarize()`: **Added**
* `sdk.assessments.create()`:  `error.code` **Changed**
* `sdk.assessments.get()`:  `error.code` **Changed**
* `sdk.assessments.delete()`: 
  *  `response.erasure_id` **Added**
  *  `error.code` **Changed**
* `sdk.assessments.record_outcome()`:  `error.code` **Changed**
* `sdk.assessments.query()`:  `error.code` **Changed**
* `sdk.assessments.aggregate()`: 
  *  `request` **Changed**
  *  `response` **Changed**
  *  `error.code` **Changed**
* `sdk.assessments.search()`: 
  *  `request` **Changed**
  *  `error.code` **Changed**
* `sdk.assessments.retrieve_version()`:  `error.code` **Changed**
* `sdk.assessments.bind_account()`:  `error.code` **Changed**
* `sdk.accounts.list_changed()`:  `error.code` **Changed**
* `sdk.accounts.get()`:  `error.code` **Changed**
* `sdk.accounts.delete()`: 
  *  `response.erasure_id` **Added**
  *  `error.code` **Changed**
* `sdk.accounts.list_assessments()`:  `error.code` **Changed**
* `sdk.accounts.record_enforcement()`:  `error.code` **Changed**
* `sdk.accounts.retrieve_decision()`:  `error.code` **Changed**
* `sdk.accounts.list_credentials()`:  `error.code` **Changed**
* `sdk.accounts.associate_credential()`:  `error.code` **Changed**
* `sdk.accounts.retire_credential()`:  `error.code` **Changed**
* `sdk.key_usage.record()`:  `error.code` **Changed**
* `sdk.keys.rotate()`:  `error.code` **Changed**
* `sdk.keys.list()`: 
  *  `response.items[]` **Changed**
  *  `error.code` **Changed**
* `sdk.keys.revoke()`: 
  *  `response` **Changed**
  *  `error.code` **Changed**
* `sdk.integrations.list()`:  `error.code` **Changed**
* `sdk.integrations.create()`:  `error.code` **Changed**
* `sdk.integrations.delete()`:  `error.code` **Changed**
* `sdk.integrations.rotate()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.list()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.create()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.delete()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.rotate_signing_key()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.send_test_event()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.list_deliveries()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.replay_delivery()`:  `error.code` **Changed**
* `sdk.settings.get()`:  `error.code` **Changed**
* `sdk.settings.update()`: 
  *  `request` **Changed**
  *  `error.code` **Changed**
* `sdk.requests.list()`: 
  *  `request.api_key_id` **Added**
  *  `response.items[].api_key_id` **Added**
  *  `error.code` **Changed**
* `sdk.lists.list()`: 
  *  `request` **Changed**
  *  `response` **Changed**
  *  `error.code` **Changed**
* `sdk.lists.create()`: 
  *  `request.expires_at` **Added**
  *  `response.expires_at` **Added**
  *  `error.code` **Changed**
* `sdk.lists.delete()`:  `error.code` **Changed**

## 8.4.1

No changes detected.

## 8.4.0

* `sdk.assessments.aggregate()`: 
  *  `request.metrics[].enum(score_outcomes)` **Added**
  *  `response` **Changed**

## 8.3.0

* `sdk.assessments.aggregate()`: **Added**
* `sdk.assessments.search()`:  `request.revision` **Added**

## 8.2.1

* `sdk.assessments.create()`:  `response.detail.identifiers` **Added**
* `sdk.assessments.get()`:  `response.detail.identifiers` **Added**
* `sdk.assessments.query()`:  `response.items[].identifiers` **Added**
* `sdk.assessments.search()`:  `response.items[].detail.identifiers` **Added**
* `sdk.assessments.retrieve_version()`:  `response.detail.identifiers` **Added**
* `sdk.accounts.list_assessments()`:  `response.items[].identifiers` **Added**
* `sdk.accounts.export()`:  `response.assessments[].detail.identifiers` **Added**

## 8.2.0

* `sdk.assessments.search()`: **Added**
* `sdk.assessments.retrieve_version()`: **Added**
* `sdk.assessments.bind_account()`: **Added**
* `sdk.accounts.record_outcome()`: **Added**
* `sdk.accounts.list_outcomes()`: **Added**
* `sdk.accounts.retrieve_decision()`: **Added**
* `sdk.accounts.associate_credential()`: **Added**
* `sdk.accounts.list_credentials()`: **Added**
* `sdk.accounts.retire_credential()`: **Added**
* `sdk.accounts.export()`: **Added**
* `sdk.requests.list()`: **Added**
* `sdk.assessments.create()`: 
  *  `response.account.risk.reasons[].code.enum(reported_account_abuse)` **Added**
  *  `error.code` **Changed**
* `sdk.assessments.get()`: 
  *  `response.account.risk.reasons[].code.enum(reported_account_abuse)` **Added**
  *  `error.code` **Changed**
* `sdk.assessments.delete()`:  `error.code` **Changed**
* `sdk.assessments.record_outcome()`:  `error.code` **Changed**
* `sdk.assessments.query()`: 
  *  `response.items[].risk.reasons[].code.enum(reported_account_abuse)` **Added**
  *  `error.code` **Changed**
* `sdk.accounts.list_changed()`: 
  *  `response.items[].risk.reasons[].code.enum(reported_account_abuse)` **Added**
  *  `error.code` **Changed**
* `sdk.accounts.get()`: 
  *  `response.risk.reasons[].code.enum(reported_account_abuse)` **Added**
  *  `error.code` **Changed**
* `sdk.accounts.delete()`:  `error.code` **Changed**
* `sdk.accounts.list_assessments()`: 
  *  `response.items[].risk.reasons[].code.enum(reported_account_abuse)` **Added**
  *  `error.code` **Changed**
* `sdk.accounts.record_enforcement()`:  `error.code` **Changed**
* `sdk.key_usage.record()`:  `error.code` **Changed**
* `sdk.keys.rotate()`:  `error.code` **Changed**
* `sdk.keys.create()`:  `error.code` **Changed**
* `sdk.keys.list()`:  `error.code` **Changed**
* `sdk.keys.revoke()`:  `error.code` **Changed**
* `sdk.integrations.create()`:  `error.code` **Changed**
* `sdk.integrations.list()`:  `error.code` **Changed**
* `sdk.integrations.delete()`:  `error.code` **Changed**
* `sdk.integrations.rotate()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.list()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.create()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.delete()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.rotate_signing_key()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.send_test_event()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.list_deliveries()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.replay_delivery()`:  `error.code` **Changed**
* `sdk.settings.get()`:  `error.code` **Changed**
* `sdk.settings.update()`:  `error.code` **Changed**
* `sdk.lists.list()`:  `error.code` **Changed**
* `sdk.lists.create()`:  `error.code` **Changed**
* `sdk.lists.delete()`:  `error.code` **Changed**

## 8.1.3

* `sdk.assessments.create()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.assessments.get()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.assessments.delete()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.assessments.record_outcome()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.assessments.query()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.accounts.list_changed()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.accounts.get()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.accounts.delete()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.accounts.list_assessments()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.accounts.record_enforcement()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.key_usage.record()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.keys.rotate()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.keys.create()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.keys.list()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.keys.revoke()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.integrations.create()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.integrations.list()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.integrations.delete()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.integrations.rotate()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.webhook_endpoints.list()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.webhook_endpoints.create()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.webhook_endpoints.delete()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.webhook_endpoints.rotate_signing_key()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.webhook_endpoints.send_test_event()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.webhook_endpoints.list_deliveries()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.webhook_endpoints.replay_delivery()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.settings.get()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.settings.update()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.lists.list()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.lists.create()`:  `error.code.enum(list_entry_too_broad)` **Added**
* `sdk.lists.delete()`:  `error.code.enum(list_entry_too_broad)` **Added**

## 8.1.2

* `sdk.lists.list()`: **Added**
* `sdk.lists.create()`: **Added**
* `sdk.lists.delete()`: **Added**
* `sdk.assessments.create()`: 
  *  `response` **Changed**
  *  `error.code` **Changed**
* `sdk.assessments.get()`: 
  *  `response` **Changed**
  *  `error.code` **Changed**
* `sdk.assessments.delete()`:  `error.code` **Changed**
* `sdk.assessments.record_outcome()`:  `error.code` **Changed**
* `sdk.assessments.query()`: 
  *  `response.items[].risk.reasons[]` **Changed**
  *  `error.code` **Changed**
* `sdk.accounts.list_changed()`: 
  *  `response.items[].risk.reasons[]` **Changed**
  *  `error.code` **Changed**
* `sdk.accounts.get()`: 
  *  `response.risk.reasons[]` **Changed**
  *  `error.code` **Changed**
* `sdk.accounts.delete()`:  `error.code` **Changed**
* `sdk.accounts.list_assessments()`: 
  *  `response.items[].risk.reasons[]` **Changed**
  *  `error.code` **Changed**
* `sdk.accounts.record_enforcement()`:  `error.code` **Changed**
* `sdk.key_usage.record()`:  `error.code` **Changed**
* `sdk.keys.rotate()`:  `error.code` **Changed**
* `sdk.keys.create()`:  `error.code` **Changed**
* `sdk.keys.list()`:  `error.code` **Changed**
* `sdk.keys.revoke()`:  `error.code` **Changed**
* `sdk.integrations.create()`:  `error.code` **Changed**
* `sdk.integrations.list()`:  `error.code` **Changed**
* `sdk.integrations.delete()`:  `error.code` **Changed**
* `sdk.integrations.rotate()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.list()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.create()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.delete()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.rotate_signing_key()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.send_test_event()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.list_deliveries()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.replay_delivery()`:  `error.code` **Changed**
* `sdk.settings.get()`:  `error.code` **Changed**
* `sdk.settings.update()`:  `error.code` **Changed**

## 8.1.1

* `sdk.webhook_endpoints.list()`:  `response.items[]` **Changed**
* `sdk.webhook_endpoints.create()`:  `response.endpoint` **Changed**

## 8.1.0

No changes detected.

## 8.0.3

* `sdk.assessments.create()`:  `response.detail.risk.summary.ip.asn` **Added**
* `sdk.assessments.get()`:  `response.detail.risk.summary.ip.asn` **Added**
* `sdk.assessments.query()`:  `response.items[].risk.summary.ip.asn` **Added**
* `sdk.accounts.list_assessments()`:  `response.items[].risk.summary.ip.asn` **Added**

## 8.0.2

No changes detected.

## 8.0.1

No changes detected.

## 8.0.0

* `sdk.assessments.create()`:  `response` **Changed** (Breaking ⚠️)
* `sdk.assessments.get()`:  `response` **Changed** (Breaking ⚠️)
* `sdk.assessments.query()`:  `response.items[].risk.reasons[].weight` **Removed** (Breaking ⚠️)
* `sdk.accounts.list_changed()`:  `response.items[].risk.reasons[].weight` **Removed** (Breaking ⚠️)
* `sdk.accounts.get()`:  `response.risk.reasons[].weight` **Removed** (Breaking ⚠️)
* `sdk.accounts.list_assessments()`:  `response.items[].risk.reasons[].weight` **Removed** (Breaking ⚠️)

## 7.2.2

No changes detected.

## 7.2.1

No changes detected.

## 7.2.0

No changes detected.

## 7.1.8

* `sdk.assessments.create()`:  `response` **Changed**
* `sdk.assessments.get()`:  `response` **Changed**
* `sdk.assessments.query()`:  `response.items[].risk` **Changed**
* `sdk.accounts.list_changed()`:  `response.items[].risk.reasons[]` **Changed**
* `sdk.accounts.get()`:  `response.risk.reasons[]` **Changed**
* `sdk.accounts.list_assessments()`:  `response.items[].risk` **Changed**

## 7.1.7

* `sdk.assessments.create()`:  `response.account.risk.reasons[].code` **Changed**
* `sdk.assessments.get()`:  `response.account.risk.reasons[].code` **Changed**
* `sdk.assessments.query()`:  `response.items[].risk.reasons[].code` **Changed**
* `sdk.accounts.list_changed()`:  `response.items[].risk.reasons[].code` **Changed**
* `sdk.accounts.get()`:  `response.risk.reasons[].code` **Changed**
* `sdk.accounts.list_assessments()`:  `response.items[].risk.reasons[].code` **Changed**

## 7.1.6

* `sdk.integrations.create()`: 
  *  `request.platform.enum(supabase)` **Added**
  *  `response.platform.enum(supabase)` **Added**
* `sdk.integrations.list()`:  `response.items[].platform.enum(supabase)` **Added**
* `sdk.integrations.rotate()`:  `response.platform.enum(supabase)` **Added**

## 7.1.5

* `sdk.assessments.create()`:  `response.account.risk.reasons[].code` **Changed**
* `sdk.assessments.get()`:  `response.account.risk.reasons[].code` **Changed**
* `sdk.assessments.query()`:  `response.items[].risk.reasons[].code` **Changed**
* `sdk.accounts.list_changed()`:  `response.items[].risk.reasons[].code` **Changed**
* `sdk.accounts.get()`:  `response.risk.reasons[].code` **Changed**
* `sdk.accounts.list_assessments()`:  `response.items[].risk.reasons[].code` **Changed**

## 7.1.4

No changes detected.

## 7.1.3

No changes detected.

## 7.1.2

No changes detected.

## 7.1.1

* `sdk.accounts.record_enforcement()`: 
  *  `request.action.enum(activate)` **Added**
  *  `response.action.enum(activate)` **Added**

## 7.1.0

* `sdk.keys.create()`: **Added**
* `sdk.keys.list()`: **Added**
* `sdk.keys.revoke()`: **Added**
* `sdk.settings.get()`: **Added**
* `sdk.settings.update()`: **Added**
* `sdk.assessments.create()`:  `error.code` **Changed**
* `sdk.assessments.get()`:  `error.code` **Changed**
* `sdk.assessments.delete()`:  `error.code` **Changed**
* `sdk.assessments.record_outcome()`:  `error.code` **Changed**
* `sdk.assessments.query()`:  `error.code` **Changed**
* `sdk.accounts.list_changed()`:  `error.code` **Changed**
* `sdk.accounts.get()`:  `error.code` **Changed**
* `sdk.accounts.delete()`:  `error.code` **Changed**
* `sdk.accounts.list_assessments()`:  `error.code` **Changed**
* `sdk.accounts.record_enforcement()`:  `error.code` **Changed**
* `sdk.key_usage.record()`:  `error.code` **Changed**
* `sdk.keys.rotate()`: 
  *  `response.scopes[].enum(management)` **Added**
  *  `error.code` **Changed**
* `sdk.integrations.create()`:  `error.code` **Changed**
* `sdk.integrations.list()`:  `error.code` **Changed**
* `sdk.integrations.delete()`:  `error.code` **Changed**
* `sdk.integrations.rotate()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.list()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.create()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.delete()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.rotate_signing_key()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.send_test_event()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.list_deliveries()`:  `error.code` **Changed**
* `sdk.webhook_endpoints.replay_delivery()`:  `error.code` **Changed**

## 7.0.5

No changes detected.

## 7.0.4

* `sdk.assessments.create()`:  `response.account.risk.reasons[].code` **Changed**
* `sdk.assessments.get()`:  `response.account.risk.reasons[].code` **Changed**
* `sdk.assessments.query()`:  `response.items[].risk.reasons[].code` **Changed**
* `sdk.accounts.list_changed()`:  `response.items[].risk.reasons[].code` **Changed**
* `sdk.accounts.get()`:  `response.risk.reasons[].code` **Changed**
* `sdk.accounts.list_assessments()`:  `response.items[].risk.reasons[].code` **Changed**

## 7.0.3

* `sdk.assessments.create()`:  `response.detail.incomplete_sources[].lane.enum(domain)` **Added**
* `sdk.assessments.get()`:  `response.detail.incomplete_sources[].lane.enum(domain)` **Added**
* `sdk.assessments.query()`:  `response.items[].incomplete_sources[].lane.enum(domain)` **Added**
* `sdk.accounts.list_assessments()`:  `response.items[].incomplete_sources[].lane.enum(domain)` **Added**

## 7.0.2

No changes detected.

## 7.0.1

* `sdk.assessments.create()`:  `response.account.risk.decision.enum(held)` **Added**
* `sdk.assessments.get()`:  `response.account.risk.decision.enum(held)` **Added**
* `sdk.accounts.list_changed()`:  `response.items[].risk.decision.enum(held)` **Added**
* `sdk.accounts.get()`:  `response.risk.decision.enum(held)` **Added**

## 7.0.0

No changes detected.

## 6.0.1

* `sdk.accounts.list_changed()`: **Added**
* `sdk.accounts.record_enforcement()`: **Added**
* `sdk.assessments.create()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.assessments.get()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.assessments.delete()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.assessments.record_outcome()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.assessments.query()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.accounts.get()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.accounts.delete()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.accounts.list_assessments()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.key_usage.record()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.keys.rotate()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.integrations.create()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.integrations.list()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.integrations.delete()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.integrations.rotate()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.webhook_endpoints.list()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.webhook_endpoints.create()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.webhook_endpoints.delete()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.webhook_endpoints.rotate_signing_key()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.webhook_endpoints.send_test_event()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.webhook_endpoints.list_deliveries()`:  `error.code.enum(risk_version_ahead)` **Added**
* `sdk.webhook_endpoints.replay_delivery()`:  `error.code.enum(risk_version_ahead)` **Added**

## 6.0.0

No changes detected.

## 5.1.1

* `sdk.assessments.create()`:  `response.account.risk_version` **Added**
* `sdk.assessments.get()`:  `response.account.risk_version` **Added**
* `sdk.accounts.get()`:  `response.risk_version` **Added**

## 5.1.0

* `sdk.keys.rotate()`:  `response.scopes[].enum(delete)` **Added**

## 5.0.1

No changes detected.

## 5.0.0

* `sdk.assessments.create()`: 
  *  `request.flow` **Changed** (Breaking ⚠️)
  *  `response` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed** (Breaking ⚠️)
* `sdk.assessments.get()`: 
  *  `response` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed** (Breaking ⚠️)
* `sdk.assessments.delete()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.assessments.record_outcome()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.assessments.query()`: 
  *  `response.items[].risk` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed** (Breaking ⚠️)
* `sdk.accounts.get()`: 
  *  `response` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed** (Breaking ⚠️)
* `sdk.accounts.delete()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.accounts.list_assessments()`: 
  *  `response.items[].risk` **Changed** (Breaking ⚠️)
  *  `error.code` **Changed** (Breaking ⚠️)
* `sdk.key_usage.record()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.keys.rotate()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.integrations.create()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.integrations.list()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.integrations.delete()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.integrations.rotate()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.webhook_endpoints.list()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.webhook_endpoints.create()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.webhook_endpoints.delete()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.webhook_endpoints.rotate_signing_key()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.webhook_endpoints.send_test_event()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.webhook_endpoints.list_deliveries()`:  `error.code` **Changed** (Breaking ⚠️)
* `sdk.webhook_endpoints.replay_delivery()`:  `error.code` **Changed** (Breaking ⚠️)

## 4.0.1

No changes detected.

## 4.0.0

* `sdk.webhook_endpoints.list_deliveries()`:  `response.items[].event_type` **Changed** (Breaking ⚠️)
* `sdk.webhook_endpoints.replay_delivery()`:  `response.event_type` **Changed** (Breaking ⚠️)

## 3.0.8

No changes detected.

## 3.0.7

No changes detected.

## 3.0.6

No changes detected.

## 3.0.5

No changes detected.

## 3.0.4

No changes detected.

## 3.0.3

* `sdk.key_usage.record()`: **Added**
* `sdk.assessments.create()`:  `response.account.risk.reasons[].code.enum(shared_api_key)` **Added**
* `sdk.assessments.get()`:  `response.account.risk.reasons[].code.enum(shared_api_key)` **Added**
* `sdk.assessments.query()`:  `response.items[].risk.reasons[].code.enum(shared_api_key)` **Added**
* `sdk.accounts.get()`:  `response.risk.reasons[].code.enum(shared_api_key)` **Added**
* `sdk.accounts.list_assessments()`:  `response.items[].risk.reasons[].code.enum(shared_api_key)` **Added**

## 3.0.2

No changes detected.

## 3.0.1

No changes detected.

## 3.0.0

* `sdk.assessments.create()`: 
  *  `request` **Changed** (Breaking ⚠️)
  *  `response` **Changed** (Breaking ⚠️)
* `sdk.assessments.get()`:  `response` **Changed** (Breaking ⚠️)

## 2.0.33

* `sdk.assessments.delete()`: **Added**

## 2.0.32

No changes detected.

## 2.0.31

No changes detected.

## 2.0.30

No changes detected.

## 2.0.29

* `sdk.accounts.delete()`: **Added**

## 2.0.28

* `sdk.assessments.create()`:  `request` **Changed**

## 2.0.27

No changes detected.

## 2.0.26

* `sdk.webhook_endpoints.list_deliveries()`: **Added**
* `sdk.webhook_endpoints.replay_delivery()`: **Added**

## 2.0.25

No changes detected.

## 2.0.24

No changes detected.

## 2.0.23

* `sdk.assessments.create()`:  `response.risk.reasons[].code.enum(test_scenario)` **Added**
* `sdk.assessments.get()`:  `response.risk.reasons[].code.enum(test_scenario)` **Added**
* `sdk.assessments.query()`:  `response.items[].risk.reasons[].code.enum(test_scenario)` **Added**
* `sdk.accounts.get()`:  `response.risk.reasons[].code.enum(test_scenario)` **Added**
* `sdk.accounts.list_assessments()`:  `response.items[].risk.reasons[].code.enum(test_scenario)` **Added**

## 2.0.22

No changes detected.

## 2.0.21

No changes detected.

## 2.0.20

* `sdk.accounts.get()`: **Added**
* `sdk.accounts.list_assessments()`: **Added**

## 2.0.19

No changes detected.

## 2.0.18

No changes detected.

## 2.0.17

No changes detected.

## 2.0.16

No changes detected.

## 2.0.15

* `sdk.assessments.create()`:  `response.auth_context` **Added**
* `sdk.assessments.get()`:  `response.auth_context` **Added**
* `sdk.assessments.query()`:  `response.items[].auth_context` **Added**

## 2.0.14

* `sdk.webhook_endpoints.list()`: **Added**
* `sdk.webhook_endpoints.create()`: **Added**
* `sdk.webhook_endpoints.delete()`: **Added**
* `sdk.webhook_endpoints.rotate_signing_key()`: **Added**
* `sdk.webhook_endpoints.send_test_event()`: **Added**
* `sdk.assessments.create()`:  `error.code` **Changed**
* `sdk.assessments.get()`:  `error.code` **Changed**
* `sdk.assessments.record_outcome()`:  `error.code` **Changed**
* `sdk.assessments.query()`:  `error.code` **Changed**
* `sdk.keys.rotate()`:  `error.code` **Changed**
* `sdk.integrations.create()`:  `error.code` **Changed**
* `sdk.integrations.list()`:  `error.code` **Changed**
* `sdk.integrations.delete()`:  `error.code` **Changed**
* `sdk.integrations.rotate()`:  `error.code` **Changed**

## 2.0.13

* `sdk.integrations.create()`: **Added**
* `sdk.integrations.list()`: **Added**
* `sdk.integrations.delete()`: **Added**
* `sdk.integrations.rotate()`: **Added**
* `sdk.assessments.create()`:  `error.code.enum(too_many_integrations)` **Added**
* `sdk.assessments.get()`:  `error.code.enum(too_many_integrations)` **Added**
* `sdk.assessments.record_outcome()`:  `error.code.enum(too_many_integrations)` **Added**
* `sdk.assessments.query()`:  `error.code.enum(too_many_integrations)` **Added**
* `sdk.keys.rotate()`: 
  *  `response.scopes[].enum(integrations)` **Added**
  *  `error.code.enum(too_many_integrations)` **Added**

## 2.0.12

* `sdk.assessments.create()`: 
  *  `request.issued_credential` **Added**
  *  `response.risk` **Changed**
* `sdk.assessments.get()`:  `response.risk` **Changed**
* `sdk.assessments.query()`:  `response.items[].risk` **Changed**

## 2.0.11

No changes detected.

## 2.0.10

No changes detected.

## 2.0.9

* `sdk.assessments.create()`:  `request.auth_context` **Changed**

## 2.0.8

No changes detected.

## 2.0.7

No changes detected.

## 2.0.6

No changes detected.

## 2.0.5

No changes detected.

## 2.0.4

No changes detected.

## 2.0.3

No changes detected.

## 2.0.2

API changes since the previous release are not listed: no earlier document was recorded.
