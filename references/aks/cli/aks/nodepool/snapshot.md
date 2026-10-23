# az aks nodepool snapshot

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool/snapshot  
> Microsoft doc last updated: unknown

Commands to manage nodepool snapshots.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_nodepool_snapshot_create`, `az_aks_nodepool_snapshot_create(aks-preview)`, `az_aks_nodepool_snapshot_delete`, `az_aks_nodepool_snapshot_delete(aks-preview)`, `az_aks_nodepool_snapshot_list`, `az_aks_nodepool_snapshot_list(aks-preview)`, `az_aks_nodepool_snapshot_show`, `az_aks_nodepool_snapshot_show(aks-preview)`, `az_aks_nodepool_snapshot_update`, `az_aks_nodepool_snapshot_update(aks-preview)`, `az_aks_nodepool_snapshot_wait`

## az aks nodepool snapshot create

Create a nodepool snapshot.

**Required parameters**

- `--name -n` — The nodepool snapshot name.
- `--nodepool-id` — The source nodepool id from which to create this snapshot.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — The tags of the snapshot.

*Create a nodepool snapshot.*
```azurecli
az aks nodepool snapshot create -g MyResourceGroup -n snapshot1 --nodepool-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedClusters/akscluster1/agentPools/nodepool1"
```

*Create a nodepool snapshot with custom tags.*
```azurecli
az aks nodepool snapshot create -g MyResourceGroup -n snapshot1 --nodepool-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedClusters/akscluster1/agentPools/nodepool1" --tags "foo=bar" "key1=val1"
```

## az aks nodepool snapshot create  (extension: aks-preview etc.)

Create a nodepool snapshot.

**Required parameters**

- `--name -n` — The nodepool snapshot name.
- `--nodepool-id` — The source nodepool id from which to create this snapshot.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — The tags of the snapshot.

*Create a nodepool snapshot.*
```azurecli
az aks nodepool snapshot create -g MyResourceGroup -n snapshot1 --nodepool-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedClusters/akscluster1/agentPools/nodepool1"
```

*Create a nodepool snapshot with custom tags.*
```azurecli
az aks nodepool snapshot create -g MyResourceGroup -n snapshot1 --nodepool-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedClusters/akscluster1/agentPools/nodepool1" --tags "foo=bar" "key1=val1"
```

## az aks nodepool snapshot delete

Delete a nodepool snapshot.

**Required parameters**

- `--name -n` — The nodepool snapshot name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks nodepool snapshot delete  (extension: aks-preview etc.)

Delete a nodepool snapshot.

**Required parameters**

- `--name -n` — The nodepool snapshot name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks nodepool snapshot list

List nodepool snapshots.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks nodepool snapshot list  (extension: aks-preview etc.)

List nodepool snapshots.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks nodepool snapshot show

Show the details of a nodepool snapshot.

**Required parameters**

- `--name -n` — The nodepool snapshot name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks nodepool snapshot show  (extension: aks-preview etc.)

Show the details of a nodepool snapshot.

**Required parameters**

- `--name -n` — The nodepool snapshot name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks nodepool snapshot update

Update tags on a snapshot of a nodepool.

**Required parameters**

- `--name -n` — The nodepool snapshot name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--tags` — The tags to set to the snapshot.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Update tags on a nodepool snapshot.*
```azurecli
az aks nodepool snapshot update -g MyResourceGroup -n snapshot1 --tags "foo=bar" "key1=val1"
```

*Clear tags on a nodepool snapshot.*
```azurecli
az aks nodepool snapshot update -g MyResourceGroup -n snapshot1 --tags ""
```

## az aks nodepool snapshot update  (extension: aks-preview etc.)

Update tags on a snapshot of a nodepool.

**Required parameters**

- `--name -n` — The nodepool snapshot name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--tags` — The tags to set to the snapshot.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Update tags on a nodepool snapshot.*
```azurecli
az aks nodepool snapshot update -g MyResourceGroup -n snapshot1 --tags "foo=bar" "key1=val1"
```

*Clear tags on a nodepool snapshot.*
```azurecli
az aks nodepool snapshot update -g MyResourceGroup -n snapshot1 --tags ""
```

## az aks nodepool snapshot wait

Wait for a nodepool snapshot to reach a desired state.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

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

*Wait for a node pool to reach a desired state, polling every minute for up to thirty minutes.*
```azurecli
az aks nodepool snapshot wait --created --interval 60 --name MySnapshot --resource-group MyResourceGroup --timeout 1800
```
