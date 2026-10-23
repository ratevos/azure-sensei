# az keyvault region

> Source: https://learn.microsoft.com/en-us/cli/azure/keyvault/region  
> Microsoft doc last updated: unknown

Manage MHSM multi-regions.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_keyvault_region_add`, `az_keyvault_region_add(keyvault-preview)`, `az_keyvault_region_list`, `az_keyvault_region_list(keyvault-preview)`, `az_keyvault_region_remove`, `az_keyvault_region_remove(keyvault-preview)`, `az_keyvault_region_wait`, `az_keyvault_region_wait(keyvault-preview)`

## az keyvault region add

Add regions for the managed HSM Pool.

**Required parameters**

- `--hsm-name` — Name of the HSM.
- `--region --region-name -r` — The region name.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Name of resource group.

*Add regions for the managed HSM.*
```azurecli
az keyvault region add --region-name westus2 --hsm-name myhsm --resource-group myrg
```

## az keyvault region add  (Preview; extension: aks-preview etc.)

Add regions for the managed HSM Pool.

**Required parameters**

- `--hsm-name` — Name of the HSM.
- `--region --region-name -r` — The region name.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Proceed only if Key Vault belongs to the specified resource group.

*Add regions for the managed HSM.*
```azurecli
az keyvault region add --region-name westus2 --hsm-name myhsm --resource-group myrg
```

## az keyvault region list

Get regions information associated with the managed HSM Pool.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--resource-group -g` — Name of resource group.

## az keyvault region list  (Preview; extension: aks-preview etc.)

Get regions information associated with the managed HSM Pool.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--resource-group -g` — Proceed only if Key Vault belongs to the specified resource group.

## az keyvault region remove

Remove regions for the managed HSM Pool.

**Required parameters**

- `--hsm-name` — Name of the HSM.
- `--region --region-name -r` — The region name.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Name of resource group.

*Remove regions for the managed HSM.*
```azurecli
az keyvault region remove --region-name westus2 --hsm-name myhsm --resource-group myrg
```

## az keyvault region remove  (Preview; extension: aks-preview etc.)

Remove regions for the managed HSM Pool.

**Required parameters**

- `--hsm-name` — Name of the HSM.
- `--region --region-name -r` — The region name.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--resource-group -g` — Proceed only if Key Vault belongs to the specified resource group.

*Remove regions for the managed HSM.*
```azurecli
az keyvault region remove --region-name westus2 --hsm-name myhsm --resource-group myrg
```

## az keyvault region wait

Place the CLI in a waiting state until a condition of the HSM is met.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--resource-group -g` — Name of resource group.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Pause CLI until the regions are updated.*
```azurecli
az keyvault region wait --hsm-name myhsm --updated
```

## az keyvault region wait  (Preview; extension: aks-preview etc.)

Place the CLI in a waiting state until a condition of the HSM is met.

**Required parameters**

- `--hsm-name` — Name of the HSM.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--resource-group -g` — Proceed only if Key Vault belongs to the specified resource group.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Pause CLI until the regions are updated.*
```azurecli
az keyvault region wait --hsm-name myhsm --updated
```
