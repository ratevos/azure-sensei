# az aks mesh

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/mesh  
> Microsoft doc last updated: unknown

Commands to manage Azure Service Mesh.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_mesh_disable`, `az_aks_mesh_disable(aks-preview)`, `az_aks_mesh_disable-egress-gateway`, `az_aks_mesh_disable-egress-gateway(aks-preview)`, `az_aks_mesh_disable-ingress-gateway`, `az_aks_mesh_disable-ingress-gateway(aks-preview)`, `az_aks_mesh_disable-istio-cni`, `az_aks_mesh_enable`, `az_aks_mesh_enable(aks-preview)`, `az_aks_mesh_enable-egress-gateway`, `az_aks_mesh_enable-egress-gateway(aks-preview)`, `az_aks_mesh_enable-ingress-gateway`, `az_aks_mesh_enable-ingress-gateway(aks-preview)`, `az_aks_mesh_enable-istio-cni`, `az_aks_mesh_get-revisions`, `az_aks_mesh_get-revisions(aks-preview)`, `az_aks_mesh_get-upgrades`, `az_aks_mesh_get-upgrades(aks-preview)`, `az_aks_mesh_proxy-redirection-mechanism`, `az_aks_mesh_upgrade`, `az_aks_mesh_upgrade_complete`, `az_aks_mesh_upgrade_complete(aks-preview)`, `az_aks_mesh_upgrade_rollback`, `az_aks_mesh_upgrade_rollback(aks-preview)`, `az_aks_mesh_upgrade_start`, `az_aks_mesh_upgrade_start(aks-preview)`

## az aks mesh disable

Disable Azure Service Mesh.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks mesh disable  (extension: aks-preview etc.)

Disable Azure Service Mesh.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks mesh disable-egress-gateway

Disable an Azure Service Mesh egress gateway.

**Required parameters**

- `--istio-eg-gtw-name --istio-egressgateway-name` — Specify the name of the Istio egress gateway.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--istio-eg-gtw-ns --istio-egressgateway-namespace` — Specify the namespace of the Istio egress gateway. Default: aks-istio-egress.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Disable an Istio egress gateway.*
```azurecli
az aks mesh disable-egress-gateway --resource-group MyResourceGroup --name MyManagedCluster --istio-egressgateway-name my-istio-egress-1 --istio-egressgateway-namespace my-namespace-1
```

## az aks mesh disable-egress-gateway  (extension: aks-preview etc.)

Disable an Azure Service Mesh egress gateway.

**Required parameters**

- `--istio-eg-gtw-name --istio-egressgateway-name` — Specify the name of the Istio egress gateway.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--istio-eg-gtw-ns --istio-egressgateway-namespace` — Specify the namespace of the Istio egress gateway. Default: aks-istio-egress.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Disable an Istio egress gateway.*
```azurecli
az aks mesh disable-egress-gateway --resource-group MyResourceGroup --name MyManagedCluster --istio-egressgateway-name my-istio-egress-1 --istio-egressgateway-namespace my-namespace-1
```

## az aks mesh disable-ingress-gateway

Disable an Azure Service Mesh ingress gateway.

**Required parameters**

- `--ingress-gateway-type` — Specify the type of ingress gateway.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Disable an internal ingress gateway.*
```azurecli
az aks mesh disable-ingress-gateway --resource-group MyResourceGroup --name MyManagedCluster --ingress-gateway-type Internal
```

## az aks mesh disable-ingress-gateway  (extension: aks-preview etc.)

Disable an Azure Service Mesh ingress gateway.

**Required parameters**

- `--ingress-gateway-type` — Specify the type of ingress gateway.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Disable an internal ingress gateway.*
```azurecli
az aks mesh disable-ingress-gateway --resource-group MyResourceGroup --name MyManagedCluster --ingress-gateway-type Internal
```

## az aks mesh disable-istio-cni  (extension: aks-preview etc.)

Disable Istio CNI chaining for Azure Service Mesh proxy redirection mechanism.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Disable Istio CNI chaining for Azure Service Mesh.*
```azurecli
az aks mesh disable-istio-cni --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks mesh enable

Enable Azure Service Mesh.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--ca-cert-object-name` — Intermediate cert object name in the Azure Keyvault.
- `--ca-key-object-name` — Intermediate key object name in the Azure Keyvault.
- `--cert-chain-object-name` — Cert chain object name in the Azure Keyvault.
- `--change-reference` — The related change reference ID for this resource operation.
- `--key-vault-id` — The Azure Keyvault id with plugin CA info.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--proxy-redirection-mechanism` — Set the proxy redirection mechanism.
- `--revision` — Azure Service Mesh revision to install.
- `--root-cert-object-name` — Root cert object name in the Azure Keyvault.

*Enable Azure Service Mesh with selfsigned CA.*
```azurecli
az aks mesh enable --resource-group MyResourceGroup --name MyManagedCluster
```

*Enable Azure Service Mesh with plugin CA.*
```azurecli
az aks mesh enable --resource-group MyResourceGroup --name MyManagedCluster --key-vault-id /subscriptions/00000/resourceGroups/foo/providers/Microsoft.KeyVault/vaults/foo --ca-cert-object-name my-ca-cert --ca-key-object-name my-ca-key --cert-chain-object-name my-cert-chain --root-cert-object-name my-root-cert
```

*Enable Azure Service Mesh with CNI chaining.*
```azurecli
az aks mesh enable --resource-group MyResourceGroup --name MyManagedCluster --proxy-redirection-mechanism CNIChaining
```

## az aks mesh enable  (extension: aks-preview etc.)

