# az group

> Source: https://learn.microsoft.com/en-us/cli/azure/group  
> Microsoft doc last updated: unknown

Manage resource groups and template deployments.

Subgroups and commands: `az_group_create`, `az_group_delete`, `az_group_exists`, `az_group_export`, `az_group_list`, `az_group_lock`, `az_group_lock_create`, `az_group_lock_delete`, `az_group_lock_list`, `az_group_lock_show`, `az_group_lock_update`, `az_group_show`, `az_group_update`, `az_group_wait`

## az group create

Create a new resource group.

**Required parameters**

- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--name --resource-group -g -n` — Name of the new resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--managed-by` — The ID of the resource that manages this resource group.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.

*Create a new resource group in the West US region.*
```azurecli
az group create -l westus -n MyResourceGroup
```

## az group delete

Delete a resource group.

**Required parameters**

- `--name --resource-group -g -n` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--force-deletion-types -f` — The resource types you want to force delete.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a resource group.*
```azurecli
az group delete -n MyResourceGroup
```

*Force delete all the Virtual Machines in a resource group.*
```azurecli
az group delete -n MyResourceGroup --force-deletion-types Microsoft.Compute/virtualMachines
```

## az group exists

Check if a resource group exists.

**Required parameters**

- `--name --resource-group -g -n` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Check if 'MyResourceGroup' exists.*
```azurecli
az group exists -n MyResourceGroup
```

## az group export

Captures a resource group as a template.

**Required parameters**

- `--name --resource-group -g -n` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--export-format` — The format of the exported template. Default: json.
- `--include-comments` — Export template with comments. Default: False.
- `--include-parameter-default-value` — Export template parameter with default value. Default: False.
- `--resource-ids` — Space-separated resource ids to filter the export by. To export all resources, do not specify this argument or supply "*".
- `--skip-all-params` — Export template parameter and skip all parameterization. Default: False.
- `--skip-resource-name-params` — Export template and skip resource name parameterization. Default: False.

## az group list

List resource groups.

**Optional parameters**

- `--tag` — A single tag in 'key[=value]' format. Use "" to clear existing tags.

*List all resource groups located in the West US region.*
```azurecli
az group list --query "[?location=='westus']"
```

## az group show

Gets a resource group.

**Required parameters**

- `--name --resource-group -g -n` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az group update

Update a resource group.

**Required parameters**

- `--name --resource-group -g -n` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON. Default: False.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`. Default: [].
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.

*Update a resource group. (autogenerated)*
```azurecli
az group update --resource-group MyResourceGroup --set tags.CostCenter='{"Dept":"IT","Environment":"Test"}'
```

## az group wait

Place the CLI in a waiting state until a condition of the resource group is met.

**Required parameters**

- `--name --resource-group -g -n` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Place the CLI in a waiting state until a condition of the resource group is met. (autogenerated)*
```azurecli
az group wait --created  --resource-group MyResourceGroup
```

*Place the CLI in a waiting state until a condition of the resource group is met. (autogenerated)*
```azurecli
az group wait --deleted --resource-group MyResourceGroup
```
