# Upgrade Options and Recommendations for Azure Kubernetes Service (AKS) Clusters

> Source: https://learn.microsoft.com/en-us/azure/aks/upgrade-options  
> Microsoft doc last updated: 06/22/2026


**Applies to**: :heavy_check_mark: AKS Automatic :heavy_check_mark: AKS Standard

> [!IMPORTANT]
> **AKS platform-initiated upgrades.** Starting on **June 1, 2027**, AKS automatically upgrades any cluster that stays on an unsupported Kubernetes version after its 60-day [platform support grace period](https://learn.microsoft.com/en-us/azure/aks/platform-initiated-upgrades#platform-support-grace-period) ends. A platform-initiated upgrade **doesn't follow your maintenance window**, **doesn't stop for deprecated API usage**, and **can override a Pod Disruption Budget** that blocks a node drain, so workloads might be disrupted. Before the upgrade month, replace APIs removed from the target Kubernetes version and update incompatible self-managed add-ons. Keep your clusters on a supported Kubernetes version to avoid a platform-initiated upgrade. For more information, see [Prepare for platform-initiated upgrades in AKS](https://learn.microsoft.com/en-us/azure/aks/platform-initiated-upgrades#prepare-before-aks-starts-the-upgrade).

For most production workloads, AKS Automatic is the recommended default cluster experience. It provides production-ready defaults for cluster and node lifecycle operations, including managed upgrade behavior, built-in safeguards, and reduced operational overhead.

AKS Standard remains available for scenarios where you need deeper manual control over upgrade mechanics, networking choices, or node pool behavior.

This article gives you a technical foundation for AKS upgrades by covering upgrade options, common scenarios, and recommendations for both AKS Automatic and AKS Standard.

## What this article covers

This technical reference covers:

- Why AKS Automatic is the recommended production-ready default for most workloads.
- How upgrade behavior differs between AKS Automatic and AKS Standard.
- Manual versus automated upgrade paths, and when to use each.
- Common upgrade scenarios with specific recommendations.
- Optimization techniques for performance and minimal disruption.
- Validation processes and pre-upgrade checks.

For related guidance:

- For AKS Automatic overview and defaults, see [Introduction to Azure Kubernetes Service (AKS) Automatic](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic).
- For production-oriented AKS upgrade strategy details, see [AKS production upgrade strategies](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies).
- For stateful workload upgrade patterns, see [Stateful workload upgrade patterns](https://learn.microsoft.com/en-us/azure/aks/stateful-workload-upgrades).
- For scenario-led guidance, see [AKS upgrade scenarios: Choose your path](https://learn.microsoft.com/en-us/azure/aks/upgrade-scenarios-hub).
- If you're new to AKS upgrades, start with the [upgrade scenarios hub](https://learn.microsoft.com/en-us/azure/aks/upgrade-scenarios-hub) for guided assistance.

## Quick navigation

| Your situation | Recommended path |
| -------------- | ---------------- |
| New or existing production workload with no special customization requirements | [Create an AKS Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network) |
| Production cluster with strict custom upgrade controls | [Production upgrade strategies](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies) |
| Database or stateful workloads | [Stateful workload patterns](https://learn.microsoft.com/en-us/azure/aks/stateful-workload-upgrades) |
| First-time AKS Standard upgrade | [Basic AKS cluster upgrade](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-cluster) |
| Multiple environments or fleet operations | [Upgrade scenarios hub](https://learn.microsoft.com/en-us/azure/aks/upgrade-scenarios-hub) |
| Node pools or Windows nodes in AKS Standard | [Node pool upgrades][nodepool-upgrade] |
| Specific node pool only | [Single node pool upgrade][specific-nodepool] |

## Upgrade operating models

### AKS Automatic (recommended production default)

AKS Automatic is designed for production-ready operation by default. For upgrades, AKS Automatic provides:

- Managed system node pools.
- Automatic cluster upgrade behavior with platform-managed defaults.
- Automatic node OS image upgrade behavior with security-focused cadence.
- Built-in checks for deprecated Kubernetes APIs.
- Planned maintenance schedule support.

Use AKS Automatic when you want to minimize manual upgrade orchestration and keep production clusters aligned to supported versions with less effort.

### AKS Standard (advanced control model)

AKS Standard gives you direct control over upgrade sequencing and tuning. You choose and manage:

- Manual or automatic upgrade configuration.
- Upgrade channel selection.
- Node pool and surge behavior.
- Operational procedures around maintenance windows and workload disruption budgets.

Use AKS Standard when your environment requires customization that goes beyond AKS Automatic defaults.

### Platform-initiated upgrades

Both operating models are subject to [platform-initiated upgrades](https://learn.microsoft.com/en-us/azure/aks/platform-initiated-upgrades). If a cluster stays on an unsupported Kubernetes version after the 60-day [platform support grace period](https://learn.microsoft.com/en-us/azure/aks/platform-initiated-upgrades#platform-support-grace-period) ends, AKS upgrades it to a supported version automatically.

Platform-initiated upgrades don't follow your maintenance window and don't run the deprecated API check. Keeping your cluster on a supported version is the only way to keep full control of upgrade timing and behavior. For more information, see [How to avoid platform-initiated upgrades](https://learn.microsoft.com/en-us/azure/aks/platform-initiated-upgrades#how-to-avoid-platform-initiated-upgrades).

## Upgrade options

### Perform manual upgrades

Applies primarily to AKS Standard, or to specialized operational workflows.

Manual upgrades let you control when your cluster upgrades to a new Kubernetes version. These upgrades are useful for testing, staged rollouts, and targeted version adoption.

- [Upgrade an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-cluster)
- [Upgrade multiple AKS clusters via Azure Kubernetes Fleet Manager](https://learn.microsoft.com/en-us/azure/kubernetes-fleet/update-orchestration)
- [Upgrade the node image](https://learn.microsoft.com/en-us/azure/aks/node-image-upgrade)
- [Customize node surge upgrade](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling#customize-node-surge)
- [Process node OS updates](https://learn.microsoft.com/en-us/azure/aks/node-updates-kured)

### Configure automatic upgrades

For AKS Standard, automatic upgrades help keep clusters on supported versions while preserving control over policy and scheduling. In AKS Automatic, upgrade automation and guardrails are already part of the default operating model.

- [Automatically upgrade an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-cluster)
- [Automatically upgrade multiple AKS clusters via Azure Kubernetes Fleet Manager](https://learn.microsoft.com/en-us/azure/kubernetes-fleet/update-automation)
- [Use planned maintenance to schedule and control upgrades](https://learn.microsoft.com/en-us/azure/aks/planned-maintenance)
- [Stop AKS cluster upgrades automatically on API breaking changes (preview)](https://learn.microsoft.com/en-us/azure/aks/stop-cluster-upgrade-api-breaking-changes)
- [Automatically upgrade AKS cluster node operating system images](https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-node-image)
- [Apply security updates to AKS nodes automatically by using GitHub actions](https://learn.microsoft.com/en-us/azure/aks/node-upgrade-github-actions)

### Special considerations for node pools that span multiple availability zones

AKS uses best-effort zone balancing in node pools. During an upgrade surge, the zones for surge nodes in virtual machine scale sets are unknown ahead of time, which can temporarily cause an unbalanced zone configuration. AKS deletes surge nodes after the upgrade and restores the original zone balance.

To keep zones balanced, set surge to a multiple of three nodes. Persistent volume claims that use Azure locally redundant storage disks are zone bound and might cause downtime if surge nodes are in a different zone. Use a [pod disruption budget (PDB)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) to maintain high availability during drains.

### Optimize upgrades to improve performance and minimize disruptions

Combine [planned maintenance window][planned-maintenance], [max surge](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling#customize-node-surge), [PDB][pdb-spec], [node drain timeout][drain-timeout], and [node soak time][soak-time] to increase the likelihood of successful, low-disruption upgrades.

#### AKS Automatic

In AKS Automatic, platform-level upgrade behavior is preconfigured. Focus your tuning on workload resilience and capacity readiness:

- Validate pod disruption budgets and replica counts.
- Ensure quota and subnet capacity for expected growth.
- Set planned maintenance schedules aligned to low-traffic periods.
- Monitor upgrade events and critical workload readiness.

#### AKS Standard

In AKS Standard, tune upgrade controls directly:

- [Planned maintenance window][planned-maintenance]: Schedule auto-upgrade during low-traffic periods. Use at least four hours.
- [Max surge](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling#set-max-surge-value): Higher values speed upgrades but might disrupt workloads. Use 33% for production.
- [Max unavailable](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling#customize-unavailable-nodes): Use when capacity is limited.
- [Pod disruption budget][pdb-spec]: Set to limit pods down during upgrades. Validate for your service.
- [Node drain timeout][drain-timeout]: Configure pod eviction wait duration. The default is 30 minutes.
- [Node soak time][soak-time]: Stagger upgrades to minimize downtime. The default is 0 minutes.

| Upgrade settings | How extra nodes are used | Expected behavior |
| ---------------- | ------------------------ | ----------------- |
| `maxSurge=5`, `maxUnavailable=0` | 5 surge nodes | Five nodes are surged for upgrade. |
| `maxSurge=5`, `maxUnavailable=0` | 0-4 surge nodes | Upgrade fails because of insufficient surge nodes. |
| `maxSurge=0`, `maxUnavailable=5` | N/A | Five existing nodes are drained for upgrade. |

> [!NOTE]
> Before you upgrade, check for API breaking changes and review the [AKS release notes](https://github.com/Azure/AKS/releases) to avoid disruptions.

## Validate LocalDNS and custom DNS before upgrading to Kubernetes 1.37

Starting with Kubernetes 1.37, AKS defaults an AKS Standard node pool that doesn't have an explicit LocalDNS profile to `Preferred` mode, and enables LocalDNS when the node pool passes the compatibility checks. This change affects the workload DNS path and can expose existing custom DNS or firewall configurations that support UDP port 53 but not TCP port 53.

Before upgrading a node pool to Kubernetes 1.37 or later:

1. Check whether the node pool has an explicit LocalDNS profile.
1. Test the custom virtual network DNS server from an AKS node over both UDP and TCP.

    ```bash
    dig +udp @<custom-dns-ip> <fqdn>
    dig +tcp @<custom-dns-ip> <fqdn>
    ```

1. Verify that NSGs, firewalls, NVAs, and routes permit both UDP and TCP port 53.
1. Upgrade a non-production node pool first and monitor CoreDNS and LocalDNS errors.
1. If the DNS path isn't ready for LocalDNS, explicitly configure `mode` as `Disabled` before upgrading.

For configuration and opt-out instructions, see [Configure LocalDNS in AKS](https://learn.microsoft.com/en-us/azure/aks/localdns-custom).

## Validations used in the upgrade process

AKS performs pre-upgrade validations to ensure cluster health:

- **API breaking changes:** Detects deprecated APIs.
- **Kubernetes upgrade version:** Ensures a valid upgrade path.
- **PDB configuration:** Checks for misconfigured PDBs (for example, `maxUnavailable=0`).
- **Quota:** Confirms enough quota for surge nodes.
- **Subnet:** Verifies sufficient IP addresses.
- **Certificates/service principals:** Detects expired credentials.
- **Managed Resource Lock Check:** Checks for resource locks applied to the managed cluster resource group.

These checks apply across AKS. In AKS Automatic, they're integrated into the managed upgrade path; in AKS Standard, they're part of your operational workflow.

> [!NOTE]
> [Platform-initiated upgrades](https://learn.microsoft.com/en-us/azure/aks/platform-initiated-upgrades) bypass the API breaking-change and PDB validations so that the upgrade can complete. Run these checks yourself and fix any problems before your cluster's platform-initiated upgrade month.

## Common upgrade scenarios and recommendations

### Scenario 1: Capacity constraints

If your cluster is limited by product tier or regional capacity, upgrades might fail when surge nodes can't be provisioned. This situation is common with specialized product tiers (like GPU nodes) or in regions with limited resources. Errors such as `SKUNotAvailable`, `AllocationFailed`, or `OverconstrainedAllocationRequest` might occur if `maxSurge` is set too high for available capacity.

#### AKS Automatic guidance

- Keep planned maintenance windows in place.
- Validate subscription quota and subnet headroom before expected upgrade periods.
- Keep workload scaling and disruption budgets aligned to maintenance windows.

#### AKS Standard guidance

- Use `maxUnavailable` to upgrade by using existing nodes instead of surging new ones. For more information, see [Customize unavailable nodes during upgrade](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling#customize-unavailable-nodes).
- Lower `maxSurge` to reduce extra capacity needs. For more information, see [Customize node surge upgrade](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling#customize-node-surge).
- For security-only updates, use security patch reimages that don't require surge nodes. For more information, see [Apply security and kernel updates to Linux nodes in Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/node-updates-kured).

### Scenario 2: Node drain failures and PDBs

Upgrades require draining nodes (evicting pods). Drains can fail when pods are slow to terminate or strict [Pod Disruption Budgets (PDBs)](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) block pod evictions.

Example error:

```output
Code: UpgradeFailed
Message: Drain node ... failed when evicting pod ... Cannot evict pod as it would violate the pod's disruption budget.
```

#### AKS Automatic guidance

- Treat PDB and replica strategy as the primary reliability controls.
- Validate disruption budgets in staging before production rollout.
- Keep critical workloads configured for rolling eviction success.

#### AKS Standard guidance

##### Option 1: Force upgrade, bypass PDB constraints

> [!WARNING]
> Force upgrade bypasses Pod Disruption Budget (PDB) constraints and might cause service disruption by draining all pods simultaneously. Before using this option, first try to fix PDB misconfigurations (review the PDB minAvailable/maxUnavailable settings, ensure adequate pod replicas, verify PDBs aren't blocking all evictions).

Use force upgrade only when PDBs prevent critical upgrades and can't be resolved. This action overrides PDB protections and can potentially cause complete service unavailability during the upgrade.

**Requirements**: Azure CLI 2.79.0+ or AKS API version 2025-09-01+

```azurecli-interactive
az aks upgrade \
  --name $CLUSTER_NAME \
  --resource-group $RESOURCE_GROUP_NAME \
  --kubernetes-version $KUBERNETES_VERSION \
  --enable-force-upgrade \
  --upgrade-override-until yyyy-mm-ddT13:00:00Z
```

> [!NOTE]
>
> - The `upgrade-override-until` parameter defines when validation bypass ends (must be a future date/time)
> - If not specified, the window defaults to three days from current time
> - The `Z` indicates UTC/GMT time zone

> [!WARNING]
> When force upgrade is enabled, it takes precedence over all other drain configurations. The undrainable node behavior settings (Option 2) aren't applied when force upgrade is active.

##### Option 2: Handle undrainable nodes while honoring PDBs

Use this conservative approach to honor PDBs while preventing upgrade failures.

Configure undrainable node behavior:

```azurecli-interactive
az aks nodepool update \
  --resource-group <resource-group-name> \
  --cluster-name <cluster-name> \
  --name <node-pool-name> \
  --undrainable-node-behavior Cordon \
  --max-blocked-nodes 2 \
  --drain-timeout 30
```

Behavior options:

- **Schedule (default)**: Deletes blocked node and surges replacement.
- **Cordon (recommended)**: Cordons node and labels it as `kubernetes.azure.com/upgrade-status=Quarantined`.

Max blocked nodes:

- Specifies how many nodes that fail to drain are tolerated
- Requires `undrainable-node-behavior` to be set
- Defaults to `maxSurge` value (typically 10%) if not specified
- Like max surge, if the calculated value is higher than the number of nodes remaining to be upgraded in the current operation, the number of nodes remaining to be upgraded is used instead

###### Example configuration with max blocked nodes

```azurecli-interactive
az aks nodepool update \
  --cluster-name jizenMC1 \
  --name nodepool1 \
  --resource-group jizenTestMaxBlockedNodesRG \
  --max-surge 1 \
  --undrainable-node-behavior Cordon \
  --max-blocked-nodes 2 \
  --drain-timeout 5
```

##### Option 3: Automatic PDB management (preview)

Use the [automatic PDB management](https://learn.microsoft.com/en-us/azure/aks/automatic-pod-disruption-budget-management) extension to proactively resolve PDB-blocked drains without bypassing PDB protections or requiring manual cleanup of quarantined nodes. Automatic PDB management detects when a PDB blocks eviction on a cordoned node and temporarily scales up the deployment's replicas so the disruption budget is satisfied. After the drain completes, it scales replicas back to their original count.

Automatic PDB management can also automatically create PDBs for deployments that don't have one, ensuring your workloads are protected during upgrade drains. For installation and configuration details, see [Manage Pod Disruption Budgets automatically during AKS upgrades](https://learn.microsoft.com/en-us/azure/aks/automatic-pod-disruption-budget-management).

###### Recommendations to prevent drain failures

- Set `maxUnavailable` in PDBs to allow at least one pod eviction
- Increase pod replicas to meet disruption budget requirements
- Extend drain timeout if workloads need more time. (The default is *30 minutes*.)
- Use [automatic PDB management](https://learn.microsoft.com/en-us/azure/aks/automatic-pod-disruption-budget-management) to automate PDB creation and replica scaling during drain operations.
- Test PDBs in staging, monitor upgrade events, and use blue-green deployments for critical workloads. For more information, see [Blue-green deployment of AKS clusters](https://learn.microsoft.com/en-us/azure/architecture/guide/aks/blue-green-deployment-for-aks).

###### Verify undrainable nodes

- The blocked nodes are unscheduled for pods and marked with the label `"kubernetes.azure.com/upgrade-status: Quarantined"`.
- Verify the label on any blocked nodes when there's a drain node failure on upgrade:

    ```bash
    kubectl get nodes --show-labels=true
    ```

###### Resolve undrainable nodes

1. Remove the responsible PDB:

    ```bash
    kubectl delete pdb <pdb-name>
    ```

1. Remove the `kubernetes.azure.com/upgrade-status: Quarantined` label:

    ```bash
    kubectl label nodes <node-name> kubernetes.azure.com/upgrade-status-
    ```

1. Optionally, delete the blocked node:

    ```azurecli-interactive
    az aks nodepool delete-machines --cluster-name <cluster-name> --machine-names <machine-name> --name <node-pool-name> --resource-group <resource-group-name>
    ```

1. After you finish this step, you can reconcile the cluster status by performing any update operation without the optional fields as outlined in [`az aks`](https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-update). Alternatively, you can scale the node pool to the same number of nodes as the count of upgraded nodes. This action ensures that the node pool gets to its intended original size. AKS prioritizes the removal of the blocked nodes. This command also restores the cluster provisioning status to `Succeeded`. In the following example, `2` is the total number of upgraded nodes.

    ```azurecli-interactive
    # Update the cluster to restore the provisioning status
    az aks update --resource-group <resource-group-name> --name <cluster-name>

    # Scale the node pool to restore the original size
    az aks nodepool scale --resource-group <resource-group-name> --cluster-name <cluster-name> --name <node-pool-name> --node-count 2
    ```

### Scenario 3: Slow upgrades

Conservative settings or node-level issues can delay upgrades, which affects your ability to stay current with patches and improvements.

Common causes of slow upgrades include:

- Low `maxSurge` or `maxUnavailable` values (limits parallelism).
- High soak times (long waits between node upgrades).
- Drain failures (see [Node drain failures](#scenario-2-node-drain-failures-and-pdbs)).

#### AKS Automatic guidance

- Keep maintenance schedules current.
- Monitor upgrade event health and workload readiness.
- Resolve blocking PDB or capacity problems quickly to avoid prolonged lag.

#### AKS Standard guidance

- Use `maxSurge=33%`, `maxUnavailable=1` for production.
- Use `maxSurge=50%`, `maxUnavailable=2` for dev/test.
- Use OS Security Patch for fast, targeted patching (avoids full node reimaging).
- Enable `--undrainable-node-behavior` to avoid upgrade blockers.

### Scenario 4: IP exhaustion

Surge nodes require more IPs. If the subnet is near capacity, node provisioning can fail (for example, `Error: SubnetIsFull`). This scenario is common with Azure Container Networking Interface, high `maxPods`, or large node counts.

#### AKS Automatic guidance

- Validate subnet and capacity plans before production expansion.
- Monitor network utilization as part of routine operations.

#### AKS Standard guidance

- Ensure that your subnet has enough IPs for all nodes, surge nodes, and pods. The formula is `Total IPs = (Number of nodes + maxSurge) * (1 + maxPods)`.
- Reclaim unused IPs or expand the subnet (for example, from /24 to /22).
- Lower `maxSurge` if subnet expansion isn't possible.

    ```azurecli-interactive
    az aks nodepool update \
      --resource-group <resource-group-name> \
      --cluster-name <cluster-name> \
      --name <node-pool-name> \
      --max-surge 10%
    ```

- Monitor IP usage with Azure Monitor or custom alerts.
- Reduce `maxPods` per node, clean up orphaned load balancer IPs, and plan subnet sizing for high-scale clusters.

## Frequently asked questions

### Should I use AKS Automatic or AKS Standard for production upgrades?

For most production workloads, use AKS Automatic. It's designed as the production-ready default with managed upgrade behavior and built-in guardrails.

Use AKS Standard when you need advanced manual control over upgrade sequencing, infrastructure choices, or node pool operations.

### Can I use open-source tools for validation?

Yes. Many open-source tools integrate well with AKS upgrade processes:

- [Trivy](https://aquasecurity.github.io/trivy/): Security scanning for container images and Kubernetes configurations.
- [Sonobuoy](https://sonobuoy.io/): Kubernetes conformance testing and cluster validation.
- [kube-bench](https://github.com/aquasecurity/kube-bench): Security benchmark checks against Center for Internet Security standards.
- [Polaris](https://github.com/FairwindsOps/polaris): Validation of Kubernetes best practices.
- [kubectl-neat](https://github.com/itaysk/kubectl-neat): Clean up Kubernetes manifests for validation.

### How do I validate API compatibility before upgrading?

Run deprecation checks by using tools like kubent:

```bash
# Install and run API deprecation scanner
kubectl apply -f https://github.com/doitintl/kube-no-trouble/releases/latest/download/knt-full.yaml

# Check for deprecated APIs in your cluster
kubectl run knt --image=doitintl/knt:latest --rm -it --restart=Never -- \
  -c /kubeconfig -o json > api-deprecation-report.json

# Review findings
cat api-deprecation-report.json | jq '.[] | select(.deprecated==true)'
```

### What makes AKS upgrades different from other Kubernetes platforms?

AKS provides several unique advantages:

- Managed operational paths in AKS Automatic for lower upgrade overhead.
- Native Azure integration with Azure Traffic Manager, Azure Load Balancer, and networking.
- Azure Kubernetes Fleet Manager for coordinated multicluster upgrades.
- Automatic node image patching without manual node management.
- Built-in validation for quota, networking, and credentials.
- Azure support for upgrade-related issues.

## Choose your upgrade path

This article provided you with a technical foundation. Now select your scenario-based path.

### Ready to execute?

| If you have... | Then go to... |
| -------------- | ------------- |
| Production workload and no special customization constraints | [Create an AKS Automatic cluster](https://learn.microsoft.com/en-us/azure/aks/automatic/quick-automatic-managed-network) |
| Production environment with advanced custom upgrade needs| [Production upgrade strategies](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies) |
| Databases or stateful apps | [Stateful workload patterns](https://learn.microsoft.com/en-us/azure/aks/stateful-workload-upgrades) |
| Multiple environments | [Upgrade scenarios hub](https://learn.microsoft.com/en-us/azure/aks/upgrade-scenarios-hub) |
| Basic AKS Standard cluster | [Upgrade an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-cluster) |

### Still deciding?

Use the [upgrade scenarios hub](https://learn.microsoft.com/en-us/azure/aks/upgrade-scenarios-hub) for a guided decision tree that considers your:

- Downtime tolerance
- Environment complexity
- Risk profile
- Timeline constraints

## Final recommendations

- Use [AKS Automatic](https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic) for most production workloads.
- Review [AKS patch and upgrade guidance][upgrade-operators-guide] for best practices and planning tips before you start any upgrade.
- Always check for [API breaking changes](https://aka.ms/aks/breakingchanges) and validate your workload's compatibility with the target Kubernetes version.
- Test upgrade settings (such as `maxSurge`, `maxUnavailable`, and PDBs) in a staging environment to minimize production risk.
- Monitor upgrade events and cluster health throughout the process.

[pdb-spec]: https://kubernetes.io/docs/tasks/run-application/configure-pdb/

[drain-timeout]: https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling#set-node-drain-timeout-value
[soak-time]: https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling#set-node-soak-time-value
[nodepool-upgrade]: https://learn.microsoft.com/en-us/azure/aks/upgrade-node-image
[planned-maintenance]: https://learn.microsoft.com/en-us/azure/aks/planned-maintenance
[specific-nodepool]: https://learn.microsoft.com/en-us/azure/aks/upgrade-node-image#upgrade-a-specific-node-pool
[upgrade-operators-guide]: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/aks-upgrade-practices
