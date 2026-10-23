# az aks prepared-image-specification version

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/prepared-image-specification/version  
> Microsoft doc last updated: unknown

Commands to manage prepared image specification versions.

Subgroups and commands: `az_aks_prepared-image-specification_version_delete`, `az_aks_prepared-image-specification_version_list`, `az_aks_prepared-image-specification_version_show`

## az aks prepared-image-specification version delete  (extension: aks-preview etc.)

Delete a prepared image specification version.

**Required parameters**

- `--name -n` — The version name.
- `--pis-name` — The prepared image specification name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks prepared-image-specification version list  (extension: aks-preview etc.)

List prepared image specification versions.

**Required parameters**

- `--pis-name` — The prepared image specification name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks prepared-image-specification version show  (extension: aks-preview etc.)

Show a prepared image specification version.

**Required parameters**

- `--name -n` — The version name.
- `--pis-name` — The prepared image specification name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
