# az aks

> Source: https://learn.microsoft.com/en-us/cli/azure/aks  
> Microsoft doc last updated: unknown

Azure Kubernetes Service.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_addon`, `az_aks_addon_disable`, `az_aks_addon_enable`, `az_aks_addon_list`, `az_aks_addon_list-available`, `az_aks_addon_show`, `az_aks_addon_update`, `az_aks_agent`, `az_aks_agent-cleanup`, `az_aks_agent-init`, `az_aks_alert-config`, `az_aks_alert-config_add`, `az_aks_alert-config_delete`, `az_aks_alert-config_list`, `az_aks_alert-config_show`, `az_aks_alert-config_update`, `az_aks_app`, `az_aks_app_up`, `az_aks_applicationloadbalancer`, `az_aks_applicationloadbalancer_disable`, `az_aks_applicationloadbalancer_enable`, `az_aks_applicationloadbalancer_update`, `az_aks_approuting`, `az_aks_approuting_defaultdomain`, `az_aks_approuting_defaultdomain_show`, `az_aks_approuting_disable`, `az_aks_approuting_disable(aks-preview)`, `az_aks_approuting_enable`, `az_aks_approuting_enable(aks-preview)`, `az_aks_approuting_gateway`, `az_aks_approuting_gateway_istio`, `az_aks_approuting_gateway_istio_disable`, `az_aks_approuting_gateway_istio_disable(aks-preview)`, `az_aks_approuting_gateway_istio_enable`, `az_aks_approuting_gateway_istio_enable(aks-preview)`, `az_aks_approuting_update`, `az_aks_approuting_update(aks-preview)`, `az_aks_approuting_zone`, `az_aks_approuting_zone_add`, `az_aks_approuting_zone_add(aks-preview)`, `az_aks_approuting_zone_delete`, `az_aks_approuting_zone_delete(aks-preview)`, `az_aks_approuting_zone_list`, `az_aks_approuting_zone_list(aks-preview)`, `az_aks_approuting_zone_update`, `az_aks_approuting_zone_update(aks-preview)`, `az_aks_bastion`, `az_aks_bastion_disable`, `az_aks_bastion_enable`, `az_aks_bastion_tunnel`, `az_aks_bastion_update`, `az_aks_browse`, `az_aks_browse(aks-preview)`, `az_aks_check-acr`, `az_aks_check-network`, `az_aks_check-network_outbound`, `az_aks_command`, `az_aks_command_invoke`, `az_aks_command_result`, `az_aks_connection`, `az_aks_connection_create`, `az_aks_connection_create_app-insights`, `az_aks_connection_create_appconfig`, `az_aks_connection_create_cognitiveservices`, `az_aks_connection_create_confluent-cloud`, `az_aks_connection_create_cosmos-cassandra`, `az_aks_connection_create_cosmos-gremlin`, `az_aks_connection_create_cosmos-mongo`, `az_aks_connection_create_cosmos-sql`, `az_aks_connection_create_cosmos-table`, `az_aks_connection_create_eventhub`, `az_aks_connection_create_keyvault`, `az_aks_connection_create_mongodb-atlas`, `az_aks_connection_create_mysql`, `az_aks_connection_create_mysql-flexible`, `az_aks_connection_create_mysql-flexible(serviceconnector-passwordless)`, `az_aks_connection_create_neon-postgres`, `az_aks_connection_create_postgres`, `az_aks_connection_create_postgres-flexible`, `az_aks_connection_create_postgres-flexible(serviceconnector-passwordless)`, `az_aks_connection_create_redis`, `az_aks_connection_create_redis-enterprise`, `az_aks_connection_create_servicebus`, `az_aks_connection_create_signalr`, `az_aks_connection_create_sql`, `az_aks_connection_create_sql(serviceconnector-passwordless)`, `az_aks_connection_create_storage-blob`, `az_aks_connection_create_storage-file`, `az_aks_connection_create_storage-queue`, `az_aks_connection_create_storage-table`, `az_aks_connection_create_webpubsub`, `az_aks_connection_delete`, `az_aks_connection_list`, `az_aks_connection_list-configuration`, `az_aks_connection_list-support-types`, `az_aks_connection_show`, `az_aks_connection_update`, `az_aks_connection_update_app-insights`, `az_aks_connection_update_appconfig`, `az_aks_connection_update_cognitiveservices`, `az_aks_connection_update_confluent-cloud`, `az_aks_connection_update_cosmos-cassandra`, `az_aks_connection_update_cosmos-gremlin`, `az_aks_connection_update_cosmos-mongo`, `az_aks_connection_update_cosmos-sql`, `az_aks_connection_update_cosmos-table`, `az_aks_connection_update_eventhub`, `az_aks_connection_update_keyvault`, `az_aks_connection_update_mongodb-atlas`, `az_aks_connection_update_mysql`, `az_aks_connection_update_mysql-flexible`, `az_aks_connection_update_neon-postgres`, `az_aks_connection_update_postgres`, `az_aks_connection_update_postgres-flexible`, `az_aks_connection_update_redis`, `az_aks_connection_update_redis-enterprise`, `az_aks_connection_update_servicebus`, `az_aks_connection_update_signalr`, `az_aks_connection_update_sql`, `az_aks_connection_update_storage-blob`, `az_aks_connection_update_storage-file`, `az_aks_connection_update_storage-queue`, `az_aks_connection_update_storage-table`, `az_aks_connection_update_webpubsub`, `az_aks_connection_validate`, `az_aks_connection_wait`, `az_aks_create`, `az_aks_create(aks-preview)`, `az_aks_delete`, `az_aks_delete(aks-preview)`, `az_aks_disable-addons`, `az_aks_disable-addons(aks-preview)`, `az_aks_draft`, `az_aks_draft_create`, `az_aks_draft_generate-workflow`, `az_aks_draft_setup-gh`, `az_aks_draft_up`, `az_aks_draft_update`, `az_aks_egress-endpoints`, `az_aks_egress-endpoints_list`, `az_aks_enable-addons`, `az_aks_enable-addons(aks-preview)`, `az_aks_extension`, `az_aks_extension_create`, `az_aks_extension_delete`, `az_aks_extension_list`, `az_aks_extension_show`, `az_aks_extension_type`, `az_aks_extension_type_list`, `az_aks_extension_type_show`, `az_aks_extension_type_version`, `az_aks_extension_type_version_list`, `az_aks_extension_type_version_show`, `az_aks_extension_update`, `az_aks_get-credentials`, `az_aks_get-credentials(aks-preview)`, `az_aks_get-upgrades`, `az_aks_get-upgrades(aks-preview)`, `az_aks_get-versions`, `az_aks_get-versions(aks-preview)`, `az_aks_identity-binding`, `az_aks_identity-binding_create`, `az_aks_identity-binding_create(aks-preview)`, `az_aks_identity-binding_delete`, `az_aks_identity-binding_delete(aks-preview)`, `az_aks_identity-binding_list`, `az_aks_identity-binding_list(aks-preview)`, `az_aks_identity-binding_show`, `az_aks_identity-binding_show(aks-preview)`, `az_aks_identity-binding_update`, `az_aks_install-cli`, `az_aks_install-desktop`, `az_aks_jwtauthenticator`, `az_aks_jwtauthenticator_add`, `az_aks_jwtauthenticator_delete`, `az_aks_jwtauthenticator_list`, `az_aks_jwtauthenticator_show`, `az_aks_jwtauthenticator_update`, `az_aks_kanalyze`, `az_aks_kollect`, `az_aks_list`, `az_aks_list(aks-preview)`, `az_aks_list-vm-skus`, `az_aks_loadbalancer`, `az_aks_loadbalancer_add`, `az_aks_loadbalancer_delete`, `az_aks_loadbalancer_list`, `az_aks_loadbalancer_rebalance-nodes`, `az_aks_loadbalancer_show`, `az_aks_loadbalancer_update`, `az_aks_machine`, `az_aks_machine_add`, `az_aks_machine_list`, `az_aks_machine_list(aks-preview)`, `az_aks_machine_show`, `az_aks_machine_show(aks-preview)`, `az_aks_machine_update`, `az_aks_maintenanceconfiguration`, `az_aks_maintenanceconfiguration_add`, `az_aks_maintenanceconfiguration_add(aks-preview)`, `az_aks_maintenanceconfiguration_delete`, `az_aks_maintenanceconfiguration_delete(aks-preview)`, `az_aks_maintenanceconfiguration_list`, `az_aks_maintenanceconfiguration_list(aks-preview)`, `az_aks_maintenanceconfiguration_show`, `az_aks_maintenanceconfiguration_show(aks-preview)`, `az_aks_maintenanceconfiguration_update`, `az_aks_maintenanceconfiguration_update(aks-preview)`, `az_aks_maintenancewindow`, `az_aks_maintenancewindow_create`, `az_aks_maintenancewindow_delete`, `az_aks_maintenancewindow_list`, `az_aks_maintenancewindow_show`, `az_aks_maintenancewindow_update`, `az_aks_maintenancewindow_wait`, `az_aks_mesh`, `az_aks_mesh_disable`, `az_aks_mesh_disable(aks-preview)`, `az_aks_mesh_disable-egress-gateway`, `az_aks_mesh_disable-egress-gateway(aks-preview)`, `az_aks_mesh_disable-ingress-gateway`, `az_aks_mesh_disable-ingress-gateway(aks-preview)`, `az_aks_mesh_disable-istio-cni`, `az_aks_mesh_enable`, `az_aks_mesh_enable(aks-preview)`, `az_aks_mesh_enable-egress-gateway`, `az_aks_mesh_enable-egress-gateway(aks-preview)`, `az_aks_mesh_enable-ingress-gateway`, `az_aks_mesh_enable-ingress-gateway(aks-preview)`, `az_aks_mesh_enable-istio-cni`, `az_aks_mesh_get-revisions`, `az_aks_mesh_get-revisions(aks-preview)`, `az_aks_mesh_get-upgrades`, `az_aks_mesh_get-upgrades(aks-preview)`, `az_aks_mesh_proxy-redirection-mechanism`, `az_aks_mesh_upgrade`, `az_aks_mesh_upgrade_complete`, `az_aks_mesh_upgrade_complete(aks-preview)`, `az_aks_mesh_upgrade_rollback`, `az_aks_mesh_upgrade_rollback(aks-preview)`, `az_aks_mesh_upgrade_start`, `az_aks_mesh_upgrade_start(aks-preview)`, `az_aks_namespace`, `az_aks_namespace_add`, `az_aks_namespace_add(aks-preview)`, `az_aks_namespace_delete`, `az_aks_namespace_delete(aks-preview)`, `az_aks_namespace_get-credentials`, `az_aks_namespace_get-credentials(aks-preview)`, `az_aks_namespace_list`, `az_aks_namespace_list(aks-preview)`, `az_aks_namespace_show`, `az_aks_namespace_show(aks-preview)`, `az_aks_namespace_update`, `az_aks_namespace_update(aks-preview)`, `az_aks_nodepool`, `az_aks_nodepool_add`, `az_aks_nodepool_add(aks-preview)`, `az_aks_nodepool_auto-scale`, `az_aks_nodepool_auto-scale_add`, `az_aks_nodepool_auto-scale_add(aks-preview)`, `az_aks_nodepool_auto-scale_delete`, `az_aks_nodepool_auto-scale_delete(aks-preview)`, `az_aks_nodepool_auto-scale_update`, `az_aks_nodepool_auto-scale_update(aks-preview)`, `az_aks_nodepool_delete`, `az_aks_nodepool_delete(aks-preview)`, `az_aks_nodepool_delete-machines`, `az_aks_nodepool_delete-machines(aks-preview)`, `az_aks_nodepool_get-bootstrap-data`, `az_aks_nodepool_get-rollback-versions`, `az_aks_nodepool_get-rollback-versions(aks-preview)`, `az_aks_nodepool_get-upgrades`, `az_aks_nodepool_get-upgrades(aks-preview)`, `az_aks_nodepool_list`, `az_aks_nodepool_list(aks-preview)`, `az_aks_nodepool_manual-scale`, `az_aks_nodepool_manual-scale_add`, `az_aks_nodepool_manual-scale_add(aks-preview)`, `az_aks_nodepool_manual-scale_delete`, `az_aks_nodepool_manual-scale_delete(aks-preview)`, `az_aks_nodepool_manual-scale_update`, `az_aks_nodepool_manual-scale_update(aks-preview)`, `az_aks_nodepool_operation-abort`, `az_aks_nodepool_operation-abort(aks-preview)`, `az_aks_nodepool_rollback`, `az_aks_nodepool_rollback(aks-preview)`, `az_aks_nodepool_scale`, `az_aks_nodepool_scale(aks-preview)`, `az_aks_nodepool_show`, `az_aks_nodepool_show(aks-preview)`, `az_aks_nodepool_snapshot`, `az_aks_nodepool_snapshot_create`, `az_aks_nodepool_snapshot_create(aks-preview)`, `az_aks_nodepool_snapshot_delete`, `az_aks_nodepool_snapshot_delete(aks-preview)`, `az_aks_nodepool_snapshot_list`, `az_aks_nodepool_snapshot_list(aks-preview)`, `az_aks_nodepool_snapshot_show`, `az_aks_nodepool_snapshot_show(aks-preview)`, `az_aks_nodepool_snapshot_update`, `az_aks_nodepool_snapshot_update(aks-preview)`, `az_aks_nodepool_snapshot_wait`, `az_aks_nodepool_start`, `az_aks_nodepool_start(aks-preview)`, `az_aks_nodepool_stop`, `az_aks_nodepool_stop(aks-preview)`, `az_aks_nodepool_update`, `az_aks_nodepool_update(aks-preview)`, `az_aks_nodepool_upgrade`, `az_aks_nodepool_upgrade(aks-preview)`, `az_aks_nodepool_wait`, `az_aks_oidc-issuer`, `az_aks_oidc-issuer_rotate-signing-keys`, `az_aks_operation`, `az_aks_operation-abort`, `az_aks_operation-abort(aks-preview)`, `az_aks_operation_list`, `az_aks_operation_show`, `az_aks_operation_show-latest`, `az_aks_pod-identity`, `az_aks_pod-identity_add`, `az_aks_pod-identity_delete`, `az_aks_pod-identity_exception`, `az_aks_pod-identity_exception_add`, `az_aks_pod-identity_exception_delete`, `az_aks_pod-identity_exception_list`, `az_aks_pod-identity_exception_update`, `az_aks_pod-identity_list`, `az_aks_prepared-image-specification`, `az_aks_prepared-image-specification_create`, `az_aks_prepared-image-specification_delete`, `az_aks_prepared-image-specification_list`, `az_aks_prepared-image-specification_show`, `az_aks_prepared-image-specification_update`, `az_aks_prepared-image-specification_version`, `az_aks_prepared-image-specification_version_delete`, `az_aks_prepared-image-specification_version_list`, `az_aks_prepared-image-specification_version_show`, `az_aks_remove-dev-spaces`, `az_aks_rotate-certs`, `az_aks_rotate-certs(aks-preview)`, `az_aks_safeguards`, `az_aks_safeguards_create`, `az_aks_safeguards_create(aks-preview)`, `az_aks_safeguards_delete`, `az_aks_safeguards_delete(aks-preview)`, `az_aks_safeguards_list`, `az_aks_safeguards_list(aks-preview)`, `az_aks_safeguards_show`, `az_aks_safeguards_show(aks-preview)`, `az_aks_safeguards_update`, `az_aks_safeguards_update(aks-preview)`, `az_aks_safeguards_wait`, `az_aks_safeguards_wait(aks-preview)`, `az_aks_scale`, `az_aks_scale(aks-preview)`, `az_aks_show`, `az_aks_show(aks-preview)`, `az_aks_snapshot`, `az_aks_snapshot_create`, `az_aks_snapshot_delete`, `az_aks_snapshot_list`, `az_aks_snapshot_show`, `az_aks_start`, `az_aks_start(aks-preview)`, `az_aks_stop`, `az_aks_stop(aks-preview)`, `az_aks_trustedaccess`, `az_aks_trustedaccess_role`, `az_aks_trustedaccess_role_list`, `az_aks_trustedaccess_rolebinding`, `az_aks_trustedaccess_rolebinding_create`, `az_aks_trustedaccess_rolebinding_delete`, `az_aks_trustedaccess_rolebinding_list`, `az_aks_trustedaccess_rolebinding_show`, `az_aks_trustedaccess_rolebinding_update`, `az_aks_update`, `az_aks_update(aks-preview)`, `az_aks_update-credentials`, `az_aks_upgrade`, `az_aks_upgrade(aks-preview)`, `az_aks_use-dev-spaces`, `az_aks_use-dev-spaces(dev-spaces)`, `az_aks_wait`, `az_aks_wait(aks-preview)`

## az aks agent  (extension: aks-preview etc.)

Run AI assistant to analyze and troubleshoot Azure Kubernetes Service (AKS) clusters.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--max-steps` — Maximum number of steps the LLM can take to investigate the issue. Default: 40.
- `--mode` — The mode decides how the agent is deployed. Default: cluster.
- `--model` — Specify the LLM provider and model or deployment to use for the AI assistant.
- `--namespace` — The Kubernetes namespace where the AKS Agent is deployed. Required for cluster mode.
- `--no-echo-request` — Disable echoing back the question provided to AKS Agent in the output. Default: False.
- `--no-interactive` — Disable interactive mode. When set, the agent will not prompt for input and will run in batch mode. Default: False.
- `--refresh-toolsets` — Refresh the toolsets status. Default: False.
- `--show-tool-output` — Show the output of each tool that was called. Default: False.
- `--status` — Show AKS agent configuration and status information. Default: False.
- `<PROMPT>` — Ask any question and answer using available tools.

## az aks agent-cleanup  (extension: aks-preview etc.)

Cleanup and uninstall the AKS agent.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--mode` — The mode decides how the agent is deployed. Default: cluster.
- `--namespace` — The Kubernetes namespace where the AKS Agent is deployed. Required for cluster mode.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks agent-init  (extension: aks-preview etc.)

Initialize AKS agent helm deployment with LLM configuration and cluster role setup.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks browse

Show the dashboard for a Kubernetes cluster in a web browser.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disable-browser` — Don't launch a web browser after establishing port-forwarding. Default: False.
- `--listen-address` — The listening address for the dashboard. Default: 127.0.0.1.
- `--listen-port` — The listening port for the dashboard. Default: 8001.

*Show the dashboard for a Kubernetes cluster in a web browser. (autogenerated)*
```azurecli
az aks browse --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks browse  (extension: aks-preview etc.)

Show the dashboard for a Kubernetes cluster in a web browser.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--disable-browser` — Don't launch a web browser after establishing port-forwarding. Default: False.
- `--listen-address` — The listening address for the dashboard. Default: 127.0.0.1.
- `--listen-port` — The listening port for the dashboard. Default: 8001.

*Show the dashboard for a Kubernetes cluster in a web browser. (autogenerated)*
```azurecli
az aks browse --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks check-acr

Validate an ACR is accessible from an AKS cluster.

**Required parameters**

- `--acr` — The FQDN of the ACR.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--node-name` — The name of a specific node to perform acr pull test checks. If not specified, it will be checked on a random node.

*Validate the ACR is accessible from the AKS cluster.*
```azurecli
az aks check-acr --name MyManagedCluster --resource-group MyResourceGroup --acr myacr.azurecr.io
```

## az aks create

