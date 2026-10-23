# Get privilegedAccessGroupAssignmentScheduleRequest

> Source: https://learn.microsoft.com/en-us/graph/api/privilegedaccessgroupassignmentschedulerequest-get?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Read the properties and relationships of a [privilegedAccessGroupAssignmentScheduleRequest](../resources/privilegedaccessgroupassignmentschedulerequest.md) object.

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
GET /identityGovernance/privilegedAccess/group/assignmentScheduleRequests/{privilegedAccessGroupAssignmentScheduleRequestId}
```

## Optional query parameters
This method supports the `$select` and `$expand` OData query parameters to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a [privilegedAccessGroupAssignmentScheduleRequest](../resources/privilegedaccessgroupassignmentschedulerequest.md) object in the response body.

## Examples

### Request
The following example shows a request.
# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/identityGovernance/privilegedAccess/group/assignmentScheduleRequests/34e963f6-150f-cf79-678c-6fcaf978bb49
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgIdentityGovernancePrivilegedAccessGroupAssignmentScheduleRequest -PrivilegedAccessGroupAssignmentScheduleRequestId $privilegedAccessGroupAssignmentScheduleRequestId

```

---

### Response
The following example shows the response.
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#identityGovernance/privilegedAccess/group/assignmentScheduleRequests/$entity",
    "id": "34e963f6-150f-cf79-678c-6fcaf978bb49",
    "status": "Provisioned",
    "completedDateTime": "2023-01-11T11:50:06Z",
    "createdDateTime": "2023-01-11T11:50:05.95Z",
    "approvalId": null,
    "customData": null,
    "createdBy": {
      "user": {
            "displayName": null,
            "id": "3fbd929d-8c56-4462-851e-0eb9a7b3a2a5"
      }
    },
    "action": "adminAssign",
    "isValidationOnly": false,
    "justification": "Assign active member access.",
    "scheduleInfo": {
        "startDateTime": "2023-01-11T11:50:05.9999343Z",
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
    },
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "accessId": "member",
    "groupId": "68e55cce-cf7e-4a2d-9046-3e4e75c4bfa7",
    "targetScheduleId": "34e963f6-150f-cf79-678c-6fcaf978bb49"
}
```
