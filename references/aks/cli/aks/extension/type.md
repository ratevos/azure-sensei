# az aks extension type

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/extension/type  
> Microsoft doc last updated: unknown

Manage extension types in Azure Kubernetes Service.

Subgroups and commands: `az_aks_extension_type_list`, `az_aks_extension_type_show`, `az_aks_extension_type_version`, `az_aks_extension_type_version_list`, `az_aks_extension_type_version_show`

## az aks extension type list  (extension: aks-preview etc.)

List available Cluster Extension Types. The properties used for filtering include kubernetes version, location of the cluster.

**Optional parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--location -l` — Location of where we want to retrieve the extension type.
- `--release-train` — Specify the release train for the K8s extension type.
- `--resource-group -g` — Name of the resource group.

*List available Cluster Extension Types for an existing cluster*
```azurecli
az aks extension type list --resource-group my-resource-group --cluster-name mycluster
```

*List available Cluster Extension Types in a region*
```azurecli
az aks extension type list --location eastus
```

## az aks extension type show  (extension: aks-preview etc.)

Show properties for a Cluster Extension Type. The properties used for filtering include kubernetes version, location of the cluster.

**Required parameters**

- `--extension-type -t` — Name of the extension type.

**Optional parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--location -l` — Location of where we want to retrieve the extension type.
- `--resource-group -g` — Name of the resource group.

*Show properties for a Cluster Extension Type for an existing cluster by cluster*
```azurecli
az aks extension type show --resource-group my-resource-group --cluster-name mycluster --extension-type <type>
```

*Show properties for a Cluster Extension Type in a location*
```azurecli
az aks extension type show --location eastus --extension-type type
```
