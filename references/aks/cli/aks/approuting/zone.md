# az aks approuting zone

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/approuting/zone  
> Microsoft doc last updated: unknown

Commands to manage App Routing DNS Zones.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_approuting_zone_add`, `az_aks_approuting_zone_add(aks-preview)`, `az_aks_approuting_zone_delete`, `az_aks_approuting_zone_delete(aks-preview)`, `az_aks_approuting_zone_list`, `az_aks_approuting_zone_list(aks-preview)`, `az_aks_approuting_zone_update`, `az_aks_approuting_zone_update(aks-preview)`

## az aks approuting zone add

Add DNS Zone(s) to App Routing.

**Required parameters**

- `--ids` — Comma-separated list of DNS zone resource IDs to add to App Routing.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--attach-zones` — Grant DNS zone Contributor permissions on all zone IDs specified in --ids. Default: False.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks approuting zone add  (extension: aks-preview etc.)

Add DNS Zone(s) to App Routing.

**Required parameters**

- `--ids` — Comma-separated list of DNS zone resource IDs to add to App Routing.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--attach-zones` — Grant DNS zone Contributor permissions on all zone IDs specified in --ids. Default: False.
- `--change-reference` — The related change reference ID for this resource operation.

*Add DNS zones to App Routing.*
```azurecli
az aks approuting zone add --resource-group MyResourceGroup --name MyManagedCluster --ids zoneResourceId
```

## az aks approuting zone delete

Delete DNS Zone(s) from App Routing.

**Required parameters**

- `--ids` — Comma-separated list of DNS zone resource IDs to delete from App Routing.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks approuting zone delete  (extension: aks-preview etc.)

Delete DNS Zone(s) from App Routing.

**Required parameters**

- `--ids` — Comma-separated list of DNS zone resource IDs to delete from App Routing.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks approuting zone list

List DNS Zone IDs in App Routing.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks approuting zone list  (extension: aks-preview etc.)

List DNS Zone IDs in App Routing.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks approuting zone update

Replace DNS Zone(s) in App Routing.

**Required parameters**

- `--ids` — Comma-separated list of DNS zone resource IDs to replace in App Routing.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--attach-zones` — Grant DNS zone Contributor permissions on all zone IDs specified in --ids. Default: False.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks approuting zone update  (extension: aks-preview etc.)

Replace DNS Zone(s) in App Routing.

**Required parameters**

- `--ids` — Comma-separated list of DNS zone resource IDs to replace in App Routing.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--attach-zones` — Grant DNS zone Contributor permissions on all zone IDs specified in --ids. Default: False.
- `--change-reference` — The related change reference ID for this resource operation.
