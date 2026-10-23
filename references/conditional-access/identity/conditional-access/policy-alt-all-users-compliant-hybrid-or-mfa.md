# Require compliant, hybrid joined devices, or MFA

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-all-users-compliant-hybrid-or-mfa  
> Microsoft doc last updated: 03/24/2026


## Overview

Organizations who deploy Microsoft Intune can use the information returned from their devices to identify devices that meet compliance requirements such as:

* Requiring a PIN to unlock
* Requiring device encryption
* Requiring a minimum or maximum operating system version
* Requiring a device isn't jailbroken or rooted

Policy compliance information is sent to Microsoft Entra ID where Conditional Access decides to grant or block access to resources. More information about device compliance policies can be found in the article, [Set rules on devices to allow access to resources in your organization using Intune](https://learn.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started)

Requiring a Microsoft Entra hybrid joined device is dependent on your devices already being Microsoft Entra hybrid joined. For more information, see the article [Configure Microsoft Entra hybrid join](https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join).

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Create a Conditional Access policy

The following steps help create a Conditional Access policy to require multifactor authentication, devices accessing resources be marked as compliant with your organization's Intune compliance policies, or be Microsoft Entra hybrid joined.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**: 
      1. Select **Users and groups** 
         1. Choose your organization's emergency access or break-glass accounts.
         1. If you use hybrid identity solutions like Microsoft Entra Connect or Microsoft Entra Connect Cloud Sync, select **Directory roles**, then select **Directory Synchronization Accounts**
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')**.
   1. If you must exclude specific applications from your policy, you can choose them from the **Exclude** tab under **Select excluded cloud apps** and choose **Select**.
1. Under **Access controls** > **Grant**.
   1. Select **Require multifactor authentication**, **Require device to be marked as compliant**, and **Require Microsoft Entra hybrid joined device**
   1. **For multiple controls** select **Require one of the selected controls**.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

> [!NOTE]
> You can enroll your new devices to Intune even if you select **Require device to be marked as compliant** for **All users** and **All resources (formerly 'All cloud apps')** using the previous steps. **Require device to be marked as compliant** control doesn't block Intune enrollment and the access to the Microsoft Intune Web Company Portal application. 

### Known behavior

On iOS, Android, macOS, and some non-Microsoft web browsers, Microsoft Entra ID identifies the device using a client certificate that is provisioned when the device is registered with Microsoft Entra ID. When a user first signs in through the browser the user is prompted to select the certificate. The end user must select this certificate before they can continue to use the browser.

#### Subscription activation

Organizations that use the Subscription Activation feature to enable users to "step-up" from one version of Windows to another and use Conditional Access policies to control access need to exclude one of the following cloud apps from their Conditional Access policies using **Select Excluded Cloud Apps**:

- [Universal Store Service APIs and Web Application, AppID 45a330b1-b1ec-4cc1-9161-9f03992aa49f](https://learn.microsoft.com/en-us/troubleshoot/azure/active-directory/verify-first-party-apps-sign-in#application-ids-of-commonly-used-microsoft-applications).

- [Windows Store for Business, AppID 45a330b1-b1ec-4cc1-9161-9f03992aa49f](https://learn.microsoft.com/en-us/troubleshoot/azure/active-directory/verify-first-party-apps-sign-in#application-ids-of-commonly-used-microsoft-applications).

Although the app ID is the same in both instances, the name of the cloud app depends on the tenant.

When a device is offline for an extended period of time, the device might not reactivate automatically if this Conditional Access exclusion isn't in place. Setting this Conditional Access exclusion ensures that Subscription Activation continues to work seamlessly.

Starting with Windows 11, version 23H2 with [KB5034848](https://support.microsoft.com/help/5034848) or later, users are prompted for authentication with a toast notification when Subscription Activation needs to reactivate. The toast notification shows the following message:

> **Your account requires authentication**
>
> **Please sign in to your work or school account to verify your information.**

Additionally, in the [**Activation**](ms-settings:activation) pane, the following message might appear:

> **Please sign in to your work or school account to verify your information.**

The prompt for authentication usually occurs when a device is offline for an extended period of time. This change eliminates the need for an exclusion in the Conditional Access policy for Windows 11, version 23H2 with [KB5034848](https://support.microsoft.com/help/5034848) or later. A Conditional Access policy can still be used with Windows 11, version 23H2 with [KB5034848](https://support.microsoft.com/help/5034848) or later if the prompt for user authentication via a toast notification isn't desired.

## Related content

[Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)

[Determine effect using Conditional Access report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting)

[Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)

[Device compliance policies work with Microsoft Entra ID](https://learn.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started#device-compliance-policies-work-with-azure-ad)
