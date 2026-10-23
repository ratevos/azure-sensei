# List rules (for a role management policy)

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedrolemanagementpolicy-list-rules?view=graph-rest-1.0  
> Microsoft doc last updated: 09/16/2026

Namespace: microsoft.graph

Get the rules or settings defined for a role management policy. The rules are a collection of following types that are derived from the [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) object:

+ [unifiedRoleManagementPolicyApprovalRule](../resources/unifiedrolemanagementpolicyapprovalrule.md)
+ [unifiedRoleManagementPolicyAuthenticationContextRule](../resources/unifiedrolemanagementpolicyauthenticationcontextrule.md)
+ [unifiedRoleManagementPolicyCustomExtensionRule](../resources/unifiedrolemanagementpolicycustomextensionrule.md)
+ [unifiedRoleManagementPolicyEnablementRule](../resources/unifiedrolemanagementpolicyenablementrule.md)
+ [unifiedRoleManagementPolicyExpirationRule](../resources/unifiedrolemanagementpolicyexpirationrule.md)
+ [unifiedRoleManagementPolicyNotificationRule](../resources/unifiedrolemanagementpolicynotificationrule.md)

## Permissions
One of the following permissions is required to call this API. To learn more, including how to choose permissions, see [Permissions](https://learn.microsoft.com/en-us/graph/permissions-reference).

<a name='for-pim-for-azure-ad-roles'></a>

### For PIM for Microsoft Entra roles

|Permission type|Permissions (from least to most privileged)|
|:---|:---|
|Delegated (work or school account)|RoleManagementPolicy.Read.Directory, RoleManagement.Read.Directory, RoleManagement.Read.All, RoleManagementPolicy.ReadWrite.Directory, RoleManagement.ReadWrite.Directory|
|Delegated (personal Microsoft account)|Not supported.|
|Application|RoleManagementPolicy.Read.Directory, RoleManagement.Read.Directory, RoleManagement.Read.All, RoleManagementPolicy.ReadWrite.Directory, RoleManagement.ReadWrite.Directory|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - For read operations: *Global Reader*, *Security Operator*, *Security Reader*, *Security Administrator*, or *Privileged Role Administrator*
> - For write operations: *Privileged Role Administrator*

### For PIM for Groups

|Permission type|Permissions (from least to most privileged)|
|:---|:---|
|Delegated (work or school account)|RoleManagementPolicy.Read.AzureADGroup, RoleManagementPolicy.ReadWrite.AzureADGroup|
|Delegated (personal Microsoft account)|Not supported.|
|Application|RoleManagementPolicy.Read.AzureADGroup, RoleManagementPolicy.ReadWrite.AzureADGroup|

## HTTP request

To retrieve rules in a policy for either Microsoft Entra roles or groups:

```http
GET /policies/roleManagementPolicies/{unifiedRoleManagementPolicyId}/rules
```

## Optional query parameters
This method supports the `$select` and `$filter` OData query parameters to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) objects in the response body.

## Examples

<a name='example-1-retrieve-rules-of-a-policy-in-pim-for-azure-ad-roles'></a>

### Example 1: Retrieve rules of a policy in PIM for Microsoft Entra roles

#### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/policies/roleManagementPolicies/DirectoryRole_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448/rules
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgPolicyRoleManagementPolicyRule -UnifiedRoleManagementPolicyId $unifiedRoleManagementPolicyId

