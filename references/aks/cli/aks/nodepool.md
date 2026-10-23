# az aks nodepool

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/nodepool  
> Microsoft doc last updated: unknown

Commands to manage node pools in Kubernetes kubernetes cluster.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_nodepool_add`, `az_aks_nodepool_add(aks-preview)`, `az_aks_nodepool_auto-scale`, `az_aks_nodepool_auto-scale_add`, `az_aks_nodepool_auto-scale_add(aks-preview)`, `az_aks_nodepool_auto-scale_delete`, `az_aks_nodepool_auto-scale_delete(aks-preview)`, `az_aks_nodepool_auto-scale_update`, `az_aks_nodepool_auto-scale_update(aks-preview)`, `az_aks_nodepool_delete`, `az_aks_nodepool_delete(aks-preview)`, `az_aks_nodepool_delete-machines`, `az_aks_nodepool_delete-machines(aks-preview)`, `az_aks_nodepool_get-bootstrap-data`, `az_aks_nodepool_get-rollback-versions`, `az_aks_nodepool_get-rollback-versions(aks-preview)`, `az_aks_nodepool_get-upgrades`, `az_aks_nodepool_get-upgrades(aks-preview)`, `az_aks_nodepool_list`, `az_aks_nodepool_list(aks-preview)`, `az_aks_nodepool_manual-scale`, `az_aks_nodepool_manual-scale_add`, `az_aks_nodepool_manual-scale_add(aks-preview)`, `az_aks_nodepool_manual-scale_delete`, `az_aks_nodepool_manual-scale_delete(aks-preview)`, `az_aks_nodepool_manual-scale_update`, `az_aks_nodepool_manual-scale_update(aks-preview)`, `az_aks_nodepool_operation-abort`, `az_aks_nodepool_operation-abort(aks-preview)`, `az_aks_nodepool_rollback`, `az_aks_nodepool_rollback(aks-preview)`, `az_aks_nodepool_scale`, `az_aks_nodepool_scale(aks-preview)`, `az_aks_nodepool_show`, `az_aks_nodepool_show(aks-preview)`, `az_aks_nodepool_snapshot`, `az_aks_nodepool_snapshot_create`, `az_aks_nodepool_snapshot_create(aks-preview)`, `az_aks_nodepool_snapshot_delete`, `az_aks_nodepool_snapshot_delete(aks-preview)`, `az_aks_nodepool_snapshot_list`, `az_aks_nodepool_snapshot_list(aks-preview)`, `az_aks_nodepool_snapshot_show`, `az_aks_nodepool_snapshot_show(aks-preview)`, `az_aks_nodepool_snapshot_update`, `az_aks_nodepool_snapshot_update(aks-preview)`, `az_aks_nodepool_snapshot_wait`, `az_aks_nodepool_start`, `az_aks_nodepool_start(aks-preview)`, `az_aks_nodepool_stop`, `az_aks_nodepool_stop(aks-preview)`, `az_aks_nodepool_update`, `az_aks_nodepool_update(aks-preview)`, `az_aks_nodepool_upgrade`, `az_aks_nodepool_upgrade(aks-preview)`, `az_aks_nodepool_wait`

## az aks nodepool add

Add a node pool to the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Comma-separated key-value pairs to specify custom headers.
- `--allowed-host-ports` — Expose host ports on the node pool. When specified, format should be a space-separated list of ranges with protocol, eg. `80/TCP 443/TCP 4000-5000/TCP`.
- `--asg-ids` — The IDs of the application security groups to which the node pool's network interface should belong. When specified, format should be a space-separated list of IDs.
- `--change-reference` — The related change reference ID for this resource operation.
- `--crg-id` — The crg id used to associate the new nodepool with the existed Capacity Reservation Group resource.
- `--disable-windows-outbound-nat` — Disable Windows OutboundNAT on Windows agent node pool. Default: False.
- `--drain-timeout` — When nodes are drain how many minutes to wait for all pods to be evicted.
- `--enable-artifact-streaming` — Enable artifact streaming for VirtualMachineScaleSets managed by a node pool, to speed up the cold-start of containers on a node through on-demand image loading. This option is only valid for Linux nodepools. To use this feature, container images must also enable artifact streaming on ACR. If not sp Default: False.
- `--enable-cluster-autoscaler -e` — Enable cluster autoscaler. Default: False.
- `--enable-encryption-at-host` — Enable EncryptionAtHost, default value is false. Default: False.
- `--enable-fips-image` — Use FIPS-enabled OS on agent nodes. Default: False.
- `--enable-managed-dranet` — Enable Managed DRANET on the node pool. Default: False.
- `--enable-node-public-ip` — Enable VMSS or VMs node public IP. Default: False.
- `--enable-secure-boot` — Enable Secure Boot on agent node pool. Must use VMSS or VMs agent pool type. Default: False.
- `--enable-ultra-ssd` — Enable UltraSSD, default value is false. Default: False.
- `--enable-vtpm` — Enable vTPM on agent node pool. Must use VMSS or VMs agent pool type. Default: False.
- `--eviction-policy` — The eviction policy of the Spot node pool. It can only be set when --priority is Spot. Default: Delete.
- `--gateway-prefix-size` — The size of Public IPPrefix attached to the Gateway-mode node pool. The node pool must be in Gateway mode.
- `--gpu-driver` — Whether to install driver for GPU node pool. Possible values are "Install" or "None". Default is "Install".
- `--gpu-instance-profile` — GPU instance profile to partition multi-gpu Nvidia GPUs.
- `--host-group-id` — The fully qualified dedicated host group id used to provision agent node pool.
- `--if-match` — The value provided will be compared to the ETag of the agentpool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool.
- `--if-none-match` — Set to '*' to allow a new agentpool to be created, but to prevent updating an existing agentpool. Other values will be ignored.
- `--kubelet-config` — Path to JSON file containing Kubelet configurations for agent nodes. https://aka.ms/aks/custom-node-config.
- `--kubernetes-version -k` — Version of Kubernetes to use for creating the cluster, such as "1.16.9".
- `--labels` — The node labels for the node pool. See https://aka.ms/node-labels for syntax of labels.
- `--linux-os-config` — Path to JSON file containing OS configurations for Linux agent nodes. https://aka.ms/aks/custom-node-config.
- `--localdns-config` — Set the localDNS Profile for a nodepool with a JSON config file.
- `--max-count` — Maximum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [0, 1000] for user nodepool, and [1,1000] for system nodepool.
- `--max-pods -m` — The maximum number of pods deployable to a node.
- `--max-surge` — Extra nodes used to speed upgrade. When specified, it represents the number or percent used, eg. 5 or 33%.
- `--max-unavailable` — The maximum number or percentage of nodes that can be simultaneously unavailable during upgrade. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--message-of-the-day` — Path to a file containing the desired message of the day. Only valid for linux nodes. Will be written to /etc/motd.
- `--min-count` — Minimum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [0, 1000] for user nodepool, and [1,1000] for system nodepool.
- `--mode` — The mode for a node pool which defines a node pool's primary function. If set as "System", AKS prefers system pods scheduling to node pools with mode `System`. Learn more at https://aka.ms/aks/nodepool/mode. Default: User.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes in the Kubernetes agent pool. After creating a cluster, you can change the size of its node pool with `az aks scale`. Default: 3.
- `--node-osdisk-size` — Size in GiB of the OS disk for each node in the agent pool. Minimum 30 GiB.
- `--node-osdisk-type` — OS disk type to be used for machines in a given agent pool. Defaults to 'Ephemeral' when possible in conjunction with VM size and OS disk size. May not be changed for this pool after creation. ('Ephemeral' or 'Managed').
- `--node-public-ip-prefix-id` — Public IP prefix ID used to assign public IPs to VMSS or VMs nodes.
- `--node-public-ip-tags` — The ipTags of the node public IPs.
- `--node-soak-duration` — The amount of time (in minutes) to wait after draining a node and before reimaging it and moving on to next node.
- `--node-taints` — The node taints for the node pool.
- `--node-vm-size -s` — Size of Virtual Machines to create as Kubernetes nodes. If the user does not specify one, server will select a default VM size for her/him.
- `--os-sku` — The OS SKU of the agent node pool. Ubuntu, Ubuntu2204, Ubuntu2404, AzureLinux, AzureLinux3, or AzureContainerLinux for Linux. Windows2019, Windows2022, or Windows2025 for Windows.
- `--os-type` — The OS Type. Linux or Windows.
- `--pod-ip-allocation-mode` — Set the ip allocation mode for how Pod IPs from the Azure Pod Subnet are allocated to the nodes in the AKS cluster. The choice is between dynamic batches of individual IPs or static allocation of a set of CIDR blocks. Accepted Values are "DynamicIndividual" or "StaticBlock".
- `--pod-subnet-id` — The Resource Id of a subnet in an existing VNet into which to assign pods in the cluster (requires azure network-plugin).
- `--ppg` — The ID of a PPG.
- `--priority` — The priority of the node pool. Default: Regular.
- `--scale-down-mode` — Describe how VMs are added to or removed from nodepools. Default: Delete.
- `--snapshot-id` — The source snapshot id used to create this nodepool.
- `--spot-max-price` — It can only be set when --priority is Spot. Specify the maximum price you are willing to pay in US Dollars. Possible values are any decimal value greater than zero or -1 which indicates default price to be up-to on-demand. It can only include up to 5 decimal places. Default: nan.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--undrainable-node-behavior` — Define the behavior for undrainable nodes during upgrade. The value should be "Cordon" or "Schedule". The default value is "Schedule". Default: Schedule.
- `--vm-set-type` — Agent pool vm set type. VirtualMachineScaleSets or AvailabilitySet or VirtualMachines. Defaults to 'VirtualMachineScaleSets'.
- `--vm-sizes` — Comma-separated list of VM sizes. Valid for VirtualMachines node pool only. If `--vm-sizes` not specified but `--node-vm-size` specified, value of `--node-vm-size` will be used. If neither of them specified, defaults to Standard_DS2_v2 for Linux or Standard_D2s_v3 for Windows.
- `--vnet-subnet-id` — The Resource Id of a subnet in an existing VNet into which to deploy the cluster.
- `--workload-runtime` — Set the workload runtime.
- `--zones -z` — Availability zones where agent nodes will be placed. Also, to install agent nodes to more than one zone you need to pass zone numbers separated by blanks. For example - To have all 3 zones, you are expected to enter `--zones 1 2 3`.

*Create a nodepool in an existing AKS cluster with ephemeral os enabled.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --node-osdisk-type Ephemeral --node-osdisk-size 48
```