Create a new managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aad-admin-group-object-ids` — Comma-separated list of aad group object IDs that will be set as cluster admin.
- `--aad-tenant-id` — The ID of an Azure Active Directory tenant.
- `--aci-subnet-name` — The name of a subnet in an existing VNet into which to deploy the virtual nodes.
- `--acns-advanced-networkpolicies` — Enable advanced network policies (None, FQDN or L7) on a cluster when enabling advanced networking features with "--enable-acns".
- `--acns-datapath-acceleration-mode` — Set the datapath acceleration mode for Azure Container Networking Solution (ACNS) Performance. Valid values are 'BpfVeth' and 'None'.
- `--acns-transit-encryption-type` — Set transit encryption type for ACNS security.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--admin-username -u` — User account to create on node VMs for SSH access. Default: azureuser.
- `--aks-custom-headers` — Comma-separated key-value pairs to specify custom headers.
- `--ampls-resource-id` — Resource ID of Azure Monitor Private Link scope for Monitoring Addon.
- `--api-server-authorized-ip-ranges` — Comma-separated list of authorized apiserver IP ranges. Set to 0.0.0.0/32 to restrict apiserver traffic to node pools.
- `--apiserver-subnet-id` — The ID of a subnet in an existing VNet into which to assign control plane apiserver pods(requires --enable-apiserver-vnet-integration).
- `--app-routing-default-nginx-controller --ardnc` — Configure default nginx ingress controller type. Valid values are annotationControlled (default behavior), external, internal, or none.
- `--appgw-id` — Resource Id of an existing Application Gateway to use with AGIC. Use with ingress-azure addon.
- `--appgw-name` — Name of the application gateway to create/use in the node resource group. Use with ingress-azure addon.
- `--appgw-subnet-cidr` — Subnet CIDR to use for a new subnet created to deploy the Application Gateway. Use with ingress-azure addon.
- `--appgw-subnet-id` — Resource Id of an existing Subnet used to deploy the Application Gateway. Use with ingress-azure addon.
- `--appgw-watch-namespace` — Specify the namespace, which AGIC should watch. This could be a single string value, or a comma-separated list of namespaces.
- `--assign-identity` — Specify an existing user assigned identity for control plane's usage in order to manage cluster resource group.
- `--assign-kubelet-identity` — Specify an existing user assigned identity for kubelet's usage, which is typically used to pull image from ACR.
- `--attach-acr` — Grant the 'acrpull' role assignment to the ACR specified by name or resource ID.
- `--auto-upgrade-channel` — Specify the upgrade channel for autoupgrade.
- `--azure-keyvault-kms-key-id` — Identifier of Azure Key Vault key.
- `--azure-keyvault-kms-key-vault-network-access` — Network Access of Azure Key Vault.
- `--azure-keyvault-kms-key-vault-resource-id` — Resource ID of Azure Key Vault.
- `--azure-monitor-workspace-resource-id` — Resource ID of the Azure Monitor Workspace.
- `--bootstrap-artifact-source` — Configure artifact source when bootstraping the cluster. Default: Direct.
- `--bootstrap-container-registry-resource-id` — Configure container registry resource ID. Must use "Cache" as bootstrap artifact source.
- `--ca-certs --custom-ca-trust-certificates` — Path to a file containing up to 10 blank line separated certificates. Only valid for Linux nodes.
- `--ca-profile --cluster-autoscaler-profile` — Comma-separated list of key=value pairs for configuring cluster autoscaler. Pass an empty string to clear the profile.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-secret` — Secret associated with the service principal. This argument is required if `--service-principal` is specified.
- `--container-storage-version` — Set azure container storage version, the latest version will be installed by default.
- `--crg-id` — The crg id used to associate the new cluster with the existed Capacity Reservation Group resource.
- `--data-collection-settings` — Path to JSON file containing data collection settings for Monitoring addon.
- `--defender-config` — Path to JSON file containing Microsoft Defender profile configurations.
- `--disable-acns-observability` — Used to disable advanced networking observability features on a clusters when enabling advanced networking features with "--enable-acns".
- `--disable-acns-security` — Used to disable advanced networking security features on a clusters when enabling advanced networking features with "--enable-acns".
- `--disable-disk-driver` — Disable AzureDisk CSI Driver. Default: False.
- `--disable-file-driver` — Disable AzureFile CSI Driver. Default: False.
- `--disable-local-accounts` — If set to true, getting static credential will be disabled for this cluster. Default: False.
- `--disable-opentelemetry-logs-traces` — Disable the OpenTelemetry (OTLP) logs and traces receiver. Default: False.
- `--disable-opentelemetry-metrics` — Disable the OpenTelemetry (OTLP) metrics receiver. Default: False.
- `--disable-prometheus-metrics-scraping` — Disable Prometheus metrics scraping by the Azure Monitor agent. Requires --enable-azure-monitor-logs. Default: False.
- `--disable-public-fqdn` — Disable public fqdn feature for private cluster. Default: False.
- `--disable-rbac` — Disable Kubernetes Role-Based Access Control.
- `--disable-run-command` — Disable Run command feature for the cluster. Default: False.
- `--disable-snapshot-controller` — Disable CSI Snapshot Controller. Default: False.
- `--dns-name-prefix -p` — Prefix for hostnames that are created. If not specified, generate a hostname using the managed cluster and resource group names.
- `--dns-service-ip` — An IP address assigned to the Kubernetes DNS service.
- `--edge-zone` — The name of the Edge Zone.
- `--enable-aad` — Enable managed AAD feature for cluster. Default: False.
- `--enable-acns` — Enable advanced network functionalities on a cluster. Enabling this will incur additional costs. For non-cilium clusters, acns security will be disabled by default until further notice.
- `--enable-addons -a` — Enable the Kubernetes addons in a comma-separated list.
- `--enable-ahub` — Enable Azure Hybrid User Benefits (AHUB) for Windows VMs. Default: False.
- `--enable-ai-toolchain-operator` — Enable AI toolchain operator to the cluster. Default: False.
- `--enable-apiserver-vnet-integration` — Enable integration of user vnet with control plane apiserver pods. Default: False.
- `--enable-app-routing` — Enable Application Routing addon. Default: False.
- `--enable-app-routing-istio --enable-ari` — Enable Gateway API based ingress on App Routing via Istio without service mesh functionality. Default: False.
- `--enable-asm --enable-azure-service-mesh` — Enable Azure Service Mesh addon.
- `--enable-azure-container-storage` — Enable azure container storage. Can be used as a flag (defaults to True) or with a storage pool type value: (azureDisk, ephemeralDisk, elasticSan).
- `--enable-azure-keyvault-kms` — Enable Azure KeyVault Key Management Service. Default: False.
- `--enable-azure-monitor-app-monitoring` — Enable Azure Monitor Application Monitoring auto-instrumentation for a Kubernetes cluster. Default: False.
- `--enable-azure-monitor-logs` — Enable Azure Monitor logs (Container Insights) for the cluster using managed identity authentication. Default: False.
- `--enable-azure-monitor-metrics` — Enable a kubernetes cluster with the Azure Monitor managed service for Prometheus integration. Default: False.
- `--enable-azure-rbac` — Enable Azure RBAC to control authorization checks on cluster. Default: False.
- `--enable-blob-driver` — Enable AzureBlob CSI Driver.
- `--enable-cluster-autoscaler` — Enable cluster autoscaler, default value is false. Default: False.
- `--enable-container-network-logs` — Enable container network log collection functionalities on a cluster. Automatically enables --enable-high-log-scale-mode.
- `--enable-control-plane-metrics --enable-cp-metrics` — Enable collection of Azure Monitor managed Prometheus control plane metrics for managed cluster components (controlplane-apiserver and controlplane-etcd targets by default). Requires Azure Monitor metrics to be enabled (already enabled or via --enable-azure-monitor-metrics). Default: False.
- `--enable-cost-analysis` — Enable exporting Kubernetes Namespace and Deployment details to the Cost Analysis views in the Azure portal. For more information see aka.ms/aks/docs/cost-analysis. Default: False.
- `--enable-defender` — Enable Microsoft Defender security profile. Default: False.
- `--enable-encryption-at-host` — Enable EncryptionAtHost, default value is false. Default: False.
- `--enable-fips-image` — Use FIPS-enabled OS on agent nodes. Default: False.
- `--enable-gateway-api` — Enable managed installation of Gateway API CRDs from the standard release channel. Default: False.
- `--enable-high-log-scale-mode` — Enable High Log Scale Mode for Container Logs. Auto-enabled when --enable-container-network-logs is specified.
- `--enable-hosted-system` — (Automatic SKU) Explicitly opt in to a Managed System Pool for the Automatic cluster. Default: False.
- `--enable-image-cleaner` — Enable ImageCleaner Service. Default: False.
- `--enable-keda` — Enable KEDA workload auto-scaler. Default: False.
- `--enable-managed-identity` — Using a system assigned managed identity to manage cluster resource group. You can explicitly specify "--service-principal" and "--client-secret" to disable managed identity, otherwise it will be enabled.
- `--enable-msi-auth-for-monitoring` — Enable Managed Identity Auth for Monitoring addon. Default: True.
- `--enable-node-public-ip` — Enable VMSS or VMs node public IP. Default: False.
- `--enable-oidc-issuer` — Enable OIDC issuer. Default: False.
- `--enable-opentelemetry-logs-traces` — Enable the OpenTelemetry (OTLP) logs and traces receiver. Requires --enable-azure-monitor-logs. Default: False.
- `--enable-opentelemetry-metrics` — Enable the OpenTelemetry (OTLP) metrics receiver. Requires --enable-azure-monitor-metrics. Default: False.
- `--enable-private-cluster` — Enable private cluster. Default: False.
- `--enable-prometheus-metrics-scraping` — Enable Prometheus metrics scraping by the Azure Monitor agent. Requires --enable-azure-monitor-logs. Default: False.
- `--enable-secret-rotation` — Enable secret rotation. Use with azure-keyvault-secrets-provider addon. Default: False.
- `--enable-secure-boot` — Enable Secure Boot on all node pools in the cluster. Must use VMSS or VMs agent pool type. Default: False.
- `--enable-sgxquotehelper` — Enable SGX quote helper for confcom addon. Default: False.
- `--enable-static-egress-gateway` — Enable Static Egress Gateway addon to the cluster. Default: False.
- `--enable-syslog` — Enable syslog data collection for Monitoring addon.
- `--enable-ultra-ssd` — Enable UltraSSD, default value is false. Default: False.
- `--enable-upstream-kubescheduler-user-configuration` — Enable user-defined scheduler configuration for kube-scheduler upstream on the cluster. Default: False.
- `--enable-vpa` — Enable vertical pod autoscaler for cluster. Default: False.
- `--enable-vtpm` — Enable vTPM on all node pools in the cluster. Must use VMSS or VMs agent pool type. Default: False.
- `--enable-windows-gmsa` — Enable Windows gmsa. Default: False.
- `--enable-windows-recording-rules` — Enable Windows Recording Rules when enabling the Azure Monitor Metrics addon. Default: False.
- `--enable-workload-identity` — Enable workload identity addon. Default: False.
- `--ephemeral-disk-nvme-perf-tier` — Set ephemeral disk volume type for azure container storage.
- `--ephemeral-disk-volume-type` — Set ephemeral disk volume type for azure container storage.
- `--fqdn-subdomain` — Prefix for FQDN that is created for private cluster with custom private dns zone scenario.
- `--generate-ssh-keys` — Generate SSH public and private key files if missing. The keys will be stored in the ~/.ssh directory. Default: False.
- `--gmsa-dns-server` — Specify DNS server for Windows gmsa for this cluster.
- `--gmsa-root-domain-name` — Specify root domain name for Windows gmsa for this cluster.
- `--gpu-instance-profile` — GPU instance profile to partition multi-gpu Nvidia GPUs.
- `--grafana-resource-id` — Resource ID of the Azure Managed Grafana Workspace.
- `--host-group-id` — The fully qualified dedicated host group id used to provision agent node pool.
- `--http-proxy-config` — HTTP Proxy configuration for this cluster.
- `--if-match` — The value provided will be compared to the ETag of the managed cluster, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new cluster.
- `--if-none-match` — Set to '*' to allow a new cluster to be created, but to prevent updating an existing cluster. Other values will be ignored.
- `--image-cleaner-interval-hours` — ImageCleaner scanning interval.
- `--ip-families` — A comma-separated list of IP versions to use for cluster networking.
- `--k8s-support-plan` — Choose from "KubernetesOfficial" or "AKSLongTermSupport", with "AKSLongTermSupport" you get 1 extra year of CVE patchs.
- `--ksm-metric-annotations-allow-list` — Comma-separated list of additional Kubernetes label keys that will be used in the resource' labels metric. By default the metric contains only name and namespace labels. To include additional labels provide a list of resource names in their plural form and Kubernetes label keys you would like to all
- `--ksm-metric-labels-allow-list` — Comma-separated list of additional Kubernetes label keys that will be used in the resource' labels metric. By default the metric contains only name and namespace labels. To include additional labels provide a list of resource names in their plural form and Kubernetes label keys you would like to all
- `--kubelet-config` — Path to JSON file containing Kubelet configurations for agent nodes. https://aka.ms/aks/custom-node-config.
- `--kubernetes-version -k` — Version of Kubernetes to use for creating the cluster, such as "1.16.9".
- `--linux-os-config` — Path to JSON file containing OS configurations for Linux agent nodes. https://aka.ms/aks/custom-node-config.
- `--load-balancer-backend-pool-type` — Load balancer backend pool type.
- `--load-balancer-idle-timeout` — Load balancer idle timeout in minutes.
- `--load-balancer-managed-outbound-ip-count` — Load balancer managed outbound IP count.
- `--load-balancer-managed-outbound-ipv6-count` — Load balancer managed outbound IPv6 IP count.
- `--load-balancer-outbound-ip-prefixes` — Load balancer outbound IP prefix resource IDs.
- `--load-balancer-outbound-ips` — Load balancer outbound IP resource IDs.
- `--load-balancer-outbound-ports` — Load balancer outbound allocated ports.
- `--load-balancer-sku` — Azure Load Balancer SKU selection for your cluster. basic or standard. Defaults to 'standard'.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--max-count` — Maximum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [1, 1000].
- `--max-pods -m` — The maximum number of pods deployable to a node.
- `--message-of-the-day` — Path to a file containing the desired message of the day. Only valid for linux nodes. Will be written to /etc/motd.
- `--min-count` — Minimum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [1, 1000].
- `--nat-gateway-idle-timeout` — NAT gateway idle timeout in minutes.
- `--nat-gateway-managed-outbound-ip-count` — NAT gateway managed outbound IP count.
- `--nat-gateway-managed-outbound-ipv6-count --nat-gw-ipv6-count` — NAT gateway managed outbound IPv6 count. Only valid with --outbound-type managedNATGateway and --outbound-type-sku StandardV2.
- `--nat-gateway-outbound-ip-prefixes --nat-gw-prefixes` — Comma-separated public IP prefix resource IDs for the cluster NAT gateway. Only valid with --outbound-type-sku StandardV2.
- `--nat-gateway-outbound-ips --nat-gw-ips` — Comma-separated public IP resource IDs for the cluster NAT gateway. Only valid with --outbound-type-sku StandardV2.
- `--network-dataplane` — The network dataplane to use.
- `--network-plugin` — The Kubernetes network plugin to use.
- `--network-plugin-mode` — The network plugin mode to use.
- `--network-policy` — Network Policy Engine to use.
- `--no-ssh-key -x` — Do not use or create a local SSH key. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes in the Kubernetes node pool. After creating a cluster, you can change the size of its node pool with `az aks scale`. Default: 3.
- `--node-os-upgrade-channel` — Manner in which the OS on your nodes is updated. It could be NodeImage, None, SecurityPatch or Unmanaged.
- `--node-osdisk-diskencryptionset-id -d` — ResourceId of the disk encryption set to use for enabling encryption at rest on agent node os disk.
- `--node-osdisk-size` — Size in GiB of the OS disk for each node in the node pool. Minimum 30 GiB.
- `--node-osdisk-type` — OS disk type to be used for machines in a given agent pool: Ephemeral or Managed. Defaults to 'Ephemeral' when possible in conjunction with VM size and OS disk size. May not be changed for this pool after creation.
- `--node-provisioning-default-pools` — The set of default Karpenter NodePools configured for node provisioning. Valid values are "Auto" and "None".
- `--node-provisioning-mode` — Set the node provisioning mode of the cluster. Valid values are "Auto" and "Manual". For more information on "Auto" mode see aka.ms/aks/nap.
- `--node-public-ip-prefix-id` — Public IP prefix ID used to assign public IPs to VMSS or VMs nodes.
- `--node-public-ip-tags` — The ipTags of the node public IPs.
- `--node-resource-group` — The node resource group is the resource group where all customer's resources will be created in, such as virtual machines.
- `--node-subnet-id` — (Automatic SKU) The ID of a subnet in an existing VNet to be used by user node pools in an Automatic cluster.
- `--node-vm-size -s` — Size of Virtual Machines to create as Kubernetes nodes. If the user does not specify one, server will select a default VM size for her/him.
- `--nodepool-allowed-host-ports` — Expose host ports on the node pool. When specified, format should be a space-separated list of ranges with protocol, eg. `80/TCP 443/TCP 4000-5000/TCP`.
- `--nodepool-asg-ids` — The IDs of the application security groups to which the node pool's network interface should belong. When specified, format should be a space-separated list of IDs.
- `--nodepool-labels` — The node labels for all node pool. See https://aka.ms/node-labels for syntax of labels.
- `--nodepool-name` — Node pool name, up to 12 alphanumeric characters. Default: nodepool1.
- `--nodepool-tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--nodepool-taints` — The node taints for all node pool.
- `--nrg-lockdown-restriction-level` — Restriction level on the managed node resource group.
- `--opentelemetry-logs-traces-port-grpc` — GRPC port for the OpenTelemetry logs and traces receiver.
- `--opentelemetry-logs-traces-port-http` — HTTP/protobuf port for the OpenTelemetry logs and traces receiver.
- `--opentelemetry-metrics-port-grpc` — GRPC port for the OpenTelemetry metrics receiver.
- `--opentelemetry-metrics-port-http` — HTTP/protobuf port for the OpenTelemetry metrics receiver.
- `--os-sku` — The OS SKU of the agent node pool. Ubuntu, AzureLinux, AzureLinux3, AzureContainerLinux, Ubuntu2204, or Ubuntu2404.
- `--outbound-type` — How outbound traffic will be configured for a cluster.
- `--outbound-type-sku` — SKU of the managed NAT Gateway (Standard or StandardV2).
- `--pod-cidr` — A CIDR notation IP range from which to assign pod IPs when Azure CNI Overlay or Kubenet is used (On 31 March 2028, Kubenet will be retired).
- `--pod-cidrs` — A comma-separated list of CIDR notation IP ranges from which to assign pod IPs when Azure CNI Overlay or Kubenet is used (On 31 March 2028, Kubenet will be retired).
- `--pod-ip-allocation-mode` — Set the ip allocation mode for how Pod IPs from the Azure Pod Subnet are allocated to the nodes in the AKS cluster. The choice is between dynamic batches of individual IPs or static allocation of a set of CIDR blocks. Accepted Values are "DynamicIndividual" or "StaticBlock".
- `--pod-subnet-id` — The ID of a subnet in an existing VNet into which to assign pods in the cluster (requires azure network-plugin).
- `--ppg` — The ID of a PPG.
- `--private-dns-zone` — Private dns zone mode for private cluster.
- `--revision` — Azure Service Mesh revision to install.
- `--rotation-poll-interval` — Set interval of rotation poll. Use with azure-keyvault-secrets-provider addon.
- `--service-cidr` — A CIDR notation IP range from which to assign service cluster IPs.
- `--service-cidrs` — A comma-separated list of CIDR notation IP ranges from which to assign service cluster IPs.
- `--service-principal` — Service principal used for authentication to Azure APIs.
- `--skip-subnet-role-assignment` — Skip role assignment for subnet (advanced networking). Default: False.
- `--sku` — Specify SKU name for managed clusters. Use '--sku base' enables a base managed cluster. Use '--sku automatic' enables an automatic managed cluster.
- `--snapshot-id` — The source snapshot id used to create this cluster.
- `--ssh-key-value` — Public key path or key contents to install on node VMs for SSH access. For example, 'ssh-rsa AAAAB...snip...UcyupgH azureuser@linuxvm'. Default: ~\.ssh\id_rsa.pub.
- `--storage-pool-name` — Set storage pool name for azure container storage.
- `--storage-pool-option` — Set ephemeral disk storage pool option for azure container storage.
- `--storage-pool-size` — Set storage pool size for azure container storage.
- `--storage-pool-sku` — Set azure disk type storage pool sku for azure container storage.
- `--syslog-port` — TCP port that the Azure Monitor agent listens on for syslog data. Requires --enable-azure-monitor-logs.
- `--system-node-subnet-id` — (Automatic SKU) The ID of a subnet in an existing VNet to be used by the Managed System Pool in an Automatic cluster.
- `--tags` — The tags of the managed cluster. The managed cluster instance and all resources managed by the cloud provider will be tagged.
- `--tier` — Specify SKU tier for managed clusters. '--tier standard' enables a standard managed cluster service with a financially backed SLA. '--tier free' does not have a financially backed SLA.
- `--vm-set-type` — Agent pool vm set type. VirtualMachineScaleSets or AvailabilitySet or VirtualMachines. Defaults to 'VirtualMachineScaleSets'.
- `--vm-sizes` — Comma-separated list of VM sizes. Valid for VirtualMachines node pool only. If `--vm-sizes` not specified but `--node-vm-size` specified, value of `--node-vm-size` will be used. If neither of them specified, defaults to Standard_DS2_v2 for Linux or Standard_D2s_v3 for Windows.
- `--vnet-subnet-id` — The ID of a subnet in an existing VNet into which to deploy the cluster.
- `--windows-admin-password` — User account password to use on windows node VMs.
- `--windows-admin-username` — User account to create on windows node VMs.
- `--workload-runtime` — Set the workload runtime.
- `--workspace-resource-id` — The resource ID of an existing Log Analytics Workspace to use for storing monitoring data. If not specified, uses the default Log Analytics Workspace if it exists, otherwise creates one.
- `--yes -y` — Do not prompt for confirmation. Default: False.
- `--zones -z` — Availability zones where agent nodes will be placed. Also, to install agent nodes to more than one zones you need to pass zone numbers (1,2 or 3) separated by blanks. For example - To have all 3 zones, you are expected to enter `--zones 1 2 3`.

