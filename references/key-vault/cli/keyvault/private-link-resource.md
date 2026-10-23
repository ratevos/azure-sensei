# az keyvault private-link-resource

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/private-link-resource  
> Microsoft doc last updated: unknown

Manage vault/HSM private link resources.

Subgroups and commands: `az_keyvault_private-link-resource_list`

## az keyvault private-link-resource list

List the private link resources supported for a Key Vault/HSM.

**Optional parameters**

- `--hsm-name` — Name of the HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them).
- `--resource-group -g` — Name of resource group.
- `--vault-name` — Name of the Vault.

*Get the private link resources that need to be created for a Key Vault.*
```azurecli
az keyvault private-link-resource list --vault-name mykv
```

*Get the private link resources that need to be created for a HSM.*
```azurecli
az keyvault private-link-resource list --hsm-name myhsm
```
