# Use instance-level public IPs in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/use-node-public-ips  
> Microsoft doc last updated: 09/25/2026


AKS nodes don't require their own public IP addresses for communication. However, scenarios may require nodes in a node pool to receive their own dedicated public IP addresses. A common scenario is for gaming workloads, where a console needs to make a direct connection to a cloud virtual machine to minimize hops. This scenario can be achieved on AKS by using Node Public IP.

First, create a new resource group.

```azurecli-interactive
az group create --name <resourceGroup> --location <region>
```

Create a new AKS cluster and attach a public IP for your nodes. Each of the nodes in the node pool receives a unique public IP. You can verify this by looking at the Virtual Machine Scale Set instances.

```azurecli-interactive
az aks create \
    --resource-group <resourceGroup> \
    --name <aksClusterName> \
    --location <region> \
    --enable-node-public-ip \
    --generate-ssh-keys
```

For existing AKS clusters, you can also add a new node pool, and attach a public IP for your nodes.

```azurecli-interactive
az aks nodepool add --resource-group <resourceGroup> --cluster-name <aksClusterName> --name <newNodePool> --enable-node-public-ip
```

## Use a public IP prefix

There are a number of [benefits to using a public IP prefix][public-ip-prefix-benefits]. AKS supports using addresses from an existing public IP prefix for your nodes by passing the resource ID with the flag `--node-public-ip-prefix-id` when creating a new cluster or adding a node pool.

First, create a public IP prefix using [az network public-ip prefix create][az-public-ip-prefix-create]:

```azurecli-interactive
az network public-ip prefix create --length 28 --location <region> --name <publicIPPrefixName> --resource-group <resourceGroup>
```

View the output, and take note of the `id` for the prefix:

```output
{
  ...
  "id": "/subscriptions/<subscription-id>/resourceGroups/<resourceGroup>/providers/Microsoft.Network/publicIPPrefixes/<publicIPPrefixName>",
  ...
}
```

Finally, when creating a new cluster or adding a new node pool, use the flag `--node-public-ip-prefix-id` and pass in the prefix's resource ID:

```azurecli-interactive
az aks create \
    --resource-group <resourceGroup> \
    --name <aksClusterName> \
    --location <region> \
    --enable-node-public-ip \
    --node-public-ip-prefix-id /subscriptions/<subscription-id>/resourceGroups/<resourceGroup>/providers/Microsoft.Network/publicIPPrefixes/<publicIPPrefixName> \
    --generate-ssh-keys
```

## Use a dual-stack public IP prefix (preview)

You can assign both IPv4 and IPv6 public IP addresses to each node in a node pool by using public IP prefixes on a dual-stack cluster. This feature is useful for workloads that require direct inbound or outbound connectivity over both IPv4 and IPv6, or for applications that operate in environments that require IPv6 compliance.

There are two supported configurations:

- **Bring your own IPv4 and IPv6 prefixes.** Each node receives one IPv4 address from your IPv4 prefix and one IPv6 address from your IPv6 prefix. Use this configuration when both addresses need to come from address ranges that you control, such as when a firewall or partner service allows traffic only from your prefixes.
- **Bring your own IPv6 prefix only.** Each node receives one IPv6 address from your IPv6 prefix, and Azure automatically assigns the IPv4 address. Use this configuration when only the IPv6 address needs to come from a range that you control. Because the node pool doesn't consume addresses from an IPv4 prefix, the size of an IPv4 prefix doesn't limit how many nodes the node pool can scale to.

### Requirements

To use dual-stack public IP prefixes with node public IPs, ensure the following prerequisites are met:

- Your cluster is configured as a dual-stack cluster with both IPv4 and IPv6 IP families. A dual-stack cluster is required for both configurations, including the IPv6-only prefix configuration.
- Your cluster uses Azure CNI with overlay networking.
- You created the public IP prefixes you plan to use in the same subscription and region as your AKS cluster. Depending on the configuration you choose, you need either one IPv4 prefix and one IPv6 prefix, or a single IPv6 prefix.
- Each public IP prefix uses the Standard SKU and isn't attached to a load balancer.
- The AKS cluster identity has permission to manage the public IP prefixes. If the prefixes are in a different resource group, assign the Network Contributor role on that resource group to the cluster identity.

