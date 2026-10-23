# az keyvault private-endpoint-connection

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/private-endpoint-connection  
> Microsoft doc last updated: unknown

Manage vault/HSM private endpoint connections.

Subgroups and commands: `az_keyvault_private-endpoint-connection_approve`, `az_keyvault_private-endpoint-connection_delete`, `az_keyvault_private-endpoint-connection_list`, `az_keyvault_private-endpoint-connection_reject`, `az_keyvault_private-endpoint-connection_show`, `az_keyvault_private-endpoint-connection_wait`

## az keyvault private-endpoint-connection approve

Approve a private endpoint connection request for a Key Vault/HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — Comments for the approve operation.
- `--hsm-name` — Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them).
- `--id` — The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
- `--name -n` — The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Name of resource group.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

*Approve a private endpoint connection request for a Key Vault by ID.*
```azurecli
az keyvault private-endpoint-connection approve --id "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myrg/providers/Microsoft.KeyVault/vaults/mykv/privateEndpointConnections/mykv.00000000-0000-0000-0000-000000000000"
```

*Approve a private endpoint connection request for a Key Vault by ID.*
```azurecli
id = (az keyvault show -n mykv --query "privateEndpointConnections[0].id")
az keyvault private-endpoint-connection approve --id $id
```

*Approve a private endpoint connection request for a Key Vault using vault name and connection name.*
```azurecli
az keyvault private-endpoint-connection approve -g myrg --vault-name mykv --name myconnection
```

*Approve a private endpoint connection request for a Key Vault using vault name and connection name.*
```azurecli
name = (az keyvault show -n mykv --query "privateEndpointConnections[0].name")
az keyvault private-endpoint-connection approve -g myrg --vault-name mykv --name $name
```

*Approve a private endpoint connection request for a HSM using hsm name and connection name.*
```azurecli
az keyvault private-endpoint-connection approve -g myrg --hsm-name myhsm --name myconnection
```

## az keyvault private-endpoint-connection delete

Delete the specified private endpoint connection associated with a Key Vault/HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--hsm-name` — Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them).
- `--id` — The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
- `--name -n` — The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Name of resource group.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

*Delete a private endpoint connection request for a Key Vault by ID.*
```azurecli
az keyvault private-endpoint-connection delete --id "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myrg/providers/Microsoft.KeyVault/vaults/mykv/privateEndpointConnections/mykv.00000000-0000-0000-0000-000000000000"
```

*Delete a private endpoint connection request for a Key Vault by ID.*
```azurecli
id = (az keyvault show -n mykv --query "privateEndpointConnections[0].id")
az keyvault private-endpoint-connection delete --id $id
```

*Delete a private endpoint connection request for a Key Vault using vault name and connection name.*
```azurecli
az keyvault private-endpoint-connection delete -g myrg --vault-name mykv --name myconnection
```

*Delete a private endpoint connection request for a Key Vault using vault name and connection name.*
```azurecli
name = (az keyvault show -n mykv --query "privateEndpointConnections[0].name")
az keyvault private-endpoint-connection delete -g myrg --vault-name mykv --name $name
```

*Delete a private endpoint connection request for a HSM using hsm name and connection name.*
```azurecli
az keyvault private-endpoint-connection delete -g myrg --hsm-name myhsm --name myconnection
```

## az keyvault private-endpoint-connection list

List all private endpoint connections associated with a HSM.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--resource-group -g` — Name of resource group.

*List all private endpoint connections associated with a HSM using hsm name.*
```azurecli
az keyvault private-endpoint-connection list -g myrg --hsm-name myhsm
```

## az keyvault private-endpoint-connection reject

Reject a private endpoint connection request for a Key Vault/HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--description` — Comments for the reject operation.
- `--hsm-name` — Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them).
- `--id` — The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
- `--name -n` — The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Name of resource group.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

*Reject a private endpoint connection request for a Key Vault by ID.*
```azurecli
az keyvault private-endpoint-connection reject --id "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myrg/providers/Microsoft.KeyVault/vaults/mykv/privateEndpointConnections/mykv.00000000-0000-0000-0000-000000000000"
```

*Reject a private endpoint connection request for a Key Vault by ID.*
```azurecli
id = (az keyvault show -n mykv --query "privateEndpointConnections[0].id")
az keyvault private-endpoint-connection reject --id $id
```

*Reject a private endpoint connection request for a Key Vault using vault name and connection name.*
```azurecli
az keyvault private-endpoint-connection reject -g myrg --vault-name mykv --name myconnection
```

*Reject a private endpoint connection request for a Key Vault using vault name and connection name.*
```azurecli
name = (az keyvault show -n mykv --query "privateEndpointConnections[0].name")
az keyvault private-endpoint-connection reject -g myrg --vault-name mystorageaccount --name $name
```

*Reject a private endpoint connection request for a HSM using hsm name and connection name.*
```azurecli
az keyvault private-endpoint-connection reject -g myrg --hsm-name myhsm --name myconnection
```

## az keyvault private-endpoint-connection show

Show details of a private endpoint connection associated with a Key Vault/HSM.

**Optional parameters**

- `--hsm-name` — Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them).
- `--id` — The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
- `--name -n` — The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified.
- `--resource-group -g` — Name of resource group.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

*Show details of a private endpoint connection request for a Key Vault by ID.*
```azurecli
az keyvault private-endpoint-connection show --id "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myrg/providers/Microsoft.KeyVault/vaults/mykv/privateEndpointConnections/mykv.00000000-0000-0000-0000-000000000000"
```

*Show details of a private endpoint connection request for a Key Vault by ID.*
```azurecli
id = (az keyvault show -n mykv --query "privateEndpointConnections[0].id")
az keyvault private-endpoint-connection show --id $id
```

*Show details of a private endpoint connection request for a Key Vault using vault name and connection name.*
```azurecli
az keyvault private-endpoint-connection show -g myrg --vault-name mykv --name myconnection
```

*Show details of a private endpoint connection request for a Key Vault using vault name and connection name.*
```azurecli
name = (az keyvault show -n mykv --query "privateEndpointConnections[0].name")
az keyvault private-endpoint-connection show -g myrg --vault-name mykv --name $name
```

## az keyvault private-endpoint-connection wait

Place the CLI in a waiting state until a condition of the private endpoint connection is met.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--hsm-name` — Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them).
- `--id` — The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
- `--interval` — Polling interval in seconds. Default: 30.
- `--name -n` — The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified.
- `--resource-group -g` — Name of resource group.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.
- `--vault-name` — Name of the Key Vault. Required if --id is not specified.

*Pause CLI until the private endpoint connection is approved/rejected by ID.*
```azurecli
az keyvault private-endpoint-connection wait --id "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myrg/providers/Microsoft.KeyVault/vaults/mykv/privateEndpointConnections/mykv.00000000-0000-0000-0000-000000000000" --created
```

*Pause CLI until the private endpoint connection is approved/rejected using vault name and connection name.*
```azurecli
az keyvault private-endpoint-connection wait -g myrg --vault-name mykv --name myconnection --created
```
