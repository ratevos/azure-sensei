# Endpoint DLP policy scenarios in Microsoft Purview

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-using  
> Microsoft doc last updated: 2026-06-26


This article provides guidance on using Endpoint Data Loss Prevention (DLP) capabilities within Microsoft Purview to help safeguard sensitive information across organizational devices. It focuses on practical, scenario-based approaches for creating and modifying DLP policies, including auditing, alerting, blocking actions, and enforcing controls on how sensitive data is accessed, shared, or transferred. By addressing common administrative use cases, this guidance helps define how policies can be applied across endpoints and integrated services to monitor and regulate user activity effectively.

By applying these scenarios, administrators can reduce data loss risks, support compliance, and gain better visibility into user activity. This scenario-based approach helps strengthen data governance and improves the organization’s overall security posture.

Important

These Endpoint DLP scenarios aren't the official procedures for creating and tuning DLP policies. For general situations, see the following topics:

- [Learn about Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
- [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy)

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Before you begin

### SKU and subscription licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

These scenarios require that you already onboard devices and that they report to Activity explorer. If you didn't onboard devices yet, see [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started).

Important

Before you start, make sure you understand the difference between an unrestricted administrator and an administrative unit restricted administrator. For more information, see [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units).

## Endpoint DLP policy scenarios

The following scenarios show common Endpoint DLP policy configurations you can implement:

- [Create policy to audit activities using a template (audit only mode)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-audit-activities)
- [Create policy to manage printer access using authorization groups](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-manage-printer-access)
- [Create policy to detect and alert on U.S. PII data exposure](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-detect-pii-data-exposure)
- [Help prevent unauthorized sensitive data sharing with block actions and allow overrides](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-unauthorized-data-sharing)
- [Help prevent risky user activity by monitoring or restricting access to sensitive service domains](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-access-to-domains)
- [Help prevent leakage of sensitive content by restricting paste actions into browsers](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-paste-in-browsers)
- [Help prevent exposure of sensitive files by configuring auto-quarantine for OneDrive sync](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-auto-quarantine-for-onedrive)
- [Help prevent sharing of sensitive items with unauthorized cloud apps and services](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-unauthorized-cloud-apps-services)
- [Create policy to manage file activities by implementing network exceptions](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-file-activities-using-network-exceptions)