### Register the preview features

Dual-stack (IPv4 and IPv6) public IP prefix support for node public IPs is currently available in preview. Before you can use this feature, you must install or update the Azure CLI extension and register the `NodePublicIPv6PrefixPreview` feature flags in your subscription.

Install or update the aks-preview extension:

```azurecli-interactive
az extension add --name aks-preview --upgrade
```

Register the required preview features:

```azurecli-interactive
az feature register --namespace Microsoft.ContainerService --name NodePublicIPv6PrefixPreview
```

It can take several minutes for the feature registrations to complete. To check the registration status, run:

```azurecli-interactive
az feature show --namespace Microsoft.ContainerService --name NodePublicIPv6PrefixPreview --query "properties.state"
```

Wait until the feature reports a state of **Registered** before proceeding.

After the feature flags are registered, refresh the resource provider to ensure the changes are applied:

```azurecli-interactive
az provider register --namespace Microsoft.ContainerService
```
Once the registration is complete, you can create or update a cluster to use dual-stack public IP prefixes for node public IPs.

### Create public IP prefixes

Create a public IP prefix for IPv4 and IPv6 by using the Azure CLI. If you plan to use the IPv6-only prefix configuration, create only the IPv6 prefix.

For IPv4:

```azurecli-interactive
az network public-ip prefix create \
  --resource-group <resourceGroup> \
  --name <ipv4PrefixName> \
  --location <region> \
  --length 28 \
  --sku Standard \
  --version IPv4
```

For IPv6:

```azurecli-interactive
az network public-ip prefix create \
  --resource-group <resourceGroup> \
  --name <ipv6PrefixName> \
  --location <region> \
  --length 124 \
  --sku Standard \
  --version IPv6
```

After creating the prefixes, note the resource ID of each prefix.

### Create a new cluster with dual-stack node public IP prefixes

When creating a new AKS cluster, use the `--node-public-ip-prefix-ids` parameter to specify both the IPv4 and IPv6 public IP prefixes.

```azurecli-interactive
az aks create \
  --resource-group <resourceGroup> \
  --name <aksClusterName> \
  --location <region> \
  --enable-node-public-ip \
  --ip-families IPv4,IPv6 \
  --network-plugin azure \
  --network-plugin-mode overlay \
  --node-public-ip-prefix-ids "<ipv4PrefixResourceId>,<ipv6PrefixResourceId>" \
  --generate-ssh-keys
```

The `--node-public-ip-prefix-ids` parameter accepts a comma-separated list of public IP prefix resource IDs. The list can contain at most one IPv4 prefix and one IPv6 prefix. Order doesn't matter, because AKS determines the IP version from each referenced prefix.

### Add a node pool with dual-stack node public IP prefixes

You can also add a node pool with dual-stack node public IP prefixes to an existing dual-stack cluster.

```azurecli-interactive
az aks nodepool add \
  --resource-group <resourceGroup> \
  --cluster-name <aksClusterName> \
  --name <nodePoolName> \
  --enable-node-public-ip \
  --node-public-ip-prefix-ids "<ipv4PrefixResourceId>,<ipv6PrefixResourceId>"
```

### Use an IPv6-only public IP prefix

If you only need the IPv6 address to come from a prefix that you control, specify a single IPv6 prefix. Each node receives an IPv6 address from your prefix, and Azure automatically assigns the IPv4 address. The node pool still requires a dual-stack cluster.

Use this configuration when the size of an IPv4 prefix would otherwise limit how far the node pool can scale. Because the node pool doesn't draw IPv4 addresses from a prefix, only the capacity of the IPv6 prefix limits the node count.

Create a new cluster with an IPv6-only node public IP prefix:

```azurecli-interactive
az aks create \
  --resource-group <resourceGroup> \
  --name <aksClusterName> \
  --location <region> \
  --enable-node-public-ip \
  --ip-families IPv4,IPv6 \
  --network-plugin azure \
  --network-plugin-mode overlay \
  --node-public-ip-prefix-ids "<ipv6PrefixResourceId>" \
  --generate-ssh-keys
```

