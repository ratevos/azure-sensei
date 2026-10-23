# unifiedRoleManagementPolicyNotificationRule resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/unifiedrolemanagementpolicynotificationrule?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

A type derived from the [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) resource type that defines the email notification rules for role assignments, activations, and approvals.

Inherits from [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md).

## Methods

None.

## Properties
|Property|Type|Description|
|:---|:---|:---|
|id|String|Identifier for the rule. Inherited from [entity](../resources/entity.md).|
|isDefaultRecipientsEnabled|Boolean|Indicates whether a default recipient will receive the notification email.|
|notificationLevel|String|The level of notification. The possible values are `None`, `Critical`, `All`.|
|notificationRecipients|String collection|The list of recipients of the email notifications.|
|notificationType|String|The type of notification. Only `Email` is supported.|
|recipientType|String|The type of recipient of the notification. The possible values are `Requestor`, `Approver`, `Admin`.|
|target|[unifiedRoleManagementPolicyRuleTarget](../resources/unifiedrolemanagementpolicyruletarget.md)|Defines details of the scope that's targeted by the notification rule. The details can include the principal type, the role assignment type, and actions affecting a role. Inherited from [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md). Supports `$filter` (`eq`, `ne`).|

## Relationships
None.

## JSON representation
The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
  "id": "String (identifier)",
  "target": {
    "@odata.type": "microsoft.graph.unifiedRoleManagementPolicyRuleTarget"
  },
  "notificationType": "String",
  "recipientType": "String",
  "notificationLevel": "String",
  "isDefaultRecipientsEnabled": "Boolean",
  "notificationRecipients": [
    "String"
  ]
}
```
