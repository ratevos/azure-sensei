# Create roleEligibilityScheduleRequest

> Source: https://learn.microsoft.com/en-us/graph/api/rbacapplication-post-roleeligibilityschedulerequests?view=graph-rest-1.0  
> Microsoft doc last updated: 08/01/2024

Namespace: microsoft.graph

In PIM, request for a role eligibility for a principal through the [unifiedRoleEligibilityScheduleRequest](../resources/unifiedroleeligibilityschedulerequest.md) object. This operation allows both admins and eligible users to add, revoke, or extend eligible assignments.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|RoleEligibilitySchedule.ReadWrite.Directory|RoleManagement.ReadWrite.Directory|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|RoleEligibilitySchedule.ReadWrite.Directory|RoleManagement.ReadWrite.Directory|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - For read operations: *Global Reader*, *Security Operator*, *Security Reader*, *Security Administrator*, or *Privileged Role Administrator*
> - For write operations: *Privileged Role Administrator*

## HTTP request

```http
POST /roleManagement/directory/roleEligibilityScheduleRequests
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body
In the request body, supply a JSON representation of the [unifiedRoleEligibilityScheduleRequest](../resources/unifiedroleeligibilityschedulerequest.md) object.

You can specify the following properties when creating an **unifiedRoleEligibilityScheduleRequest**.

|Property|Type|Description|
|:---|:---|:---|
|action|unifiedRoleScheduleRequestActions|Represents the type of operation on the role eligibility request.The possible values are: `adminAssign`, `adminUpdate`, `adminRemove`, `selfActivate`, `selfDeactivate`, `adminExtend`, `adminRenew`, `selfExtend`, `selfRenew`, `unknownFutureValue`. <br/><ul><li>`adminAssign`: For administrators to assign eligible roles to principals.</li><li>`adminRemove`: For administrators to remove eligible roles from principals.</li><li> `adminUpdate`: For administrators to change existing role eligibilities.</li><li>`adminExtend`: For administrators to extend expiring role eligibilities.</li><li>`adminRenew`: For administrators to renew expired eligibilities.</li><li>`selfActivate`: For users to activate their assignments.</li><li>`selfDeactivate`: For users to deactivate their active assignments.</li><li>`selfExtend`: For users to request to extend their expiring assignments.</li><li>`SelfRenew`: For users to request to renew their expired assignments.</li></ul>|
|appScopeId|String|Identifier of the app-specific scope when the role eligibility is scoped to an app. The scope of a role eligibility determines the set of resources for which the principal is eligible to access. App scopes are scopes that are defined and understood by this application only. Use `/` for tenant-wide app scopes. Use **directoryScopeId** to limit the scope to particular directory objects, for example, administrative units. Either **directoryScopeId** or **appScopeId** is required.|
|directoryScopeId|String|Identifier of the directory object representing the scope of the role eligibility. The scope of an role eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use `/` for tenant-wide scope. Use **appScopeId** to limit the scope to an application only. Either **directoryScopeId** or **appScopeId** is required.|
|isValidationOnly|Boolean|Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request. Optional.|
|justification|String|A message provided by users and administrators when create they create the **unifiedRoleEligibilityScheduleRequest** object.  <br/><br/>Optional for `selfDeactivate` and `adminRemove` actions; might be optional or required for other action types depending on the rules in the policy that's linked to the Microsoft Entra role. For more information, see [Rules in PIM](https://learn.microsoft.com/en-us/graph/identity-governance-pim-rules-overview).|
|principalId|String|Identifier of the principal that has been granted the role eligibility. Required.|
|roleDefinitionId|String|Identifier of the [unifiedRoleDefinition](../resources/unifiedroledefinition.md) object that is being assigned to the principal. Required.|
|scheduleInfo|[requestSchedule](../resources/requestschedule.md)|The period of the role eligibility. Optional when **action** is `adminRemove`. The period of eligibility is dependent on the [settings of the Microsoft Entra role](../api/unifiedrolemanagementpolicy-list-rules.md).|
|ticketInfo|[ticketInfo](../resources/ticketinfo.md)|Ticket details linked to the role eligibility request including details of the ticket number and ticket system.  <br/><br/>Optional for `selfDeactivate` and `adminRemove` actions; might be optional or required for other action types depending on the rules in the policy that's linked to the Microsoft Entra role. For more information, see [Rules in PIM](https://learn.microsoft.com/en-us/graph/identity-governance-pim-rules-overview).|

## Response

If successful, this method returns a `201 Created` response code and an [unifiedRoleEligibilityScheduleRequest](../resources/unifiedroleeligibilityschedulerequest.md) object in the response body.

## Examples

### Example 1: Admin to assign a role eligibility schedule request

#### Request

# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleRequests
Content-Type: application/json

{
    "action": "adminAssign",
    "justification": "Assign Attribute Assignment Admin eligibility to restricted user",
    "roleDefinitionId": "8424c6f0-a189-499e-bbd0-26c1753c96d4",
    "directoryScopeId": "/",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "scheduleInfo": {
        "startDateTime": "2022-04-10T00:00:00Z",
        "expiration": {
            "type": "afterDateTime",
            "endDateTime": "2024-04-10T00:00:00Z"
        }
    }
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	action = "adminAssign"
	justification = "Assign Attribute Assignment Admin eligibility to restricted user"
	roleDefinitionId = "8424c6f0-a189-499e-bbd0-26c1753c96d4"
	directoryScopeId = "/"
	principalId = "071cc716-8147-4397-a5ba-b2105951cc0b"
	scheduleInfo = @{
		startDateTime = [System.DateTime]::Parse("2022-04-10T00:00:00Z")
		expiration = @{
			type = "afterDateTime"
			endDateTime = [System.DateTime]::Parse("2024-04-10T00:00:00Z")
		}
	}
}

New-MgRoleManagementDirectoryRoleEligibilityScheduleRequest -BodyParameter $params

```

