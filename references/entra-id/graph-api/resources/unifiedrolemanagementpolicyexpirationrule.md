# unifiedRoleManagementPolicyExpirationRule resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/unifiedrolemanagementpolicyexpirationrule?view=graph-rest-1.0  
> Microsoft doc last updated: 04/03/2024


Namespace: microsoft.graph

A type derived from the [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) resource type that defines the maximum duration a role can be assigned to a principal (either through direct assignment or through activation of eligibility).

## Methods

None.

## Properties
|Property|Type|Description|
|:---|:---|:---|
|id|String|Identifier for the rule. Inherited from [entity](../resources/entity.md).|
|isExpirationRequired|Boolean|Indicates whether expiration is required or if it's a permanently active assignment or eligibility. |
|maximumDuration|Duration| The maximum duration allowed for eligibility or assignment that isn't permanent. Required when **isExpirationRequired** is `true`. |
|target|[unifiedRoleManagementPolicyRuleTarget](../resources/unifiedrolemanagementpolicyruletarget.md)|Defines details of the scope that's targeted by the expiration rule. The details can include the principal type, the role assignment type, and actions affecting a role. Inherited from [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md). Supports `$filter` (`eq`, `ne`).|

## Relationships
None.

## JSON representation
The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
  "id": "String (identifier)",
  "target": {
    "@odata.type": "microsoft.graph.unifiedRoleManagementPolicyRuleTarget"
  },
  "isExpirationRequired": "Boolean",
  "maximumDuration": "String (duration)"
}
```
