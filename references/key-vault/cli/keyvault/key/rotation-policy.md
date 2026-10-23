# az keyvault key rotation-policy

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/key/rotation-policy  
> Microsoft doc last updated: unknown

Manage key's rotation policy.

Subgroups and commands: `az_keyvault_key_rotation-policy_show`, `az_keyvault_key_rotation-policy_update`

## az keyvault key rotation-policy show

Get the rotation policy of a Key Vault key.

**Optional parameters**

- `--hsm-name` — Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them).
- `--id` — Id of the key. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the key. Required if --id is not specified.
- `--vault-name` — Name of the Vault.

## az keyvault key rotation-policy update

Update the rotation policy of a Key Vault key.

**Required parameters**

- `--value` — The rotation policy file definition as JSON, or a path to a file containing JSON policy definition.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them).
- `--id` — Id of the key. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the key. Required if --id is not specified.
- `--vault-name` — Name of the Vault.

*Set rotation policy using json file*
```azurecli
az keyvault key rotation-policy update -n mykey --vault-name mykeyvault --value path/to/policy.json
A valid example for policy.json is:
{
  "lifetimeActions": [
    {
      "trigger": {
        "timeAfterCreate": "P90D", // ISO 8601 duration. For example: 90 days is "P90D", 3 months is "P3M", and 48 hours is "PT48H".
        "timeBeforeExpiry" : null
      },
      "action": {
        "type": "Rotate"
      }
    },
    {
      "trigger": {
        "timeBeforeExpiry" : "P30D" // ISO 8601 duration.
      },
      "action": {
        "type": "Notify"
      }
    }
  ],
  "attributes": {
    "expiryTime": "P2Y" // ISO 8601 duration.
  }
}
```
