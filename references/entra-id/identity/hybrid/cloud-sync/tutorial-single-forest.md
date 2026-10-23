# Tutorial - Integrate a single forest with a single Microsoft Entra tenant

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/tutorial-single-forest  
> Microsoft doc last updated: 04/09/2025


This tutorial walks you through creating a hybrid identity environment using Microsoft Entra Cloud Sync.

You can use the environment you create in this tutorial for testing or for getting more familiar with cloud sync.

## Prerequisites

<a name='in-the-entra-portal'></a>

### In the Microsoft Entra admin center

- Microsoft recommends that organizations have two cloud-only emergency access accounts permanently assigned the [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) role. These accounts are highly privileged and aren't assigned to specific individuals. The accounts are limited to emergency or "break glass" scenarios where normal accounts can't be used or all other administrators are accidentally locked out. These accounts should be created following the [emergency access account recommendations](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- Add one or more [custom domain names](https://learn.microsoft.com/en-us/entra/fundamentals/add-custom-domain) to your Microsoft Entra tenant. Your users can sign in with one of these domain names.

### In your on-premises environment

1. Identify a domain-joined host server running Windows Server 2016 or greater with minimum of 4-GB RAM and .NET 4.7.1+ runtime 

2. If there's a firewall between your servers and Microsoft Entra ID, configure the following items:
   - Ensure that agents can make *outbound* requests to Microsoft Entra ID over the following ports:

     | Port number | How it's used |
     | --- | --- |
     | **80** | Downloads the certificate revocation lists (CRLs) while validating the TLS/SSL certificate |
     | **443** | Handles all outbound communication with the service |
     | **8080** (optional) | Agents report their status every 10 minutes over port 8080, if port 443 is unavailable. This status is displayed on the portal. |
     
     If your firewall enforces rules according to the originating users, open these ports for traffic from Windows services that run as a network service.
   - If your firewall or proxy allows you to specify safe suffixes, then add connections to **\*.msappproxy.net** and **\*.servicebus.windows.net**. If not, allow access to the [Azure datacenter IP ranges](https://www.microsoft.com/download/details.aspx?id=41653), which are updated weekly.
   - Your agents need access to **login.windows.net** and **login.microsoftonline.com** for initial registration. Open your firewall for those URLs as well.
   - For certificate validation, unblock the following URLs: **mscrl.microsoft.com:80**, **crl.microsoft.com:80**, **ocsp.msocsp.com:80**, and **www\.microsoft.com:80**. Since these URLs are used for certificate validation with other Microsoft products, you may already have these URLs unblocked.

<a name='install-the-azure-ad-connect-provisioning-agent'></a>

## Install the Microsoft Entra provisioning agent

If you're using the  [Basic AD and Azure environment](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/tutorial-basic-ad-azure) tutorial, it would be DC1. To install the agent, follow these steps: 

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).
1. On the left pane, select **Entra Connect**, and then select **Cloud Sync**.

   

1. On the left pane, select **Agents**.
1. Select **Download on-premises agent**, and then select **Accept terms & download**.

   

1. After you download the Microsoft Entra Connect Provisioning Agent Package, run the *AADConnectProvisioningAgentSetup.exe* installation file from your downloads folder.

1. On the screen that opens, select the **I agree to the license terms and conditions** checkbox, and then select **Install**.

   

1. After the installation finishes, the configuration wizard opens. Select **Next** to start the configuration.

   
   
1. Sign in with an account with at least the [Hybrid Identity administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) role. If you have Internet Explorer enhanced security enabled, it blocks the sign-in. If so, close the installation, [disable Internet Explorer enhanced security](https://learn.microsoft.com/en-us/troubleshoot/developer/browsers/security-privacy/enhanced-security-configuration-faq), and restart the Microsoft Entra Provisioning Agent Package installation.

   

1. On the **Configure Service Account** screen, select a group Managed Service Account (gMSA). This account is used to run the agent service. If a managed service account is already configured in your domain by another agent and you're installing a second agent, select **Create gMSA**. The system detects the existing account and adds the required permissions for the new agent to use the gMSA account. When you're prompted, choose one of two options:

   - **Create gMSA**: Let the agent create the **provAgentgMSA$** managed service account for you. The group managed service account (for example, `CONTOSO\provAgentgMSA$`) is created in the same Active Directory domain where the host server joined. To use this option, enter the Active Directory domain administrator credentials (recommended).
   - **Use custom gMSA**: Provide the name of the managed service account that you manually created for this task.

   

1. To continue, select **Next**.

1. On the **Connect Active Directory** screen, if your domain name appears under **Configured domains**, skip to the next step. Otherwise, enter your Active Directory domain name, and select **Add directory**.

   

1. Sign in with your Active Directory domain administrator account. The domain administrator account shouldn't have an expired password. If the password is expired or changes during the agent installation, reconfigure the agent with the new credentials. This operation adds your on-premises directory. Select **OK**, and then select **Next** to continue.

1. Select **Next** to continue.

1. On the **Configuration complete** screen, select **Confirm**. This operation registers and restarts the agent.

   

1. After the operation finishes, you see a notification that your agent configuration was successfully verified. Select **Exit**. If you still get the initial screen, select **Close**.

## Verify agent installation

Agent verification occurs in the Azure portal and on the local server that runs the agent.

### Verify the agent in the Azure portal

To verify that Microsoft Entra ID registers the agent, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).
1. Select **Entra Connect**, and then select **Cloud Sync**.

    

1. On the **Cloud Sync** page, click **Agents** to see the agents that you installed. Verify that the agent appears and that the status is **active**.

### Verify the agent on the local server

To verify that the agent is running, follow these steps:

1. Sign in to the server with an administrator account.
1. Go to **Services**. You can also use *Start/Run/Services.msc* to get to it.
1. Under **Services**, make sure that **Microsoft Azure AD Connect Agent Updater** and **Microsoft Azure AD Connect Provisioning Agent** are present and that the status is **Running**.

    [](./media/entra-cloud-sync-how-to-verify-installation/windows-services.png#lightbox)

### Verify the provisioning agent version

To verify the version of the agent that's running, follow these steps:

1. Go to *C:\Program Files\Microsoft Azure AD Connect Provisioning Agent*.
1. Right-click *AADConnectProvisioningAgent.exe* and select **Properties**.
1. Select the **Details** tab. The version number appears next to the product version.

<a name='configure-azure-ad-connect-cloud-sync'></a>

## Configure Microsoft Entra Cloud Sync

Use the following steps to configure and start the provisioning:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).

1. Browse to **Entra ID** > **Entra Connect** > **Cloud sync**.

   
 3. Select **New configuration** > **AD to Microsoft Entra ID sync**.
 4. Choose the domain that you want to sync, and select **Create**.

For more information about how to configure Microsoft Entra Cloud Sync, see [Provision Active Directory to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure).

## Verify users are created and synchronization is occurring

You'll now verify that the users that you had in your on-premises directory that are in scope of synchronization have been synchronized and now exist in your Microsoft Entra tenant. The sync operation may take a few hours to complete. To verify users are synchronized, follow these steps:

 1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).
 2. Browse to **Entra ID** > **Users**.
 3. Verify that you see the new users in your tenant

## Test signing in with one of your users

 1. Browse to [https://myapps.microsoft.com](https://myapps.microsoft.com)

 2. Sign in with a user account that was created in your tenant.  You'll need to sign in using the following format: (user@domain.onmicrosoft.com). Use the same password that the user uses to sign in on-premises.

   

You've now successfully configured a hybrid identity environment using Microsoft Entra Cloud Sync.

## Next steps 

- [What is provisioning?](https://learn.microsoft.com/en-us/entra/identity/hybrid/what-is-provisioning)
- [What is Microsoft Entra Connect cloud provisioning?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync)
