# az aks approuting defaultdomain

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/approuting/defaultdomain  
> Microsoft doc last updated: unknown

Commands to manage App Routing Default Domain.

Subgroups and commands: `az_aks_approuting_defaultdomain_show`

## az aks approuting defaultdomain show  (extension: aks-preview etc.)

Show the Default Domain configuration for App Routing.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Show the default domain for a cluster.*
```azurecli
az aks approuting defaultdomain show --resource-group MyResourceGroup --name MyManagedCluster
```
