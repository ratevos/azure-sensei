# az aksarc

> Source: https://learn.microsoft.com/en-us/cli/azure/aksarc  
> Microsoft doc last updated: unknown

Manage provisioned clusters.

Subgroups and commands: `az_aksarc_create`, `az_aksarc_delete`, `az_aksarc_deploy`, `az_aksarc_get-credentials`, `az_aksarc_get-logs`, `az_aksarc_get-upgrades`, `az_aksarc_get-versions`, `az_aksarc_list`, `az_aksarc_logs`, `az_aksarc_logs_hci`, `az_aksarc_nodepool`, `az_aksarc_nodepool_add`, `az_aksarc_nodepool_delete`, `az_aksarc_nodepool_list`, `az_aksarc_nodepool_scale`, `az_aksarc_nodepool_show`, `az_aksarc_nodepool_update`, `az_aksarc_notice`, `az_aksarc_release`, `az_aksarc_release_download`, `az_aksarc_release_save`, `az_aksarc_show`, `az_aksarc_undeploy`, `az_aksarc_update`, `az_aksarc_upgrade`, `az_aksarc_vmsize`, `az_aksarc_vmsize_list`, `az_aksarc_vnet`, `az_aksarc_vnet_create`, `az_aksarc_vnet_delete`, `az_aksarc_vnet_list`, `az_aksarc_vnet_show`

## az aksarc create  (extension: aks-preview etc.)

Creates the provisioned cluster.

**Required parameters**

- `--custom-location` — Name or ID of the custom location to use for the provisioned cluster.
- `--name -n` — Name of the provisioned cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.
- `--vnet-id --vnet-ids` — ARM resource ID of aksarc virtual network or Azure Local logical network.

**Optional parameters**

- `--aad-admin-group-object-ids -i` — Comma-separated list of aad group object IDs that will be set as cluster admin on the provisioned cluster.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--ca-certs --custom-ca-trust-certificates` — Path to a file containing custom CA trust certificates for the security profile. The file can contain multiple PEM format certificates (up to 10). Each certificate will be base64 encoded and added to the trust store on all nodes.
- `--ca-profile --cluster-autoscaler-profile` — Space-separated list of key=value pairs for configuring cluster autoscaler. Pass an empty string to clear the profile.
- `--change-reference` — The related change reference ID for this resource operation.
- `--control-plane-count --control-plane-node-count` — Number of control plane nodes.
- `--control-plane-ip` — Kubernetes APIServer IPAddress. The IPAddress should be routable from Azure Resource Bridge Appliance VM.It should be part of the Network subnet being referenced.The cluster creation may fail or timeout if a non-routable IPAddress is passed.
- `--control-plane-vm-size` — VM Size of control plane.
- `--disable-nfs-driver` — Disable NFS driver for the provisioned cluster. Default: False.
- `--disable-smb-driver` — Disable SMB driver for the provisioned cluster. Default: False.
- `--enable-ahub` — Enable Azure Hybrid User Benefits (AHUB) for the provisioned cluster. Default: False.
- `--enable-ai-toolchain-operator --enable-kaito` — Enable AI Toolchain Operator for the provisioned cluster. Default: False.
- `--enable-azure-rbac` — Enable Azure RBAC to control authorization checks on cluster. Default: False.
- `--enable-cluster-autoscaler -e` — Enable cluster auto-scaler for the provisioned cluster. Default: False.
- `--enable-oidc-issuer` — Enable OIDC issuer. Default: False.
- `--enable-wi --enable-workload-identity` — Enable workload identity addon. Default: False.
- `--gateway-id` — Gateway Arm ID of the provisioned cluster.
- `--generate-ssh-keys` — Generate ssh key-pair if not present. Default: False.
- `--gpu-count-per-node` — Number of gpus attached to a node.
- `--kubernetes-version -k` — The kubernetes version of the provisioned cluster.
- `--load-balancer-count` — Number of load balancer nodes.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--max-count` — The maximum number of nodes for auto-scaling.
- `--max-pods -m` — Maximum number of pods that can run on a node.
- `--min-count` — The minimum number of nodes for auto-scaling.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes to be created in the nodepool. Default: 1.
- `--node-vm-size` — VM Size of the nodes in the nodepool.
- `--nodepool-labels` — Space-separated labels: key[=value] [key[=value] ...].
- `--nodepool-taints` — Comma-separated list of nodepool taints.
- `--pod-cidr` — The CIDR notation IP ranges from which to assign pod IPs.
- `--ssh-auth-ips --ssh-authorized-ip-ranges` — Comma-separated list of IP addresses or CIDR that are allowed to ssh to the cluster vm.
- `--ssh-key-value` — Path to the ssh public key to be injected into the control plane. Default: ~\.ssh\id_rsa.pub.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--validate` — Validate the cluster's input parameters without actually creating the cluster. Default: False.

*PutProvisionedCluster*
```azurecli
az aksarc create --resource-group sample-rg --custom-location sample-cl --name sample-aksarccluster --vnet-ids "vnet-arm-id"
```

## az aksarc delete  (extension: aks-preview etc.)

Deletes the provisioned cluster.

**Required parameters**

- `--name -n` — Name of the provisioned cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*DeleteProvisionedCluster*
```azurecli
az aksarc delete --name "sample-aksarccluster" --resource-group "sample-rg"
```

## az aksarc deploy  (extension: aks-preview etc.)

Deploy a full AKS baremetal cluster onto one or more existing Arc-for-Servers (BareMetal) hosts.

**Required parameters**

- `--arc-machine-name --arc-machine-names --machine-names -m` — Space-separated names of the existing Arc-enabled (Arc-for-Servers) machines in the resource group to form the cluster device pool. Provide one for a single-node pool or several for a multi-node pool. This is the only required input; all other cluster resources are auto-derived.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--enable-wi --enable-workload-identity` — Enable workload identity and the OIDC issuer required for Azure IoT Operations. Default: False.
- `--hci-rp-object-id` — Tenant-specific object ID of the Microsoft.AzureStackHCI resource provider service principal. When omitted, the CLI uses HCI_RP_OBJECT_ID if set, then falls back to Microsoft Graph.
- `--kubernetes-version -k` — Kubernetes versioned bundle for the cluster, such as 1.35.5-20260701. When omitted, the AKS Arc operator selects its current default version.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--validate` — Validate the deployment template without actually deploying. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Deploy a single-node AKS baremetal cluster*
```azurecli
az aksarc deploy --resource-group sample-rg --arc-machine-names myArcHost
```

*Deploy a multi-node AKS baremetal cluster*
```azurecli
az aksarc deploy --resource-group sample-rg --arc-machine-names host1 host2 host3
```

*Deploy with WorkloadIdentity support enabled*
```azurecli
az aksarc deploy --resource-group sample-rg --arc-machine-names myArcHost --enable-workload-identity
```

*Deploy a specific Kubernetes versioned bundle*
```azurecli
az aksarc deploy --resource-group sample-rg --arc-machine-names myArcHost --kubernetes-version 1.35.5-20260701
```

*Deploy without Microsoft Graph lookup*
```azurecli
az aksarc deploy --resource-group sample-rg --arc-machine-names myArcHost --hci-rp-object-id <hci-rp-object-id>
```

*Validate without deploying*
```azurecli
az aksarc deploy --resource-group sample-rg --arc-machine-names host1 host2 --validate
```

## az aksarc get-credentials  (extension: aks-preview etc.)

Get local kubeconfig of the provisioned cluster.

**Required parameters**

- `--name -n` — Name of the provisioned cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--admin -a` — Get cluster administrator credentials. Default: False.
- `--change-reference` — The related change reference ID for this resource operation.
- `--context` — If specified, overwrite the default context name.
- `--file -f` — Kubernetes configuration file to update. If not provided, updates the file '~/.kube/config'. Default: ~\.kube\config.
- `--overwrite-existing` — Overwrite any existing cluster entry with the same name. Default: False.