*Create a Kubernetes cluster with an existing SSH public key.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --ssh-key-value /path/to/publickey
```

*Create a Kubernetes cluster with a specific version.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --kubernetes-version 1.16.9
```

*Create a Kubernetes cluster with a larger node pool.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --node-count 7
```

*Create a kubernetes cluster with default kubernetes version, default SKU load balancer (Standard) and default vm set type (VirtualMachineScaleSets).*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster
```

*Create a kubernetes cluster with standard SKU load balancer and two AKS created IPs for the load balancer outbound connection usage.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-managed-outbound-ip-count 2
```

*Create a kubernetes cluster with a standard SKU load balancer, with two outbound AKS managed IPs an idle flow timeout of 5 minutes and 8000 allocated ports per machine*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-managed-outbound-ip-count 2 --load-balancer-idle-timeout 5 --load-balancer-outbound-ports 8000
```

*Create a kubernetes cluster with standard SKU load balancer and use the provided public IPs for the load balancer outbound connection usage.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-outbound-ips <ip-resource-id-1,ip-resource-id-2>
```

*Create a kubernetes cluster with standard SKU load balancer and use the provided public IP prefixes for the load balancer outbound connection usage.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-outbound-ip-prefixes <ip-prefix-resource-id-1,ip-prefix-resource-id-2>
```

*Create a kubernetes cluster with a AKS managed NAT gateway, with two outbound AKS managed IPs an idle flow timeout of 4 minutes*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --nat-gateway-managed-outbound-ip-count 2 --nat-gateway-idle-timeout 4 --outbound-type managedNATGateway --generate-ssh-keys
```

*Create a kubernetes cluster with basic SKU load balancer and AvailabilitySet vm set type.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku basic --vm-set-type AvailabilitySet
```

*Create a kubernetes cluster with authorized apiserver IP ranges.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --api-server-authorized-ip-ranges 193.168.1.0/24,194.168.1.0/24,195.168.1.0
```

*Create a kubernetes cluster which enables managed identity.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-managed-identity
```

*Create a kubernetes cluster with userDefinedRouting, standard load balancer SKU and a custom subnet preconfigured with a route table*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --outbound-type userDefinedRouting --load-balancer-sku standard --vnet-subnet-id customUserSubnetVnetID
```

*Create a kubernetes cluster with supporting Windows agent pools.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku Standard --network-plugin azure --windows-admin-username azure --windows-admin-password 'replacePassword1234$'
```

*Create a kubernetes cluster with supporting Windows agent pools with AHUB enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku Standard --network-plugin azure --windows-admin-username azure --windows-admin-password 'replacePassword1234$' --enable-ahub
```

*Create a kubernetes cluster with managed AAD enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-aad --aad-admin-group-object-ids <id-1,id-2> --aad-tenant-id <id>
```

*Create a kubernetes cluster with server side encryption using your owned key.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --node-osdisk-diskencryptionset-id <disk-encryption-set-resource-id>
```

*Create a kubernetes cluster with ephemeral OS enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --node-osdisk-type Ephemeral --node-osdisk-size 48
```

*Create a kubernetes cluster with EncryptionAtHost enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-encryption-at-host
```

*Create a kubernetes cluster with UltraSSD enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-ultra-ssd
```

*Create a kubernetes cluster with Azure RBAC enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-aad --enable-azure-rbac
```

*Create a kubernetes cluster with custom control plane identity and kubelet identity.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --assign-identity <control-plane-identity-resource-id> --assign-kubelet-identity <kubelet-identity-resource-id>
```

*Create a kubernetes cluster in the Edge Zone.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --location <location> --kubernetes-version 1.20.7 --edge-zone <edge-zone-name>
```

*Create a kubernetes cluster with a specific OS SKU*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --os-sku Ubuntu
```

*Create a kubernetes cluster with custom tags*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --tags "foo=bar" "baz=qux"
```

*Create a kubernetes cluster with custom headers*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --aks-custom-headers WindowsContainerRuntime=containerd
```

*Create a kubernetes cluster with FIPS-enabled OS*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-fips-image
```

*Create a kubernetes cluster with enabling Windows gmsa and with setting DNS server in the vnet used by the cluster.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku Standard --network-plugin azure --windows-admin-username azure --windows-admin-password 'replacePassword1234$' --enable-windows-gmsa
```

*Create a kubernetes cluster with enabling Windows gmsa but without setting DNS server in the vnet used by the cluster.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku Standard --network-plugin azure --windows-admin-username azure --windows-admin-password 'replacePassword1234$' --enable-windows-gmsa --gmsa-dns-server "10.240.0.4" --gmsa-root-domain-name "contoso.com"
```

*create a kubernetes cluster with a snapshot id.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --kubernetes-version 1.20.9 --snapshot-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/snapshots/mysnapshot1"
```

*create a kubernetes cluster with support of hostgroup id.*
```azurecli
az aks create -g MyResourceGroup -n MyMC --kubernetes-version 1.20.13 --location westus2 --host-group-id /subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/hostGroups/myHostGroup --node-vm-size VMSize --enable-managed-identity --assign-identity <user_assigned_identity_resource_id>
```

*Create a kubernetes cluster with no CNI installed.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --network-plugin none
```

*Create a kubernetes cluster with KEDA workload autoscaler enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-keda
```

*Create a kubernetes cluster with the Azure Monitor managed service for Prometheus integration enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-metrics
```

*Create a kubernetes cluster with Azure Monitor logs (Container Insights) enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-logs
```

*Create a kubernetes cluster with Azure Monitor logs enabled and syslog collected on a custom port.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-logs --enable-syslog --syslog-port 28330
```

*Create a kubernetes cluster with the OpenTelemetry logs and traces receiver enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-logs --enable-opentelemetry-logs-traces --opentelemetry-logs-traces-port-grpc 4317
```

*Create a kubernetes cluster with the OpenTelemetry metrics receiver enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-metrics --enable-opentelemetry-metrics --opentelemetry-metrics-port-grpc 4319
```

*Create a kubernetes cluster with vertical pod autoscaler enaled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-vpa
```

*create a kubernetes cluster with a Capacity Reservation Group(CRG) ID.*
```azurecli
az aks create -g MyResourceGroup -n MyMC --kubernetes-version 1.20.9 --node-vm-size VMSize --assign-identity "subscriptions/SubID/resourceGroups/RGName/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID" --enable-managed-identity --crg-id "subscriptions/SubID/resourceGroups/RGName/providers/Microsoft.ContainerService/CapacityReservationGroups/MyCRGID"
```

*Create a kubernetes cluster with Azure Service Mesh enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-service-mesh
```

*Create a kubernetes cluster with a nodepool having ip allocation mode set to "StaticBlock"*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --os-sku Ubuntu --max-pods MaxPodsPerNode --network-plugin azure --vnet-subnet-id /subscriptions/SubID/resourceGroups/AnotherResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/NodeSubnet --pod-subnet-id /subscriptions/SubID/resourceGroups/AnotherResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/PodSubnet --pod-ip-allocation-mode StaticBlock
```

*Create a kubernetes cluster with VirtualMachines vm set type.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --vm-set-type VirtualMachines --vm-sizes "VMSize1,VMSize2" --node-count 3
```

*Create a kubernetes cluster with auto node provisioning.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --node-provisioning-mode Auto
```

*Create a kubernetes cluster with auto node provisioning and no default pools.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --node-provisioning-mode Auto --node-provisioning-default-pools None
```

*Create a Kubernetes cluster with KataVmIsolation enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --os-sku AzureLinux --vm-size Standard_D4s_v3 --workload-runtime KataVmIsolation --node-count 1
```

