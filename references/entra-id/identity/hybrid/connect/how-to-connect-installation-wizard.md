# Re-running the Microsoft Entra Connect install wizard

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-installation-wizard  
> Microsoft doc last updated: 04/09/2025

The first time you run the Microsoft Entra Connect installation wizard, it walks you through how to configure your installation. If you run the installation wizard again, it offers options for maintenance.

>[!IMPORTANT]
>Be aware that you can't run the installation wizard while a synchronization is in progress.  Please verify that a synchronization is not running before  launching the wizard.

You can find the installation wizard in the start menu named **Microsoft Entra Connect**.

When you start the installation wizard, you see a page with these options:

If you have installed ADFS with Microsoft Entra Connect, you have even more options. The other options you have for ADFS are documented in [ADFS management](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-management#manage-ad-fs).

Select one of the tasks and click **Next** to continue.

> [!IMPORTANT]
> While the installation is wizard open, all operations in the sync engine are suspended. Make sure you close the installation wizard as soon as you have completed your configuration changes.
>
>

## View current configuration
This option gives you a quick view of your currently configured options.

Click **Previous** to go back. If you select **Exit**, you close the installation wizard.

## Customize synchronization options
This option is used to make changes to the sync configuration. You see a subset of options from the custom configuration installation path. You see this option even if you used express installation initially.

* [Add more directories](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom#connect-your-directories). 
* [Change Domain and OU filtering](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom#domain-and-ou-filtering).
* Remove Group filtering.
* [Change optional features](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom#optional-features).

The other options from the initial installation can't be changed and aren't available. These options are:

* Change the attribute to use for userPrincipalName and sourceAnchor.
* Change the joining method for objects from different forest.
* Enable group-based filtering.

## Refresh directory schema
This option is used if you have changed the schema in one of your on-premises AD DS forests. For example, you might have installed Exchange or upgraded to a Windows Server 2012 schema with device objects. In this case, you need to instruct Microsoft Entra Connect to read the schema again from AD DS and update its cache. This action also regenerates the Sync Rules. If you add the Exchange schema, as an example, the Sync Rules for Exchange are added to the configuration.

When you select this option, all the directories in your configuration are listed. You can keep the default setting and refresh all forests or unselect some of them.

## Configure staging mode
This option allows you to enable and disable staging mode on the server. More information about staging mode and how it's used can be found in [Operations](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-staging-server).

The option shows if staging is currently enabled or disabled:  

To change the state, select this option and select or unselect the checkbox.  

## Change user sign-in
This option allows you to change the user sign-in method to and from password hash sync, pass-through authentication or federation. You can't change to **do not configure**.

For more information on this option, see [user sign-in](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/plan-connect-user-signin#changing-the-user-sign-in-method).

## Next steps
* Learn more about the configuration model used by Microsoft Entra Connect Sync in [Understanding Declarative Provisioning](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-declarative-provisioning).

**Overview topics**

* [Microsoft Entra Connect Sync: Understand and customize synchronization](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis)
* [Integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity)
