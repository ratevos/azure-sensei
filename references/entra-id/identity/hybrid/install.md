# Install your synchronization tool

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/install  
> Microsoft doc last updated: 09/18/2025

The following document provides the steps to install either cloud sync or Microsoft Entra Connect.  

<a name='install-the-azure-ad-connect-provisioning-agent-for-cloud-sync'></a>

## Install the Microsoft Entra provisioning agent for cloud sync
Cloud sync uses the Microsoft Entra provisioning agent. Use the steps below to install it.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).

1. Browse to **Entra ID** > **Entra Connect** > **Cloud sync**.

   
 3. Select **cloud sync**
 4. On the left, select **Agent**.
 5. Select **Download on-premises agent**, and select **Accept terms & download**.
 6. Once the **Microsoft Entra provisioning agent package** has completed downloading, run the *AADConnectProvisioningAgentSetup.exe* installation file from your downloads folder.
 7. On the splash screen, select **I agree to the license and conditions**, and then select **Install**.
 8. Once the installation operation completes, the configuration wizard launches. Select **Next** to start the configuration.
 9. On the **Select Extension** screen, select **HR-driven provisioning (Workday and SuccessFactors) / Microsoft Entra Connect cloud sync** and select **Next**.
 10. Sign in with your Microsoft Entra Hybrid Identity Administrator account. 
 11. On the **Configure Service Account** screen, select a group Managed Service Account (gMSA). This account is used to run the agent service. To continue, select **Next**.
 12. On the **Connect Active Directory** screen, if your domain name appears under **Configured domains**, skip to the next step. Otherwise, type your Active Directory domain name, and select **Add directory**.  
 13. Sign in with your Active Directory domain administrator account. Select **OK**, then select **Next** to continue. 
 14. Select **Next** to continue.
 15. On the **Configuration complete** screen, select **Confirm**.  
 16. Once this operation completes, you should be notified that **Your agent configuration was successfully verified.**  You can select **Exit**.
 17. If you still get the initial splash screen, select **Close**.

For more information, see [Installing the provisioning agent](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-install) in the cloud sync reference section.

<a name='install-azure-ad-connect-with-express-settings'></a>

## Install Microsoft Entra Connect with express settings
Express settings are the default option to install Microsoft Entra Connect, and it's used for the most commonly deployed scenario. 

 1. Sign in as Local Administrator on the server you want to install Microsoft Entra Connect on.  The server you sign in on is the sync server.
 2. Go to *AzureADConnect.msi* and double-select to open the installation file.
 3. On **Welcome**, select the checkbox to agree to the licensing terms, and then select **Continue**.
 4. On **Express settings**, select **Use express settings**.
 5. On **Connect to Microsoft Entra ID**, enter the username and password of the Hybrid Identity Administrator account, and then select **Next**.
 6. On **Connect to AD DS**, enter the username and password for an Enterprise Admin account. You can enter the domain part in either NetBIOS or FQDN format, like `FABRIKAM\administrator` or `fabrikam.com\administrator`. Select **Next**
 7. The [Microsoft Entra sign-in configuration](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/plan-connect-user-signin#azure-ad-sign-in-configuration) page appears only if you didn't complete the step to [verify your domains](https://learn.microsoft.com/en-us/entra/fundamentals/add-custom-domain) in the [prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-prerequisites)
 8. On **Ready to configure**, select **Install**
 9. When the installation is finished, select **Exit**.
 10. Before you use Synchronization Service Manager or Synchronization Rule Editor, sign out, and then sign in again.

For more information, see [Installing the Microsoft Entra Connect with express settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-express) in the Microsoft Entra Connect Sync reference section.

<a name='azure-ad-connect-with-custom-settings'></a>

## Microsoft Entra Connect with custom settings
Use *custom settings* in Microsoft Entra Connect when you want more options for the installation.

For more information, see [Installing the Microsoft Entra Connect with custom settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom) in the Microsoft Entra Connect Sync reference section.
