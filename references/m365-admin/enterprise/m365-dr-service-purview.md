# Data Residency for Microsoft Purview

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-purview  
> Microsoft doc last updated: 05/09/2025


This article lists the Data Residency commitments (available with the _Advanced Data Residency_ add-on) for supported Microsoft Purview services and solutions.

The required conditions for the related commitments for the following services are:

1. _Tenant_ has a sign-up country/region included in _Local Region Geography_ or _Future Local Region Geography_.
1. _Tenant_ has a valid _Advanced Data Residency_ subscription for all users in the _Tenant_.
1. The Purview service Customer Data is provisioned in _Local Region Geography_ or _Future Local Region Geography_.

## Migration

Customer Data supporting Purview services is closely aligned with the Exchange Online and SharePoint services, and the bulk of the data migrated, if required to fulfill the data residency commitments for the Purview services, will be handled by those services. In the cases where supporting Customer Data is maintained in an Azure Service, for example, the migration of that data is tied to the migration of the underlying Exchange Online/SharePoint data.

## How can I determine Customer Data location?

We are in the process of updating the data location for eligible Purview services in the Microsoft 365 admin center. When this change is complete, you will be able to see the _Current Geography_ and _Committed Geography_ location for eligible Purview services data within the _Data Location Card_ by navigating to **Admin** > **Settings** > **Org settings** > **Organization profile** > **Data location**. Until that change is visible, you can view the Exchange Online data location information in order to understand where your committed data is stored for this service.

## Advanced Data Residency Eligible Services

###### **Table 1: Eligible Microsoft Purview Services for _Advanced Data Residency_**