*GetAdminCredential*
```azurecli
az aksarc get-credentials --name "sample-aksarccluster" --resource-group "sample-rg" --admin
```

*GetAADUserCredential*
```azurecli
az aksarc get-credentials --name "sample-aksarccluster" --resource-group "sample-rg"
```

## az aksarc get-logs  (extension: aks-preview etc.)

Collect logs from provisioned clusters and the underlying infrastructure.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--credentials-dir --ssh-key` — Path to SSH credentials to connect to nodes, either id_rsa file or directory is accepted.
- `--ip --ips` — IP addresses of nodes (control plane nodes or worker nodes) from which logs need to be collected.
- `--kubeconfig` — Path to kubeconfig file to connect to the cluster.
- `--out-dir` — Output directory to store collected logs. If not specified, logs will be stored in the current directory.

*Collect logs with IP address and SSH credentials*
```azurecli
az aksarc get-logs --ip 192.168.200.31 192.168.200.32 --ssh-key ~/.ssh --out-dir ./logs
```

*Collect logs with kubeconfig and SSH credentials, kubeconfig is only used to collect IP addresses, and ssh-key file path is used instead of directory*
```azurecli
az aksarc get-logs --kubeconfig ~/.kube/config --ssh-key ~/.ssh/id_rsa --out-dir ./logs
```

## az aksarc get-upgrades  (extension: aks-preview etc.)

Get the upgrade versions available for the provisioned cluster.

**Required parameters**

- `--name -n` — Name of the provisioned cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the upgrade versions available for the Hybrid AKS provisioned cluster*
```azurecli
az aksarc get-upgrades --name "samplecluster" --resource-group "sample-rg"
```

## az aksarc get-versions  (extension: aks-preview etc.)

List the supported Kubernetes versions in the specified custom location.

**Required parameters**

- `--custom-location` — Name of the custom location to use for displaying the supported k8s versions.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*VMListSkus*
```azurecli
az aksarc get-versions -g sample-rg --custom-location sample-cl
```

## az aksarc list  (extension: aks-preview etc.)

Lists the provisioned clusters in a resource group or in a subscription.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*ListProvisionedClusterByResourceGroup*
```azurecli
az aksarc list --resource-group "sample-rg"
```

*ListProvisionedClusterBySubscription*
```azurecli
az aksarc list
```

## az aksarc notice  (extension: aks-preview etc.)

Output NOTICE file to user specified filepath.

**Required parameters**

- `--output-filepath` — Output filepath for NOTICE file.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*GetNoticeFile*
```azurecli
az aksarc notice --output-filepath "./Notice"
```

## az aksarc show  (extension: aks-preview etc.)

Gets the provisioned cluster.

**Required parameters**

- `--name -n` — Name of the provisioned cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*GetProvisionedCluster*
```azurecli
az aksarc show --name "sample-aksarccluster" --resource-group "sample-rg"
```

## az aksarc undeploy  (extension: aks-preview etc.)

Tear down an AKS baremetal cluster previously created by 'az aksarc deploy'.

**Required parameters**

- `--arc-machine-name --arc-machine-names --machine-names -m` — Space-separated names of the Arc machines whose AKS Arc deployment should be torn down. Resource names are auto-derived from them.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Undeploy AKS Arc resources for the given Arc machines*
```azurecli
az aksarc undeploy --resource-group sample-rg --arc-machine-names host1 host2 host3
```

## az aksarc update  (extension: aks-preview etc.)

Updates the provisioned cluster.

**Required parameters**

- `--name -n` — Name of the provisioned cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aad-admin-group-object-ids -i` — Comma-separated list of aad group object IDs that will be set as cluster admin on the provisioned cluster.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--ca-certs --custom-ca-trust-certificates` — Path to a file containing custom CA trust certificates for the security profile. The file can contain multiple PEM format certificates (up to 10). Each certificate will be base64 encoded and added to the trust store on all nodes.
- `--ca-profile --cluster-autoscaler-profile` — Space-separated list of key=value pairs for configuring cluster autoscaler. Pass an empty string to clear the profile.
- `--change-reference` — The related change reference ID for this resource operation.
- `--control-plane-count --control-plane-node-count` — Number of nodes to scale the Control Plane to.
- `--control-plane-vm-size` — VM Size of control plane.
- `--disable-ahub` — Disable Azure Hybrid User Benefits (AHUB) for the provisioned cluster. Default: False.
- `--disable-ai-toolchain-operator --disable-kaito` — Disable AI Toolchain Operator for the provisioned cluster. Default: False.
- `--disable-cluster-autoscaler -d` — Disable cluster auto-scaler for the provisioned cluster. Default: False.
- `--disable-gateway` — Disable gateway for the provisioned cluster. Default: False.
- `--disable-nfs-driver` — Disable NFS driver for the provisioned cluster. Default: False.
- `--disable-smb-driver` — Disable SMB driver for the provisioned cluster. Default: False.
- `--enable-ahub` — Enable Azure Hybrid User Benefits (AHUB) for the provisioned cluster. Default: False.
- `--enable-ai-toolchain-operator --enable-kaito` — Enable AI Toolchain Operator for the provisioned cluster. Default: False.
- `--enable-cluster-autoscaler -e` — Enable cluster auto-scaler for the provisioned cluster. Default: False.
- `--enable-nfs-driver` — Enable NFS driver for the provisioned cluster. Default: False.
- `--enable-smb-driver` — Enable SMB driver for the provisioned cluster. Default: False.
- `--gateway-id` — Gateway Arm ID of the provisioned cluster.
- `--max-count` — The maximum number of nodes for auto-scaling.
- `--min-count` — The minimum number of nodes for auto-scaling.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--update-cluster-autoscaler -u` — Update cluster auto-scaler for the provisioned cluster. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*UpdateProvisionedCluster*
```azurecli
az aksarc update --tags additionalProperties="sample" --name "sample-aksarccluster" --resource-group "sample-rg"
```

*Enable Azure Hybrid User Benefits feature for a provisioned cluster.*
```azurecli
az aksarc update --name "sample-aksarccluster" --resource-group "sample-rg" --enable-ahub
```

*Disable Azure Hybrid User Benefits feature for a provisioned cluster.*
```azurecli
az aksarc update --name "sample-aksarccluster" --resource-group "sample-rg"--disable-ahub
```

*Scale Up Control Plane Nodes.*
```azurecli
az aksarc update --name "sample-aksarccluster" --resource-group "sample-rg" --control-plane-node-count 5
```

## az aksarc upgrade  (extension: aks-preview etc.)

Upgrades the provisioned cluster.

**Required parameters**

- `--name -n` — Name of the provisioned cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--kubernetes-version -k` — The kubernetes version of the provisioned cluster.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes` — Flag to disable confirmation prompts. Default: False.

*UpgradeProvisionedCluster*
```azurecli
az aksarc upgrade --name "sample-aksarccluster" --resource-group "sample-rg" --kubernetes-version "1.22.2"
```
