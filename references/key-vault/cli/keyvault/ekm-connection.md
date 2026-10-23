# az keyvault ekm-connection

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/ekm-connection  
> Microsoft doc last updated: unknown

Manage External Key Manager (EKM) connection for a Managed HSM.

Subgroups and commands: `az_keyvault_ekm-connection_certificate`, `az_keyvault_ekm-connection_certificate_show`, `az_keyvault_ekm-connection_check`, `az_keyvault_ekm-connection_create`, `az_keyvault_ekm-connection_delete`, `az_keyvault_ekm-connection_show`, `az_keyvault_ekm-connection_update`

## az keyvault ekm-connection check

Check connectivity and authentication with the EKM proxy.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.

## az keyvault ekm-connection create

Create the EKM connection.

**Required parameters**

- `--host` — EKM proxy host (FQDN or FQDN:port). If port is omitted, 443 is assumed.
- `--server-ca-certificate` — Path(s) to server CA certificate(s) in PEM or DER format. Pass a single file containing a PEM chain (multiple certificate blocks), or multiple space-separated file paths (each PEM or DER).

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.
- `--path-prefix` — Optional path prefix to append to EKM proxy requests. Must start with "/".
- `--server-cn --server-subject-common-name` — Optional expected Common Name (CN) for the EKM proxy server certificate.

## az keyvault ekm-connection delete

Delete the EKM connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.

## az keyvault ekm-connection show

Show the EKM connection.

**Optional parameters**

- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.

## az keyvault ekm-connection update

Update the EKM connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--host` — EKM proxy host (FQDN or FQDN:port). If port is omitted, 443 is assumed.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.
- `--path-prefix` — Optional path prefix to append to EKM proxy requests. Must start with "/".
- `--server-ca-certificate` — Path(s) to server CA certificate(s) in PEM or DER format. Pass a single file containing a PEM chain (multiple certificate blocks), or multiple space-separated file paths (each PEM or DER).
- `--server-cn --server-subject-common-name` — Optional expected Common Name (CN) for the EKM proxy server certificate.
