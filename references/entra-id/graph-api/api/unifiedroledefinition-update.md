# Update unifiedRoleDefinition

> Source: https://learn.microsoft.com/en-us/graph/api/unifiedroledefinition-update?view=graph-rest-1.0  
> Microsoft doc last updated: 07/26/2024


Namespace: microsoft.graph

Update the properties of a [unifiedRoleDefinition](../resources/unifiedroledefinition.md) object. You cannot update built-in roles. This feature requires a Microsoft Entra ID P1 or P2 license.

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
PATCH /roleManagement/directory/roleDefinitions/{id}
```

## Request headers
    
| Name       | Description|
|:-----------|:-----------|
|Authorization|Bearer {token}. Required. Learn more about [authentication and authorization](https://learn.microsoft.com/en-us/graph/auth/auth-concepts).|
| Content-Type | application/json. Required. |
    
## Request body
    
In the request body, supply the values for relevant fields that should be updated. Existing properties that are not included in the request body will maintain their previous values or be recalculated based on changes to other property values. For the best performance, don't include existing values that haven't changed.
    
The following table shows the properties that are required when you update the [unifiedRoleDefinition](../resources/unifiedroledefinition.md).

| Property     | Type        | Description |
|:-------------|:------------|:------------|
|description|String| The description for the role definition. Read-only when **isBuiltIn** is `true`. |
|displayName|String| The display name for the role definition. Read-only when **isBuiltIn** is `true`. Required.|
|isEnabled|Boolean| Flag indicating if the role is enabled for assignment. If `false`, the role is not available for assignment. Read-only when **isBuiltIn** is true. |
|rolePermissions|[unifiedRolePermission](../resources/unifiedrolepermission.md) collection| List of permissions included in the role. Read-only when **isBuiltIn** is `true`. Required. |
|templateId|String| Custom template identifier that can be set when **isBuiltIn** is `false`. This identifier is typically used if one needs an identifier to be the same across different directories. Read-only when **isBuiltIn** is `true`. |
|version|String| Indicates version of the role definition. Read-only when **isBuiltIn** is `true`.|

## Response

If successful, this method returns a `204 No Content` response code. It doesn't return anything in the response body.

## Example

### Request

The following example shows a request.

# [HTTP](#tab/http)

```http
PATCH https://graph.microsoft.com/v1.0/roleManagement/directory/roleDefinitions/0d55728d-3e24-4309-9b1b-5ac09921475a
Content-type: application/json

{
  "description": "Update basic properties of application registrations",
  "displayName": "Application Registration Support Administrator",
  "rolePermissions":
    [
        {
            "allowedResourceActions": 
            [
                "microsoft.directory/applications/basic/read"
            ]
        }
    ]
}
```

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Identity.Governance

$params = @{
	description = "Update basic properties of application registrations"
	displayName = "Application Registration Support Administrator"
	rolePermissions = @(
		@{
			allowedResourceActions = @(
			"microsoft.directory/applications/basic/read"
		)
	}
)
}

Update-MgRoleManagementDirectoryRoleDefinition -UnifiedRoleDefinitionId $unifiedRoleDefinitionId -BodyParameter $params

```

---

### Response

The following example shows the response.

```http
HTTP/1.1 204 OK
Content-type: application/json
```
