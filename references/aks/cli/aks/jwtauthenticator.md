# az aks jwtauthenticator

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/jwtauthenticator  
> Microsoft doc last updated: unknown

Commands to manage JWT authenticators in Azure Kubernetes Service.

Subgroups and commands: `az_aks_jwtauthenticator_add`, `az_aks_jwtauthenticator_delete`, `az_aks_jwtauthenticator_list`, `az_aks_jwtauthenticator_show`, `az_aks_jwtauthenticator_update`

## az aks jwtauthenticator add  (extension: aks-preview etc.)

Add a JWT authenticator to a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--config-file` — Path to JSON file containing the JWT authenticator configuration.
- `--name -n` — Name of the JWT authenticator (must be unique within the cluster).
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Add a JWT authenticator from a configuration file*
```azurecli
az aks jwtauthenticator add -g MyResourceGroup --cluster-name MyCluster --name myjwt --config-file config.json
```

## az aks jwtauthenticator delete  (extension: aks-preview etc.)

Delete a JWT authenticator from a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the JWT authenticator to delete.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a JWT authenticator*
```azurecli
az aks jwtauthenticator delete -g MyResourceGroup --cluster-name MyCluster --name myjwt
```

## az aks jwtauthenticator list  (extension: aks-preview etc.)

List all JWT authenticators in a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.

*List all JWT authenticators in a cluster*
```azurecli
az aks jwtauthenticator list -g MyResourceGroup --cluster-name MyCluster
```

## az aks jwtauthenticator show  (extension: aks-preview etc.)

Show details of a JWT authenticator in a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the JWT authenticator to show.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.

*Show a specific JWT authenticator configuration*
```azurecli
az aks jwtauthenticator show -g MyResourceGroup --cluster-name MyCluster --name myjwt
```

## az aks jwtauthenticator update  (extension: aks-preview etc.)

Update a JWT authenticator in a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--config-file` — Path to JSON file containing the updated JWT authenticator configuration.
- `--name -n` — Name of the JWT authenticator to update.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Update a JWT authenticator configuration*
```azurecli
az aks jwtauthenticator update -g MyResourceGroup --cluster-name MyCluster --name myjwt --config-file updated-config.json
```
