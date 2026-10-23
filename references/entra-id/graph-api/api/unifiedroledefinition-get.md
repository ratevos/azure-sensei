# Get unifiedRoleDefinition

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroledefinition-get?view=graph-rest-1.0  
> Microsoft doc last updated: 10/07/2026


Namespace: microsoft.graph

Read the properties and relationships of a [unifiedRoleDefinition](../resources/unifiedRoleDefinition.md) object.

The following role-based access control (RBAC) providers are currently supported:

- directory (Microsoft Entra directory roles)
- entitlement management (Microsoft Entra entitlement management)

## Permissions

One of the following permissions is required to call this API. To learn more, including how to choose permissions, see [Permissions](https://learn.microsoft.com/en-us/graph/permissions-reference).

<a name='for-the-directory-azure-ad-provider'></a>

### For the directory (Microsoft Entra ID) provider

|Permission type      | Permissions (from least to most privileged)              |
|:--------------------|:---------------------------------------------------------|
|Delegated (work or school account) | RoleManagement.Read.Directory, Directory.Read.All, RoleManagement.ReadWrite.Directory, Directory.ReadWrite.All    |
|Delegated (personal Microsoft account) | Not supported.    |
|Application | RoleManagement.Read.Directory, Directory.Read.All, RoleManagement.ReadWrite.Directory, Directory.ReadWrite.All |

> [!IMPORTANT]
> For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:
> - Directory Readers
> - Global Reader
> - Privileged Role Administrator

### For the entitlement management provider

|Permission type      | Permissions (from least to most privileged)              |
|:--------------------|:---------------------------------------------------------|
|Delegated (work or school account) |  EntitlementManagement.Read.All, EntitlementManagement.ReadWrite.All   |
|Delegated (personal Microsoft account) | Not supported.    |
|Application | EntitlementManagement.Read.All, EntitlementManagement.ReadWrite.All  |

## HTTP request

Get a role definition for the directory provider:

```http
GET /roleManagement/directory/roleDefinitions/{id}
```

Get a soft-deleted custom role definition for the directory provider:

```http
GET /roleManagement/directory/deletedItems/roleDefinitions/{id}
```

Get a role definition for the entitlement management provider:

```http
GET /roleManagement/entitlementManagement/roleDefinitions/{id}
```

## Optional query parameters

This method supports the `$select` OData query parameter to help customize the response. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers

| Name      |Description|
|:----------|:----------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and the requested [unifiedRoleDefinition](../resources/unifiedroledefinition.md) object in the response body.

## Examples

### Example 1: Get the definition of a custom role

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleDefinitions/f189965f-f560-4c59-9101-933d4c87a91a
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleDefinition -UnifiedRoleDefinitionId $unifiedRoleDefinitionId

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleDefinitions/$entity",
    "id": "f189965f-f560-4c59-9101-933d4c87a91a",
    "description": "Allows reading Application Registrations",
    "displayName": "Application Registration Reader",
    "isBuiltIn": false,
    "isEnabled": true,
    "templateId": "f189965f-f560-4c59-9101-933d4c87a91a",
    "version": null,
    "rolePermissions": [
        {
            "allowedResourceActions": [
                "microsoft.directory/applications/allProperties/read"
            ],
            "condition": null
        }
    ],
    "inheritsPermissionsFrom": []
}
```

### Example 2: Get the definition of a built-in role

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleDefinitions/3a2c62db-5318-420d-8d74-23affee5d9d5
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleDefinition -UnifiedRoleDefinitionId $unifiedRoleDefinitionId

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleDefinitions/$entity",
    "id": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
    "description": "Members of this role can create/manage groups, create/manage groups settings like naming and expiration policies, and view groups activity and audit reports.",
    "displayName": "Groups Administrator",
    "isBuiltIn": true,
    "isEnabled": true,
    "resourceScopes": [
        "/"
    ],
    "templateId": "fdd7a751-b60b-444a-984c-02652fe8fa1c",
    "version": "1",
    "rolePermissions": [
        {
            "allowedResourceActions": [
                "microsoft.directory/groups/assignLicense",
                "microsoft.directory/groups/create",
                "microsoft.directory/groups/delete",
                "microsoft.directory/groups/hiddenMembers/read",
                "microsoft.directory/groups/reprocessLicenseAssignment",
                "microsoft.directory/groups/restore",
                "microsoft.directory/groups/basic/update",
                "microsoft.directory/groups/classification/update",
                "microsoft.directory/groups/dynamicMembershipRule/update",
                "microsoft.directory/groups/groupType/update",
                "microsoft.directory/groups/members/update",
                "microsoft.directory/groups/owners/update",
                "microsoft.directory/groups/settings/update",
                "microsoft.directory/groups/visibility/update",
                "microsoft.azure.serviceHealth/allEntities/allTasks",
                "microsoft.azure.supportTickets/allEntities/allTasks",
                "microsoft.office365.serviceHealth/allEntities/allTasks",
                "microsoft.office365.supportTickets/allEntities/allTasks",
                "microsoft.office365.webPortal/allEntities/standard/read"
            ],
            "condition": null
        }
    ],
    "inheritsPermissionsFrom": [
        {
            "id": "88d8e3e3-8f55-4a1e-953a-9b9898b8876b"
        }
    ]
}
```

### Example 3: Get a soft-deleted custom role for the directory provider

#### Request

The following example shows a request.

```http
GET https://graph.microsoft.com/v1.0/roleManagement/directory/deletedItems/roleDefinitions/a1b2c3d4-5678-90ab-cdef-1234567890ab
```

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/deletedItems/roleDefinitions/$entity",
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
