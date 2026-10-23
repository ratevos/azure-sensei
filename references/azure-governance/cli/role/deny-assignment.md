# az role deny-assignment

> Source: https://learn.microsoft.com/en-us/cli/azure/role/deny-assignment  
> Microsoft doc last updated: unknown

Manage deny assignments.

Subgroups and commands: `az_role_deny-assignment_create`, `az_role_deny-assignment_delete`, `az_role_deny-assignment_list`, `az_role_deny-assignment_show`

## az role deny-assignment create

Create a user-assigned deny assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--actions` — Space-separated list of actions to deny, e.g. "Microsoft.Authorization/roleAssignments/write". Note: read actions (*/read) are not permitted for user-assigned deny assignments.
- `--assignment-name` — A GUID for the deny assignment. If omitted, a new GUID is generated.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — Description of the deny assignment.
- `--exclude-principal-ids` — Space-separated list of principal object IDs to exclude from the deny. Required when no --principal-object-id is specified (Everyone mode). Optional when --principal-object-id is specified.
- `--exclude-principal-types` — Space-separated list of principal types corresponding to --exclude-principal-ids. Accepted values: User, Group, ServicePrincipal.
- `--name -n` — The display name of the deny assignment.
- `--not-actions` — Space-separated list of actions to exclude from the deny.
- `--principal-object-id` — The object ID of a specific User or ServicePrincipal to deny. If omitted, the deny assignment applies to Everyone (all principals) and --exclude-principal-ids is required. Group principals are not permitted.
- `--principal-type` — The type of the principal specified by --principal-object-id. Required when --principal-object-id is provided. Accepted values: User, ServicePrincipal.
- `--scope` — Scope at which the deny assignment applies. For example, /subscriptions/00000000-0000-0000-0000-000000000000 or /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup.

*Create a deny assignment blocking role assignment writes for everyone, excluding a service principal.*
```azurecli
az role deny-assignment create --name "Block role assignment changes" --scope /subscriptions/00000000-0000-0000-0000-000000000000 --actions "Microsoft.Authorization/roleAssignments/write" "Microsoft.Authorization/roleAssignments/delete" --exclude-principal-ids 00000000-0000-0000-0000-000000000001 --exclude-principal-types ServicePrincipal
```

*Create a deny assignment targeting a specific user.*
```azurecli
az role deny-assignment create --name "Deny resource deletion for user" --scope /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup --actions "*/delete" --principal-object-id 00000000-0000-0000-0000-000000000001 --principal-type User
```

*Create a deny assignment targeting a specific service principal with exclusions.*
```azurecli
az role deny-assignment create --name "Deny write actions for app" --scope /subscriptions/00000000-0000-0000-0000-000000000000 --actions "*/write" --principal-object-id 00000000-0000-0000-0000-000000000001 --principal-type ServicePrincipal --exclude-principal-ids 00000000-0000-0000-0000-000000000002 --exclude-principal-types ServicePrincipal --description "Block write operations for this application"
```

## az role deny-assignment delete

Delete a user-assigned deny assignment.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — The fully qualified ID of the deny assignment to delete.
- `--name -n` — The name (GUID) of the deny assignment to delete.
- `--scope` — Scope at which the deny assignment applies. For example, /subscriptions/00000000-0000-0000-0000-000000000000 or /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a deny assignment by its fully qualified ID.*
```azurecli
az role deny-assignment delete --id /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Authorization/denyAssignments/00000000-0000-0000-0000-000000000001
```

*Delete a deny assignment by name and scope.*
```azurecli
az role deny-assignment delete --name 00000000-0000-0000-0000-000000000001 --scope /subscriptions/00000000-0000-0000-0000-000000000000
```

## az role deny-assignment list

List deny assignments.

**Optional parameters**

- `--filter` — OData filter expression to apply. For example, "atScope()" to list at the current scope, or "gdprExportPrincipalId eq '{objectId}'" to list for a specific principal.
- `--scope` — Scope at which the deny assignment applies. For example, /subscriptions/00000000-0000-0000-0000-000000000000 or /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup.

*List deny assignments at the subscription scope.*
```azurecli
az role deny-assignment list --scope /subscriptions/00000000-0000-0000-0000-000000000000
```

*List all deny assignments in the current subscription.*
```azurecli
az role deny-assignment list
```

*List deny assignments at a resource group scope.*
```azurecli
az role deny-assignment list --scope /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup
```

## az role deny-assignment show

Get a deny assignment.

**Optional parameters**

- `--id` — The fully qualified ID of the deny assignment including scope, e.g. /subscriptions/{id}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId}.
- `--name -n` — The name (GUID) of the deny assignment.
- `--scope` — Scope at which the deny assignment applies. For example, /subscriptions/00000000-0000-0000-0000-000000000000 or /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup.

*Show a deny assignment by its fully qualified ID.*
```azurecli
az role deny-assignment show --id /subscriptions/00000000-0000-0000-0000-000000000000/providers/Microsoft.Authorization/denyAssignments/00000000-0000-0000-0000-000000000001
```

*Show a deny assignment by name and scope.*
```azurecli
az role deny-assignment show --name 00000000-0000-0000-0000-000000000001 --scope /subscriptions/00000000-0000-0000-0000-000000000000
```
