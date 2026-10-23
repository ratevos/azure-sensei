# Create roleAssignmentScheduleRequests

> Source: https://learn.microsoft.com/en-us/graph/api/rbacapplication-post-roleassignmentschedulerequests?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

In PIM, carry out the following operations through the [unifiedRoleAssignmentScheduleRequest](../resources/unifiedroleassignmentschedulerequest.md) object:

+ Request active and persistent role assignments for a principal, with or without expiry dates.
+ Activate, deactivate, extend, or renew an eligible role assignment for a principal.

To call this API to update, renew, and extend assignments for yourself, you must have multifactor authentication (MFA) enforced, and running the query in a session in which they were challenged for MFA. See [Enable per-user Microsoft Entra multifactor authentication to secure sign-in events](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-userstates).

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|RoleAssignmentSchedule.ReadWrite.Directory|RoleAssignmentSchedule.Remove.Directory, RoleEligibilitySchedule.Remove.Directory, RoleManagement.ReadWrite.Directory|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|RoleAssignmentSchedule.ReadWrite.Directory|RoleManagement.ReadWrite.Directory, RoleAssignmentSchedule.Remove.Directory, RoleEligibilitySchedule.Remove.Directory|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - For read operations: *Global Reader*, *Security Operator*, *Security Reader*, *Security Administrator*, or *Privileged Role Administrator*
> - For write operations: *Privileged Role Administrator*

## HTTP request

```http
POST /roleManagement/directory/roleAssignmentScheduleRequests
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body

In the request body, supply a JSON representation of the [unifiedRoleAssignmentScheduleRequest](../resources/unifiedroleassignmentschedulerequest.md) object.

You can specify the following properties when creating an **unifiedRoleAssignmentScheduleRequest**.

|Property|Type|Description|
|:---|:---|:---|
|action|unifiedRoleScheduleRequestActions|Represents the type of the operation on the role assignment request. The possible values are: `adminAssign`, `adminUpdate`, `adminRemove`, `selfActivate`, `selfDeactivate`, `adminExtend`, `adminRenew`, `selfExtend`, `selfRenew`, `unknownFutureValue`. <br/><ul><li>`adminAssign`: For administrators to assign roles to users or groups.</li><li>`adminRemove`: For administrators to remove users or groups from roles.</li><li> `adminUpdate`: For administrators to change existing role assignments.</li><li>`adminExtend`: For administrators to extend expiring assignments.</li><li>`adminRenew`: For administrators to renew expired assignments.</li><li>`selfActivate`: For users to activate their assignments.</li><li>`selfDeactivate`: For users to deactivate their active assignments.</li><li>`selfExtend`: For users to request to extend their expiring assignments.</li><li>`selfRenew`: For users to request to renew their expired assignments.</li></ul>|
|customData|String|Free text field to define any custom data for the request. Optional.|
|principalId|String|Identifier of the principal that has been granted the assignment. Required.|
|roleDefinitionId|String|Identifier of the [unifiedRoleDefinition](../resources/unifiedroledefinition.md) object that is being assigned. Required.|
|directoryScopeId|String|Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use `/` for tenant-wide scope. Use **appScopeId** to limit the scope to an application only. Either **directoryScopeId** or **appScopeId** is required.|
|appScopeId|String|Identifier of the app-specific scope when the assignment is scoped to an app. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use `/` for tenant-wide app scopes. Use **directoryScopeId** to limit the scope to particular directory objects, for example, administrative units. Either **directoryScopeId** or **appScopeId** is required.|
|justification|String|A message provided by users and administrators when create they create the **unifiedRoleAssignmentScheduleRequest** object.  <br/><br/>Optional for `selfDeactivate` and `adminRemove` actions; might be optional or required for other action types depending on the rules in the policy that's linked to the Microsoft Entra role. For more information, see [Rules in PIM](https://learn.microsoft.com/en-us/graph/identity-governance-pim-rules-overview).|
|scheduleInfo|[requestSchedule](../resources/requestschedule.md)|The period of the role assignment request. Recurring schedules are currently unsupported. Required.|
|ticketInfo|[ticketInfo](../resources/ticketinfo.md)|Ticket details linked to the role assignment request including details of the ticket number and ticket system. <br/><br/>Optional for `selfDeactivate` and `adminRemove` actions; might be optional or required for other action types depending on the rules in the policy that's linked to the Microsoft Entra role. For more information, see [Rules in PIM](https://learn.microsoft.com/en-us/graph/identity-governance-pim-rules-overview).|

## Response

If successful, this method returns a `201 Created` response code and an [unifiedRoleAssignmentScheduleRequest](../resources/unifiedroleassignmentschedulerequest.md) object in the response body.

## Examples

### Example 1: Admin assigning a directory role to a principal

In the following request, the admin creates a request to assign a role identified by `fdd7a751-b60b-444a-984c-02652fe8fa1c` to a principal identified by ID `071cc716-8147-4397-a5ba-b2105951cc0b`. The scope of their role is all directory objects in the tenant and the assignment is permanent.

#### Request

# [HTTP](#tab/http)

```msgraph-interactive
POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleRequests
Content-Type: application/json

