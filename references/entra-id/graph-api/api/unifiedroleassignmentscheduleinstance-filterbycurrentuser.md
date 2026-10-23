# unifiedRoleAssignmentScheduleInstance: filterByCurrentUser

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroleassignmentscheduleinstance-filterbycurrentuser?view=graph-rest-1.0  
> Microsoft doc last updated: 06/26/2024

Namespace: microsoft.graph

Get the instances of active role assignments for the calling principal.

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
GET /roleManagement/directory/roleAssignmentScheduleInstances/filterByCurrentUser(on=parameterValue)
```

## Function parameters
In the request URL, provide the following query parameters with values.

|Parameter|Type|Description|
|:---|:---|:---|
|on|roleAssignmentScheduleInstanceFilterByCurrentUserOptions|The possible values are `principal`, `unknownFutureValue`.|

## Optional query parameters

This method supports the `$select`, `$filter`, and `$expand` OData query parameters to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this function returns a `200 OK` response code and a [unifiedRoleAssignmentScheduleInstance](../resources/unifiedroleassignmentscheduleinstance.md) collection in the response body.

## Examples

### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleInstances/filterByCurrentUser(on='principal')
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Invoke-MgFilterRoleManagementDirectoryRoleAssignmentScheduleInstanceByCurrentUser -On $onId 

```

---

### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(unifiedRoleAssignmentScheduleInstance)",
    "value": [
        {
            "@odata.type": "#microsoft.graph.unifiedRoleAssignmentScheduleInstance",
            "id": "lAPpYvVpN0KRkAEhdxReEJ2SvT9WjGJEhR4OuaezoqU-1",
            "principalId": "3fbd929d-8c56-4462-851e-0eb9a7b3a2a5",
            "roleDefinitionId": "62e90394-69f5-4237-9190-012177145e10",
            "directoryScopeId": "/",
            "appScopeId": null,
            "startDateTime": null,
            "endDateTime": null,
            "assignmentType": "Assigned",
            "memberType": "Direct",
            "roleAssignmentOriginId": "lAPpYvVpN0KRkAEhdxReEJ2SvT9WjGJEhR4OuaezoqU-1",
            "roleAssignmentScheduleId": "lAPpYvVpN0KRkAEhdxReEJ2SvT9WjGJEhR4OuaezoqU-1"
        }
    ]
}
```