| Solution Area | Services | Components |
|:-----|:-----|:----- |
| Risk & Compliance |Audit (Standard) |See [Audit (Standard)](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#audit-standard) for specific commitments.|
| Risk & Compliance |Audit (Premium) |See [Audit (Premium)](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#audit-premium) for specific commitments.|
| Risk & Compliance |Data Lifecycle Management (DLM) |See [Data Lifecycle Management (DLM)](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#data-lifecycle-management-dlm) for specific commitments.|
| Data Security |Data Loss Prevention (DLP) |See [Data Loss Prevention (DLP)](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#data-loss-prevention-dlp) for specific commitments.|
| Data Security |Information Barriers |See [Information Barriers](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#information-barriers) for specific commitments.|
| Data Security |Information Protection (MIP) |See [Information Protection (MIP)](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#information-protection-mip) for specific commitments.|

> [!NOTE]
> The Microsoft Purview services list includes all services covered as part of the _Advanced Data Residency_ commitment as of February 2026. Additional Microsoft Purview services aren't currently supported.

### Risk & Compliance - Audit (Standard)

#### Summary

Service documentation: [Microsoft Purview auditing solutions](https://learn.microsoft.com/en-us/microsoft-365/compliance/auditing-solutions-overview)

Capability summary: Microsoft Purview Audit (Standard) provides you with the ability to log and search your data for audit activities and power your forensics, IT, and compliance efforts and legal investigations.

#### Data Residency commitments available

Commitment:

Refer to the [ADR Commitments page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#audit-standard) for the specific Customer Data at rest commitment for Audit (Standard).

### Risk & Compliance - Audit (Premium)

#### Summary

Service documentation: [Microsoft Purview auditing solutions](https://learn.microsoft.com/en-us/microsoft-365/compliance/auditing-solutions-overview)

Capability summary: Microsoft Purview Audit (Premium) builds on the capabilities of Audit (Standard) by providing audit log retention policies, longer retention of audit records, capability to identify high-value crucial events, and higher bandwidth access to the Office 365 Management Activity API.

#### Data Residency commitments available

Commitment:

Refer to the [ADR Commitments page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#audit-premium) for the specific Customer Data at rest commitment for Audit (Premium).

### Risk & Compliance - Data Lifecycle Management (DLM)

#### Summary

_ADR_ applies to the following services within Purview Data lifecycle management:

#### Data Retention:

- Manual retention labels
- Basic org-wide or location-wide retention policies
- Rules-based automatic retention policies
- Machine Learning-based retention
- Teams message retention policies

Service documentation: [Learn about retention policies & labels](https://learn.microsoft.com/en-us/microsoft-365/compliance/retention)

For more detailed information about how retention settings work for different workloads, see the following articles:

- [Learn about retention for Exchange](https://learn.microsoft.com/en-us/microsoft-365/compliance/retention-policies-exchange)
- [Learn about retention for SharePoint and OneDrive](https://learn.microsoft.com/en-us/microsoft-365/compliance/retention-policies-sharepoint)
- [Learn about retention for Microsoft Teams](https://learn.microsoft.com/en-us/microsoft-365/compliance/retention-policies-teams)

Capability summary: Lets you retain or delete content with policy management for email, documents, and Teams.

#### Data Residency commitments available

Commitment:

Refer to the [ADR Commitments page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#data-retention) for the specific Customer Data at rest commitment for Data Retention.

#### Records Management:

Service documentation: [Learn about Microsoft Purview Records Management](https://learn.microsoft.com/en-us/microsoft-365/compliance/records-management)

Capability summary: Organizations of all types require a records-management solution to manage regulatory, legal, and business-critical records across their corporate data. Records management for Microsoft Purview helps an organization manage their legal obligations, provides the ability to demonstrate compliance with regulations, and increases efficiency with regular disposition of items that are no longer required to be retained, no longer of value, or no longer required for business purposes.

#### Data Residency commitments available

Commitment:

Refer to the [ADR Commitments page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#records-management) for the specific Customer Data at rest commitment for Records Management.

### Data Security - Data Loss Prevention (DLP)

#### Summary

_ADR_ applies to the following services within Purview Information Protection, Data Loss Prevention (DLP):

- Office 365 Data Loss Prevention (DLP) for emails and files
- DLP for Teams chat
- DLP for Microsoft 365 Copilot

Service documentation: [Learn about data loss prevention](https://learn.microsoft.com/en-us/microsoft-365/compliance/dlp-learn-about-dlp)

Capability summary:

Organizations have sensitive information under their control such as financial data, proprietary data, credit card numbers, health records, or social security numbers. To help protect this sensitive data and reduce risk, they need a way to prevent their users from inappropriately sharing it with people who shouldn't have it. This practice is called data loss prevention (DLP).

In Microsoft Purview, you implement data loss prevention by defining and applying DLP policies. With a DLP policy, you can identify, monitor, and automatically protect sensitive items across:

- Microsoft 365 services such as Teams, Exchange, SharePoint, OneDrive, and Microsoft 365 Copilot
- Office applications such as Word, Excel, and PowerPoint
- Windows 10, Windows 11, and macOS (Catalina 10.15 and higher) endpoints
- non-Microsoft cloud apps
- on-premises file shares and on-premises SharePoint.

DLP detects sensitive items by using deep content analysis, not by just a simple text scan. Content is analyzed for primary data matches to keywords, by the evaluation of regular expressions, by internal function validation, and by secondary data matches that are in proximity to the primary data match. Beyond that DLP also uses machine learning algorithms and other methods to detect content that matches your DLP policies.

#### Data Residency commitments available

Commitment:

Refer to the [ADR Commitments page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#data-loss-prevention-dlp) for the specific Customer Data at rest commitment for Data Loss Prevention (DLP).

### Data Security - Information Barriers

#### Summary

Service documentation: [Learn about information barriers](https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers)

Capability summary: Microsoft Purview Information Barriers (IB) is a compliance solution that allows you to restrict two-way communication and collaboration between groups and users in Microsoft Teams, SharePoint, and OneDrive. Often used in highly regulated industries, IB can help to avoid conflicts of interest and safeguard internal information between users and organizational areas.

#### Data Residency commitments available

Commitment:

Refer to the [ADR Commitments page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#information-barriers) for the specific Customer Data at rest commitment for Information Barriers.

### Data Security - Information Protection (MIP)

#### Summary

_ADR_ applies to the following services within Purview Information Protection:

#### Office Message Encryption (OME):

- Basic Office Message Encryption
- Advanced Office Message Encryption

Service documentation: [Office 365 Message Encryption - Microsoft Purview](https://learn.microsoft.com/en-us/microsoft-365/compliance/ome)

Capability summary: With Office 365 Message Encryption, your organization can send and receive encrypted email messages between people inside and outside your organization. Office 365 Message Encryption works with Outlook.com, Yahoo!, Gmail, and other email services. Email message encryption helps to ensure that only intended recipients can view message content.

#### Data Residency commitments available

Commitment:

Refer to the [ADR Commitments page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#office-message-encryption-ome) for the specific Customer Data at rest commitment for Office Message Encryption.

#### Sensitivity Labels:

- Manual, default, and mandatory sensitivity labeling in Office 365
- Automatic sensitivity labeling in Office 365 apps
- Automatic sensitivity labels in Exchange, SharePoint, and OneDrive
- Sensitivity labels based on advanced classification
- Sensitivity labeling for containers in Office 365

Service documentation:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/microsoft-365/compliance/sensitivity-labels)
- [Get started with Activity explorer](https://learn.microsoft.com/en-us/microsoft-365/compliance/data-classification-activity-explorer)

Capability summary: Sensitivity labels from Microsoft Purview Information Protection let you classify and protect your organization's data, while making sure that user productivity and their ability to collaborate isn't hindered.

#### Data Residency commitments available

Commitment:

Refer to the [ADR Commitments page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#sensitivity-labels) for the specific Customer Data at rest commitment for Sensitivity Labels.
