# az aksarc vnet

> Source: https://learn.microsoft.com/en-us/cli/azure/aksarc/vnet  
> Microsoft doc last updated: unknown

Manage virtual networks for provisioned clusters.

Subgroups and commands: `az_aksarc_vnet_create`, `az_aksarc_vnet_delete`, `az_aksarc_vnet_list`, `az_aksarc_vnet_show`

## az aksarc vnet create  (extension: aks-preview etc.)

Creates the virtual network.

**Required parameters**

- `--custom-location` — Name or ID of the custom location to use for the virtual network.
- `--name -n` — Name of the virtual network.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--moc-group` — Name of the MOC group containing the MOC network for Azure Local Infrastructure. Default: target-group.
- `--moc-location` — Name of the MOC location containing the MOC group with the network for Azure Local Infrastructure. Default: MocLocation.
- `--moc-vnet-name` — Name of the MOC network for Azure Local Infrastructure.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.

*PutVirtualNetwork*
```azurecli
az aksarc vnet create --name "test-vnet-static" --resource-group "test-arcappliance-resgrp" --custom-location "testcustomlocation" --moc-vnet-name "test-vnet"
```

## az aksarc vnet delete  (extension: aks-preview etc.)

Deletes the virtual network.

**Required parameters**

- `--name -n` — Name of the virtual network.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*DeleteVirtualNetwork*
```azurecli
az aksarc vnet delete --resource-group "test-arcappliance-resgrp" --name "test-vnet-static"
```

## az aksarc vnet list  (extension: aks-preview etc.)

Lists the virtual networks by resource group or subscription.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*ListVirtualNetworkByResourceGroup*
```azurecli
az aksarc vnet list --resource-group "test-arcappliance-resgrp"
```

*ListVirtualNetworkBySubscription*
```azurecli
az aksarc vnet list
```

## az aksarc vnet show  (extension: aks-preview etc.)

Gets the virtual network.

**Required parameters**

- `--name -n` — Name of the virtual network.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*GetVirtualNetwork*
```azurecli
az aksarc vnet show --resource-group "test-arcappliance-resgrp" --name "test-vnet-static"
```
