# az aks operation

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/operation  
> Microsoft doc last updated: unknown

Commands to manage and view operations on managed Kubernetes cluster.

Subgroups and commands: `az_aks_operation_list`, `az_aks_operation_show`, `az_aks_operation_show-latest`

## az aks operation list  (extension: aks-preview etc.)

List operations on a managed Kubernetes cluster or one of its node pools.

**Required parameters**

- `--name -n` — The name of the managed cluster.
- `--resource-group -g` — Name of the resource group.

**Optional parameters**

- `--active-only` — Only list operations that are currently active (not terminal). Default: False.
- `--nodepool-name` — The name of the nodepool. When specified, operations are listed for the node pool instead of the cluster.

*List historical operations on a managed cluster.*
```azurecli
az aks operation list -g myResourceGroup -n myAKSCluster
```

*List active operations on a managed cluster.*
```azurecli
az aks operation list -g myResourceGroup -n myAKSCluster --active-only
```

*List historical operations on a node pool.*
```azurecli
az aks operation list -g myResourceGroup -n myAKSCluster --nodepool-name nodepool1
```

*List active operations on a node pool.*
```azurecli
az aks operation list -g myResourceGroup -n myAKSCluster --nodepool-name nodepool1 --active-only
```

## az aks operation show  (extension: aks-preview etc.)

Show the details for a specific operation on managed Kubernetes cluster.

**Required parameters**

- `--name -n` — The name of the managed cluster.
- `--operation-id` — The ID of the operation.
- `--resource-group -g` — Name of the resource group.

**Optional parameters**

- `--nodepool-name` — The name of the nodepool.

## az aks operation show-latest  (extension: aks-preview etc.)

Show the details for the latest operation on managed Kubernetes cluster.

**Required parameters**

- `--name -n` — The name of the managed cluster.
- `--resource-group -g` — Name of the resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--nodepool-name` — The name of the nodepool.
