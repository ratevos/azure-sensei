# az policy enrollment

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/enrollment  
> Microsoft doc last updated: unknown

Manage policy enrollments.

Subgroups and commands: `az_policy_enrollment_create`, `az_policy_enrollment_delete`, `az_policy_enrollment_list`, `az_policy_enrollment_show`, `az_policy_enrollment_update`

## az policy enrollment create

Create a policy enrollment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--assignment-scope-validation -v` — The option whether to validate the enrollment is at or under the assignment scope.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — The description of the policy enrollment.
- `--display-name` — The display name of the policy enrollment.
- `--metadata` — The policy enrollment metadata. Metadata is an open ended object and is typically a collection of key value pairs. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--name -n` — The name of the policy enrollment.
- `--policy-assignment -a` — The policy assignment to enroll.
- `--policy-definition-reference-ids -r` — The policy definition reference IDs. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-selectors` — The resource selector list to filter policies by resource properties. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--scope` — The fully qualified Azure Resource manager identifier of the resource.

*Create a policy enrollment in default subscription*
```azurecli
az policy enrollment create -n enrollTestVm --policy-assignment "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments/limitVMSku"
```

*Create a policy enrollment in the resource group*
```azurecli
az policy enrollment create -n enrollTestVm --policy-assignment "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments/limitVMSku" --resource-group MyResourceGroup
```

*Create a policy enrollment in the management group*
```azurecli
az policy enrollment create -n enrollTestVm --policy-assignment "/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyAssignments/limitVMSku" --scope "/providers/Microsoft.Management/managementGroups/{managementGroupName}"
```

## az policy enrollment delete

Delete a policy enrollment.

**Required parameters**

- `--name -n` — The name of the policy enrollment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The fully qualified Azure Resource manager identifier of the resource.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a policy enrollment*
```azurecli
az policy enrollment delete --name MyPolicyEnrollment --resource-group "myResourceGroup"
```

## az policy enrollment list

Retrieve all applicable policy enrollments.

**Optional parameters**

- `--disable-scope-strict-match -d` — Include policy enrollments either inherited from parent scopes or at child scopes.
- `--filter` — Filter list results.
- `--management-group` — The management group.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — Scope at which to list applicable policy enrollments. If scope is not provided, the scope will be the implied or specified subscription.

*List policy enrollments for management group*
```azurecli
az policy enrollment list --management-group DevOrg --filter atScopeAndBelow()
```

*List policy enrollments for resource group*
```azurecli
az policy enrollment list --resource-group TestResourceGroup
```

*List policy enrollments for subscription*
```azurecli
az policy enrollment list
```

## az policy enrollment show

Retrieve a policy enrollment.

**Required parameters**

- `--name -n` — The name of the policy enrollment.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--scope` — The fully qualified Azure Resource manager identifier of the resource.

*Show a policy enrollment*
```azurecli
az policy enrollment show --name MyPolicyEnrollment --resource-group "myResourceGroup"
```

## az policy enrollment update

Update a policy enrollment.

**Required parameters**

- `--name -n` — The name of the policy enrollment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--assignment-scope-validation -v` — The option whether to validate the enrollment is at or under the assignment scope.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — The description of the policy enrollment.
- `--display-name` — The display name of the policy enrollment.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--metadata` — The policy enrollment metadata. Metadata is an open ended object and is typically a collection of key value pairs. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--policy-assignment -a` — The policy assignment to enroll.
- `--policy-definition-reference-ids -r` — The policy definition reference IDs. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-selectors` — The resource selector list to filter policies by resource properties. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--scope` — The fully qualified Azure Resource manager identifier of the resource.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.

*Update a policy enrollment in a resource group*
```azurecli
az policy enrollment update -n enrollTestVM --display-name "Updated display name" --resource-group myResourceGroup
```

*Update a policy enrollment at scope*
```azurecli
az policy enrollment update -n enrollTestVM --description "This enrollment is very cool." --scope "/providers/Microsoft.Management/managementGroups/{managementGroupName}"
```