Enable Azure Service Mesh.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--ca-cert-object-name` — Intermediate cert object name in the Azure Keyvault.
- `--ca-key-object-name` — Intermediate key object name in the Azure Keyvault.
- `--cert-chain-object-name` — Cert chain object name in the Azure Keyvault.
- `--change-reference` — The related change reference ID for this resource operation.
- `--key-vault-id` — The Azure Keyvault id with plugin CA info.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--revision` — Azure Service Mesh revision to install.
- `--root-cert-object-name` — Root cert object name in the Azure Keyvault.

*Enable Azure Service Mesh with selfsigned CA.*
```azurecli
az aks mesh enable --resource-group MyResourceGroup --name MyManagedCluster
```

*Enable Azure Service Mesh with plugin CA.*
```azurecli
az aks mesh enable --resource-group MyResourceGroup --name MyManagedCluster --key-vault-id /subscriptions/8ecadfc9-d1a3-4ea4-b844-0d9f87e4d7c8/resourceGroups/foo/providers/Microsoft.KeyVault/vaults/foo --ca-cert-object-name my-ca-cert --ca-key-object-name my-ca-key --cert-chain-object-name my-cert-chain --root-cert-object-name my-root-cert
```

## az aks mesh enable-egress-gateway

Enable an Azure Service Mesh egress gateway.

**Required parameters**

- `--gateway-configuration-name --gtw-config-name` — Specify the name of the StaticGatewayConfiguration resource.
- `--istio-eg-gtw-name --istio-egressgateway-name` — Specify the name of the Istio egress gateway.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--istio-eg-gtw-ns --istio-egressgateway-namespace` — Specify the namespace of the Istio egress gateway. Default: aks-istio-egress.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Enable an Istio egress gateway. Static egress gateway must be enabled prior to creating an Istio egress gateway. See https://aka.ms/aks-static-egress-gateway on how to create and configure a Static Egress Gateway agentpool.*
```azurecli
az aks mesh enable-egress-gateway --resource-group MyResourceGroup --name MyManagedCluster --istio-egressgateway-name my-istio-egress-1 --istio-egressgateway-namespace my-namespace-1 --gateway-configuration-name sgc-istio-egress-1
```

## az aks mesh enable-egress-gateway  (extension: aks-preview etc.)

Enable an Azure Service Mesh egress gateway.

**Required parameters**

- `--gateway-configuration-name --gtw-config-name` — Specify the name of the StaticGatewayConfiguration resource.
- `--istio-eg-gtw-name --istio-egressgateway-name` — Specify the name of the Istio egress gateway.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--istio-eg-gtw-ns --istio-egressgateway-namespace` — Specify the namespace of the Istio egress gateway. Default: aks-istio-egress.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Enable an Istio egress gateway. Static egress gateway must be enabled prior to creating an Istio egress gateway. See https://aka.ms/aks-static-egress-gateway on how to create and configure a Static Egress Gateway agentpool.*
```azurecli
az aks mesh enable-egress-gateway --resource-group MyResourceGroup --name MyManagedCluster --istio-egressgateway-name my-istio-egress-1 --istio-egressgateway-namespace my-namespace-1 --gateway-configuration-name sgc-istio-egress-1
```

## az aks mesh enable-ingress-gateway

Enable an Azure Service Mesh ingress gateway.

**Required parameters**

- `--ingress-gateway-type` — Specify the type of ingress gateway.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Enable an internal ingress gateway.*
```azurecli
az aks mesh enable-ingress-gateway --resource-group MyResourceGroup --name MyManagedCluster --ingress-gateway-type Internal
```

## az aks mesh enable-ingress-gateway  (extension: aks-preview etc.)

Enable an Azure Service Mesh ingress gateway.

**Required parameters**

- `--ingress-gateway-type` — Specify the type of ingress gateway.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Enable an internal ingress gateway.*
```azurecli
az aks mesh enable-ingress-gateway --resource-group MyResourceGroup --name MyManagedCluster --ingress-gateway-type Internal
```

## az aks mesh enable-istio-cni  (extension: aks-preview etc.)

Enable Istio CNI chaining for Azure Service Mesh proxy redirection mechanism.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Enable Istio CNI chaining for Azure Service Mesh.*
```azurecli
az aks mesh enable-istio-cni --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks mesh get-revisions

Discover available Azure Service Mesh revisions and their compatibility.

**Required parameters**

- `--location -l` — Location in which to discover available Azure Service Mesh revisions.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Discover Azure Service Mesh revisions.*
```azurecli
az aks mesh get-revisions --location westus2
```

## az aks mesh get-revisions  (extension: aks-preview etc.)

Discover available Azure Service Mesh revisions and their compatibility.

**Required parameters**

- `--location -l` — Location in which to discover available Azure Service Mesh revisions.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Discover Azure Service Mesh revisions.*
```azurecli
az aks mesh get-revisions --location westus2
```

## az aks mesh get-upgrades

Discover available Azure Service Mesh upgrades.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Discover Azure Service Mesh upgrades.*
```azurecli
az aks mesh get-upgrades --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks mesh get-upgrades  (extension: aks-preview etc.)

Discover available Azure Service Mesh upgrades.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Discover Azure Service Mesh upgrades.*
```azurecli
az aks mesh get-upgrades --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks mesh proxy-redirection-mechanism

Set the proxy redirection mechanism for Azure Service Mesh.

**Required parameters**

- `--mechanism` — The proxy redirection mechanism.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Set proxy redirection mechanism to CNI chaining.*
```azurecli
az aks mesh proxy-redirection-mechanism --resource-group MyResourceGroup --name MyManagedCluster --mechanism CNIChaining
```

*Set proxy redirection mechanism to init containers.*
```azurecli
az aks mesh proxy-redirection-mechanism --resource-group MyResourceGroup --name MyManagedCluster --mechanism InitContainers
```
