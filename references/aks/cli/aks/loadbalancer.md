# az aks loadbalancer

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/loadbalancer  
> Microsoft doc last updated: unknown

Commands to manage load balancer configurations in a managed Kubernetes cluster.

Subgroups and commands: `az_aks_loadbalancer_add`, `az_aks_loadbalancer_delete`, `az_aks_loadbalancer_list`, `az_aks_loadbalancer_rebalance-nodes`, `az_aks_loadbalancer_show`, `az_aks_loadbalancer_update`

## az aks loadbalancer add  (extension: aks-preview etc.)

Add a load balancer configuration to a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the load balancer configuration.
- `--primary-agent-pool-name -p` — Name of the primary agent pool for this load balancer.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers to the AKS API.
- `--allow-service-placement -a` — Whether to automatically place services on the load balancer.
- `--change-reference` — The related change reference ID for this resource operation.
- `--node-selector -d` — Node label selector for nodes that can be members of this load balancer.
- `--service-label-selector -l` — Label selector for services that can be placed on this load balancer.
- `--service-namespace-selector -s` — Namespace label selector for services that can be placed on this load balancer.

*Add a load balancer configuration with a specific primary agent pool*
```azurecli
az aks loadbalancer add -g MyResourceGroup -n secondary --cluster-name MyManagedCluster --primary-agent-pool-name nodepool1
```

*Add a load balancer configuration with service label selector*
```azurecli
az aks loadbalancer add -g MyResourceGroup -n app-lb --cluster-name MyManagedCluster --primary-agent-pool-name nodepool2 --service-label-selector app=frontend
```

*Add a load balancer configuration that doesn't automatically place services*
```azurecli
az aks loadbalancer add -g MyResourceGroup -n restricted-lb --cluster-name MyManagedCluster --primary-agent-pool-name nodepool3 --allow-service-placement false
```

*Add a load balancer configuration with custom AKS API headers*
```azurecli
az aks loadbalancer add -g MyResourceGroup -n api-lb --cluster-name MyManagedCluster --primary-agent-pool-name nodepool1 --aks-custom-headers CustomHeader=Value
```

## az aks loadbalancer delete  (extension: aks-preview etc.)

Delete a load balancer configuration from a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the load balancer configuration to delete.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Delete a load balancer configuration*
```azurecli
az aks loadbalancer delete -g MyResourceGroup -n secondary --cluster-name MyManagedCluster
```

## az aks loadbalancer list  (extension: aks-preview etc.)

List all load balancer configurations in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*List all load balancer configurations*
```azurecli
az aks loadbalancer list -g MyResourceGroup --cluster-name MyManagedCluster
```

*List all load balancer configurations in table format*
```azurecli
az aks loadbalancer list -g MyResourceGroup --cluster-name MyManagedCluster -o table
```

## az aks loadbalancer rebalance-nodes  (extension: aks-preview etc.)

Rebalance nodes across specific load balancers.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--lb-names --load-balancer-names` — Space-separated list of load balancer names to rebalance. If not specified, all load balancers will be rebalanced.

## az aks loadbalancer show  (extension: aks-preview etc.)

Show details of a specific load balancer configuration in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the load balancer configuration to show.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Show details of a specific load balancer configuration*
```azurecli
az aks loadbalancer show -g MyResourceGroup -n secondary --cluster-name MyManagedCluster
```

*Show details of a load balancer configuration in table format*
```azurecli
az aks loadbalancer show -g MyResourceGroup -n kubernetes --cluster-name MyManagedCluster -o table
```

## az aks loadbalancer update  (extension: aks-preview etc.)

Update a load balancer configuration in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — Name of the managed cluster.
- `--name -n` — Name of the load balancer configuration to update.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers to the AKS API.
- `--allow-service-placement -a` — Whether to automatically place services on the load balancer.
- `--change-reference` — The related change reference ID for this resource operation.
- `--node-selector -d` — Node label selector for nodes that can be members of this load balancer.
- `--primary-agent-pool-name -p` — Name of the primary agent pool for this load balancer.
- `--service-label-selector -l` — Label selector for services that can be placed on this load balancer.
- `--service-namespace-selector -s` — Namespace label selector for services that can be placed on this load balancer.

*Update a load balancer configuration's primary agent pool*
```azurecli
az aks loadbalancer update -g MyResourceGroup -n secondary --cluster-name MyManagedCluster --primary-agent-pool-name nodepool2
```

*Update a load balancer configuration to disable automatic service placement*
```azurecli
az aks loadbalancer update -g MyResourceGroup -n app-lb --cluster-name MyManagedCluster --allow-service-placement false
```

*Update a load balancer configuration with new service selector*
```azurecli
az aks loadbalancer update -g MyResourceGroup -n app-lb --cluster-name MyManagedCluster --service-label-selector tier=frontend,environment=production
```

*Update a load balancer configuration with custom AKS API headers*
```azurecli
az aks loadbalancer update -g MyResourceGroup -n api-lb --cluster-name MyManagedCluster --aks-custom-headers CustomHeader=Value
```
