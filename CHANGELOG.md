# Changelog

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
