# az lock

> Source: https://learn.microsoft.com/en-us/cli/azure/lock  
> Microsoft doc last updated: unknown

Manage Azure locks.

Subgroups and commands: `az_lock_create`, `az_lock_delete`, `az_lock_list`, `az_lock_show`, `az_lock_update`

## az lock create

Create a lock.

**Required parameters**

- `--lock-type -t` — The type of lock restriction.
- `--name -n` — Name of the lock.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--namespace` — Provider namespace (Ex: 'Microsoft.Provider').
- `--notes` — Notes about this lock.
- `--parent` — The parent path (Ex: 'resA/myA/resB/myB').
- `--resource --resource-name` — Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC').

*Create a read-only subscription level lock.*
```azurecli
az lock create --name lockName --lock-type ReadOnly
```

*Create a read-only resource group level lock.*
```azurecli
az lock create --name lockName --resource-group group --lock-type ReadOnly
```

*Create a read-only resource level lock on a vnet resource.*
```azurecli
az lock create --name lockName --resource-group group --lock-type ReadOnly --resource-type \
    Microsoft.Network/virtualNetworks --resource myVnet
```

*Create a read-only resource level lock on a subnet resource with a specific parent.*
```azurecli
az lock create --name lockName --resource-group group --lock-type ReadOnly --resource-type \
    Microsoft.Network/subnets --parent virtualNetworks/myVnet --resource mySubnet
```

## az lock delete

Delete a lock.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--ids` — One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
- `--name -n` — Name of the lock.
- `--namespace` — Provider namespace (Ex: 'Microsoft.Provider').
- `--parent` — The parent path (Ex: 'resA/myA/resB/myB').
- `--resource --resource-name` — Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC').

*Delete a subscription level lock*
```azurecli
az lock delete --name lockName
```

*Delete a resource group level lock*
```azurecli
az lock delete --name lockName --resource-group group
```

*Delete a resource level lock*
```azurecli
az lock delete --name lockName --resource-group group --resource resourceName --resource-type resourceType
```

## az lock list

List lock information.

**Optional parameters**

- `--filter-string` — A query filter to use to restrict the results.
- `--namespace` — Provider namespace (Ex: 'Microsoft.Provider').
- `--parent` — The parent path (Ex: 'resA/myA/resB/myB').
- `--resource --resource-name` — Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC').

*List out the locks on a vnet resource. Includes locks in the associated group and subscription.*
```azurecli
az lock list --resource myvnet --resource-type Microsoft.Network/virtualNetworks -g group
```

*List out all locks on the subscription level*
```azurecli
az lock list
```

## az lock show

Show the properties of a lock.

**Optional parameters**

- `--ids` — One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
- `--name -n` — Name of the lock.
- `--namespace` — Provider namespace (Ex: 'Microsoft.Provider').
- `--parent` — The parent path (Ex: 'resA/myA/resB/myB').
- `--resource --resource-name` — Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC').

*Show a subscription level lock*
```azurecli
az lock show -n lockname
```

*Show the properties of a lock (autogenerated)*
```azurecli
az lock show --name lockname --resource-group MyResourceGroup --resource-name MyResource --resource-type Microsoft.Network/virtualNetworks
```

## az lock update

Update a lock.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--ids` — One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
- `--lock-type -t` — The type of lock restriction.
- `--name -n` — Name of the lock.
- `--namespace` — Provider namespace (Ex: 'Microsoft.Provider').
- `--notes` — Notes about this lock.
- `--parent` — The parent path (Ex: 'resA/myA/resB/myB').
- `--resource --resource-name` — Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC').

*Update a resource group level lock with new notes and type*
```azurecli
az lock update --name lockName --resource-group group --notes newNotesHere --lock-type CanNotDelete
```
