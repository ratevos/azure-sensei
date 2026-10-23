# az policy event

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/event  
> Microsoft doc last updated: unknown

Manage policy events.

Subgroups and commands: `az_policy_event_list`

## az policy event list

List policy events.

**Optional parameters**

- `--apply` — Apply expression for aggregations using OData notation.
- `--filter` — Filter expression using OData notation.
- `--from` — ISO 8601 formatted timestamp specifying the start time of the interval to query.
- `--management-group -m` — Name of management group.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--order-by` — Ordering expression using OData notation.
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--policy-assignment -a` — Name of policy assignment.
- `--policy-definition -d` — Name of policy definition.
- `--policy-set-definition -s` — Name of policy set definition.
- `--resource` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).
- `--select` — Select expression using OData notation.
- `--to` — ISO 8601 formatted timestamp specifying the end time of the interval to query.
- `--top` — Maximum number of records to return.

*Get policy events at current subscription scope created in the last day.*
```azurecli
az policy event list
```

*Get policy events at management group scope.*
```azurecli
az policy event list -m "myMg"
```

*Get policy events at resource group scope in current subscription.*
```azurecli
az policy event list -g "myRg"
```

*Get policy events for a resource using resource ID.*
```azurecli
az policy event list --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup /providers/Microsoft.EventHub/namespaces/myns1/eventhubs/eh1/consumergroups/cg1"
```

*Get policy events for a resource using resource name.*
```azurecli
az policy event list --resource "myKeyVault" --namespace "Microsoft.KeyVault" --resource-type "vaults" -g "myresourcegroup"
```

*Get policy events for a nested resource using resource name.*
```azurecli
az policy event list --resource "myRule1" --namespace "Microsoft.Network" --resource-type "securityRules" --parent "networkSecurityGroups/mysecuritygroup1" -g "myresourcegroup"
```

*Get policy events for a policy set definition in current subscription.*
```azurecli
az policy event list -s "fff58873-fff8-fff5-fffc-fffbe7c9d697"
```

*Get policy events for a policy definition in current subscription.*
```azurecli
az policy event list -d "fff69973-fff8-fff5-fffc-fffbe7c9d698"
```

*Get policy events for a policy assignment in current subscription.*
```azurecli
az policy event list -a "ddd8ef92e3714a5ea3d208c1"
```

*Get policy events for a policy assignment in the specified resource group in current subscription.*
```azurecli
az policy event list -g "myRg" -a "ddd8ef92e3714a5ea3d208c1"
```

*Get top 5 policy events in current subscription, selecting a subset of properties and customizing ordering.*
```azurecli
az policy event list --top 5 --order-by "timestamp desc, policyAssignmentName asc" --select "timestamp, resourceId, policyAssignmentId, policySetDefinitionId, policyDefinitionId"
```

*Get policy events in current subscription during a custom time interval.*
```azurecli
az policy event list --from "2018-03-08T00:00:00Z" --to "2018-03-15T00:00:00Z"
```

*Get policy events in current subscription filtering results based on some property values.*
```azurecli
az policy event list --filter "(policyDefinitionAction eq 'deny' or policyDefinitionAction eq 'audit') and resourceLocation ne 'eastus'"
```

*Get number of policy events in current subscription.*
```azurecli
az policy event list --apply "aggregate($count as numberOfRecords)"
```

*Get policy events in current subscription aggregating results based on some properties.*
```azurecli
az policy event list --apply "groupby((policyAssignmentId, policyDefinitionId, policyDefinitionAction, resourceId), aggregate($count as numEvents))"
```

*Get policy events in current subscription grouping results based on some properties.*
```azurecli
az policy event list --apply "groupby((policyAssignmentName, resourceId))"
```

*Get policy events in current subscription aggregating results based on some properties specifying multiple groupings.*
```azurecli
az policy event list --apply "groupby((policyAssignmentId, policyDefinitionId, resourceId))/groupby((policyAssignmentId, policyDefinitionId), aggregate($count as numResourcesWithEvents))"
```