*Create a nodepool with EncryptionAtHost enabled.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --enable-encryption-at-host
```

*Create a nodepool with UltraSSD enabled.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --enable-ultra-ssd
```

*Create a nodepool cluster with a specific OS SKU*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --os-sku Ubuntu
```

*Create a nodepool with FIPS-enabled OS*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --enable-fips-image
```

*create a kubernetes cluster with a snapshot id.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --kubernetes-version 1.20.9 --snapshot-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/snapshots/mysnapshot1"
```

*create a nodepool in an existing AKS cluster with host group id*
```azurecli
az aks nodepool add -g MyResourceGroup -n MyNodePool --cluster-name MyMC --host-group-id /subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/hostGroups/myHostGroup --node-vm-size VMSize
```

*create a nodepool with a Capacity Reservation Group(CRG) ID.*
```azurecli
az aks nodepool add -g MyResourceGroup -n MyNodePool --cluster-name MyMC --node-vm-size VMSize --crg-id "/subscriptions/SubID/resourceGroups/ResourceGroupName/providers/Microsoft.ContainerService/CapacityReservationGroups/MyCRGID"
```

*Create a nodepool with ip allocation mode set to "StaticBlock" and using a pod subnet ID*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster  --os-sku Ubuntu --pod-subnet-id /subscriptions/SubID/resourceGroups/AnotherResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/MySubnet --pod-ip-allocation-mode StaticBlock
```

*create a nodepool of type VirtualMachines*
```azurecli
az aks nodepool add -g MyResourceGroup -n MyNodePool --cluster-name MyMC --vm-set-type VirtualMachines --vm-sizes "VMSize1,VMSize2" --node-count 3
```

