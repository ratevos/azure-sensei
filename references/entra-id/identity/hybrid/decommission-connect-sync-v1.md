# Decommissioning Azure AD Connect V1

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/decommission-connect-sync-v1  
> Microsoft doc last updated: 04/09/2025


The one-year advanced notice of Azure AD Connect V1's retirement was announced in August 2021. As of August 31, 2022, all V1 versions went out of support and were subject to stop working unexpectedly at any point.

On **October 1, 2023**, Microsoft Entra cloud services stopped accepting connections from Azure AD Connect V1 servers, and identities no longer synchronize.

If you're still using Azure AD Connect V1, you must take action immediately.

##  Migrate to cloud sync
Before moving to Microsoft Entra Connect Sync, you should see if cloud sync is right for you instead. Cloud sync uses a light-weight provisioning agent and is fully configurable through the portal. To choose the best sync tool for your situation, use the [supported sync scenarios comparison.](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)

Based on your environment and needs, you may qualify for moving to cloud sync. For a comparison of cloud sync and connect sync, see [Comparison between cloud sync and connect sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide#comparison-between-microsoft-entra-connect-and-cloud-sync). To learn more, read [What is cloud sync?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync) and [What is the provisioning agent?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-provisioning-agent)

## Migrating to Microsoft Entra Connect V2
If you aren't yet eligible to move to cloud sync, use this table for more information on migrating to V2.

|Title|Description|
|-----|-----|
|[Information on deprecation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/deprecated-azure-ad-connect)|Information on Azure AD Connect V1 deprecation|
|[What is Microsoft Entra Connect V2?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect-v2)|Information on the latest version of Microsoft Entra Connect|
|[Upgrading from a previous version](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-upgrade-previous-version)|Information on moving from one version of Microsoft Entra Connect to another|

## Frequently asked questions

## Next steps

- [What is Microsoft Entra Connect V2?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect-v2)
- [Azure AD cloud sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync)
- [Microsoft Entra Connect version history](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history)
