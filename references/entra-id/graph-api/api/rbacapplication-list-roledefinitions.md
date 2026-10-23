# List roleDefinitions

> Source: https://learn.microsoft.com/en-us/graph/api/rbacapplication-list-roledefinitions?view=graph-rest-1.0  
> Microsoft doc last updated: 07/26/2024


Namespace: microsoft.graph

Get a list of [unifiedRoleDefinition](../resources/unifiedroledefinition.md) objects for the provider.

The following RBAC providers are currently supported:
- directory (Microsoft Entra ID)
- entitlement management (Microsoft Entra Entitlement Management)

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
|Application | EntitlementManagement.Read.All, EntitlementManagement.ReadWrite.All |

## HTTP request

To list role definitions for the directory provider:

```http
GET /roleManagement/directory/roleDefinitions
```

To list role definitions for the entitlement management provider:

```http
GET /roleManagement/entitlementManagement/roleDefinitions
```

## Optional query parameters
This method supports the `$filter` (`eq` and `in` operators) OData query parameter on `id`, `displayName`, and `isBuiltIn` properties. It also supports `$expand` on the relationships. For general information, see [OData query parameters](https://learn.microsoft.com/en-us/graph/query-parameters).

## Request headers

| Name      |Description|
|:----------|:----------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [unifiedRoleDefinition](../resources/unifiedroledefinition.md) objects in the response body.

## Example

### Example 1: Retrieve role definitions for the directory provider

#### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleDefinitions
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementDirectoryRoleDefinition

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleDefinitions",
    "value": [
        {
            "id": "729827e3-9c14-49f7-bb1b-9608f156bbb8",
            "description": "Can reset passwords for non-administrators and Helpdesk Administrators.",
            "displayName": "Helpdesk Administrator",
            "isBuiltIn": true,
            "isEnabled": true,
            "templateId": "729827e3-9c14-49f7-bb1b-9608f156bbb8",
            "version": "1",
            "rolePermissions": [
                {
                    "allowedResourceActions": [
                        "microsoft.directory/users/invalidateAllRefreshTokens",
                        "microsoft.directory/users/bitLockerRecoveryKeys/read",
                        "microsoft.directory/users/password/update",
                        "microsoft.azure.serviceHealth/allEntities/allTasks",
                        "microsoft.azure.supportTickets/allEntities/allTasks",
                        "microsoft.office365.webPortal/allEntities/standard/read",
                        "microsoft.office365.serviceHealth/allEntities/allTasks",
                        "microsoft.office365.supportTickets/allEntities/allTasks"
                    ],
                    "condition": null
                }
            ],
            "inheritsPermissionsFrom": [
                {
                    "id": "88d8e3e3-8f55-4a1e-953a-9b9898b8876b"
                }
            ]
        },
        {
            "id": "f023fd81-a637-4b56-95fd-791ac0226033",
            "description": "Can read service health information and manage support tickets.",
            "displayName": "Service Support Administrator",
            "isBuiltIn": true,
            "isEnabled": true,
            "templateId": "f023fd81-a637-4b56-95fd-791ac0226033",
            "version": "1",
            "rolePermissions": [
                {
                    "allowedResourceActions": [
                        "microsoft.azure.serviceHealth/allEntities/allTasks",
                        "microsoft.azure.supportTickets/allEntities/allTasks",
                        "microsoft.office365.webPortal/allEntities/standard/read",
                        "microsoft.office365.serviceHealth/allEntities/allTasks",
                        "microsoft.office365.supportTickets/allEntities/allTasks"
                    ],
                    "condition": null
                }
            ],
            "inheritsPermissionsFrom": [
                {
                    "id": "88d8e3e3-8f55-4a1e-953a-9b9898b8876b"
                }
            ]
        },
        {
            "id": "b0f54661-2d74-4c50-afa3-1ec803f12efe",
            "description": "Can perform common billing related tasks like updating payment information.",
            "displayName": "Billing Administrator",
            "isBuiltIn": true,
            "isEnabled": true,
            "templateId": "b0f54661-2d74-4c50-afa3-1ec803f12efe",
            "version": "1",
            "rolePermissions": [
                {
                    "allowedResourceActions": [
                        "microsoft.directory/organization/basic/update",
                        "microsoft.azure.serviceHealth/allEntities/allTasks",
                        "microsoft.azure.supportTickets/allEntities/allTasks",
                        "microsoft.commerce.billing/allEntities/allTasks",
                        "microsoft.office365.webPortal/allEntities/standard/read",
                        "microsoft.office365.serviceHealth/allEntities/allTasks",
                        "microsoft.office365.supportTickets/allEntities/allTasks"
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
    ]
}
```

### Example 2: Retrieve role definitions for the entitlement management provider

#### Request

# [HTTP](#tab/http)

```msgraph-interactive
GET https://graph.microsoft.com/v1.0/roleManagement/entitlementManagement/roleDefinitions
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

Get-MgRoleManagementEntitlementManagementRoleDefinition

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/entitlementManagement/roleDefinitions",
    "value": [
        {
            "id": "ae79f266-94d4-4dab-b730-feca7e132178",
            "displayName": "Catalog owner",
            "description": "Catalog owner",
            "isBuiltIn": true,
            "isEnabled": true,
            "templateId": "ae79f266-94d4-4dab-b730-feca7e132178",
            "version": "1.0",
            "rolePermissions": [
                {
                    "allowedResourceActions": [
                        "microsoft.entitlementManagement/allEntities/allTasks"
                    ],
                    "condition": null
                }
            ]
        },
        {
            "id": "44272f93-9762-48e8-af59-1b5351b1d6b3",
            "displayName": "Catalog reader",
            "description": "Catalog reader",
            "isBuiltIn": true,
            "isEnabled": true,
            "templateId": "44272f93-9762-48e8-af59-1b5351b1d6b3",
            "version": "1.0",
            "rolePermissions": [
                {
                    "allowedResourceActions": [
                        "microsoft.entitlementManagement/allEntities/Read"
                    ],
                    "condition": null
                }
            ]
        },
        {
            "id": "7f480852-ebdc-47d4-87de-0d8498384a83",
            "displayName": "AccessPackages manager",
            "description": "AccessPackages manager",
            "isBuiltIn": true,
            "isEnabled": true,
            "templateId": "7f480852-ebdc-47d4-87de-0d8498384a83",
            "version": "1.0",
            "rolePermissions": [
                {
                    "allowedResourceActions": [
                        "microsoft.entitlementManagement/AccessPackageCatalog/AccessPackage/allTasks",
                        "microsoft.entitlementManagement/AccessPackageCatalog/allEntities/Read"
                    ],
                    "condition": null
                }
            ]
        },
        {
            "id": "ba92d953-d8e0-4e39-a797-0cbedb0a89e8",
            "displayName": "Catalog creator",
            "description": "Catalog creator",
            "isBuiltIn": true,
            "isEnabled": true,
            "templateId": "ba92d953-d8e0-4e39-a797-0cbedb0a89e8",
            "version": "1.0",
            "rolePermissions": [
                {
                    "allowedResourceActions": [
                        "microsoft.entitlementManagement/AccessPackageCatalog/Create"
                    ],
                    "condition": null
                }
            ]
        },
        {
            "id": "e2182095-804a-4656-ae11-64734e9b7ae5",
            "displayName": "AccessPackage assignment manager",
            "description": "AccessPackage assignment manager",
            "isBuiltIn": true,
            "isEnabled": true,
            "templateId": "e2182095-804a-4656-ae11-64734e9b7ae5",
            "version": "1.0",
            "rolePermissions": [
                {
                    "allowedResourceActions": [
                        "microsoft.entitlementManagement/AccessPackageCatalog/AccessPackage/GrantRequests/allTasks",
                        "microsoft.entitlementManagement/AccessPackageCatalog/AccessPackage/Grants/allTasks",
                        "microsoft.entitlementManagement/AccessPackageCatalog/allEntities/Read"
                    ],
                    "condition": null
                }
            ]
        }
    ]
}
```