*Create a kubernetes cluster with a managed installation of Gateway API CRDs from the standard release channel.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-gateway-api
```

## az aks create  (extension: aks-preview etc.)

Create a new managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aad-admin-group-object-ids` — Comma-separated list of aad group object IDs that will be set as cluster admin.
- `--aad-tenant-id` — The ID of an Azure Active Directory tenant.
- `--aci-subnet-name` — The name of a subnet in an existing VNet into which to deploy the virtual nodes.
- `--acns-advanced-networkpolicies` — Used to enable advanced network policies (None, FQDN or L7) on a cluster when enabling advanced networking features with "--enable-acns".
- `--acns-datapath-acceleration-mode` — Used to set the acceleration mode (None or BpfVeth) on a cluster when enabling advanced networking features with "--enable-acns".
- `--acns-transit-encryption-type` — Specify the transit encryption type for ACNS. Available values are 'None', 'WireGuard', and 'mTLS'.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--admin-username -u` — User account to create on node VMs for SSH access. Default: azureuser.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--ampls-resource-id` — Resource ID of Azure Monitor Private Link scope for Monitoring Addon.
- `--api-server-authorized-ip-ranges` — Comma-separated list of authorized apiserver IP ranges. Set to 0.0.0.0/32 to restrict apiserver traffic to node pools.
- `--apiserver-subnet-id` — The ID of a subnet in an existing VNet into which to assign control plane apiserver pods(requires --enable-apiserver-vnet-integration).
- `--app-routing-default-nginx-controller --ardnc` — Configure default nginx ingress controller type. Valid values are annotationControlled (default behavior), external, internal, or none.
- `--appgw-id` — Resource Id of an existing Application Gateway to use with AGIC. Use with ingress-azure addon.
- `--appgw-name` — Name of the application gateway to create/use in the node resource group. Use with ingress-azure addon.
- `--appgw-subnet-cidr` — Subnet CIDR to use for a new subnet created to deploy the Application Gateway. Use with ingress-azure addon.
- `--appgw-subnet-id` — Resource Id of an existing Subnet used to deploy the Application Gateway. Use with ingress-azure addon.
- `--appgw-watch-namespace` — Specify the namespace, which AGIC should watch. This could be a single string value, or a comma-separated list of namespaces.
- `--assign-identity` — Specify an existing user assigned identity to manage cluster resource group.
- `--assign-kubelet-identity` — Specify an existing user assigned identity for kubelet's usage, which is typically used to pull image from ACR.
- `--attach-acr` — Grant the 'acrpull' role assignment to the ACR specified by name or resource ID.
- `--auto-upgrade-channel` — Specify the upgrade channel for autoupgrade. It could be rapid, stable, patch, node-image or none, none means disable autoupgrade.
- `--azure-keyvault-kms-key-id` — Identifier of Azure Key Vault key.
- `--azure-keyvault-kms-key-vault-network-access` — Network Access of Azure Key Vault. Default: Public.
- `--azure-keyvault-kms-key-vault-resource-id` — Resource ID of Azure Key Vault.
- `--azure-monitor-workspace-resource-id` — Resource ID of the Azure Monitor Workspace.
- `--backup-configuration` — Backup configuration as inline JSON string or @file.json. Supports storageAccountResourceId, blobContainerName, backupResourceGroupId, backupVaultId, backupPolicyId, tags. backupVaultId and backupPolicyId are required for Custom strategy. Only valid with --enable-backup.
- `--backup-strategy` — Backup strategy preset. Week (default, 7-day operational retention), Month (30-day operational retention), DisasterRecovery (7-day operational + 90-day vault retention), Custom (bring your own vault and policy via --backup-configuration). Only valid with --enable-backup.
- `--bootstrap-artifact-source` — Configure artifact source when bootstraping the cluster. Default: Direct.
- `--bootstrap-container-registry-resource-id` — Configure container registry resource ID. Must use "Cache" as bootstrap artifact source.
- `--ca-certs --custom-ca-trust-certificates` — Path to a file containing up to 10 blank line separated certificates. Only valid for linux nodes.
- `--ca-profile --cluster-autoscaler-profile` — Space-separated list of key=value pairs for configuring cluster autoscaler. Pass an empty string to clear the profile.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-secret` — Secret associated with the service principal. This argument is required if `--service-principal` is specified.
- `--cluster-service-load-balancer-health-probe-mode` — Set the cluster service health probe mode.
- `--cluster-snapshot-id` — The source cluster snapshot id is used to create new cluster.
- `--container-storage-version` — Set azure container storage version, the latest version will be installed by default.
- `--control-plane-scaling-size --cp-scaling-size` — (PREVIEW) The control plane scaling size for the cluster.
- `--crg-id` — The crg-id used to associate the new cluster with the existed Capacity Reservation Group resource.
- `--data-collection-settings` — Path to JSON file containing data collection settings for Monitoring addon.
- `--defender-config` — Path to JSON file containing Microsoft Defender profile configurations.
- `--disable-acns-observability` — Used to disable advanced networking observability features on a clusters when enabling advanced networking features with "--enable-acns".
- `--disable-acns-security` — Used to disable advanced networking security features on a clusters when enabling advanced networking features with "--enable-acns".
- `--disable-disk-driver` — Disable AzureDisk CSI Driver. Default: False.
- `--disable-file-driver` — Disable AzureFile CSI Driver. Default: False.
- `--disable-local-accounts` — (Preview) If set to true, getting static credential will be disabled for this cluster. Default: False.
- `--disable-opentelemetry-logs` — Disable OpenTelemetry logs and traces collection. Default: False.
- `--disable-opentelemetry-logs-traces` — Disable OpenTelemetry logs and traces collection. Default: False.
- `--disable-opentelemetry-metrics` — Disable OpenTelemetry metrics collection. Default: False.
- `--disable-prometheus-metrics-scraping` — Disable Prometheus metrics scraping by the Azure Monitor agent. Applies to the Azure Monitor profile. Default: False.
- `--disable-public-fqdn` — Disable public fqdn feature for private cluster. Default: False.
- `--disable-rbac` — Disable Kubernetes Role-Based Access Control.
- `--disable-run-command` — Disable Run command feature for the cluster. Default: False.
- `--disable-snapshot-controller` — Disable CSI Snapshot Controller. Default: False.
- `--dns-name-prefix -p` — Prefix for hostnames that are created. If not specified, generate a hostname using the managed cluster and resource group names.
- `--dns-service-ip` — An IP address assigned to the Kubernetes DNS service.
- `--dns-zone-resource-ids` — A comma separated list of resource IDs of the DNS zone resource to use with the App Routing addon.
- `--edge-zone` — The name of edge zone.
- `--enable-aad` — Enable managed AAD feature for cluster. Default: False.
- `--enable-acns` — Enable advanced network functionalities on a cluster. Enabling this will incur additional costs. For non-cilium clusters, acns security will be disabled by default until further notice.
- `--enable-addons -a` — Enable the Kubernetes addons in a comma-separated list.
- `--enable-ahub` — Enable Azure Hybrid User Benefits (AHUB) for Windows VMs. Default: False.
- `--enable-ai-toolchain-operator` — Enable AI toolchain operator to the cluster. Default: False.
- `--enable-apiserver-vnet-integration` — Enable integration of user vnet with control plane apiserver pods. Default: False.
- `--enable-app-routing` — Enable Application Routing addon. Default: False.
- `--enable-app-routing-istio --enable-ari` — Enable Gateway API based ingress on App Routing via Istio without service mesh functionality. Default: False.
- `--enable-application-load-balancer` — Enable Application Load Balancer (Application Gateway for Containers) addon. Default: False.
- `--enable-asm --enable-azure-service-mesh` — Enable Azure Service Mesh.
- `--enable-azure-container-storage` — Enable azure container storage. Can be used as a flag (defaults to True) or with a storage pool type value: (azureDisk, ephemeralDisk, elasticSan, distributedAccelerator).
- `--enable-azure-keyvault-kms` — Enable Azure KeyVault Key Management Service. Default: False.
- `--enable-azure-monitor-app-monitoring` — Enable Azure Monitor Application Monitoring. Default: False.
- `--enable-azure-monitor-logs` — Enable Azure Monitor logs for the cluster. Default: False.
- `--enable-azure-monitor-metrics` — Enable Azure Monitor Metrics Profile. Default: False.
- `--enable-azure-rbac` — Enable Azure RBAC to control authorization checks on cluster. Default: False.
- `--enable-backup` — Enable Azure Backup for this AKS cluster. Orchestrates the same flow as 'az dataprotection enable-backup trigger' (requires the 'dataprotection' extension). Implicitly waits for cluster creation to complete (ignores --no-wait). Default: False.
- `--enable-blob-driver` — Enable AzureBlob CSI Driver.
- `--enable-cluster-autoscaler` — Enable cluster autoscaler, default value is false. Default: False.
- `--enable-container-network-logs` — Enable container network log collection functionalities on a cluster. Automatically enables --enable-high-log-scale-mode.
- `--enable-continuous-control-plane-and-addon-monitor` — Enable continuous control plane and addon monitor for the cluster. Default: False.
- `--enable-control-plane-metrics --enable-cp-metrics` — Enable collection of Azure Monitor managed Prometheus control plane metrics for managed cluster components (controlplane-apiserver and controlplane-etcd targets by default). Requires Azure Monitor metrics to be enabled (already enabled or via --enable-azure-monitor-metrics). Default: False.
- `--enable-cost-analysis` — Enable exporting Kubernetes Namespace and Deployment details to the Cost Analysis views in the Azure portal. For more information see aka.ms/aks/docs/cost-analysis. Default: False.
- `--enable-default-domain` — Enable default domain for Application Routing addon. Default: False.
- `--enable-defender` — Enable Microsoft Defender security profile. Default: False.
- `--enable-disk-driver` — Enable AzureDisk CSI Driver. Default: False.
- `--enable-encryption-at-host` — Enable EncryptionAtHost on agent node pool. Default: False.
- `--enable-fips` — Enable FIPS mode at the cluster level. Default: False.
- `--enable-fips-image` — Use FIPS-enabled OS on agent nodes. Required and always enabled when --os-sku is Windows2025; cannot be disabled for these node pools. Default: False.
- `--enable-gateway-api` — Enable managed installation of Gateway API CRDs from the standard release channel. Default: False.
- `--enable-high-log-scale-mode` — Enable High Log Scale Mode for Container Logs. Auto-enabled when --enable-container-network-logs is specified.
- `--enable-hosted-system` — (Automatic SKU) Explicitly opt in to a Managed System Pool for the Automatic cluster. Default: False.
- `--enable-image-cleaner` — Enable ImageCleaner Service. Default: False.
- `--enable-image-integrity` — Enable ImageIntegrity Service. Default: False.
- `--enable-imds-restriction` — Enable IMDS restriction in the cluster. Non-hostNetwork Pods will not be able to access IMDS. Default: False.
- `--enable-keda` — Enable KEDA workload auto-scaler. Default: False.
- `--enable-managed-identity` — Using managed identity to manage cluster resource group. You can explicitly specify "--service-principal" and "--client-secret" to disable managed identity, otherwise it will be enabled.
- `--enable-msi-auth-for-monitoring` — Send monitoring data to Log Analytics using the cluster's assigned identity (instead of the Log Analytics Workspace's shared key). Default: True.
- `--enable-node-hardening` — Enable node hardening at the cluster level. Default: False.
- `--enable-node-public-ip` — Enable VMSS node public IP. Default: False.
- `--enable-oidc-issuer` — Enable OIDC issuer. Default: False.
- `--enable-on-demand-monitor` — Enable on-demand monitor for the cluster. Default: False.
- `--enable-opentelemetry-logs` — Enable OpenTelemetry logs and traces collection. Default: False.
- `--enable-opentelemetry-logs-traces` — Enable OpenTelemetry logs and traces collection. Requires Azure Monitor logs to be enabled. Default: False.
- `--enable-opentelemetry-metrics` — Enable OpenTelemetry metrics collection. Requires Azure Monitor metrics to be enabled. Default: False.
- `--enable-optimized-addon-scaling` — Enable optimized addon scaling feature for cluster. Default: False.
- `--enable-osdisk-fc --enable-osdisk-full-caching` — Enable the full-cache ephemeral OS disk feature for the default node pool. Default: False.
- `--enable-pod-identity` — (PREVIEW) Enable pod identity addon. Default: False.
- `--enable-pod-identity-with-kubenet` — (PREVIEW) Enable pod identity addon for cluster using Kubnet network plugin. Default: False.
- `--enable-private-cluster` — Enable private cluster. Default: False.
- `--enable-prometheus-metrics-scraping` — Enable Prometheus metrics scraping by the Azure Monitor agent. Applies to the Azure Monitor profile. Default: False.
- `--enable-secret-rotation` — Enable secret rotation. Use with azure-keyvault-secrets-provider addon. Default: False.
- `--enable-secure-boot` — Enable Secure Boot on all node pools in the cluster. Must use VMSS agent pool type. Default: False.
- `--enable-service-account-image-pull` — Enable service account based image pull. For more information, see https://aka.ms/aks/identity-binding/acr-image-pull/docs. Default: False.
- `--enable-sgxquotehelper` — Enable SGX quote helper for confcom addon. Default: False.
- `--enable-static-egress-gateway` — Enable Static Egress Gateway addon to the cluster. Default: False.
- `--enable-syslog` — Enable syslog data collection for Monitoring addon.
- `--enable-ultra-ssd` — Enable UltraSSD on agent node pool. Default: False.
- `--enable-upgrade-gate` — Enable upgrade gate for the cluster. Agent pool upgrades wait for health signal validation and abort if unhealthy signals are observed. Default: False.
- `--enable-upstream-kubescheduler-user-configuration` — Enable user-defined scheduler configuration for kube-scheduler upstream on the cluster. Default: False.
- `--enable-vpa` — Enable vertical pod autoscaler for cluster. Default: False.
- `--enable-vtpm` — Enable vTPM on all node pools in the cluster. Must use VMSS agent pool type. Default: False.
- `--enable-windows-gmsa` — Enable Windows gmsa. Default: False.
- `--enable-windows-recording-rules` — Enable Windows Recording Rules when enabling the Azure Monitor Metrics addon. Default: False.
- `--enable-workload-identity` — (PREVIEW) Enable workload identity addon. Default: False.
- `--ephemeral-disk-nvme-perf-tier` — Set ephemeral disk volume type for azure container storage.
- `--ephemeral-disk-volume-type` — Set ephemeral disk volume type for azure container storage.
- `--fqdn-subdomain` — Prefix for FQDN that is created for private cluster with custom private dns zone scenario.
- `--generate-ssh-keys` — Generate SSH public and private key files if missing. Default: False.
- `--gmsa-dns-server` — Specify DNS server for Windows gmsa for this cluster.
- `--gmsa-root-domain-name` — Specify root domain name for Windows gmsa for this cluster.
- `--gpu-instance-profile` — GPU instance profile to partition multi-gpu Nvidia GPUs.
- `--grafana-resource-id` — Resource ID of the Azure Managed Grafana Workspace.
- `--host-group-id` — (PREVIEW) The fully qualified dedicated host group id used to provision agent node pool.
- `--http-proxy-config` — Http Proxy configuration for this cluster.
- `--if-match` — The value provided will be compared to the ETag of the managed cluster, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new cluster.
- `--if-none-match` — Set to '*' to allow a new cluster to be created, but to prevent updating an existing cluster. Other values will be ignored.
- `--image-cleaner-interval-hours` — ImageCleaner scanning interval.
- `--ip-families` — A comma separated list of IP versions to use for cluster networking.
- `--k8s-support-plan` — Choose from "KubernetesOfficial" or "AKSLongTermSupport", with "AKSLongTermSupport" you get 1 extra year of CVE patchs.
- `--kms-infrastructure-encryption` — Enable encryption at rest of Kubernetes resource objects using service-managed keys. Default: Disabled.
- `--ksm-metric-annotations-allow-list` — Comma-separated list of additional Kubernetes label keys that will be used in the resource' labels metric. By default the metric contains only name and namespace labels. To include additional labels provide a list of resource names in their plural form and Kubernetes label keys you would like to all
- `--ksm-metric-labels-allow-list` — Comma-separated list of additional Kubernetes label keys that will be used in the resource' labels metric. By default the metric contains only name and namespace labels. To include additional labels provide a list of resource names in their plural form and Kubernetes label keys you would like to all
- `--kube-proxy-config` — Kube-proxy configuration for this cluster.
- `--kubelet-config` — Kubelet configurations for agent nodes.
- `--kubernetes-version -k` — Version of Kubernetes to use for creating the cluster, such as "1.7.12" or "1.8.7".
- `--linux-os-config` — OS configurations for Linux agent nodes.
- `--load-balancer-backend-pool-type` — Load balancer backend pool type.
- `--load-balancer-idle-timeout` — Load balancer idle timeout in minutes.
- `--load-balancer-managed-outbound-ip-count` — Load balancer managed outbound IP count.
- `--load-balancer-managed-outbound-ipv6-count` — Load balancer managed outbound IPv6 IP count.
- `--load-balancer-outbound-ip-prefixes` — Load balancer outbound IP prefix resource IDs.
- `--load-balancer-outbound-ips` — Load balancer outbound IP resource IDs.
- `--load-balancer-outbound-ports` — Load balancer outbound allocated ports.
- `--load-balancer-sku` — Azure Load Balancer SKU selection for your cluster. basic or standard.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--max-count` — Maximum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [1, 1000].
- `--max-pods -m` — The maximum number of pods deployable to a node. Default: 0.
- `--message-of-the-day` — Path to a file containing the desired message of the day. Only valid for linux nodes. Will be written to /etc/motd.
- `--min-count` — Minimun nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [1, 1000].
- `--nat-gateway-idle-timeout` — NAT gateway idle timeout in minutes.
- `--nat-gateway-managed-outbound-ip-count` — NAT gateway managed outbound IP count.
- `--nat-gateway-managed-outbound-ipv6-count --nat-gw-ipv6-count` — NAT gateway managed outbound IPv6 IP count. Valid only with --outbound-type managedNATGatewayV2.
- `--nat-gateway-outbound-ip-prefixes --nat-gw-prefixes` — Comma-separated public IP prefix resource IDs for the cluster NAT gateway. V2 only.
- `--nat-gateway-outbound-ips --nat-gw-ips` — Comma-separated public IP resource IDs for the cluster NAT gateway. V2 only.
- `--network-dataplane` — The network dataplane to use.
- `--network-plugin` — The Kubernetes network plugin to use.
- `--network-plugin-mode` — The network plugin mode to use.
- `--network-policy` — (PREVIEW) The Kubernetes network policy to use.
- `--no-ssh-key -x` — Do not use or create a local SSH key. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-count -c` — Number of nodes in the Kubernetes node pool. It is required when --enable-cluster-autoscaler specified. After creating a cluster, you can change the size of its node pool with `az aks scale`. Default: 3.
- `--node-disruption-policy` — Set the node disruption policy for the cluster.
- `--node-init-taints --nodepool-initialization-taints` — The node initialization taints for node pools created with aks create operation.
- `--node-os-upgrade-channel` — Manner in which the OS on your nodes is updated. It could be NodeImage, None, SecurityPatch or Unmanaged.
- `--node-osdisk-diskencryptionset-id -d` — ResourceId of the disk encryption set to use for enabling encryption at rest on agent node os disk.
- `--node-osdisk-size` — Size in GiB of the OS disk for each node in the node pool. Minimum 30 GiB. Default: 0.
- `--node-osdisk-type` — OS disk type to be used for machines in a given agent pool. Defaults to 'Ephemeral' when possible in conjunction with VM size and OS disk size. May not be changed for this pool after creation. ('Ephemeral' or 'Managed').
- `--node-provisioning-default-pools` — The set of default Karpenter NodePools configured for node provisioning. Valid values are "Auto" and "None".
- `--node-provisioning-mode` — Set the node provisioning mode of the cluster. Valid values are "Auto" and "Manual". For more information on "Auto" mode see aka.ms/aks/nap.
- `--node-public-ip-prefix-id` — Public IP prefix ID used to assign public IPs to VMSS nodes.
- `--node-public-ip-prefix-ids` — Comma-separated list of public IP prefix resource IDs for dual-stack node public IPs (IPv4 and/or IPv6).
- `--node-public-ip-tags` — The ipTags of the node public IPs.
- `--node-resource-group` — The node resource group is the resource group where all customer's resources will be created in, such as virtual machines.
- `--node-subnet-id` — (Automatic SKU) The ID of a subnet in an existing VNet to be used by user node pools in an Automatic cluster.
- `--node-vm-size -s` — Size of Virtual Machines to create as Kubernetes nodes. If the user does not specify one, server will select a default VM size for her/him.
- `--nodepool-allowed-host-ports` — Expose host ports on the node pool. When specified, format should be a comma-separated list of ranges with protocol, eg. 80/TCP,443/TCP,4000-5000/TCP.
- `--nodepool-asg-ids` — The IDs of the application security groups to which the node pool's network interface should belong. When specified, format should be a comma-separated list of IDs.
- `--nodepool-labels` — The node labels for all node pools in this cluster. See https://aka.ms/node-labels for syntax of labels.
- `--nodepool-name` — Node pool name, alphanumeric characters only. See https://aka.ms/aks-naming-rules for length limits. Default: nodepool1.
- `--nodepool-tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--nodepool-taints` — The node taints for all node pools in this cluster.
- `--nrg-lockdown-restriction-level` — Restriction level on the managed node resource group.
- `--opentelemetry-logs-port` — HTTP/protobuf port for OpenTelemetry logs and traces collection.
- `--opentelemetry-logs-traces-port-grpc` — GRPC port for OpenTelemetry logs and traces collection (default port will be used if not specified).
- `--opentelemetry-logs-traces-port-http` — HTTP/protobuf port for OpenTelemetry logs and traces collection (default port will be used if not specified).
- `--opentelemetry-metrics-port` — HTTP/protobuf port for OpenTelemetry metrics collection.
- `--opentelemetry-metrics-port-grpc` — GRPC port for OpenTelemetry metrics collection (default port will be used if not specified).
- `--opentelemetry-metrics-port-http` — HTTP/protobuf port for OpenTelemetry metrics collection (default port will be used if not specified).
- `--os-sku` — The os-sku of the agent node pool. Ubuntu, Ubuntu2204, Ubuntu2404, Ubuntu2604, CBLMariner, AzureLinux, AzureLinux3, AzureLinuxOSGuard, AzureLinux3OSGuard, AzureContainerLinux, or Flatcar when os-type is Linux, default is Ubuntu if not set; Windows2019, Windows2022, Windows2025, or WindowsAnnual when
- `--outbound-type` — How outbound traffic will be configured for a cluster.
- `--outbound-type-sku` — SKU of the managed NAT gateway (Standard or StandardV2).
- `--pis-id --prepared-image-specification-id` — The resource ID of the prepared image specification to use for provisioning nodes in the default node pool.
- `--pod-cidr` — A CIDR notation IP range from which to assign pod IPs when Azure CNI Overlay or Kubenet is used (On 31 March 2028, Kubenet will be retired).
- `--pod-cidrs` — A comma-separated list of CIDR notation IP ranges from which to assign pod IPs when Azure CNI Overlay or Kubenet is used (On 31 March 2028, Kubenet will be retired).
- `--pod-ip-allocation-mode` — Set the ip allocation mode for how Pod IPs from the Azure Pod Subnet are allocated to the nodes in the AKS cluster. The choice is between dynamic batches of individual IPs or static allocation of a set of CIDR blocks. Accepted Values are "DynamicIndividual" or "StaticBlock".
- `--pod-subnet-id` — The ID of a subnet in an existing VNet into which to assign pods in the cluster (requires azure network-plugin).
- `--ppg` — The ID of a PPG.
- `--private-dns-zone` — Private dns zone mode for private cluster. "none" mode is in preview.
- `--revision` — Azure Service Mesh revision to install.
- `--rotation-poll-interval` — Set interval of rotation poll. Use with azure-keyvault-secrets-provider addon.
- `--safeguards-excluded-ns` — Comma-separated list of Kubernetes namespaces to exclude from deployment safeguards.
- `--safeguards-level` — The deployment safeguards Level. Accepted Values are [Off, Warning, Enforcement]. Requires azure policy addon to be enabled.
- `--safeguards-version` — The version of deployment safeguards to use. Default "v1.0.0" Use the ListSafeguardsVersions API to discover available versions.
- `--service-account-image-pull-default-managed-identity-id` — The default managed identity resource ID used for image pulls at the cluster level.
- `--service-cidr` — A CIDR notation IP range from which to assign service cluster IPs.
- `--service-cidrs` — A comma separated list of CIDR notation IP ranges from which to assign service cluster IPs.
- `--service-principal` — Service principal used for authentication to Azure APIs.
- `--skip-subnet-role-assignment` — Skip role assignment for subnet (advanced networking). Default: False.
- `--sku` — Specify SKU name for managed clusters. '--sku base' enables a base managed cluster. '--sku automatic' enables an automatic managed cluster.
- `--snapshot-id` — The source nodepool snapshot id used to create this cluster.
- `--ssh-access` — Configure SSH setting for the first system pool in this cluster. Use "disabled" to disable SSH access, "localuser" to enable SSH access using private key. Note, this configuration will not take effect for later created new node pools, please use option `az aks nodepool add --ssh-access` to configure Default: localuser.
- `--ssh-key-value` — Public key path or key contents to install on node VMs for SSH access. For example, 'ssh-rsa AAAAB...snip...UcyupgH azureuser@linuxvm'. Default: ~\.ssh\id_rsa.pub.
- `--storage-pool-name` — Set storage pool name for azure container storage.
- `--storage-pool-option` — Set ephemeral disk storage pool option for azure container storage.
- `--storage-pool-size` — Set storage pool size for azure container storage.
- `--storage-pool-sku` — Set azure disk type storage pool sku for azure container storage.
- `--syslog-port` — Host port used by the Azure Monitor agent to collect syslog. Defaults to 28330 when unset.
- `--system-node-subnet-id` — (Automatic SKU) The ID of a subnet in an existing VNet to be used by the Managed System Pool in an Automatic cluster.
- `--tags` — The tags of the managed cluster. The managed cluster instance and all resources managed by the cloud provider will be tagged.
- `--tier` — Specify SKU tier for managed clusters. '--tier standard' enables a standard managed cluster service with a financially backed SLA. '--tier free' does not have a financially backed SLA.
- `--vm-set-type` — Agent pool vm set type. VirtualMachineScaleSets, AvailabilitySet or VirtualMachines(Preview).
- `--vm-sizes` — Comma-separated list of sizes. Must use VirtualMachines agent pool type.
- `--vnet-subnet-id` — The ID of a subnet in an existing VNet into which to deploy the cluster.
- `--windows-admin-password` — User account password to use on windows node VMs.
- `--windows-admin-username` — User account to create on windows node VMs.
- `--workload-runtime` — Determines the type of workload a node can run. Defaults to OCIContainer. Default: OCIContainer.
- `--workspace-resource-id` — The resource ID of an existing Log Analytics Workspace to use for storing monitoring data. If not specified, uses the default Log Analytics Workspace if it exists, otherwise creates one.
- `--yes -y` — Do not prompt for confirmation. Default: False.
- `--zones -z` — Space-separated list of availability zones where agent nodes will be placed.

*Create a kubernetes cluster with upgrade gate enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-upgrade-gate
```

*Create a Kubernetes cluster with an existing SSH public key.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --ssh-key-value /path/to/publickey
```

*Create a Kubernetes cluster with a specific version.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --kubernetes-version 1.13.9
```

*Create a Kubernetes cluster with a larger node pool.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --node-count 7
```

*Create a kubernetes cluster with cluster autosclaler enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --kubernetes-version 1.13.9 --node-count 3 --enable-cluster-autoscaler --min-count 1 --max-count 5
```

*Create a kubernetes cluster with k8s 1.13.9 but use vmas.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --kubernetes-version 1.13.9 --vm-set-type AvailabilitySet
```

*Create a kubernetes cluster with default kubernetes vesrion, default SKU load balancer(standard) and default vm set type(VirtualMachineScaleSets).*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster
```

*Create a kubernetes cluster with standard SKU load balancer and two AKS created IPs for the load balancer outbound connection usage.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-managed-outbound-ip-count 2
```

*Create a kubernetes cluster with standard SKU load balancer and use the provided public IPs for the load balancer outbound connection usage.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-outbound-ips <ip-resource-id-1,ip-resource-id-2>
```

*Create a kubernetes cluster with standard SKU load balancer and use the provided public IP prefixes for the load balancer outbound connection usage.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-outbound-ip-prefixes <ip-prefix-resource-id-1,ip-prefix-resource-id-2>
```

*Create a kubernetes cluster with a standard SKU load balancer, with two outbound AKS managed IPs an idle flow timeout of 5 minutes and 8000 allocated ports per machine*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-managed-outbound-ip-count 2 --load-balancer-idle-timeout 5 --load-balancer-outbound-ports 8000
```

*Create a kubernetes cluster with a AKS managed NAT gateway, with two outbound AKS managed IPs an idle flow timeout of 4 minutes*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --nat-gateway-managed-outbound-ip-count 2 --nat-gateway-idle-timeout 4
```

*Create a kubernetes cluster with basic SKU load balancer and AvailabilitySet vm set type.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku basic --vm-set-type AvailabilitySet
```

*Create a kubernetes cluster with authorized apiserver IP ranges.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --api-server-authorized-ip-ranges 193.168.1.0/24,194.168.1.0/24,195.168.1.0
```

*Create a kubernetes cluster with server side encryption using your owned key.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --node-osdisk-diskencryptionset-id <disk-encryption-set-resource-id>
```

*Create a kubernetes cluster with userDefinedRouting, standard load balancer SKU and a custom subnet preconfigured with a route table*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --outbound-type userDefinedRouting --load-balancer-sku standard --vnet-subnet-id customUserSubnetVnetID
```

*Create a kubernetes cluster with supporting Windows agent pools with AHUB enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku Standard --network-plugin azure --windows-admin-username azure --windows-admin-password 'replacePassword1234$' --enable-ahub
```

*Create a kubernetes cluster with managed AAD enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-aad --aad-admin-group-object-ids <id-1,id-2> --aad-tenant-id <id>
```

*Create a kubernetes cluster with ephemeral os enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --node-osdisk-type Ephemeral --node-osdisk-size 48
```

*Create a kubernetes cluster with custom tags*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --tags "foo=bar" "baz=qux"
```

*Create a kubernetes cluster with EncryptionAtHost enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-encryption-at-host
```

*Create a kubernetes cluster with UltraSSD enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-ultra-ssd
```

*Create a kubernetes cluster with custom control plane identity and kubelet identity.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --assign-identity <control-plane-identity-resource-id> --assign-kubelet-identity <kubelet-identity-resource-id>
```

*Create a kubernetes cluster with Azure RBAC enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-aad --enable-azure-rbac
```

*Create a kubernetes cluster with a specific os-sku*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --os-sku Ubuntu
```

*Create a kubernetes cluster with enabling Windows gmsa and with setting DNS server in the vnet used by the cluster.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku Standard --network-plugin azure --windows-admin-username azure --windows-admin-password 'replacePassword1234$' --enable-windows-gmsa
```

*Create a kubernetes cluster with enabling Windows gmsa but without setting DNS server in the vnet used by the cluster.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --load-balancer-sku Standard --network-plugin azure --windows-admin-username azure --windows-admin-password 'replacePassword1234$' --enable-windows-gmsa --gmsa-dns-server "10.240.0.4" --gmsa-root-domain-name "contoso.com"
```

*create a kubernetes cluster with a nodepool snapshot id.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --kubernetes-version 1.20.9 --snapshot-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/snapshots/mysnapshot1"
```

*create a kubernetes cluster with a cluster snapshot id.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --cluster-snapshot-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedclustersnapshots/mysnapshot1"
```

*create a kubernetes cluster with a Capacity Reservation Group(CRG) ID.*
```azurecli
az aks create -g MyResourceGroup -n MyMC --kubernetes-version 1.20.9 --node-vm-size VMSize --assign-identity CRG-RG-ID --enable-managed-identity --crg-id "subscriptions/SubID/resourceGroups/RGName/providers/Microsoft.ContainerService/CapacityReservationGroups/MyCRGID"
```

*create a kubernetes cluster with support of hostgroup id.*
```azurecli
az aks create -g MyResourceGroup -n MyMC --kubernetes-version 1.20.13 --location westus2 --host-group-id /subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/hostGroups/myHostGroup --node-vm-size VMSize --enable-managed-identity --assign-identity <user_assigned_identity_resource_id>
```

*Create a kubernetes cluster with no CNI installed.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --network-plugin none
```

*Create a kubernetes cluster with safeguards set to "Warning"*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --safeguards-level Warning --enable-addons azure-policy
```

*Create a kubernetes cluster with safeguards set to "Warning" and some namespaces excluded*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --safeguards-level Warning --safeguards-excluded-ns ns1,ns2 --enable-addons azure-policy
```

*Create a kubernetes cluster with Azure Service Mesh enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-service-mesh
```

