# az keyvault security-domain

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/security-domain  
> Microsoft doc last updated: unknown

Manage security domain operations.

Subgroups and commands: `az_keyvault_security-domain_download`, `az_keyvault_security-domain_init-recovery`, `az_keyvault_security-domain_restore-blob`, `az_keyvault_security-domain_upload`, `az_keyvault_security-domain_wait`

## az keyvault security-domain download

Download the security domain file from the HSM.

**Required parameters**

- `--sd-quorum` — The minimum number of shares required to decrypt the security domain for recovery.
- `--sd-wrapping-keys` — Space-separated file paths to PEM files containing public keys.
- `--security-domain-file` — Path to a file where the JSON blob returned by this command is stored.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Security domain download (N=3, M=2).*
```azurecli
az keyvault security-domain download --hsm-name MyHSM --security-domain-file "{SD_FILE_NAME}" --sd-quorum 2 --sd-wrapping-keys "{PEM_PUBLIC_KEY1_FILE_NAME}" "{PEM_PUBLIC_KEY2_FILE_NAME}" "{PEM_PUBLIC_KEY3_FILE_NAME}"
```

## az keyvault security-domain init-recovery

Retrieve the exchange key of the HSM.

**Required parameters**

- `--sd-exchange-key` — Local file path to store the exported key.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.

*Retrieve the exchange key and store it.*
```azurecli
az keyvault security-domain init-recovery --hsm-name MyHSM --sd-exchange-key "{PATH_TO_RESTORE}"
```

## az keyvault security-domain restore-blob

Enable to decrypt and encrypt security domain file as blob. Can be run in offline environment, before file is uploaded to HSM using security-domain upload.

**Required parameters**

- `--sd-exchange-key` — The exchange key for security domain.
- `--sd-file` — This file contains security domain encrypted using SD Exchange file downloaded in security-domain init-recovery command.
- `--sd-file-restore-blob` — Local file path to store the security domain encrypted with the exchange key.
- `--sd-wrapping-keys` — Space-separated file paths to PEM files containing private keys.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--passwords` — Space-separated password list for --sd-wrapping-keys. CLI will match them in order. Can be omitted if your keys are without password protection.

*Security domain restore blob.*
```azurecli
az keyvault security-domain restore-blob --sd-file "{SD_TRANSFER_FILE}" --sd-exchange-key "{PEM_FILE_NAME}" --sd-wrapping-keys "{PEM_PRIVATE_KEY1_FILE_NAME}" "{PEM_PRIVATE_KEY2_FILE_NAME}" --sd-file-restore-blob "{SD_TRANSFER_FILE_RESTORE_BLOB}"
```

## az keyvault security-domain upload

Start to restore the HSM.

**Required parameters**

- `--sd-file` — This file contains security domain encrypted using SD Exchange file downloaded in security-domain init-recovery command.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--passwords` — Space-separated password list for --sd-wrapping-keys. CLI will match them in order. Can be omitted if your keys are without password protection.
- `--restore-blob` — Indicator if blob is already restored. Default: False.
- `--sd-exchange-key` — The exchange key for security domain.
- `--sd-wrapping-keys` — Space-separated file paths to PEM files containing private keys.

*Security domain upload (M=2).*
```azurecli
az keyvault security-domain upload --hsm-name MyHSM --sd-file "{SD_TRANSFER_FILE}" --sd-exchange-key "{PEM_FILE_NAME}" --sd-wrapping-keys "{PEM_PRIVATE_KEY1_FILE_NAME}" "{PEM_PRIVATE_KEY2_FILE_NAME}"
```

*Security domain upload, in which sd_file is already restored using keyvault security-domain restore-blob command*
```azurecli
az keyvault security-domain upload --hsm-name MyHSM --sd-file "{SD_TRANSFER_FILE}" --restore-blob
```

## az keyvault security-domain wait

Place the CLI in a waiting state until HSM security domain operation is finished.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Can be omitted if --id is specified.
- `--id` — Full URI of the HSM.
- `--target-operation` — Target operation that needs waiting. Default: upload.

*Pause CLI until the security domain operation is finished.*
```azurecli
az keyvault security-domain wait --hsm-name MyHSM
```
