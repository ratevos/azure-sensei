# az aks approuting gateway istio

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/approuting/gateway/istio  
> Microsoft doc last updated: unknown

Commands to manage the Istio Gateway API implementation for App Routing.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_approuting_gateway_istio_disable`, `az_aks_approuting_gateway_istio_disable(aks-preview)`, `az_aks_approuting_gateway_istio_enable`, `az_aks_approuting_gateway_istio_enable(aks-preview)`

## az aks approuting gateway istio disable

Disable Gateway API based ingress on App Routing via Istio.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Disable Istio Gateway API implementation for App Routing.*
```azurecli
az aks approuting gateway istio disable --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks approuting gateway istio disable  (extension: aks-preview etc.)

Disable Gateway API based ingress on App Routing via Istio.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2. Use AKSHTTPCustomFeatures=Microsoft.ContainerService/AppRoutingIstioGatewayAPIPreview to enable the preview feature flag after registering your subscription to use it.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Disable Istio Gateway API implementation for App Routing.*
```azurecli
az aks approuting gateway istio disable --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks approuting gateway istio enable

Enable Gateway API based ingress on App Routing via Istio without service mesh functionality.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Enable Istio Gateway API implementation for App Routing.*
```azurecli
az aks approuting gateway istio enable --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks approuting gateway istio enable  (extension: aks-preview etc.)

Enable Gateway API based ingress on App Routing via Istio without service mesh functionality.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2. Use AKSHTTPCustomFeatures=Microsoft.ContainerService/AppRoutingIstioGatewayAPIPreview to enable the preview feature flag after registering your subscription to use it.
- `--change-reference` — The related change reference ID for this resource operation.

*Enable Istio Gateway API implementation for App Routing.*
```azurecli
az aks approuting gateway istio enable --resource-group MyResourceGroup --name MyManagedCluster
```