*Create a nodepool with KataVmIsolation enabled.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --os-sku AzureLinux --vm-size Standard_D4s_v3 --workload-runtime KataVmIsolation --node-count 1
```

## az aks nodepool add  (extension: aks-preview etc.)

Add a node pool to the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--allowed-host-ports` — Expose host ports on the node pool. When specified, format should be a comma-separated list of ranges with protocol, eg. 80/TCP,443/TCP,4000-5000/TCP. Must use VMSS agent pool type.
- `--asg-ids` — The IDs of the application security groups to which the node pool's network interface should belong. When specified, format should be a comma-separated list of IDs. Must use VMSS agent pool type.
- `--batch-soak-duration` — Wait time (in minutes) after draining a batch of nodes before proceeding to the next batch. Default is 15 minutes. Only for blue-green upgrades.
- `--change-reference` — The related change reference ID for this resource operation.
- `--crg-id` — The crg-id used to associate the new nodepool with the existed Capacity Reservation Group resource. Must use VMSS agent pool type.
- `--disable-upgrade-gate` — Disable upgrade gate for the node pool. Default: False.
- `--disable-windows-outbound-nat` — Disable Windows OutboundNAT on Windows agent node pool. Must use VMSS agent pool type. Default: False.
- `--drain-batch-size` — Number or percentage of nodes to drain per batch during blue-green upgrades. Accepts an integer (e.g. '5') or percentage (e.g. '50%'). Default is 10%.
- `--drain-timeout` — When nodes are drain how many minutes to wait for all pods to be evicted.
- `--drain-timeout-bg` — Timeout (in minutes) to evict pods and gracefully terminate per node during blue-green upgrades. Default is 30 minutes.
- `--driver-type` — Specify the type of GPU driver to install when creating Windows agent pools. Valid values are "GRID" and "CUDA". If not provided, AKS selects the driver based on system compatibility. This option cannot be changed once the AgentPool has been created. The default is system selected.
- `--enable-artifact-streaming` — Enable artifact streaming for VirtualMachineScaleSets managed by a node pool, to speed up the cold-start of containers on a node through on-demand image loading. To use this feature, container images must also enable artifact streaming on ACR. If not specified, the default is false. Default: False.
- `--enable-cluster-autoscaler -e` — Enable cluster autoscaler. Must use VMSS agent pool type. Default: False.
- `--enable-encryption-at-host` — Enable EncryptionAtHost on agent node pool. Default: False.
- `--enable-fips-image` — Use FIPS-enabled OS on agent nodes. Required and always enabled when --os-sku is Windows2025; cannot be disabled for these node pools. Default: False.
- `--enable-managed-dranet` — Enable Managed DRANET on the node pool. Default: False.
- `--enable-managed-gpu` — Enable the Managed GPU experience, which installs additional components like DCGM metrics for monitoring on top of the GPU driver. For more details, visit aka.ms/aks/managed-gpu. Default: False.
- `--enable-node-public-ip` — Enable VMSS node public IP. Must use VMSS agent pool type. Default: False.
- `--enable-osdisk-fc --enable-osdisk-full-caching` — Enable the full-cache ephemeral OS disk feature for the node pool. Default: False.
- `--enable-secure-boot` — Enable Secure Boot on agent node pool. Must use VMSS agent pool type. Default: False.
- `--enable-ultra-ssd` — Enable UltraSSD on agent node pool. Must use VMSS agent pool type. Default: False.
- `--enable-upgrade-gate` — Enable upgrade gate for the node pool. Upgrades of this node pool wait for health signal validation and abort if unhealthy signals are observed. Default: False.
- `--enable-vtpm` — Enable vTPM on agent node pool. Must use VMSS agent pool type. Default: False.
- `--eviction-policy` — The eviction policy of the Spot node pool. It can only be set when --priority is Spot. Default: Delete.
- `--final-soak-duration` — Wait time (in minutes) after all old nodes are drained before removing them. Default is 60 minutes. Only for blue-green upgrades.
- `--gateway-prefix-size` — The size of Public IPPrefix attached to the Gateway-mode node pool. The node pool must be in Gateway mode.
- `--gpu-driver` — Whether to install driver for GPU node pool. Possible values are "Install" or "None". Default is "Install".
- `--gpu-driver-mode --managed-gpu-driver-mode` — Specify the Managed GPU driver mode. Valid values are "DRA" and "DevicePlugin". The default is "DevicePlugin". Requires `--enable-managed-gpu` to be set to true.
- `--gpu-instance-profile` — GPU instance profile to partition multi-gpu Nvidia GPUs.
- `--gpu-mig-profiles` — Space-separated ordered list of MIG partition profiles. Valid values are "MIG1g", "MIG2g", "MIG3g", "MIG4g", and "MIG7g".
- `--gpu-mig-strategy` — Specify the MIG (Multi-Instance GPU) strategy for managed MIG support. Valid values are "Single" and "Mixed". When not specified, managed MIG is disabled.
- `--host-group-id` — (PREVIEW) The fully qualified dedicated host group id used to provision agent node pool. Must use VMSS agent pool type.
- `--if-match` — The value provided will be compared to the ETag of the agentpool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool.
- `--if-none-match` — Set to '*' to allow a new agentpool to be created, but to prevent updating an existing agentpool. Other values will be ignored.
- `--kubelet-config` — Kubelet configurations for agent nodes.
- `--kubernetes-version -k` — Version of Kubernetes to use for creating the cluster, such as "1.7.12" or "1.8.7".
- `--labels` — The node labels for the node pool. See https://aka.ms/node-labels for syntax of labels.
- `--linux-os-config` — OS configurations for Linux agent nodes.
- `--localdns-config` — Set the localDNS Profile for a nodepool with a JSON config file.
- `--max-blocked-nodes` — The maximum number or percentage of extra nodes that are allowed to be blocked in the agent pool during an upgrade when undrainable node behavior is Cordon. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--max-count` — Maximum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [0, 1000] for user nodepool, and [1,1000] for system nodepool.
- `--max-pods -m` — The maximum number of pods deployable to a node. Default: 0.
- `--max-surge` — Extra nodes used to speed upgrade. When specified, it represents the number or percent used, eg. 5 or 33%.
- `--max-unavailable` — The maximum number or percentage of nodes that can be simultaneously unavailable during upgrade. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--message-of-the-day` — Path to a file containing the desired message of the day. Only valid for linux nodes. Will be written to /etc/motd.
- `--min-count` — Minimun nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [0, 1000] for user nodepool, and [1,1000] for system nodepool.
- `--mode` — The mode for a node pool which defines a node pool's primary function. If set as "System", AKS prefers system pods scheduling to node pools with mode `System`. If set as "ManagedSystem", all other properties except name and mode will be reset and managed by AKS. Learn more at https://aka.ms/aks/node Default: User.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes in the Kubernetes agent pool. After creating a cluster, you can change the size of its node pool with `az aks scale`. Default: 3.
- `--node-osdisk-size` — Size in GiB of the OS disk for each node in the agent pool. Minimum 30 GiB. Default: 0.
- `--node-osdisk-type` — OS disk type to be used for machines in a given agent pool. Defaults to 'Ephemeral' when possible in conjunction with VM size and OS disk size. May not be changed for this pool after creation. ('Ephemeral' or 'Managed').
- `--node-public-ip-prefix-id` — Public IP prefix ID used to assign public IPs to VMSS nodes. Must use VMSS agent pool type.
- `--node-public-ip-prefix-ids` — Comma-separated list of public IP prefix resource IDs for dual-stack node public IPs (IPv4 and/or IPv6).
- `--node-public-ip-tags` — The ipTags of the node public IPs. Must use VMSS agent pool type.
- `--node-soak-duration` — The amount of time (in minutes) to wait after draining a node and before reimaging it and moving on to next node.
- `--node-taints` — The node taints for the node pool.
- `--node-vm-size -s` — Size of Virtual Machines to create as Kubernetes nodes. If the user does not specify one, server will select a default VM size for her/him.
- `--os-sku` — The os-sku of the agent node pool. Ubuntu, Ubuntu2204, Ubuntu2404, Ubuntu2604, CBLMariner, AzureLinux, AzureLinux3, AzureLinuxOSGuard, AzureLinux3OSGuard, AzureContainerLinux, or Flatcar when os-type is Linux, default is Ubuntu if not set; Windows2019, Windows2022, Windows2025, or WindowsAnnual when
- `--os-type` — The OS Type. Linux or Windows. Windows not supported yet for "VirtualMachines" VM set type.
- `--pis-id --prepared-image-specification-id` — The resource ID of the prepared image specification to use for provisioning nodes in the node pool.
- `--pod-ip-allocation-mode` — Set the ip allocation mode for how Pod IPs from the Azure Pod Subnet are allocated to the nodes in the AKS cluster. The choice is between dynamic batches of individual IPs or static allocation of a set of CIDR blocks. Accepted Values are "DynamicIndividual" or "StaticBlock".
- `--pod-subnet-id` — The ID of a subnet in an existing VNet into which to assign pods in the cluster (requires azure network-plugin).
- `--ppg` — The ID of a PPG. Must use VMSS agent pool type.
- `--priority` — The priority of the node pool. Default: Regular.
- `--scale-down-mode` — Describes how VMs are added to or removed from nodepools. Default: Delete.
- `--secondary-network-interfaces --secondary-nics` — Secondary network interface configurations as a JSON string or `@filename`.
- `--snapshot-id` — The source snapshot id used to create this nodepool. Must use VMSS agent pool type.
- `--spot-max-price` — It can only be set when --priority is Spot. Specify the maximum price you are willing to pay in US Dollars. Possible values are any decimal value greater than zero or -1 which indicates default price to be up-to on-demand. It can only include up to 5 decimal places. Default: nan.
- `--ssh-access` — Configure SSH setting for the node pool. Use "disabled" to disable SSH access, "localuser" to enable SSH access using private key. Default: localuser.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--undrainable-node-behavior` — Define the behavior for undrainable nodes during upgrade. The value should be "Cordon" or "Schedule". The default value is "Schedule".
- `--upgrade-strategy` — Upgrade strategy for the node pool. Allowed values are "Rolling" or "BlueGreen". Default is "Rolling".
- `--vm-set-type` — Agent pool vm set type. VirtualMachineScaleSets, AvailabilitySet, VirtualMachines(Preview) or FlexNodes(Preview).
- `--vm-sizes` — Comma-separated list of sizes. Must use VirtualMachines agent pool type.
- `--vnet-subnet-id` — The ID of a subnet in an existing VNet into which to deploy the cluster.
- `--workload-runtime` — Determines the type of workload a node can run. Defaults to OCIContainer. Default: OCIContainer.
- `--zones -z` — Space-separated list of availability zones where agent nodes will be placed. Must use VMSS agent pool type.

*Create a nodepool in an existing AKS cluster with ephemeral os enabled.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --node-osdisk-type Ephemeral --node-osdisk-size 48
```

