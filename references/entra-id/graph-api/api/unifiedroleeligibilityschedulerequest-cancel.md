# unifiedRoleEligibilityScheduleRequest: cancel

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroleeligibilityschedulerequest-cancel?view=graph-rest-1.0  
> Microsoft doc last updated: 04/04/2024

Namespace: microsoft.graph

Immediately cancel a unifiedRoleEligibilityScheduleRequest object whose status is `Granted` and have the system automatically delete the cancelled request after 30 days. After calling this action, the **status** of the cancelled **unifiedRoleEligibilityScheduleRequest** changes to `Revoked`.

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
POST /roleManagement/directory/roleEligibilityScheduleRequests/{unifiedRoleEligibilityScheduleRequestId}/cancel
```

## Request headers
|Name|Description|
|:---|:---|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body
Don't supply a request body for this method.

## Response

If successful, this action returns a `204 No Content` response code. Attempting to cancel a request that is not in a cancelable state, for example, a unifiedRoleEligibilityScheduleRequest object whose **status** is `Provisioned` or `Failed`, returns a `400 Bad Request` error code.

## Examples

### Request

# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleRequests/532bef1f-c677-4564-aa6f-811444a4f018/cancel
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Stop-MgRoleManagementDirectoryRoleEligibilityScheduleRequest -UnifiedRoleEligibilityScheduleRequestId $unifiedRoleEligibilityScheduleRequestId

```

---

### Response

```http
HTTP/1.1 204 No Content
```
