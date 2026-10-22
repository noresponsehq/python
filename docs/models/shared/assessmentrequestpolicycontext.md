# AssessmentRequestPolicyContext


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `flow`                                                                  | [Optional[shared.Flow]](../../models/shared/flow.md)                    | :heavy_minus_sign:                                                      | The provider flow the assessment gates. Absent means signup.            |                                                                         |
| `region`                                                                | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | ISO 3166-1 alpha-2 region of the signup, as the provider determines it. | AU                                                                      |