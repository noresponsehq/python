# IntegrationList

GET /v1/integrations: every integration of the workspace, oldest first, at most 10. No secret is ever listed.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `items`                                                        | List[[shared.Integration](../../models/shared/integration.md)] | :heavy_check_mark:                                             | N/A                                                            |