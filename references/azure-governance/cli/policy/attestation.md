# az policy attestation

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/attestation  
> Microsoft doc last updated: unknown

Manage resource policy attestations.

Subgroups and commands: `az_policy_attestation_create`, `az_policy_attestation_delete`, `az_policy_attestation_list`, `az_policy_attestation_show`, `az_policy_attestation_update`

## az policy attestation create

Create a policy attestation.

**Required parameters**

- `--attestation-name --name -n` — The name of the attestation.
- `--policy-assignment --policy-assignment-id -a` — The resource ID of the policy assignment that the attestation is setting the state for.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--assessment-date` — The time the evidence was assessed.
- `--change-reference` — The related change reference ID for this resource operation.
- `--comments` — Comments describing why this attestation was created.
- `--compliance-state` — The compliance state that should be set on the resource.
- `--definition-reference-id` — The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire s
- `--evidence` — The evidence supporting the compliance state set in this attestation.
- `--expires-on` — The time the compliance state should expire.
- `--metadata` — Additional metadata in space-separated key=value pairs for an attestation. This overwrites any existing metadata for the attestation.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--owner` — The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource --resource-id` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).

*Create an attestation at resource group scope for a policy assignment*
```azurecli
az policy attestation create -g myRg -n myAttestation --policy-assignment eeb18edc813c42d0ad5a9eab
```

*Create an attestation at resource group scope for a policy assignment using the policy assignment resource ID*
```azurecli
az policy attestation create -g myRg -n myAttestation \
  --policy-assignment "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/providers/Microsoft.Authorization/policyAssignments/myPa"
```

*Create an attestation at subscription scope for a policy set assignment*
```azurecli
az policy attestation create -n myAttestation \
  --policy-assignment eeb18edc813c42d0ad5a9eab \
  --definition-reference-id auditVMPolicyReference
```

*Create an attestation for a specific resource using the resource ID*
```azurecli
az policy attestation create \
  --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myRg/providers/Microsoft.Compute/virtualMachines/myVm" \
  -n myAttestation --policy-assignment eeb18edc813c42d0ad5a9eab
```

*Create an attestation at resource group scope using all properties*
```azurecli
az policy attestation create --attestation-name myAttestation -g myRg -a eeb18edc813c42d0ad5a9eab \
 --compliance-state Compliant --assessment-date 2023-01-01T08:29:18Z \
 --evidence source-uri=https://sampleuri.com description="Sample description for the sample uri" \
 --evidence source-uri=https://sampleuri2.com description="Sample description 2 for the sample uri 2" \
 --expires-on 2024-08-01T05:29:18Z --owner user@myOrg.com --metadata Location=NYC Dept=ACC \
 --definition-reference-id auditVMPolicyReference
```

## az policy attestation delete

Delete an existing policy attestation.

**Required parameters**

- `--attestation-name --name -n` — The name of the attestation.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource --resource-id` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).

*Delete an attestation at resource group scope*
```azurecli
az policy attestation delete -g myRg -n myAttestation
```

## az policy attestation list

List all attestations for a resource.

**Optional parameters**

- `--filter` — OData filter expression.
- `--resource --resource-id` — Resource ID.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--top` — Maximum number of records to return.

*List all policy attestations at subscription scope*
```azurecli
az policy attestation list
```

*List the top two policy attestations at resource group scope*
```azurecli
az policy attestation list -g myRg --top 2
```

*List all attestations that has the policy assignment id of myPolicyAssignment*
```azurecli
az policy attestation list --filter "PolicyAssignmentId eq '/subscriptions/35ee058e-5fa0-414c-8145-3ebb8d09b6e2/providers/microsoft.authorization/policyassignments/b101830944f246d8a14088c5'"
```

## az policy attestation show

Get a policy attestation.

**Required parameters**

- `--attestation-name --name -n` — The name of the attestation.

**Optional parameters**

- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--resource --resource-id` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).

*Show an attestation at subscription.*
```azurecli
az policy attestation show --attestation-name myAttestation
```

## az policy attestation update

Update an existing policy attestation.

**Required parameters**

- `--attestation-name --name -n` — The name of the attestation.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--assessment-date` — The time the evidence was assessed.
- `--change-reference` — The related change reference ID for this resource operation.
- `--comments` — Comments describing why this attestation was created.
- `--compliance-state` — The compliance state that should be set on the resource.
- `--definition-reference-id` — The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire s
- `--evidence` — The evidence supporting the compliance state set in this attestation.
- `--expires-on` — The time the compliance state should expire.
- `--metadata` — Additional metadata in space-separated key=value pairs for an attestation. This overwrites any existing metadata for the attestation.
- `--namespace` — Provider namespace (Ex: Microsoft.Provider).
- `--owner` — The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.
- `--parent` — The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
- `--policy-assignment --policy-assignment-id -a` — The resource ID of the policy assignment that the attestation is setting the state for.
- `--resource --resource-id` — Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-type` — Resource type (Ex: resourceTypeC).

*Update an attestation at resource scope*
```azurecli
az policy attestation update --attestation-name myAttestation \
  --resource "/subscriptions/fff10b27-fff3-fff5-fff8-fffbe01e86a5/resourceGroups/myRg/providers/Microsoft.Compute/virtualMachines/myVm" \
  --comments "Adding comments for this attestation"
```
