# privilegedAccessGroupAssignmentScheduleRequest: filterByCurrentUser

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroupassignmentschedulerequest-filterbycurrentuser?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

In PIM for Groups, retrieve the requests for membership or ownership assignments for the calling principal to groups that are governed by PIM.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup|Not available.|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup|Not available.|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be an owner or member of the group or be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
>
> - For role-assignable groups: *Global Reader* or *Privileged Role Administrator*
> - For non-role-assignable groups: *Global Reader*, *Directory Writer*, *Groups Administrator*, *Identity Governance Administrator*, or *User Administrator*
>
> The role assignments for the calling user should be scoped at the directory level.
>
> Other roles with permissions to manage groups (such as Exchange Administrators for non-role-assignable Microsoft 365 groups) and administrators with assignments scoped at administrative unit level can manage groups through groups API and override changes made in Microsoft Entra PIM through PIM for Groups APIs.

## HTTP request

```http
GET /identityGovernance/privilegedAccess/group/assignmentScheduleRequests/filterByCurrentUser(on='parameterValue')
```

## Function parameters
In the request URL, provide the following query parameters with values.
The following table shows the parameters that can be used with this function.

|Parameter|Type|Description|
|:---|:---|:---|
|on|assignmentScheduleRequestFilterByCurrentUserOptions|Filter used to query assignmentScheduleRequests. The possible values are `principal`, `createdBy`, `approver`, `unknownFutureValue`. Required.|

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this function returns a `200 OK` response code and a [privilegedAccessGroupAssignmentScheduleRequest](../resources/privilegedaccessgroupassignmentschedulerequest.md) collection in the response body.

## Examples

### Example 1: Retrieve a principal's requests scoped to a specific group and that are pending approval

#### Request
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/assignmentScheduleRequests/filterByCurrentUser(on='principal')?$filter=status eq 'PendingApproval' and groupId eq 'd5f0ad2e-6b34-401b-b6da-0c8fc2c5a3fc'
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Invoke-MgFilterIdentityGovernancePrivilegedAccessGroupAssignmentScheduleRequestByCurrentUser -Filter "status eq 'PendingApproval' and groupId eq 'd5f0ad2e-6b34-401b-b6da-0c8fc2c5a3fc'"  -On $onId 

```

---

#### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "value": [
    {
      "@odata.type": "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest",
      "id": "12345",
      "accessId": "member",
      "principalId": "c277c8cb-6bb7-42e5-a17f-0add9a718151",
      "groupId": "d5f0ad2e-6b34-401b-b6da-0c8fc2c5a3fc",
      "status": "PendingApproval",
      "createdDateTIme": "2022-02-26T08:00:00.000Z",
      "completedDateTIme": null,
      "isValidationOnly": false,
      "action": "SelfActivate",
      "scheduleInfo":
        {
          "startDateTime": "2022-04-01T08:00:00.000Z",
          "expiration":
            {
              "type": "AfterDuration",
              "duration" : "PT8H",
            }
        },
      "justification":"Activate access",
      "ticketInfo":
        {
          "ticketNumber": "09876"
        }
    }
  ]
}
```
