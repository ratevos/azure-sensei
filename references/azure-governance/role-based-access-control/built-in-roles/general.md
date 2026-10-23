# Azure built-in roles for General - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general  
> Microsoft doc last updated: 07/01/2026


This article lists the Azure built-in roles in the General category.

## Reader

View all resources, but does not allow you to make any changes.

> [!NOTE]
> This role includes the `*/read` action for the control plane. Users that are assigned this role can read [control plane](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-definitions#control-and-data-actions) information for all Azure resources.

[Learn more](https://learn.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles)

> | Actions | Description |
> | --- | --- |
> | */read | Read control plane information for all Azure resources. |
> | **NotActions** |  |
> | *none* |  |
> | **DataActions** |  |
> | *none* |  |
> | **NotDataActions** |  |
> | *none* |  |

```json
{
  "assignableScopes": [
    "/"
  ],
  "description": "View all resources, but does not allow you to make any changes.",
  "id": "/providers/Microsoft.Authorization/roleDefinitions/acdd72a7-3385-48ef-bd42-f606fba81ae7",
  "name": "acdd72a7-3385-48ef-bd42-f606fba81ae7",
  "permissions": [
    {
      "actions": [
        "*/read"
      ],
      "notActions": [],
      "dataActions": [],
      "notDataActions": []
    }
  ],
  "roleName": "Reader",
  "roleType": "BuiltInRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

## Next steps

- [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)
