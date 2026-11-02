# Microsoft Entra Global Secure Access operations guide

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/overview-operations  
> Microsoft doc last updated: 05/04/2026


This operations guide suite provides prescriptive, post-deployment procedures for running Microsoft Entra Global Secure Access in an enterprise environment. The guides cover day-to-day alerting, health checks, integration, automation, and metrics—focusing on operational tasks that keep the service reliable, secure, and performant.

## Who this guide is for

- **IT administrators and network security engineers** responsible for Global Secure Access configuration and maintenance
- **Platform operations and monitoring engineers** who manage health checks, automation, and dashboards
- **Security leadership** reviewing operational metrics and service value

This guide assumes Global Secure Access is already deployed and configured. For deployment and initial setup, see the [Global Secure Access deployment guide](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-intro). For broader identity-layer security investigations and incident response, see the [Microsoft Entra Security Operations Guide](https://aka.ms/AzureADSecOps).

## Overview

The operational practices in these guides align with the Information Technology Infrastructure Library (ITIL) service management processes and the National Institute of Standards and Technology (NIST) Cybersecurity Framework. Rather than teaching these frameworks, the guides apply their principles directly: alert-first monitoring (NIST Detect), structured change management (ITIL), configuration backup and failover testing (NIST Recover), and continuous improvement through metrics-driven reviews.

The guide suite groups content by Global Secure Access capability, plus a shared common guide for cross-cutting topics.

### Shared operations

| Guide | What it covers |
| --- | --- |
| [Common operations](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operations-common) | RACI matrix (responsible, accountable, consulted, informed) for roles and responsibilities, change management process, metrics and reporting framework, continuous improvement |
| [Security operations for network access](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-security-operations) | Security monitoring, detection patterns, Sentinel analytics rules, and cross-signal investigation guidance for Global Secure Access |
| [PowerShell samples](https://learn.microsoft.com/en-us/entra/global-secure-access/powershell-samples) | Automation samples for operations monitoring, configuration backup compliance, role assignment reviews, alert noise analysis, and recovery |

### Capability-specific operations

Each capability guide follows a consistent structure: Alerting and monitoring, Maintenance and health checks, Integration and automation, Operational metrics, and Troubleshooting quick reference.

| Guide | What it covers |
| --- | --- |
| [Private Access operations](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operate-private-access) | Connector health, application segment management, ZTNA-specific alerting, Graph API automation for connector and app management |
| [Internet Access operations](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operate-internet-access) | Web filtering policy management, Transport Layer Security (TLS) inspection, URL categorization, threat blocking metrics |
| [Remote Networks operations](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operate-remote-networks) | GRE/IPsec tunnel monitoring, branch site capacity management, customer-premises equipment (CPE) device health, tunnel failover testing |
| [Microsoft Traffic operations](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operate-microsoft-traffic) | Microsoft 365 traffic profile management, compliant network enforcement, Microsoft 365 endpoint coverage, service performance monitoring |

### Templates and checklists

| Template | Purpose |
| --- | --- |
| [Daily health check](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-daily-health-check) | Consolidated daily checklist covering all Global Secure Access capabilities |
| [Private Access health check](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-private-access-health-check) | Capability-specific checklist for Private Access connectors and application segments |
| [Change request template](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-change-request-template) | Structured template for Global Secure Access configuration change requests |
| [Communication plan template](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-communication-plan) | Template for communicating planned changes to stakeholders |

## Getting started with operations

If you completed deployment, follow this sequence:

1. **Establish your team**—Assign roles using the [RACI matrix](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operations-common#raci-matrix). Ensure at least two people cover each role.
2. **Configure alerting**—Set up the critical alerts listed in the [Security operations for network access](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-security-operations) guide and each capability guide: [Private Access](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operate-private-access#alerting-and-monitoring), [Internet Access](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operate-internet-access#alerting-and-monitoring), [Remote Networks](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operate-remote-networks#alerting-and-monitoring), and [Microsoft Traffic](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-operate-microsoft-traffic#alerting-and-monitoring). Don't rely on dashboards for issue detection.
3. **Establish baselines**—Collect a 30-day performance baseline for traffic volume, latency, and usage. Calibrate alert thresholds against this baseline. Each capability guide includes Kusto Query Language (KQL) queries for baseline establishment.
4. **Set up automation**—Start with configuration backups and alert notifications. Expand to the full automation playbook list over time.
5. **Schedule recurring checks**—Implement the daily, weekly, and monthly checklists from each capability guide.
6. **Begin reporting**—Start with weekly operational team reports. Add monthly management reports after the first month.

## Related content

- [Global Secure Access documentation](https://learn.microsoft.com/en-us/entra/global-secure-access/)
- [Global Secure Access deployment guide](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-intro)
- [Microsoft Entra Security Operations Guide](https://aka.ms/AzureADSecOps)
- [Microsoft Entra what's new](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new)
