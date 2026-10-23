# az aks namespace

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/namespace  
> Microsoft doc last updated: unknown

Commands to manage namespace in managed Kubernetes cluster.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_namespace_add`, `az_aks_namespace_add(aks-preview)`, `az_aks_namespace_delete`, `az_aks_namespace_delete(aks-preview)`, `az_aks_namespace_get-credentials`, `az_aks_namespace_get-credentials(aks-preview)`, `az_aks_namespace_list`, `az_aks_namespace_list(aks-preview)`, `az_aks_namespace_show`, `az_aks_namespace_show(aks-preview)`, `az_aks_namespace_update`, `az_aks_namespace_update(aks-preview)`

## az aks namespace add

Add namespace to the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--cpu-limit` — CPU limit of the namespace.
- `--cpu-request` — CPU request of the namespace.
- `--memory-limit` — Memory limit of the namespace.
- `--memory-request` — Memory request of the namespace.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--adoption-policy` — Action if Kubernetes namespace with same name already exists. The default value is Never.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--annotations` — Annotations for the managed namespace.
- `--change-reference` — The related change reference ID for this resource operation.
- `--delete-policy` — Delete options of a namespace. The default value is Keep.
- `--egress-policy` — Egress policy for the network. The default value is AllowAll.
- `--ingress-policy` — Ingress policy for the network. The default value is AllowSameNamespace.
- `--labels` — Labels for the managed namespace.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — The tags of the managed namespace.

*Create a namespace in an existing AKS cluster.*
```azurecli
az aks namespace add -g MyResourceGroup --cluster-name MyClusterName --name NamespaceName --cpu-request 500m --cpu-limit 800m --memory-request 1Gi --memory-limit 2Gi
```

*Create a namespace in an existing AKS cluster with labels, annotations and tags*
```azurecli
az aks namespace add -g MyResourceGroup --cluster-name MyClusterName --name NamespaceName --labels a=b p=q --annotations a=b p=q --tags a=b p=q --cpu-request 500m --cpu-limit 800m --memory-request 1Gi --memory-limit 2Gi
```

## az aks namespace add  (extension: aks-preview etc.)

Add namespace to the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--cpu-limit` — CPU limit of the namespace.
- `--cpu-request` — CPU request of the namespace.
- `--memory-limit` — Memory limit of the namespace.
- `--memory-request` — Memory request of the namespace.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--adoption-policy` — Action if Kubernetes namespace with same name already exists. The default value is Never.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--annotations` — Annotations for the managed namespace.
- `--change-reference` — The related change reference ID for this resource operation.
- `--delete-policy` — Delete options of a namespace. The default value is Keep.
- `--egress-policy` — Egress policy for the network. The default value is AllowAll.
- `--ingress-policy` — Ingress policy for the network. The default value is AllowSameNamespace.
- `--labels` — Labels for the managed namespace.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — The tags of the managed namespace.

*Create a namespace in an existing AKS cluster.*
```azurecli
az aks namespace add -g MyResourceGroup --cluster-name MyClusterName --name NamespaceName --cpu-request 500m --cpu-limit 800m --memory-request 1Gi --memory-limit 2Gi
```

*Create a namespace in an existing AKS cluster with labels, annotations and tags*
```azurecli
az aks namespace add -g MyResourceGroup --cluster-name MyClusterName --name NamespaceName --labels a=b p=q --annotations a=b p=q --tags a=b p=q --cpu-request 500m --cpu-limit 800m --memory-request 1Gi --memory-limit 2Gi
```

## az aks namespace delete

Delete a managed namespace in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az aks namespace delete  (extension: aks-preview etc.)

Delete a managed namespace in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az aks namespace get-credentials

Get access credentials for a managed namespace.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--context` — If specified, overwrite the default context name.
- `--file -f` — Kubernetes configuration file to update. Use "-" to print YAML to stdout instead. Default: ~\.kube\config.
- `--overwrite-existing` — Overwrite any existing cluster entry with the same name. Default: False.

*Get access credentials for a managed namespace. (autogenerated)*
```azurecli
az aks namespace get-credentials --resource-group MyResourceGroup --cluster-name MyManagedCluster --name ManagedNamespaceName
```

## az aks namespace get-credentials  (extension: aks-preview etc.)

Get access credentials for a managed namespace.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--context` — If specified, overwrite the default context name.
- `--file -f` — Kubernetes configuration file to update. Use "-" to print YAML to stdout instead. Default: ~\.kube\config.
- `--overwrite-existing` — Overwrite any existing cluster entry with the same name. Default: False.

*Get access credentials for a managed namespace. (autogenerated)*
```azurecli
az aks namespace get-credentials --resource-group MyResourceGroup --cluster-name MyManagedCluster --name ManagedNamespaceName
```

## az aks namespace list

List managed namespaces in managed Kubernetes cluster.

**Optional parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks namespace list  (extension: aks-preview etc.)

List managed namespaces in managed Kubernetes cluster.

**Optional parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks namespace show

Show the details of a managed namespace in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks namespace show  (extension: aks-preview etc.)

Show the details of a managed namespace in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks namespace update

Update namespace on the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--adoption-policy` — Action if Kubernetes namespace with same name already exists.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--annotations` — Annotations for the managed namespace.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cpu-limit` — CPU limit of the namespace.
- `--cpu-request` — CPU request of the namespace.
- `--delete-policy` — Delete options of a namespace.
- `--egress-policy` — Egress policy rule for the network.
- `--ingress-policy` — Ingress policy rule for the network.
- `--labels` — Labels for the managed namespace.
- `--memory-limit` — Memory limit of the namespace.
- `--memory-request` — Memory request of the namespace.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — The tags of the managed namespace.

*update namespace in an existing AKS cluster.*
```azurecli
az aks namespace update -g MyResourceGroup --cluster-name MyClusterName --name NamespaceName --labels a=b p=q --annotations a=b p=q --tags a=b p=q --cpu-request 600m --cpu-limit 800m --memory-request 2Gi --memory-limit 3Gi --adoption-policy Always
```

## az aks namespace update  (extension: aks-preview etc.)

Update namespace on the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — The managed namespace name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--adoption-policy` — Action if Kubernetes namespace with same name already exists.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--annotations` — Annotations for the managed namespace.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cpu-limit` — CPU limit of the namespace.
- `--cpu-request` — CPU request of the namespace.
- `--delete-policy` — Delete options of a namespace.
- `--egress-policy` — Egress policy rule for the network.
- `--ingress-policy` — Ingress policy rule for the network.
- `--labels` — Labels for the managed namespace.
- `--memory-limit` — Memory limit of the namespace.
- `--memory-request` — Memory request of the namespace.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — The tags of the managed namespace.

*update namespace in an existing AKS cluster.*
```azurecli
az aks namespace update -g MyResourceGroup --cluster-name MyClusterName --name NamespaceName --labels a=b p=q --annotations a=b p=q --tags a=b p=q --cpu-request 600m --cpu-limit 800m --memory-request 2Gi --memory-limit 3Gi --adoption-policy Always
```
