# az aks safeguards

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/safeguards  
> Microsoft doc last updated: unknown

Manage Deployment Safeguards.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_safeguards_create`, `az_aks_safeguards_create(aks-preview)`, `az_aks_safeguards_delete`, `az_aks_safeguards_delete(aks-preview)`, `az_aks_safeguards_list`, `az_aks_safeguards_list(aks-preview)`, `az_aks_safeguards_show`, `az_aks_safeguards_show(aks-preview)`, `az_aks_safeguards_update`, `az_aks_safeguards_update(aks-preview)`, `az_aks_safeguards_wait`, `az_aks_safeguards_wait(aks-preview)`

## az aks safeguards create

Enable Deployment Safeguards for a Managed Cluster.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--excluded-namespaces --excluded-ns` — User defined list of namespaces to exclude from Deployment Safeguards. Deployments in these namespaces will not be checked against any safeguards Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--level` — The deployment safeguards level. Possible values are Warn and Enforce.
- `--name -n` — The name of the Managed Cluster.You may provide either 'managed_cluster' or both 'resource_group' and name', but not both.
- `--no-wait` — Do not wait for the long-running operation to finish.
- `--pss-level` — The pod security standards level.
- `--resource-group -g` — The name of the resource group. You can configure the default group using az configure --defaults group=`<name>`. You may provide either 'managed_cluster' or both 'resource_group' and 'name', but not both.

*Create a DeploymentSafeguards resource at Warn level with a managed cluster resource id*
```azurecli
az aks safeguards create --resource /subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1 --level Warn
```

*Create a DeploymentSafeguards resource at Warn level using subscription, resourcegroup, and name tags*
```azurecli
az aks safeguards create --subscription subid1 -g rg1 -n cluster1 --level Warn
```

*Create a DeploymentSafeguards resource at Warn level with ignored namespaces*
```azurecli
az aks safeguards create -g rg1 -n mc1 --excluded-ns ns1 ns2 --level Warn
```

*Create a DeploymentSafeguards resource at Warn level with Pod Security Standards level set to Baseline*
```azurecli
az aks safeguards create --managed-cluster /subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1 --level Warn --pss-level Baseline
```

*Create a DeploymentSafeguards resource with PSS level set to Restricted using -g/-n pattern*
```azurecli
az aks safeguards create -g rg1 -n cluster1 --level Enforce --pss-level Restricted
```

## az aks safeguards create  (extension: aks-preview etc.)

Enable Deployment Safeguards for a Managed Cluster.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--excluded-namespaces --excluded-ns` — User defined list of namespaces to exclude from Deployment Safeguards. Deployments in these namespaces will not be checked against any safeguards Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--level` — The deployment safeguards level. Possible values are Warn and Enforce.
- `--name -n` — The name of the Managed Cluster. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--no-wait` — Do not wait for the long-running operation to finish.
- `--pss-level` — The pod security standards level.
- `--resource-group -g` — The name of the resource group. You can configure the default group using `az configure --defaults group=`<name>``. You may provide either --managed-cluster or both --resource-group and --name, but not both.

*Creates a DeploymentSafeguards resource at Warn level with a managed cluster resource id*
```azurecli
az aks safeguards create --resource /subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1 --level Warn
```

*Creates a DeploymentSafeguards resource at Warn level using subscription, resourcegroup, and name tags*
```azurecli
az aks safeguards create --subscription subid1 -g rg1 -n cluster1 --level Warn
```

*Create a DeploymentSafeguards resource at Warn level with ignored namespaces*
```azurecli
az aks safeguards create -g rg1 -n mc1 --excluded-ns ns1 ns2 --level Warn
```

*Creates a DeploymentSafeguards resource at Warn level with pod security standards level set to Baseline*
```azurecli
az aks safeguards create --managed-cluster subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1 --level Warn --pss-level Baseline
```

## az aks safeguards delete

