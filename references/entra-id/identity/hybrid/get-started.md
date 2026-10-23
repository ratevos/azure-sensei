# Get started integrating with Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/get-started  
> Microsoft doc last updated: 10/06/2026


Use this guide to integrate on-premises Active Directory with Microsoft Entra ID. It explains how to choose between Microsoft Entra Cloud Sync and Microsoft Entra Connect Sync and configure synchronization for users, groups, and devices.

First, use [Choose the right sync tool](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios) to select a synchronization tool. Then follow the section for that tool.

## Cloud Sync
Use these tasks to deploy Cloud Sync and integrate Active Directory with Microsoft Entra ID.

|Task|Description|
|-----|-----|
|[Choose the right sync tool](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios) |Use the wizard to determine whether Cloud Sync or Connect Sync is right for you.|
|[Review Cloud Sync prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-prerequisites)|Review the prerequisites before you begin.|
|[Download and install the provisioning agent](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-install)|Download and install the Microsoft Entra provisioning agent. |
|[Configure Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure)|Configure synchronization for your organization.|
|[Configure device sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/device-sync)|Synchronize Active Directory computer objects to Microsoft Entra ID for Microsoft Entra hybrid join.|
|[Verify that users synchronize](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/tutorial-single-forest#verify-users-are-created-and-synchronization-is-occurring)|Confirm that synchronization is working.|

<a name='azure-ad-connect'></a>

## Microsoft Entra Connect
Use these tasks if you're deploying Microsoft Entra Connect to integrate with Active Directory.

|Task|Description|
|-----|-----|
|[Choose the right sync tool](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios) |Use the wizard to determine whether Cloud Sync or Connect Sync is right for you.|
|[Review the Microsoft Entra Connect prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-prerequisites)|Review the necessary prerequisites before getting started.|
|[Review and choose an installation type](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-select-installation)|Determine whether you'll use express or custom installation.|
|[Download Microsoft Entra Connect](https://www.microsoft.com/download/details.aspx?id=47594)|Download Microsoft Entra Connect.|
|[Install and configure Microsoft Entra Connect express settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-express)|If you're using express settings, install and configure Microsoft Entra Connect with express settings.|
|[Install and configure Microsoft Entra Connect custom settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom)|If you're using custom settings, install and configure Microsoft Entra Connect with express settings.|
|[Perform post installation tasks](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-post-installation)|Perform the post installation tasks.|
|[Verify users are synchronizing](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/tutorial-single-forest#verify-users-are-created-and-synchronization-is-occurring)|Make sure it's working.|

## Next steps
- [Common scenarios](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Tools for synchronization](https://learn.microsoft.com/en-us/entra/identity/hybrid/sync-tools)
- [Choosing the right sync tool](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/prerequisites)
