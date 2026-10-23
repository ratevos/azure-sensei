# az policy remediation

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/remediation  
> Microsoft doc last updated: unknown

Manage resource policy remediations.

Subgroups and commands: `az_policy_remediation_cancel`, `az_policy_remediation_create`, `az_policy_remediation_delete`, `az_policy_remediation_deployment`, `az_policy_remediation_deployment_list`, `az_policy_remediation_list`, `az_policy_remediation_show`

## az policy remediation cancel

Cancel a resource policy remediation.

**Required parameters**

- `--name -n` — Name of the remediation.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--management-group -m` — Name of management group.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).

## az policy remediation create

Create a resource policy remediation.

**Required parameters**

- `--name -n` — Name of the remediation.
- `--policy-assignment -a` — Name or resource ID of the policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--definition-reference-id` — Policy definition reference ID inside the policy set definition. Only required when the policy assignment is assigning a policy set definition.
- `--location-filters` — Space separated list of resource locations that should be remediated (Ex: centralus westeurope).
- `--management-group -m` — Name of management group.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-discovery-mode` — The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).

*Create a remediation at resource group scope for a policy assignment*
```azurecli
az policy remediation create -g myRg -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab
```

*Create a remediation at resource group scope for a policy assignment using the policy assignment resource ID*
```azurecli
az policy remediation create -g myRg -n myRemediation --policy-assignment "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/providers/Microsoft.Authorization/policyAssignments/myPa"
```

*Create a remediation at subscription scope for a policy set assignment*
```azurecli
az policy remediation create -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab --definition-reference-id auditVMPolicyReference
```

*Create a remediation at management group scope for specific resource locations*
```azurecli
az policy remediation create -m myMg -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab --location-filters eastus westeurope
```

*Create a remediation for a specific resource using the resource ID*
```azurecli
az policy remediation create --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myRg/providers/Microsoft.Compute/virtualMachines/myVm" -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab
```

*Create a remediation that will re-evaluate compliance before remediating*
```azurecli
az policy remediation create -g myRg -n myRemediation --policy-assignment eeb18edc813c42d0ad5a9eab --resource-discovery-mode ReEvaluateCompliance
```

## az policy remediation delete

Delete a resource policy remediation.

**Required parameters**

- `--name -n` — Name of the remediation.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--management-group -m` — Name of management group.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).

## az policy remediation list

List resource policy remediations.

**Optional parameters**

- `--management-group -m` — Name of management group.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).

## az policy remediation show

Show a resource policy remediation.

**Required parameters**

- `--name -n` — Name of the remediation.

**Optional parameters**

- `--management-group -m` — Name of management group.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).
