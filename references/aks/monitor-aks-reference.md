# Monitoring data reference for Azure Kubernetes Service

> Source: https://learn.microsoft.com/en-us/azure/aks/monitor-aks-reference  
> Microsoft doc last updated: 09/06/2024


See [Monitor Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/monitor-aks) for details on the data you can collect for AKS and how to use it.

### Supported metrics for Microsoft.ContainerService/managedClusters

The following table lists the metrics available for the Microsoft.ContainerService/managedClusters resource type.

> [!IMPORTANT]
> The `pod` dimension for the AKS platform metrics `kube_pod_status_ready` and
> `kube_pod_status_phase` will be retired on September 30, 2027. To continue
> using the `pod` dimension in these metrics after the retirement date, use
> [Azure Monitor managed service for Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/prometheus-metrics-overview).

### Supported metrics for microsoft.kubernetes/connectedClusters

The following table lists the metrics available for the microsoft.kubernetes/connectedClusters resource type.

### Supported metrics for microsoft.kubernetesconfiguration/extensions

The following table lists the metrics available for the microsoft.kubernetesconfiguration/extensions resource type.

### Supported metrics for Microsoft.Compute/virtualMachines

The following table lists the metrics available for the Microsoft.Compute/virtualMachines resource type.

### Supported metrics for Microsoft.Compute/virtualmachineScaleSets

The following table lists the metrics available for the Microsoft.Compute/virtualmachineScaleSets resource type.

### Supported metrics for Microsoft.Compute/virtualMachineScaleSets/virtualMachines

The following table lists the metrics available for the Microsoft.Compute/virtualMachineScaleSets/virtualMachines resource type.

## Minimal ingestion profile for control plane Metrics in Managed Prometheus

Azure Monitor metrics add-on collects many Prometheus metrics by default. `Minimal ingestion profile` is a setting that helps reduce ingestion volume of metrics, as only metrics used by default dashboards, default recording rules and default alerts are collected. This section describes how this setting is configured specifically for control plane metrics. This section also lists metrics collected by default when `minimal ingestion profile` is enabled.

> [!NOTE]
> For add-on-based collection, `Minimal ingestion profile` setting is enabled by default. The discussion here is focused on control plane metrics. The current set of default targets and metrics is listed [here](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/prometheus-metrics-scrape-configuration-minimal).

Following targets are **enabled/ON** by default - meaning you don't have to provide any scrape job configuration for scraping these targets, as metrics add-on scrapes these targets automatically by default:

- `controlplane-apiserver` (job=`controlplane-apiserver`)
- `controlplane-etcd` (job=`controlplane-etcd`)

