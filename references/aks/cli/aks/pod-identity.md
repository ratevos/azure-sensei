# az aks pod-identity

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/pod-identity  
> Microsoft doc last updated: unknown

Commands to manage pod identities in managed Kubernetes cluster.

Subgroups and commands: `az_aks_pod-identity_add`, `az_aks_pod-identity_delete`, `az_aks_pod-identity_exception`, `az_aks_pod-identity_exception_add`, `az_aks_pod-identity_exception_delete`, `az_aks_pod-identity_exception_list`, `az_aks_pod-identity_exception_update`, `az_aks_pod-identity_list`

## az aks pod-identity add  (extension: aks-preview etc.)

Add a pod identity to a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--identity-resource-id` — Resource id of the identity to use.
- `--namespace` — The pod identity namespace.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--binding-selector` — Optional binding selector to use.
- `--change-reference` — The related change reference ID for this resource operation.
- `--name -n` — The pod identity name. Generate if not specified.

*Add pod identity*
```azurecli
az aks pod-identity add --cluster-name MyManagedCluster --resource-group MyResourceGroup --namespace my-namespace --name my-identity --identity-resource-id <my-identity-resource-id>
```

## az aks pod-identity delete  (extension: aks-preview etc.)

Remove a pod identity from a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The pod identity name.
- `--namespace` — The pod identity namespace.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks pod-identity list  (extension: aks-preview etc.)

List pod identities in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
