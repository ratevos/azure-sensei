# az aks identity-binding

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/identity-binding  
> Microsoft doc last updated: unknown

Commands to manage identity bindings in Azure Kubernetes Service.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_identity-binding_create`, `az_aks_identity-binding_create(aks-preview)`, `az_aks_identity-binding_delete`, `az_aks_identity-binding_delete(aks-preview)`, `az_aks_identity-binding_list`, `az_aks_identity-binding_list(aks-preview)`, `az_aks_identity-binding_show`, `az_aks_identity-binding_show(aks-preview)`, `az_aks_identity-binding_update`

## az aks identity-binding create

Create a new identity binding in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--managed-identity-resource-id` — The resource ID of the managed identity to use.
- `--name -n` — Name of the identity binding to create.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Create a new identity binding*
```azurecli
az aks identity-binding create -g myResourceGroup --cluster-name myCluster -n myIdentityBinding --managed-identity-resource-id /subscriptions/0000/resourceGroups/myResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity
```

## az aks identity-binding create  (extension: aks-preview etc.)

Create a new identity binding in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--managed-identity-resource-id` — The resource ID of the managed identity to use.
- `--name -n` — Name of the identity binding to create.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--allowed-subjects-from-file -f` — Path to a JSON file with the list of subjects authorized to use this identity binding for token exchange.
- `--change-reference` — The related change reference ID for this resource operation.

*Create an identity binding with allowed subjects targeting specific namespaces by name.*
```azurecli
az aks identity-binding create --resource-group myRG --cluster-name myCluster \
  --name my-identity-binding \
  --managed-identity-resource-id /subscriptions/.../userAssignedIdentities/myMI \
  --allowed-subjects-from-file allowed-subjects.json
```

## az aks identity-binding delete

Delete a specific identity binding in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--name -n` — Name of the identity binding to delete.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete an identity binding*
```azurecli
az aks identity-binding delete -g myResourceGroup --cluster-name myCluster -n myIdentityBinding
```

## az aks identity-binding delete  (extension: aks-preview etc.)

Delete a specific identity binding in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--name -n` — Name of the identity binding to delete.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks identity-binding list

List all identity bindings under a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*List all identity bindings in a managed cluster*
```azurecli
az aks identity-binding list -g myResourceGroup --cluster-name myCluster
```

## az aks identity-binding list  (extension: aks-preview etc.)

List all identity bindings under a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks identity-binding show

Show details of a specific identity binding in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--name -n` — Name of the identity binding to show.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Show details of an identity binding*
```azurecli
az aks identity-binding show -g myResourceGroup --cluster-name myCluster -n myIdentityBinding
```

## az aks identity-binding show  (extension: aks-preview etc.)

Show details of a specific identity binding in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--name -n` — Name of the identity binding to show.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks identity-binding update  (extension: aks-preview etc.)

Update an existing identity binding in a managed Kubernetes cluster.

**Required parameters**

- `--allowed-subjects-from-file -f` — Path to a JSON file with the list of subjects authorized to use this identity binding for token exchange.
- `--cluster-name` — Name of the managed Kubernetes cluster.
- `--name -n` — Name of the identity binding to update.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Update the allowed subjects on an existing identity binding.*
```azurecli
az aks identity-binding update --resource-group myRG --cluster-name myCluster \
  --name my-identity-binding \
  --allowed-subjects-from-file updated-subjects.json
```
