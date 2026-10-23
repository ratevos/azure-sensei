# az aks alert-config

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/alert-config  
> Microsoft doc last updated: unknown

Commands to manage AKS-managed alert configurations for a cluster.

Subgroups and commands: `az_aks_alert-config_add`, `az_aks_alert-config_delete`, `az_aks_alert-config_list`, `az_aks_alert-config_show`, `az_aks_alert-config_update`

## az aks alert-config add  (extension: aks-preview etc.)

Add an alert configuration to a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--mode` — How AKS manages alerts for the cluster.
- `--name -n` — Name of the alert configuration (must be unique within the cluster).
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--action-group-id` — Resource ID of the Azure Monitor action group to send notifications to.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Add a managed alert configuration that notifies an action group*
```azurecli
az aks alert-config add -g MyResourceGroup --cluster-name MyCluster -n myalerts --mode Managed --action-group-id /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.Insights/actionGroups/myag
```

*Add an alert configuration with alerting disabled*
```azurecli
az aks alert-config add -g MyResourceGroup --cluster-name MyCluster -n myalerts --mode Disabled
```

## az aks alert-config delete  (extension: aks-preview etc.)

Delete an alert configuration from a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the alert configuration to delete.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete an alert configuration*
```azurecli
az aks alert-config delete -g MyResourceGroup --cluster-name MyCluster -n myalerts
```

## az aks alert-config list  (extension: aks-preview etc.)

List the alert configurations of a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.

*List all alert configurations in a cluster*
```azurecli
az aks alert-config list -g MyResourceGroup --cluster-name MyCluster
```

## az aks alert-config show  (extension: aks-preview etc.)

Show the details of an alert configuration.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the alert configuration to show.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.

*Show an alert configuration*
```azurecli
az aks alert-config show -g MyResourceGroup --cluster-name MyCluster -n myalerts
```

## az aks alert-config update  (extension: aks-preview etc.)

Update an alert configuration in a managed cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the alert configuration to update.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--action-group-id` — Resource ID of the Azure Monitor action group to send notifications to.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--mode` — How AKS manages alerts for the cluster.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Turn off alerting without changing the notification target*
```azurecli
az aks alert-config update -g MyResourceGroup --cluster-name MyCluster -n myalerts --mode Disabled
```

*Point an existing alert configuration at a different action group*
```azurecli
az aks alert-config update -g MyResourceGroup --cluster-name MyCluster -n myalerts --action-group-id /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.Insights/actionGroups/otherag
```

*Clear the notification target*
```azurecli
az aks alert-config update -g MyResourceGroup --cluster-name MyCluster -n myalerts --action-group-id ""
```
