# Data Residency for Viva Connections

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-service-viva-connections  
> Microsoft doc last updated: 05/10/2025


## Overview

Service documentation: [Overview: Viva Connections](https://learn.microsoft.com/en-us/viva/connections/viva-connections-overview)

Capability Summary: Microsoft Viva Connections is your gateway to a modern employee experience designed to keep everyone engaged and informed. Viva Connections is a customizable app in Microsoft Teams that gives everyone a personalized destination to discover relevant news, conversations, and the tools they need to succeed. Data storage is related to the following Viva Connections Components: Dashboard and feed.

## Data Residency Commitments Available

### Advanced Data Residency add-on

Required Conditions:

1. _Tenant_ has a sign-up country/region included in _Local Region Geography_ or _Expanded Local Region Geography_.
1. _Tenant_ has a valid Advanced Data Residency subscription for all users in the _Tenant_.
1. The Viva Connections subscription customer data is provisioned in _Local Region Geography_ or _Expanded Local Region Geography_.

**Commitment:**

Refer to the [ADR Commitment page](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-commitments#viva-connections) for the specific customer data at rest commitment for Viva Connections.

### Migration

Data is stored within Exchange Online, SharePoint and Microsoft Teams. Migration processes are handled by the applicable/relevant workloads.

### How can I determine customer data location?

You can find the actual data location in Tenant Admin Center. As a tenant administrator you can find the actual data location, for committed data, by navigating to **Admin -> Settings -> Org Settings -> Organization Profile -> Data Location**.
