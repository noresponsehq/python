# Changelog

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
