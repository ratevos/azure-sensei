# What is the provisioning agent?

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-provisioning-agent  
> Microsoft doc last updated: 04/09/2025


The provisioning agent is the synchronization tool that is used to deliver several features for use with Microsoft Entra ID and is managed from the cloud.

The provisioning agent provides connectivity between Microsoft Entra ID and your on-premises environment.

 These features include:

 - cloud sync
 - on-premises app provisioning

## How it works
The provisioning agent uses SCIM ([System for Cross-domain Identity Management (SCIM) 2.0](https://techcommunity.microsoft.com/t5/identity-standards-blog/provisioning-with-scim-getting-started/ba-p/880010)). The SCIM specification provides a common user schema to help users move into, out of, and around apps. SCIM is becoming the de facto standard for provisioning and, when used in conjunction with federation standards like SAML or OpenID Connect, provides administrators an end-to-end standards-based solution for access management.

## Next steps 

- [What is provisioning?](https://learn.microsoft.com/en-us/entra/identity/hybrid/what-is-provisioning)
- [Install cloud sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-install)