*Create a nodepool with EncryptionAtHost enabled.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --enable-encryption-at-host
```

*Create a nodepool with a specific os-sku*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster  --os-sku Ubuntu
```

*Create a nodepool which can run wasm workloads.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster  --workload-runtime WasmWasi
```

*create a kubernetes cluster with a snapshot id.*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --kubernetes-version 1.20.9 --snapshot-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/snapshots/mysnapshot1"
```

*create a nodepool with a Capacity Reservation Group(CRG) ID.*
```azurecli
az aks nodepool add -g MyResourceGroup -n MyNodePool --cluster-name MyMC --node-vm-size VMSize --crg-id "/subscriptions/SubID/resourceGroups/ResourceGroupName/providers/Microsoft.ContainerService/CapacityReservationGroups/MyCRGID"
```

*create a nodepool in an existing AKS cluster with host group id*
```azurecli
az aks nodepool add -g MyResourceGroup -n MyNodePool --cluster-name MyMC --host-group-id /subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/hostGroups/myHostGroup --node-vm-size VMSize
```

*Create a nodepool with ip allocation mode set to "StaticBlock" and using a pod subnet ID*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster  --os-sku Ubuntu --pod-subnet-id /subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/MySubnet --pod-ip-allocation-mode StaticBlock
```

*Create a nodepool of type VirtualMachines*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --vm-set-type VirtualMachines --vm-sizes "Standard_D4s_v3,Standard_D8s_v3" --node-count 3
```

*Create a FlexNodes pool for customer-provided machines*
```azurecli
az aks nodepool add -g MyResourceGroup -n flexpool --cluster-name MyManagedCluster --vm-set-type FlexNodes --kubernetes-version 1.32
```

