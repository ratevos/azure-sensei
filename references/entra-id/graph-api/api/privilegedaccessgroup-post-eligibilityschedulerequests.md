# Create eligibilityScheduleRequest

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroup-post-eligibilityschedulerequests?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Create a new [privilegedAccessGroupEligibilityScheduleRequest](../resources/privilegedaccessgroupeligibilityschedulerequest.md) object.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup|PrivilegedEligibilitySchedule.Remove.AzureADGroup|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup|PrivilegedEligibilitySchedule.Remove.AzureADGroup|

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
POST /identityGovernance/privilegedAccess/group/eligibilityScheduleRequests
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
|Content-Type|application/json. Required.|

## Request body
In the request body, supply a JSON representation of the [privilegedAccessGroupEligibilityScheduleRequest](../resources/privilegedaccessgroupeligibilityschedulerequest.md) object.

You can specify the following properties when creating a **privilegedAccessGroupEligibilityScheduleRequest**.

|Property|Type|Description|
|:---|:---|:---|
|accessId|privilegedAccessGroupRelationships|The identifier of the membership or ownership eligibility relationship to the group. The possible values are: `owner`, `member`. Required.|
|action|String|Represents the type of operation on the group membership or ownership eligibility assignment request. The possible values are: `adminAssign`, `adminUpdate`, `adminRemove`, `selfActivate`, `selfDeactivate`, `adminExtend`, `adminRenew`. <br/><ul><li>`adminAssign`: For administrators to assign group membership or ownership eligibility to principals.</li><li>`adminRemove`: For administrators to remove principals from group membership or ownership eligibilities.</li><li> `adminUpdate`: For administrators to change existing eligible assignments.</li><li>`adminExtend`: For administrators to extend expiring eligible assignments.</li><li>`adminRenew`: For administrators to renew expired eligible assignments.</li><li>`selfActivate`: For principals to activate their eligible assignments.</li><li>`selfDeactivate`: For principals to deactivate their eligible assignments.</li></ul>|
|groupId|String|The identifier of the group representing the scope of the membership or ownership eligibility through PIM for Groups. Required.|
|justification|String|A message provided by users and administrators when they create the **privilegedAccessGroupAssignmentScheduleRequest** object.|
|principalId|String|The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for Groups. Required.|
|scheduleInfo|[requestSchedule](../resources/requestschedule.md)|The period of the group membership or ownership assignment for PIM for Groups. Recurring schedules are currently unsupported. Required.|
|ticketInfo|[ticketInfo](../resources/ticketinfo.md)|Ticket details linked to the group membership or ownership assignment request including details of the ticket number and ticket system. Optional.|

## Response

If successful, this method returns a `201 Created` response code and a [privilegedAccessGroupEligibilityScheduleRequest](../resources/privilegedaccessgroupeligibilityschedulerequest.md) object in the response body.

## Examples

### Example 1: An admin creates an eligible group ownership request for a principal

The following request creates an eligibility schedule request to make a principal eligible to be a group owner. The eligible ownership expires after two hours.

#### Request
# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilityScheduleRequests
Content-Type: application/json

{
    "accessId": "member",
    "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
    "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
    "action": "AdminAssign",
    "scheduleInfo": {
        "startDateTime": "2023-02-06T19:25:00.000Z",
        "expiration": {
            "type": "AfterDateTime",
            "endDateTime": "2023-02-07T19:56:00.000Z"
        }
    },
    "justification": "Assign eligible request."
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	accessId = "member"
	principalId = "3cce9d87-3986-4f19-8335-7ed075408ca2"
	groupId = "2b5ed229-4072-478d-9504-a047ebd4b07d"
	action = "AdminAssign"
	scheduleInfo = @{
		startDateTime = [System.DateTime]::Parse("2023-02-06T19:25:00.000Z")
		expiration = @{
			type = "AfterDateTime"
			endDateTime = [System.DateTime]::Parse("2023-02-07T19:56:00.000Z")
		}
	}
	justification = "Assign eligible request."
}

New-MgIdentityGovernancePrivilegedAccessGroupEligibilityScheduleRequest -BodyParameter $params

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/$entity",
    "id": "f8bd9e2d-bc15-49b1-8a9b-c571b3cf9555",
    "status": "Provisioned",
    "createdDateTime": "2023-02-07T06:57:54.1633903Z",
    "completedDateTime": "2023-02-07T06:57:55.6183972Z",
    "action": "adminAssign",
    "isValidationOnly": false,
    "justification": "Assign eligible request.",
    "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
    "accessId": "member",
    "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
    "targetScheduleId": "2b5ed229-4072-478d-9504-a047ebd4b07d_member_f8bd9e2d-bc15-49b1-8a9b-c571b3cf9555",
    "createdBy": {
        "user": {
            "id": "3cce9d87-3986-4f19-8335-7ed075408ca2"
        }
    },
    "scheduleInfo": {
        "startDateTime": "2023-02-07T06:57:55.6183972Z",
        "recurrence": null,
        "expiration": {
            "type": "afterDateTime",
            "endDateTime": "2023-02-07T19:56:00Z",
            "duration": null
        }
    }
}
```

### Example 2: An admin extends an eligible group membership for a principal

The following request extends an existing eligibility schedule request before it expires.

#### Request
# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/eligibilityScheduleRequests
Content-Type: application/json

{
    "accessId": "member",
    "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
    "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
    "action": "AdminExtend",
    "scheduleInfo": {
        "startDateTime": "2023-02-06T19:25:00.000Z",
        "expiration": {
            "type": "AfterDateTime",
            "endDateTime": "2023-02-07T20:56:00.000Z"
        }
    },
    "justification": "Extend eligible request."
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	accessId = "member"
	principalId = "3cce9d87-3986-4f19-8335-7ed075408ca2"
	groupId = "2b5ed229-4072-478d-9504-a047ebd4b07d"
	action = "AdminExtend"
	scheduleInfo = @{
		startDateTime = [System.DateTime]::Parse("2023-02-06T19:25:00.000Z")
		expiration = @{
			type = "AfterDateTime"
			endDateTime = [System.DateTime]::Parse("2023-02-07T20:56:00.000Z")
		}
	}
	justification = "Extend eligible request."
}

New-MgIdentityGovernancePrivilegedAccessGroupEligibilityScheduleRequest -BodyParameter $params

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/$entity",
    "id": "e3405b79-c0d8-4597-87b5-a84451e29224",
    "status": "Provisioned",
    "createdDateTime": "2023-02-07T07:01:25.9239454Z",
    "completedDateTime": "2023-02-07T07:01:27.3379548Z",
    "action": "adminExtend",
    "isValidationOnly": false,
    "justification": "Extend eligible request.",
    "principalId": "3cce9d87-3986-4f19-8335-7ed075408ca2",
    "accessId": "member",
    "groupId": "2b5ed229-4072-478d-9504-a047ebd4b07d",
    "targetScheduleId": "2b5ed229-4072-478d-9504-a047ebd4b07d_member_e3405b79-c0d8-4597-87b5-a84451e29224",
    "createdBy": {
        "user": {
            "id": "3cce9d87-3986-4f19-8335-7ed075408ca2"
        }
    },
    "scheduleInfo": {
        "startDateTime": "2023-02-07T07:01:27.3379548Z",
        "expiration": {
            "type": "afterDateTime",
            "endDateTime": "2023-02-07T20:56:00Z",
            "duration": null
        }
    }
}
```
