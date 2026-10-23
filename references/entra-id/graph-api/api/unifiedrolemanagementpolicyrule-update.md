# Update unifiedRoleManagementPolicyRule

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedrolemanagementpolicyrule-update?view=graph-rest-1.0  
> Microsoft doc last updated: 09/16/2026

Namespace: microsoft.graph

Update a rule defined for a role management policy. The rule can be one of the following types that are derived from the [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) object:

+ [unifiedRoleManagementPolicyApprovalRule](../resources/unifiedrolemanagementpolicyapprovalrule.md)
+ [unifiedRoleManagementPolicyAuthenticationContextRule](../resources/unifiedrolemanagementpolicyauthenticationcontextrule.md)
+ [unifiedRoleManagementPolicyCustomExtensionRule](../resources/unifiedrolemanagementpolicycustomextensionrule.md)
+ [unifiedRoleManagementPolicyEnablementRule](../resources/unifiedrolemanagementpolicyenablementrule.md)
+ [unifiedRoleManagementPolicyExpirationRule](../resources/unifiedrolemanagementpolicyexpirationrule.md)
+ [unifiedRoleManagementPolicyNotificationRule](../resources/unifiedrolemanagementpolicynotificationrule.md)

For more information about rules for Microsoft Entra roles and examples of updating rules, see the following articles:

