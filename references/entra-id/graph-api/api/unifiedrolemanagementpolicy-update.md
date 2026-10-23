# Update unifiedRoleManagementPolicy

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedrolemanagementpolicy-update?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Update the details of a role management policy [unifiedRoleManagementPolicy](../resources/unifiedrolemanagementpolicy.md) object.

## Permissions
One of the following permissions is required to call this API. To learn more, including how to choose permissions, see [Permissions](https://learn.microsoft.com/en-us/graph/permissions-reference).

<a name='for-pim-for-azure-ad-roles'></a>

### For PIM for Microsoft Entra roles

|Permission type|Permissions (from least to most privileged)|
|:---|:---|
|Delegated (work or school account)|RoleManagementPolicy.ReadWrite.Directory, RoleManagement.ReadWrite.Directory|
|Delegated (personal Microsoft account)|Not supported.|
|Application|RoleManagementPolicy.ReadWrite.Directory, RoleManagement.ReadWrite.Directory|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - For read operations: *Global Reader*, *Security Operator*, *Security Reader*, *Security Administrator*, or *Privileged Role Administrator*
> - For write operations: *Privileged Role Administrator*

### For PIM for Groups

|Permission type|Permissions (from least to most privileged)|
|:---|:---|
|Delegated (work or school account)|RoleManagementPolicy.ReadWrite.AzureADGroup|
|Delegated (personal Microsoft account)|Not supported.|
|Application|RoleManagementPolicy.ReadWrite.AzureADGroup|

## HTTP request

To update the details of a role management policy for either Microsoft Entra roles or groups:

```http
PATCH /policies/roleManagementPolicies/{unifiedRoleManagementPolicyId}
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body

|Property|Type|Description|
|:---|:---|:---|
|rules|[unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) collection |The list of policy rules to be updated.|

## Response

If successful, this method returns a `200 OK` response code and an [unifiedRoleManagementPolicy](../resources/unifiedrolemanagementpolicy.md) object in the response body.

## Examples

<a name='example-1-update-the-details-of-a-policy-defined-in-pim-for-azure-ad-roles'></a>

### Example 1: Update the details of a policy defined in PIM for Microsoft Entra roles

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
PATCH https://graph.microsoft.com/v1.0/policies/roleManagementPolicies/DirectoryRole_2132228a-d66e-401c-ab8a-a8ae31254a36_0f8c4bbc-4f1a-421c-b63d-a68f571b7fab
Content-Type: application/json

{
  "rules": [
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
      "id": "Expiration_Admin_Eligibility",
      "isExpirationRequired": false,
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
    }
  ]
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	rules = @(
		@{
			"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule"
			id = "Approval_EndUser_Assignment"
			target = @{
				caller = "EndUser"
				operations = @(
				"All"
			)
			level = "Assignment"
			inheritableSettings = @(
			)
			enforcedSettings = @(
			)
		}
		setting = @{
			isApprovalRequired = $false
			isApprovalRequiredForExtension = $false
			isRequestorJustificationRequired = $true
			approvalMode = "SingleStage"
			approvalStages = @(
				@{
					approvalStageTimeOutInDays = 
					isApproverJustificationRequired = $true
					escalationTimeInMinutes = 
					isEscalationEnabled = $false
					primaryApprovers = @(
					)
					escalationApprovers = @(
					)
				}
			)
		}
	}
	@{
		"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule"
		id = "AuthenticationContext_EndUser_Assignment"
		isEnabled = $false
		claimValue = ""
		target = @{
			caller = "EndUser"
			operations = @(
			"All"
		)
		level = "Assignment"
		inheritableSettings = @(
		)
		enforcedSettings = @(
		)
	}
}
@{
	"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule"
	id = "Enablement_Admin_Eligibility"
	enabledRules = @(
	)
	target = @{
		caller = "Admin"
		operations = @(
		"All"
	)
	level = "Eligibility"
	inheritableSettings = @(
	)
	enforcedSettings = @(
	)
}
}
@{
"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule"
id = "Expiration_Admin_Eligibility"
isExpirationRequired = $false
maximumDuration = "P365D"
target = @{
	caller = "Admin"
	operations = @(
	"All"
)
level = "Eligibility"
inheritableSettings = @(
)
enforcedSettings = @(
)
}
}
@{
"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule"
id = "Notification_Admin_Admin_Eligibility"
notificationType = "Email"
recipientType = "Admin"
notificationLevel = "All"
isDefaultRecipientsEnabled = $true
notificationRecipients = @(
)
target = @{
caller = "Admin"
operations = @(
"All"
)
level = "Eligibility"
inheritableSettings = @(
)
enforcedSettings = @(
)
}
}
)
}

Update-MgPolicyRoleManagementPolicy -UnifiedRoleManagementPolicyId $unifiedRoleManagementPolicyId -BodyParameter $params

```

---

#### Response

The following example shows the response.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicies/$entity",
    "id": "DirectoryRole_2132228a-d66e-401c-ab8a-a8ae31254a36_0f8c4bbc-4f1a-421c-b63d-a68f571b7fab",
    "displayName": "DirectoryRole",
    "description": "DirectoryRole",
    "isOrganizationDefault": false,
    "scopeId": "/",
    "scopeType": "DirectoryRole",
    "lastModifiedDateTime": "2023-10-01T19:27:32.663Z",
    "lastModifiedBy": {
        "displayName": "Test User 1",
        "id": null
    }
}
```

### Example 2: Update the details of a policy defined in PIM for Groups

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
PATCH https://graph.microsoft.com/v1.0/policies/roleManagementPolicies/Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369
Content-Type: application/json

{
  "rules": [
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
        "isApprovalRequired": true,
        "isApprovalRequiredForExtension": false,
        "isRequestorJustificationRequired": true,
        "approvalMode": "SingleStage",
        "approvalStages": [
          {
            "approvalStageTimeOutInDays": 1,
            "isApproverJustificationRequired": true,
            "escalationTimeInMinutes": 0,
            "isEscalationEnabled": false,
            "primaryApprovers": [
              {
                "@odata.type": "#microsoft.graph.singleUser",
                "isBackup": false,
                "id": "c277c8cb-6bb7-42e5-a17f-0add9a718151",
                "description": null
              }
            ],
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
    }
  ]
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	rules = @(
		@{
			"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule"
			id = "Approval_EndUser_Assignment"
			target = @{
				caller = "EndUser"
				operations = @(
				"All"
			)
			level = "Assignment"
			inheritableSettings = @(
			)
			enforcedSettings = @(
			)
		}
		setting = @{
			isApprovalRequired = $true
			isApprovalRequiredForExtension = $false
			isRequestorJustificationRequired = $true
			approvalMode = "SingleStage"
			approvalStages = @(
				@{
					approvalStageTimeOutInDays = 
					isApproverJustificationRequired = $true
					escalationTimeInMinutes = 
					isEscalationEnabled = $false
					primaryApprovers = @(
						@{
							"@odata.type" = "#microsoft.graph.singleUser"
							isBackup = $false
							id = "c277c8cb-6bb7-42e5-a17f-0add9a718151"
							description = $null
						}
					)
					escalationApprovers = @(
					)
				}
			)
		}
	}
	@{
		"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule"
		id = "AuthenticationContext_EndUser_Assignment"
		isEnabled = $false
		claimValue = ""
		target = @{
			caller = "EndUser"
			operations = @(
			"All"
		)
		level = "Assignment"
		inheritableSettings = @(
		)
		enforcedSettings = @(
		)
	}
}
@{
	"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule"
	id = "Enablement_Admin_Eligibility"
	enabledRules = @(
	)
	target = @{
		caller = "Admin"
		operations = @(
		"All"
	)
	level = "Eligibility"
	inheritableSettings = @(
	)
	enforcedSettings = @(
	)
}
}
@{
"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule"
id = "Expiration_Admin_Eligibility"
isExpirationRequired = $true
maximumDuration = "P365D"
target = @{
	caller = "Admin"
	operations = @(
	"All"
)
level = "Eligibility"
inheritableSettings = @(
)
enforcedSettings = @(
)
}
}
@{
"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule"
id = "Notification_Admin_Admin_Eligibility"
notificationType = "Email"
recipientType = "Admin"
notificationLevel = "All"
isDefaultRecipientsEnabled = $true
notificationRecipients = @(
)
target = @{
caller = "Admin"
operations = @(
"All"
)
level = "Eligibility"
inheritableSettings = @(
)
enforcedSettings = @(
)
}
}
)
}

Update-MgPolicyRoleManagementPolicy -UnifiedRoleManagementPolicyId $unifiedRoleManagementPolicyId -BodyParameter $params

```

---

#### Response

The following example shows the response.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicies/$entity",
    "id": "Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369",
    "displayName": "Group",
    "description": "Group",
    "isOrganizationDefault": false,
    "scopeId": "60bba733-f09d-49b7-8445-32369aa066b3",
    "scopeType": "Group",
    "lastModifiedDateTime": "2023-10-01T23:29:43.687Z",
    "lastModifiedBy": {
        "displayName": "Test User 1",
        "id": null
    }
}
```
