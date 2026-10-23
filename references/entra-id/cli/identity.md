# az identity

> Source: https://learn.microsoft.com/en-us/cli/azure/identity  
> Microsoft doc last updated: unknown

Manage Managed Identity.

Subgroups and commands: `az_identity_create`, `az_identity_delete`, `az_identity_federated-credential`, `az_identity_federated-credential_create`, `az_identity_federated-credential_delete`, `az_identity_federated-credential_list`, `az_identity_federated-credential_show`, `az_identity_federated-credential_update`, `az_identity_list`, `az_identity_list-operations`, `az_identity_list-resources`, `az_identity_show`, `az_identity_update`

## az identity create

Create an identity in the specified subscription and resource group.

**Required parameters**

- `--name --resource-name -n` — The name of the identity resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--isolation-scope` — Enum to configure regional restrictions on identity assignment, as necessary.
- `--location -l` — The geo-location where the resource lives When not specified, the location of the resource group will be used.
- `--resource-restriction` — Restrictions on which resource providers this identity can be assigned to. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--tags` — Resource tags. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.

*Create an identity with a name and a resource group.*
```azurecli
az identity create --name myIdentityName --resource-group myResourceGroup
```

*Create an identity using the resource restrictions and isolation scope parameter.*
```azurecli
az identity create --name myIdentityName --resource-group myResourceGroup --resource-restriction {"providers":["Microsoft.Compute"]} --isolation-scope Regional
```

## az identity delete

Delete the identity.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--ids` — One or more resource IDs (space-delimited). It should be a complete resource ID containing all information of 'Resource Id' arguments. You should provide either --ids or other 'Resource Id' arguments.
- `--name --resource-name -n` — The name of the identity resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--subscription` — Name or ID of subscription. You can configure the default subscription using `az account set -s NAME_OR_ID`.

## az identity list

List all the userAssignedIdentities available under the subscription or specified ResourceGroup.

**Optional parameters**

- `--max-items` — Total number of items to return in the command's output. If the total number of items available is more than the value specified, a token is provided in the command's output. To resume pagination, provide the token value in `--next-token` argument of a subsequent command.
- `--next-token` — Token to specify where to start paginating. This is the token value from a previously truncated response.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*List user-assigned identities under a resource group.*
```azurecli
az identity list --resource-group MyResourceGroup
```

*List user-assigned identities under the current subscription.*
```azurecli
az identity list
```

## az identity list-operations

List available operations for the Managed Identity provider.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az identity list-resources

List the associated resources for the identity.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--ids` — One or more resource IDs (space-delimited). It should be a complete resource ID containing all information of 'Resource Id' arguments. You should provide either --ids or other 'Resource Id' arguments.
- `--name -n` — The name of the identity resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--subscription` — Name or ID of subscription. You can configure the default subscription using `az account set -s NAME_OR_ID`.

## az identity show

Get the identity.

**Optional parameters**

- `--ids` — One or more resource IDs (space-delimited). It should be a complete resource ID containing all information of 'Resource Id' arguments. You should provide either --ids or other 'Resource Id' arguments.
- `--name --resource-name -n` — The name of the identity resource.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--subscription` — Name or ID of subscription. You can configure the default subscription using `az account set -s NAME_OR_ID`.

## az identity update

Update an identity in the specified subscription and resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--add` — Add an object to a list of objects by specifying a path and key value pairs. Example: `--add property.listProperty <key=value, string or JSON string>`.
- `--change-reference` — The related change reference ID for this resource operation.
- `--force-string` — When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
- `--ids` — One or more resource IDs (space-delimited). It should be a complete resource ID containing all information of 'Resource Id' arguments. You should provide either --ids or other 'Resource Id' arguments.
- `--isolation-scope` — Enum to configure regional restrictions on identity assignment, as necessary.
- `--name --resource-name -n` — The name of the identity resource.
- `--remove` — Remove a property or an element from a list. Example: `--remove property.list <indexToRemove>` OR `--remove propertyToRemove`.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--resource-restriction` — Restrictions on which resource providers this identity can be assigned to. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.
- `--set` — Update an object by specifying a property path and value to set. Example: `--set property1.property2=<value>`.
- `--subscription` — Name or ID of subscription. You can configure the default subscription using `az account set -s NAME_OR_ID`.
- `--tags` — Resource tags. Support shorthand-syntax, json-file and yaml-file. Try "??" to show more.

*Update an identity's isolation scope with a name and resource group.*
```azurecli
az identity update --name myIdentityName --resource-group myResourceGroup --isolation-scope None
```

*Update an identity using the resource restrictions and isolation scope parameter.*
```azurecli
az identity update --name myIdentityName --resource-group myResourceGroup --resource-restriction {"providers":["Microsoft.Storage"]} --isolation-scope Regional
```
