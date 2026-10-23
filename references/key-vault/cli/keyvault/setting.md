# az keyvault setting

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/setting  
> Microsoft doc last updated: unknown

Manage MHSM settings.

Subgroups and commands: `az_keyvault_setting_list`, `az_keyvault_setting_show`, `az_keyvault_setting_update`

## az keyvault setting list

Get all settings associated with the managed HSM.

**Optional parameters**

- `--hsm-name` — Name of the HSM.
- `--id` — Full URI of the HSM. If specified all other 'Id' arguments should be omitted.

## az keyvault setting show

Get specific setting associated with the managed HSM.

**Required parameters**

- `--name -n` — Name of the setting.

**Optional parameters**

- `--hsm-name` — Name of the HSM.
- `--id` — Full URI of the HSM. If specified all other 'Id' arguments should be omitted.

*Add "AllowKeyManagementOperationsThroughARM" setting of the managed HSM.*
```azurecli
az keyvault setting show --name AllowKeyManagementOperationsThroughARM --hsm-name myhsm
```

## az keyvault setting update

Update specific setting associated with the managed HSM.

**Required parameters**

- `--name -n` — Name of the setting.
- `--value` — Value of the setting.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM.
- `--id` — Full URI of the HSM. If specified all other 'Id' arguments should be omitted.
- `--setting-type --type` — Type of the setting value.

*Allow key management operations through ARM for the managed HSM.*
```azurecli
az keyvault setting update --name AllowKeyManagementOperationsThroughARM --value true --type boolean --hsm-name myhsm
```
