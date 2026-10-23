# az aks approuting

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/approuting  
> Microsoft doc last updated: unknown

Commands to manage App Routing addon.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_approuting_defaultdomain`, `az_aks_approuting_defaultdomain_show`, `az_aks_approuting_disable`, `az_aks_approuting_disable(aks-preview)`, `az_aks_approuting_enable`, `az_aks_approuting_enable(aks-preview)`, `az_aks_approuting_gateway`, `az_aks_approuting_gateway_istio`, `az_aks_approuting_gateway_istio_disable`, `az_aks_approuting_gateway_istio_disable(aks-preview)`, `az_aks_approuting_gateway_istio_enable`, `az_aks_approuting_gateway_istio_enable(aks-preview)`, `az_aks_approuting_update`, `az_aks_approuting_update(aks-preview)`, `az_aks_approuting_zone`, `az_aks_approuting_zone_add`, `az_aks_approuting_zone_add(aks-preview)`, `az_aks_approuting_zone_delete`, `az_aks_approuting_zone_delete(aks-preview)`, `az_aks_approuting_zone_list`, `az_aks_approuting_zone_list(aks-preview)`, `az_aks_approuting_zone_update`, `az_aks_approuting_zone_update(aks-preview)`

## az aks approuting disable

Disable App Routing addon.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks approuting disable  (extension: aks-preview etc.)

Disable App Routing addon.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks approuting enable

Enable App Routing.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--attach-kv` — Attach a keyvault id to access secrets and certificates.
- `--change-reference` — The related change reference ID for this resource operation.
- `--enable-kv` — Enable the keyvault secrets provider. Default: False.
- `--nginx` — Configure default NginxIngressController resource.

## az aks approuting enable  (extension: aks-preview etc.)

Enable App Routing.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--attach-kv` — Attach a keyvault id to access secrets and certificates.
- `--change-reference` — The related change reference ID for this resource operation.
- `--enable-default-domain` — Enable default domain for Application Routing addon. Default: False.
- `--enable-kv` — Enable the keyvault secrets provider. Default: False.
- `--nginx` — Configure default NginxIngressController resource.

## az aks approuting update

Update App Routing addon.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--attach-kv` — Attach a keyvault id to access secrets and certificates.
- `--change-reference` — The related change reference ID for this resource operation.
- `--enable-kv` — Enable the keyvault secrets provider addon. Default: False.
- `--nginx` — Configure default NginxIngressController resource.

## az aks approuting update  (extension: aks-preview etc.)

Update App Routing addon.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--attach-kv` — Attach a keyvault id to access secrets and certificates.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disable-default-domain` — Disable default domain for Application Routing addon. Default: False.
- `--enable-default-domain` — Enable default domain for Application Routing addon. Default: False.
- `--enable-kv` — Enable the keyvault secrets provider addon. Default: False.
- `--nginx` — Configure default NginxIngressController resource.
