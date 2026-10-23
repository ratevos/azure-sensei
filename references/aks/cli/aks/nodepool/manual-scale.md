# az aks nodepool manual-scale

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool/manual-scale  
> Microsoft doc last updated: unknown

Commands to manage nodepool virtualMachinesProfile.scale.manual.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_nodepool_manual-scale_add`, `az_aks_nodepool_manual-scale_add(aks-preview)`, `az_aks_nodepool_manual-scale_delete`, `az_aks_nodepool_manual-scale_delete(aks-preview)`, `az_aks_nodepool_manual-scale_update`, `az_aks_nodepool_manual-scale_update(aks-preview)`

## az aks nodepool manual-scale add

Add a new manual to a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--node-count -c` — Number of nodes in the manual.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--vm-sizes` — Comma-separated list of sizes in the manual.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az aks nodepool manual-scale add  (extension: aks-preview etc.)

Add a new manual to a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--node-count -c` — Number of nodes in the manual.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--vm-sizes` — Comma-separated list of sizes in the manual.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--use-patch-api` — Manage the manual scale profiles using the preview PATCH agent pool API instead of the default PUT API. Default: False.

## az aks nodepool manual-scale delete

Delete an existing manual to a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--current-vm-sizes` — Comma-separated list of sizes in the manual to be deleted.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks nodepool manual-scale delete  (extension: aks-preview etc.)

Delete an existing manual to a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--current-vm-sizes` — Comma-separated list of sizes in the manual to be deleted.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--use-patch-api` — Manage the manual scale profiles using the preview PATCH agent pool API instead of the default PUT API. Default: False.

## az aks nodepool manual-scale update

Update an existing manual of a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--current-vm-sizes` — Comma-separated list of sizes in the manual to be updated.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes in the manual.
- `--vm-sizes` — Comma-separated list of new sizes.

## az aks nodepool manual-scale update  (extension: aks-preview etc.)

Update an existing manual of a VirtualMachines agentpool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--current-vm-sizes` — Comma-separated list of sizes in the manual to be updated.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes in the manual.
- `--use-patch-api` — Manage the manual scale profiles using the preview PATCH agent pool API instead of the default PUT API. Default: False.
- `--vm-sizes` — Comma-separated list of new sizes.
