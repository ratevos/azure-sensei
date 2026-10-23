# az aks extension

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/extension  
> Microsoft doc last updated: unknown

Commands to manage extensions in the Kubernetes cluster.

Subgroups and commands: `az_aks_extension_create`, `az_aks_extension_delete`, `az_aks_extension_list`, `az_aks_extension_show`, `az_aks_extension_type`, `az_aks_extension_type_list`, `az_aks_extension_type_show`, `az_aks_extension_type_version`, `az_aks_extension_type_version_list`, `az_aks_extension_type_version_show`, `az_aks_extension_update`

## az aks extension create  (extension: aks-preview etc.)

Creates the Cluster extension instance on the managed cluster. Please refer to the example at the end to see how to create a cluster extension.

**Required parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--extension-type -t` — Name of the extension type.
- `--name -n` — Name of the extension instance.
- `--resource-group -g` — Name of the resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config --configuration-settings` — Configuration Settings as key=value pair.
- `--config-file --config-settings-file` — JSON file path for configuration-settings.
- `--config-protected --config-protected-settings` — Configuration Protected Settings as key=value pair.
- `--config-protected-file --config-protected-settings-file` — JSON file path for configuration-protected-settings.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--release-namespace` — Specify the namespace to install the extension release.
- `--scope` — Specify scope of the extension type, takes in namespace or cluster as the scope.
- `--target-namespace` — Specify the target namespace to install to for the extension instance. This parameter is required if extension scope is set to 'namespace'.

*Install Cluster extension on AKS cluster with required parameters*
```azurecli
az aks extension create --resource-group my-resource-group --cluster-name mycluster --name myextension --extension-type microsoft.flux
```

*Install Cluster extension with optional parameter configuration settings*
```azurecli
az aks extension create --resource-group abc --cluster-name test --name flux --extension-type microsoft.flux --config useKubeletIdentity=true
```

## az aks extension delete  (extension: aks-preview etc.)

Delete a Cluster Extension.

**Required parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--name -n` — Name of the extension instance.
- `--resource-group -g` — Name of the resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--force` — Specify whether to force delete the extension from the cluster. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Ignores confirmation prompt. Default: False.

*Delete an existing Cluster extension on AKS cluster*
```azurecli
az aks extension delete --resource-group resource-group --cluster-name cluster --name ext
```

*Delete an existing Cluster extension on AKS cluster with optional parameters*
```azurecli
az aks extension delete --resource-group resource-group --cluster-name cluster --name ext --yes --force
```

## az aks extension list  (extension: aks-preview etc.)

List Cluster Extensions.

**Required parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--resource-group -g` — Name of the resource group.

*List all Cluster Extensions on a cluster*
```azurecli
az aks extension list --resource-group <group> --cluster-name <name>
```

## az aks extension show  (extension: aks-preview etc.)

Show a Cluster Extension.

**Required parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--name -n` — Name of the extension instance.
- `--resource-group -g` — Name of the resource group.

*Show details of a Cluster Extension*
```azurecli
az aks extension show --resource-group my-resource-group --cluster-name mycluster --name myextension
```

## az aks extension update  (extension: aks-preview etc.)

Update mutable properties of a Cluster Extension.

**Required parameters**

- `--cluster-name -c` — Name of the AKS cluster.
- `--name -n` — Name of the extension instance.
- `--resource-group -g` — Name of the resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config --configuration-settings` — Configuration Settings as key=value pair.
- `--config-file --config-settings-file` — JSON file path for configuration-settings.
- `--config-protected --config-protected-settings` — Configuration Protected Settings as key=value pair.
- `--config-protected-file --config-protected-settings-file` — JSON file path for configuration-protected-settings.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Ignores confirmation prompt. Default: False.

*Update Cluster extension on AKS cluster*
```azurecli
az aks extension update --resource-group my-resource-group --cluster-name mycluster --name myextension
```

*Update Cluster extension on AKS cluster with optional parameters included*
```azurecli
az aks extension update --resource-group my-resource-group --cluster-name mycluster --name myextension --configuration-settings settings-key=settings-value --config-protected-settings protected-settings-key=protected-value --config-settings-file=config-settings-file --config-protected-file=protected-settings-file
```
