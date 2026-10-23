# az keyvault role definition

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/role/definition  
> Microsoft doc last updated: unknown

Manage role definitions.

Subgroups and commands: `az_keyvault_role_definition_create`, `az_keyvault_role_definition_delete`, `az_keyvault_role_definition_list`, `az_keyvault_role_definition_show`, `az_keyvault_role_definition_update`

## az keyvault role definition create

Create a custom role definition.

**Required parameters**

- `--hsm-name` — Name of the HSM.
- `--role-definition` — Description of a role as JSON, or a path to a file containing a JSON description.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Create a role by a JSON string.*
```azurecli
az keyvault role definition create --hsm-name MyHSM --role-definition '{
    "roleName": "My Custom Role",
    "description": "The description of the custom rule.",
    "actions": [],
    "notActions": [],
    "dataActions": [
        "Microsoft.KeyVault/managedHsm/keys/read/action"
    ],
    "notDataActions": []
}'
```

*Create a role from a file containing a JSON description.*
```azurecli
az keyvault role definition create --hsm-name MyHSM --role-definition @keyvault-role.json
```

## az keyvault role definition delete

Delete a role definition.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--name -n` — The role definition name. This is a GUID in the "name" property of a role definition.
- `--role-id` — The role definition ID.

## az keyvault role definition list

List role definitions.

**Optional parameters**

- `--custom-role-only` — Only show custom role definitions. Default: False.
- `--hsm-name` — Name of the HSM.
- `--scope` — Scope at which the role assignment or definition applies to, e.g., "/" or "/keys" or "/keys/{keyname}".

## az keyvault role definition show

Show the details of a role definition.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--name -n` — The role definition name. This is a GUID in the "name" property of a role definition.
- `--role-id` — The role definition ID.

## az keyvault role definition update

Update a role definition.

**Required parameters**

- `--hsm-name` — Name of the HSM.
- `--role-definition` — Description of a role as JSON, or a path to a file containing a JSON description.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Update a role by a JSON string.*
```azurecli
az keyvault role definition update --hsm-name MyHSM --role-definition '{
    "roleName": "My Custom Role",
    "name": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "id": "Microsoft.KeyVault/providers/Microsoft.Authorization/roleDefinitions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "description": "The description of the custom rule.",
    "actions": [],
    "notActions": [],
    "dataActions": [
        "Microsoft.KeyVault/managedHsm/keys/read/action",
        "Microsoft.KeyVault/managedHsm/keys/write/action",
        "Microsoft.KeyVault/managedHsm/keys/backup/action",
        "Microsoft.KeyVault/managedHsm/keys/create"
    ],
    "notDataActions": []
}'
```

*Update a role from a file containing a JSON description.*
```azurecli
az keyvault role definition update --hsm-name MyHSM --role-definition @keyvault-role.json
```