*Create a kubernetes cluster with Azure Monitor Metrics enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-metrics
```

*Create a kubernetes cluster with Azure Monitor App Monitoring enabled*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-app-monitoring
```

*Create a kubernetes cluster with OpenTelemetry metrics collection enabled*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-metrics --enable-azure-monitor-metrics
```

*Create a kubernetes cluster with OpenTelemetry logs and traces collection enabled*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-logs-traces --enable-addons monitoring
```

*Create a kubernetes cluster with Azure Monitor logs enabled (shorthand)*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-logs
```

*Create a kubernetes cluster with Azure Monitor logs, Prometheus scraping disabled and a custom syslog port*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-logs --disable-prometheus-metrics-scraping --syslog-port 28331
```

*Create a kubernetes cluster with OpenTelemetry metrics on custom port*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-metrics --opentelemetry-metrics-port-http 8888 --enable-azure-monitor-metrics
```

*Create a kubernetes cluster with OpenTelemetry logs and traces on custom ports*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-logs-traces --opentelemetry-logs-traces-port-http 8080 --opentelemetry-logs-traces-port-grpc 8082 --enable-azure-monitor-logs
```

*Create a kubernetes cluster with OpenTelemetry metrics on custom HTTP and gRPC ports*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-metrics --opentelemetry-metrics-port-http 8888 --opentelemetry-metrics-port-grpc 8889 --enable-azure-monitor-metrics
```

*Create a kubernetes cluster with a nodepool having ip allocation mode set to "StaticBlock"*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --os-sku Ubuntu --max-pods MaxPodsPerNode --network-plugin azure --vnet-subnet-id /subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/NodeSubnet --pod-subnet-id /subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.Network/virtualNetworks/MyVnet/subnets/PodSubnet --pod-ip-allocation-mode StaticBlock
```

*Create a kubernetes cluster with a VirtualMachines nodepool*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --vm-set-type VirtualMachines --vm-sizes "VMSize1,VMSize2" --node-count 3
```

*Create a kubernetes cluster with a fully managed system node pool*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-managed-system-pool
```

*Create a kubernetes cluster with a managed installation of Gateway API CRDs from the standard release channel.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --enable-gateway-api
```

*Create a kubernetes cluster with control plane scaling size H4.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --control-plane-scaling-size H4
```

*Create an automatic cluster with hosted system components enabled.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --sku automatic --enable-hosted-system
```

*Create a hosted-system automatic cluster in a BYO VNet.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --sku automatic --system-node-subnet-id <systemNodeSubnetID> --node-subnet-id <nodeSubnetID> --apiserver-subnet-id <apiserverSubnetID>
```

*Create a hosted-system automatic cluster in a BYO VNet with Load Balancer outbound.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --sku automatic --enable-hosted-system --system-node-subnet-id <systemNodeSubnetID> --node-subnet-id <nodeSubnetID> --apiserver-subnet-id <apiserverSubnetID> --outbound-type loadBalancer
```

*Create a kubernetes cluster with Azure Backup enabled (default Week strategy). Requires the 'dataprotection' extension. Implicitly waits for cluster creation.*
```azurecli
az aks create -g MyResourceGroup -n MyManagedCluster --generate-ssh-keys --enable-backup --yes
```

## az aks delete

Delete a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--if-match` — The value provided will be compared to the ETag of the managed cluster, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites.
- `--if-none-match` — Set to '*' to allow deleting a cluster only if it exists. Other values will be ignored.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a managed Kubernetes cluster. (autogenerated)*
```azurecli
az aks delete --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks delete  (extension: aks-preview etc.)

Delete a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--if-match` — The value provided will be compared to the ETag of the managed cluster, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites.
- `--if-none-match` — Not applicable for delete operations. This option will be ignored if provided.
- `--ignore-pod-disruption-budget` — Delete those pods on a node without considering Pod Disruption Budget.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Delete a managed Kubernetes cluster.*
```azurecli
az aks delete --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks disable-addons

Disable Kubernetes addons.

**Required parameters**

- `--addons -a` — Disable the Kubernetes addons in a comma-separated list.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Disable Kubernetes addons. (autogenerated)*
```azurecli
az aks disable-addons --addons virtual-node --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks disable-addons  (extension: aks-preview etc.)

Disable Kubernetes addons.

**Required parameters**

- `--addons -a` — Disable the Kubernetes addons in a comma-separated list.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Disable Kubernetes addons. (autogenerated)*
```azurecli
az aks disable-addons --addons virtual-node --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks enable-addons

Enable Kubernetes addons.

**Required parameters**

- `--addons -a` — Enable the Kubernetes addons in a comma-separated list.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--ampls-resource-id` — Resource ID of Azure Monitor Private Link scope for Monitoring Addon.
- `--appgw-id` — Resource Id of an existing Application Gateway to use with AGIC. Use with ingress-azure addon.
- `--appgw-name` — Name of the application gateway to create/use in the node resource group. Use with ingress-azure addon.
- `--appgw-subnet-cidr` — Subnet CIDR to use for a new subnet created to deploy the Application Gateway. Use with ingress-azure addon.
- `--appgw-subnet-id` — Resource Id of an existing Subnet used to deploy the Application Gateway. Use with ingress-azure addon.
- `--appgw-watch-namespace` — Specify the namespace, which AGIC should watch. This could be a single string value, or a comma-separated list of namespaces.
- `--change-reference` — The related change reference ID for this resource operation.
- `--data-collection-settings` — Path to JSON file containing data collection settings for Monitoring addon.
- `--enable-high-log-scale-mode` — Enable High Log Scale Mode for Container Logs. Auto-enabled when --enable-container-network-logs is specified.
- `--enable-msi-auth-for-monitoring` — Enable Managed Identity Auth for Monitoring addon. Default: True.
- `--enable-secret-rotation` — Enable secret rotation. Use with azure-keyvault-secrets-provider addon. Default: False.
- `--enable-sgxquotehelper` — Enable SGX quote helper for confcom addon. Default: False.
- `--enable-syslog` — Enable syslog data collection for Monitoring addon.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--rotation-poll-interval` — Set interval of rotation poll. Use with azure-keyvault-secrets-provider addon.
- `--subnet-name -s` — Name of an existing subnet to use with the virtual-node add-on.
- `--workspace-resource-id` — The resource ID of an existing Log Analytics Workspace to use for storing monitoring data.

*Enable Kubernetes addons. (autogenerated)*
```azurecli
az aks enable-addons --addons virtual-node --name MyManagedCluster --resource-group MyResourceGroup --subnet MySubnetName
```

*Enable ingress-appgw addon with subnet prefix.*
```azurecli
az aks enable-addons --name MyManagedCluster --resource-group MyResourceGroup --addons ingress-appgw --appgw-subnet-cidr 10.225.0.0/16 --appgw-name gateway
```

*Enable open-service-mesh addon.*
```azurecli
az aks enable-addons --name MyManagedCluster --resource-group MyResourceGroup --addons open-service-mesh
```

## az aks enable-addons  (extension: aks-preview etc.)

Enable Kubernetes addons.

**Required parameters**

- `--addons -a` — Enable the Kubernetes addons in a comma-separated list.
- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--ampls-resource-id` — Resource ID of Azure Monitor Private Link scope for Monitoring Addon.
- `--appgw-id` — Resource Id of an existing Application Gateway to use with AGIC. Use with ingress-azure addon.
- `--appgw-name` — Name of the application gateway to create/use in the node resource group. Use with ingress-azure addon.
- `--appgw-subnet-cidr` — Subnet CIDR to use for a new subnet created to deploy the Application Gateway. Use with ingress-azure addon.
- `--appgw-subnet-id` — Resource Id of an existing Subnet used to deploy the Application Gateway. Use with ingress-azure addon.
- `--appgw-watch-namespace` — Specify the namespace, which AGIC should watch. This could be a single string value, or a comma-separated list of namespaces. Use with ingress-azure addon.
- `--change-reference` — The related change reference ID for this resource operation.
- `--data-collection-settings` — Path to JSON file containing data collection settings for Monitoring addon.
- `--dns-zone-resource-ids` — A comma separated list of resource IDs of the DNS zone resource to use with the App Routing addon.
- `--enable-high-log-scale-mode` — Enable High Log Scale Mode for Container Logs. Auto-enabled when --enable-container-network-logs is specified.
- `--enable-msi-auth-for-monitoring` — Send monitoring data to Log Analytics using the cluster's assigned identity (instead of the Log Analytics Workspace's shared key). Default: True.
- `--enable-secret-rotation` — Enable secret rotation. Use with azure-keyvault-secrets-provider addon. Default: False.
- `--enable-sgxquotehelper` — Enable SGX quote helper for confcom addon. Default: False.
- `--enable-syslog` — Enable syslog data collection for Monitoring addon.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--rotation-poll-interval` — Set interval of rotation poll. Use with azure-keyvault-secrets-provider addon.
- `--subnet-name -s` — The subnet name for the virtual node to use.
- `--workspace-resource-id` — The resource ID of an existing Log Analytics Workspace to use for storing monitoring data.

*Enable Kubernetes addons. (autogenerated)*
```azurecli
az aks enable-addons --addons virtual-node --name MyManagedCluster --resource-group MyResourceGroup --subnet-name VirtualNodeSubnet
```

*Enable ingress-appgw addon with subnet prefix.*
```azurecli
az aks enable-addons --name MyManagedCluster --resource-group MyResourceGroup --addons ingress-appgw --appgw-subnet-cidr 10.2.0.0/16 --appgw-name gateway
```

*Enable open-service-mesh addon.*
```azurecli
az aks enable-addons --name MyManagedCluster --resource-group MyResourceGroup --addons open-service-mesh
```

## az aks get-credentials

Get access credentials for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--admin -a` — Get cluster administrator credentials. Default: cluster user credentials. Default: False.
- `--change-reference` — The related change reference ID for this resource operation.
- `--context` — If specified, overwrite the default context name. The `--admin` parameter takes precedence over `--context`.
- `--file -f` — Kubernetes configuration file to update. Use "-" to print YAML to stdout instead. Default: ~\.kube\config.
- `--format` — Specify the format of the returned credential. Available values are ["exec", "azure"]. Only take effect when requesting clusterUser credential of AAD clusters.
- `--overwrite-existing` — Overwrite any existing cluster entry with the same name. Default: False.
- `--public-fqdn` — Get private cluster credential with server address to be public fqdn. Default: False.

*Get access credentials for a managed Kubernetes cluster. (autogenerated)*
```azurecli
az aks get-credentials --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks get-credentials  (extension: aks-preview etc.)

Get access credentials for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--admin -a` — Get cluster administrator credentials. Default: cluster user credentials. Default: False.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--context` — If specified, overwrite the default context name.
- `--file -f` — Kubernetes configuration file to update. Use "-" to print YAML to stdout instead. Default: ~\.kube\config.
- `--format` — Specify the format of the returned credential. Available values are ["exec", "azure"]. Only take effect when requesting clusterUser credential of AAD clusters.
- `--overwrite-existing` — Overwrite any existing cluster entry with the same name. Default: False.
- `--public-fqdn` — Get private cluster credential with server address to be public fqdn. Default: False.
- `--user -u` — Get credentials for the user. Only valid when --admin is False. Default: cluster user credentials. Default: clusterUser.

*Get access credentials for a managed Kubernetes cluster. (autogenerated)*
```azurecli
az aks get-credentials --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks get-upgrades

Get the upgrade versions available for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the upgrade versions available for a managed Kubernetes cluster*
```azurecli
az aks get-upgrades --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks get-upgrades  (extension: aks-preview etc.)

Get the upgrade versions available for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the upgrade versions available for a managed Kubernetes cluster*
```azurecli
az aks get-upgrades --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks get-versions

Get the versions available for creating a managed Kubernetes cluster.

**Required parameters**

- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the versions available for creating a managed Kubernetes cluster*
```azurecli
az aks get-versions --location westus2
```

## az aks get-versions  (extension: aks-preview etc.)

Get the versions available for creating a managed Kubernetes cluster.

**Required parameters**

- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

*Get the versions available for creating a managed Kubernetes cluster*
```azurecli
az aks get-versions --location westus2
```

## az aks install-cli

Download and install kubectl, the Kubernetes command-line tool. Download and install kubelogin, a client-go credential (exec) plugin implementing azure authentication.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--base-src-url` — Base download source URL for kubectl releases.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-version` — Version of kubectl to install. Default: latest.
- `--gh-token` — GitHub authentication token used when downloading kubelogin binaries from GitHub releases. Supplying a token helps avoid GitHub API rate limits.
- `--install-location` — Path at which to install kubectl. Note: the path should contain the binary filename. Default: ~\.azure-kubectl\kubectl.exe.
- `--kubelogin-base-src-url -l` — Base download source URL for kubelogin releases.
- `--kubelogin-install-location` — Path at which to install kubelogin. Note: the path should contain the binary filename. Default: ~\.azure-kubelogin\kubelogin.exe.
- `--kubelogin-version` — Version of kubelogin to install. Default: latest.

## az aks install-desktop

Download and install AKS Desktop for the current platform.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--gh-token` — GitHub authentication token used to retrieve AKS Desktop release metadata. Prefer the GH_TOKEN environment variable to avoid exposing credentials in shell history, process listings, or debug logs. This option overrides GH_TOKEN. Supplying a token helps avoid GitHub API rate limits.
- `--version` — Version of AKS Desktop to install. By default, the latest stable version is installed.

*Install the latest stable version of AKS Desktop*
```azurecli
az aks install-desktop
```

*Install a specific version of AKS Desktop*
```azurecli
az aks install-desktop --version 0.9.1
```

## az aks kanalyze  (extension: aks-preview etc.)

Display diagnostic results for the Kubernetes cluster after kollect is done.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks kollect  (extension: aks-preview etc.)

Collecting diagnostic information for the Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--container-logs` — The list of container logs to collect.
- `--kube-objects` — The list of kubernetes objects to describe.
- `--node-logs` — The list of node logs to collect for Linux nodes. For example, /var/log/cloud-init.log.
- `--node-logs-windows` — The list of node logs to collect for Windows nodes. For example, C:\AzureData\CustomDataSetupScript.log.
- `--sas-token` — The SAS token with writable permission for the storage account.
- `--storage-account` — Name or ID of the storage account to save the diagnostic information.

*using storage account name and a shared access signature token with write permission*
```azurecli
az aks kollect -g MyResourceGroup -n MyManagedCluster --storage-account MyStorageAccount --sas-token "MySasToken"
```

*using the resource id of a storagea account resource you own.*
```azurecli
az aks kollect -g MyResourceGroup -n MyManagedCluster --storage-account "MyStoreageAccountResourceId"
```

*using the storagea account in diagnostics settings for your managed cluster.*
```azurecli
az aks kollect -g MyResourceGroup -n MyManagedCluster
```

*customize the container logs to collect.*
```azurecli
az aks kollect -g MyResourceGroup -n MyManagedCluster --container-logs "mynamespace1/mypod1 myns2"
```

*customize the kubernetes objects to collect.*
```azurecli
az aks kollect -g MyResourceGroup -n MyManagedCluster --kube-objects "mynamespace1/service myns2/deployment/deployment1"
```

*customize the node log files to collect.*
```azurecli
az aks kollect -g MyResourceGroup -n MyManagedCluster --node-logs "/var/log/azure-vnet.log /var/log/azure-vnet-ipam.log"
```

## az aks list

List managed Kubernetes clusters.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks list  (extension: aks-preview etc.)

List managed Kubernetes clusters.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks list-vm-skus  (extension: aks-preview etc.)

Lists the VM SKUs accepted by AKS when creating node pools in a specified location.

**Required parameters**

- `--location -l` — Location. Values from: 'az account list-locations'.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--all` — Show all VM SKU information including those not available for the current subscription.
- `--change-reference` — The related change reference ID for this resource operation.
- `--size -s` — VM size name filter, partial name is accepted.
- `--zone -z` — Show only VM SKUs that support availability zones.

## az aks operation-abort

Abort last running operation on managed cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Abort operation on managed cluster*
```azurecli
az aks operation-abort -g myResourceGroup -n myAKSCluster
```

## az aks operation-abort  (extension: aks-preview etc.)

Abort last running operation on managed cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

*Abort operation on managed cluster*
```azurecli
az aks operation-abort -g myResourceGroup -n myAKSCluster
```

## az aks remove-dev-spaces  (Deprecated)

Remove Azure Dev Spaces from a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Remove Azure Dev Spaces from a managed Kubernetes cluster.*
```azurecli
az aks remove-dev-spaces -g my-aks-group -n my-aks
```

*Remove Azure Dev Spaces from a managed Kubernetes cluster without prompting.*
```azurecli
az aks remove-dev-spaces -g my-aks-group -n my-aks --yes
```

## az aks rotate-certs

Rotate certificates and keys on a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks rotate-certs  (extension: aks-preview etc.)

Rotate certificates and keys on a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks scale

Scale the node pool in a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--node-count -c` — Number of nodes in the Kubernetes node pool.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--nodepool-name` — Node pool name, up to 12 alphanumeric characters.

*Scale the node pool in a managed Kubernetes cluster. (autogenerated)*
```azurecli
az aks scale --name MyManagedCluster --node-count 3 --resource-group MyResourceGroup
```

## az aks scale  (extension: aks-preview etc.)

Scale the node pool in a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--node-count -c` — Number of nodes in the Kubernetes node pool.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--nodepool-name` — Node pool name, alphanumeric characters only. See https://aka.ms/aks-naming-rules for length limits.

## az aks show

Show the details for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

*Show the details for a managed Kubernetes cluster*
```azurecli
az aks show --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks show  (extension: aks-preview etc.)

Show the details for a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.

*Show the details for a managed Kubernetes cluster*
```azurecli
az aks show -g MyResourceGroup -n MyManagedCluster
```

## az aks start

Starts a previously stopped Managed Cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az aks start  (extension: aks-preview etc.)

Starts a previously stopped Managed Cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az aks stop

Stop a managed cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az aks stop  (extension: aks-preview etc.)

Stop a managed cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.

## az aks update