+ [Overview of rules for Microsoft Entra roles in PIM APIs in Microsoft Graph](https://learn.microsoft.com/en-us/graph/identity-governance-pim-rules-overview)
+ [Use PIM APIs in Microsoft Graph to update Microsoft Entra ID rules](https://learn.microsoft.com/en-us/graph/how-to-pim-update-rules)

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

To update a rule defined for a policy for either Microsoft Entra roles or groups in PIM:

```http
PATCH /policies/roleManagementPolicies/{unifiedRoleManagementPolicyId}/rules/{unifiedRoleManagementPolicyRuleId}
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body

|Property|Type|Description|
|:---|:---|:---|
|claimValue|String|The value of the authentication context claim. <br/><br/>Can be updated for the **unifiedRoleManagementPolicyAuthenticationContextRule** rule type.|
|customExtensionId|String|The unique identifier of the PIM custom extension associated with the rule.<br/><br/>Can be updated for the **unifiedRoleManagementPolicyCustomExtensionRule** rule type.|
|enabledRules|String collection|The collection of rules that are enabled for this policy rule. For example, `MultiFactorAuthentication`, `Ticketing`, and `Justification`.<br/><br/>Can be updated for the **unifiedRoleManagementPolicyEnablementRule** rule type.|
|isDefaultRecipientsEnabled|Boolean|Indicates whether a default recipient will receive the notification email.<br/><br/>Can be updated for the **unifiedRoleManagementPolicyNotificationRule** rule type.|
|isEnabled|Boolean|Whether this rule is enabled. <br/><br/>Can be updated for the **unifiedRoleManagementPolicyAuthenticationContextRule** and **unifiedRoleManagementPolicyCustomExtensionRule** rule types.|
|isExpirationRequired|Boolean|Indicates whether expiration is required or if it's a permanently active assignment or eligibility. <br/><br/>Can be updated for the **unifiedRoleManagementPolicyExpirationRule** rule type.|
|maximumDuration|Duration| The maximum duration allowed for eligibility or assignment which is not permanent. Required when **isExpirationRequired** is `true`. <br/><br/>Can be updated for the **unifiedRoleManagementPolicyExpirationRule** rule type. |
|notificationLevel|String|The level of notification. The possible values are `None`, `Critical`, `All`.<br/><br/>Can be updated for the **unifiedRoleManagementPolicyNotificationRule** rule type.|
|notificationRecipients|String collection|The list of recipients of the email notifications.<br/><br/>Can be updated for the **unifiedRoleManagementPolicyNotificationRule** rule type.|
|notificationType|String|The type of notification. Only `Email` is supported.<br/><br/>Can be updated for the **unifiedRoleManagementPolicyNotificationRule** rule type.|
|recipientType|String|The type of recipient of the notification. The possible values are `Requestor`, `Approver`, `Admin`.<br/>Can be updated for the **unifiedRoleManagementPolicyNotificationRule** rule type.|
|setting|[approvalSettings](../resources/approvalsettings.md)|The settings for approval of the role assignment. <br/><br/>Can be updated for the **unifiedRoleManagementPolicyApprovalRule** rule type.|
|target|[unifiedRoleManagementPolicyRuleTarget](../resources/unifiedrolemanagementpolicyruletarget.md)|Defines details of the scope that's targeted by role management policy rule. The details can include the principal type, the role assignment type, and actions affecting a role. <br/><br/> Can be updated for all rule types.|

>**Note:** The `@odata.type` property with a value of the specific rule type must be included in the body. For example, `"@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule"`.

## Response

If successful, this method returns a `200 OK` response code and an [unifiedRoleManagementPolicyRule](../resources/unifiedrolemanagementpolicyrule.md) object in the response body.

## Examples

<a name='example-1-update-a-rule-defined-for-a-policy-in-pim-for-azure-ad-roles'></a>

### Example 1: Update a rule defined for a policy in PIM for Microsoft Entra roles

#### Request

The following example updates a role management policy rule of type **unifiedRoleManagementPolicyExpirationRule** and with ID is `Expiration_EndUser_Assignment`.

# [HTTP](#tab/http)

```http
PATCH https://graph.microsoft.com/v1.0/policies/roleManagementPolicies/DirectoryRole_84841066-274d-4ec0-a5c1-276be684bdd3_200ec19a-09e7-4e7a-9515-cf1ee64b96f9/rules/Expiration_EndUser_Assignment
Content-Type: application/json

{
    "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
    "id": "Expiration_EndUser_Assignment",
    "isExpirationRequired": true,
    "maximumDuration": "PT1H45M",
    "target": {
        "@odata.type": "microsoft.graph.unifiedRoleManagementPolicyRuleTarget",
        "caller": "EndUser",
        "operations": [
            "All"
        ],
        "level": "Assignment",
        "inheritableSettings": [],
        "enforcedSettings": []
    }
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule"
	id = "Expiration_EndUser_Assignment"
	isExpirationRequired = $true
	maximumDuration = "PT1H45M"
	target = @{
		"@odata.type" = "microsoft.graph.unifiedRoleManagementPolicyRuleTarget"
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

Update-MgPolicyRoleManagementPolicyRule -UnifiedRoleManagementPolicyId $unifiedRoleManagementPolicyId -UnifiedRoleManagementPolicyRuleId $unifiedRoleManagementPolicyRuleId -BodyParameter $params

```

---

#### Response

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicies('DirectoryRole_84841066-274d-4ec0-a5c1-276be684bdd3_200ec19a-09e7-4e7a-9515-cf1ee64b96f9')/rules/$entity",
    "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
    "id": "Expiration_EndUser_Assignment",
    "isExpirationRequired": true,
    "maximumDuration": "PT1H45M",
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
```

### Example 2: Update a rule defined for a policy in PIM for Groups

#### Request

The following example updates a role management policy rule with ID `Expiration_EndUser_Assignment`.

# [HTTP](#tab/http)

```http
PATCH https://graph.microsoft.com/v1.0/policies/roleManagementPolicies/Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369/rules/Expiration_EndUser_Assignment
Content-Type: application/json

{
    "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
    "id": "Expiration_EndUser_Assignment",
    "isExpirationRequired": true,
    "maximumDuration": "PT1H45M",
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
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.SignIns

$params = @{
	"@odata.type" = "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule"
	id = "Expiration_EndUser_Assignment"
	isExpirationRequired = $true
	maximumDuration = "PT1H45M"
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

Update-MgPolicyRoleManagementPolicyRule -UnifiedRoleManagementPolicyId $unifiedRoleManagementPolicyId -UnifiedRoleManagementPolicyRuleId $unifiedRoleManagementPolicyRuleId -BodyParameter $params

```

---

#### Response

The following example shows the response.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/roleManagementPolicies('Group_60bba733-f09d-49b7-8445-32369aa066b3_f21b26d9-9ff9-4af1-b1d4-bddf28591369')/rules/$entity",
    "@odata.type": "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule",
    "id": "Expiration_EndUser_Assignment",
    "isExpirationRequired": true,
    "maximumDuration": "PT1H45M",
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
```

## Related content

+ [Overview of rules for Microsoft Entra roles in PIM APIs in Microsoft Graph](https://learn.microsoft.com/en-us/graph/identity-governance-pim-rules-overview)
+ [Use PIM APIs in Microsoft Graph to update Microsoft Entra ID rules](https://learn.microsoft.com/en-us/graph/how-to-pim-update-rules)
