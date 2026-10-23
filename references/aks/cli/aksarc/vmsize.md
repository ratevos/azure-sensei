# az aksarc vmsize

> Source: https://learn.microsoft.com/en-us/cli/azure/aksarc/vmsize  
> Microsoft doc last updated: unknown

Manage virtual machine SKUs for provisioned clusters.

Subgroups and commands: `az_aksarc_vmsize_list`

## az aksarc vmsize list  (extension: aks-preview etc.)

Lists the supported virtual machine sizes in the specified custom location.

**Required parameters**

- `--custom-location` — Name or ID of the custom location to use for the virtual machine skus.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*VMListSkus*
```azurecli
az aksarc vmsize list -g sample-rg --custom-location sample-cl
```
