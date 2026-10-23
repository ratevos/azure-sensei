# What is the Microsoft Entra Connect Administration Agent - Microsoft Entra Connect

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-aadc-admin-agent  
> Microsoft doc last updated: 04/09/2025


The Microsoft Entra Connect Administration Agent is a component of Microsoft Entra Connect that can be installed on a Microsoft Entra Connect server. The agent is used to collect specific data from your hybrid Active Directory environment. The collected data helps a Microsoft support engineer troubleshoot issues when you open a support case.

> [!NOTE]
> The Microsoft Entra Connect Administration Agent is no longer part of the Microsoft Entra Connect installation, and it can't be used with Microsoft Entra Connect version 2.1.12.0 or later.

The Microsoft Entra Connect Administration Agent waits for specific requests for data from Microsoft Entra ID.  The agent then takes the requested data from the sync environment and sends it to Microsoft Entra ID, where it's presented to the Microsoft support engineer.

The information that the Microsoft Entra Connect Administration Agent retrieves from your environment isn't stored. The information is shown only to the Microsoft support engineer to help them investigate and troubleshoot a Microsoft Entra Connect-related support case.

By default, the Microsoft Entra Connect Administration Agent isn't installed on the Microsoft Entra Connect server. To assist with support cases, you must install the agent to collect data.

<a name='install-the-azure-ad-connect-administration-agent'></a>

## Install the Microsoft Entra Connect Administration Agent

To install the Microsoft Entra Connect Administration Agent on the Microsoft Entra Connect server, first be sure you meet some prerequisites, and then install the agent.

Prerequisites:

- Microsoft Entra Connect is installed on the server.
- Microsoft Entra Connect Health is installed on the server.

The Microsoft Entra Connect Administration Agent binaries are placed on the Microsoft Entra Connect server.

To install the agent:

1. Open PowerShell as administrator.
1. Go to the directory where the application is located: `cd "C:\Program Files\Microsoft Azure Active Directory Connect\Tools"`.
1. Run `ConfigureAdminAgent.ps1`.

When prompted, enter your Microsoft Entra Hybrid Identity Administrator credentials. These credentials should be the same credentials you entered during Microsoft Entra Connect installation.

> [!NOTE]
> The `ConfigureAdminAgent.ps1` script is no longer included in Microsoft Entra Connect version 2.1.12.0 or later. The Microsoft Entra Connect Administration Agent itself is deprecated and cannot be installed on these versions.

After the agent is installed, you'll see the following two new programs in **Add/Remove Programs** in Control Panel on your server:

## What data in my sync service is visible to the Microsoft support engineer?

When you open a support case, the Microsoft support engineer can see this information for a specific user:

- The relevant data in Windows Server Active Directory (Windows Server AD).
- The Windows Server AD connector space on the Microsoft Entra Connect server.
- The Microsoft Entra connector space on the Microsoft Entra Connect server.
- The metaverse in the Microsoft Entra Connect server.

The Microsoft support engineer can't change any data in your system, and they can't see any passwords.

## What if I don't want the Microsoft support engineer to access my data?

After the agent is installed, if you don't want the Microsoft support engineer to access your data for a support call, you can disable the functionality by modifying the service config file:

1. In Notepad, open *C:\Program Files\Microsoft Azure AD Connect Administration Agent\AzureADConnectAdministrationAgentService.exe.config*.
1. Disable the **UserDataEnabled** setting as shown in the following example. If the **UserDataEnabled** setting exists and is set to **true**, set it to **false**. If the setting doesn't exist, add the setting.

    ```xml
    <appSettings>
      <add key="TraceFilename" value="ADAdministrationAgent.log" />
      <add key="UserDataEnabled" value="false" />
    </appSettings>
    ```

1. Save the config file.
1. Restart the Microsoft Entra Connect Administration Agent service as shown in the following figure:

   

## Next steps

Learn more about [integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity).
