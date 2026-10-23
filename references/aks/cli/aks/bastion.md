# az aks bastion

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/bastion  
> Microsoft doc last updated: unknown

Commands to manage or connect to Azure Bastion for a managed Kubernetes cluster.

Subgroups and commands: `az_aks_bastion_disable`, `az_aks_bastion_enable`, `az_aks_bastion_tunnel`, `az_aks_bastion_update`

## az aks bastion disable  (extension: aks-preview etc.)

Disable managed Azure Bastion host for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Disable managed Azure Bastion host for a managed Kubernetes cluster.*
```azurecli
az aks bastion disable --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks bastion enable  (extension: aks-preview etc.)

Enable managed Azure Bastion host for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--bastion-public-ip` — The resource ID of an existing public IP address to be assigned to the managed Azure Bastion host.
- `--bastion-scale-units` — The number of scale units for the managed Azure Bastion host.
- `--bastion-sku -s` — Specify the SKU of the managed Azure Bastion host.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Enable managed Azure Bastion host for a managed Kubernetes cluster with default settings.*
```azurecli
az aks bastion enable --name MyManagedCluster --resource-group MyResourceGroup
```

*Enable managed Azure Bastion host with premium sku and custom scale units.*
```azurecli
az aks bastion enable --name MyManagedCluster --resource-group MyResourceGroup --bastion-sku premium --bastion-scale-units 7
```

*Enable managed Azure Bastion host with BYO public IP address.*
```azurecli
az aks bastion enable --name MyManagedCluster --resource-group MyResourceGroup --bastion-public-ip /subscriptions/{subscription-id}/resourceGroups/MyResourceGroup/providers/Microsoft.Network/publicIPAddresses/MyPublicIP
```

## az aks bastion tunnel  (extension: aks-preview etc.)

Connect to a managed Kubernetes cluster using Azure Bastion.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--admin` — Use the cluster admin credentials to connect to the bastion. Default: False.
- `--bastion` — The name or resource ID of a pre-deployed Bastion resource configured to connect to the current AKS cluster.
- `--change-reference` — The related change reference ID for this resource operation.
- `--kubeconfig-path` — Path to an existing kubeconfig file to use.
- `--port` — The local port number used for the bastion connection.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Connect to a managed Kubernetes cluster using Azure Bastion with custom port and admin credentials.*
```azurecli
az aks bastion tunnel -g MyResourceGroup --name MyManagedCluster --bastion MyBastionResource --port 50001 --admin
```

*Connect using an existing kubeconfig file.*
```azurecli
az aks bastion tunnel -g MyResourceGroup --name MyManagedCluster --kubeconfig-path ~/.kube/config
```

## az aks bastion update  (extension: aks-preview etc.)

Update managed Azure Bastion host for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--bastion-scale-units` — The number of scale units for the managed Azure Bastion host.
- `--bastion-sku -s` — Specify the SKU of the managed Azure Bastion host.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Upgrade managed Azure Bastion host to Premium SKU.*
```azurecli
az aks bastion update --name MyManagedCluster --resource-group MyResourceGroup --bastion-sku premium
```

*Scale managed Azure Bastion host.*
```azurecli
az aks bastion update --name MyManagedCluster --resource-group MyResourceGroup --bastion-scale-units 7
```
