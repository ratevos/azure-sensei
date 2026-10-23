# Get unifiedRoleManagementPolicyAssignment

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedrolemanagementpolicyassignment-get?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Get the details of a policy assignment in PIM that's assigned to Microsoft Entra roles or group membership or ownership.

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

To retrieve the details of a policy assignment made in PIM for Microsoft Entra roles or PIM for Groups membership and ownership:

```http
GET /policies/roleManagementPolicyAssignments/{unifiedRoleManagementPolicyAssignmentId}
```

## Optional query parameters
This method supports the `$select` and `$expand` OData query parameters to help customize the response. You can also specify the wildcard value `*` to expand all supported relationships, that is, `?$expand=*`. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and an [unifiedRoleManagementPolicyAssignment](../resources/unifiedrolemanagementpolicyassignment.md) object in the response body.

## Examples

<a name='example-1-retrieve-the-details-of-a-policy-assignment-for-pim-for-azure-ad-roles'></a>

### Example 1: Retrieve the details of a policy assignment for PIM for Microsoft Entra roles

#### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/policies/roleManagementPolicyAssignments/Directory_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448_62e90394-69f5-4237-9190-012177145e10
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgPolicyRoleManagementPolicyAssignment -UnifiedRoleManagementPolicyAssignmentId $unifiedRoleManagementPolicyAssignmentId

```

---

#### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicyAssignments/$entity",
    "id": "Directory_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448_62e90394-69f5-4237-9190-012177145e10",
    "policyId": "Directory_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448",
    "scopeId": "/",
    "scopeType": "Directory",
    "roleDefinitionId": "62e90394-69f5-4237-9190-012177145e10"
}
```

<a name='example-2-retrieve-the-details-of-a-policy-assignment-for-pim-for-azure-ad-roles-and-expand-the-policy-and-its-associated-rules'></a>

### Example 2: Retrieve the details of a policy assignment for PIM for Microsoft Entra roles and expand the policy and its associated rules

#### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/policies/roleManagementPolicyAssignments/Directory_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448_62e90394-69f5-4237-9190-012177145e10?$expand=policy($expand=rules)
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgPolicyRoleManagementPolicyAssignment -UnifiedRoleManagementPolicyAssignmentId $unifiedRoleManagementPolicyAssignmentId -ExpandProperty "policy(`$expand=rules)" 

```

---

#### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicyAssignments(policy(rules()))/$entity",
    "id": "Directory_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448_62e90394-69f5-4237-9190-012177145e10",
    "policyId": "Directory_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448",
    "scopeId": "/",
    "scopeType": "Directory",
    "roleDefinitionId": "62e90394-69f5-4237-9190-012177145e10",
    "policy": {
        "id": "Directory_cab01047-8ad9-4792-8e42-569340767f1b_70c808b5-0d35-4863-a0ba-07888e99d448",
        "displayName": "Directory",
        "description": "Directory",
        "isOrganizationDefault": false,
        "scopeId": "/",
        "scopeType": "Directory",
        "lastModifiedDateTime": null,
        "lastModifiedBy": {
            "displayName": null,
            "id": null
        },
        "rules": [
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
}
```

### Example 3: Retrieve the details of a policy assignment for PIM for Groups

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/policies/roleManagementPolicyAssignments/Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369_member
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

Get-MgPolicyRoleManagementPolicyAssignment -UnifiedRoleManagementPolicyAssignmentId $unifiedRoleManagementPolicyAssignmentId

```

---

#### Response

The following example shows the response.

>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicyAssignments/$entity",
    "id": "Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369_member",
    "policyId": "Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369",
    "scopeId": "60bba733-f09d-49b7-8445-32369aa066b3",
    "scopeType": "Group",
    "roleDefinitionId": "member"
}
```
