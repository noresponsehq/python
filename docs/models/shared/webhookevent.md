# WebhookEvent

The body of every webhook delivery: {id, type, created_at, data}, where type chooses the shape of data. Deliveries are at least once and unordered: deduplicate on id, and keep an assessment only when its detail.assessment_version is newer than the one you hold. GET /v1/assessments/{assessment_id} stays authoritative.


## Supported Types

### `shared.AssessmentUpdatedEvent`

```python
value: shared.AssessmentUpdatedEvent = /* values here */
```

### `shared.EndpointVerificationEvent`

```python
value: shared.EndpointVerificationEvent = /* values here */
```

### `shared.AccountDeletedEvent`

```python
value: shared.AccountDeletedEvent = /* values here */
```

### `shared.WorkspaceDeletedEvent`

```python
value: shared.WorkspaceDeletedEvent = /* values here */
```

### `shared.WebhookEndpointDisabledEvent`

```python
value: shared.WebhookEndpointDisabledEvent = /* values here */
```

### `shared.AccountRiskChangedEvent`

```python
value: shared.AccountRiskChangedEvent = /* values here */
```

