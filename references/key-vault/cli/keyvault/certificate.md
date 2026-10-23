# az keyvault certificate

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/certificate  
> Microsoft doc last updated: unknown

Manage certificates.

Subgroups and commands: `az_keyvault_certificate_backup`, `az_keyvault_certificate_contact`, `az_keyvault_certificate_contact_add`, `az_keyvault_certificate_contact_delete`, `az_keyvault_certificate_contact_list`, `az_keyvault_certificate_create`, `az_keyvault_certificate_delete`, `az_keyvault_certificate_download`, `az_keyvault_certificate_get-default-policy`, `az_keyvault_certificate_import`, `az_keyvault_certificate_issuer`, `az_keyvault_certificate_issuer_admin`, `az_keyvault_certificate_issuer_admin_add`, `az_keyvault_certificate_issuer_admin_delete`, `az_keyvault_certificate_issuer_admin_list`, `az_keyvault_certificate_issuer_create`, `az_keyvault_certificate_issuer_delete`, `az_keyvault_certificate_issuer_list`, `az_keyvault_certificate_issuer_show`, `az_keyvault_certificate_issuer_update`, `az_keyvault_certificate_list`, `az_keyvault_certificate_list-deleted`, `az_keyvault_certificate_list-versions`, `az_keyvault_certificate_pending`, `az_keyvault_certificate_pending_delete`, `az_keyvault_certificate_pending_merge`, `az_keyvault_certificate_pending_show`, `az_keyvault_certificate_purge`, `az_keyvault_certificate_recover`, `az_keyvault_certificate_restore`, `az_keyvault_certificate_set-attributes`, `az_keyvault_certificate_show`, `az_keyvault_certificate_show-deleted`

## az keyvault certificate backup

Backs up the specified certificate.

**Required parameters**

- `--file -f` — Local file path in which to store certificate backup.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — Id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault certificate create

Create a Key Vault certificate.

**Required parameters**

- `--name -n` — Name of the certificate.
- `--policy -p` — JSON encoded policy definition. Use @{file} to load from a file(e.g. @my_policy.json).
- `--vault-name` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disabled` — Create certificate in disabled state.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--validity` — Number of months the certificate is valid for. Overrides the value specified with --policy/-p.

*Create a self-signed certificate with the default policy and add it to a virtual machine.*
```azurecli
az keyvault certificate create --vault-name vaultname -n cert1 \
  -p "$(az keyvault certificate get-default-policy)"

secrets=$(az keyvault secret list-versions --vault-name vaultname \
  -n cert1 --query "[?attributes.enabled].id" -o tsv)

vm_secrets=$(az vm secret format -s "$secrets")

az vm create -g group-name -n vm-name --admin-username deploy  \
  --image Debian11 --secrets "$vm_secrets"
```

## az keyvault certificate delete  (Deprecated)

Deletes a certificate from a specified key vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — Id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault certificate download

Download the public portion of a Key Vault certificate.

**Required parameters**

- `--file -f` — File to receive the binary certificate contents.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--encoding -e` — Encoding of the certificate. DER will create a binary DER formatted x509 certificate, and PEM will create a base64 PEM x509 certificate. Default: PEM.
- `--id` — Id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.
- `--version -v` — The certificate version. If omitted, uses the latest version.

*Download a certificate as PEM and check its fingerprint in openssl.*
```azurecli
az keyvault certificate download --vault-name vault -n cert-name -f cert.pem && \
openssl x509 -in cert.pem -inform PEM  -noout -sha1 -fingerprint
```

*Download a certificate as DER and check its fingerprint in openssl.*
```azurecli
az keyvault certificate download --vault-name vault -n cert-name -f cert.crt -e DER && \
openssl x509 -in cert.crt -inform DER  -noout -sha1 -fingerprint
```

## az keyvault certificate get-default-policy

Get the default policy for self-signed certificates.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--scaffold` — Create a fully formed policy structure with default values. Default: False.

*Create a self-signed certificate with the default policy*
```azurecli
az keyvault certificate create --vault-name vaultname -n cert1 \
  -p "$(az keyvault certificate get-default-policy)"
```

## az keyvault certificate import

Import a certificate into KeyVault.

**Required parameters**

- `--file -f` — PKCS12 file or PEM file containing the certificate and private key.
- `--name -n` — Name of the certificate.
- `--vault-name` — Name of the Vault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disabled` — Import the certificate in disabled state.
- `--password` — If the private key in certificate is encrypted, the password used for encryption.
- `--policy -p` — JSON encoded policy definition. Use @{file} to load from a file(e.g. @my_policy.json).
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.

*Create a service principal with a certificate, add the certificate to Key Vault and provision a VM with that certificate.*
```azurecli
service_principal=$(az ad sp create-for-rbac --create-cert)

cert_file=$(echo $service_principal | jq .fileWithCertAndPrivateKey -r)

az keyvault create -g my-group -n vaultname

az keyvault certificate import --vault-name vaultname -n cert_name -f cert_file

secrets=$(az keyvault secret list-versions --vault-name vaultname \
  -n cert1 --query "[?attributes.enabled].id" -o tsv)

vm_secrets=$(az vm secret format -s "$secrets")

az vm create -g group-name -n vm-name --admin-username deploy  \
  --image Debian11 --secrets "$vm_secrets"
```

## az keyvault certificate list

List certificates in a specified key vault.

**Optional parameters**

- `--id` — Full URI of the Vault. If specified all other 'Id' arguments should be omitted.
- `--include-pending` — Specifies whether to include certificates which are not completely provisioned.
- `--maxresults` — Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault certificate list-deleted

Lists the currently-recoverable deleted certificates.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — Full URI of the Vault. If specified all other 'Id' arguments should be omitted.
- `--include-pending` — Specifies whether to include certificates which are not completely provisioned.
- `--maxresults` — Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault certificate list-versions

List the versions of a certificate.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — Id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--maxresults` — Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

## az keyvault certificate purge

Permanently deletes the specified deleted certificate.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — The recovery id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--vault-name` — Name of the Vault. Required if --id is not specified.

## az keyvault certificate recover

Recover a deleted certificate to its latest version.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — The recovery id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--vault-name` — Name of the Vault. Required if --id is not specified.

## az keyvault certificate restore

Restores a backed up certificate to a vault.

**Required parameters**

- `--file -f` — Local certificate backup from which to restore certificate.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--vault-name` — Name of the Key Vault.

## az keyvault certificate set-attributes

Updates the specified attributes associated with the given certificate.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--enabled` — Enable the certificate.
- `--id` — Id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--policy -p` — JSON encoded policy definition. Use @{file} to load from a file(e.g. @my_policy.json).
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.
- `--version -v` — The certificate version. If omitted, uses the latest version.

## az keyvault certificate show

Gets information about a certificate.

**Optional parameters**

- `--id` — Id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.
- `--version -v` — The certificate version. If omitted, uses the latest version.

## az keyvault certificate show-deleted

Get a deleted certificate.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--id` — The recovery id of the certificate. If specified all other 'Id' arguments should be omitted.
- `--name -n` — Name of the certificate. Required if --id is not specified.
- `--vault-name` — Name of the Vault. Required if --id is not specified.
