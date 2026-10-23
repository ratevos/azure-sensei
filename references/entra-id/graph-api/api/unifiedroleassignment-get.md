# Get unifiedRoleAssignment

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroleassignment-get?view=graph-rest-1.0  
> Microsoft doc last updated: 07/26/2024


Namespace: microsoft.graph

Retrieve the properties and relationships of a [unifiedRoleAssignment](../resources/unifiedroleassignment.md) object.

## Permissions

One of the following permissions is required to call this API. To learn more, including how to choose permissions, see [Permissions](https://learn.microsoft.com/en-us/graph/permissions-reference).

<a name='for-the-directory-azure-ad-provider'></a>

### For the directory (Microsoft Entra ID) provider

|Permission type      | Permissions (from least to most privileged)              |
|:--------------------|:---------------------------------------------------------|
|Delegated (work or school account) | RoleManagement.Read.Directory, RoleManagement.Read.All, Directory.Read.All, RoleManagement.ReadWrite.Directory, Directory.ReadWrite.All    |
|Delegated (personal Microsoft account) | Not supported.    |
|Application | RoleManagement.Read.Directory, RoleManagement.Read.All, Directory.Read.All, RoleManagement.ReadWrite.Directory, Directory.ReadWrite.All |

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Directory Readers
> - Global Reader
> - Privileged Role Administrator

### For the entitlement management provider

|Permission type      | Permissions (from least to most privileged)              |
|:--------------------|:---------------------------------------------------------|
|Delegated (work or school account) |  EntitlementManagement.Read.All, EntitlementManagement.ReadWrite.All  |
|Delegated (personal Microsoft account) | Not supported.    |
|Application | EntitlementManagement.Read.All, EntitlementManagement.ReadWrite.All |

## HTTP request

Get a role assignment for the directory provider:

```http
GET /roleManagement/directory/roleAssignments/{id}
```

Get a role assignment for the entitlement management provider:

```http
GET /roleManagement/entitlementManagement/roleAssignments/{id}
```

## Optional query parameters

This method supports th `$select` and `$expand` OData query parameters to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers

| Name      |Description|
|:----------|:----------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and the requested [unifiedRoleAssignment](../resources/unifiedroleassignment.md) object in the response body.

## Examples

### Example 1: Get the details of a role assignment

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments/lAPpYvVpN0KRkAEhdxReELhrmgjL6CxJqkHAeKoLUSA-11
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleAssignment -UnifiedRoleAssignmentId $unifiedRoleAssignmentId

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignments/$entity",
    "id": "lAPpYvVpN0KRkAEhdxReELhrmgjL6CxJqkHAeKoLUSA-1",
    "principalId": "089a6bb8-e8cb-492c-aa41-c078aa0b5120",
    "directoryScopeId": "/",
    "roleDefinitionId": "62e90394-69f5-4237-9190-012177145e10"
}
```

### Example 2: Get the details of a role assignment and expand the relationships

#### Request

The following example shows a request with the `$expand` query parameter.

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments/lAPpYvVpN0KRkAEhdxReEJC2sEqbR_9Hr48lds9SGHI-1?$expand=roleDefinition
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleAssignment -UnifiedRoleAssignmentId $unifiedRoleAssignmentId -ExpandProperty "roleDefinition" 

```

---

#### Response

The following example shows the response.
> **Note:** The response object shown here might be shortened for readability. All the properties will be returned from an actual call.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignments/$entity",
    "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
    "id": "lAPpYvVpN0KRkAEhdxReEJC2sEqbR_9Hr48lds9SGHI-1",
    "roleDefinitionId": "c2cf284d-6c41-4e6b-afac-4b80928c9034",
    "roleDefinition": {
      "id": "c2cf284d-6c41-4e6b-afac-4b80928c9034",
      "displayName": "Billing Administrator",
      "description": "Can perform common billing related tasks like updating payment information.",
      "rolePermissions": [
        {
          "allowedResourceActions": [
            "microsoft.commerce.billing/allEntities/allTasks",
            "microsoft.directory/organization/basic/update",
          ],
          "excludedResourceActions": []
        }],
      "isEnabled": true,
      },
    "principalId": "f8ca5a85-489a-49a0-b555-0a6d81e56f0d",
    "directoryScopeId": "28ca5a85-489a-49a0-b555-0a6d81e56f0d"
}
```
