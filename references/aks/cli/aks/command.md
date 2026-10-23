# az aks command

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/command  
> Microsoft doc last updated: unknown

See detail usage in 'az aks command invoke', 'az aks command result'.

Subgroups and commands: `az_aks_command_invoke`, `az_aks_command_result`

## az aks command invoke

Run a shell command (with kubectl, helm) on your aks cluster, support attaching files as well.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--command -c` — Command or shell script you want to run.
- `--file -f` — Files to be used by the command, use '.' to attach the current folder.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az aks command result

Fetch result from previously triggered 'aks command invoke'.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--command-id -i` — CommandId returned from 'aks command invoke'.