Update a managed Kubernetes cluster. When called with no optional arguments this attempts to move the cluster to its goal state without changing the current cluster configuration. This can be used to move out of a non succeeded state.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aad-admin-group-object-ids` — Comma-separated list of aad group object IDs that will be set as cluster admin.
- `--aad-tenant-id` — The ID of an Azure Active Directory tenant.
- `--acns-advanced-networkpolicies` — Enable advanced network policies (None, FQDN or L7) on a cluster when enabling advanced networking features with "--enable-acns".
- `--acns-datapath-acceleration-mode` — Set the datapath acceleration mode for Azure Container Networking Solution (ACNS) Performance. Valid values are 'BpfVeth' and 'None'.
- `--acns-transit-encryption-type` — Set transit encryption type for ACNS security.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Comma-separated key-value pairs to specify custom headers.
- `--ampls-resource-id` — Resource ID of Azure Monitor Private Link scope for Monitoring Addon.
- `--api-server-authorized-ip-ranges` — Comma-separated list of authorized apiserver IP ranges. Set to "" to allow all traffic on a previously restricted cluster. Set to 0.0.0.0/32 to restrict apiserver traffic to node pools.
- `--apiserver-subnet-id` — The ID of a subnet in an existing VNet into which to assign control plane apiserver pods(requires --enable-apiserver-vnet-integration).
- `--assign-identity` — Specify an existing user assigned identity to manage cluster resource group.
- `--assign-kubelet-identity` — Update cluster's kubelet identity to an existing user assigned identity. Please note this operation will recreate all agent nodes in the cluster.
- `--assignee-principal-type -t` — Use this parameter in conjunction with --attach-acr to explicitly set the principal type in the ACR role assignment. This helps avoid RBAC-related errors by ensuring the correct principal type is applied. Valid values are 'User', 'Group' or 'ServicePrincipal'.
- `--attach-acr` — Grant the 'acrpull' role assignment to the ACR specified by name or resource ID.
- `--auto-upgrade-channel` — Specify the upgrade channel for autoupgrade.
- `--azure-container-storage-nodepools` — Define the comma separated nodepool list to install azure container storage.
- `--azure-keyvault-kms-key-id` — Identifier of Azure Key Vault key.
- `--azure-keyvault-kms-key-vault-network-access` — Network Access of Azure Key Vault.
- `--azure-keyvault-kms-key-vault-resource-id` — Resource ID of Azure Key Vault.
- `--azure-monitor-workspace-resource-id` — Resource ID of the Azure Monitor Workspace.
- `--bootstrap-artifact-source` — Configure artifact source when bootstraping the cluster.
- `--bootstrap-container-registry-resource-id` — Configure container registry resource ID. Must use "Cache" as bootstrap artifact source.
- `--ca-certs --custom-ca-trust-certificates` — Path to a file containing up to 10 blank line separated certificates. Only valid for Linux nodes.
- `--ca-profile --cluster-autoscaler-profile` — Comma-separated list of key=value pairs for configuring cluster autoscaler. Pass an empty string to clear the profile.
- `--change-reference` — The related change reference ID for this resource operation.
- `--container-storage-version` — Set azure container storage version, the latest version will be installed by default.
- `--data-collection-settings` — Path to JSON file containing data collection settings for Monitoring addon.
- `--defender-config` — Path to JSON file containing Microsoft Defender profile configurations.
- `--detach-acr` — Disable the 'acrpull' role assignment to the ACR specified by name or resource ID.
- `--disable-acns` — Disable all advanced networking functionalities on a cluster.
- `--disable-acns-observability` — Used to disable advanced networking observability features on a clusters when enabling advanced networking features with "--enable-acns".
- `--disable-acns-security` — Used to disable advanced networking security features on a clusters when enabling advanced networking features with "--enable-acns".
- `--disable-ahub` — Disable Azure Hybrid User Benefits (AHUB) feature for cluster. Default: False.
- `--disable-ai-toolchain-operator` — Disable AI toolchain operator. Default: False.
- `--disable-app-routing-istio --disable-ari` — Disable Gateway API based ingress on App Routing via Istio. Default: False.
- `--disable-azure-container-storage` — Disable azure container storage or any one of the storage pool types. Can be used as a flag (defaults to True) or with a storagepool type value: azureDisk, ephemeralDisk, elasticSan, all (to disable all storage pools).
- `--disable-azure-keyvault-kms` — Disable Azure KeyVault Key Management Service. Default: False.
- `--disable-azure-monitor-app-monitoring` — Disable Azure Monitor Application Monitoring auto-instrumentation for a Kubernetes cluster. Default: False.
- `--disable-azure-monitor-logs` — Disable Azure Monitor logs (Container Insights) for the cluster. Default: False.
- `--disable-azure-monitor-metrics` — Disable Azure Monitor Metrics Profile. This will delete all DCRA's associated with the cluster, any linked DCRs with the data stream = prometheus-stream and the recording rule groups created by the addon for this AKS cluster. Default: False.
- `--disable-azure-rbac` — Disable Azure RBAC to control authorization checks on cluster. Default: False.
- `--disable-blob-driver` — Disable AzureBlob CSI Driver.
- `--disable-cluster-autoscaler -d` — Disable cluster autoscaler. For VirtualMachines pools, converts all autoscale profiles back to manual scale profiles. Default: False.
- `--disable-container-network-logs` — Disable container network log collection functionalities on a cluster.
- `--disable-control-plane-metrics --disable-cp-metrics` — Disable collection of Azure Monitor managed Prometheus control plane metrics. Leaves Azure Monitor metrics enabled. Default: False.
- `--disable-cost-analysis` — Disable exporting Kubernetes Namespace and Deployment details to the Cost Analysis views in the Azure portal. Default: False.
- `--disable-defender` — Disable defender profile. Default: False.
- `--disable-disk-driver` — Disable AzureDisk CSI Driver. Default: False.
- `--disable-file-driver` — Disable AzureFile CSI Driver. Default: False.
- `--disable-force-upgrade` — Disable forceUpgrade cluster upgrade settings override. Default: False.
- `--disable-gateway-api` — Disable managed installation of Gateway API CRDs. Default: False.
- `--disable-http-proxy` — Disable HTTP Proxy Configuration on the cluster. Default: False.
- `--disable-image-cleaner` — Disable ImageCleaner Service. Default: False.
- `--disable-keda` — Disable KEDA workload auto-scaler. Default: False.
- `--disable-local-accounts` — If set to true, getting static credential will be disabled for this cluster. Default: False.
- `--disable-opentelemetry-logs-traces` — Disable the OpenTelemetry (OTLP) logs and traces receiver. Default: False.
- `--disable-opentelemetry-metrics` — Disable the OpenTelemetry (OTLP) metrics receiver. Default: False.
- `--disable-private-cluster` — Disable private cluster for apiserver vnet integration cluster. Default: False.
- `--disable-prometheus-metrics-scraping` — Disable Prometheus metrics scraping by the Azure Monitor agent. Requires Azure Monitor logs to be enabled. Default: False.
- `--disable-public-fqdn` — Disable public fqdn feature for private cluster. Default: False.
- `--disable-run-command` — Disable Run command feature for the cluster. Default: False.
- `--disable-secret-rotation` — Disable secret rotation. Use with azure-keyvault-secrets-provider addon. Default: False.
- `--disable-snapshot-controller` — Disable CSI Snapshot Controller. Default: False.
- `--disable-static-egress-gateway` — Disable Static Egress Gateway addon to the cluster. Default: False.
- `--disable-upstream-kubescheduler-user-configuration` — Disable user-defined scheduler configuration for kube-scheduler upstream on the cluster. Default: False.
- `--disable-vpa` — Disable vertical pod autoscaler for cluster. Default: False.
- `--disable-windows-gmsa` — Disable Windows gmsa on cluster. Default: False.
- `--disable-workload-identity` — Disable workload identity addon. Default: False.
- `--enable-aad` — Enable managed AAD feature for cluster. Default: False.
- `--enable-acns` — Enable advanced network functionalities on a cluster. Enabling this will incur additional costs. For non-cilium clusters, acns security will be disabled by default until further notice.
- `--enable-ahub` — Enable Azure Hybrid User Benefits (AHUB) feature for cluster. Default: False.
- `--enable-ai-toolchain-operator` — Enable AI toolchain operator to the cluster. Default: False.
- `--enable-apiserver-vnet-integration` — Enable integration of user vnet with control plane apiserver pods. Default: False.
- `--enable-app-routing-istio --enable-ari` — Enable Gateway API based ingress on App Routing via Istio without service mesh functionality. Default: False.
- `--enable-azure-container-storage` — Enable azure container storage. Can be used as a flag (defaults to True) or with a storage pool type value: (azureDisk, ephemeralDisk, elasticSan).
- `--enable-azure-keyvault-kms` — Enable Azure KeyVault Key Management Service. Default: False.
- `--enable-azure-monitor-app-monitoring` — Enable Azure Monitor Application Monitoring auto-instrumentation for a Kubernetes cluster. Default: False.
- `--enable-azure-monitor-logs` — Enable Azure Monitor logs (Container Insights) for the cluster using managed identity authentication. Default: False.
- `--enable-azure-monitor-metrics` — Enable a kubernetes cluster with the Azure Monitor managed service for Prometheus integration. Default: False.
- `--enable-azure-rbac` — Enable Azure RBAC to control authorization checks on cluster. Default: False.
- `--enable-blob-driver` — Enable AzureBlob CSI Driver.
- `--enable-cluster-autoscaler -e` — Enable cluster autoscaler. For VirtualMachines pools, converts all manual scale profiles to autoscale profiles using the same min/max counts. Default: False.
- `--enable-container-network-logs` — Enable container network log collection functionalities on a cluster. Automatically enables --enable-high-log-scale-mode.
- `--enable-control-plane-metrics --enable-cp-metrics` — Enable collection of Azure Monitor managed Prometheus control plane metrics for managed cluster components (controlplane-apiserver and controlplane-etcd targets by default). Requires Azure Monitor metrics to be enabled (already enabled or via --enable-azure-monitor-metrics). Default: False.
- `--enable-cost-analysis` — Enable exporting Kubernetes Namespace and Deployment details to the Cost Analysis views in the Azure portal. For more information see aka.ms/aks/docs/cost-analysis. Default: False.
- `--enable-defender` — Enable Microsoft Defender security profile. Default: False.
- `--enable-disk-driver` — Enable AzureDisk CSI Driver. Default: False.
- `--enable-file-driver` — Enable AzureFile CSI Driver. Default: False.
- `--enable-force-upgrade` — Enable forceUpgrade cluster upgrade settings override. Default: False.
- `--enable-gateway-api` — Enable managed installation of Gateway API CRDs from the standard release channel. Default: False.
- `--enable-high-log-scale-mode` — Enable High Log Scale Mode for Container Logs. Auto-enabled when --enable-container-network-logs is specified.
- `--enable-http-proxy` — Enable HTTP Proxy Configuration on the cluster. Default: False.
- `--enable-image-cleaner` — Enable ImageCleaner Service. Default: False.
- `--enable-keda` — Enable KEDA workload auto-scaler. Default: False.
- `--enable-local-accounts` — If set to true, will enable getting static credential for this cluster. Default: False.
- `--enable-managed-identity` — Update current cluster to use managed identity to manage cluster resource group. Default: False.
- `--enable-msi-auth-for-monitoring` — Enable Managed Identity Auth for Monitoring addon.
- `--enable-oidc-issuer` — Enable OIDC issuer. Default: False.
- `--enable-opentelemetry-logs-traces` — Enable the OpenTelemetry (OTLP) logs and traces receiver. Requires Azure Monitor logs to be enabled. Default: False.
- `--enable-opentelemetry-metrics` — Enable the OpenTelemetry (OTLP) metrics receiver. Requires Azure Monitor metrics to be enabled. Default: False.
- `--enable-private-cluster` — Enable private cluster for apiserver vnet integration cluster. Default: False.
- `--enable-prometheus-metrics-scraping` — Enable Prometheus metrics scraping by the Azure Monitor agent. Requires Azure Monitor logs to be enabled. Default: False.
- `--enable-public-fqdn` — Enable public fqdn feature for private cluster. Default: False.
- `--enable-run-command` — Enable Run command feature for the cluster. Default: False.
- `--enable-secret-rotation` — Enable secret rotation. Use with azure-keyvault-secrets-provider addon. Default: False.
- `--enable-snapshot-controller` — Enable Snapshot Controller. Default: False.
- `--enable-static-egress-gateway` — Enable Static Egress Gateway addon to the cluster. Default: False.
- `--enable-syslog` — Enable syslog data collection for Monitoring addon.
- `--enable-upstream-kubescheduler-user-configuration` — Enable user-defined scheduler configuration for kube-scheduler upstream on the cluster. Default: False.
- `--enable-vpa` — Enable vertical pod autoscaler for cluster. Default: False.
- `--enable-windows-gmsa` — Enable Windows gmsa on cluster. Default: False.
- `--enable-windows-recording-rules` — Enable Windows Recording Rules when enabling the Azure Monitor Metrics addon. Default: False.
- `--enable-workload-identity` — Enable workload identity addon. Default: False.
- `--ephemeral-disk-nvme-perf-tier` — Set ephemeral disk volume type for azure container storage.
- `--ephemeral-disk-volume-type` — Set ephemeral disk volume type for azure container storage.
- `--gmsa-dns-server` — Specify DNS server for Windows gmsa on cluster.
- `--gmsa-root-domain-name` — Specify root domain name for Windows gmsa on cluster.
- `--grafana-resource-id` — Resource ID of the Azure Managed Grafana Workspace.
- `--http-proxy-config` — HTTP Proxy configuration for this cluster.
- `--if-match` — The value provided will be compared to the ETag of the managed cluster, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new cluster.
- `--if-none-match` — Set to '*' to allow a new cluster to be created, but to prevent updating an existing cluster. Other values will be ignored.
- `--image-cleaner-interval-hours` — ImageCleaner scanning interval.
- `--ip-families` — A comma-separated list of IP versions to use for cluster networking.
- `--k8s-support-plan` — Choose from "KubernetesOfficial" or "AKSLongTermSupport", with "AKSLongTermSupport" you get 1 extra year of CVE patchs.
- `--ksm-metric-annotations-allow-list` — Comma-separated list of additional Kubernetes label keys that will be used in the resource' labels metric. By default the metric contains only name and namespace labels. To include additional labels provide a list of resource names in their plural form and Kubernetes label keys you would like to all
- `--ksm-metric-labels-allow-list` — Comma-separated list of additional Kubernetes label keys that will be used in the resource' labels metric. By default the metric contains only name and namespace labels. To include additional labels provide a list of resource names in their plural form and Kubernetes label keys you would like to all
- `--load-balancer-backend-pool-type` — Load balancer backend pool type.
- `--load-balancer-idle-timeout` — Load balancer idle timeout in minutes.
- `--load-balancer-managed-outbound-ip-count` — Load balancer managed outbound IP count.
- `--load-balancer-managed-outbound-ipv6-count` — Load balancer managed outbound IPv6 IP count.
- `--load-balancer-outbound-ip-prefixes` — Load balancer outbound IP prefix resource IDs.
- `--load-balancer-outbound-ips` — Load balancer outbound IP resource IDs.
- `--load-balancer-outbound-ports` — Load balancer outbound allocated ports.
- `--load-balancer-sku` — Azure Load Balancer SKU selection for your cluster. only standard is accepted.
- `--max-count` — Maximum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [1, 1000].
- `--migrate-vmas-to-vms` — Migrate cluster with VMAS node pool to VMS node pool. Default: False.
- `--min-count` — Minimum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [1, 1000].
- `--nat-gateway-idle-timeout` — NAT gateway idle timeout in minutes.
- `--nat-gateway-managed-outbound-ip-count` — NAT gateway managed outbound IP count.
- `--nat-gateway-managed-outbound-ipv6-count --nat-gw-ipv6-count` — NAT gateway managed outbound IPv6 count. Only valid with --outbound-type managedNATGateway and --outbound-type-sku StandardV2.
- `--nat-gateway-outbound-ip-prefixes --nat-gw-prefixes` — Comma-separated public IP prefix resource IDs for the cluster NAT gateway. Only valid with --outbound-type-sku StandardV2.
- `--nat-gateway-outbound-ips --nat-gw-ips` — Comma-separated public IP resource IDs for the cluster NAT gateway. Only valid with --outbound-type-sku StandardV2.
- `--network-dataplane` — The network dataplane to use.
- `--network-plugin` — The Kubernetes network plugin to use.
- `--network-plugin-mode` — Update the mode of a network plugin to migrate to a different pod networking setup.
- `--network-policy` — Update Network Policy Engine.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-os-upgrade-channel` — Manner in which the OS on your nodes is updated. It could be NodeImage, None, SecurityPatch or Unmanaged.
- `--node-provisioning-default-pools` — The set of default Karpenter NodePools configured for node provisioning. Valid values are "Auto" and "None".
- `--node-provisioning-mode` — Set the node provisioning mode of the cluster. Valid values are "Auto" and "Manual". For more information on "Auto" mode see aka.ms/aks/nap.
- `--nodepool-labels` — The node labels for all node pool. See https://aka.ms/node-labels for syntax of labels.
- `--nodepool-taints` — The node taints for all node pool.
- `--nrg-lockdown-restriction-level` — Restriction level on the managed node resource group.
- `--opentelemetry-logs-traces-port-grpc` — GRPC port for the OpenTelemetry logs and traces receiver.
- `--opentelemetry-logs-traces-port-http` — HTTP/protobuf port for the OpenTelemetry logs and traces receiver.
- `--opentelemetry-metrics-port-grpc` — GRPC port for the OpenTelemetry metrics receiver.
- `--opentelemetry-metrics-port-http` — HTTP/protobuf port for the OpenTelemetry metrics receiver.
- `--outbound-type` — How outbound traffic will be configured for a cluster.
- `--outbound-type-sku` — SKU of the managed NAT Gateway (Standard or StandardV2).
- `--pod-cidr` — Update the pod CIDR for a cluster. Used when updating a cluster from Azure CNI to Azure CNI Overlay.
- `--private-dns-zone` — The private dns zone mode for private cluster.
- `--rotation-poll-interval` — Set interval of rotation poll. Use with azure-keyvault-secrets-provider addon.
- `--sku` — Specify SKU name for managed clusters. Use '--sku base' enables a base managed cluster. Use '--sku automatic' enables an automatic managed cluster.
- `--storage-pool-name` — Set storage pool name for azure container storage.
- `--storage-pool-option` — Set ephemeral disk storage pool option for azure container storage.
- `--storage-pool-size` — Set storage pool size for azure container storage.
- `--storage-pool-sku` — Set azure disk type storage pool sku for azure container storage.
- `--syslog-port` — TCP port that the Azure Monitor agent listens on for syslog data. Requires Azure Monitor logs to be enabled.
- `--tags` — The tags of the managed cluster. The managed cluster instance and all resources managed by the cloud provider will be tagged.
- `--tier` — Specify SKU tier for managed clusters. '--tier standard' enables a standard managed cluster service with a financially backed SLA. '--tier free' changes a standard managed cluster to a free one.
- `--update-cluster-autoscaler -u` — Update min-count or max-count for cluster autoscaler. Not supported for VirtualMachines pools; use 'az aks nodepool auto-scale update' instead. Default: False.
- `--upgrade-override-until` — Until when the cluster upgradeSettings overrides are effective. It needs to be in a valid date-time format that's within the next 30 days. For example, 2023-04-01T13:00:00Z. Note that if --force-upgrade is set to true and --upgrade-override-until is not set, by default it will be set to 3 days from 
- `--windows-admin-password` — User account password to use on windows node VMs.
- `--workspace-resource-id` — The resource ID of an existing Log Analytics Workspace to use for storing monitoring data. If not specified, uses the default Log Analytics Workspace if it exists, otherwise creates one.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Reconcile the cluster back to its current state.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster
```

*Enable Azure Monitor logs (Container Insights) on an existing cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-logs
```

*Disable Azure Monitor logs (Container Insights) on an existing cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-azure-monitor-logs
```

*Change the syslog port used by Azure Monitor logs on an existing cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-syslog --syslog-port 28330
```

*Enable the OpenTelemetry logs and traces receiver on an existing cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-logs-traces --opentelemetry-logs-traces-port-grpc 4317
```

*Enable the OpenTelemetry metrics receiver on an existing cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-metrics --opentelemetry-metrics-port-grpc 4319
```

*Update a kubernetes cluster with standard SKU load balancer to use two AKS created IPs for the load balancer outbound connection usage.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --load-balancer-managed-outbound-ip-count 2
```

*Update a kubernetes cluster with standard SKU load balancer to use the provided public IPs for the load balancer outbound connection usage.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --load-balancer-outbound-ips <ip-resource-id-1,ip-resource-id-2>
```

*Update a kubernetes cluster with a standard SKU load balancer, with two outbound AKS managed IPs an idle flow timeout of 5 minutes and 8000 allocated ports per machine*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --load-balancer-managed-outbound-ip-count 2 --load-balancer-idle-timeout 5 --load-balancer-outbound-ports 8000
```

*Update a kubernetes cluster with standard SKU load balancer to use the provided public IP prefixes for the load balancer outbound connection usage.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --load-balancer-outbound-ip-prefixes <ip-prefix-resource-id-1,ip-prefix-resource-id-2>
```

*Update a kubernetes cluster of managedNATGateway outbound type with two outbound AKS managed IPs an idle flow timeout of 4 minutes*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --nat-gateway-managed-outbound-ip-count 2 --nat-gateway-idle-timeout 4
```

*Attach AKS cluster to ACR by name "acrName"*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --attach-acr acrName
```

*Update a kubernetes cluster with authorized apiserver ip ranges.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --api-server-authorized-ip-ranges 193.168.1.0/24,194.168.1.0/24
```

*Disable authorized apiserver ip ranges feature for a kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --api-server-authorized-ip-ranges ""
```

*Restrict apiserver traffic in a kubernetes cluster to agentpool nodes.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --api-server-authorized-ip-ranges 0.0.0.0/32
```

*Update a AKS-managed AAD cluster with tenant ID or admin group object IDs.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --aad-admin-group-object-ids <id-1,id-2> --aad-tenant-id <id>
```

*Migrate a AKS AAD-Integrated cluster or a non-AAD cluster to a AKS-managed AAD cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-aad --aad-admin-group-object-ids <id-1,id-2> --aad-tenant-id <id>
```

*Enable Azure Hybrid User Benefits featture for a kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-ahub
```

*Disable Azure Hybrid User Benefits featture for a kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-ahub
```

*Update Windows password of a kubernetes cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCLuster --windows-admin-password "Repl@cePassw0rd12345678"
```

*Update the cluster to use system assigned managed identity in control plane.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-managed-identity
```

*Update the cluster to use user assigned managed identity in control plane.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-managed-identity --assign-identity <user_assigned_identity_resource_id>
```

*Update a non managed AAD AKS cluster to use Azure RBAC*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-aad --enable-azure-rbac
```

*Update a managed AAD AKS cluster to use Azure RBAC*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-azure-rbac
```

*Disable Azure RBAC in a managed AAD AKS cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-azure-rbac
```

*Update the tags of a kubernetes cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCLuster --tags "foo=bar" "baz=qux"
```