Following targets are available to scrape, but scraping isn't enabled (**disabled/OFF**) by default. Meaning you don't have to provide any scrape job configuration for scraping these targets, and you need to turn **ON/enable** scraping for these targets using the [ama-metrics-settings-configmap](https://github.com/Azure/prometheus-collector/blob/89e865a73601c0798410016e9beb323f1ecba335/otelcollector/configmaps/ama-metrics-settings-configmap.yaml) under the `default-scrape-settings-enabled` section.

- `controlplane-cluster-autoscaler`
- `controlplane-node-auto-provisioning`
- `controlplane-kube-scheduler`
- `controlplane-kube-controller-manager`

> [!NOTE]
> The default scrape frequency for all default targets and scrapes is `30 seconds`. You can override it for each target using the [ama-metrics-settings-configmap](https://github.com/Azure/prometheus-collector/blob/89e865a73601c0798410016e9beb323f1ecba335/otelcollector/configmaps/ama-metrics-settings-configmap.yaml) under `default-targets-scrape-interval-settings` section.

### Minimal ingestion for default ON targets

The following metrics are allow-listed with `minimalingestionprofile=true` for default **ON** targets. The below metrics are collected by default, as these targets are scraped by default.

controlplane-apiserver:

- `apiserver_request_total`
- `apiserver_cache_list_fetched_objects_total`
- `apiserver_cache_list_returned_objects_total`
- `apiserver_flowcontrol_demand_seats_average`
- `apiserver_flowcontrol_current_limit_seats`
- ~~`apiserver_request_sli_duration_seconds_bucket`~~
- `apiserver_request_sli_duration_seconds_sum`
- `apiserver_request_sli_duration_seconds_count`
- `process_start_time_seconds`
- ~~`apiserver_request_duration_seconds_bucket`~~
- `apiserver_request_duration_seconds_sum`
- `apiserver_request_duration_seconds_count`
- `apiserver_storage_list_fetched_objects_total`
- `apiserver_storage_list_returned_objects_total`
- `apiserver_current_inflight_requests`

> [!NOTE]
> `apiserver_request_sli_duration_seconds_bucket` and `apiserver_request_duration_seconds_bucket`  are not collected now with a recent release. These are high cardinality metrics which may increase the number of metrics stored based on the number of custom resources in the cluster. If you would like to collect these bucket metrics, you can add it to the keep list. We highly recommend not turning off the minimal ingestion profile for the control plane components

controlplane-etcd:

- `etcd_server_has_leader`
- `rest_client_requests_total`
- `etcd_mvcc_db_total_size_in_bytes`
- `etcd_mvcc_db_total_size_in_use_in_bytes`
- `etcd_server_slow_read_indexes_total`
- `etcd_server_slow_apply_total`
- `etcd_network_client_grpc_sent_bytes_total`
- `etcd_server_heartbeat_send_failures_total`

### Minimal ingestion for default OFF targets

The following are metrics that are allow-listed with `minimalingestionprofile=true` for default **OFF** targets. These metrics aren't collected by default. You can turn **ON** scraping for these targets using `default-scrape-settings-enabled.<target-name>=true` using the [ama-metrics-settings-configmap](https://github.com/Azure/prometheus-collector/blob/89e865a73601c0798410016e9beb323f1ecba335/otelcollector/configmaps/ama-metrics-settings-configmap.yaml) under the `default-scrape-settings-enabled` section.

controlplane-kube-controller-manager:

- `workqueue_depth `
- `rest_client_requests_total`
- `rest_client_request_duration_seconds `

controlplane-kube-scheduler:

- `scheduler_pending_pods`
- `scheduler_unschedulable_pods`
- `scheduler_queue_incoming_pods_total`
- `scheduler_schedule_attempts_total`
- `scheduler_preemption_attempts_total`

controlplane-cluster-autoscaler:

- `rest_client_requests_total`
- `cluster_autoscaler_last_activity`
- `cluster_autoscaler_cluster_safe_to_autoscale`
- `cluster_autoscaler_failed_scale_ups_total`
- `cluster_autoscaler_scale_down_in_cooldown`
- `cluster_autoscaler_scaled_up_nodes_total`
- `cluster_autoscaler_unneeded_nodes_count`
- `cluster_autoscaler_unschedulable_pods_count`
- `cluster_autoscaler_nodes_count`
- `cloudprovider_azure_api_request_errors`
- `cloudprovider_azure_api_request_duration_seconds_bucket`
- `cloudprovider_azure_api_request_duration_seconds_count`

controlplane-node-auto-provisioning:

- `karpenter_pods_state`
- `karpenter_nodes_created_total`
- `karpenter_nodes_terminated_total`
- `karpenter_nodeclaims_disrupted_total`
- `karpenter_voluntary_disruption_eligible_nodes`
- `karpenter_voluntary_disruption_decisions_total`

> [!NOTE]
> The CPU and memory usage metrics for all control-plane targets are not exposed irrespective of the profile.

| Dimension Name | Description |
|:------------------- |:----------------- |
| requestKind | Used by metrics such as *Inflight Requests* to split by type of request. |
| condition | Used by metrics such as *Statuses for various node conditions*, *Number of pods in Ready state* to split by condition type. |
| status | Used by metrics such as *Statuses for various node conditions* to split by status of the condition. |
| status2 | Used by metrics such as *Statuses for various node conditions* to split by status of the condition.  |
| node | Used by metrics such as *CPU Usage Millicores* to split by the name of the node. |
| phase | Used by metrics such as *Number of pods by phase* to split by the phase of the pod. |
| namespace | Used by metrics such as *Number of pods by phase* to split by the namespace of the pod. |
| pod | Used by metrics such as *Number of pods by phase* to split by the name of the pod. |
| nodepool | Used by metrics such as *Disk Used Bytes* to split by the name of the nodepool. |
| device | Used by metrics such as *Disk Used Bytes* to split by the name of the device. |
| 3gppGen | Used by metrics such as *Number of Active PDU Sessions*. |
| Cause | Used by metrics such as *User plane packet drop rate*. |
| Direction | Used by metrics such as *User plane bandwidth*. |
| Dnn | Used by metrics such as *PDU session establishment attempts rate*. |
| Interface | Used by metrics such as *User plane bandwidth*. |
| LUN | Used by metrics such as *Percentage of data disk bandwidth consumed*. |
| PccpId | Used by metrics such as *Number of Active PDU Sessions*. |
| Result | Used by metrics such as *Authentication failure rate*. |
| SiteId | Used by metrics such as *Number of Active PDU Sessions*. |
| Tai | Used by metrics such as *Service request failure rate*. |
| VMName | Used by metrics such as *Amount of physical memory*. |

### Supported resource logs for Microsoft.ContainerService/fleets

### Supported resource logs for Microsoft.ContainerService/managedClusters

### Supported resource logs for microsoft.kubernetes/connectedClusters

### Supported resource logs for Microsoft.Compute/virtualMachines

### AKS Microsoft.ContainerService/managedClusters

- [AzureActivity](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/azureactivity#columns)
- [AzureDiagnostics](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/azurediagnostics#columns)
- [AzureMetrics](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/azuremetrics#columns)
- [ContainerImageInventory](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/containerimageinventory#columns)
- [ContainerInventory](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/containerinventory#columns)
- [ContainerLog](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/containerlog#columns)
- [ContainerLogV2](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/containerlogv2#columns)
- [ContainerNodeInventory](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/containernodeinventory#columns)
- [ContainerServiceLog](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/containerservicelog#columns)
- [Heartbeat](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/heartbeat#columns)
- [InsightsMetrics](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/insightsmetrics#columns)
- [KubeEvents](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/kubeevents#columns)
- [KubeMonAgentEvents](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/kubemonagentevents#columns)
- [KubeNodeInventory](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/kubenodeinventory#columns)
- [KubePodInventory](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/kubepodinventory#columns)
- [KubePVInventory](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/kubepvinventory#columns)
- [KubeServices](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/kubeservices#columns)
- [Perf](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/perf#columns)
- [Syslog](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/syslog#columns)
- [AKSAudit](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aksaudit#columns)
- [AKSAuditAdmin](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aksauditAdmin#columns)
- [AKSControlPlane](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/akscontrolplane#columns)

- [Microsoft.ContainerService resource provider operations](https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#containers)

The following table lists a few example operations related to AKS that might be created in the Activity log. Use the Activity log to track information such as when a cluster is created or had its configuration change. You can view this information in the portal or by using [other methods](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log#other-methods-to-retrieve-activity-log-events). You can also use it to create an Activity log alert to be proactively notified when an event occurs.

| Operation | Description |
|:---|:---|
| Microsoft.ContainerService/managedClusters/write | Create or update managed cluster |
| Microsoft.ContainerService/managedClusters/delete | Delete Managed Cluster |
| Microsoft.ContainerService/managedClusters/listClusterMonitoringUserCredential/action | List clusterMonitoringUser credential |
| Microsoft.ContainerService/managedClusters/listClusterAdminCredential/action | List clusterAdmin credential |
| Microsoft.ContainerService/managedClusters/agentpools/write | Create or Update Agent Pool |

## Related content

- See [Monitor Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/monitor-aks) for a description of monitoring AKS.
- See [Monitor Azure resources with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/monitor-azure-resource) for details on monitoring Azure resources.