*Create a nodepool with ManagedSystem mode*
```azurecli
az aks nodepool add -g MyResourceGroup -n managedsystem1 --cluster-name MyManagedCluster --mode ManagedSystem
```

*Create a node pool with blue-green upgrade strategy and default parameters*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --upgrade-strategy BlueGreen
```

*Create a node pool with an ordered mixed MIG profile layout*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --enable-managed-gpu --gpu-mig-strategy Mixed --gpu-mig-profiles MIG1g MIG2g MIG2g MIG2g
```

*Create a node pool with upgrade gate enabled*
```azurecli
az aks nodepool add -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --enable-upgrade-gate
```

## az aks nodepool delete

Delete the agent pool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--if-match` — The value provided will be compared to the ETag of the node pool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool.
- `--ignore-pdb -i` — Delete an existing nodepool without considering Pod Disruption Budget.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Delete an agent pool with ignore-pdb*
```azurecli
az aks nodepool delete --resource-group MyResourceGroup --cluster-name MyManagedCluster --name nodepool1 --if-match etag --ignore-pdb
```

## az aks nodepool delete  (extension: aks-preview etc.)

Delete the agent pool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--if-match` — The value provided will be compared to the ETag of the node pool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool.
- `--ignore-pod-disruption-budget -i` — (PREVIEW) ignore-pod-disruption-budget deletes an existing nodepool without considering Pod Disruption Budget.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Delete an agent pool with ignore-pod-disruption-budget*
```azurecli
az aks nodepool delete --resource-group MyResourceGroup --cluster-name MyManagedCluster --name nodepool1 --ignore-pod-disruption-budget=true
```

## az aks nodepool delete-machines

Delete specific machines in an agentpool for a managed cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--machine-names` — Space-separated list of machine names from the agent pool to be deleted.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Delete specific machines in an agent pool*
```azurecli
az aks nodepool delete-machines -g myResourceGroup --nodepool-name nodepool1 --cluster-name myAKSCluster --machine-names machine1
```

## az aks nodepool delete-machines  (extension: aks-preview etc.)

Delete specific machines in an agentpool for a managed cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--machine-names` — Space-separated list of machine names from the agent pool to be deleted.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Delete specific machines in an agent pool*
```azurecli
az aks nodepool delete-machines -g myResourceGroup --nodepool-name nodepool1 --cluster-name myAKSCluster --machine-names machine1
```

## az aks nodepool get-bootstrap-data  (extension: aks-preview etc.)

Get bootstrap data for a FlexNodes pool.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get bootstrap data for a FlexNodes pool*
```azurecli
az aks nodepool get-bootstrap-data -g MyResourceGroup --cluster-name MyManagedCluster -n flexpool
```

## az aks nodepool get-rollback-versions

Get the available rollback versions for an agent pool of the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the available rollback versions for an agent pool.*
```azurecli
az aks nodepool get-rollback-versions --resource-group MyResourceGroup --cluster-name MyManagedCluster --nodepool-name MyNodePool
```

## az aks nodepool get-rollback-versions  (extension: aks-preview etc.)

Get the available rollback versions for an agent pool of the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the available rollback versions for an agent pool.*
```azurecli
az aks nodepool get-rollback-versions --resource-group MyResourceGroup --cluster-name MyManagedCluster --nodepool-name MyNodePool
```

## az aks nodepool get-upgrades

Get the available upgrade versions for an agent pool of the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the available upgrade versions for an agent pool of the managed Kubernetes cluster.*
```azurecli
az aks nodepool get-upgrades --resource-group MyResourceGroup --cluster-name MyManagedCluster --nodepool-name MyNodePool
```

## az aks nodepool get-upgrades  (extension: aks-preview etc.)

Get the available upgrade versions for an agent pool of the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the available upgrade versions for an agent pool of the managed Kubernetes cluster.*
```azurecli
az aks nodepool get-upgrades --resource-group MyResourceGroup --cluster-name MyManagedCluster --nodepool-name MyNodePool
```

## az aks nodepool list

List node pools in the managed Kubernetes cluster. To get list of nodes in the cluster run `kubectl get nodes` command.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks nodepool list  (extension: aks-preview etc.)

List node pools in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks nodepool operation-abort

Abort last running operation on nodepool.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Abort operation on agent pool*
```azurecli
az aks nodepool operation-abort -g myResourceGroup --nodepool-name nodepool1 --cluster-name myAKSCluster
```

## az aks nodepool operation-abort  (extension: aks-preview etc.)

Abort last running operation on nodepool.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Abort operation on agent pool*
```azurecli
az aks nodepool operation-abort -g myResourceGroup --nodepool-name nodepool1 --cluster-name myAKSCluster
```

## az aks nodepool rollback

Rollback an agent pool to the most recently used configuration (N-1).

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Comma-separated key-value pairs to specify custom headers.
- `--change-reference` — The related change reference ID for this resource operation.
- `--if-match` — The value provided will be compared to the ETag of the node pool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool.
- `--if-none-match` — Set to '*' to allow a new node pool to be created, but to prevent updating an existing node pool. Other values will be ignored.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Rollback a nodepool to the most recently used version.*
```azurecli
az aks nodepool rollback --resource-group MyResourceGroup --cluster-name MyManagedCluster --nodepool-name MyNodePool
```

## az aks nodepool rollback  (extension: aks-preview etc.)

