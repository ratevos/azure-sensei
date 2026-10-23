# az aks applicationloadbalancer

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/applicationloadbalancer  
> Microsoft doc last updated: unknown

Commands to manage Application Load Balancer (Application Gateway for Containers) addon.

Subgroups and commands: `az_aks_applicationloadbalancer_disable`, `az_aks_applicationloadbalancer_enable`, `az_aks_applicationloadbalancer_update`

## az aks applicationloadbalancer disable  (extension: aks-preview etc.)

Disable Application Load Balancer (Application Gateway for Containers) addon.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks applicationloadbalancer enable  (extension: aks-preview etc.)

Enable Application Load Balancer (Application Gateway for Containers) addon.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks applicationloadbalancer update  (extension: aks-preview etc.)

Update Application Load Balancer (Application Gateway for Containers) addon.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
