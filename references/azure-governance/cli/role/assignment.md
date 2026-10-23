# az role assignment

> Source: https://learn.microsoft.com/en-us/cli/azure/role/assignment  
> Microsoft doc last updated: unknown

Manage role assignments.

Subgroups and commands: `az_role_assignment_create`, `az_role_assignment_delete`, `az_role_assignment_list`, `az_role_assignment_list-changelogs`, `az_role_assignment_update`

## az role assignment create

Create a new role assignment for a user, group, or service principal.

**Required parameters**

- `--role` — Role name or id.
- `--scope` — Scope at which the role assignment or definition applies to, e.g., /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333, /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup, or /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Comput

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--assignee` — Represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name.
- `--assignee-object-id` — The assignee's object ID (also known as principal ID). Use this argument instead of '--assignee' to bypass Microsoft Graph query in case the logged-in account has no permission or the machine has no network access to query Microsoft Graph.
- `--assignee-principal-type` — Use with --assignee-object-id to avoid errors caused by propagation latency in Microsoft Graph.
- `--change-reference` — The related change reference ID for this resource operation.
- `--condition` — Condition under which the user can be granted permission.
- `--condition-version` — Version of the condition syntax. If --condition is specified without --condition-version, default to 2.0.
- `--description` — Description of role assignment.
- `--name -n` — A GUID for the role assignment. It must be unique and different for each role assignment. If omitted, a new GUID is generated.

*Create role assignment to grant the specified assignee the Reader role on an Azure virtual machine.*
```azurecli
az role assignment create --assignee sp_name --role Reader --scope /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.Compute/virtualMachines/MyVm
```

*Create role assignment for an assignee with description and condition.*
```azurecli
az role assignment create --role Owner --scope /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.Storage/storageAccounts/MyStorageAccount --assignee "John.Doe@Contoso.com" --description "Role assignment foo to check on bar" --condition "@Resource[Microsoft.Storage/storageAccounts/blobServices/containers:Name] stringEquals 'foo'" --condition-version "2.0"
```

*Create role assignment with your own assignment name.*
```azurecli
az role assignment create --assignee-object-id 00000000-0000-0000-0000-000000000000 --assignee-principal-type ServicePrincipal --role Reader --scope /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup --name 00000000-0000-0000-0000-000000000000
```

## az role assignment delete

Delete role assignments.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--assignee` — Represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name.
- `--assignee-object-id` — The assignee's object ID (also known as principal ID). Use this argument instead of '--assignee' to bypass Microsoft Graph query in case the logged-in account has no permission or the machine has no network access to query Microsoft Graph.
- `--change-reference` — The related change reference ID for this resource operation.
- `--ids` — Space-separated role assignment ids.
- `--include-inherited` — Include assignments applied on parent scopes. Default: False.
- `--resource-group -g` — Use it only if the role or assignment was added at the level of a resource group.
- `--role` — Role name or id.
- `--scope` — Scope at which the role assignment or definition applies to, e.g., /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333, /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup, or /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Comput
- `--yes -y` — Currently no-op.

*Delete all role assignments with "Reader" role at the subscription scope.*
```azurecli
az role assignment delete --role Reader --scope /subscriptions/00000000-0000-0000-0000-000000000000
```

*Delete all role assignments of an assignee at the subscription scope.*
```azurecli
az role assignment delete --assignee 00000000-0000-0000-0000-000000000000 --scope /subscriptions/00000000-0000-0000-0000-000000000000
```

*Delete all role assignments of an assignee (with its object ID) at the subscription scope.*
```azurecli
az role assignment delete --assignee-object-id 00000000-0000-0000-0000-000000000000 --scope /subscriptions/00000000-0000-0000-0000-000000000000
```

## az role assignment list

List role assignments.

**Optional parameters**