Rollback an agent pool to the most recently used configuration (N-1).

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--if-match` — The revision of the resource being updated. This should match the current revision.
- `--if-none-match` — Set to '*' to allow a new resource to be created, but to prevent updating an existing resource.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Rollback a nodepool to the most recently used version.*
```azurecli
az aks nodepool rollback --resource-group MyResourceGroup --cluster-name MyManagedCluster --nodepool-name MyNodePool
```

## az aks nodepool scale

Scale the node pool in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes in the Kubernetes node pool. Default: 3.

## az aks nodepool scale  (extension: aks-preview etc.)

Scale the node pool in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes in the Kubernetes node pool. Default: 3.
- `--use-patch-api` — Scale a node pool using the preview PATCH agent pool API instead of the default PUT API. Default: False.

## az aks nodepool show

Show the details for a node pool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks nodepool show  (extension: aks-preview etc.)

Show the details for a node pool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks nodepool start

Start stopped agent pool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Start agent pool in the managed cluster*
```azurecli
az aks nodepool start --nodepool-name nodepool1 -g MyResourceGroup --cluster-name MyManagedCluster
```

## az aks nodepool start  (extension: aks-preview etc.)

Start stopped agent pool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Start agent pool in the managed cluster*
```azurecli
az aks nodepool start --nodepool-name nodepool1 -g MyResourceGroup --cluster-name MyManagedCluster
```

## az aks nodepool stop

Stop running agent pool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Stop agent pool in the managed cluster*
```azurecli
az aks nodepool stop --nodepool-name nodepool1 -g MyResourceGroup --cluster-name MyManagedCluster
```

## az aks nodepool stop  (extension: aks-preview etc.)

Stop running agent pool in the managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Stop agent pool in the managed cluster*
```azurecli
az aks nodepool stop --nodepool-name nodepool1 -g MyResourceGroup --cluster-name MyManagedCluster
```

## az aks nodepool update

Update a node pool properties.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Comma-separated key-value pairs to specify custom headers.
- `--allowed-host-ports` — Expose host ports on the node pool. When specified, format should be a space-separated list of ranges with protocol, eg. `80/TCP 443/TCP 4000-5000/TCP`.
- `--asg-ids` — The IDs of the application security groups to which the node pool's network interface should belong. When specified, format should be a space-separated list of IDs.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disable-artifact-streaming` — Disable artifact streaming for VirtualMachineScaleSets managed by a Linux node pool. Default: False.
- `--disable-cluster-autoscaler -d` — Disable cluster autoscaler. For VirtualMachines pools, converts all autoscale profiles back to manual scale profiles. Default: False.
- `--disable-fips-image` — Switch to use non-FIPS-enabled OS on agent nodes. Default: False.
- `--disable-secure-boot` — Disable Secure Boot on on an existing Trusted Launch enabled agent node pool. Default: False.
- `--disable-vtpm` — Disable vTPM on an existing Trusted Launch enabled agent node pool. Default: False.
- `--drain-timeout` — When nodes are drain how many minutes to wait for all pods to be evicted.
- `--enable-artifact-streaming` — Enable artifact streaming for VirtualMachineScaleSets managed by a Linux node pool, to speed up the cold-start of containers on a node through on-demand image loading. To use this feature, container images must also enable artifact streaming on ACR. If not specified, the default is false. Default: False.
- `--enable-cluster-autoscaler -e` — Enable cluster autoscaler. For VirtualMachines pools, converts all manual scale profiles to autoscale profiles using the same min/max counts. Default: False.
- `--enable-fips-image` — Switch to use FIPS-enabled OS on agent nodes. Default: False.
- `--enable-managed-dranet` — Enable Managed DRANET on the node pool. Default: False.
- `--enable-secure-boot` — Enable Secure Boot on an existing Trusted Launch enabled agent node pool. Must use VMSS or VMs agent pool type. Default: False.
- `--enable-vtpm` — Enable vTPM on an existing Trusted Launch enabled agent node pool. Must use VMSS or VMs agent pool type. Default: False.
- `--gpu-driver` — Whether to install driver for GPU node pool. Possible values are "Install" or "None".
- `--if-match` — The value provided will be compared to the ETag of the node pool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool.
- `--if-none-match` — Set to '*' to allow a new node pool to be created, but to prevent updating an existing node pool. Other values will be ignored.
- `--labels` — The node labels for the node pool. See https://aka.ms/node-labels for syntax of labels.
- `--localdns-config` — Set the localDNS Profile for a nodepool with a JSON config file.
- `--max-count` — Maximum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [0, 1000] for user nodepool, and [1,1000] for system nodepool.
- `--max-surge` — Extra nodes used to speed upgrade. When specified, it represents the number or percent used, eg. 5 or 33%.
- `--max-unavailable` — The maximum number or percentage of nodes that can be simultaneously unavailable during upgrade. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--min-count` — Minimum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [0, 1000] for user nodepool, and [1,1000] for system nodepool.
- `--mode` — The mode for a node pool which defines a node pool's primary function. If set as "System", AKS prefers system pods scheduling to node pools with mode `System`. Learn more at https://aka.ms/aks/nodepool/mode.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-soak-duration` — The amount of time (in minutes) to wait after draining a node and before reimaging it and moving on to next node.
- `--node-taints` — The node taints for the node pool. You can update the existing node taint of a nodepool or create a new node taint for a nodepool. Pass the empty string `""` to remove all taints.
- `--os-sku` — The os-sku of the agent node pool.
- `--scale-down-mode` — Describe how VMs are added to or removed from nodepools.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--undrainable-node-behavior` — Define the behavior for undrainable nodes during upgrade. The value should be "Cordon" or "Schedule". The default value is "Schedule".
- `--update-cluster-autoscaler -u` — Update min-count or max-count for cluster autoscaler. Not supported for VirtualMachines pools; use 'az aks nodepool auto-scale update' instead. Default: False.

*Reconcile the nodepool back to its current state.*
```azurecli
az aks nodepool update -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

*Enable cluster-autoscaler within node count range [1,5]*
```azurecli
az aks nodepool update --enable-cluster-autoscaler --min-count 1 --max-count 5 -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

*Disable cluster-autoscaler for an existing cluster*
```azurecli
az aks nodepool update --disable-cluster-autoscaler -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

