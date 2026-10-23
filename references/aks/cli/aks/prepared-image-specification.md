# az aks prepared-image-specification

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/prepared-image-specification  
> Microsoft doc last updated: unknown

Commands to manage prepared image specifications.

Subgroups and commands: `az_aks_prepared-image-specification_create`, `az_aks_prepared-image-specification_delete`, `az_aks_prepared-image-specification_list`, `az_aks_prepared-image-specification_show`, `az_aks_prepared-image-specification_update`, `az_aks_prepared-image-specification_version`, `az_aks_prepared-image-specification_version_delete`, `az_aks_prepared-image-specification_version_list`, `az_aks_prepared-image-specification_version_show`

## az aks prepared-image-specification create  (extension: aks-preview etc.)

Create a new prepared image specification.

**Required parameters**

- `--name -n` — The prepared image specification name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--version` — The prepared image specification version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--assign-identity` — Specify an existing user assigned identity.
- `--change-reference` — The related change reference ID for this resource operation.
- `--container-images` — Container images.
- `--customization-scripts` — Customization scripts. Expected value: json-string/@json-file.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.

*Create a new prepared image specification specifying a container image.*
```azurecli
az aks prepared-image-specification create -g MyResourceGroup -n MyPIS --version MyVersion --container-images myacr.azurecr.io/myimage:latest
```

*Create a new prepared image specification specifying a customization script.*
```azurecli
az aks prepared-image-specification create -g MyResourceGroup -n MyPIS --version MyVersion --customization-scripts '[{"name":"myscript","script":"/bin/true","scriptType":"Bash","executionPoint":"NodeImageBuildTime"}]'
```

*Create a new prepared image specification specifying a managed identity.*
```azurecli
az aks prepared-image-specification create -g MyResourceGroup -n MyPIS --version MyVersion --assign-identity /subscriptions/MySubscription/resourceGroups/AnotherResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/MyIdentity
```

*Create a new prepared image specification specifying tags.*
```azurecli
az aks prepared-image-specification create -g MyResourceGroup -n MyPIS --version MyVersion --tags k1=v1 k2=v2
```

## az aks prepared-image-specification delete  (extension: aks-preview etc.)

Delete a prepared image specification.

**Required parameters**

- `--name -n` — The prepared image specification name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks prepared-image-specification list  (extension: aks-preview etc.)

List prepared image specifications.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks prepared-image-specification show  (extension: aks-preview etc.)

Show a prepared image specification.

**Required parameters**

- `--name -n` — The prepared image specification name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks prepared-image-specification update  (extension: aks-preview etc.)

Update a prepared image specification.

**Required parameters**

- `--name -n` — The prepared image specification name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