*Update a kubernetes cluster with custom headers*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --aks-custom-headers WindowsContainerRuntime=containerd,AKSHTTPCustomFeatures=Microsoft.ContainerService/CustomNodeConfigPreview
```

*Enable Windows gmsa for a kubernetes cluster with setting DNS server in the vnet used by the cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-windows-gmsa
```

*Enable Windows gmsa for a kubernetes cluster without setting DNS server in the vnet used by the cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-windows-gmsa --gmsa-dns-server "10.240.0.4" --gmsa-root-domain-name "contoso.com"
```

*Disable Windows gmsa for a kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-windows-gmsa
```

*Enable KEDA workload autoscaler for an existing kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-keda
```

*Disable KEDA workload autoscaler for an existing kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-keda
```

*Enable VPA(Vertical Pod Autoscaler) for an existing kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCLuster --enable-vpa
```

*Disable VPA(Vertical Pod Autoscaler) for an existing kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCLuster --disable-vpa
```

*Update a kubernetes cluster to use auto node provisioning.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --node-provisioning-mode Auto
```

*Update a kubernetes cluster to use auto node provisioning mode with no default pools.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --node-provisioning-mode Auto --node-provisioning-default-pools None
```

*Upgrade load balancer sku to standard*
```azurecli
az aks update --load-balancer-sku standard -g MyResourceGroup -n MyManagedCluster
```

*Update a kubernetes cluster to enable a managed installation of Gateway API CRDs from the standard release channel.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-gateway-api
```

*Update a kubernetes cluster to disable the managed installation of Gateway API CRDs.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-gateway-api
```

## az aks update  (extension: aks-preview etc.)

Update the properties of a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--aad-admin-group-object-ids` — Comma-separated list of aad group object IDs that will be set as cluster admin.
- `--aad-tenant-id` — The ID of an Azure Active Directory tenant.
- `--acns-advanced-networkpolicies` — Used to enable advanced network policies (None, FQDN or L7) on a cluster when enabling advanced networking features with "--enable-acns".
- `--acns-datapath-acceleration-mode` — Used to set the acceleration mode (None or BpfVeth) on a cluster when enabling advanced networking features with "--enable-acns".
- `--acns-transit-encryption-type` — Specify the transit encryption type for ACNS. Available values are 'None', 'WireGuard', and 'mTLS'.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--ampls-resource-id` — Resource ID of Azure Monitor Private Link scope for Monitoring Addon.
- `--api-server-authorized-ip-ranges` — Comma-separated list of authorized apiserver IP ranges. Set to "" to allow all traffic on a previously restricted cluster. Set to 0.0.0.0/32 to restrict apiserver traffic to node pools.
- `--apiserver-subnet-id` — The ID of a subnet in an existing VNet into which to assign control plane apiserver pods(requires --enable-apiserver-vnet-integration).
- `--assign-identity` — Specify an existing user assigned identity to manage cluster resource group.
- `--assign-kubelet-identity` — Update cluster's kubelet identity to an existing user assigned identity. Note, this operation will recreate all agent node in the cluster.
- `--attach-acr` — Grant the 'acrpull' role assignment to the ACR specified by name or resource ID.
- `--auto-upgrade-channel` — Specify the upgrade channel for autoupgrade. It could be rapid, stable, patch, node-image or none, none means disable autoupgrade.
- `--azure-container-storage-nodepools` — Define the comma separated nodepool list to install azure container storage.
- `--azure-keyvault-kms-key-id` — Identifier of Azure Key Vault key.
- `--azure-keyvault-kms-key-vault-network-access` — Network Access of Azure Key Vault.
- `--azure-keyvault-kms-key-vault-resource-id` — Resource ID of Azure Key Vault.
- `--azure-monitor-workspace-resource-id` — Resource ID of the Azure Monitor Workspace.
- `--backup-configuration` — Backup configuration as inline JSON string or @file.json. Supports storageAccountResourceId, blobContainerName, backupResourceGroupId, backupVaultId, backupPolicyId, tags. backupVaultId and backupPolicyId are required for Custom strategy. Only valid with --enable-backup.
- `--backup-strategy` — Backup strategy preset. Week (default, 7-day operational retention), Month (30-day operational retention), DisasterRecovery (7-day operational + 90-day vault retention), Custom (bring your own vault and policy via --backup-configuration). Only valid with --enable-backup.
- `--bootstrap-artifact-source` — Configure artifact source when bootstraping the cluster.
- `--bootstrap-container-registry-resource-id` — Configure container registry resource ID. Must use "Cache" as bootstrap artifact source.
- `--ca-certs --custom-ca-trust-certificates` — Path to a file containing up to 10 blank line separated certificates. Only valid for linux nodes.
- `--ca-profile --cluster-autoscaler-profile` — Space-separated list of key=value pairs for configuring cluster autoscaler. Pass an empty string to clear the profile.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster-service-load-balancer-health-probe-mode` — Set the cluster service health probe mode.
- `--cluster-snapshot-id` — The source cluster snapshot id is used to update existing cluster.
- `--container-storage-version` — Set azure container storage version, the latest version will be installed by default.
- `--control-plane-scaling-size --cp-scaling-size` — The control plane scaling size. Provides scaled and performance-guaranteed control plane capacity. Available values are 'H2', 'H4', and 'H8'. The control plane scaling profile must already be enabled on the cluster.
- `--data-collection-settings` — Path to JSON file containing data collection settings for Monitoring addon.
- `--defender-config` — Path to JSON file containing Microsoft Defender profile configurations.
- `--detach-acr` — Disable the 'acrpull' role assignment to the ACR specified by name or resource ID.
- `--disable-acns` — Disable all advanced networking functionalities on a cluster.
- `--disable-acns-observability` — Used to disable advanced networking observability features on a clusters when enabling advanced networking features with "--enable-acns".
- `--disable-acns-security` — Used to disable advanced networking security features on a clusters when enabling advanced networking features with "--enable-acns".
- `--disable-ahub` — Disable Azure Hybrid User Benefits (AHUB) feature for cluster. Default: False.
- `--disable-ai-toolchain-operator` — Disable AI toolchain operator. Default: False.
- `--disable-app-routing-istio --disable-ari` — Disable Gateway API based ingress on App Routing via Istio. Default: False.
- `--disable-application-load-balancer` — Disable Application Load Balancer (Application Gateway for Containers) addon. Default: False.
- `--disable-azure-container-storage` — Disable azure container storage or any one of the storage types. Can be used as a flag (defaults to True) or with a storage type value: azureDisk, ephemeralDisk, elasticSan, distributedAccelerator, all (to disable all storage types).
- `--disable-azure-keyvault-kms` — Disable Azure KeyVault Key Management Service. Default: False.
- `--disable-azure-monitor-app-monitoring` — Disable Azure Monitor Application Monitoring. Default: False.
- `--disable-azure-monitor-logs` — Disable Azure Monitor logs for the cluster. Default: False.
- `--disable-azure-monitor-metrics` — Disable Azure Monitor Metrics Profile. This will delete all DCRA's associated with the cluster, any linked DCRs with the data stream = prometheus-stream and the recording rule groups created by the addon for this AKS cluster. Default: False.
- `--disable-azure-rbac` — Disable Azure RBAC to control authorization checks on cluster. Default: False.
- `--disable-blob-driver` — Disable AzureBlob CSI Driver.
- `--disable-cluster-autoscaler -d` — Disable cluster autoscaler. For VirtualMachines pools, converts all autoscale profiles back to manual scale profiles. Default: False.
- `--disable-container-network-logs` — Disable container network log collection functionalities on a cluster.
- `--disable-continuous-control-plane-and-addon-monitor` — Disable continuous control plane and addon monitor for the cluster. Default: False.
- `--disable-control-plane-metrics --disable-cp-metrics` — Disable collection of Azure Monitor managed Prometheus control plane metrics. Leaves Azure Monitor metrics enabled. Default: False.
- `--disable-cost-analysis` — Disable exporting Kubernetes Namespace and Deployment details to the Cost Analysis views in the Azure portal. Default: False.
- `--disable-defender` — Disable defender profile. Default: False.
- `--disable-disk-driver` — Disable AzureDisk CSI Driver. Default: False.
- `--disable-file-driver` — Disable AzureFile CSI Driver. Default: False.
- `--disable-fips` — Disable FIPS mode at the cluster level. Default: False.
- `--disable-force-upgrade` — Disable forceUpgrade cluster upgrade settings override. Default: False.
- `--disable-gateway-api` — Disable managed installation of Gateway API CRDs. Default: False.
- `--disable-http-proxy` — Disable HTTP Proxy Configuration on the cluster. Default: False.
- `--disable-image-cleaner` — Disable ImageCleaner Service. Default: False.
- `--disable-image-integrity` — Disable ImageIntegrity Service. Default: False.
- `--disable-imds-restriction` — Disable IMDS restriction in the cluster. All Pods in the cluster will be able to access IMDS. Default: False.
- `--disable-keda` — Disable KEDA workload auto-scaler. Default: False.
- `--disable-local-accounts` — (Preview) If set to true, getting static credential will be disabled for this cluster. Default: False.
- `--disable-node-hardening` — Disable node hardening at the cluster level. Default: False.
- `--disable-on-demand-monitor` — Disable on-demand monitor for the cluster. Default: False.
- `--disable-opentelemetry-logs` — Disable OpenTelemetry logs and traces collection. Default: False.
- `--disable-opentelemetry-logs-traces` — Disable OpenTelemetry logs and traces collection. Default: False.
- `--disable-opentelemetry-metrics` — Disable OpenTelemetry metrics collection. Default: False.
- `--disable-optimized-addon-scaling` — Disable optimized addon scaling feature for cluster. Default: False.
- `--disable-pod-identity` — (PREVIEW) Disable Pod Identity addon for cluster. Default: False.
- `--disable-private-cluster` — Disable private cluster for apiserver vnet integration cluster. Default: False.
- `--disable-prometheus-metrics-scraping` — Disable Prometheus metrics scraping by the Azure Monitor agent. Applies to the Azure Monitor profile. Default: False.
- `--disable-public-fqdn` — Disable public fqdn feature for private cluster. Default: False.
- `--disable-run-command` — Disable Run command feature for the cluster. Default: False.
- `--disable-secret-rotation` — Disable secret rotation. Use with azure-keyvault-secrets-provider addon. Default: False.
- `--disable-service-account-image-pull` — Disable service account based image pull. Default: False.
- `--disable-snapshot-controller` — Disable CSI Snapshot Controller. Default: False.
- `--disable-static-egress-gateway` — Disable Static Egress Gateway addon to the cluster. Default: False.
- `--disable-upgrade-gate` — Disable upgrade gate for the cluster. Default: False.
- `--disable-upstream-kubescheduler-user-configuration` — Disable user-defined scheduler configuration for kube-scheduler upstream on the cluster. Default: False.
- `--disable-vpa` — Disable vertical pod autoscaler for cluster. Default: False.
- `--disable-workload-identity` — (PREVIEW) Disable Workload Identity addon for cluster. Default: False.
- `--enable-aad` — Enable managed AAD feature for cluster. Default: False.
- `--enable-acns` — Enable advanced network functionalities on a cluster. Enabling this will incur additional costs. For non-cilium clusters, acns security will be disabled by default until further notice.
- `--enable-ahub` — Enable Azure Hybrid User Benefits (AHUB) feature for cluster. Default: False.
- `--enable-ai-toolchain-operator` — Enable AI toolchain operator to the cluster. Default: False.
- `--enable-apiserver-vnet-integration` — Enable integration of user vnet with control plane apiserver pods. Default: False.
- `--enable-app-routing-istio --enable-ari` — Enable Gateway API based ingress on App Routing via Istio without service mesh functionality. Default: False.
- `--enable-application-load-balancer` — Enable Application Load Balancer (Application Gateway for Containers) addon. Default: False.
- `--enable-azure-container-storage` — Enable azure container storage. Can be used as a flag (defaults to True) or with a storage pool type value: (azureDisk, ephemeralDisk, elasticSan, distributedAccelerator).
- `--enable-azure-keyvault-kms` — Enable Azure KeyVault Key Management Service. Default: False.
- `--enable-azure-monitor-app-monitoring` — Enable Azure Monitor Application Monitoring. Default: False.
- `--enable-azure-monitor-logs` — Enable Azure Monitor logs for the cluster. Default: False.
- `--enable-azure-monitor-metrics` — Enable Azure Monitor Metrics Profile. Default: False.
- `--enable-azure-rbac` — Enable Azure RBAC to control authorization checks on cluster. Default: False.
- `--enable-backup` — Enable Azure Backup for this AKS cluster. Orchestrates the same flow as 'az dataprotection enable-backup trigger' (requires the 'dataprotection' extension). Default: False.
- `--enable-blob-driver` — Enable AzureBlob CSI Driver.
- `--enable-cluster-autoscaler -e` — Enable cluster autoscaler. For VirtualMachines pools, converts all manual scale profiles to autoscale profiles using the same min/max counts. Default: False.
- `--enable-container-network-logs` — Enable container network log collection functionalities on a cluster. Automatically enables --enable-high-log-scale-mode.
- `--enable-continuous-control-plane-and-addon-monitor` — Enable continuous control plane and addon monitor for the cluster. Default: False.
- `--enable-control-plane-metrics --enable-cp-metrics` — Enable collection of Azure Monitor managed Prometheus control plane metrics for managed cluster components (controlplane-apiserver and controlplane-etcd targets by default). Requires Azure Monitor metrics to be enabled (already enabled or via --enable-azure-monitor-metrics). Default: False.
- `--enable-cost-analysis` — Enable exporting Kubernetes Namespace and Deployment details to the Cost Analysis views in the Azure portal. For more information see aka.ms/aks/docs/cost-analysis. Default: False.
- `--enable-defender` — Enable Microsoft Defender security profile. Default: False.
- `--enable-disk-driver` — Enable AzureDisk CSI Driver. Default: False.
- `--enable-file-driver` — Enable AzureFile CSI Driver. Default: False.
- `--enable-fips` — Enable FIPS mode at the cluster level. Default: False.
- `--enable-force-upgrade` — Enable forceUpgrade cluster upgrade settings override. Default: False.
- `--enable-gateway-api` — Enable managed installation of Gateway API CRDs from the standard release channel. Default: False.
- `--enable-high-log-scale-mode` — Enable High Log Scale Mode for Container Logs. Auto-enabled when --enable-container-network-logs is specified.
- `--enable-hosted-system` — (Automatic SKU) Convert an existing Automatic cluster to use a Managed System Pool. Default: False.
- `--enable-http-proxy` — Enable HTTP Proxy Configuration on the cluster. Default: False.
- `--enable-image-cleaner` — Enable ImageCleaner Service. Default: False.
- `--enable-image-integrity` — Enable ImageIntegrity Service. Default: False.
- `--enable-imds-restriction` — Enable IMDS restriction in the cluster. Non-hostNetwork Pods will not be able to access IMDS. Default: False.
- `--enable-keda` — Enable KEDA workload auto-scaler. Default: False.
- `--enable-local-accounts` — (Preview) If set to true, will enable getting static credential for this cluster. Default: False.
- `--enable-managed-identity` — Update current cluster to managed identity to manage cluster resource group. Default: False.
- `--enable-msi-auth-for-monitoring` — Send monitoring data to Log Analytics using the cluster's assigned identity (instead of the Log Analytics Workspace's shared key).
- `--enable-node-hardening` — Enable node hardening at the cluster level. Default: False.
- `--enable-oidc-issuer` — Enable OIDC issuer. Default: False.
- `--enable-on-demand-monitor` — Enable on-demand monitor for the cluster. Default: False.
- `--enable-opentelemetry-logs` — Enable OpenTelemetry logs and traces collection. Default: False.
- `--enable-opentelemetry-logs-traces` — Enable OpenTelemetry logs and traces collection. Requires Azure Monitor logs to be enabled. Default: False.
- `--enable-opentelemetry-metrics` — Enable OpenTelemetry metrics collection. Requires Azure Monitor metrics to be enabled. Default: False.
- `--enable-optimized-addon-scaling` — Enable optimized addon scaling feature for cluster. Default: False.
- `--enable-pod-identity` — (PREVIEW) Enable Pod Identity addon for cluster. Default: False.
- `--enable-pod-identity-with-kubenet` — (PREVIEW) Enable pod identity addon for cluster using Kubnet network plugin. Default: False.
- `--enable-private-cluster` — Enable private cluster for apiserver vnet integration cluster. Default: False.
- `--enable-prometheus-metrics-scraping` — Enable Prometheus metrics scraping by the Azure Monitor agent. Applies to the Azure Monitor profile. Default: False.
- `--enable-public-fqdn` — Enable public fqdn feature for private cluster. Default: False.
- `--enable-run-command` — Enable Run command feature for the cluster. Default: False.
- `--enable-secret-rotation` — Enable secret rotation. Use with azure-keyvault-secrets-provider addon. Default: False.
- `--enable-service-account-image-pull` — Enable service account based image pull. For more information, see https://aka.ms/aks/identity-binding/acr-image-pull/docs. Default: False.
- `--enable-snapshot-controller` — Enable Snapshot Controller. Default: False.
- `--enable-static-egress-gateway` — Enable Static Egress Gateway addon to the cluster. Default: False.
- `--enable-syslog` — Enable syslog data collection for Monitoring addon.
- `--enable-upgrade-gate` — Enable upgrade gate for the cluster. Agent pool upgrades wait for health signal validation and abort if unhealthy signals are observed. Default: False.
- `--enable-upstream-kubescheduler-user-configuration` — Enable user-defined scheduler configuration for kube-scheduler upstream on the cluster. Default: False.
- `--enable-vpa` — Enable vertical pod autoscaler for cluster. Default: False.
- `--enable-windows-gmsa` — Enable Windows gmsa on cluster. Default: False.
- `--enable-windows-recording-rules` — Enable Windows Recording Rules when enabling the Azure Monitor Metrics addon. Default: False.
- `--enable-workload-identity` — (PREVIEW) Enable Workload Identity addon for cluster. Default: False.
- `--ephemeral-disk-nvme-perf-tier` — Set ephemeral disk volume type for azure container storage.
- `--ephemeral-disk-volume-type` — Set ephemeral disk volume type for azure container storage.
- `--gmsa-dns-server` — Specify DNS server for Windows gmsa on cluster.
- `--gmsa-root-domain-name` — Specify root domain name for Windows gmsa on cluster.
- `--grafana-resource-id` — Resource ID of the Azure Managed Grafana Workspace.
- `--http-proxy-config` — HTTP Proxy configuration for this cluster.
- `--if-match` — The value provided will be compared to the ETag of the managed cluster, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new cluster.
- `--if-none-match` — Set to '*' to allow a new cluster to be created, but to prevent updating an existing cluster. Other values will be ignored.
- `--image-cleaner-interval-hours` — ImageCleaner scanning interval.
- `--ip-families` — A comma separated list of IP versions to use for cluster networking.
- `--k8s-support-plan` — Choose from "KubernetesOfficial" or "AKSLongTermSupport", with "AKSLongTermSupport" you get 1 extra year of CVE patchs.
- `--kms-infrastructure-encryption` — Enable encryption at rest of Kubernetes resource objects using service-managed keys.
- `--ksm-metric-annotations-allow-list` — Comma-separated list of additional Kubernetes label keys that will be used in the resource' labels metric. By default the metric contains only name and namespace labels. To include additional labels provide a list of resource names in their plural form and Kubernetes label keys you would like to all
- `--ksm-metric-labels-allow-list` — Comma-separated list of additional Kubernetes label keys that will be used in the resource' labels metric. By default the metric contains only name and namespace labels. To include additional labels provide a list of resource names in their plural form and Kubernetes label keys you would like to all
- `--kube-proxy-config` — Kube-proxy configuration for this cluster.
- `--load-balancer-backend-pool-type` — Load balancer backend pool type.
- `--load-balancer-idle-timeout` — Load balancer idle timeout in minutes.
- `--load-balancer-managed-outbound-ip-count` — Load balancer managed outbound IP count.
- `--load-balancer-managed-outbound-ipv6-count` — Load balancer managed outbound IPv6 IP count.
- `--load-balancer-outbound-ip-prefixes` — Load balancer outbound IP prefix resource IDs.
- `--load-balancer-outbound-ips` — Load balancer outbound IP resource IDs.
- `--load-balancer-outbound-ports` — Load balancer outbound allocated ports.
- `--load-balancer-sku` — Azure Load Balancer SKU selection for your cluster. only standard is accepted.
- `--max-count` — Maximum nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [1, 1000].
- `--migrate-vmas-to-vms` — Migrate cluster with VMAS node pool to VMS node pool. Default: False.
- `--min-count` — Minimun nodes count used for autoscaler, when "--enable-cluster-autoscaler" specified. Please specify the value in the range of [1, 1000].
- `--nat-gateway-idle-timeout` — NAT gateway idle timeout in minutes.
- `--nat-gateway-managed-outbound-ip-count` — NAT gateway managed outbound IP count.
- `--nat-gateway-managed-outbound-ipv6-count --nat-gw-ipv6-count` — NAT gateway managed outbound IPv6 IP count. Valid only with --outbound-type managedNATGatewayV2.
- `--nat-gateway-outbound-ip-prefixes --nat-gw-prefixes` — Comma-separated public IP prefix resource IDs for the cluster NAT gateway. V2 only.
- `--nat-gateway-outbound-ips --nat-gw-ips` — Comma-separated public IP resource IDs for the cluster NAT gateway. V2 only.
- `--network-dataplane` — The network dataplane to use.
- `--network-plugin` — The Kubernetes network plugin to use.
- `--network-plugin-mode` — The network plugin mode to use.
- `--network-policy` — Update the mode of a network policy.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-disruption-policy` — Set the node disruption policy for the cluster.
- `--node-init-taints --nodepool-initialization-taints` — The node initialization taints for all node pools in cluster.
- `--node-os-upgrade-channel` — Manner in which the OS on your nodes is updated. It could be NodeImage, None, SecurityPatch or Unmanaged.
- `--node-provisioning-default-pools` — The set of default Karpenter NodePools configured for node provisioning. Valid values are "Auto" and "None".
- `--node-provisioning-mode` — Set the node provisioning mode of the cluster. Valid values are "Auto" and "Manual". For more information on "Auto" mode see aka.ms/aks/nap.
- `--node-subnet-id` — (Automatic SKU) The ID of a subnet in an existing VNet to be used by user node pools.
- `--nodepool-labels` — The node labels for all node pool. See https://aka.ms/node-labels for syntax of labels.
- `--nodepool-taints` — The node taints for all node pool.
- `--nrg-lockdown-restriction-level` — Restriction level on the managed node resource.
- `--opentelemetry-logs-port` — HTTP/protobuf port for OpenTelemetry logs and traces collection.
- `--opentelemetry-logs-traces-port-grpc` — GRPC port for OpenTelemetry logs and traces collection (default port will be used if not specified).
- `--opentelemetry-logs-traces-port-http` — HTTP/protobuf port for OpenTelemetry logs and traces collection (default port will be used if not specified).
- `--opentelemetry-metrics-port` — HTTP/protobuf port for OpenTelemetry metrics collection.
- `--opentelemetry-metrics-port-grpc` — GRPC port for OpenTelemetry metrics collection (default port will be used if not specified).
- `--opentelemetry-metrics-port-http` — HTTP/protobuf port for OpenTelemetry metrics collection (default port will be used if not specified).
- `--outbound-type` — How outbound traffic will be configured for a cluster.
- `--outbound-type-sku` — SKU of the managed NAT gateway (Standard or StandardV2).
- `--pod-cidr` — A CIDR notation IP range from which to assign pod IPs when kubenet is used.
- `--private-dns-zone` — The private dns zone mode for private cluster.
- `--rotation-poll-interval` — Set interval of rotation poll. Use with azure-keyvault-secrets-provider addon.
- `--safeguards-excluded-ns` — Comma-separated list of Kubernetes namespaces to exclude from deployment safeguards. Use "" to clear a previously non-empty list.
- `--safeguards-level` — The deployment safeguards Level. Accepted Values are [Off, Warning, Enforcement]. Requires azure policy addon to be enabled.
- `--safeguards-version` — The version of deployment safeguards to use. Default "v1.0.0" Use the ListSafeguardsVersions API to discover available versions.
- `--service-account-image-pull-default-managed-identity-id` — The default managed identity resource ID used for image pulls at the cluster level.
- `--sku` — Specify SKU name for managed clusters. '--sku base' enables a base managed cluster. '--sku automatic' enables an automatic managed cluster.
- `--ssh-key-value` — Public key path or key contents to install on node VMs for SSH access. For example, 'ssh-rsa AAAAB...snip...UcyupgH azureuser@linuxvm'.
- `--storage-pool-name` — Set storage pool name for azure container storage.
- `--storage-pool-option` — Set ephemeral disk storage pool option for azure container storage.
- `--storage-pool-size` — Set storage pool size for azure container storage.
- `--storage-pool-sku` — Set azure disk type storage pool sku for azure container storage.
- `--syslog-port` — Host port used by the Azure Monitor agent to collect syslog. Defaults to 28330 when unset.
- `--system-node-subnet-id` — (Automatic SKU) The ID of a subnet in an existing VNet to be used by the Managed System Pool.
- `--tags` — The tags of the managed cluster. The managed cluster instance and all resources managed by the cloud provider will be tagged.
- `--tier` — Specify SKU tier for managed clusters. '--tier standard' enables a standard managed cluster service with a financially backed SLA. '--tier free' changes a standard managed cluster to a free one.
- `--update-cluster-autoscaler -u` — Update min-count or max-count for cluster autoscaler. Not supported for VirtualMachines pools; use 'az aks nodepool auto-scale update' instead. Default: False.
- `--upgrade-override-until` — Until when the cluster upgradeSettings overrides are effective. It needs to be in a valid date-time format that's within the next 30 days. For example, 2023-04-01T13:00:00Z. Note that if --force-upgrade is set to true and --upgrade-override-until is not set, by default it will be set to 3 days from 
- `--windows-admin-password` — User account password to use on windows node VMs.
- `--workspace-resource-id` — The resource ID of an existing Log Analytics Workspace to use for storing monitoring data. If not specified, uses the default Log Analytics Workspace if it exists, otherwise creates one.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Reconcile the cluster back to its current state.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster
```

*Enable upgrade gate for a kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-upgrade-gate
```

