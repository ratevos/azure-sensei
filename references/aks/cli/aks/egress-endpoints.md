# az aks egress-endpoints

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/egress-endpoints  
> Microsoft doc last updated: unknown

Commands to manage egress endpoints in managed Kubernetes cluster.

Subgroups and commands: `az_aks_egress-endpoints_list`

## az aks egress-endpoints list  (extension: aks-preview etc.)

List egress endpoints that are required or recommended to be whitelisted for a cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
