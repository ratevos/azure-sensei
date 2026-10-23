# Advanced Data Residency Commitments

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments  
> Microsoft doc last updated: 1/30/2026


> [!NOTE]
> If you have purchased a _Multi-Geo_ subscription, then Microsoft will store certain customer data at rest in more than one _Geography_ based on your configuration even if you have purchased the _Microsoft 365 Advanced Data Residency add-on ("ADR")_.

Microsoft makes commitments to store certain in scope customer data at rest in the applicable _Local Region Geography_ for [eligible customers](https://learn.microsoft.com/en-us/microsoft-365/enterprise/advanced-data-residency#eligibility) that purchase _ADR_. The commitments are specified as follows.

## Exchange Online

The following customer data is stored at rest in the _Local Region Geography_:

- Exchange Online mailbox content (e-mail body, calendar entries, and the content of e-mail attachments stored in the related _Local Region Geography_).

## Microsoft 365 Copilot and Copilot Chat

The following customer data is stored at rest in the _Local Region Geography_:

- Any stored content of interactions with Microsoft 365 Copilot and Microsoft 365 Copilot Chat to the extent not included in the preceding commitments.

## Microsoft 365 web apps (formerly known as "Office for the Web")

The following customer data is stored at rest in the _Local Region Geography_:

- Microsoft 365 web apps stores files on a storage host that has its applicable promises to _Local Region Geography_.

## Microsoft Defender for Office P1

The following customer data is stored at rest in the _Local Region Geography_:

- Microsoft Defender for Office 365 P1 doesn't store any customer data within its service.
- [Built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP))](https://learn.microsoft.com/en-us/defender-office-365/eop-about): The following customer data is stored at rest in the _Local Region Geography_: Service configuration data and policies, quarantined email and attachments, junk email, grading analysis, blocklists (url, tenant, user), spam domains, reports, and alerts.

## Microsoft Purview

### Audit (Standard)

The following customer data is stored at rest in the _Local Region Geography_:

- Service configuration data
- Audited Activities
- Audit Records
- Audit log query permissions

### Audit (Premium)

The following customer data is stored at rest in the _Local Region Geography_:

- All data covered under Audit (Standard)
- Configuration and Customer Data related to high-value crucial events

### Data lifecycle Management (DLM)

#### Data Retention

The following customer data is stored at rest in the _Local Region Geography_:

- Retention policy settings and retention label definitions
- Customer Data stored in original locations for the following services:
  - Exchange email
  - SharePoint site
  - OneDrive accounts
  - Microsoft 365 Groups
  - Exchange public folders
  - Microsoft Teams chats and channel messages
  - Viva Engage user and community messages
- Customer Data copied and stored in Exchange Online hidden mailboxes
  - Teams channel messages
  - Teams chats
  - Teams private channel messages
  - Viva Engage user and community messages
  - SharePoint, OneDrive, Exchange Online and Microsoft Teams follow the data residency commitments for those services. Refer to [Exchange Online](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-exo), [SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-spo), and [Microsoft Teams](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-teams) workload data residency pages for more details.
- Training classifiers
- Disposition data
- Mappings between retention labels and Data Loss Prevention (DLP) policies

#### Records Management

The following customer data is stored at rest in the _Local Region Geography_:

- Record retention label definitions
- File plan definitions
- Event-based retention policy settings
- Disposition review records and records of deletion

### Data Loss Prevention (DLP)

The following customer data is stored at rest in the _Local Region Geography_:

- DLP Admin Configuration
- DLP policies in Microsoft Purview portal
- DLP monitored activities
- Violation history
- Activity Explorer and Microsoft 365 unified audit logs
- Quarantine storage
- DLP Alerts and DLP Alert management dashboard

### Information Barriers

The following customer data is stored at rest in the _Local Region Geography_:

- Policy settings
- Risk indicators
- Segments Configuration

### Information Protection (MIP)

#### Sensitivity labels

The following customer data is stored at rest in the _Local Region Geography_:

- Label configuration
- Labels definition
- Label policies
- Custom help page
- Activity Explorer and Microsoft 365 unified audit logs
- Label change justification records

#### Office Message Encryption (OME)

The following customer data is stored at rest in the _Local Region Geography_:

- Encryption policies
- Admin settings
- Encrypted messages

#### Classifiers

- Sensitive information types, including Enhanced Data Match (EDM) and Trainable Classifiers, configured by customers

> [!NOTE]
> The Microsoft Purview services list includes all services covered as part of the _Advanced Data Residency_ commitment as of February 2026. Additional Microsoft Purview services aren't currently supported.

## Microsoft Teams

The following customer data is stored at rest in the _Local Region Geography_:

- Microsoft Teams chat messages (including private messages, channel messages, meeting messages and images used in chats), and, for customers using Microsoft Stream (on SharePoint), meeting recordings

## SharePoint/OneDrive

The following customer data is stored at rest in the _Local Region Geography_:

- SharePoint site content and the files stored within that site and files uploaded to OneDrive

## Viva Connections

The following customer data is stored in the _Local Region Geography_:

- Viva Connections Dashboard and Feed can have content sourced from SharePoint, Exchange Online and Microsoft Teams. All customer data sourced from these services covered by data residency commitments will be stored in the _Local Region Geography_. Refer to [Exchange Online](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-exo), [SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-spo), and [Microsoft Teams](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-teams) workload data residency pages for more details.
