# unifiedRoleManagementPolicyApprovalRule resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/unifiedrolemanagementpolicyapprovalrule?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

A type derived from the [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) resource type that defines rules for approving a role assignment.

## Methods

None.

## Properties
|Property|Type|Description|
|:---|:---|:---|
|id|String|Identifier for the rule. Inherited from [entity](../resources/entity.md).|
|setting|[approvalSettings](../resources/approvalsettings.md)|The settings for approval of the role assignment.|
|target|[unifiedRoleManagementPolicyRuleTarget](../resources/unifiedrolemanagementpolicyruletarget.md)|Defines details of the scope that's targeted by the approval rule. The details can include the principal type, the role assignment type, and actions affecting a role. Inherited from [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md). Supports `$filter` (`eq`, `ne`).|

## Relationships
None.

## JSON representation
The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule",
  "id": "String (identifier)",
  "target": {
    "@odata.type": "microsoft.graph.unifiedRoleManagementPolicyRuleTarget"
  },
  "setting": {
    "@odata.type": "microsoft.graph.approvalSettings"
  }
}
```
