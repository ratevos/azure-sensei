# Get unifiedRoleAssignmentSchedule

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroleassignmentschedule-get?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Retrieve the schedule for an active role assignment operation.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|RoleAssignmentSchedule.Read.Directory|RoleAssignmentSchedule.ReadWrite.Directory, RoleManagement.Read.All, RoleManagement.Read.Directory, RoleManagement.ReadWrite.Directory|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|RoleAssignmentSchedule.Read.Directory|RoleAssignmentSchedule.ReadWrite.Directory, RoleManagement.Read.All, RoleManagement.Read.Directory, RoleManagement.ReadWrite.Directory|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - For read operations: *Global Reader*, *Security Operator*, *Security Reader*, *Security Administrator*, or *Privileged Role Administrator*
> - For write operations: *Privileged Role Administrator*

## HTTP request

```http
GET /roleManagement/directory/roleAssignmentSchedules/{unifiedRoleAssignmentScheduleId}
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

If successful, this method returns a `200 OK` response code and an [unifiedRoleAssignmentSchedule](../resources/unifiedroleassignmentschedule.md) object in the response body.

## Examples

### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentSchedules/95c690fb-3eb3-4942-a03f-4524aed6f31e
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleAssignmentSchedule -UnifiedRoleAssignmentScheduleId $unifiedRoleAssignmentScheduleId

```

---

### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignmentSchedules/$entity",
    "id": "95c690fb-3eb3-4942-a03f-4524aed6f31e",
    "principalId": "071cc716-8147-4397-a5ba-b2105951cc0b",
    "roleDefinitionId": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
    "directoryScopeId": "/",
    "appScopeId": null,
    "createdUsing": "95c690fb-3eb3-4942-a03f-4524aed6f31e",
    "createdDateTime": "2022-04-11T11:50:06.343Z",
    "modifiedDateTime": null,
    "status": "Provisioned",
    "assignmentType": "Assigned",
    "memberType": "Direct",
    "scheduleInfo": {
        "startDateTime": "2022-04-11T11:50:06.343Z",
        "recurrence": null,
        "expiration": {
            "type": "noExpiration",
            "endDateTime": null,
            "duration": null
        }
    }
}
```
