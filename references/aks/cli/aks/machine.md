# az aks machine

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/machine  
> Microsoft doc last updated: unknown

Get information about machines in a nodepool of a managed clusters.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_machine_add`, `az_aks_machine_list`, `az_aks_machine_list(aks-preview)`, `az_aks_machine_show`, `az_aks_machine_show(aks-preview)`, `az_aks_machine_update`

## az aks machine add  (extension: aks-preview etc.)

Add a machine to the specified node pool.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--nodepool-name` — Name of the agentpool of a managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--capacity-reservation-group --crg` — The fully qualified resource ID of the Capacity Reservation Group to associate with the machine.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disable-fips-image` — Switch to use non-FIPS-enabled OS on the machine. Default: False.
- `--enable-fips-image` — Switch to use FIPS-enabled OS on the machine. Default: False.
- `--enable-node-public-ip` — Enable the machine public IP. Default: False.
- `--enable-ultra-ssd` — Whether to enable UltraSSD. Default: False.
- `--eviction-policy` — The eviction policy for machine. This cannot be specified unless the priority is 'Spot'. If not specified, the default is 'Delete'.
- `--kubernetes-version` — Version of Kubernetes to use for creating the machine, such as "1.7.12" or "1.8.7".
- `--labels` — Node labels for a FlexNode machine.
- `--machine-name` — Host name of the machine.
- `--max-pods -m` — Maximum pods for a FlexNode machine.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-public-ip-prefix-id` — Public IP prefix ID used to assign public IPs to the machine.
- `--node-public-ip-tags` — The ipTags of the machine public IPs.
- `--node-taints` — Node taints for a FlexNode machine.
- `--os-sku` — The os-sku of the agent node pool.
- `--os-type` — The operating system type of the machine.
- `--pod-subnet-id` — The ID of a subnet in an existing VNet into which to assign pods in the machine (requires azure network-plugin).
- `--priority` — The priority of the machine.
- `--spot-max-price` — The max price (in US Dollars) you are willing to pay for spot instances. Default: nan.
- `--tags` — The tags of the machine.
- `--vm-size` — The size of the machine.
- `--vnet-subnet-id` — The ID of a subnet in an existing VNet into which to deploy the machine.
- `--zones -z` — Space-separated list of availability zones where a machine will be placed.

## az aks machine list

Get information about IP Addresses, Hostname for all machines in an agentpool.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--nodepool-name` — Name of the agentpool of a managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Get information about IP Addresses, Hostname, Availability Zones for all machines in an agentpool*
```azurecli
az aks machine list  --resource-group <rg> --cluster-name <clusterName> --nodepool-name <apName>
```

## az aks machine list  (extension: aks-preview etc.)

List the details for all machines in an agentpool.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--nodepool-name` — Name of the agentpool of a managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*List the details for all machines in an agentpool*
```azurecli
az aks machine list --resource-group <resourceGroupName> --cluster-name <clusterName> --nodepool-name <apName>
```

## az aks machine show

Show IP Addresses, Hostname for a specific machine in an agentpool for a managedcluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--machine-name` — Name of the machine in the agentpool of a managed cluster.
- `--nodepool-name` — Name of the agentpool of a managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks machine show  (extension: aks-preview etc.)

Show the details of a specific machine in an agentpool of a managedcluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--machine-name` — Name of the machine.
- `--nodepool-name` — Name of the agentpool of a managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Show the details of a specific machine in an agentpool of a managedcluster.*
```azurecli
az aks machine show --resource-group <resourceGroupName> --cluster-name <clusterName> --nodepool-name <apName> --machine-name <machineName>
```

## az aks machine update  (extension: aks-preview etc.)

Update the specified machine in an agentpool.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--nodepool-name` — Name of the agentpool of a managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--kubernetes-version` — Kubernetes version for a FlexNode machine. This option is not supported for regular machines.
- `--labels` — The labels of the machine.
- `--machine-name` — Host name of the machine.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-taints` — The taints of the machine.
- `--tags` — The tags of the machine.
