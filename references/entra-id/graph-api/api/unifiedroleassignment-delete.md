# Delete unifiedRoleAssignment

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroleassignment-delete?view=graph-rest-1.0  
> Microsoft doc last updated: 07/26/2024


Namespace: microsoft.graph

Delete a [unifiedRoleAssignment](../resources/unifiedRoleAssignment.md) object.

## Permissions

One of the following permissions is required to call this API. To learn more, including how to choose permissions, see [Permissions](https://learn.microsoft.com/en-us/graph/permissions-reference).

<a name='for-the-directory-azure-ad-provider'></a>

### For the directory (Microsoft Entra ID) provider

| Permission type                        | Permissions (from least to most privileged) |
|:---------------------------------------|:--------------------------------------------|
| Delegated (work or school account)     | RoleManagement.ReadWrite.Directory |
| Delegated (personal Microsoft account) | Not supported. |
| Application                            | RoleManagement.ReadWrite.Directory |

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. *Privileged Role Administrator* is the least privileged role supported for this operation.

### For the Entitlement management provider

|Permission type      | Permissions (from least to most privileged)              |
|:--------------------|:---------------------------------------------------------|
|Delegated (work or school account) |  EntitlementManagement.ReadWrite.All  |
|Delegated (personal Microsoft account) | Not supported.    |
|Application | EntitlementManagement.ReadWrite.All |

## HTTP request

Remove a role assignment from the directory provider:

```http
DELETE /roleManagement/directory/roleAssignments/{id}
```

Remove a role assignment from the entitlement management provider:

```http
DELETE /roleManagement/entitlementManagement/roleAssignments/{id}
```

## Request headers

| Name          | Description   |
|:--------------|:--------------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns `204 No Content` response code. It doesn't return anything in the response body.

## Example

### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
DELETE https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments/lAPpYvVpN0KRkAEhdxReEJC2sEqbR_9Hr48lds9SGHI-1
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Remove-MgRoleManagementDirectoryRoleAssignment -UnifiedRoleAssignmentId $unifiedRoleAssignmentId

```

---

### Response

The following example shows the response.

```http
HTTP/1.1 204 No Content
```
