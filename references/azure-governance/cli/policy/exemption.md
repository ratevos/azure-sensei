# az policy exemption

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/exemption  
> Microsoft doc last updated: unknown

Manage policy exemptions.

Subgroups and commands: `az_policy_exemption_create`, `az_policy_exemption_delete`, `az_policy_exemption_list`, `az_policy_exemption_show`, `az_policy_exemption_update`

## az policy exemption create

Create a policy exemption.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--assignment-scope-validation -v` — The assignment scope validation. Default: Default.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — Policy exemption description.
- `--display-name` — The display name of the policy exemption.
- `--exemption-category -e` — The policy exemption category.
- `--expires-on` — The expiration date and time.
- `--metadata` — The policy exemption metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--name -n` — The name of the policy exemption.
- `--policy-assignment -a` — The policy assignment to exempt.
- `--policy-definition-reference-ids -r` — The policy definition reference IDs. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-selectors` — The resource selectors list to filter policies by resource properties. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--scope` — The scope of the policy assignment.

*Create a policy exemption in default subscription*
```azurecli
az policy exemption create -n exemptTestVM --policy-assignment "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments/limitVMSku" --exemption-category "Waiver"
```

*Create a policy exemption in the resource group*
```azurecli
az policy exemption create -n exemptTestVM --policy-assignment "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments/limitVMSku" --exemption-category "Waiver" --resource-group "myResourceGroup"
```

*Create a policy exemption in a management group*
```azurecli
az policy exemption create -n exemptTestVM --policy-assignment "/providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Authorization/policyAssignments/limitVMSku" --exemption-category "Waiver" --scope "/providers/Microsoft.Management/managementGroups/{managementGroupName}"
```

## az policy exemption delete

Delete a policy exemption.

**Required parameters**

- `--name -n` — The name of the policy exemption.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Delete a policy exemption*
```azurecli
az policy exemption delete --name MyPolicyExemption --resource-group "myResourceGroup"
```

## az policy exemption list

Retrieve all applicable policy exemptions.

**Optional parameters**

- `--disable-scope-strict-match -d` — Include policy exemptions either inherited from parent scopes or at child scopes.
- `--filter` — Filter list results.
- `--management-group` — The management group.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — Scope at which to list applicable policy exemptions. If scope is not provided, the scope will be the implied or specified subscription.

*List policy exemptions that apply to a management group*
```azurecli
az policy exemption list --management-group DevOrg --filter atScopeAndBelow()
```

*List policy exemptions that apply to a resource group*
```azurecli
az policy exemption list --resource-group TestResourceGroup
```

*List policy exemptions that apply to a subscription*
```azurecli
az policy exemption list
```

## az policy exemption show

Retrieve a policy exemption.

**Required parameters**

- `--name -n` — The name of the policy exemption.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The scope of the policy assignment.

*Show a policy exemption*
```azurecli
az policy exemption show --name MyPolicyExemption --resource-group "myResourceGroup"
```

## az policy exemption update

Update a policy exemption.

**Required parameters**

- `--name -n` — The name of the policy exemption.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--assignment-scope-validation -v` — The assignment scope validation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — Policy exemption description.
- `--display-name` — The display name of the policy exemption.
- `--exemption-category -e` — The policy exemption category.
- `--expires-on` — The expiration date and time.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--metadata` — The policy exemption metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--policy-assignment -a` — The policy assignment to exempt.
- `--policy-definition-reference-ids -r` — The policy definition reference IDs. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-selectors` — The resource selectors list to filter policies by resource properties. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--scope` — The scope of the policy assignment.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.

*Update a policy exemption category*
```azurecli
az policy exemption update -n exemptTestVM --exemption-category "Mitigated"
```

*Update a policy exemption in a resource group*
```azurecli
az policy exemption update -n exemptTestVM --display-name "Updated display name" --resource-group myResourceGroup
```

*Update a policy exemption at scope*
```azurecli
az policy exemption update -n exemptTestVM --description "This exemption is very cool." --scope "/providers/Microsoft.Management/managementGroups/{managementGroupName}"
```
