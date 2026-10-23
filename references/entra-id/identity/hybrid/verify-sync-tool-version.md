# Verify your version of cloud sync or connect sync

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/verify-sync-tool-version  
> Microsoft doc last updated: 04/09/2025

This article describes the steps to verify the installed version of the provisioning agent and connect sync.

## Verify the provisioning agent
To see what version of the provisioning agent you're using, use the following steps:

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

## Verify connect sync
To see what version of connect sync you're using, use the following steps:

### On the local server

To verify that the agent is running, follow these steps:

 1. Sign in to the server with an administrator account.
 2. Open **Services** either by navigating to it or by going to *Start/Run/Services.msc*.
 3. Under **Services**, make sure that **Microsoft Entra ID Sync** is present and the status is **Running**.

### Verify the connect sync version

To verify the version of the agent that is running, follow these steps:

1.  Navigate to 'C:\Program Files\Microsoft Azure AD Connect'
2.  Right-click on **AzureADConnect.exe** and select **properties**.
3.  Click the **details** tab and the version number ID next to the Product version.

## Next steps
- [Common scenarios](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Choosing the right sync tool](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios)
- [Steps to start](https://learn.microsoft.com/en-us/entra/identity/hybrid/get-started)
- [Prerequisites](https://learn.microsoft.com/en-us/entra/identity/hybrid/prerequisites)
