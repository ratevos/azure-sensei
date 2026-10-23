# az policy set-definition version

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/set-definition/version  
> Microsoft doc last updated: unknown

Manage Version.

Subgroups and commands: `az_policy_set-definition_version_create`, `az_policy_set-definition_version_delete`, `az_policy_set-definition_version_list`, `az_policy_set-definition_version_show`, `az_policy_set-definition_version_update`

## az policy set-definition version create

Create a policy set definition version.

**Required parameters**

- `--name -n` — The name of the policy set definition.
- `--version` — The policy set definition version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--definition-groups` — The metadata describing groups of policy definition references within the policy set definition. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--definitions` — An array of policy definition references. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--description` — The policy set definition description.
- `--display-name` — The display name of the policy set definition.
- `--management-group` — The management group.
- `--metadata` — The policy set definition metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--params -p` — The policy set definition parameter definitions. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.

*Create a policy set definition with older version*
```azurecli
az policy set-definition version create -n readOnlyStorage --definitions "[ { 'policyDefinitionId': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyDefinitions/{policyDefinitionName}' } ]" --version 1.1.0
```

## az policy set-definition version delete

Delete a policy set definition version.

**Required parameters**

- `--name -n` — The name of the policy set definition.
- `--version` — The policy set definition version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--management-group` — The management group.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a policy set definition version*
```azurecli
az policy set-definition version delete --name CostManagement --version 1.2.1
```

## az policy set-definition version list

Retrieve policy set definition versions.

**Required parameters**

- `--name -n` — The name of the policy set definition.

**Optional parameters**

- `--expand` — Comma-separated list of additional properties to be included in the response. Supported values are 'LatestDefinitionVersion, EffectiveDefinitionVersion'.
- `--management-group` — The management group.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--top` — Maximum number of records to return. When the $top filter is not provided, it will return 500 records.

*List policy set definitions*
```azurecli
az policy set-definition version list --name CostManagement
```

## az policy set-definition version show

Retrieves a policy set definition version.

**Required parameters**

- `--name -n` — The name of the policy set definition.
- `--version` — The policy set definition version.

**Optional parameters**

- `--expand` — Comma-separated list of additional properties to be included in the response. Supported values are 'LatestDefinitionVersion, EffectiveDefinitionVersion'.
- `--management-group` — The management group.

*Retrieve a policy set definition version*
```azurecli
az policy set-definition version show --name CostManagement --version 1.2.1
```

## az policy set-definition version update

Update a policy set definition version.

**Required parameters**

- `--name -n` — The name of the policy set definition.
- `--version` — The policy set definition version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--definition-groups` — The metadata describing groups of policy definition references within the policy set definition. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--definitions` — An array of policy definition references. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--description` — The policy set definition description.
- `--display-name` — The display name of the policy set definition.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--management-group` — The management group.
- `--metadata` — The policy set definition metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--params -p` — The policy set definition parameter definitions. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.

*Update a policy set definition version*
```azurecli
az az policy set-definition version update -n readOnlyStorage --display-name "Updated display name goes here"
```