Disable Deployment Safeguards for a Managed Cluster.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--name -n` — The name of the Managed Cluster.You may provide either 'managed_cluster' or both 'resource_group' and name', but not both.
- `--no-wait` — Do not wait for the long-running operation to finish.
- `--resource-group -g` — The name of the resource group. You can configure the default group using az configure --defaults group=`<name>`. You may provide either 'managed_cluster' or both 'resource_group' and 'name', but not both.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a DeploymentSafeguard resource by managed cluster id*
```azurecli
az aks safeguards delete -c subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1
```

*Delete a DeploymentSafeguard resource with resourceGroup and clusterName arguments*
```azurecli
az aks safeguards delete -g rg1 -n cluster1
```

## az aks safeguards delete  (extension: aks-preview etc.)

Disable Deployment Safeguards for a Managed Cluster.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--name -n` — The name of the Managed Cluster. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--no-wait` — Do not wait for the long-running operation to finish.
- `--resource-group -g` — The name of the resource group. You can configure the default group using `az configure --defaults group=`<name>``. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Deletes a DeploymentSafeguard resource by managed cluster id*
```azurecli
az aks safeguards delete -c subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1
```

*Deletes a DeploymentSafeguard resource with resourceGroup and clusterName arguments*
```azurecli
az aks safeguards delete -g rg1 -n cluster1
```

## az aks safeguards list

List DeploymentSafeguards by parent resource.

**Optional parameters**

- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--name -n` — The name of the Managed Cluster.You may provide either 'managed_cluster' or both 'resource_group' and name', but not both.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--resource-group -g` — The name of the resource group. You can configure the default group using az configure --defaults group=`<name>`. You may provide either 'managed_cluster' or both 'resource_group' and 'name', but not both.

*List DeploymentSafeguards by parent resource*
```azurecli
az aks safeguards list --managed-cluster subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1
```

*List DeploymentSafeguards by parent resource*
```azurecli
az aks safeguards list -g rg1 -n cluster1
```

## az aks safeguards list  (extension: aks-preview etc.)

List DeploymentSafeguards by parent resource.

**Optional parameters**

- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--name -n` — The name of the Managed Cluster. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--resource-group -g` — The name of the resource group. You can configure the default group using `az configure --defaults group=`<name>``. You may provide either --managed-cluster or both --resource-group and --name, but not both.

*List DeploymentSafeguards by parent resource*
```azurecli
az aks safeguards list --managed-cluster subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1
```

*List DeploymentSafeguards by parent resource*
```azurecli
az aks safeguards list -g rg1 -n cluster1
```

## az aks safeguards show

Show Deployment Safeguards Configuration for a Managed Cluster.

**Optional parameters**

- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--name -n` — The name of the Managed Cluster.You may provide either 'managed_cluster' or both 'resource_group' and name', but not both.
- `--resource-group -g` — The name of the resource group. You can configure the default group using az configure --defaults group=`<name>`. You may provide either 'managed_cluster' or both 'resource_group' and 'name', but not both.

*Get a DeploymentSafeguard resource by managed cluster id*
```azurecli
az aks safeguards show --managed-cluster subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1
```

*Get a DeploymentSafeguard resource with resourceGroup and clusterName arguments*
```azurecli
az aks safeguards show -g rg1 -n cluster1
```

## az aks safeguards show  (extension: aks-preview etc.)

Show Deployment Safeguards Configuration for a Managed Cluster.

**Optional parameters**

- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--name -n` — The name of the Managed Cluster. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--resource-group -g` — The name of the resource group. You can configure the default group using `az configure --defaults group=`<name>``. You may provide either --managed-cluster or both --resource-group and --name, but not both.

*Gets a DeploymentSafeguard resource by managed cluster id*
```azurecli
az aks safeguards show --managed-cluster subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1
```

*Gets a DeploymentSafeguard resource with resourceGroup and clusterName arguments*
```azurecli
az aks safeguards show -g rg1 -n cluster1
```

## az aks safeguards update

Update Deployment Safeguards configuration for a Managed Cluster.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--excluded-namespaces --excluded-ns` — User defined list of namespaces to exclude from Deployment Safeguards. Deployments in these namespaces will not be checked against any safeguards Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--level` — The deployment safeguards level. Possible values are Warn and Enforce.
- `--name -n` — The name of the Managed Cluster.You may provide either 'managed_cluster' or both 'resource_group' and name', but not both.
- `--no-wait` — Do not wait for the long-running operation to finish.
- `--pss-level` — The pod security standards level. Possible values: Privileged (off), Baseline, Restricted.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--resource-group -g` — The name of the resource group. You can configure the default group using az configure --defaults group=`<name>`. You may provide either 'managed_cluster' or both 'resource_group' and 'name', but not both.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.

