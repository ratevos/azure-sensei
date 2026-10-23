# az aks trustedaccess rolebinding

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/trustedaccess/rolebinding  
> Microsoft doc last updated: unknown

Commands to manage trusted access role bindings.

Subgroups and commands: `az_aks_trustedaccess_rolebinding_create`, `az_aks_trustedaccess_rolebinding_delete`, `az_aks_trustedaccess_rolebinding_list`, `az_aks_trustedaccess_rolebinding_show`, `az_aks_trustedaccess_rolebinding_update`

## az aks trustedaccess rolebinding create

Create a new trusted access role binding.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — Specify the role binding name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--roles` — Specify the comma-separated roles.
- `--source-resource-id` — Specify the source resource id of the binding.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Create a new trusted access role binding*
```azurecli
az aks trustedaccess rolebinding create -g myResourceGroup --cluster-name myCluster -n bindingName --source-resource-id /subscriptions/0000/resourceGroups/myResourceGroup/providers/Microsoft.Demo/samples --roles Microsoft.Demo/samples/reader,Microsoft.Demo/samples/writer
```

## az aks trustedaccess rolebinding delete

Delete a trusted access role binding according to name.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — Specify the role binding name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks trustedaccess rolebinding list

List all the trusted access role bindings.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks trustedaccess rolebinding show

Get the specific trusted access role binding according to binding name.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — Specify the role binding name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks trustedaccess rolebinding update

Update a trusted access role binding.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — Specify the role binding name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--roles` — Specify the comma-separated roles.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
