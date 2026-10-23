# az policy definition

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/definition  
> Microsoft doc last updated: unknown

Manage policy definitions.

Subgroups and commands: `az_policy_definition_create`, `az_policy_definition_delete`, `az_policy_definition_list`, `az_policy_definition_show`, `az_policy_definition_update`, `az_policy_definition_version`, `az_policy_definition_version_create`, `az_policy_definition_version_delete`, `az_policy_definition_version_list`, `az_policy_definition_version_show`, `az_policy_definition_version_update`

## az policy definition create

Create a policy definition.

**Required parameters**

- `--name -n` — The name of the policy definition.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — Policy definition description.
- `--display-name` — The display name of the policy definition.
- `--external-evaluation-enforcement-settings --external-settings` — The details of the source of external evaluation results required by the policy during enforcement evaluation. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--management-group` — The management group.
- `--metadata` — The policy definition metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--mode -m` — The policy definition mode. Default: Indexed.
- `--params -p` — The policy rule parameter definitions. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--rule --rules` — The policy rule. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--version` — The policy definition version.

*Create a read-only storage policy*
```azurecli
az policy definition create --name readOnlyStorage --rules "{ 'if': { 'field': 'type', 'equals': 'Microsoft.Storage/storageAccounts/write' }, 'then': { 'effect': 'deny' } }"
```

*Create a policy definition with parameters*
```azurecli
az policy definition create --name allowedLocations --rules "{ 'if': { 'allOf': [{ 'field': 'location','notIn': '[parameters(\'listOfAllowedLocations\')]' }, { 'field': 'location', 'notEquals': 'global' }, { 'field': 'type', 'notEquals': 'Microsoft.AzureActiveDirectory/b2cDirectories'}] }, 'then': { 'effect': 'deny' } }" --params "{ 'allowedLocations': {'type': 'array', 'metadata': { 'description': 'The list of locations that can be specified when deploying resources', 'strongType': 'location', 'displayName': 'Allowed locations' } } }"
```

*Create a read-only storage policy that can be applied within a management group*
```azurecli
az policy definition create -n readOnlyStorage --management-group "MyManagementGroup" --rules "{ 'if': { 'field': 'type', 'equals': 'Microsoft.Storage/storageAccounts/write' }, 'then': { 'effect': 'deny' } }"
```

*Create a policy definition with mode*
```azurecli
az policy definition create --name TagsPolicyDefinition --subscription "MySubscription" --mode Indexed --rules "{ 'if': { 'field': 'tags', 'exists': 'false' }, 'then': { 'effect': 'deny' } }"
```

*Create a read-only storage policy with newer version*
```azurecli
az policy definition create --name readOnlyStorage --rules "{ 'if': { 'field': 'type', 'equals': 'Microsoft.Storage/storageAccounts/write' }, 'then': { 'effect': 'deny' } }" --version 2.0.0
```

*Create a policy definition with external evaluation enforcement settings*
```azurecli
az policy definition create --name externalPolicy --rules "{ 'if': { 'value': '[claims().isValid]', 'equals': 'true' }, 'then': { 'effect': 'deny' } }" --external-settings "{ 'roleDefinitionIds': [ '/providers/Microsoft.Authorization/roleDefinitions/b24988ac-6180-42a0-ab88-20f7382dd24c' ], 'endpointSettings': { 'kind': 'CoinFlip' } }"
```

## az policy definition delete

Delete a policy definition.

**Required parameters**

- `--name -n` — The name of the policy definition.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--management-group` — The management group.

*Delete a policy definition*
```azurecli
az policy definition delete --name MyPolicyDefinition
```

## az policy definition list

Retrieve policy definitions.

**Optional parameters**

- `--filter` — Filter list results.
- `--management-group` — The management group.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.

*List built-in policy definitions*
```azurecli
az policy definition list --filter atScopeAndBelow()
```

*List policy definitions by management group*
```azurecli
az policy definition list --management-group MyManagementGroup
```

*List policy definitions by subscription*
```azurecli
az policy definition list
```

## az policy definition show

Retrieves a policy definition.

**Required parameters**

- `--name -n` — The name of the policy definition.

**Optional parameters**

- `--management-group` — The management group.

*Retrieve a policy definition at management group level*
```azurecli
az policy definition show --management-group MyManagementGroup --name ResourceNaming
```

*Retrieve a policy definition*
```azurecli
az policy definition show --name ResourceNaming
```

## az policy definition update

Update a policy definition.

**Required parameters**

- `--name -n` — The name of the policy definition.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — Policy definition description.
- `--display-name` — The display name of the policy definition.
- `--external-evaluation-enforcement-settings --external-settings` — The details of the source of external evaluation results required by the policy during enforcement evaluation. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--management-group` — The management group.
- `--metadata` — The policy definition metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--mode -m` — The policy definition mode.
- `--params -p` — The policy rule parameter definitions. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--rule --rules` — The policy rule. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.
- `--version` — The policy definition version.

*Update a policy definition display name*
```azurecli
az policy definition update --name MyPolicyDefinition --display-name "Updated display name goes here"
```