*Update a DeploymentSafeguards resource by cluster id to Enforce level*
```azurecli
az aks safeguards update -c /subscriptions/subid/resourcegroups/rg1/providers/Microsoft.ContainerService/managedClusters/mc1 --level Enforce
```

*Update a DeploymentSafeguards resource to Enforce level using resourceGroup and name arguments*
```azurecli
az aks safeguards update --level Enforce -g rg1 -n mc1
```

*Update a DeploymentSafeguards resource by adding 2 new namespaces to ignore*
```azurecli
az aks safeguards update -g rg1 -n mc1 --excluded-ns ns1 ns2
```

*Update Pod Security Standards level to Restricted*
```azurecli
az aks safeguards update --managed-cluster /subscriptions/subid1/resourceGroups/rg1/providers/Microsoft.ContainerService/managedClusters/cluster1 --pss-level Restricted
```

*Update PSS level to Baseline using -g/-n pattern*
```azurecli
az aks safeguards update -g rg1 -n cluster1 --pss-level Baseline
```

*Update both safeguards level and PSS level*
```azurecli
az aks safeguards update -g rg1 -n cluster1 --level Enforce --pss-level Restricted
```

## az aks safeguards update  (extension: aks-preview etc.)

Update Deployment Safeguards configuration for a Managed Cluster.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--excluded-namespaces --excluded-ns` — User defined list of namespaces to exclude from Deployment Safeguards. Deployments in these namespaces will not be checked against any safeguards Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--level` — The deployment safeguards level. Possible values are Warn and Enforce.
- `--name -n` — The name of the Managed Cluster. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--no-wait` — Do not wait for the long-running operation to finish.
- `--pss-level` — The pod security standards level.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--resource-group -g` — The name of the resource group. You can configure the default group using `az configure --defaults group=`<name>``. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.

*Update a DeploymentSafeguards resource by cluster id to Enforce level*
```azurecli
az aks safeguards update -c /subscriptions/subid/resourcegroups/rg1/providers/Microsoft.ContainerService/managedClusters/mc1 --level Enforce
```

*Update a DeploymentSafeguards resource to Enforce level using resourceGroup and name arguments*
```azurecli
az aks safeguards update --level Enforce -g rg1 -n mc1
```

*Update a DeploymentSafeguards resource by adding 2 new namespaces to ignore*
```azurecli
az aks safeguards update -g rg1 -n mc1 --excluded-ns ns1 ns2
```

## az aks safeguards wait

Place the CLI in a waiting state until a condition is met.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--name -n` — The name of the Managed Cluster.You may provide either 'managed_cluster' or both 'resource_group' and name', but not both.
- `--resource-group -g` — The name of the resource group. You can configure the default group using az configure --defaults group=`<name>`. You may provide either 'managed_cluster' or both 'resource_group' and 'name', but not both.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

## az aks safeguards wait  (extension: aks-preview etc.)

Place the CLI in a waiting state until a condition is met.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster --managed-cluster -c` — The fully qualified Azure Resource manager identifier of the Managed Cluster.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--name -n` — The name of the Managed Cluster. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--resource-group -g` — The name of the resource group. You can configure the default group using `az configure --defaults group=`<name>``. You may provide either --managed-cluster or both --resource-group and --name, but not both.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.
