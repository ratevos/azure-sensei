# az aks mesh upgrade

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/mesh/upgrade  
> Microsoft doc last updated: unknown

Commands to manage the upgrades for Azure Service Mesh.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_mesh_upgrade_complete`, `az_aks_mesh_upgrade_complete(aks-preview)`, `az_aks_mesh_upgrade_rollback`, `az_aks_mesh_upgrade_rollback(aks-preview)`, `az_aks_mesh_upgrade_start`, `az_aks_mesh_upgrade_start(aks-preview)`

## az aks mesh upgrade complete

Complete Azure Service Mesh upgrade.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Complete Azure Service Mesh upgrade.*
```azurecli
az aks mesh upgrade complete --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks mesh upgrade complete  (extension: aks-preview etc.)

Complete Azure Service Mesh upgrade.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Complete Azure Service Mesh upgrade.*
```azurecli
az aks mesh upgrade complete --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks mesh upgrade rollback

Rollback Azure Service Mesh upgrade.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Rollback Azure Service Mesh upgrade.*
```azurecli
az aks mesh upgrade rollback --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks mesh upgrade rollback  (extension: aks-preview etc.)

Rollback Azure Service Mesh upgrade.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Rollback Azure Service Mesh upgrade.*
```azurecli
az aks mesh upgrade rollback --resource-group MyResourceGroup --name MyManagedCluster
```

## az aks mesh upgrade start

Initiate Azure Service Mesh upgrade.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--revision` — Azure Service Mesh revision to upgrade to.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Initiate Azure Service Mesh upgrade.*
```azurecli
az aks mesh upgrade start --resource-group MyResourceGroup --name MyManagedCluster --revision asm-1-18
```

## az aks mesh upgrade start  (extension: aks-preview etc.)

Initiate Azure Service Mesh upgrade.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--revision` — Azure Service Mesh revision to upgrade to.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Initiate Azure Service Mesh upgrade.*
```azurecli
az aks mesh upgrade start --resource-group MyResourceGroup --name MyManagedCluster --revision asm-1-18
```
