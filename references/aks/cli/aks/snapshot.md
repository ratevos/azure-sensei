# az aks snapshot

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/snapshot  
> Microsoft doc last updated: unknown

Commands to manage nodepool snapshots.

Subgroups and commands: `az_aks_snapshot_create`, `az_aks_snapshot_delete`, `az_aks_snapshot_list`, `az_aks_snapshot_show`

## az aks snapshot create  (extension: aks-preview etc.)

Create a snapshot of a cluster.

**Required parameters**

- `--cluster-id` — The source cluster id from which to create this snapshot.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — The tags of the snapshot.

*Create a cluster snapshot.*
```azurecli
az aks snapshot create -g MyResourceGroup -n snapshot1 --cluster-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedClusters/akscluster1"
```

*Create a cluster snapshot with custom tags.*
```azurecli
az aks snapshot create -g MyResourceGroup -n snapshot1 --cluster-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedClusters/akscluster1" --tags "foo=bar" "key1=val1"
```

## az aks snapshot delete  (extension: aks-preview etc.)

Delete a cluster snapshot.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks snapshot list  (extension: aks-preview etc.)

List cluster snapshots.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks snapshot show  (extension: aks-preview etc.)

Show the details of a cluster snapshot.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
