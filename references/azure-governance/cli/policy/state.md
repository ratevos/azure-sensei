# az policy state

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/state  
> Microsoft doc last updated: unknown

Manage policy compliance states.

Subgroups and commands: `az_policy_state_list`, `az_policy_state_summarize`, `az_policy_state_trigger-scan`

## az policy state list

List policy compliance states.

**Optional parameters**

- `--all` — Within the specified time interval, get all policy states instead of the latest only. Default: False.
- `--apply` — Apply expression for aggregations using OData notation.
- `--expand` — Expand expression using OData notation.
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

*Get latest policy states at current subscription scope.*
```azurecli
az policy state list
```

*Get all policy states at current subscription scope.*
```azurecli
az policy state list --all
```

*Get latest policy states at management group scope.*
```azurecli
az policy state list -m "myMg"
```

*Get latest policy states at resource group scope in current subscription.*
```azurecli
az policy state list -g "myRg"
```

*Get latest policy states for a resource using resource ID.*
```azurecli
az policy state list --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup /providers/Microsoft.EventHub/namespaces/myns1/eventhubs/eh1/consumergroups/cg1"
```

*Get latest policy states for a resource using resource name.*
```azurecli
az policy state list --resource "myKeyVault" --namespace "Microsoft.KeyVault" --resource-type "vaults" -g "myresourcegroup"
```

*Get latest policy states for a nested resource using resource name.*
```azurecli
az policy state list --resource "myRule1" --namespace "Microsoft.Network" --resource-type "securityRules" --parent "networkSecurityGroups/mysecuritygroup1" -g "myresourcegroup"
```

*Get latest policy states for a policy set definition in current subscription.*
```azurecli
az policy state list -s "fff58873-fff8-fff5-fffc-fffbe7c9d697"
```

*Get latest policy states for a policy definition in current subscription.*
```azurecli
az policy state list -d "fff69973-fff8-fff5-fffc-fffbe7c9d698"
```

*Get latest policy states for a policy assignment in current subscription.*
```azurecli
az policy state list -a "ddd8ef92e3714a5ea3d208c1"
```

*Get latest policy states for a policy assignment in the specified resource group in current subscription.*
```azurecli
az policy state list -g "myRg" -a "ddd8ef92e3714a5ea3d208c1"
```

*Get top 5 latest policy states in current subscription, selecting a subset of properties and customizing ordering.*
```azurecli
az policy state list --top 5 --order-by "timestamp desc, policyAssignmentName asc" --select "timestamp, resourceId, policyAssignmentId, policySetDefinitionId, policyDefinitionId"
```

*Get latest policy states in current subscription during a custom time interval.*
```azurecli
az policy state list --from "2018-03-08T00:00:00Z" --to "2018-03-15T00:00:00Z"
```

*Get latest policy states in current subscription filtering results based on some property values.*
```azurecli
az policy state list --filter "(policyDefinitionAction eq 'deny' or policyDefinitionAction eq 'audit') and resourceLocation ne 'eastus'"
```

*Get number of latest policy states in current subscription.*
```azurecli
az policy state list --apply "aggregate($count as numberOfRecords)"
```

*Get latest policy states in current subscription aggregating results based on some properties.*
```azurecli
az policy state list --apply "groupby((policyAssignmentId, policySetDefinitionId, policyDefinitionReferenceId, policyDefinitionId), aggregate($count as numStates))"
```

*Get latest policy states in current subscription grouping results based on some properties.*
```azurecli
az policy state list --apply "groupby((policyAssignmentName, resourceId))"
```

*Get latest policy states in current subscription aggregating results based on some properties specifying multiple groupings.*
```azurecli
az policy state list --apply "groupby((policyAssignmentId, policySetDefinitionId, policyDefinitionReferenceId, policyDefinitionId, resourceId))/groupby((policyAssignmentId, policySetDefinitionId, policyDefinitionReferenceId, policyDefinitionId), aggregate($count as numNonCompliantResources))"
```

*Get latest policy states for a resource including policy evaluation details.*
```azurecli
az policy state list --resource "myKeyVault" --namespace "Microsoft.KeyVault" --resource-type "vaults" -g "myresourcegroup" --expand PolicyEvaluationDetails
```

*Get latest component policy states for a resource (eg. vault) and policy assignment referencing a resource provider mode policy definition*
```azurecli
az policy state list --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup/providers/Microsoft.KeyVault/vaults/myKeyVault" --filter "policyAssignmentId eq '/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/providers/Microsoft.Authorization/policyAssignments/myPa'" --expand "Components($filter=ComplianceState eq 'NonCompliant' or ComplianceState eq 'Compliant')"
```

