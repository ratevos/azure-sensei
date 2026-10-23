# AKS Upgrade Scenarios: Choose Your Path

> Source: https://learn.microsoft.com/en-us/azure/aks/upgrade-scenarios-hub  
> Microsoft doc last updated: 07/09/2025


Upgrading Azure Kubernetes Service (AKS) clusters safely requires the right strategy for your specific situation. Use this hub to quickly identify your scenario and get targeted guidance.

## What this article covers

This decision hub helps you choose the right AKS upgrade approach based on:

- A quick scenario finder with time constraints and priorities.
- Emergency upgrade paths for critical security responses.
- A strategy matrix that compares downtime tolerance and complexity.
- Role-based guidance for site reliability engineers, database administrators, developers, and security teams.
- Decision trees for complex multi-environment setups.

This hub is best for first-time upgraders, teams that need to evaluate options, and complex environments that require tailored approaches.

For more information, see these related articles:

- To upgrade your production AKS clusters, see [AKS production upgrade strategies](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies).
- To get upgrade patterns for AKS clusters with stateful workloads, see [Stateful workload upgrade patterns](https://learn.microsoft.com/en-us/azure/aks/stateful-workload-upgrades).
- To check for and apply basic upgrades to your AKS cluster, see [Upgrade an Azure Kubernetes Service (AKS) cluster](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-upgrade-cluster).

---

## Quick scenario finder

What's your primary concern? Select your answer from the following table.

| My priority | Time constraint | Go to |
|-------------|----------------|-------|
| Zero production downtime | Upgrade needed within hours | [Production upgrade strategies](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies#scenario-1-minimal-downtime-production-upgrades) |
| Multi-environment safety | Planned windows | [Staged fleet upgrades](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies#scenario-2-stage-upgrades-across-environments) |
| New Kubernetes version risk | Safety-first approach | [Safe version intake](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies#scenario-3-safe-kubernetes-version-intake) |
| Security compliance | Response required for common vulnerabilities and exposures  | [Fast security patching](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies#scenario-4-fastest-security-patch-deployment) |
| Database/stateful apps | Running databases | [Stateful workload patterns](https://learn.microsoft.com/en-us/azure/aks/stateful-workload-upgrades) |
| Architecture planning | Design for upgrades | [Resilient architecture](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies#scenario-5-application-architecture-for-resilient-upgrades) |

## Emergency upgrade (30-90 minutes)

If you need a critical security patch now, select a link for instructions:

- **Immediate action:** [Automated security patching](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies#scenario-4-fastest-security-patch-deployment)
- **With stateful workloads:** [Database safety patterns](https://learn.microsoft.com/en-us/azure/aks/stateful-workload-upgrades#emergency-upgrade-checklist)
- **Rollback ready:** [Quick recovery guide](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies#emergency-rollback-procedures)

## Upgrade strategy matrix

Find your ideal approach based on business constraints.

| Downtime tolerance | Environment | Best strategy | Time investment |
|-------------------|-------------|---------------|----------------|
| <2 minutes | Production | Blue-green deployment | 45-60 min |
| <30 seconds | Stateful apps | Ferris wheel pattern | 60-90 min |
| Planned window | Multi-environment | Staged fleet upgrade | 2-4 hours |
| Zero tolerance | Mission-critical | Application architecture | Ongoing |

## Key upgrade topics

### Core upgrade mechanics

- [Basic cluster upgrade process](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-upgrade-cluster)
- [Node pool upgrade strategies](https://learn.microsoft.com/en-us/azure/aks/upgrade-aks-node-pools-rolling)
- [Auto-upgrade configuration](https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-cluster)

### Production-ready strategies

- [Scenario-based production upgrades](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies)
- [Stateful workload upgrade patterns](https://learn.microsoft.com/en-us/azure/aks/stateful-workload-upgrades)
- [Cross-environment upgrade staging](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies#scenario-2-stage-upgrades-across-environments)

### Advanced topics

- [Long-term support strategies](https://learn.microsoft.com/en-us/azure/aks/long-term-support)
- [Maintenance window planning](https://learn.microsoft.com/en-us/azure/aks/planned-maintenance)
- [Upgrade monitoring and alerts](https://learn.microsoft.com/en-us/azure/aks/aks-communication-manager)

## Quick wins (5-15 minutes)

Immediate actions that you can take:

- **Pre-upgrade health check:** Run [cluster diagnostics](https://learn.microsoft.com/en-us/azure/aks/aks-diagnostics).
- **Backup validation:** Verify your [disaster recovery](https://learn.microsoft.com/en-us/azure/aks/reliability-multi-region-deployment-models) setup.
- **Monitoring setup:** Enable [upgrade notifications](https://learn.microsoft.com/en-us/azure/aks/aks-communication-manager).
- **Team preparation:** Review [support policies](https://learn.microsoft.com/en-us/azure/aks/support-policies).

## Learning path

If you're new to AKS upgrades, follow this learning sequence:

1. **Learn:** Learn about [Kubernetes concepts](https://learn.microsoft.com/en-us/azure/aks/core-aks-concepts) and read the [Upgrade overview](https://learn.microsoft.com/en-us/azure/aks/upgrade-conceptual).
1. **Practice:** Take the tutorial on how to [upgrade an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-upgrade-cluster).
1. **Production:** Use the [production strategies](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies).
1. **Optimize:** Find out about [stateful patterns](https://learn.microsoft.com/en-us/azure/aks/stateful-workload-upgrades).

## Pro tips

- **Always test in nonproduction first:** Perform tests even for emergency patches.
- **Monitor during upgrades:** Set up [real-time alerts](https://learn.microsoft.com/en-us/azure/aks/aks-communication-manager).
- **Plan for rollback:** Have a tested recovery procedure.
- **Communicate with teams:** Coordinate with app owners during upgrades.

---

## Related content

- For more help, choose your scenario from the preceding options or start with [Production upgrade strategies](https://learn.microsoft.com/en-us/azure/aks/aks-production-upgrade-strategies).
- For more information, see [AKS support options](https://learn.microsoft.com/en-us/azure/aks/aks-support-help) or the [AKS troubleshooting guide](https://learn.microsoft.com/en-us/azure/aks/troubleshooting).
