# AKS Regulated Cluster for PCI DSS 4.0.1 - Requirement Mapping Matrix

> Source: https://learn.microsoft.com/en-us/azure/aks/pci-requirement-mapping-matrix  
> Microsoft doc last updated: 06/25/2025


This document provides a mapping of AKS controls and documentation to PCI DSS 4.0.1 requirements, including customized approaches where applicable.

## AKS PCI DSS 4.0.1 requirement mapping matrix

| PCI DSS 4.0.1 requirement | AKS control | Customized approach |
|--------------------------|---------------------|--------------------|
| MFA for admin access     | [Enhanced MFA implementation](https://learn.microsoft.com/en-us/azure/aks/pci-enhanced-mfa-implementation) | Yes (if using Azure AD Conditional Access) |
| Continuous monitoring    | [Continuous security and monitoring](https://learn.microsoft.com/en-us/azure/aks/pci-continuous-security-monitoring) | No |
| Key management           | [Cryptography and key management](https://learn.microsoft.com/en-us/azure/aks/pci-cryptography-key-management) | No |
| Third-party management   | [Third-party and supply chain security](https://learn.microsoft.com/en-us/azure/aks/pci-third-party-supply-chain-security) | No |
| Security awareness       | [Security awareness and training](https://learn.microsoft.com/en-us/azure/aks/pci-security-awareness-training) | No |

## Integrated AKS security context

You should leverage the requirement mapping matrix as part of a broader security strategy that includes:

- [Security policies](https://learn.microsoft.com/en-us/azure/aks/pci-policy) for policy and governance.
- [Identity and access management](https://learn.microsoft.com/en-us/azure/aks/pci-identity) for identity and access management.
- [Monitoring and logging](https://learn.microsoft.com/en-us/azure/aks/pci-monitor) for monitoring and alerting.

## Next steps

Review the complete summary of PCI DSS 4.0.1 implementation on AKS and next steps for compliance.

> [Review summary and next steps](https://learn.microsoft.com/en-us/azure/aks/pci-summary)

## Related resources

For more information, review the official [PCI DSS 4.0.1 documentation](https://www.pcisecuritystandards.org/).

For the latest AKS security features, see the [Azure Kubernetes Service (AKS) documentation](https://learn.microsoft.com/en-us/azure/aks/).