*Get latest component policy states for a resource (eg. vault) and policy assignment referencing an initiative containing a resource provider mode policy definition*
```azurecli
az policy state list --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup/providers/Microsoft.KeyVault/vaults/myKeyVault" --filter "policyAssignmentId eq '/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/providers/Microsoft.Authorization/policyAssignments/myPa' and policyDefinitionReferenceId eq 'myResourceProviderModeDefinitionReferenceId'" --expand "Components($filter=ComplianceState eq 'NonCompliant' or ComplianceState eq 'Compliant')"
```

*Get latest component counts by compliance state for a resource (eg. vault) and policy assignment referencing a resource provider mode policy definition*
```azurecli
az policy state list --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup/providers/Microsoft.KeyVault/vaults/myKeyVault" --filter "policyAssignmentId eq '/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/providers/Microsoft.Authorization/policyAssignments/myPa'" --expand "Components($filter=ComplianceState eq 'NonCompliant' or ComplianceState eq 'Compliant' or ComplianceState eq 'Conflict';$apply=groupby((complianceState),aggregate($count as count)))"
```

## az policy state summarize

Summarize policy compliance states.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--filter` — Filter expression using OData notation.
- `--from` — ISO 8601 formatted timestamp specifying the start time of the interval to query.
- `--management-group -m` — Name of management group.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--policy-assignment -a` — Name of policy assignment.
- `--policy-definition -d` — Name of policy definition.
- `--policy-set-definition -s` — Name of policy set definition.
- `--resource` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).
- `--to` — ISO 8601 formatted timestamp specifying the end time of the interval to query.
- `--top` — Maximum number of records to return.

*Get latest non-compliant policy states summary at current subscription scope.*
```azurecli
az policy state summarize
```

*Get latest non-compliant policy states summary at management group scope.*
```azurecli
az policy state summarize -m "myMg"
```

*Get latest non-compliant policy states summary at resource group scope in current subscription.*
```azurecli
az policy state summarize -g "myRg"
```

*Get latest non-compliant policy states summary for a resource using resource ID.*
```azurecli
az policy state summarize --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myResourceGroup /providers/Microsoft.EventHub/namespaces/myns1/eventhubs/eh1/consumergroups/cg1"
```

*Get latest non-compliant policy states summary for a resource using resource name.*
```azurecli
az policy state summarize --resource "myKeyVault" --namespace "Microsoft.KeyVault" --resource-type "vaults" -g "myresourcegroup"
```

*Get latest non-compliant policy states summary for a nested resource using resource name.*
```azurecli
az policy state summarize --resource "myRule1" --namespace "Microsoft.Network" --resource-type "securityRules" --parent "networkSecurityGroups/mysecuritygroup1" -g "myresourcegroup"
```

*Get latest non-compliant policy states summary for a policy set definition in current subscription.*
```azurecli
az policy state summarize -s "fff58873-fff8-fff5-fffc-fffbe7c9d697"
```

*Get latest non-compliant policy states summary for a policy definition in current subscription.*
```azurecli
az policy state summarize -d "fff69973-fff8-fff5-fffc-fffbe7c9d698"
```

*Get latest non-compliant policy states summary for a policy assignment in current subscription.*
```azurecli
az policy state summarize -a "ddd8ef92e3714a5ea3d208c1"
```

*Get latest non-compliant policy states summary for a policy assignment in the specified resource group in current subscription.*
```azurecli
az policy state summarize -g "myRg" -a "ddd8ef92e3714a5ea3d208c1"
```

*Get latest non-compliant policy states summary in current subscription, limiting the assignments summary to top 5.*
```azurecli
az policy state summarize --top 5
```

*Get latest non-compliant policy states summary in current subscription for a custom time interval.*
```azurecli
az policy state summarize --from "2018-03-08T00:00:00Z" --to "2018-03-15T00:00:00Z"
```

*Get latest non-compliant policy states summary in current subscription filtering results based on some property values.*
```azurecli
az policy state summarize --filter "(policyDefinitionAction eq 'deny' or policyDefinitionAction eq 'audit') and resourceLocation ne 'eastus'"
```

## az policy state trigger-scan

Trigger a policy compliance evaluation for a scope.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Trigger a policy compliance evaluation at the current subscription scope.*
```azurecli
az policy state trigger-scan
```

*Trigger a policy compliance evaluation for a resource group.*
```azurecli
az policy state trigger-scan -g "myRg"
```

*Trigger a policy compliance evaluation for a resource group and do not wait for it to complete.*
```azurecli
az policy state trigger-scan -g "myRg" --no-wait
```