Add a node pool with an IPv6-only node public IP prefix to an existing dual-stack cluster:

```azurecli-interactive
az aks nodepool add \
  --resource-group <resourceGroup> \
  --cluster-name <aksClusterName> \
  --name <nodePoolName> \
  --enable-node-public-ip \
  --node-public-ip-prefix-ids "<ipv6PrefixResourceId>"
```

Because Azure assigns the IPv4 address automatically, the IPv4 address of each node isn't predictable and you can't add it to an allow list in advance. As a result, you can't use an IPv6-only public IP prefix on a cluster that uses [API server authorized IP ranges][api-server-authorized-ip-ranges]. Use [API Server VNet Integration][api-server-vnet-integration] or a [private cluster][private-clusters] instead, or include an IPv4 prefix in the list.

### Verify the node public IP prefix configuration

Confirm which prefixes a node pool uses with the [az aks nodepool show][az-aks-nodepool-show] command:

```azurecli-interactive
az aks nodepool show \
  --resource-group <resourceGroup> \
  --cluster-name <aksClusterName> \
  --name <nodePoolName> \
  --query "networkProfile.nodePublicIPPrefixIDs"
```

List the public IP addresses that the nodes received with the [az vmss list-instance-public-ips][az-list-ips] command. Use the [node resource group][node-resource-group]:

```azurecli-interactive
az vmss list-instance-public-ips \
  --resource-group <MC_resourceGroup_aksClusterName_region> \
  --name <virtualMachineScaleSetName> \
  --query "[].{name:name, ipAddress:ipAddress, version:publicIPAddressVersion}" \
  --output table
```

For an IPv6-only prefix, each node has one IPv6 address from your prefix and one IPv4 address from the Azure-managed address pool.

### Limitations

The following limitations apply to public IP prefixes for node public IPs.

**Prefix list:**

- The prefix list can contain at most one IPv4 prefix and one IPv6 prefix. Two prefixes of the same IP version are rejected.
- You must enable node public IPs on the node pool when you specify prefixes.
- You can't use the `--node-public-ip-prefix-ids` and `--node-public-ip-prefix-id` parameters in the same command.
- Node public IP configuration is immutable. To change the public IP prefixes, you must create a new node pool and migrate workloads.

**Prefix resources:**

- Each prefix must use the Standard SKU. Basic and Standard V2 prefixes aren't supported.
- Each prefix must be in the same subscription and the same region as your AKS cluster.
- You can't use a prefix that's already attached to a load balancer.
- If your node pool uses availability zones, each prefix's zones must cover the zones of the node pool. A zone-redundant prefix, which has no zones assigned, works with any node pool.

**Capacity and scale:**

- Each prefix must have enough addresses for the node pool's node count, because each node consumes one address from each prefix you provide.
- Cluster Autoscaler is supported, but ensure that the configured maximum node count doesn't exceed the number of available IP addresses in each prefix you provide. If you use an IPv6-only prefix, only the IPv6 prefix limits the node count, because Azure assigns the IPv4 addresses automatically.

**Feature compatibility:**

- You can't use an IPv6-only public IP prefix on a cluster that uses API server authorized IP ranges, because Azure assigns the node's IPv4 address automatically and you can't add it to an allow list in advance. Use API Server VNet Integration or a private cluster instead, or include an IPv4 prefix in the list.
- Each node is assigned a single IPv6 public IP address.
- This feature isn't supported with AKS Automatic or node auto-provisioning.
- Multi-NIC node pools aren't supported.

## Locate public IPs for nodes

You can locate the public IPs for your nodes in various ways:

* Use the Azure CLI command [`az vmss list-instance-public-ips`][az-list-ips].
* Use [PowerShell or Bash commands][vmss-commands]. 
* You can also view the public IPs in the Azure portal by viewing the instances in the Virtual Machine Scale Set.

> [!Important]
> The [node resource group][node-resource-group] contains the nodes and their public IPs. Use the node resource group when executing commands to find the public IPs for your nodes.

