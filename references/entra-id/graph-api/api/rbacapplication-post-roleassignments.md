# Create unifiedRoleAssignment

> Source: https://learn.microsoft.com/en-us/graph/api/rbacapplication-post-roleassignments?view=graph-rest-1.0  
> Microsoft doc last updated: 07/26/2024


Namespace: microsoft.graph

Create a new [unifiedRoleAssignment](../resources/unifiedroleassignment.md) object.

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

### For the entitlement management provider

|Permission type      | Permissions (from least to most privileged)              |
|:--------------------|:---------------------------------------------------------|
|Delegated (work or school account) |  EntitlementManagement.ReadWrite.All   |
|Delegated (personal Microsoft account) | Not supported.    |
|Application | EntitlementManagement.ReadWrite.All |

## HTTP request

Create a role assignment for the directory provider:

```http
POST /roleManagement/directory/roleAssignments
```

Create a role assignment for the entitlement management provider:

```http
POST /roleManagement/entitlementManagement/roleAssignments
```

## Request headers

| Name          | Description   |
|:--------------|:--------------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|

## Request body

In the request body, supply a JSON representation of a [unifiedRoleAssignment](../resources/unifiedroleassignment.md) object.

You can specify the following properties when creating a **unifiedRoleAssignment**.

| Property     | Type        | Description |
|:-------------|:------------|:------------|
|appScopeId|String|Required. Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by a resource application only. <br/><br/>For the entitlement management provider, use this property to specify a catalog, for example `/AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997`. <br/><br/> Either **appScopeId** or **directoryScopeId** must be specified.|
|directoryScopeId|String|Required. Identifier of the [directory object](../resources/directoryobject.md) representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications, unlike app scopes that are defined and understood by a resource application only. <br/><br/> For the directory (Microsoft Entra ID) provider, this property supports the following formats: <li> `/` for tenant-wide scope <li> `/administrativeUnits/{administrativeunit-ID}` to scope to an administrative unit <li> `/{application-objectID}` to scope to a resource application <br/><br/> For entitlement management provider, `/` for tenant-wide scope. To scope to an access package catalog, use the **appScopeId** property. <br/><br/> Either **appScopeId** or **directoryScopeId** must be specified.|
|principalId|String|Required. Identifier of the principal to which the assignment is granted. |
|roleDefinitionId|String| Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports `$filter` (`eq`, `in`). |

## Response

If successful, this method returns a `201 Created` response code and a new [unifiedRoleAssignment](../resources/unifiedroleassignment.md) object in the response body.

## Examples

### Example 1: Create a role assignment with tenant scope

#### Request

The following example shows a request. Note the use of the roleTemplateId for roleDefinitionId. roleDefinitionId can be either the service-wide template Id or the directory-specific roleDefinitionId.

# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments
Content-type: application/json

{ 
    "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
    "roleDefinitionId": "c2cf284d-6c41-4e6b-afac-4b80928c9034",
    "principalId": "f8ca5a85-489a-49a0-b555-0a6d81e56f0d",
    "directoryScopeId": "/"
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	"@odata.type" = "#microsoft.graph.unifiedRoleAssignment"
	roleDefinitionId = "c2cf284d-6c41-4e6b-afac-4b80928c9034"
	principalId = "f8ca5a85-489a-49a0-b555-0a6d81e56f0d"
	directoryScopeId = "/"
}

