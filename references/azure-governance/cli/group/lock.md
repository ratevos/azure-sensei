# az group lock

> Source: https://learn.microsoft.com/en-us/cli/azure/group/lock  
> Microsoft doc last updated: unknown

Manage Azure resource group locks.

Subgroups and commands: `az_group_lock_create`, `az_group_lock_delete`, `az_group_lock_list`, `az_group_lock_show`, `az_group_lock_update`

## az group lock create

Create a resource group lock.

**Required parameters**

- `--lock-type -t` — The type of lock restriction.
- `--name -n` — Name of the lock.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--notes` — Notes about this lock.

*Create a read-only resource group level lock.*
```azurecli
az group lock create --lock-type ReadOnly -n lockName -g MyResourceGroup
```

## az group lock delete

Delete a resource group lock.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--ids` — One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
- `--name -n` — Name of the lock.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Delete a resource group lock*
```azurecli
az group lock delete --name lockName -g MyResourceGroup
```

## az group lock list

List lock information in the resource-group.

**Required parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--filter-string` — A query filter to use to restrict the results.

*List out all locks on the resource group level*
```azurecli
az group lock list -g MyResourceGroup
```

## az group lock show

Show the details of a resource group lock.

**Optional parameters**

- `--ids` — One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
- `--name -n` — Name of the lock.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Show a resource group level lock*
```azurecli
az group lock show -n lockname -g MyResourceGroup
```

## az group lock update

Update a resource group lock.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--ids` — One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
- `--lock-type -t` — The type of lock restriction.
- `--name -n` — Name of the lock.
- `--notes` — Notes about this lock.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Update a resource group lock with new notes and type*
```azurecli
az group lock update --name lockName -g MyResourceGroup --notes newNotesHere --lock-type CanNotDelete
```
