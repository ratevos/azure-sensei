# az account management-group

> Source: https://learn.microsoft.com/en-us/cli/azure/account/management-group  
> Microsoft doc last updated: unknown

Manage Azure Management Groups.

Subgroups and commands: `az_account_management-group_check-name-availability`, `az_account_management-group_create`, `az_account_management-group_delete`, `az_account_management-group_entities`, `az_account_management-group_entities_list`, `az_account_management-group_hierarchy-settings`, `az_account_management-group_hierarchy-settings_create`, `az_account_management-group_hierarchy-settings_delete`, `az_account_management-group_hierarchy-settings_list`, `az_account_management-group_hierarchy-settings_update`, `az_account_management-group_list`, `az_account_management-group_show`, `az_account_management-group_subscription`, `az_account_management-group_subscription_add`, `az_account_management-group_subscription_remove`, `az_account_management-group_subscription_show`, `az_account_management-group_subscription_show-sub-under-mg`, `az_account_management-group_tenant-backfill`, `az_account_management-group_tenant-backfill_get`, `az_account_management-group_tenant-backfill_start`, `az_account_management-group_update`

## az account management-group check-name-availability

Check if a Management Group Name is Valid.

**Required parameters**

- `--name -n` — Name of the management group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Check if a Management Group Name is Valid.*
```azurecli
az account management-group check-name-availability --name GroupName
```

## az account management-group create

Create a new management group.

**Required parameters**

- `--name -n` — Name of the management group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--display-name -d` — Sets the display name of the management group. If null, the group name is set as the display name.
- `--no-register` — Skip registration for resource provider Microsoft.Management. Default: False.
- `--parent -p` — Sets the parent of the management group. Can be the fully qualified id or the name of the management group. If null, the root tenant group is set as the parent.

*Create a new management group.*
```azurecli
az account management-group create --name GroupName
```

*Create a new management group with a specific display name.*
```azurecli
az account management-group create --name GroupName --display-name DisplayName
```

*Create a new management group with a specific parent.*
```azurecli
az account management-group create --name GroupName --parent ParentId/ParentName
```

*Create a new management group with a specific display name and parent.*
```azurecli
az account management-group create --name GroupName --display-name DisplayName --parent ParentId/ParentName
```

## az account management-group delete

Delete an existing management group.

**Required parameters**

- `--name -n` — Name of the management group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-register` — Skip registration for resource provider Microsoft.Management. Default: False.

*Delete an existing management group*
```azurecli
az account management-group delete --name GroupName
```

## az account management-group list

List all management groups in the current tenant.

**Optional parameters**

- `--no-register` — Skip registration for resource provider Microsoft.Management. Default: False.

*List all management groups*
```azurecli
az account management-group list
```

## az account management-group show

Get the details of the management group.

**Required parameters**

- `--name -n` — Name of the management group (the last segment of the resource ID). Do not use display name.

**Optional parameters**

- `--expand -e` — If given, lists the children in the first level of hierarchy. Default: False.
- `--no-register` — Skip registration for resource provider Microsoft.Management. Default: False.
- `--recurse -r` — If given, lists the children in all levels of hierarchy. Default: False.

*Get a management group.*
```azurecli
az account management-group show --name GroupName
```

*Get a management group with children in the first level of hierarchy.*
```azurecli
az account management-group show --name GroupName -e
```

*Get a management group with children in all levels of hierarchy.*
```azurecli
az account management-group show --name GroupName -e -r
```

## az account management-group update

Update an existing management group.

**Required parameters**

- `--name -n` — Name of the management group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`. Default: [].
- `--change-reference` — The related change reference ID for this resource operation.
- `--display-name -d` — Updates the display name of the management group. If null, no change is made.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON. Default: False.
- `--parent -p` — Update the parent of the management group. Can be the fully qualified id or the name of the management group. If null, no change is made.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`. Default: [].
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`. Default: [].

*Update an existing management group with a specific display name.*
```azurecli
az account management-group update --name GroupName --display-name DisplayName
```

*Update an existing management group with a specific parent.*
```azurecli
az account management-group update --name GroupName --parent ParentId/ParentName
```

*Update an existing management group with a specific display name and parent.*
```azurecli
az account management-group update --name GroupName --display-name DisplayName --parent ParentId/ParentName
```
