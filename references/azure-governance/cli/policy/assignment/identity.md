# az policy assignment identity

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/assignment/identity  
> Microsoft doc last updated: unknown

Manage identity of the policy assignment.

Subgroups and commands: `az_policy_assignment_identity_assign`, `az_policy_assignment_identity_remove`, `az_policy_assignment_identity_show`

## az policy assignment identity assign

Assign a managed identity.

**Required parameters**

- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--identity-scope` — Scope that the system assigned identity can access.
- `--mi-system-assigned --system-assigned` — Set the system managed identity.
- `--mi-user-assigned --user-assigned` — Set the user managed identity. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--role` — Role name or id that will be assigned to the managed identity.
- `--scope` — The scope of the policy assignment.

*Add a system assigned managed identity to a policy assignment*
```azurecli
az policy assignment identity assign --system-assigned -g MyResourceGroup -n MyPolicyAssignment
```

*Add a system assigned managed identity to a policy assignment and grant it the Contributor role for a resource group*
```azurecli
az policy assignment identity assign --system-assigned -g MyResourceGroup -n MyPolicyAssignment --role Contributor --identity-scope /subscriptions/{subscriptionId}/resourceGroups/MyResourceGroup
```

*Add a user assigned managed identity to a policy assignment*
```azurecli
az policy assignment identity assign --user-assigned MyAssignedId -g MyResourceGroup -n MyPolicyAssignment
```

## az policy assignment identity remove

Remove the managed identity.

**Required parameters**

- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--mi-system-assigned --system-assigned` — Remove the system managed identity.
- `--mi-user-assigned --user-assigned` — Remove the user managed identity. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Remove user assigned managed identity from a policy assignment*
```azurecli
az policy assignment identity remove --name MyPolicyAssignment --user-assigned
```

## az policy assignment identity show

Retrieve the managed identity.

**Required parameters**

- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Show a policy assignment's managed identity*
```azurecli
az policy assignment identity show --name MyPolicyAssignment --scope '/providers/Microsoft.Management/managementGroups/{managementGroupName}'
```
