# Configure your integration with Active Directory

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/configure  
> Microsoft doc last updated: 10/06/2026


Choose Microsoft Entra Cloud Sync or Microsoft Entra Connect Sync based on your synchronization goals. The tables below link to configuration tasks for each tool.

## Cloud Sync
After you install the Microsoft Entra provisioning agent, configure Cloud Sync in the Microsoft Entra admin center. The following table lists configuration tasks.

|Task|Description|
|-----|-----|
|[Configure a new Cloud Sync installation](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure)|Configure synchronization for your organization.|
|[Configure device sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/device-sync)|Synchronize Active Directory computer objects to Microsoft Entra ID for Microsoft Entra hybrid join.|
|[Scope provisioning to specific users and groups](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure#scope-provisioning-to-specific-users-and-groups)|Scope Cloud Sync to selected users and groups.|
|[Mapping user and group attributes](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure#attribute-mapping)|Map attributes for users and groups.|
|[Working with directory extensions and custom attributes](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure#directory-extensions-and-custom-attribute-mapping)|Use directory extensions and custom attributes|
|[Configure single sign-on](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-sso)|Set up Cloud Sync single sign-on.|

<a name='azure-ad-connect'></a>

## Microsoft Entra Connect
Several of the configuration tasks used with Microsoft Entra Connect are set up when you install the tool.  You should review the custom installation section to make sure you have the information you'll need when setting up.  Also, the post installation tasks should be reviewed to further validate and customize your specific configuration.
  
|Task|Description|
|-----|-----|
|[Configure sync features](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-roadmap#configure-sync-features)|Review the configurable sync features for Microsoft Entra Connect.|
|[Customize Microsoft Entra Connect Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-roadmap#customize-azure-ad-connect-sync)|How to customize the default configuration.|
|[Configure federation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-roadmap#configure-federation-features)|How to federate with Microsoft Entra Connect.|
|[Post installation tasks](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-post-installation)|More tasks for managing Microsoft Entra Connect|
|[Mapping user and group attributes](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure#attribute-mapping)|Map attributes for users and groups.|
|[Device writeback](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-device-writeback)|Configure device writeback.|
|[Configure single sign-on](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sso-quick-start)|Set up Microsoft Entra Connect to use single sign-on.|
