# az aks extension type version

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/extension/type/version  
> Microsoft doc last updated: unknown

Manage extension types version in Azure Kubernetes Service.

Subgroups and commands: `az_aks_extension_type_version_list`, `az_aks_extension_type_version_show`

## az aks extension type version list  (extension: aks-preview etc.)

List available Cluster Extension Type versions. The properties used for filtering include kubernetes version, location of the cluster.

**Required parameters**

- `--extension-type -t` — Name of the extension type.

**Optional parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--location -l` — Location of where we want to retrieve the extension type.
- `--major-version` — Filter results by only the major version of an extension type.For example if 1 is specified, all versions with major version 1 (1.1, 1.1.2) will be shown.The default value is None.
- `--release-train` — Specify the release train for the extension type.
- `--resource-group -g` — Name of the resource group.
- `--show-latest` — Filter results by only the latest version.For example, if this flag is used the latest version of the extensionType will be shown. Default: False.

*List available Cluster Extension Types for an existing cluster*
```azurecli
az aks extension type version list --resource-group my-resource-group --cluster-name mycluster --extension-type <type>
```

*List available Cluster Extension Types in a region*
```azurecli
az aks extension type version list --location eastus --extension-type <type>
```

## az aks extension type version show  (extension: aks-preview etc.)

Show properties associated with a Cluster Extension Type version. The properties used for filtering include kubernetes version, location of the cluster.

**Required parameters**

- `--extension-type -t` — Name of the extension type.
- `--version` — Specify the extension version to show to the user.

**Optional parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--location -l` — Location of where we want to retrieve the extension type.
- `--resource-group -g` — Name of the resource group.

*Show properties for a Cluster Extension Type version for an existing cluster*
```azurecli
az aks extension type version show --resource-group my-resource-group --cluster-name mycluster --extension-type type --version 1.0.0
```

*Show properties for a Cluster Extension Type version for a location*
```azurecli
az aks extension type version show --location eastus --extension-type <type> --version 1.0.0
```