---

### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleEligibilityScheduleRequests/$entity",
    "id": "50877283-9d40-433c-bab8-7986dc10458a",
    "status": "Provisioned",
    "createdDateTime": "2022-04-12T09:05:39.7594064Z",
    "completedDateTime": "2022-04-12T09:05:41.8532931Z",
    "approvalId": null,
    "customData": null,
    "action": "adminAssign",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "roleDefinitionId": "8424c6f0-a189-499e-bbd0-26c1753c96d4",
    "directoryScopeId": "/",
    "appScopeId": null,
    "isValidationOnly": false,
    "targetScheduleId": "50877283-9d40-433c-bab8-7986dc10458a",
    "justification": "Assign Attribute Assignment Admin eligibility to restricted user",
    "createdBy": {
        "application": null,
        "device": null,
        "user": {
            "displayName": null,
            "id": "3fbd929d-8c56-4462-851e-0eb9a7b3a2a5"
        }
    },
    "scheduleInfo": {
        "startDateTime": "2022-04-12T09:05:41.8532931Z",
        "recurrence": null,
        "expiration": {
            "type": "afterDateTime",
            "endDateTime": "2024-04-10T00:00:00Z",
            "duration": null
        }
    },
    "ticketInfo": {
        "ticketNumber": null,
        "ticketSystem": null
    }
}
```

### Example 2: Admin to remove an existing role eligibility schedule request

In the following request, the admin creates a request to revoke the eligibility of a principal with ID `071cc716-8147-4397-a5ba-b2105951cc0b` to a role with ID `8424c6f0-a189-499e-bbd0-26c1753c96d4`.

#### Request

# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleRequests
Content-Type: application/json

{
    "action": "adminRemove",
    "roleDefinitionId": "8424c6f0-a189-499e-bbd0-26c1753c96d4",
    "directoryScopeId": "/",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b"
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	action = "adminRemove"
	roleDefinitionId = "8424c6f0-a189-499e-bbd0-26c1753c96d4"
	directoryScopeId = "/"
	principalId = "071cc716-8147-4397-a5ba-b2105951cc0b"
}

New-MgRoleManagementDirectoryRoleEligibilityScheduleRequest -BodyParameter $params

```

---

#### Response

The following example shows the response. The response object shows a previous role eligibility for a principal is `Revoked`. The principal will no longer see their previously eligible role.

>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleEligibilityScheduleRequests/$entity",
    "id": "f341269e-c926-41fa-a905-cef3b01b2a67",
    "status": "Revoked",
    "createdDateTime": "2022-04-12T09:12:15.6859992Z",
    "completedDateTime": null,
    "approvalId": null,
    "customData": null,
    "action": "adminRemove",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "roleDefinitionId": "8424c6f0-a189-499e-bbd0-26c1753c96d4",
    "directoryScopeId": "/",
    "appScopeId": null,
    "isValidationOnly": false,
    "targetScheduleId": null,
    "justification": null,
    "scheduleInfo": null,
    "createdBy": {
        "application": null,
        "device": null,
        "user": {
            "displayName": null,
            "id": "3fbd929d-8c56-4462-851e-0eb9a7b3a2a5"
        }
    },
    "ticketInfo": {
        "ticketNumber": null,
        "ticketSystem": null
    }
}
```
