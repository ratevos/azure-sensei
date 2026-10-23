# Data Residency for Microsoft Defender for Office P1

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-mdo-p1  
> Microsoft doc last updated: 01/30/2026


## Overview

Service documentation: [Office 365 Security including Microsoft Defender for Office 365 and the built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP))](https://learn.microsoft.com/en-us/defender-office-365/mdo-about)

Capability Summary: Protects email and collaboration from zero-day malware, phish, and business email compromise. Microsoft Defender for Office 365 Plan 1 builds on [the built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP))](https://learn.microsoft.com/en-us/defender-office-365/eop-about).

## Data Residency commitments available

### Advanced Data Residency add-on

Required Conditions:

1. _Tenant_ has a sign-up country included in _Local Region Geography_ or _Expanded Local Region Geography_.
1. _Tenant_ has a valid Advanced Data Residency subscription for all users in the _Tenant_
1. The MDO P1 subscription customer data is provisioned in _Local Region Geography_ or _Expanded Local Region Geography_.

**Commitment:**

Refer to the [ADR Commitment page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#microsoft-defender-for-office-p1) for the specific customer data at rest commitment for Microsoft Defender for Office P1.

Other Information

In addition, processing of data that is required to analyze threats and inspect suspicious emails, documents, messages, and links is done in a sandbox environment and performed within the _Local Region Geography_ or _Expanded Local Region_.

<a name='exchange-online-protection'></a>

## Built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP))

### Overview

Service documentation: [Overview of the built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP))](https://learn.microsoft.com/en-us/defender-office-365/eop-about)

Capability summary: Built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP)) is the cloud-based filtering service that protects your organization against spam, malware, and other email threats.

### Data Residency commitments available

#### Advanced Data Residency add-on

Required Conditions:

1. _Tenant_ has a sign-up country included in _Local Region Geography_ or _Expanded Local Region Geography_.
1. _Tenant_ has a valid Advanced Data Residency subscription for all users in the _Tenant_
1. Customer data for the built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP)) is provisioned in _Local Region Geography_ or _Expanded Local Region Geography_

**Commitment:**

Refer to the [Advanced Data Residency Commitment](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments) page for the specific customer data at rest commitment for the built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP)).

## Migration

Customer data for the built-in security features for all cloud mailboxes (formerly Exchange Online Protection (EOP)) migrates after ADR migration is initiated. Microsoft Defender for Office 365 Plan 1 doesn't have customer data to migrate.

## How can I determine customer data location?

You can find the actual data location in Tenant Admin Center. As a tenant administrator you can find the actual data location, for committed data, by navigating to **Admin -> Settings -> Org Settings -> Organization Profile -> Data Location**.