*Update min-count or max-count for cluster autoscaler.*
```azurecli
az aks nodepool update --update-cluster-autoscaler --min-count 1 --max-count 10 -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

## az aks nodepool update  (extension: aks-preview etc.)

Update a node pool properties.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--allowed-host-ports` — Expose host ports on the node pool. When specified, format should be a comma-separated list of ranges with protocol, eg. 80/TCP,443/TCP,4000-5000/TCP. Must use VMSS agent pool type.
- `--asg-ids` — The IDs of the application security groups to which the node pool's network interface should belong. When specified, format should be a comma-separated list of IDs. Must use VMSS agent pool type.
- `--batch-soak-duration` — Wait time (in minutes) after draining a batch of nodes before proceeding to the next batch. Default is 15 minutes. Only for blue-green upgrades.
- `--change-reference` — The related change reference ID for this resource operation.
- `--crg-id` — The Capacity Reservation Group (CRG) ID used to associate the existing nodepool with the existing Capacity Reservation Group resource.
- `--disable-artifact-streaming` — Disable artifact streaming for VirtualMachineScaleSets managed by a node pool. Default: False.
- `--disable-cluster-autoscaler -d` — Disable cluster autoscaler. For VirtualMachines pools, converts all autoscale profiles back to manual scale profiles. Default: False.
- `--disable-fips-image` — Switch to use non-FIPS-enabled OS on agent nodes. Default: False.
- `--disable-secure-boot` — Disable Secure Boot on on an existing Trusted Launch enabled agent node pool. Default: False.
- `--disable-upgrade-gate` — Disable upgrade gate for the node pool. Default: False.
- `--disable-vtpm` — Disable vTPM on an existing Trusted Launch enabled agent node pool. Default: False.
- `--drain-batch-size` — Number or percentage of nodes to drain per batch during blue-green upgrades. Accepts an integer (e.g. '5') or percentage (e.g. '50%'). Default is 10%.
- `--drain-timeout` — When nodes are drain how many minutes to wait for all pods to be evicted.
- `--drain-timeout-bg` — Timeout (in minutes) to evict pods and gracefully terminate per node during blue-green upgrades. Default is 30 minutes.
- `--enable-artifact-streaming` — Enable artifact streaming for VirtualMachineScaleSets managed by a node pool, to speed up the cold-start of containers on a node through on-demand image loading. To use this feature, container images must also enable artifact streaming on ACR. If not specified, the default is false. Default: False.
- `--enable-cluster-autoscaler -e` — Enable cluster autoscaler. For VMSS pools, enables autoscaler on the pool. For VirtualMachines pools, converts all manual scale profiles to autoscale profiles using the same min/max counts. Default: False.
- `--enable-fips-image` — Switch to use FIPS-enabled OS on agent nodes. Default: False.
- `--enable-managed-dranet` — Enable Managed DRANET on the node pool. Default: False.
- `--enable-managed-gpu` — Enable the Managed GPU experience, which installs additional components like DCGM metrics for monitoring on top of the GPU driver. For more details, visit aka.ms/aks/managed-gpu.
- `--enable-secure-boot` — Enable Secure Boot on an existing Trusted Launch enabled agent node pool. Must use VMSS agent pool type. Default: False.
- `--enable-upgrade-gate` — Enable upgrade gate for the node pool. Upgrades of this node pool wait for health signal validation and abort if unhealthy signals are observed. Default: False.
- `--enable-vtpm` — Enable vTPM on an existing Trusted Launch enabled agent node pool. Must use VMSS agent pool type. Default: False.
- `--final-soak-duration` — Wait time (in minutes) after all old nodes are drained before removing them. Default is 60 minutes. Only for blue-green upgrades.
- `--gpu-driver` — Whether to install driver for GPU node pool. Possible values are "Install" or "None".
- `--gpu-driver-mode --managed-gpu-driver-mode` — Specify the Managed GPU driver mode. Valid values are "DRA" and "DevicePlugin". The default is "DevicePlugin". Requires `--enable-managed-gpu` to be set to true.
- `--gpu-mig-profiles` — Space-separated ordered list of MIG partition profiles. Valid values are "MIG1g", "MIG2g", "MIG3g", "MIG4g", and "MIG7g".
- `--gpu-mig-strategy` — Specify the GPU Multi-Instance GPU (MIG) strategy. Allowed values: Single, Mixed.
- `--if-match` — The value provided will be compared to the ETag of the node pool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool.
- `--if-none-match` — Set to '*' to allow a new node pool to be created, but to prevent updating an existing node pool. Other values will be ignored.
- `--labels` — The node labels for the node pool. See https://aka.ms/node-labels for syntax of labels.
- `--localdns-config` — Set the localDNS Profile for a nodepool with a JSON config file.
- `--max-blocked-nodes` — The maximum number or percentage of extra nodes that are allowed to be blocked in the agent pool during an upgrade when undrainable node behavior is Cordon. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--max-count` — Maximum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [0, 1000] for user nodepool, and [1,1000] for system nodepool.
- `--max-surge` — Extra nodes used to speed upgrade. When specified, it represents the number or percent used, eg. 5 or 33%.
- `--max-unavailable` — The maximum number or percentage of nodes that can be simultaneously unavailable during upgrade. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--min-count` — Minimun nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [0, 1000] for user nodepool, and [1,1000] for system nodepool.
- `--mode` — The mode for a node pool which defines a node pool's primary function. If set as "System", AKS prefers system pods scheduling to node pools with mode `System`. If set as "ManagedSystem", all other properties except name and mode will be rejected and managed by AKS. Learn more at https://aka.ms/aks/n
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-public-ip-prefix-ids` — Comma-separated list of public IP prefix resource IDs for dual-stack node public IPs (IPv4 and/or IPv6).
- `--node-soak-duration` — The amount of time (in minutes) to wait after draining a node and before reimaging it and moving on to next node.
- `--node-taints` — The node taints for the node pool.
- `--node-vm-size -s` — VM size for Kubernetes nodes. For VMSS pools, changing this triggers a rolling upgrade to replace nodes with the new size (preview). For VirtualMachines pools, only configurable when updating autoscale settings.
- `--os-sku` — The os-sku of the agent node pool.
- `--pis-id --prepared-image-specification-id` — The resource ID of the prepared image specification to use for provisioning nodes in the node pool.
- `--scale-down-mode` — Describes how VMs are added to or removed from nodepools.
- `--ssh-access` — Update SSH setting for the node pool. Use "disabled" to disable SSH access, "localuser" to enable SSH access using private key.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--undrainable-node-behavior` — Define the behavior for undrainable nodes during upgrade. The value should be "Cordon" or "Schedule". The default value is "Schedule".
- `--update-cluster-autoscaler -u` — Update min-count or max-count for cluster autoscaler. Not supported for VirtualMachines pools; use 'az aks nodepool auto-scale update' instead. Default: False.
- `--upgrade-strategy` — Upgrade strategy for the node pool. Allowed values are "Rolling" or "BlueGreen". Default is "Rolling".
- `--yes -y` — Do not prompt for confirmation. Default: False.
- `--zones -z` — Use `auto` to migrate a regional node pool to automatic zone placement. Other availability zone changes are subject to service restrictions.

