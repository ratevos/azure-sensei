# Get unifiedRoleEligibilitySchedule

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroleeligibilityschedule-get?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Retrieve the schedule for a role eligibility operation.

## Permissions
Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|RoleEligibilitySchedule.Read.Directory|RoleEligibilitySchedule.ReadWrite.Directory, RoleManagement.Read.All, RoleManagement.Read.Directory, RoleManagement.ReadWrite.Directory|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|RoleEligibilitySchedule.Read.Directory|RoleEligibilitySchedule.ReadWrite.Directory, RoleManagement.Read.All, RoleManagement.Read.Directory, RoleManagement.ReadWrite.Directory|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - For read operations: *Global Reader*, *Security Operator*, *Security Reader*, *Security Administrator*, or *Privileged Role Administrator*
> - For write operations: *Privileged Role Administrator*

## HTTP request

```http
GET /roleManagement/directory/roleEligibilitySchedules/{unifiedRoleEligibilityScheduleId}
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

If successful, this method returns a `200 OK` response code and an [unifiedRoleEligibilitySchedule](../resources/unifiedroleeligibilityschedule.md) object in the response body.

## Examples

### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilitySchedules/1f06eafc-7532-429b-abf1-ab5a5f4a7052
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleEligibilitySchedule -UnifiedRoleEligibilityScheduleId $unifiedRoleEligibilityScheduleId

```

---

### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleEligibilitySchedules/$entity",
    "id": "1f06eafc-7532-429b-abf1-ab5a5f4a7052",
    "principalId": "b2af90c6-279b-41f7-8e79-2f55d07af928",
    "roleDefinitionId": "75934031-6c7e-415a-99d7-48dbd49e875e",
    "directoryScopeId": "/",
    "appScopeId": null,
    "createdUsing": "1f06eafc-7532-429b-abf1-ab5a5f4a7052",
    "createdDateTime": "2022-02-18T20:41:37.163Z",
    "modifiedDateTime": null,
    "status": "Provisioned",
    "memberType": "Direct",
    "scheduleInfo": {
        "startDateTime": "2022-02-18T20:41:37.163Z",
        "recurrence": null,
        "expiration": {
            "type": "noExpiration",
            "endDateTime": null,
            "duration": null
        }
    }
}
```
