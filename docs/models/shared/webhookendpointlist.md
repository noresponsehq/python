# WebhookEndpointList

GET /v1/webhooks answer: every endpoint of the calling tenant, in every state, ordered by endpoint_id. A tenant holds at most 5, so there is no page.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `items`                                                                | List[[shared.WebhookEndpoint](../../models/shared/webhookendpoint.md)] | :heavy_check_mark:                                                     | N/A                                                                    |