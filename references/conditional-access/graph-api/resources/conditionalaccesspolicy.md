# conditionalAccessPolicy resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccesspolicy?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

Represents a Microsoft Entra Conditional Access policy. Conditional access policies are custom rules that define an access scenario. For more information, see the [Conditional access documentation](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/).

## Methods

| Method       | Return Type | Description |
|:-------------|:------------|:------------|
| [List](../api/conditionalaccessroot-list-policies.md) | [conditionalAccessPolicy](conditionalaccesspolicy.md) collection | Get all of the conditionalAccessPolicies objects in the organization. |
| [Create](../api/conditionalaccessroot-post-policies.md) | [conditionalAccessPolicy](conditionalaccesspolicy.md) | Create a new conditionalAccessPolicy object. |
| [Get](../api/conditionalaccesspolicy-get.md) | [conditionalAccessPolicy](conditionalaccesspolicy.md) | Read properties and relationships of a conditionalAccessPolicy object. |
| [Update](../api/conditionalaccesspolicy-update.md) | [conditionalAccessPolicy](conditionalaccesspolicy.md) | Update a conditionalAccessPolicy object. |
| [Delete](../api/conditionalaccesspolicy-delete.md) | None | Delete a conditionalAccessPolicy object. |

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
|conditions|[conditionalAccessConditionSet](conditionalaccessconditionset.md)| Specifies the rules that must be met for the policy to apply. Required. |
|createdDateTime|DateTimeOffset| The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. |
|displayName|String| Specifies a display name for the conditionalAccessPolicy object. |
|grantControls|[conditionalAccessGrantControls](conditionalaccessgrantcontrols.md)| Specifies the grant controls that must be fulfilled to pass the policy. |
|id|String| Specifies the identifier of a conditionalAccessPolicy object. Read-only.|
|modifiedDateTime| DateTimeOffset|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. |
|sessionControls|[conditionalAccessSessionControls](conditionalaccesssessioncontrols.md)| Specifies the session controls that are enforced after sign-in. |
|state|conditionalAccessPolicyState| Specifies the state of the conditionalAccessPolicy object. The possible values are: `enabled`, `disabled`, `enabledForReportingButNotEnforced`. Required. |
|templateId|String|Specifies the unique identifier of a [Conditional Access template](../resources/conditionalaccesstemplate.md). Inherited from [entity](../resources/entity.md).|

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "conditions": {"@odata.type": "microsoft.graph.conditionalAccessConditionSet"},
  "createdDateTime": "String (timestamp)",
  "displayName": "String",
  "grantControls": {"@odata.type": "microsoft.graph.conditionalAccessGrantControls"},
  "id": "String (identifier)",
  "modifiedDateTime": "String (timestamp)",
  "sessionControls": {"@odata.type": "microsoft.graph.conditionalAccessSessionControls"},
  "state": "string"
}
```
