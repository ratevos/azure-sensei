# Install the Microsoft Entra provisioning agent

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-install  
> Microsoft doc last updated: 09/18/2025


This article walks you through the installation process for the Microsoft Entra provisioning agent and how to initially configure it in the Microsoft Entra admin center.

> [!IMPORTANT]
> The following installation instructions assume that you've met all the [prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-prerequisites).

>[!NOTE]
>This article deals with installing the provisioning agent by using the wizard. For information about installing the Microsoft Entra provisioning agent by using a CLI, see [Install the Microsoft Entra provisioning agent by using a CLI and PowerShell](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-install-pshell).

For more information and an example, view the following video:

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=f28ee688-8834-4d0b-a3e0-bc99a167e0ef]

## Group Managed Service Accounts
A group Managed Service Account (gMSA) is a managed domain account that provides automatic password management, simplified service principal name (SPN) management, and the ability to delegate the management to other administrators. A gMSA also extends this functionality over multiple servers. Microsoft Entra Cloud Sync supports and recommends the use of a gMSA for running the agent. For more information, see [Group Managed Service Accounts](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-prerequisites#group-managed-service-accounts).

### Update an existing agent to use the gMSA
To update an existing agent to use the Group Managed Service Account created during installation, upgrade the agent service to the latest version by running *AADConnectProvisioningAgent.msi*. Now run through the installation wizard again and provide the credentials to create the account when you're prompted to do so.

## Install the agent

>[!NOTE]
>By default, the Microsoft Entra provisioning agent is installed in the default Azure environment.

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

## Verify the agent installation

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

>[!IMPORTANT]
> After you've installed the agent, you must configure and enable it before it will start synchronizing users. To configure a new agent, see [Create a new configuration for Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure).

## Enable password writeback in cloud sync 

You can enable password writeback in SSPR directly in the portal or through PowerShell. 

### Enable password writeback in the portal
To use *password writeback* and enable the self-service password reset (SSPR) service to detect the cloud sync agent, using the portal, complete the following steps: 

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).
 2. Browse to **Entra ID** > **Password reset** > **On-premises integration**.
 3. Check the option for **Enable password write back for synced users** .
 4. (optional) If Microsoft Entra Connect provisioning agents are detected, you can additionally check the option for **Write back passwords with Microsoft Entra Cloud Sync**.   
 5. Check the option for **Allow users to unlock accounts without resetting their password** to *Yes*.
 6. When ready, select **Save**.

### Using PowerShell

To use *password writeback* and enable the self-service password reset (SSPR) service to detect the cloud sync agent, use the `Set-AADCloudSyncPasswordWritebackConfiguration` cmdlet and the tenant’s Global Administrator credentials: 

  ```   
   Import-Module "C:\\Program Files\\Microsoft Azure AD Connect Provisioning Agent\\Microsoft.CloudSync.Powershell.dll" 
   Set-AADCloudSyncPasswordWritebackConfiguration -Enable $true -Credential $(Get-Credential)
  ```

For more information about using password writeback with Microsoft Entra Cloud Sync, see [Tutorial: Enable cloud sync self-service password reset writeback to an on-premises environment ](https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-cloud-sync-sspr-writeback).

## Password hash synchronization and FIPS with cloud sync

If your server has been locked down according to the Federal Information Processing Standard (FIPS), MD5 (message-digest algorithm 5) is disabled.

To enable MD5 for password hash synchronization, do the following:

1. Go to %programfiles%\Microsoft Azure AD Connect Provisioning Agent.
1. Open *AADConnectProvisioningAgent.exe.config*.
1. Go to the configuration/runtime node at the top of the file.
1. Add the `<enforceFIPSPolicy enabled="false"/>` node.
1. Save your changes.

For reference, your code should look like the following snippet:

```xml
<configuration>
   <runtime>
      <enforceFIPSPolicy enabled="false"/>
   </runtime>
</configuration>
```

For information about security and FIPS, see [Microsoft Entra password hash sync, encryption, and FIPS compliance](https://techcommunity.microsoft.com/t5/microsoft-entra-azure-ad-blog/aad-password-sync-encryption-and-fips-compliance/ba-p/243709).

## Next steps 

- [What is provisioning?](https://learn.microsoft.com/en-us/entra/identity/hybrid/what-is-provisioning)
- [What is Microsoft Entra Cloud Sync?](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync)
- [Create a new configuration for Microsoft Entra Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-configure).
