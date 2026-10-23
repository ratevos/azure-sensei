# az keyvault certificate pending

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/certificate/pending  
> Microsoft doc last updated: unknown

Manage pending certificate creation operations.

Subgroups and commands: `az_keyvault_certificate_pending_delete`, `az_keyvault_certificate_pending_merge`, `az_keyvault_certificate_pending_show`

## az keyvault certificate pending delete

Deletes the creation operation for a specific certificate.

**Required parameters**

- `--name -n` — Name of the pending certificate.
- `--vault-name` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az keyvault certificate pending merge

Merges a certificate or a certificate chain with a key pair existing on the server.

**Required parameters**

- `--file -f` — File containing the certificate or certificate chain to merge.
- `--name -n` — Name of the pending certificate.
- `--vault-name` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disabled` — Create certificate in disabled state.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.

## az keyvault certificate pending show

Gets the creation operation of a certificate.

**Required parameters**

- `--name -n` — Name of the pending certificate.
- `--vault-name` — Name of the Vault.
