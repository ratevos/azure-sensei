# AKS Regulated Cluster for PCI DSS 4.0.1 - Targeted Risk Analysis

> Source: https://learn.microsoft.com/en-us/azure/aks/pci-targeted-risk-analysis  
> Microsoft doc last updated: 06/25/2025


PCI DSS 4.0.1 introduces targeted risk analysis for certain requirements. This document outlines how to perform and document risk analysis for AKS workloads.

## AKS feature support

AKS provides several features to help you meet PCI DSS 4.0.1 targeted risk analysis requirements:

- **Azure Policy**: Supports risk-based policy enforcement and can help automate risk analysis for AKS resources.
- **Microsoft Defender for Cloud**: Provides risk assessment, security recommendations, and compliance tracking for AKS clusters.
- **Azure Monitor**: Enables tracking of risk indicators and audit events for ongoing risk analysis.

## Your responsibilities

- Identify which PCI DSS requirements in your AKS environment allow for targeted risk analysis (e.g., key rotation, access reviews).
- Document the risk analysis process, findings, and mitigation steps for each applicable requirement.
- Use Azure Policy and Defender for Cloud to automate risk identification and mitigation where possible.
- Regularly review and update risk analysis documentation as the AKS environment and threat landscape evolve.

## Key steps

- Identify requirements that allow for targeted risk analysis.
- Document the risk analysis process, findings, and mitigation steps.
- Review and update risk analysis regularly.

## Example template

| Requirement | Risk Identified | Mitigation | Review Date |
|-------------|----------------|-----------|-------------|
| Key rotation frequency | Key compromise | Automated rotation | 2025-06-01 |

## Integrated AKS security context

You should implement targeted risk analysis as part of a broader security strategy that includes:

- [Security policies](https://learn.microsoft.com/en-us/azure/aks/pci-policy) for policy and governance.
- [Identity and access management](https://learn.microsoft.com/en-us/azure/aks/pci-identity) for identity and access management.
- [Monitoring and logging](https://learn.microsoft.com/en-us/azure/aks/pci-monitor) for monitoring and alerting.

For the latest AKS security features, see the [Azure Kubernetes Service (AKS) documentation](https://learn.microsoft.com/en-us/azure/aks/).

## Next steps

Implement comprehensive security awareness training for all personnel with access to the cardholder data environment.

> [Implement security awareness training](https://learn.microsoft.com/en-us/azure/aks/pci-security-awareness-training)

## Related resources

For more information, review the official [PCI DSS 4.0.1 documentation](https://www.pcisecuritystandards.org/).