```

---

#### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicies('DirectoryRole_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448')/rules",
    "value": [
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
            "id": "Expiration_Admin_Eligibility",
            "isExpirationRequired": false,
            "maximumDuration": "P365D",
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule",
            "id": "Enablement_Admin_Eligibility",
            "enabledRules": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Admin_Admin_Eligibility",
            "notificationType": "Email",
            "recipientType": "Admin",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Requestor_Admin_Eligibility",
            "notificationType": "Email",
            "recipientType": "Requestor",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Approver_Admin_Eligibility",
            "notificationType": "Email",
            "recipientType": "Approver",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
            "id": "Expiration_Admin_Assignment",
            "isExpirationRequired": false,
            "maximumDuration": "P180D",
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule",
            "id": "Enablement_Admin_Assignment",
            "enabledRules": [
                "Justification"
            ],
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Admin_Admin_Assignment",
            "notificationType": "Email",
            "recipientType": "Admin",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Requestor_Admin_Assignment",
            "notificationType": "Email",
            "recipientType": "Requestor",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Approver_Admin_Assignment",
            "notificationType": "Email",
            "recipientType": "Approver",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
            "id": "Expiration_EndUser_Assignment",
            "isExpirationRequired": true,
            "maximumDuration": "PT8H",
            "target": {
                "caller": "EndUser",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule",
            "id": "Enablement_EndUser_Assignment",
            "enabledRules": [
                "MultiFactorAuthentication",
                "Justification"
            ],
            "target": {
                "caller": "EndUser",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule",
            "id": "Approval_EndUser_Assignment",
            "target": {
                "caller": "EndUser",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            },
            "setting": {
                "isApprovalRequired": false,
                "isApprovalRequiredForExtension": false,
                "isRequestorJustificationRequired": true,
                "approvalMode": "SingleStage",
                "approvalStages": [
                    {
                        "approvalStageTimeOutInDays": 1,
                        "isApproverJustificationRequired": true,
                        "escalationTimeInMinutes": 0,
                        "isEscalationEnabled": false,
                        "primaryApprovers": [],
                        "escalationApprovers": []
                    }
                ]
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule",
            "id": "AuthenticationContext_EndUser_Assignment",
            "isEnabled": false,
            "claimValue": null,
            "target": {
                "caller": "EndUser",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Admin_EndUser_Assignment",
            "notificationType": "Email",
            "recipientType": "Admin",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "EndUser",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Requestor_EndUser_Assignment",
            "notificationType": "Email",
            "recipientType": "Requestor",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "EndUser",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Approver_EndUser_Assignment",
            "notificationType": "Email",
            "recipientType": "Approver",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "EndUser",
                "operations": [
                    "all"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        }
    ]
}
```

### Example 2: Retrieve rules of a policy in PIM for Groups

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/policies/roleManagementPolicies/Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369/rules
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgPolicyRoleManagementPolicyRule -UnifiedRoleManagementPolicyId $unifiedRoleManagementPolicyId

```

---

#### Response

The following example shows the response.

**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicies('Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369')/rules",
    "value": [
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
            "id": "Expiration_Admin_Eligibility",
            "isExpirationRequired": true,
            "maximumDuration": "P365D",
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Admin_Admin_Eligibility",
            "notificationType": "Email",
            "recipientType": "Admin",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Requestor_Admin_Eligibility",
            "notificationType": "Email",
            "recipientType": "Requestor",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Approver_Admin_Eligibility",
            "notificationType": "Email",
            "recipientType": "Approver",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule",
            "id": "Enablement_Admin_Eligibility",
            "enabledRules": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Eligibility",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
            "id": "Expiration_Admin_Assignment",
            "isExpirationRequired": true,
            "maximumDuration": "P180D",
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule",
            "id": "Enablement_Admin_Assignment",
            "enabledRules": [
                "Justification"
            ],
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Admin_Admin_Assignment",
            "notificationType": "Email",
            "recipientType": "Admin",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Requestor_Admin_Assignment",
            "notificationType": "Email",
            "recipientType": "Requestor",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Approver_Admin_Assignment",
            "notificationType": "Email",
            "recipientType": "Approver",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "Admin",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
            "id": "Expiration_EndUser_Assignment",
            "isExpirationRequired": true,
            "maximumDuration": "PT7H",
            "target": {
                "caller": "EndUser",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule",
            "id": "Enablement_EndUser_Assignment",
            "enabledRules": [
                "Justification"
            ],
            "target": {
                "caller": "EndUser",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule",
            "id": "Approval_EndUser_Assignment",
            "target": {
                "caller": "EndUser",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            },
            "setting": {
                "isApprovalRequired": false,
                "isApprovalRequiredForExtension": false,
                "isRequestorJustificationRequired": true,
                "approvalMode": "SingleStage",
                "approvalStages": [
                    {
                        "approvalStageTimeOutInDays": 1,
                        "isApproverJustificationRequired": true,
                        "escalationTimeInMinutes": 0,
                        "isEscalationEnabled": false,
                        "primaryApprovers": [],
                        "escalationApprovers": []
                    }
                ]
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule",
            "id": "AuthenticationContext_EndUser_Assignment",
            "isEnabled": false,
            "claimValue": "",
            "target": {
                "caller": "EndUser",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Admin_EndUser_Assignment",
            "notificationType": "Email",
            "recipientType": "Admin",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "EndUser",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Requestor_EndUser_Assignment",
            "notificationType": "Email",
            "recipientType": "Requestor",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "EndUser",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        },
        {
            "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule",
            "id": "Notification_Approver_EndUser_Assignment",
            "notificationType": "Email",
            "recipientType": "Approver",
            "notificationLevel": "All",
            "isDefaultRecipientsEnabled": true,
            "notificationRecipients": [],
            "target": {
                "caller": "EndUser",
                "operations": [
                    "All"
                ],
                "level": "Assignment",
                "inheritableSettings": [],
                "enforcedSettings": []
            }
        }
    ]
}
```
