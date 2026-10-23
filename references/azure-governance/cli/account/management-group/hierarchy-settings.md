# az account management-group hierarchy-settings

> Source: https://learn.microsoft.com/en-us/cli/azure/account/management-group/hierarchy-settings  
> Microsoft doc last updated: unknown

Provide operations for hierarchy settings defined at the management group level. Settings can only be set on the root Management Group of the hierarchy.

Subgroups and commands: `az_account_management-group_hierarchy-settings_create`, `az_account_management-group_hierarchy-settings_delete`, `az_account_management-group_hierarchy-settings_list`, `az_account_management-group_hierarchy-settings_update`

## az account management-group hierarchy-settings create

Create hierarchy settings defined at the Management Group level.

**Required parameters**

- `--name -n` — Name of the management group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--default-management-group -m` — Set the default Management Group under which new subscriptions get added in this tenant. Default setting is the Root Management Group.
- `--require-authorization-for-group-creation -r` — Indicate whether RBAC access is required upon group creation under the root Management Group. True means user will require Microsoft.Management/managementGroups/write action on the root Management Group. Default setting is false.

*Create hierarchy settings defined at the Management Group level.*
```azurecli
az account management-group hierarchy-settings create --name GroupName
```

*Set the default Management Group new Subscriptions get placed under.*
```azurecli
az account management-group hierarchy-settings create --name GroupName -m /providers/Microsoft.Management/managementGroups/DefaultGroup
```

*Require user to have Microsoft.Management/managementGroups/write access on the Root to create new Management Groups under the Root.*
```azurecli
az account management-group hierarchy-settings create --name GroupName -r True
```

*Update both hierarchy settings.*
```azurecli
az account management-group hierarchy-settings create --name GroupName -m /providers/Microsoft.Management/managementGroups/DefaultGroup -r True
```

## az account management-group hierarchy-settings delete

Delete the hierarchy settings defined at the Management Group level.

**Required parameters**

- `--name -n` — Name of the management group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete all hierarchy settings defined at the Management Group level.*
```azurecli
az account management-group hierarchy-settings delete --name GroupName
```

## az account management-group hierarchy-settings list

Get all the hierarchy settings defined at the Management Group level.

**Required parameters**

- `--name -n` — Name of the management group.

*Get all hierarchy settings defined at the Management Group level.*
```azurecli
az account management-group hierarchy-settings list --name GroupName
```

## az account management-group hierarchy-settings update

Update the hierarchy settings defined at the Management Group level.

**Required parameters**

- `--name -n` — Name of the management group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`. Default: [].
- `--change-reference` — The related change reference ID for this resource operation.
- `--default-management-group -m` — Set the default Management Group under which new subscriptions get added in this tenant. Default setting is the Root Management Group.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON. Default: False.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`. Default: [].
- `--require-authorization-for-group-creation -r` — Indicate whether RBAC access is required upon group creation under the root Management Group. True means user will require Microsoft.Management/managementGroups/write action on the root Management Group. Default setting is false.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`. Default: [].

*Create hierarchy settings defined at the Management Group level.*
```azurecli
az account management-group hierarchy-settings update --name GroupName
```

*Set the default Management Group new Subscriptions get placed under.*
```azurecli
az account management-group hierarchy-settings update --name GroupName -m /providers/Microsoft.Management/managementGroups/DefaultGroup
```

*Require user to have Microsoft.Management/managementGroups/write access on the Root to create new Management Groups under the Root.*
```azurecli
az account management-group hierarchy-settings update --name GroupName -r True
```

*Update both hierarchy settings.*
```azurecli
az account management-group hierarchy-settings update --name GroupName -m /providers/Microsoft.Management/managementGroups/DefaultGroup -r True
```
