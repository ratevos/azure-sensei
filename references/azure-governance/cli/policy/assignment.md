# az policy assignment

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/assignment  
> Microsoft doc last updated: unknown

Manage policy assignments.

Subgroups and commands: `az_policy_assignment_create`, `az_policy_assignment_delete`, `az_policy_assignment_identity`, `az_policy_assignment_identity_assign`, `az_policy_assignment_identity_remove`, `az_policy_assignment_identity_show`, `az_policy_assignment_list`, `az_policy_assignment_non-compliance-message`, `az_policy_assignment_non-compliance-message_create`, `az_policy_assignment_non-compliance-message_delete`, `az_policy_assignment_non-compliance-message_list`, `az_policy_assignment_non-compliance-message_show`, `az_policy_assignment_non-compliance-message_update`, `az_policy_assignment_show`, `az_policy_assignment_update`

## az policy assignment create

Create a policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--assign-identity --mi-system-assigned --system-assigned` — Sets the system assigned managed identity.
- `--change-reference` — The related change reference ID for this resource operation.
- `--definition-version` — The policy version to assign.
- `--description` — Policy assignment description.
- `--display-name` — The display name of the policy assignment.
- `--enforcement-mode -e` — The policy assignment enforcement mode. Default: Default.
- `--identity-scope` — Scope that the system assigned identity can access.
- `--location -l` — The location of the policy assignment.
- `--metadata` — The policy assignment metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--mi-user-assigned --user-assigned` — Sets the user assigned managed identity. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--name -n` — The name of the policy assignment.
- `--non-compliance-messages -m` — The messages that describe why a resource is non-compliant with the policy. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--not-scopes` — The policy assignment excluded scopes. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--overrides` — The policy override. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--params -p` — The parameter values for the assigned policy rule. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--policy` — The name or resource ID of the policy definition or policy set definition to be assigned.
- `--policy-set-definition -d` — The policy definition or policy set definition to assign.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-selectors` — The resource selectors list to filter policies by resource properties. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--role` — Role name or id that will be assigned to the managed identity.
- `--scope` — The scope of the policy assignment.
- `--self-serve --self-serve-exemption-settings` — The self-serve exemption settings for the policy assignment. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.

*Create a resource policy assignment at scope*
```azurecli
az policy assignment create --scope "/providers/Microsoft.Management/managementGroups/{managementGroupName}" --policy {policyName} -p "{ 'allowedLocations': { 'value': [ 'australiaeast', 'eastus', 'japaneast' ] } }"
```

*Create a resource policy assignment and provide rule parameter values*
```azurecli
az policy assignment create --policy {policyName} -p "{ 'allowedLocations': { 'value': [ 'australiaeast', 'eastus', 'japaneast' ] } }"
```

*Create a resource policy assignment with a system assigned identity*
```azurecli
az policy assignment create --name myPolicy --policy {policyName} --mi-system-assigned --location eastus
```

*Create a resource policy assignment with a system assigned identity with Contributor role access to the subscription*
```azurecli
az policy assignment create --name myPolicy --policy {policyName} --mi-system-assigned --identity-scope /subscriptions/{subscriptionId} --role Contributor --location eastus
```

*Create a resource policy assignment with a user assigned identity*
```azurecli
az policy assignment create --name myPolicy --policy {policyName} -g MyResourceGroup --mi-user-assigned myAssignedId --location westus
```

*Create a resource policy assignment with an enforcement mode*
```azurecli
az policy assignment create --name myPolicy --policy {policyName} --enforcement-mode DoNotEnforce
```

## az policy assignment delete

Delete a policy assignment.

**Required parameters**

- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Delete a policy assignment at scope*
```azurecli
az policy assignment delete --scope subscriptions/{subscriptionId} --name EnforceNaming
```

*Delete a policy assignment*
```azurecli
az policy assignment delete --name MyPolicyAssignment
```

## az policy assignment list

Retrieve all applicable policy assignments.

**Optional parameters**

- `--disable-scope-strict-match -d` — Include policy assignments either inherited from parent scopes or at child scopes.
- `--expand` — Additional properties to include in output.
- `--filter` — Filter list results.
- `--management-group` — The management group.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — Scope at which to list applicable policy assignments. If scope is not provided, the scope will be the implied or specified subscription.

*List policy assignments that apply to a resource group*
```azurecli
az policy assignment list --resource-group TestResourceGroup --filter atScope() --expand LatestDefinitionVersion, EffectiveDefinitionVersion
```

*List policy assignments that apply to a management group*
```azurecli
az policy assignment list --management-group TestManagementGroup --filter atScope()
```

*List policy assignments that apply to a subscription*
```azurecli
az policy assignment list --filter atScope()
```

## az policy assignment show

Retrieve a policy assignment.

**Required parameters**

- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--expand` — Additional properties to include in output.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Show a resource policy assignment*
```azurecli
az policy assignment show --name MyPolicyAssignment
```

## az policy assignment update

Update a policy assignment.

**Required parameters**

- `--name -n` — The name of the policy assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--definition-version` — The policy version to assign.
- `--description` — Policy assignment description.
- `--display-name` — The display name of the policy assignment.
- `--enforcement-mode -e` — The policy assignment enforcement mode.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--location -l` — The location of the policy assignment.
- `--metadata` — The policy assignment metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--non-compliance-messages -m` — The messages that describe why a resource is non-compliant with the policy. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--not-scopes` — The policy assignment excluded scopes. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--overrides` — The policy property value override. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--params -p` — The parameter values for the assigned policy rule. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--policy` — The name or resource ID of the policy definition or policy set definition to be assigned.
- `--policy-set-definition -d` — The policy definition or policy set definition to assign.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-selectors` — The resource selectors list to filter policies by resource properties. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--scope` — The scope of the policy assignment.
- `--self-serve --self-serve-exemption-settings` — The self-serve exemption settings for the policy assignment. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.

*Update a resource policy assignment's description*
```azurecli
az policy assignment update --name myPolicy --description 'My policy description'
```
