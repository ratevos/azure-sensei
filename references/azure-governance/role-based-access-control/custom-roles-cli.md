# Create or update Azure custom roles using Azure CLI - Azure RBAC

> Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles-cli  
> Microsoft doc last updated: 12/01/2023


If the [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) don't meet the specific needs of your organization, you can create your own custom roles. This article describes how to list, create, update, or delete custom roles using Azure CLI.

For a step-by-step tutorial on how to create a custom role, see [Tutorial: Create an Azure custom role using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-cli).

## Prerequisites

To create custom roles, you need:

- Permissions to create custom roles, such as [User Access Administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator)
- [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview) or [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

## List custom roles

To list custom roles that are available for assignment, use [az role definition list](https://learn.microsoft.com/en-us/cli/azure/role/definition#az-role-definition-list). The following example lists all the custom roles in the current subscription.

```azurecli
az role definition list --custom-role-only true --output json --query '[].{roleName:roleName, roleType:roleType}'
```

```json
[
  {
    "roleName": "My Management Contributor",
    "type": "CustomRole"
  },
  {
    "roleName": "My Service Reader Role",
    "type": "CustomRole"
  },
  {
    "roleName": "Virtual Machine Operator",
    "type": "CustomRole"
  }
]
```

## List a custom role definition

To list a custom role definition, use [az role definition list](https://learn.microsoft.com/en-us/cli/azure/role/definition#az-role-definition-list). This command is the same command you would use for a built-in role.

```azurecli
az role definition list --name {roleName}
```

The following example lists the *Virtual Machine Operator* role definition:

```azurecli
az role definition list --name "Virtual Machine Operator"
```

```json
[
  {
    "assignableScopes": [
      "/subscriptions/{subscriptionId}"
    ],
    "description": "Can monitor and restart virtual machines.",
    "id": "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/roleDefinitions/00000000-0000-0000-0000-000000000000",
    "name": "00000000-0000-0000-0000-000000000000",
    "permissions": [
      {
        "actions": [
          "Microsoft.Storage/*/read",
          "Microsoft.Network/*/read",
          "Microsoft.Compute/*/read",
          "Microsoft.Compute/virtualMachines/start/action",
          "Microsoft.Compute/virtualMachines/restart/action",
          "Microsoft.Authorization/*/read",
          "Microsoft.ResourceHealth/availabilityStatuses/read",
          "Microsoft.Resources/subscriptions/resourceGroups/read",
          "Microsoft.Insights/alertRules/*",
          "Microsoft.Insights/diagnosticSettings/*",
          "Microsoft.Support/*"
        ],
        "dataActions": [],
        "notActions": [],
        "notDataActions": []
      }
    ],
    "roleName": "Virtual Machine Operator",
    "roleType": "CustomRole",
    "type": "Microsoft.Authorization/roleDefinitions"
  }
]
```

The following example lists just the actions of the *Virtual Machine Operator* role:

```azurecli
az role definition list --name "Virtual Machine Operator" --output json --query '[].permissions[0].actions'
```

```json
[
  [
    "Microsoft.Storage/*/read",
    "Microsoft.Network/*/read",
    "Microsoft.Compute/*/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/restart/action",
    "Microsoft.Authorization/*/read",
    "Microsoft.ResourceHealth/availabilityStatuses/read",
    "Microsoft.Resources/subscriptions/resourceGroups/read",
    "Microsoft.Insights/alertRules/*",
    "Microsoft.Insights/diagnosticSettings/*",
    "Microsoft.Support/*"
  ]
]
```

## Create a custom role

To create a custom role, use [az role definition create](https://learn.microsoft.com/en-us/cli/azure/role/definition#az-role-definition-create). The role definition can be a JSON description or a path to a file containing a JSON description.

```azurecli
az role definition create --role-definition {roleDefinition}
```

The following example creates a custom role named *Virtual Machine Operator*. This custom role assigns access to all read actions of *Microsoft.Compute*, *Microsoft.Storage*, and *Microsoft.Network* resource providers and assigns access to start, restart, and monitor virtual machines. This custom role can be used in two subscriptions. This example uses a JSON file as an input.

vmoperator.json

```json
{
  "Name": "Virtual Machine Operator",
  "IsCustom": true,
  "Description": "Can monitor and restart virtual machines.",
  "Actions": [
    "Microsoft.Storage/*/read",
    "Microsoft.Network/*/read",
    "Microsoft.Compute/*/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/restart/action",
    "Microsoft.Authorization/*/read",
    "Microsoft.ResourceHealth/availabilityStatuses/read",
    "Microsoft.Resources/subscriptions/resourceGroups/read",
    "Microsoft.Insights/alertRules/*",
    "Microsoft.Support/*"
  ],
  "NotActions": [

  ],
  "AssignableScopes": [
    "/subscriptions/{subscriptionId1}",
    "/subscriptions/{subscriptionId2}"
  ]
}
```

```azurecli
az role definition create --role-definition ~/roles/vmoperator.json
```

## Update a custom role

To update a custom role, first use [az role definition list](https://learn.microsoft.com/en-us/cli/azure/role/definition#az-role-definition-list) to retrieve the role definition. Second, make the desired changes to the role definition. Finally, use [az role definition update](https://learn.microsoft.com/en-us/cli/azure/role/definition#az-role-definition-update) to save the updated role definition.

```azurecli
az role definition update --role-definition {roleDefinition}
```

The following example adds the *Microsoft.Insights/diagnosticSettings/* action to `Actions` and adds a management group to `AssignableScopes` for the *Virtual Machine Operator* custom role.

vmoperator.json

```json
{
  "Name": "Virtual Machine Operator",
  "IsCustom": true,
  "Description": "Can monitor and restart virtual machines.",
  "Actions": [
    "Microsoft.Storage/*/read",
    "Microsoft.Network/*/read",
    "Microsoft.Compute/*/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/restart/action",
    "Microsoft.Authorization/*/read",
    "Microsoft.ResourceHealth/availabilityStatuses/read",
    "Microsoft.Resources/subscriptions/resourceGroups/read",
    "Microsoft.Insights/alertRules/*",
    "Microsoft.Insights/diagnosticSettings/*",
    "Microsoft.Support/*"
  ],
  "NotActions": [

  ],
  "AssignableScopes": [
    "/subscriptions/{subscriptionId1}",
    "/subscriptions/{subscriptionId2}",
    "/providers/Microsoft.Management/managementGroups/marketing-group"
  ]
}
```

```azurecli
az role definition update --role-definition ~/roles/vmoperator.json
```

## Delete a custom role

1. Remove any role assignments that use the custom role. For more information, see [Find role assignments to delete a custom role](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles#find-role-assignments-to-delete-a-custom-role).

1. Use [az role definition delete](https://learn.microsoft.com/en-us/cli/azure/role/definition#az-role-definition-delete) to delete the custom role. To specify the role to delete, use the role name or the role ID. To determine the role ID, use [az role definition list](https://learn.microsoft.com/en-us/cli/azure/role/definition#az-role-definition-list).

    ```azurecli
    az role definition delete --name {roleNameOrId}
    ```
    
    The following example deletes the *Virtual Machine Operator* custom role.
    
    ```azurecli
    az role definition delete --name "Virtual Machine Operator"
    ```
    
## Next steps

- [Tutorial: Create an Azure custom role using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-cli)
- [Azure custom roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)
- [Azure resource provider operations](https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations)