```azurecli
az vmss list-instance-public-ips --resource-group <MC_region_aksClusterName_region> --name <virtualMachineScaleSetName>
```

## Use public IP tags on node public IPs

Public IP tags can be utilized on node public IPs to utilize the [Azure Routing Preference](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/routing-preference-overview) feature, which is available in [specified regions](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/routing-preference-overview#regional-availability).

### Requirements

* AKS version 1.29 or greater is required.

### Create a new cluster using routing preference internet

```azurecli-interactive
az aks create \
    --name <aksClusterName> \
    --location <region> \
    --resource-group <resourceGroup> \
    --enable-node-public-ip \
    --node-public-ip-tags RoutingPreference=Internet \
    --generate-ssh-keys
```

### Add a node pool with routing preference internet

```azurecli-interactive
az aks nodepool add --cluster-name <aksClusterName> \
  --name <nodePoolName> \
  --location <region> \
  --resource-group <resourceGroup> \
  --enable-node-public-ip \
  --node-public-ip-tags RoutingPreference=Internet
```

## Allow host port connections and add node pools to application security groups

AKS nodes utilizing node public IPs that host services on their host address need to have an NSG rule added to allow the traffic. Adding the desired ports in the node pool configuration will create the appropriate allow rules in the cluster network security group.

If a network security group is in place on the subnet with a cluster using bring-your-own virtual network, an allow rule must be added to that network security group. This can be limited to the nodes in a given node pool by adding the node pool to an [application security group (ASG)](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview#application-security-groups). A managed ASG will be created by default in the managed resource group if allowed host ports are specified. Nodes can also be added to one or more custom ASGs by specifying the resource ID of the NSG(s) in the node pool parameters.

### Host port specification format

When specifying the list of ports to allow, use a comma-separate list with entries in the format of `port/protocol` or `startPort-endPort/protocol`.

Examples:

- 80/tcp
- 80/tcp,443/tcp
- 53/udp,80/tcp
- 50000-60000/tcp

### Requirements

* AKS version 1.29 or greater is required.

### Create a new cluster with allowed ports and application security groups

```azurecli-interactive
az aks create \
    --resource-group <resourceGroup> \
    --name <aksClusterName> \
    --nodepool-name <nodePoolName> \
    --nodepool-allowed-host-ports 80/tcp,443/tcp,53/udp,40000-60000/tcp,40000-50000/udp\
    --nodepool-asg-ids "<asgId>,<asgId>" \
    --generate-ssh-keys
```

### Add a new node pool with allowed ports and application security groups

```azurecli-interactive
az aks nodepool add \
  --resource-group <resourceGroup> \
  --cluster-name <aksClusterName> \
  --name <nodePoolName> \
  --allowed-host-ports 80/tcp,443/tcp,53/udp,40000-60000/tcp,40000-50000/udp \
  --asg-ids "<asgId>,<asgId>"
```

### Update the allowed ports and application security groups for a node pool

```azurecli-interactive
az aks nodepool update \
  --resource-group <resourceGroup> \
  --cluster-name <aksClusterName> \
  --name <nodePoolName> \
  --allowed-host-ports 80/tcp,443/tcp,53/udp,40000-60000/tcp,40000-50000/udp \
  --asg-ids "<asgId>,<asgId>"
```

## Automatically assign host ports for pod workloads (PREVIEW)

When public IPs are configured on nodes, host ports can be utilized to allow pods to directly receive traffic without having to configure a load balancer service. This is especially useful in scenarios like gaming, where the ephemeral nature of the node IP and port is not a problem because a matchmaker service at a well-known hostname can provide the correct host and port to use at connection time. However, because only one process on a host can be listening on the same port, using applications with host ports can lead to problems with scheduling. To avoid this issue, AKS provides the ability to have the system dynamically assign an available port at scheduling time, preventing conflicts.

> [!WARNING]
> Pod host port traffic will be blocked by the default NSG rules in place on the cluster. This feature should be combined with allowing host ports on the node pool to allow traffic to flow.

### Requirements

* AKS version 1.29 or greater is required.

### Register the 'PodHostPortAutoAssignPreview' feature flag

Register the `PodHostPortAutoAssignPreview` feature flag by using the [az feature register][az-feature-register] command, as shown in the following example:

```azurecli-interactive
az feature register --namespace "Microsoft.ContainerService" --name "PodHostPortAutoAssignPreview"
```

It takes a few minutes for the status to show *Registered*. Verify the registration status by using the [az feature show][az-feature-show] command:

```azurecli-interactive
az feature show --namespace "Microsoft.ContainerService" --name "PodHostPortAutoAssignPreview"
```

When the status reflects *Registered*, refresh the registration of the *Microsoft.ContainerService* resource provider by using the [az provider register][az-provider-register] command:

```azurecli-interactive
az provider register --namespace Microsoft.ContainerService
```

### Automatically assign a host port to a pod

Triggering host port auto assignment is done by deploying a workload without any host ports and applying the `kubernetes.azure.com/assign-hostports-for-containerports` annotation with the list of ports that need host port assignments. The value of the annotation should be specified as a comma-separated list of entries like `port/protocol`, where the port is an individual port number that is defined in the Pod spec and the protocol is `tcp` or `udp`.

Ports will be assigned from the range `40000-59999` and will be unique across the cluster. The assigned ports will also be added to environment variables inside the pod so that the application can determine what ports were assigned. The environment variable name will be in the following format (example below): `<deployment name>_PORT_<port number>_<protocol>_HOSTPORT`, so an example would be `mydeployment_PORT_8080_TCP_HOSTPORT: 41932`.

Here is an example `echoserver` deployment, showing the mapping of host ports for ports 8080 and 8443:

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: echoserver-hostport
  labels:
    app: echoserver-hostport
spec:
  replicas: 3
  selector:
    matchLabels:
      app: echoserver-hostport
  template:
    metadata:
      annotations:
        kubernetes.azure.com/assign-hostports-for-containerports: 8080/tcp,8443/tcp
      labels:
        app: echoserver-hostport
    spec:
      nodeSelector:
        kubernetes.io/os: linux
      containers:
        - name: echoserver-hostport
          image: k8s.gcr.io/echoserver:1.10
          ports:
            - name: http
              containerPort: 8080
              protocol: TCP
            - name: https
              containerPort: 8443
              protocol: TCP
```

When the deployment is applied, the `hostPort` entries will be in the YAML of the individual pods:

```shell
$ kubectl describe pod echoserver-hostport-75dc8d8855-4gjfc
<cut for brevity>
Containers:
  echoserver-hostport:
    Container ID:   containerd://d0b75198afe0612091f412ee7cf7473f26c80660143a96b459b3e699ebaee54c
    Image:          k8s.gcr.io/echoserver:1.10
    Image ID:       k8s.gcr.io/echoserver@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229                                                                                                      Ports:          8080/TCP, 8443/TCP
    Host Ports:     46645/TCP, 49482/TCP
    State:          Running
      Started:      Thu, 12 Jan 2023 18:02:50 +0000
    Ready:          True
    Restart Count:  0
    Environment:
      echoserver-hostport_PORT_8443_TCP_HOSTPORT:  49482
      echoserver-hostport_PORT_8080_TCP_HOSTPORT:  46645
```

## Next steps

* Learn about [using multiple node pools in AKS](https://learn.microsoft.com/en-us/azure/aks/create-node-pools).

* Learn about [using standard load balancers in AKS](https://learn.microsoft.com/en-us/azure/aks/load-balancer-standard)

[kubernetes-drain]: https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
[kubectl-get]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get
[kubectl-taint]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint
[kubectl-describe]: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe
[kubernetes-labels]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
[kubernetes-label-syntax]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set
[capacity-reservation-groups]:https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-associate-virtual-machine-scale-set

[arm-sku-vm1]: https://learn.microsoft.com/en-us/azure/aks/articles/virtual-machines/dpsv5-dpdsv5-series
[arm-sku-vm2]: https://learn.microsoft.com/en-us/azure/aks/articles/virtual-machines/dplsv5-dpldsv5-series
[arm-sku-vm3]: https://learn.microsoft.com/en-us/azure/aks/articles/virtual-machines/epsv5-epdsv5-series
[aks-quickstart-windows-cli]: https://learn.microsoft.com/en-us/azure/aks/learn/quick-windows-container-deploy-cli
[az-aks-get-credentials]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-credentials
[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[az-aks-get-upgrades]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-get-upgrades
[az-aks-nodepool-add]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-add
[az-aks-nodepool-list]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-list
[az-aks-nodepool-update]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-update
[az-aks-nodepool-upgrade]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-upgrade
[az-aks-nodepool-scale]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-scale
[az-aks-nodepool-delete]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-delete
[az-aks-show]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-show
[az-extension-add]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-add
[az-extension-update]: https://learn.microsoft.com/en-us/cli/azure/extension#az-extension-update
[az-feature-register]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-register
[az-feature-list]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-list
[az-feature-show]: https://learn.microsoft.com/en-us/cli/azure/feature#az-feature-show
[az-provider-register]: https://learn.microsoft.com/en-us/cli/azure/provider#az-provider-register
[az-group-create]: https://learn.microsoft.com/en-us/cli/azure/group#az-group-create
[az-group-delete]: https://learn.microsoft.com/en-us/cli/azure/group#az-group-delete
[az-deployment-group-create]: https://learn.microsoft.com/en-us/cli/azure/deployment/group#az-deployment-group-create
[az-aks-nodepool-add]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-nodepool-add
[az-aks-nodepool-show]: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool#az-aks-nodepool-show
[api-server-authorized-ip-ranges]: https://learn.microsoft.com/en-us/azure/aks/api-server-authorized-ip-ranges
[api-server-vnet-integration]: https://learn.microsoft.com/en-us/azure/aks/api-server-vnet-integration
[private-clusters]: https://learn.microsoft.com/en-us/azure/aks/private-clusters
[enable-fips-nodes]: https://learn.microsoft.com/en-us/azure/aks/enable-fips-nodes
[gpu-cluster]: https://learn.microsoft.com/en-us/azure/aks/gpu-cluster
[install-azure-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[operator-best-practices-advanced-scheduler]: https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-advanced-scheduler
[quotas-skus-regions]: https://learn.microsoft.com/en-us/azure/aks/quotas-skus-regions
[supported-versions]: https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions
[tag-limitation]: https://learn.microsoft.com/en-us/azure/aks/articles/azure-resource-manager/management/tag-resources
[taints-tolerations]: https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-advanced-scheduler#provide-dedicated-nodes-using-taints-and-tolerations
[vm-sizes]: https://learn.microsoft.com/en-us/azure/aks/articles/virtual-machines/sizes
[use-system-pool]: https://learn.microsoft.com/en-us/azure/aks/use-system-pools
[node-resource-group]: faq.yml
[vmss-commands]: https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-networking#public-ipv4-per-virtual-machine
[az-list-ips]: https://learn.microsoft.com/en-us/cli/azure/vmss#az-vmss-list-instance-public-ips
[reduce-latency-ppg]: https://learn.microsoft.com/en-us/azure/aks/reduce-latency-ppg
[public-ip-prefix-benefits]: https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-address-prefix
[az-public-ip-prefix-create]: https://learn.microsoft.com/en-us/cli/azure/network/public-ip/prefix#az-network-public-ip-prefix-create
[node-image-upgrade]: https://learn.microsoft.com/en-us/azure/aks/node-image-upgrade
[use-tags]: https://learn.microsoft.com/en-us/azure/aks/use-tags
[use-labels]: https://learn.microsoft.com/en-us/azure/aks/use-labels
[cordon-and-drain]: https://learn.microsoft.com/en-us/azure/aks/resize-node-pool#cordon-the-existing-nodes
[internal-lb-different-subnet]: https://learn.microsoft.com/en-us/azure/aks/internal-lb#specify-a-different-subnet
[drain-nodes]: https://learn.microsoft.com/en-us/azure/aks/resize-node-pool#drain-the-existing-nodes
