# Tools used for synchronization

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/sync-tools  
> Microsoft doc last updated: 10/06/2026

This article compares Microsoft Entra Cloud Sync, Connect Sync, Microsoft Identity Manager (MIM), and the ECMA host connector. Use the comparison to choose a tool for synchronizing identities or provisioning users to on-premises applications.

## List of tools 

- **Cloud Sync and the provisioning agent** - Microsoft Entra Cloud Sync synchronizes users, groups, and contacts from Active Directory to Microsoft Entra ID. When device sync is enabled, it can also synchronize computer objects for Microsoft Entra hybrid join. Cloud Sync uses the lightweight provisioning agent and is configurable through the Microsoft Entra admin center. For more information, see [What is Microsoft Entra Cloud Sync?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync), [What is the provisioning agent?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-provisioning-agent), and [Configure device sync with Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/device-sync).

- **Connect Sync** - Microsoft Entra Connect is an on-premises application for synchronizing identities with Microsoft Entra ID. For more information, see [What is Microsoft Entra Connect?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect-v2).

- **Microsoft Identity Manager with the Graph connector** - Microsoft's on-premises identity and access management solution that provides advanced inter-directory provisioning to achieve hybrid identity environments for Active Directory, Microsoft Entra ID, and other directories. For more information, see [Microsoft Identity Manager](https://learn.microsoft.com/en-us/microsoft-identity-manager/microsoft-identity-manager-2016). MIM is slowly being deprecated and should only be used in advanced scenarios. For more information, see [Deprecated Features and planning for the future](https://learn.microsoft.com/en-us/microsoft-identity-manager/microsoft-identity-manager-2016-deprecated-features)

- **ECMA Host connector** - The ECMA host works with the provisioning agent to provision and synchronize users from the cloud into on-premises applications such as SQL and LDAP. For more information, see [Microsoft Entra on-premises application identity provisioning architecture](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/on-premises-application-provisioning-architecture) and [What is the provisioning agent?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-provisioning-agent)

## Selecting the right tool
These tools support different hybrid identity scenarios. Compare their capabilities in the [supported sync scenarios table](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios#supported-sync-scenarios), then use the [sync tool selection wizard](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios) to choose a tool.

## Next steps
- [Common scenarios](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Choosing the right sync tool](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Steps to start](https://learn.microsoft.com/en-us/entra/identity/hybrid/get-started)
- [Prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/prerequisites)