- `--all` — Show all assignments under the current subscription. Default: False.
- `--assignee` — Represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name.
- `--assignee-object-id` — The assignee's object ID (also known as principal ID). Use this argument instead of '--assignee' to bypass Microsoft Graph query in case the logged-in account has no permission or the machine has no network access to query Microsoft Graph.
- `--fill-principal-name` — Query Microsoft Graph to get the assignee's userPrincipalName (for user), servicePrincipalNames (for service principal) or displayName (for group), then fill principalName property with it. If the logged-in account has no permission or the machine has no network access to query Microsoft Graph, set  Default: True.
- `--fill-role-definition-name` — Fill roleDefinitionName property in addition to roleDefinitionId. This operation is expensive. If you encounter performance issue, set this flag to false. Default: True.
- `--include-groups` — Include extra assignments to the groups of which the user is a member (transitively). Default: False.
- `--include-inherited` — Include assignments applied on parent scopes. Default: False.
- `--resource-group -g` — Use it only if the role or assignment was added at the level of a resource group.
- `--role` — Role name or id.
- `--scope` — Scope at which the role assignment or definition applies to, e.g., /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333, /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup, or /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Comput

*List role assignments at the subscription scope.*
```azurecli
az role assignment list --scope /subscriptions/00000000-0000-0000-0000-000000000000
```

*List role assignments at the subscription scope, without filling roleDefinitionName property.*
```azurecli
az role assignment list --scope /subscriptions/00000000-0000-0000-0000-000000000000 --fill-role-definition-name false
```

*List role assignments with "Reader" role at the subscription scope.*
```azurecli
az role assignment list --role Reader --scope /subscriptions/00000000-0000-0000-0000-000000000000
```

*List role assignments of an assignee at the subscription scope.*
```azurecli
az role assignment list --assignee 00000000-0000-0000-0000-000000000000 --scope /subscriptions/00000000-0000-0000-0000-000000000000
```

*List role assignments of an assignee (with its object ID) at the subscription scope, without filling principalName property. This command does not query Microsoft Graph.*
```azurecli
az role assignment list --assignee-object-id 00000000-0000-0000-0000-000000000000 --scope /subscriptions/00000000-0000-0000-0000-000000000000 --fill-principal-name false
```

## az role assignment list-changelogs

List changelogs for role assignments.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--end-time` — The end time of the query in the format of %Y-%m-%dT%H:%M:%SZ, e.g. 2000-12-31T12:59:59Z. Defaults to the current time.
- `--start-time` — The start time of the query in the format of %Y-%m-%dT%H:%M:%SZ, e.g. 2000-12-31T12:59:59Z. Defaults to 1 Hour prior to the current time.

## az role assignment update

Update an existing role assignment for a user, group, or service principal.

**Required parameters**

- `--role-assignment` — Description of an existing role assignment as JSON, or a path to a file containing a JSON description.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Update a role assignment from a JSON file.*
```azurecli
az role assignment update --role-assignment assignment.json
```

*Update a role assignment from a JSON string. (Bash)*
```azurecli
az role assignment update --role-assignment '{
    "canDelegate": null,
    "condition": "@Resource[Microsoft.Storage/storageAccounts/blobServices/containers:Name] stringEquals '"'"'foo'"'"'",
    "conditionVersion": "2.0",
    "description": "Role assignment foo to check on bar",
    "id": "/subscriptions/00000001-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Authorization/roleAssignments/3eabdd43-375b-4dbd-8dc4-04acd15ce56b",
    "name": "3eabdd43-375b-4dbd-8dc4-04acd15ce56b",
    "principalId": "00000002-0000-0000-0000-000000000000",
    "principalType": "User",
    "resourceGroup": "rg1",
    "roleDefinitionId": "/subscriptions/00000001-0000-0000-0000-000000000000/providers/Microsoft.Authorization/roleDefinitions/acdd72a7-3385-48ef-bd42-f606fba81ae7",
    "scope": "/subscriptions/00000001-0000-0000-0000-000000000000/resourceGroups/rg1",
    "type": "Microsoft.Authorization/roleAssignments"
}'
```
