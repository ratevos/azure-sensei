# az ad sp credential

> Source: https://learn.microsoft.com/en-us/cli/azure/ad/sp/credential  
> Microsoft doc last updated: unknown

Manage a service principal's password or certificate credentials.

Subgroups and commands: `az_ad_sp_credential_delete`, `az_ad_sp_credential_list`, `az_ad_sp_credential_reset`

## az ad sp credential delete

Delete a service principal's password or certificate credentials.

**Required parameters**

- `--id` — Service principal name, or object id.
- `--key-id` — Credential key id.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--cert` — Operate on certificate credentials. Default: False.
- `--change-reference` — The related change reference ID for this resource operation.

*Delete a service principal's password credential*
```azurecli
az ad sp credential delete --id 00000000-0000-0000-0000-000000000000 --key-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

*Delete a service principal's certificate credential*
```azurecli
az ad sp credential delete --id 00000000-0000-0000-0000-000000000000 --key-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --cert
```

## az ad sp credential list

List a service principal's password or certificate credential metadata. (The content of the password or certificate credential is not retrievable.).

**Required parameters**

- `--id` — Service principal name, or object id.

**Optional parameters**

- `--cert` — Operate on certificate credentials. Default: False.

*List a service principal's password credentials*
```azurecli
az ad sp credential list --id 00000000-0000-0000-0000-000000000000
```

*List a service principal's certificate credentials*
```azurecli
az ad sp credential list --id 00000000-0000-0000-0000-000000000000 --cert
```

## az ad sp credential reset

Reset a service principal's password or certificate credentials.

**Required parameters**

- `--id` — Service principal name, or object id.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--append` — Append the new credential instead of overwriting. Default: False.
- `--cert` — Certificate to use for credentials. When used with `--keyvault,`, indicates the name of the cert to use or create. Otherwise, supply a PEM or DER formatted public certificate string. Use `@{path}` to load from a file. Do not include the private key.
- `--change-reference` — The related change reference ID for this resource operation.
- `--create-cert` — Create a self-signed certificate to use for the credential. Only the current OS user has read/write permission to this certificate. Use with `--keyvault` to create the certificate in Key Vault. Otherwise, a certificate will be created locally. Default: False.
- `--display-name` — Friendly name for the credential.
- `--end-date` — Finer grain of expiry time if '--years' is insufficient, e.g. '2020-12-31T11:59:59+00:00' or '2299-12-31'.
- `--keyvault` — Name or ID of a KeyVault to use for creating or retrieving certificates.
- `--years` — Number of years for which the credentials will be valid. Default: 1 year.

*Reset a service principal's credential with a password*
```azurecli
az ad sp credential reset --id 00000000-0000-0000-0000-000000000000
```

*Reset a service principal's credential with a new self-signed certificate*
```azurecli
az ad sp credential reset --id 00000000-0000-0000-0000-000000000000 --create-cert
```

*Append a certificate to the service principal with the certificate string.*
```azurecli
az ad sp credential reset --id 00000000-0000-0000-0000-000000000000 --cert "MIICoT..." --append
```

*Append a certificate to the service principal with the certificate file.*
```azurecli
az ad sp credential reset --id 00000000-0000-0000-0000-000000000000 --cert "@~/cert.pem" --append
`cert.pem` contains the following content
-----BEGIN CERTIFICATE-----  <<< this line is optional
MIICoT...
-----END CERTIFICATE-----    <<< this line is optional
```
