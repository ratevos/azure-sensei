# az keyvault secret

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/secret  
> Microsoft doc last updated: unknown

Manage secrets.

Subgroups and commands: `az_keyvault_secret_backup`, `az_keyvault_secret_delete`, `az_keyvault_secret_download`, `az_keyvault_secret_list`, `az_keyvault_secret_list-deleted`, `az_keyvault_secret_list-versions`, `az_keyvault_secret_purge`, `az_keyvault_secret_recover`, `az_keyvault_secret_restore`, `az_keyvault_secret_set`, `az_keyvault_secret_set-attributes`, `az_keyvault_secret_show`, `az_keyvault_secret_show-deleted`

## az keyvault secret backup

Backs up the specified secret.

**Required parameters**

- `--file -f` — File to receive the secret contents.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — Id of the secret. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault secret delete  (Deprecated)

Delete all versions of a secret.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — Id of the secret. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault secret download

Download a secret from a KeyVault.

**Required parameters**

- `--file -f` — File to receive the secret contents.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--encoding -e` — Encoding of the secret. By default, will look for the 'file-encoding' tag on the secret. Otherwise will assume 'utf-8'.
- `--id` — Id of the secret. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--overwrite` — Overwrite the file if it exists. Default: False.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.
- `--version -v` — The secret version. If omitted, uses the latest version.

## az keyvault secret list

List secrets in a specified key vault.

**Optional parameters**

- `--id` — Full URI of the Vault. If specified all other 'Id' arguments should be omitted.
- `--include-managed` — Include managed secrets. Default: false. Default: False.
- `--maxresults` — Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault secret list-deleted

Lists deleted secrets for the specified vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — Full URI of the Vault. If specified all other 'Id' arguments should be omitted.
- `--maxresults` — Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault secret list-versions

List all versions of the specified secret.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — Id of the secret. If specified all other 'Id' arguments should be omitted.
- `--maxresults` — Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault secret purge

Permanently deletes the specified secret.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — The recovery id of the secret. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--vault-name` — Name of the Vault. Required if --id is not specified.

## az keyvault secret recover

Recovers the deleted secret to the latest version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — The recovery id of the secret. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--vault-name` — Name of the Vault. Required if --id is not specified.

## az keyvault secret restore

Restores a backed up secret to a vault.

**Required parameters**

- `--file -f` — File to receive the secret contents.
- `--vault-name` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az keyvault secret set

Create a secret (if one doesn't exist) or update a secret in a KeyVault.

**Required parameters**

- `--name -n` — Name of the secret.
- `--vault-name` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--content-type --description` — Description of the secret contents (e.g. password, connection string, etc).
- `--disabled` — Create secret in disabled state.
- `--encoding -e` — Source file encoding. The value is saved as a tag (`file-encoding=<val>`) and used during download to automatically encode the resulting file. Default: utf-8.
- `--expires` — Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
- `--file -f` — Source file for secret. Use in conjunction with '--encoding'.
- `--not-before` — Secret not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--value` — Plain text secret value. Cannot be used with '--file' or '--encoding'.

*Create a secret (if one doesn't exist) or update a secret in a KeyVault.*
```azurecli
az keyvault secret set --name MySecretName --vault-name MyKeyVault --value MyVault
```

*Create a secret (if one doesn't exist) or update a secret in a KeyVault through a file.*
```azurecli
az keyvault secret set --name MySecretName --vault-name MyKeyVault --file /path/to/file --encoding MyEncoding
```

## az keyvault secret set-attributes

Updates the attributes associated with a specified secret in a given key vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--content-type` — Type of the secret value such as a password.
- `--enabled` — Enable the secret.
- `--expires` — Expiration UTC datetime (Y-m-d'T'H:M:S'Z').
- `--id` — Id of the secret. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--not-before` — Secret not usable before the provided UTC datetime (Y-m-d'T'H:M:S'Z').
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.
- `--version -v` — The secret version. If omitted, uses the latest version.

## az keyvault secret show

Get a specified secret from a given key vault.

**Optional parameters**

- `--id` — Id of the secret. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.
- `--version -v` — The secret version. If omitted, uses the latest version.

## az keyvault secret show-deleted

Gets the specified deleted secret.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — The recovery id of the secret. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the secret. Required if --id is not specified.
- `--vault-name` — Name of the Vault. Required if --id is not specified.
