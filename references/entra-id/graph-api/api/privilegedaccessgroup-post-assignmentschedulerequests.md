# Create assignmentScheduleRequest

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroup-post-assignmentschedulerequests?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Create a new [privilegedAccessGroupAssignmentScheduleRequest](../resources/privilegedaccessgroupassignmentschedulerequest.md) object.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup|PrivilegedAssignmentSchedule.Remove.AzureADGroup|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup|PrivilegedAssignmentSchedule.Remove.AzureADGroup|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be an owner or member of the group or be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
>
> - For role-assignable groups: *Privileged Role Administrator*
> - For non-role-assignable groups: *Directory Writer*, *Groups Administrator*, *Identity Governance Administrator*, or *User Administrator*
>
> The role assignments for the calling user should be scoped at the directory level.
>
> Other roles with permissions to manage groups (such as Exchange Administrators for non-role-assignable Microsoft 365 groups) and administrators with assignments scoped at administrative unit level can manage groups through groups API and override changes made in Microsoft Entra PIM through PIM for Groups APIs.

## HTTP request

```http
POST /identityGovernance/privilegedAccess/group/assignmentScheduleRequests
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body
In the request body, supply a JSON representation of the [privilegedAccessGroupAssignmentScheduleRequest](../resources/privilegedaccessgroupassignmentschedulerequest.md) object.

You can specify the following properties when creating a **privilegedAccessGroupAssignmentScheduleRequest**.

|Property|Type|Description|
|:---|:---|:---|
|accessId|privilegedAccessGroupRelationships|The identifier of the membership or ownership assignment relationship to the group. The possible values are: `owner`, `member`. Required.|
|action|String|Represents the type of the operation on the group membership or ownership assignment request. The possible values are: `adminAssign`, `adminUpdate`, `adminRemove`, `selfActivate`, `selfDeactivate`, `adminExtend`, `adminRenew`. <br/><ul><li>`adminAssign`: For administrators to assign group membership or ownership to principals.</li><li>`adminRemove`: For administrators to remove principals from group membership or ownership.</li><li> `adminUpdate`: For administrators to change existing group membership or ownership assignments.</li><li>`adminExtend`: For administrators to extend expiring assignments.</li><li>`adminRenew`: For administrators to renew expired assignments.</li><li>`selfActivate`: For principals to activate their assignments.</li><li>`selfDeactivate`: For principals to deactivate their active assignments.</li></ul> Required.|
|customData|String|Free text field to define any custom data for the request. Optional.|
|groupId|String|The identifier of the group representing the scope of the membership or ownership assignment through PIM for Groups. Required.|
|justification|String|A message provided by users and administrators when they create the **privilegedAccessGroupAssignmentScheduleRequest** object. Optional.|
|principalId|String|The identifier of the principal whose membership or ownership assignment is granted through PIM for Groups. Required.|
|scheduleInfo|[requestSchedule](../resources/requestschedule.md)|The period of the group membership or ownership assignment for PIM for Groups. Recurring schedules are currently unsupported. Required.|
|ticketInfo|[ticketInfo](../resources/ticketinfo.md)|Ticket details linked to the group membership or ownership assignment request including details of the ticket number and ticket system. Optional.|

## Response

If successful, this method returns a `201 Created` response code and a [privilegedAccessGroupAssignmentScheduleRequest](../resources/privilegedaccessgroupassignmentschedulerequest.md) object in the response body.

## Examples

### Example 1: Create an assignment schedule request

The following request creates an assignment schedule request to assign a principal active membership to the specified group. The active membership expires after two hours.

#### Request
# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/assignmentScheduleRequests
Content-Type: application/json

{
  "accessId": "member", 
  "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2", 
  "groupId": "68e55cce-cf7e-4a2d-9046-3e4e75c4bfa7", 
  "action": "adminAssign", 
  "scheduleInfo": { 
    "startDateTime": "2022-12-08T07:43:00.000Z", 
    "expiration": { 
      "type": "afterDuration", 
      "duration": "PT2H" 
    } 
  }, 
  "justification": "Assign active member access."
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	accessId = "member"
	principalId = "3cce9d87-3986-4f19-8335-7ed075408ca2"
	groupId = "68e55cce-cf7e-4a2d-9046-3e4e75c4bfa7"
	action = "adminAssign"
	scheduleInfo = @{
		startDateTime = [System.DateTime]::Parse("2022-12-08T07:43:00.000Z")
		expiration = @{
			type = "afterDuration"
			duration = "PT2H"
		}
	}
	justification = "Assign active member access."
}

New-MgIdentityGovernancePrivilegedAccessGroupAssignmentScheduleRequest -BodyParameter $params

```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "@odata.type": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/assignmentScheduleRequests/$entity",
  "id": "34e963f6-150f-cf79-678c-6fcaf978bb49",
  "status": "Provisioned",
  "completedDateTime": "2023-02-07T07:05:55.3404527Z",
  "createdDateTime": "2023-02-07T07:05:53.7895614Z",
  "approvalId": null,
  "customData": null,
  "createdBy": {
      "user": {
          "id": "3cce9d87-3986-4f19-8335-7ed075408ca2"
      }
  },
  "action": "adminAssign",
  "isValidationOnly": false,
  "justification": "Assign active member access.",
  "scheduleInfo": {
      "startDateTime": "2023-02-07T07:05:55.3404527Z",
      "expiration": {
        "type": "afterDuration",
         "duration": "PT2H"
      }
  },
  "ticketInfo": {
      "ticketNumber": null,
      "ticketSystem": null
  },
  "accessId": "member", 
  "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2", 
  "groupId": "68e55cce-cf7e-4a2d-9046-3e4e75c4bfa7",
  "targetScheduleId": "2b5ed229-4072-478d-9504-a047ebd4b07d_member_6aacaee8-4089-4048-9510-3119367fc943"
}
```

### Example 2: User activates their eligible assignment for PIM for Groups

In the following request, a user identified by **principalId** `3cce9d87-3986-4f19-8335-7ed075408ca2` activates their *eligible membership* to a group managed by PIM identified by **groupId** `2b5ed229-4072-478d-9504-a047ebd4b07d`.

#### Request
# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/assignmentScheduleRequests
Content-Type: application/json

{
  "accessId": "member", 
  "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2", 
  "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d", 
  "action": "selfActivate", 
  "scheduleInfo": { 
    "startDateTime": "2023-02-08T07:43:00.000Z", 
    "expiration": { 
      "type": "afterDuration", 
      "duration": "PT2H" 
    } 
  }, 
  "justification": "Activate assignment."
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	accessId = "member"
	principalId = "3cce9d87-3986-4f19-8335-7ed075408ca2"
	groupId = "2b5ed229-4072-478d-9504-a047ebd4b07d"
	action = "selfActivate"
	scheduleInfo = @{
		startDateTime = [System.DateTime]::Parse("2023-02-08T07:43:00.000Z")
		expiration = @{
			type = "afterDuration"
			duration = "PT2H"
		}
	}
	justification = "Activate assignment."
}

New-MgIdentityGovernancePrivilegedAccessGroupAssignmentScheduleRequest -BodyParameter $params

```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "@odata.type": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/assignmentScheduleRequests/$entity",
  "id": "6aacaee8-4089-4048-9510-3119367fc943",
  "status": "Provisioned",
  "completedDateTime": "2023-02-07T07:05:55.3404527Z",
  "createdDateTime": "2023-02-07T07:05:53.7895614Z",
  "approvalId": null,
  "customData": null,
  "createdBy": {
      "user": {
          "id": "3cce9d87-3986-4f19-8335-7ed075408ca2"
      }
  },
  "action": "selfActivate",
  "isValidationOnly": false,
  "justification": "Activate assignment.",
  "scheduleInfo": {
      "startDateTime": "2023-02-07T07:05:55.3404527Z",
      "expiration": {
        "type": "afterDuration",
         "duration": "PT2H"
      }
  },
  "ticketInfo": {
      "ticketNumber": null,
      "ticketSystem": null
  },
  "accessId": "member", 
  "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2", 
  "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
  "targetScheduleId": "2b5ed229-4072-478d-9504-a047ebd4b07d_member_6aacaee8-4089-4048-9510-3119367fc943"
}
```
