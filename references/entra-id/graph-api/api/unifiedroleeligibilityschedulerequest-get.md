# Get unifiedRoleEligibilityScheduleRequest

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroleeligibilityschedulerequest-get?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

In PIM, read the details of a request for for a role eligibility request made through the [unifiedRoleEligibilityScheduleRequest](../resources/unifiedroleeligibilityschedulerequest.md) object.

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
GET /roleManagement/directory/roleEligibilityScheduleRequests/{unifiedRoleEligibilityScheduleRequestId}
```

## Optional query parameters
This method supports the `$select` and `$expand` OData query parameters to help customize the response. All supported relationships can be expanded. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and an [unifiedRoleEligibilityScheduleRequest](../resources/unifiedroleeligibilityschedulerequest.md) object in the response body.

## Examples

### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleRequests/f341269e-c926-41fa-a905-cef3b01b2a67
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleEligibilityScheduleRequest -UnifiedRoleEligibilityScheduleRequestId $unifiedRoleEligibilityScheduleRequestId

```

---

### Response
>**Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleEligibilityScheduleRequests/$entity",
    "id": "f341269e-c926-41fa-a905-cef3b01b2a67",
    "status": "Revoked",
    "createdDateTime": "2022-04-12T09:12:18.187Z",
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
