# az keyvault backup

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/backup  
> Microsoft doc last updated: unknown

Manage full HSM backup.

Subgroups and commands: `az_keyvault_backup_start`

## az keyvault backup start

Begin a full backup of the HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--blob-container-name` — Name of Blob Container.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.
- `--storage-account-name` — Name of Azure Storage Account.
- `--storage-container-SAS-token -t` — The SAS token pointing to an Azure Blob storage container.
- `--storage-resource-uri` — Azure Blob storage container Uri. If specified all other 'Storage Id' arguments should be omitted.
- `--use-managed-identity` — If True, Managed HSM will use the configured user-assigned managed identity to authenticate with Azure Storage. Otherwise, a `sas_token` has to be specified.
