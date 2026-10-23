# Changelog

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
