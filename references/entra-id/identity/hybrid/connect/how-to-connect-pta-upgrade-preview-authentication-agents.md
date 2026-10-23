# Microsoft Entra Connect - Pass-through Authentication - Upgrade auth agents

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta-upgrade-preview-authentication-agents  
> Microsoft doc last updated: 04/09/2025


## Overview

This article is for customers using Microsoft Entra pass-through authentication through preview. We recently upgraded (and rebranded) the Authentication Agent software. You need to *manually* upgrade preview Authentication Agents installed on your on-premises servers. This manual upgrade is a one-time action only. All future updates to Authentication Agents are automatic. The reasons to upgrade are as follows:

- The preview versions of Authentication Agents won't receive any further security or bug fixes.
- The preview versions of Authentication Agents can't be installed on other servers, for high availability.

## Check versions of your Authentication Agents

### Step 1: Check where your Authentication Agents are installed

Follow these steps to check where your Authentication Agents are installed:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).
2. Browse to **Entra ID** > **Entra Connect** > **Connect sync**.
4. Select **Pass-through Authentication**. This blade lists the servers where your Authentication Agents are installed.

 - Pass-through Authentication blade](./media/how-to-connect-pta-upgrade-preview-authentication-agents/pta8.png)

### Step 2: Check the versions of your Authentication Agents

To check the versions of your Authentication Agents, on each server identified in the preceding step, follow these instructions:

1. Go to **Control Panel -> Programs -> Programs and Features** on the on-premises server.
2. If there's an entry for "**Microsoft Entra Connect Authentication Agent**", you don't need to take any action on this server.
3. If there's an entry for "**Microsoft Entra private network connector**", you need to manually upgrade on this server.

## Best practices to follow before starting the upgrade

Before upgrading, ensure that you have the following items in place:

1. **Create cloud-only Hybrid Identity Administrator account**: Don’t upgrade without having a cloud-only Hybrid Identity Administrator account to use in emergency situations where your Pass-through Authentication Agents aren't working properly. Learn about [emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access). This step is critical and ensures that you don't get locked out of your tenant.
2. **Ensure high availability**: If not completed previously, install a second standalone Authentication Agent to provide high availability for sign-in requests, using these [instructions](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta-quick-start#step-4-ensure-high-availability).

<a name='upgrading-the-authentication-agent-on-your-azure-ad-connect-server'></a>

## Upgrading the Authentication Agent on your Microsoft Entra Connect server

You need upgrade Microsoft Entra Connect before upgrading the Authentication Agent on the same server. Follow these steps on both your primary and staging Microsoft Entra Connect servers:

1. **Upgrade Microsoft Entra Connect**: Follow this [article](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-upgrade-previous-version) and upgrade to the latest Microsoft Entra Connect version.
2. **Uninstall the preview version of the Authentication Agent**: Download [this PowerShell script](https://aka.ms/rmpreviewagent) and run it as an Administrator on the server.
3. **Download the latest version of the Authentication Agent (versions 1.5.2482.0 or later)**: Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).  Browse to **Entra ID** > **Entra Connect** > **Connect sync**.

 Select **Pass-through Authentication -> Download agent**. Accept the [terms of service](https://aka.ms/authagenteula) and download the latest version of the Authentication Agent. You can also download the Authentication Agent from [here](https://aka.ms/getauthagent).
4. **Install the latest version of the Authentication Agent**: Run the executable downloaded in Step 3. Provide your tenant's Hybrid Identity Administrator credentials when prompted.
5. **Verify that the latest version has been installed**: As shown before, go to **Control Panel -> Programs -> Programs and Features** and verify that there's an entry for "**Microsoft Entra Connect Authentication Agent**".

> [!NOTE]
> If you check the Pass-through Authentication blade on the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator). after completing the preceding steps, you'll see two Authentication Agent entries per server - one entry showing the Authentication Agent as **Active** and the other as **Inactive**. This is *expected*. The **Inactive** entry is automatically dropped after a few days.

## Upgrading the Authentication Agent on other servers

Follow these steps to upgrade Authentication Agents on other servers (where Microsoft Entra Connect isn't installed):

1. **Uninstall the preview version of the Authentication Agent**: Download [this PowerShell script](https://aka.ms/rmpreviewagent) and run it as an Administrator on the server.
2. **Download the latest version of the Authentication Agent (versions 1.5.2482.0 or later)**: Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) with your tenant's Hybrid Identity Administrator credentials. Select **Microsoft Entra ID -> Microsoft Entra Connect -> Pass-through Authentication -> Download agent**. Accept the terms of service and download the latest version.
3. **Install the latest version of the Authentication Agent**: Run the executable downloaded in Step 2. Provide your tenant's Hybrid Identity Administrator credentials when prompted.
4. **Verify that the latest version has been installed**: As shown before, go to **Control Panel -> Programs -> Programs and Features** and verify that there's an entry called **Microsoft Entra Connect Authentication Agent**.

> [!NOTE]
> If you check the Pass-through Authentication blade on the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator) after completing the preceding steps, you'll see two Authentication Agent entries per server - one entry showing the Authentication Agent as **Active** and the other as **Inactive**. This is *expected*. The **Inactive** entry is automatically dropped after a few days.

## Next steps
- [**Troubleshoot**](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication) - Learn how to resolve common issues with the feature.
