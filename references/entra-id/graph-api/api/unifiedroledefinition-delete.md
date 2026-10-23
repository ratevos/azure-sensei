# Delete unifiedRoleDefinition

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroledefinition-delete?view=graph-rest-1.0  
> Microsoft doc last updated: 10/07/2026


Namespace: microsoft.graph

Delete a [unifiedRoleDefinition](../resources/unifiedRoleDefinition.md) object. You can't delete built-in roles. Deleting an active custom role definition soft-deletes it. You can then restore the role or permanently delete it from the deleted-items collection. This feature requires a Microsoft Entra ID P1 or P2 license.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|RoleManagement.ReadWrite.Directory|Directory.ReadWrite.All|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|RoleManagement.ReadWrite.Directory|Directory.ReadWrite.All|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. *Privileged Role Administrator* is the least privileged role supported for this operation.

## HTTP request

```http
DELETE /roleManagement/directory/roleDefinitions/{id}

```

To permanently delete a soft-deleted custom role definition:

```http
DELETE /roleManagement/directory/deletedItems/roleDefinitions/{id}
```

## Request headers

| Name          | Description   |
|:--------------|:--------------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns `204 No Content` response code. It doesn't return anything in the response body.

## Examples

### Example 1: Soft-delete a custom role definition

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
DELETE https://graph.microsoft.com/v1.0/roleManagement/directory/roleDefinitions/f189965f-f560-4c59-9101-933d4c87a91a
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Remove-MgRoleManagementDirectoryRoleDefinition -UnifiedRoleDefinitionId $unifiedRoleDefinitionId

```

---

#### Response

The following example shows the response.

```http
HTTP/1.1 204 No Content
```

### Example 2: Permanently delete a soft-deleted custom role definition

#### Request

The following example shows a request.

```http
DELETE https://graph.microsoft.com/v1.0/roleManagement/directory/deletedItems/roleDefinitions/a1b2c3d4-5678-90ab-cdef-1234567890ab
```

#### Response

The following example shows the response.

```http
HTTP/1.1 204 No Content
```
