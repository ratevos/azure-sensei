# Using a deprecated version of Microsoft Entra Connect

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/deprecated-azure-ad-connect  
> Microsoft doc last updated: 10/06/2026


You may have received a notification email that says that your [Microsoft Entra Connect version is deprecated](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect-v2) and no longer supported.  Or, you may have read a portal recommendation about upgrading your Microsoft Entra Connect version. What is next?

> [!IMPORTANT]
> Instead of upgrading to the latest version of Microsoft Entra Connect, see if cloud sync is right for you. 
> For more information, evaluate your options using the [supported sync scenarios comparison](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)

Using a deprecated and unsupported version of Microsoft Entra Connect isn't recommended and not supported. Deprecated and unsupported versions of Microsoft Entra Connect may **unexpectedly stop working**.  In these instances, you may need to install the latest version of Microsoft Entra Connect as your only remedy to restore your sync process. 

We regularly update Microsoft Entra Connect with [newer versions](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history). The new versions have bug fixes, performance improvements, new functionality, and security fixes, so it's important to stay up to date.

## How to replace your deprecated version

If you're still using a deprecated and unsupported version of Microsoft Entra Connect, here's what you should do:

 1. Check which version to install. Many organizations can use [Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/azure/active-directory/cloud-sync/what-is-cloud-sync) instead of Microsoft Entra Connect. Cloud Sync synchronizes users, groups, and contacts from Active Directory to Microsoft Entra ID. When device sync is enabled, it can also synchronize computer objects for Microsoft Entra hybrid join. For device setup, see [Configure device sync with Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/device-sync). Cloud Sync uses a lightweight agent, is managed from the cloud, and updates automatically.

 2. If you're not yet eligible for Microsoft Entra Cloud Sync, [download Microsoft Entra Connect](https://www.microsoft.com/download/details.aspx?id=47594) and install the latest version. For more information, see [Upgrade Microsoft Entra Connect from a previous version](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-upgrade-previous-version).

## Next steps

- [What is Microsoft Entra Connect V2?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect-v2)
- [Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/azure/active-directory/cloud-sync/what-is-cloud-sync)
- [Microsoft Entra Connect version history](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history)
