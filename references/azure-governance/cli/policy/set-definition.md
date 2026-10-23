# az policy set-definition

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/set-definition  
> Microsoft doc last updated: unknown

Manage policy set definitions.

Subgroups and commands: `az_policy_set-definition_create`, `az_policy_set-definition_delete`, `az_policy_set-definition_list`, `az_policy_set-definition_show`, `az_policy_set-definition_update`, `az_policy_set-definition_version`, `az_policy_set-definition_version_create`, `az_policy_set-definition_version_delete`, `az_policy_set-definition_version_list`, `az_policy_set-definition_version_show`, `az_policy_set-definition_version_update`

## az policy set-definition create

Create a policy set definition.

**Required parameters**

- `--name -n` — The name of the policy set definition.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--definition-groups` — The metadata describing groups of policy definition references within the policy set definition. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--definitions` — An array of policy definition references. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--description` — Policy set definition description.
- `--display-name` — The display name of the policy set definition.
- `--management-group` — The management group.
- `--metadata` — The policy set definition metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--params -p` — The policy set definition parameter definitions. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--version` — The policy set definition version.

*Create a policy set definition*
```azurecli
az policy set-definition create -n readOnlyStorage --definitions '[ { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}' } ]'
```

*Create a policy set definition with parameters*
```azurecli
az policy set-definition create -n readOnlyStorage --definitions "[ { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}', 'parameters': { 'storageSku': { 'value': '[parameters(\'requiredSku\')]' } } }]" --params "{ 'requiredSku': { 'type': 'String' } }"
```

*Create a policy set definition in a subscription*
```azurecli
az policy set-definition create -n readOnlyStorage --subscription {subscriptionName} --definitions "[ { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}' } ]"
```

*Create a policy set definition with policy definition groups*
```azurecli
az policy set-definition create -n computeRequirements --definitions "[ { 'policyDefinitionId ': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/storagePolicy', 'groupNames': [ 'CostSaving', 'Organizational' ] }, { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/tagPolicy', 'groupNames': [ 'Organizational' ] } ]" --definition-groups "[{ 'name': 'CostSaving' }, { 'name': 'Organizational' } ]"
```

*Create a policy set definition with newer version*
```azurecli
az policy set-definition create -n readOnlyStorage --definitions "[ { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}' } ]" --version 2.0.0
```

## az policy set-definition delete

Delete a policy set definition.

**Required parameters**

- `--name -n` — The name of the policy set definition.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--management-group` — The management group.

*Delete a policy set definition*
```azurecli
az policy set-definition delete --management-group myMg --name MyPolicySetDefinition
```

## az policy set-definition list

Retrieve policy set definitions.

**Optional parameters**

- `--expand` — Additional properties to include in output.
- `--filter` — Filter list results.
- `--management-group` — The management group.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.

*List policy set definitions*
```azurecli
az policy set-definition list
```

*List policy set definitions at management group level*
```azurecli
az policy set-definition list --management-group MyManagementGroup
```

## az policy set-definition show

Retrieve a policy set definition.

**Required parameters**

- `--name -n` — The name of the policy set definition.

**Optional parameters**

- `--expand` — Additional properties to include in output.
- `--management-group` — The management group.

*Retrieve a policy set definition at management group level*
```azurecli
az policy set-definition show --management-group MyManagementGroup --name CostManagement
```

*Retrieve a policy set definition*
```azurecli
az policy set-definition show --name CostManagement
```

## az policy set-definition update

Update a policy set definition.

**Required parameters**

- `--name -n` — The name of the policy set definition.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--definition-groups` — The metadata describing groups of policy definition references within the policy set definition. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--definitions` — An array of policy definition references. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--description` — Policy set definition description.
- `--display-name` — The display name of the policy set definition.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--management-group` — The management group.
- `--metadata` — The policy set definition metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--params -p` — The policy set definition parameter definitions. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.
- `--version` — The policy set definition version.

*Update a policy set definition*
```azurecli
az policy set-definition update --definitions '[ { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/storagePolicy' } ]' --name MyPolicySetDefinition
```

*Update the groups and definitions within a policy set definition*
```azurecli
az policy set-definition update -n computeRequirements --definitions "[ { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/storagePolicy', 'groupNames': [ 'CostSaving', 'Organizational' ] }, { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/tagPolicy', 'groupNames': [ 'Organizational' ] } ]" --definition-groups "[{ 'name': 'CostSaving' }, { 'name': 'Organizational' } ]"
```