New-MgRoleManagementDirectoryRoleAssignment -BodyParameter $params

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability. 

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignments/$entity",
    "id": "YUb1sHQtUEyvox7IA_Eu_mm3jqnUe4lEhvatluHVi2I-1",
    "roleDefinitionId": "c2cf284d-6c41-4e6b-afac-4b80928c9034",
    "principalId": "f8ca5a85-489a-49a0-b555-0a6d81e56f0d",
    "directoryScopeId": "/"
}
```

### Example 2: Create a role assignment with administrative unit scope

#### Request

The following example assigns the User Administrator role to a principal with administrative unit scope.

# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments
Content-type: application/json

{
    "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
    "roleDefinitionId": "fe930be7-5e62-47db-91af-98c3a49a38b1",
    "principalId": "f8ca5a85-489a-49a0-b555-0a6d81e56f0d",
    "directoryScopeId": "/administrativeUnits/5d107bba-d8e2-4e13-b6ae-884be90e5d1a"
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	"@odata.type" = "#microsoft.graph.unifiedRoleAssignment"
	roleDefinitionId = "fe930be7-5e62-47db-91af-98c3a49a38b1"
	principalId = "f8ca5a85-489a-49a0-b555-0a6d81e56f0d"
	directoryScopeId = "/administrativeUnits/5d107bba-d8e2-4e13-b6ae-884be90e5d1a"
}

New-MgRoleManagementDirectoryRoleAssignment -BodyParameter $params

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignments/$entity",
    "id": "BH21sHQtUEyvox7IA_Eu_mm3jqnUe4lEhvatluHIWb7-1",
    "roleDefinitionId": "fe930be7-5e62-47db-91af-98c3a49a38b1",
    "principalId": "f8ca5a85-489a-49a0-b555-0a6d81e56f0d",
    "directoryScopeId": "/administrativeUnits/5d107bba-d8e2-4e13-b6ae-884be90e5d1a"
}
```

### Example 3: Create a role assignment with application scope

#### Request

The following example assigns a principal the Application Administrator role at application scope. The object ID of the application registration is 661e1310-bd76-4795-89a7-8f3c8f855bfc.

# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments
Content-type: application/json

{
    "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
    "principalId": "6b937a9d-c731-465b-a844-2d5b5368c161",
    "roleDefinitionId": "9b895d92-2cd3-44c7-9d02-a6ac2d5ea5c3",
    "directoryScopeId": "/661e1310-bd76-4795-89a7-8f3c8f855bfc"
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	"@odata.type" = "#microsoft.graph.unifiedRoleAssignment"
	principalId = "6b937a9d-c731-465b-a844-2d5b5368c161"
	roleDefinitionId = "9b895d92-2cd3-44c7-9d02-a6ac2d5ea5c3"
	directoryScopeId = "/661e1310-bd76-4795-89a7-8f3c8f855bfc"
}

New-MgRoleManagementDirectoryRoleAssignment -BodyParameter $params

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/directory/roleAssignments/$entity",
    "id": "kl2Jm9Msx0SdAqasLV6lw516k2sxx1tGqEQtW1NowWEQEx5mdr2VR4mnjzyPhVv8-1",
    "principalId": "6b937a9d-c731-465b-a844-2d5b5368c161",
    "directoryScopeId": "/661e1310-bd76-4795-89a7-8f3c8f855bfc",
    "roleDefinitionId": "9b895d92-2cd3-44c7-9d02-a6ac2d5ea5c3"
}
```

### Example 4: Create a role assignment with access package catalog scope

#### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
POST https://graph.microsoft.com/v1.0/roleManagement/entitlementManagement/roleAssignments
Content-type: application/json

{
    "principalId": "679a9213-c497-48a4-830a-8d3d25d94ddc",
    "roleDefinitionId": "ae79f266-94d4-4dab-b730-feca7e132178",
    "appScopeId": "/AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997"
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	principalId = "679a9213-c497-48a4-830a-8d3d25d94ddc"
	roleDefinitionId = "ae79f266-94d4-4dab-b730-feca7e132178"
	appScopeId = "/AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997"
}

New-MgRoleManagementEntitlementManagementRoleAssignment -BodyParameter $params

```

---

#### Response

The following example shows the response.

> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#roleManagement/entitlementManagement/roleAssignments/$entity",
    "id": "f3092518-7874-462e-93e9-0cd6c11ffc52",
    "principalId": "679a9213-c497-48a4-830a-8d3d25d94ddc",
    "roleDefinitionId": "ae79f266-94d4-4dab-b730-feca7e132178",
    "appScopeId": "/AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997"
}
```
