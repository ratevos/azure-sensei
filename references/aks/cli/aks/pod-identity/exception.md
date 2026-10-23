# az aks pod-identity exception

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/pod-identity/exception  
> Microsoft doc last updated: unknown

Commands to manage pod identity exceptions in managed Kubernetes cluster.

Subgroups and commands: `az_aks_pod-identity_exception_add`, `az_aks_pod-identity_exception_delete`, `az_aks_pod-identity_exception_list`, `az_aks_pod-identity_exception_update`

## az aks pod-identity exception add  (extension: aks-preview etc.)

Add a pod identity exception to a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--namespace` — The pod identity exception namespace.
- `--pod-labels` — Space-separated labels: key=value [key=value ...].
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--name -n` — The pod identity exception name. Generate if not specified.

## az aks pod-identity exception delete  (extension: aks-preview etc.)

Remove a pod identity exception from a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The pod identity exception name to remove.
- `--namespace` — The pod identity exception namespace to remove.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks pod-identity exception list  (extension: aks-preview etc.)

List pod identity exceptions in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks pod-identity exception update  (extension: aks-preview etc.)

Update a pod identity exception in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The pod identity exception name to remove.
- `--namespace` — The pod identity exception namespace to remove.
- `--pod-labels` — Pod labels in key=value [key=value ...].
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
