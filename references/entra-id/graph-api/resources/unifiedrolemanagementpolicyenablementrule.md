# unifiedRoleManagementPolicyEnablementRule resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/unifiedrolemanagementpolicyenablementrule?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

A type derived from the [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) resource type that defines the rules to enable the assignment, for example, enable MFA, justification on assignments or ticketing information.

## Methods

None.

## Properties
|Property|Type|Description|
|:---|:---|:---|
|enabledRules|String collection|The collection of rules that are enabled for this policy rule. For example, `MultiFactorAuthentication`, `Ticketing`, and `Justification`.|
|id|String|Identifier for the rule. Inherited from [entity](../resources/entity.md).|
|target|[unifiedRoleManagementPolicyRuleTarget](../resources/unifiedrolemanagementpolicyruletarget.md)|Defines details of the scope that's targeted by the enablement rule. The details can include the principal type, the role assignment type, and actions affecting a role. Inherited from [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md). Supports `$filter` (`eq`, `ne`).|

## Relationships
None.

## JSON representation
The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule",
  "id": "String (identifier)",
  "target": {
    "@odata.type": "microsoft.graph.unifiedRoleManagementPolicyRuleTarget"
  },
  "enabledRules": [
    "String"
  ]
}
```