*Reconcile the nodepool back to its current state.*
```azurecli
az aks nodepool update -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

*Enable upgrade gate for a node pool.*
```azurecli
az aks nodepool update -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --enable-upgrade-gate
```

*Enable cluster-autoscaler within node count range [1,5]*
```azurecli
az aks nodepool update --enable-cluster-autoscaler --min-count 1 --max-count 5 -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

*Disable cluster-autoscaler for an existing cluster*
```azurecli
az aks nodepool update --disable-cluster-autoscaler -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

*Update min-count or max-count for cluster autoscaler.*
```azurecli
az aks nodepool update --update-cluster-autoscaler --min-count 1 --max-count 10 -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

*Change a node pool to system mode*
```azurecli
az aks nodepool update --mode System -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster
```

*Update cluster autoscaler vm size, min-count and max-count for virtual machines node pool*
```azurecli
az aks nodepool update -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --update-cluster-autoscaler --node-vm-size "Standard_D2s_v3" --min-count 2 --max-count 4
```

*Resize VM size for a VMSS node pool (preview, requires AFEC registration)*
```azurecli
az aks nodepool update -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --node-vm-size Standard_D4s_v3
```

*Migrate a regional node pool to automatic zone placement.*
```azurecli
az aks nodepool update -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --zones auto
```

*Update a node pool with blue-green upgrade settings*
```azurecli
az aks nodepool update -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --drain-batch-size 50% --drain-timeout-bg 5 --batch-soak-duration 10 --final-soak-duration 10
```

*Add an IPv6 public IP prefix to an existing dual-stack node pool (grows the assigned prefixes; existing nodes are recreated with the new public IPs)*
```azurecli
az aks nodepool update -g MyResourceGroup -n nodepool1 --cluster-name MyManagedCluster --node-public-ip-prefix-ids "/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Network/publicIPPrefixes/<v4prefix>,/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Network/publicIPPrefixes/<v6prefix>"
```

*Update a nodepool with a Capacity Reservation Group(CRG) ID.*
```azurecli
az aks nodepool update -g MyResourceGroup -n MyNodePool --cluster-name MyMC --node-vm-size VMSize --crg-id "/subscriptions/SubID/resourceGroups/ResourceGroupName/providers/Microsoft.Compute/CapacityReservationGroups/MyCRGID"
```

## az aks nodepool upgrade

Upgrade the node pool in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Comma-separated key-value pairs to specify custom headers.
- `--change-reference` — The related change reference ID for this resource operation.
- `--drain-timeout` — When nodes are drain how long to wait for all pods to be evicted.
- `--if-match` — The value provided will be compared to the ETag of the node pool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool. For upgrade node image version requests this will
- `--if-none-match` — Set to '*' to allow a new node pool to be created, but to prevent updating an existing node pool. Other values will be ignored.
- `--kubernetes-version -k` — Version of Kubernetes to upgrade the node pool to, such as "1.16.9".
- `--max-surge` — Extra nodes used to speed upgrade. When specified, it represents the number or percent used, eg. 5 or 33% (mutually exclusive with "--node-image-only". See "az aks nodepool update --max-surge" to update max surge before upgrading with "--node-image-only").
- `--max-unavailable` — The maximum number or percentage of nodes that can be simultaneously unavailable during upgrade. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-image-only` — Only upgrade agent pool's node image. Default: False.
- `--node-soak-duration` — The amount of time (in minutes) to wait after draining a node and before reimaging it and moving on to next node.
- `--snapshot-id` — The source snapshot id used to upgrade this nodepool.
- `--undrainable-node-behavior` — Define the behavior for undrainable nodes during upgrade. The value should be "Cordon" or "Schedule". The default value is "Schedule".
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks nodepool upgrade  (extension: aks-preview etc.)

Upgrade the node pool in a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--batch-soak-duration` — Wait time (in minutes) after draining a batch of nodes before proceeding to the next batch. Default is 15 minutes. Only for blue-green upgrades.
- `--change-reference` — The related change reference ID for this resource operation.
- `--drain-batch-size` — Number or percentage of nodes to drain per batch during blue-green upgrades. Accepts an integer (e.g. '5') or percentage (e.g. '50%'). Default is 10%.
- `--drain-timeout` — When nodes are drain how many minutes to wait for all pods to be evicted.
- `--drain-timeout-bg` — Timeout (in minutes) to evict pods and gracefully terminate per node during blue-green upgrades. Default is 30 minutes.
- `--final-soak-duration` — Wait time (in minutes) after all old nodes are drained before removing them. Default is 60 minutes. Only for blue-green upgrades.
- `--if-match` — The value provided will be compared to the ETag of the node pool, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new agentpool. For upgrade node image version requests this will
- `--if-none-match` — Set to '*' to allow a new node pool to be created, but to prevent updating an existing node pool. Other values will be ignored.
- `--kubernetes-version -k` — Version of Kubernetes to upgrade the node pool to, such as "1.11.12".
- `--max-blocked-nodes` — The maximum number or percentage of extra nodes that are allowed to be blocked in the agent pool during an upgrade when undrainable node behavior is Cordon. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--max-surge` — Extra nodes used to speed upgrade. When specified, it represents the number or percent used, eg. 5 or 33%.
- `--max-unavailable` — The maximum number or percentage of nodes that can be simultaneously unavailable during upgrade. When specified, it represents the number or percent used, eg. 1 or 5%.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-image-only` — Only upgrade agent pool's node image. Default: False.
- `--node-soak-duration` — The amount of time (in minutes) to wait after draining a node and before reimaging it and moving on to next node.
- `--snapshot-id` — The source snapshot id used to upgrade this nodepool. Must use VMSS agent pool type.
- `--undrainable-node-behavior` — Define the behavior for undrainable nodes during upgrade. The value should be "Cordon" or "Schedule". The default value is "Schedule".
- `--upgrade-strategy` — Upgrade strategy for the node pool. Allowed values are "Rolling" or "BlueGreen". Default is "Rolling".
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks nodepool wait

Wait for a node pool to reach a desired state.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name --nodepool-name -n` — The node pool name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Wait for a node pool to reach a desired state, polling every minute for up to thirty minutes.*
```azurecli
az aks nodepool wait --created --interval 60 --cluster-name MyManagedCluster --resource-group MyResourceGroup --nodepool-name MyNodePool --timeout 1800
```
