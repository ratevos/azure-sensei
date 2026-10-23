# az aks check-network

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/check-network  
> Microsoft doc last updated: unknown

Commands to troubleshoot network connectivity in managed Kubernetes cluster.

Subgroups and commands: `az_aks_check-network_outbound`

## az aks check-network outbound  (extension: aks-preview etc.)

Perform outbound network connectivity check for a node in a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of the resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--custom-endpoints` — Additional endpoint(s) to perform the connectivity check, separated by comma.
- `--node-name` — Name of the node to perform the connectivity check. If not specified, a random node will be chosen.
