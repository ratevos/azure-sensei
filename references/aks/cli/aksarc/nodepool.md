# az aksarc nodepool

> Source: https://learn.microsoft.com/en-us/cli/azure/aksarc/nodepool  
> Microsoft doc last updated: unknown

Manage nodepools in a provisioned cluster.

Subgroups and commands: `az_aksarc_nodepool_add`, `az_aksarc_nodepool_delete`, `az_aksarc_nodepool_list`, `az_aksarc_nodepool_scale`, `az_aksarc_nodepool_show`, `az_aksarc_nodepool_update`

## az aksarc nodepool add  (extension: aks-preview etc.)

Adds a nodepool in the provisioned cluster.

**Required parameters**

- `--cluster-name` — Name of the provisioned cluster.
- `--name -n` — Name of the nodepool.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--enable-cluster-autoscaler -e` — Enable cluster auto-scaler for the provisioned cluster. Default: False.
- `--gpu-count-per-node` — Number of gpus attached to a node.
- `--labels` — Space-separated labels: key[=value] [key[=value] ...].
- `--max-count` — The maximum number of nodes for auto-scaling.
- `--max-pods -m` — Maximum number of pods that can run on a node.
- `--min-count` — The minimum number of nodes for auto-scaling.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes to be created in the nodepool.
- `--node-taints` — Comma-separated list of nodepool taints.
- `--node-vm-size` — VM Size of the nodes in the nodepool.
- `--os-sku` — OS Sku for the nodes in the nodepool. Options: "CBLMariner" | "Windows2019" | "Windows2022".
- `--os-type` — OS Type for the nodes in the nodepool. Options: "Linux" | "Windows".
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.

*AddNodepool*
```azurecli
az aksarc nodepool add --name "samplenodepool" --cluster-name "samplecluster" --resource-group "sample-rg"
```

## az aksarc nodepool delete  (extension: aks-preview etc.)

Deletes the nodepool in the provisioned cluster.

**Required parameters**

- `--cluster-name` — Name of the provisioned cluster.
- `--name -n` — Name of the nodepool.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*DeleteNodepool*
```azurecli
az aksarc nodepool delete --name "samplenodepool" --cluster-name "samplecluster" --resource-group "sample-rg"
```

## az aksarc nodepool list  (extension: aks-preview etc.)

Lists all the nodepools in the provisioned cluster.

**Required parameters**

- `--cluster-name` — Name of the provisioned cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*ListNodepool*
```azurecli
az aksarc nodepool list --cluster-name "samplecluster" --resource-group "sample-rg"
```

## az aksarc nodepool scale  (extension: aks-preview etc.)

Scales the nodepool in the provisioned cluster.

**Required parameters**

- `--cluster-name` — Name of the provisioned cluster.
- `--name -n` — Name of the nodepool.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--gpu-count-per-node` — Number of gpus attached to a node.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes to scale to in the nodepool.
- `--node-vm-size` — VM Size of the nodes in the nodepool.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*ScaleNodePoolCount*
```azurecli
az aksarc nodepool scale --name "samplenodepool" --cluster-name "samplecluster" --resource-group "sample-rg" --node-count 3
```

*ScaleNodePoolVMSize*
```azurecli
az aksarc nodepool scale --name "samplenodepool" --cluster-name "samplecluster" --resource-group "sample-rg" --node-vm-size "Standard_A2_v2"
```

## az aksarc nodepool show  (extension: aks-preview etc.)

Gets the nodepool in the provisioned cluster.

**Required parameters**

- `--cluster-name` — Name of the provisioned cluster.
- `--name -n` — Name of the nodepool.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*GetNodepool*
```azurecli
az aksarc nodepool show --name "samplenodepool" --cluster-name "samplecluster" --resource-group "sample-rg"
```

## az aksarc nodepool update  (extension: aks-preview etc.)

Update a nodepool in the provisioned cluster.

**Required parameters**

- `--cluster-name` — Name of the provisioned cluster.
- `--name -n` — Name of the nodepool.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disable-cluster-autoscaler -d` — Disable cluster auto-scaler for the provisioned cluster. Default: False.
- `--enable-cluster-autoscaler -e` — Enable cluster auto-scaler for the provisioned cluster. Default: False.
- `--labels` — Space-separated labels: key[=value] [key[=value] ...]. Pass an empty string to clear the labels.
- `--max-count` — The maximum number of nodes for auto-scaling.
- `--min-count` — The minimum number of nodes for auto-scaling.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-taints` — Comma-separated list of nodepool taints. Pass an empty string to clear the taints.
- `--update-cluster-autoscaler -u` — Update cluster auto-scaler for the provisioned cluster. Default: False.

*UpdateNodepool*
```azurecli
az aksarc nodepool update --name "samplenodepool" --cluster-name "samplecluster" --resource-group "sample-rg" --disable-cluster-autoscaler
```
