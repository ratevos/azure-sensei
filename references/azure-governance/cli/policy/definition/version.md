# az policy definition version

> Source: https://learn.microsoft.com/en-us/cli/azure/policy/definition/version  
> Microsoft doc last updated: unknown

Manage policy definition versions.

Subgroups and commands: `az_policy_definition_version_create`, `az_policy_definition_version_delete`, `az_policy_definition_version_list`, `az_policy_definition_version_show`, `az_policy_definition_version_update`

## az policy definition version create

Create a policy definition version.

**Required parameters**

- `--name -n` — The name of the policy definition.
- `--version` — The policy definition version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — The policy definition description.
- `--display-name` — The display name of the policy definition.
- `--external-evaluation-enforcement-settings --external-settings` — The details of the source of external evaluation results required by the policy during enforcement evaluation. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--management-group` — The management group.
- `--metadata` — The policy definition metadata. Support shorthand-syntax(full value only), json-file and yaml-file.
- `--mode -m` — The policy definition mode. Default: Indexed.
- `--params -p` — The policy rule parameter definitions. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--rule --rules` — The policy rule. Support shorthand-syntax(full value only), json-file and yaml-file.

*Create a policy definition with older version*
```azurecli
az policy definition version create --name readOnlyStorage --rules "{ 'if': { 'field': 'type', 'equals': 'Microsoft.Storage/storageAccounts/write' }, 'then': { 'effect': 'deny' } }" --version 1.1.0
```

## az policy definition version delete

Delete a policy definition version.

**Required parameters**

- `--name -n` — The name of the policy definition.
- `--version` — The policy definition version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--management-group` — The management group.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a policy definition version*
```azurecli
az policy definition version delete --name ResourceNaming --version 1.2.1
```

## az policy definition version list

Retrieve policy definition versions.

**Required parameters**

- `--name -n` — The name of the policy definition.

**Optional parameters**

- `--management-group` — The management group.
- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--top` — Maximum number of records to return. When the $top filter is not provided, it will return 500 records.

*List policy definition versions by subscription*
```azurecli
az policy definition version list --name ResourceNaming
```

## az policy definition version show

Retrieves a policy definition version.

**Required parameters**

- `--name -n` — The name of the policy definition.
- `--version` — The policy definition version.

**Optional parameters**

- `--management-group` — The management group.

*Retrieve a policy definition version*
```azurecli
az policy definition version show --name ResourceNaming --version 1.2.1
```

## az policy definition version update

Update a policy definition version.

**Required parameters**

- `--name -n` — The name of the policy definition.
- `--version` — The policy definition version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — The policy definition description.
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

*Update a policy definition version*
```azurecli
az policy definition version update -n readOnlyStorage --display-name "Updated display name goes here"
```
