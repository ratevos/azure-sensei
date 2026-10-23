# az aks nodepool auto-scale

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool/auto-scale  
> Microsoft doc last updated: unknown

Commands to manage nodepool virtualMachinesProfile.scale.autoscale.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_nodepool_auto-scale_add`, `az_aks_nodepool_auto-scale_add(aks-preview)`, `az_aks_nodepool_auto-scale_delete`, `az_aks_nodepool_auto-scale_delete(aks-preview)`, `az_aks_nodepool_auto-scale_update`, `az_aks_nodepool_auto-scale_update(aks-preview)`

## az aks nodepool auto-scale add

Add a new autoscale profile to a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--max-count` — Maximum number of nodes for autoscaling.
- `--min-count` — Minimum number of nodes for autoscaling.
- `--name --nodepool-name -n` — The node pool name.
- `--node-vm-size` — VM size for the autoscale profile.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Add an autoscale profile to a VirtualMachines agentpool*
```azurecli
az aks nodepool auto-scale add -g MyResourceGroup --cluster-name MyMC --name MyNodePool --node-vm-size Standard_D2s_v3 --min-count 3 --max-count 5
```

## az aks nodepool auto-scale add  (extension: aks-preview etc.)

Add a new autoscale profile to a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--max-count` — Maximum number of nodes for autoscaling.
- `--min-count` — Minimum number of nodes for autoscaling.
- `--name --nodepool-name -n` — The node pool name.
- `--node-vm-size` — VM size for the autoscale profile.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Add an autoscale profile to a VirtualMachines agentpool*
```azurecli
az aks nodepool auto-scale add -g MyResourceGroup --cluster-name MyMC --name MyNodePool --node-vm-size Standard_D2s_v3 --min-count 3 --max-count 5
```

## az aks nodepool auto-scale delete

Delete an existing autoscale profile from a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--current-node-vm-size` — The VM size of the autoscale profile to be deleted.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete an autoscale profile from a VirtualMachines agentpool*
```azurecli
az aks nodepool auto-scale delete -g MyResourceGroup --cluster-name MyMC --name MyNodePool --current-node-vm-size Standard_D2s_v3
```

## az aks nodepool auto-scale delete  (extension: aks-preview etc.)

Delete an existing autoscale profile from a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--current-node-vm-size` — The VM size of the autoscale profile to be deleted.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Delete an autoscale profile from a VirtualMachines agentpool*
```azurecli
az aks nodepool auto-scale delete -g MyResourceGroup --cluster-name MyMC --name MyNodePool --current-node-vm-size Standard_D2s_v3
```

## az aks nodepool auto-scale update

Update an existing autoscale profile of a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--current-node-vm-size` — The current VM size of the autoscale profile to be updated.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--max-count` — Maximum number of nodes for autoscaling.
- `--min-count` — Minimum number of nodes for autoscaling.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-vm-size` — The new VM size for the autoscale profile.

*Update an existing autoscale profile in a VirtualMachines agentpool*
```azurecli
az aks nodepool auto-scale update -g MyResourceGroup --cluster-name MyMC --name MyNodePool --current-node-vm-size Standard_D2s_v3 --node-vm-size Standard_D8s_v3 --min-count 2 --max-count 4
```

## az aks nodepool auto-scale update  (extension: aks-preview etc.)

Update an existing autoscale profile of a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--current-node-vm-size` — The current VM size of the autoscale profile to be updated.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--max-count` — Maximum number of nodes for autoscaling.
- `--min-count` — Minimum number of nodes for autoscaling.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-vm-size` — The new VM size for the autoscale profile.

*Update an existing autoscale profile in a VirtualMachines agentpool*
```azurecli
az aks nodepool auto-scale update -g MyResourceGroup --cluster-name MyMC --name MyNodePool --current-node-vm-size Standard_D2s_v3 --node-vm-size Standard_D8s_v3 --min-count 2 --max-count 4
```
