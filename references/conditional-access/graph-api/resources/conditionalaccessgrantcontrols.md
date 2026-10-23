# conditionalAccessGrantControls resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessgrantcontrols?view=graph-rest-1.0  
> Microsoft doc last updated: 04/06/2026


Namespace: microsoft.graph

Represents grant controls that must be fulfilled to pass the policy.

## Properties

| Property | Type | Description |
|:-------- |:---- |:----------- |
| builtInControls | conditionalAccessGrantControl collection | List of values of built-in controls required by the policy. Possible values: `block`, `mfa`, `compliantDevice`, `domainJoinedDevice`, `approvedApplication`, `compliantApplication`, `passwordChange`, `unknownFutureValue`, `riskRemediation`.  Use the `Prefer: include-unknown-enum-members` request header to get the following value in this evolvable enum: `riskRemediation`.|
| customAuthenticationFactors | String collection | List of custom controls IDs required by the policy. For more information, see [Custom controls](https://learn.microsoft.com/en-us/entra/identity/conditional-access/controls). |
| operator | String | Defines the relationship of the grant controls. Possible values: `AND`, `OR`. |
| termsOfUse | String collection | List of [terms of use](https://learn.microsoft.com/en-us/graph/api/resources/agreement) IDs required by the policy. |

### Special considerations when using `passwordChange` as a control

Consider the following when you use the `passwordChange` and `riskRemediation` controls:

- `passwordChange` and `riskRemediation` must be used separately, not in combination.
- `passwordChange` must be accompanied by `mfa` using an `AND` operator. This combination ensures that the password is updated in a secure way.
- `riskRemediation` must be accompanied by `authenticationStrength` using an `AND` operator. This combination ensures that the authentication strength for the user is enforced during the remediation flow.
- `passwordChange` and `riskRemediation` must each be used in a policy containing `userRiskLevels`. This is designed to enable scenarios where users can self-remediate their user risk.
- The policy should target `all` applications, and not exclude any applications.
- The policy can't contain any other condition except `users`, `applications`, and `userRiskLevels`.

## Relationships

|Relationship|Type|Description|
|:---|:---|:---|
| authenticationStrength | [authenticationStrengthPolicy](authenticationstrengthpolicy.md) | The authentication strength required by the conditional access policy. Optional.|

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "builtInControls": ["String"],
  "customAuthenticationFactors": ["String"],
  "operator": "String",
  "termsOfUse": ["String"]
}
```