{
    "action": "adminAssign",
    "justification": "Assign Groups Admin to IT Helpdesk group",
    "roleDefinitionId": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
    "directoryScopeId": "/",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "scheduleInfo": {
        "startDateTime": "2022-04-10T00:00:00Z",
        "expiration": {
            "type": "NoExpiration"
        }
    }
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	action = "adminAssign"
	justification = "Assign Groups Admin to IT Helpdesk group"
	roleDefinitionId = "fdd7a751-b60b-444a-984c-02652fe8fa1c"
	directoryScopeId = "/"
	principalId = "071cc716-8147-4397-a5ba-b2105951cc0b"
	scheduleInfo = @{
		startDateTime = [System.DateTime]::Parse("2022-04-10T00:00:00Z")
		expiration = @{
			type = "NoExpiration"
		}
	}
}

New-MgRoleManagementDirectoryRoleAssignmentScheduleRequest -BodyParameter $params

```

---

#### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignmentScheduleRequests/$entity",
    "id": "95c690fb-3eb3-4942-a03f-4524aed6f31e",
    "status": "Provisioned",
    "createdDateTime": "2022-04-11T11:50:03.9014347Z",
    "completedDateTime": "2022-04-11T11:50:05.9999343Z",
    "approvalId": null,
    "customData": null,
    "action": "adminAssign",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "roleDefinitionId": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
    "directoryScopeId": "/",
    "appScopeId": null,
    "isValidationOnly": false,
    "targetScheduleId": "95c690fb-3eb3-4942-a03f-4524aed6f31e",
    "justification": "Assign Groups Admin to IT Helpdesk group",
    "createdBy": {
        "application": null,
        "device": null,
        "user": {
            "displayName": null,
            "id": "3fbd929d-8c56-4462-851e-0eb9a7b3a2a5"
        }
    },
    "scheduleInfo": {
        "startDateTime": "2022-04-11T11:50:05.9999343Z",
        "recurrence": null,
        "expiration": {
            "type": "noExpiration",
            "endDateTime": null,
            "duration": null
        }
    },
    "ticketInfo": {
        "ticketNumber": null,
        "ticketSystem": null
    }
}
```

### Example 2: User activating their eligible role

#### Request

In the following request, a user identified by **principalId** `071cc716-8147-4397-a5ba-b2105951cc0b` activates their own *eligible role* to a Microsoft Entra role identified by ID `8424c6f0-a189-499e-bbd0-26c1753c96d4`. The scope of their role is all directory objects in the tenant and the assignment is for five hours. To run this request, the calling user must have multifactor authentication (MFA) enforced, and running the query in a session in which they were challenged for MFA.

To retrieve the details of their eligibility requests and identify the eligibility to activate, the user will call the [unifiedRoleEligibilitySchedule: filterByCurrentUser](unifiedroleeligibilityschedule-filterbycurrentuser.md) API.

# [HTTP](#tab/http)

```msgraph-interactive
POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleRequests/
Content-Type: application/json

{
    "action": "selfActivate",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "roleDefinitionId": "8424c6f0-a189-499e-bbd0-26c1753c96d4",
    "directoryScopeId": "/",
    "justification": "I need access to the Attribute Administrator role to manage attributes to be assigned to restricted AUs",
    "scheduleInfo": {
        "startDateTime": "2022-04-14T00:00:00.000Z",
        "expiration": {
            "type": "AfterDuration",
            "duration": "PT5H"
        }
    },
    "ticketInfo": {
        "ticketNumber": "CONTOSO:Normal-67890",
        "ticketSystem": "MS Project"
    }
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	action = "selfActivate"
	principalId = "071cc716-8147-4397-a5ba-b2105951cc0b"
	roleDefinitionId = "8424c6f0-a189-499e-bbd0-26c1753c96d4"
	directoryScopeId = "/"
	justification = "I need access to the Attribute Administrator role to manage attributes to be assigned to restricted AUs"
	scheduleInfo = @{
		startDateTime = [System.DateTime]::Parse("2022-04-14T00:00:00.000Z")
		expiration = @{
			type = "AfterDuration"
			duration = "PT5H"
		}
	}
	ticketInfo = @{
		ticketNumber = "CONTOSO:Normal-67890"
		ticketSystem = "MS Project"
	}
}

New-MgRoleManagementDirectoryRoleAssignmentScheduleRequest -BodyParameter $params

```

---

#### Response

The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignmentScheduleRequests/$entity",
    "id": "911bab8a-6912-4de2-9dc0-2648ede7dd6d",
    "status": "Granted",
    "createdDateTime": "2022-04-13T08:52:32.6485851Z",
    "completedDateTime": "2022-04-14T00:00:00Z",
    "approvalId": null,
    "customData": null,
    "action": "selfActivate",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "roleDefinitionId": "8424c6f0-a189-499e-bbd0-26c1753c96d4",
    "directoryScopeId": "/",
    "appScopeId": null,
    "isValidationOnly": false,
    "targetScheduleId": "911bab8a-6912-4de2-9dc0-2648ede7dd6d",
    "justification": "I need access to the Attribute Administrator role to manage attributes to be assigned to restricted AUs",
    "createdBy": {
        "application": null,
        "device": null,
        "user": {
            "displayName": null,
            "id": "071cc716-8147-4397-a5ba-b2105951cc0b"
        }
    },
    "scheduleInfo": {
        "startDateTime": "2022-04-14T00:00:00Z",
        "recurrence": null,
        "expiration": {
            "type": "afterDuration",
            "endDateTime": null,
            "duration": "PT5H"
        }
    },
    "ticketInfo": {
        "ticketNumber": "CONTOSO:Normal-67890",
        "ticketSystem": "MS Project"
    }
}
```
