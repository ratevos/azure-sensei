# unifiedRoleDefinition: restore

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroledefinition-restore?view=graph-rest-1.0  
> Microsoft doc last updated: 10/07/2026


Namespace: microsoft.graph

Restore a soft-deleted custom [unifiedRoleDefinition](../resources/unifiedroledefinition.md) object to the active role definitions collection for Microsoft Entra directory role management.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](https://learn.microsoft.com/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](https://learn.microsoft.com/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

|Permission type|Least privileged permissions|Higher privileged permissions|
|:---|:---|:---|
|Delegated (work or school account)|RoleManagement.ReadWrite.Directory|Not available.|
|Delegated (personal Microsoft account)|Not supported.|Not supported.|
|Application|RoleManagement.ReadWrite.Directory|Not available.|

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. *Privileged Role Administrator* is the least privileged role supported for this operation.

## HTTP request

```http
POST /roleManagement/directory/deletedItems/roleDefinitions/{id}/restore
```

## Request headers

| Name | Description |
|:---|:---|
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts). |

## Request body

Don't supply a request body for this action.

## Response

If successful, this action returns a `200 OK` response code and a [unifiedRoleDefinition](../resources/unifiedroledefinition.md) object in the response body.

## Examples

### Example 1: Restore a soft-deleted custom role definition

#### Request

The following example shows a request.

```http
POST https://graph.microsoft.com/v1.0/roleManagement/directory/deletedItems/roleDefinitions/a1b2c3d4-5678-90ab-cdef-1234567890ab/restore
```

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleDefinitions/$entity",
  "id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "description": "Can manage basic aspects of application registrations.",
  "displayName": "Application Support Administrator",
  "isBuiltIn": false,
  "isEnabled": true,
  "rolePermissions": [
    {
      "allowedResourceActions": [
        "microsoft.directory/applications/basic/update"
      ]
    }
  ]
}
```