*Enable cluster-autoscaler within node count range [1,5]*
```azurecli
az aks update --enable-cluster-autoscaler --min-count 1 --max-count 5 -g MyResourceGroup -n MyManagedCluster
```

*Disable cluster-autoscaler for an existing cluster*
```azurecli
az aks update --disable-cluster-autoscaler -g MyResourceGroup -n MyManagedCluster
```

*Disable FIPS mode at the cluster level.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-fips
```

*Update min-count or max-count for cluster autoscaler.*
```azurecli
az aks update --update-cluster-autoscaler --min-count 1 --max-count 10 -g MyResourceGroup -n MyManagedCluster
```

*Upgrade load balancer sku to standard*
```azurecli
az aks update --load-balancer-sku standard -g MyResourceGroup -n MyManagedCluster
```

*Update a kubernetes cluster with standard SKU load balancer to use two AKS created IPs for the load balancer outbound connection usage.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --load-balancer-managed-outbound-ip-count 2
```

*Update a kubernetes cluster with standard SKU load balancer to use the provided public IPs for the load balancer outbound connection usage.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --load-balancer-outbound-ips <ip-resource-id-1,ip-resource-id-2>
```

*Update a kubernetes cluster with standard SKU load balancer to use the provided public IP prefixes for the load balancer outbound connection usage.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --load-balancer-outbound-ip-prefixes <ip-prefix-resource-id-1,ip-prefix-resource-id-2>
```

*Update a kubernetes cluster with new outbound type*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --outbound-type managedNATGateway
```

*Update a kubernetes cluster with two outbound AKS managed IPs an idle flow timeout of 5 minutes and 8000 allocated ports per machine*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --load-balancer-managed-outbound-ip-count 2 --load-balancer-idle-timeout 5 --load-balancer-outbound-ports 8000
```

*Update a kubernetes cluster of managedNATGateway outbound type with two outbound AKS managed IPs an idle flow timeout of 4 minutes*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --nat-gateway-managed-outbound-ip-count 2 --nat-gateway-idle-timeout 4
```

*Update a kubernetes cluster with authorized apiserver ip ranges.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --api-server-authorized-ip-ranges 193.168.1.0/24,194.168.1.0/24
```

*Disable authorized apiserver ip ranges feature for a kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --api-server-authorized-ip-ranges ""
```

*Restrict apiserver traffic in a kubernetes cluster to agentpool nodes.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --api-server-authorized-ip-ranges 0.0.0.0/32
```

*Update a AKS-managed AAD cluster with tenant ID or admin group object IDs.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --aad-admin-group-object-ids <id-1,id-2> --aad-tenant-id <id>
```

*Migrate a AKS AAD-Integrated cluster or a non-AAD cluster to a AKS-managed AAD cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-aad --aad-admin-group-object-ids <id-1,id-2> --aad-tenant-id <id>
```

*Enable Azure Hybrid User Benefits featture for a kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-ahub
```

*Disable Azure Hybrid User Benefits featture for a kubernetes cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-ahub
```

*Update the cluster to use system assigned managed identity in control plane.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-managed-identity
```

*Update the cluster to use user assigned managed identity in control plane.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-managed-identity --assign-identity <user_assigned_identity_resource_id>
```

*Enable pod identity addon.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-pod-identity
```

*Disable pod identity addon.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-pod-identity
```

*Update the tags of a kubernetes cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCLuster --tags "foo=bar" "baz=qux"
```

*Update Windows password of a kubernetes cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCLuster --windows-admin-password "Repl@cePassw0rd12345678"
```

*Update a managed AAD AKS cluster to use Azure RBAC*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-azure-rbac
```

*Disable Azure RBAC in a managed AAD AKS cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-azure-rbac
```

*Enable Windows gmsa for a kubernetes cluster with setting DNS server in the vnet used by the cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-windows-gmsa
```

*Enable Windows gmsa for a kubernetes cluster without setting DNS server in the vnet used by the cluster.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-windows-gmsa --gmsa-dns-server "10.240.0.4" --gmsa-root-domain-name "contoso.com"
```

*Update a existing managed cluster to a managed cluster snapshot.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --cluster-snapshot-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedclustersnapshots/mysnapshot1"
```

*Update a kubernetes cluster with safeguards set to "Warning". Assumes azure policy addon is already enabled*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --safeguards-level Warning
```

*Update a kubernetes cluster with safeguards set to "Warning" and some namespaces excluded. Assumes azure policy addon is already enabled*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --safeguards-level Warning --safeguards-excluded-ns ns1,ns2
```

*Enable Azure Monitor logs for a kubernetes cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-azure-monitor-logs
```

*Re-enable Prometheus scraping and change the syslog port on a cluster with Azure Monitor logs enabled*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-prometheus-metrics-scraping --syslog-port 29000
```

*Enable Azure Backup for a kubernetes cluster (default Week strategy). Requires the 'dataprotection' extension.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-backup --yes
```

*Enable Azure Backup with a custom strategy using an existing vault and policy*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-backup --backup-strategy Custom --backup-configuration @config.json --yes
```

*Disable Azure Monitor logs for a kubernetes cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-azure-monitor-logs
```

*Update a kubernetes cluster to clear any namespaces excluded from safeguards. Assumes azure policy addon is already enabled*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --safeguards-excluded-ns ""
```

*Update a kubernetes cluster to enable a managed installation of Gateway API CRDs from the standard release channel.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-gateway-api
```

*Update a kubernetes cluster to disable the managed installation of Gateway API CRDs.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-gateway-api
```

*Enable OpenTelemetry metrics collection on an existing cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-metrics
```

*Enable OpenTelemetry logs and traces collection on an existing cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-logs-traces
```

*Configure OpenTelemetry metrics with custom port*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-metrics --opentelemetry-metrics-port-http 8888
```

*Configure OpenTelemetry logs and traces with custom ports*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-logs-traces --opentelemetry-logs-traces-port-http 8080 --opentelemetry-logs-traces-port-grpc 8082
```

*Configure OpenTelemetry metrics with custom HTTP and gRPC ports*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-opentelemetry-metrics --opentelemetry-metrics-port-http 8888 --opentelemetry-metrics-port-grpc 8889
```

*Disable OpenTelemetry metrics collection on an existing cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-opentelemetry-metrics
```

*Disable OpenTelemetry logs and traces collection on an existing cluster*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --disable-opentelemetry-logs-traces
```

*Convert an existing Automatic cluster to use a Managed System Pool.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-hosted-system
```

*Convert an existing Automatic cluster to use a Managed System Pool in a bring-your-own VNet.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-hosted-system --system-node-subnet-id <systemNodeSubnetID>
```

*Convert an existing Automatic cluster to use a Managed System Pool, also moving node pools and the API server onto a bring-your-own VNet.*
```azurecli
az aks update -g MyResourceGroup -n MyManagedCluster --enable-hosted-system --system-node-subnet-id <systemNodeSubnetID> --node-subnet-id <nodeSubnetID> --apiserver-subnet-id <apiserverSubnetID>
```

## az aks update-credentials

Update credentials for a managed Kubernetes cluster, like service principal.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-secret` — Secret associated with the service principal. This argument is required if `--service-principal` is specified.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--reset-service-principal` — Reset service principal for a managed cluster. Default: False.
- `--service-principal` — Service principal used for authentication to Azure APIs. This argument is required if `--reset-service-principal` is specified.

*Update an existing Kubernetes cluster with new service principal.*
```azurecli
az aks update-credentials -g MyResourceGroup -n MyManagedCluster --reset-service-principal --service-principal MyNewServicePrincipalID --client-secret MyNewServicePrincipalSecret
```

## az aks upgrade

Upgrade a managed Kubernetes cluster to a newer version.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--control-plane-only` — Upgrade the cluster control plane only. If not specified, both control plane AND all node pools will be upgraded. Default: False.
- `--disable-force-upgrade` — Disable forceUpgrade cluster upgrade settings override. Default: False.
- `--enable-force-upgrade` — Enable forceUpgrade cluster upgrade settings override. Default: False.
- `--if-match` — The value provided will be compared to the ETag of the managed cluster, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new cluster.
- `--if-none-match` — Set to '*' to allow a new cluster to be created, but to prevent updating an existing cluster. Other values will be ignored.
- `--k8s-support-plan` — Choose from "KubernetesOfficial" or "AKSLongTermSupport", with "AKSLongTermSupport" you get 1 extra year of CVE patchs.
- `--kubernetes-version -k` — Version of Kubernetes to upgrade the cluster to, such as "1.16.9".
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-image-only` — Only upgrade node image for agent pools. Default: False.
- `--tier` — Specify SKU tier for managed clusters. '--tier standard' enables a standard managed cluster service with a financially backed SLA. '--tier free' does not have a financially backed SLA. '--tier premium' is required for '--k8s-support-plan AKSLongTermSupport'.
- `--upgrade-override-until` — Until when the cluster upgradeSettings overrides are effective.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Upgrade a managed Kubernetes cluster to a newer version. (autogenerated)*
```azurecli
az aks upgrade --kubernetes-version 1.12.6 --name MyManagedCluster --resource-group MyResourceGroup
```

## az aks upgrade  (extension: aks-preview etc.)

Upgrade a managed Kubernetes cluster to a newer version.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--aks-custom-headers` — Send custom headers. When specified, format should be Key1=Value1,Key2=Value2.
- `--change-reference` — The related change reference ID for this resource operation.
- `--cluster-snapshot-id` — The source cluster snapshot id is used to upgrade existing cluster.
- `--control-plane-only` — Upgrade the cluster control plane only. If not specified, control plane AND all node pools will be upgraded. Default: False.
- `--disable-force-upgrade` — Disable forceUpgrade cluster upgrade settings override. Default: False.
- `--enable-force-upgrade` — Enable forceUpgrade cluster upgrade settings override. Default: False.
- `--if-match` — The value provided will be compared to the ETag of the managed cluster, if it matches the operation will proceed. If it does not match, the request will be rejected to prevent accidental overwrites. This must not be specified when creating a new cluster.
- `--if-none-match` — Set to '*' to allow a new cluster to be created, but to prevent updating an existing cluster. Other values will be ignored.
- `--k8s-support-plan` — Choose from "KubernetesOfficial" or "AKSLongTermSupport". With "AKSLongTermSupport" you get 1 extra year of CVE patches.
- `--kubernetes-version -k` — Version of Kubernetes to upgrade the cluster to, such as "1.11.12".
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--node-image-only` — Only upgrade node image for agent pools. Default: False.
- `--tier` — Specify SKU tier for managed clusters. '--tier standard' enables a standard managed cluster service with a financially backed SLA. '--tier free' does not have a financially backed SLA. '--tier premium' is required for '--k8s-support-plan AKSLongTermSupport'.
- `--upgrade-override-until` — Until when the cluster upgradeSettings overrides are effective.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Upgrade a existing managed cluster to a managed cluster snapshot.*
```azurecli
az aks upgrade -g MyResourceGroup -n MyManagedCluster --cluster-snapshot-id "/subscriptions/00000/resourceGroups/AnotherResourceGroup/providers/Microsoft.ContainerService/managedclustersnapshots/mysnapshot1"
```

## az aks use-dev-spaces  (Deprecated)

Use Azure Dev Spaces with a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--endpoint -e` — The endpoint type to be used for an Azure Dev Spaces controller. See https://aka.ms/azds-networking for more information. Default: Public.
- `--space -s` — Name of the new or existing dev space to select. Defaults to an interactive selection experience.
- `--update` — Update to the latest Azure Dev Spaces client components. Default: False.
- `--yes -y` — Do not prompt for confirmation. Requires --space. Default: False.

*Use Azure Dev Spaces with a managed Kubernetes cluster, interactively selecting a dev space.*
```azurecli
az aks use-dev-spaces -g my-aks-group -n my-aks
```

*Use Azure Dev Spaces with a managed Kubernetes cluster, updating to the latest Azure Dev Spaces             client components and selecting a new or existing dev space 'my-space'.*
```azurecli
az aks use-dev-spaces -g my-aks-group -n my-aks --update --space my-space
```

*Use Azure Dev Spaces with a managed Kubernetes cluster, selecting a new or existing dev space             'develop/my-space' without prompting for confirmation.*
```azurecli
az aks use-dev-spaces -g my-aks-group -n my-aks -s develop/my-space -y
```

*Use Azure Dev Spaces with a managed Kubernetes cluster with a private endpoint.*
```azurecli
az aks use-dev-spaces -g my-aks-group -n my-aks -e private
```

## az aks use-dev-spaces  (extension: aks-preview etc.)

Use Azure Dev Spaces with a managed Kubernetes cluster.

**Required parameters**

- `--name -n` — Name of the managed cluster.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--endpoint -e` — The endpoint type to be used for an Azure Dev Spaces controller. See https://aka.ms/azds-networking for more information. Default: Public.
- `--space -s` — Name of the new or existing dev space to select. Defaults to an interactive selection experience.
- `--update` — Update to the latest Azure Dev Spaces client components. Default: False.
- `--yes -y` — Do not prompt for confirmation. Requires --space. Default: False.

*Use Azure Dev Spaces with a managed Kubernetes cluster, interactively selecting a dev space.*
```azurecli
az aks use-dev-spaces -g my-aks-group -n my-aks
```

*Use Azure Dev Spaces with a managed Kubernetes cluster, updating to the latest Azure Dev Spaces             client components and selecting a new or existing dev space 'my-space'.*
```azurecli
az aks use-dev-spaces -g my-aks-group -n my-aks --update --space my-space
```

*Use Azure Dev Spaces with a managed Kubernetes cluster, selecting a new or existing dev space             'develop/my-space' without prompting for confirmation.*
```azurecli
az aks use-dev-spaces -g my-aks-group -n my-aks -s develop/my-space -y
```

*Use Azure Dev Spaces with a managed Kubernetes cluster with a private endpoint.*
```azurecli
az aks use-dev-spaces -g my-aks-group -n my-aks -e private
```

## az aks wait

Wait for a managed Kubernetes cluster to reach a desired state.

**Required parameters**

- `--name -n` — Name of the managed cluster.
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

*Wait for a cluster to be upgraded, polling every minute for up to thirty minutes.*
```azurecli
az aks wait -g MyResourceGroup -n MyManagedCluster --updated --interval 60 --timeout 1800
```

*Wait for a managed Kubernetes cluster to reach a desired state (autogenerated)*
```azurecli
az aks wait --created --interval 60 --name MyManagedCluster --resource-group MyResourceGroup --timeout 1800
```

## az aks wait  (extension: aks-preview etc.)

Wait for a managed Kubernetes cluster to reach a desired state.

**Required parameters**

- `--name -n` — Name of the managed cluster.
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

*Wait for a cluster to be upgraded, polling every minute for up to thirty minutes.*
```azurecli
az aks wait -g MyResourceGroup -n MyManagedCluster --updated --interval 60 --timeout 1800
```

*Wait for a managed Kubernetes cluster to reach a desired state (autogenerated)*
```azurecli
az aks wait --created --interval 60 --name MyManagedCluster --resource-group MyResourceGroup --timeout 1800
```
