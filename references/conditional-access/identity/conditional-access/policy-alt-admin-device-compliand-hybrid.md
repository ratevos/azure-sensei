# Require administrators use compliant or hybrid joined devices

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-admin-device-compliand-hybrid  
> Microsoft doc last updated: 03/24/2026


## Overview

Accounts that are assigned administrative rights are a target for attackers. Requiring users with these highly privileged rights to perform actions from devices marked as compliant or Microsoft Entra hybrid joined can help limit possible exposure.

More information about device compliance policies can be found in the article, [Set rules on devices to allow access to resources in your organization using Intune](https://learn.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started).

Requiring a Microsoft Entra hybrid joined device is dependent on your devices already being Microsoft Entra hybrid joined. For more information, see the article [Configure Microsoft Entra hybrid join](https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join).

Microsoft recommends you require phishing-resistant multifactor authentication on the following roles at a minimum:

- Global Administrator
- Application Administrator
- Authentication Administrator
- Billing Administrator
- Cloud Application Administrator
- Conditional Access Administrator
- Exchange Administrator
- Helpdesk Administrator
- Password Administrator
- Privileged Authentication Administrator
- Privileged Role Administrator
- Security Administrator
- SharePoint Administrator
- User Administrator

Organizations can choose to include or exclude roles as they see fit.

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
   1. Under **Include**, select **Directory roles** and choose at least the previously listed roles.
   
      > [!WARNING]
      > Conditional Access policies support built-in roles. Conditional Access policies are not enforced for other role types including [administrative unit-scoped](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal) or [custom roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create).

   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts.
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Access controls** > **Grant**.
   1. Select **Require device to be marked as compliant**, and **Require Microsoft Entra hybrid joined device**
   1. **For multiple controls** select **Require one of the selected controls**.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

> [!NOTE]
> You can enroll your new devices to Intune even if you select **Require device to be marked as compliant** for **All users** and **All resources (formerly 'All cloud apps')** using the previous steps. **Require device to be marked as compliant** control does not block Intune enrollment. 

### Known behavior

On Windows 7, iOS, Android, macOS, and some non-Microsoft web browsers, Microsoft Entra ID identifies the device using a client certificate that is provisioned when the device is registered with Microsoft Entra ID. When a user first signs in through the browser the user is prompted to select the certificate. The end user must select this certificate before they can continue to use the browser.

#### Subscription activation

Organizations that use the [Subscription Activation](https://learn.microsoft.com/en-us/windows/deployment/windows-10-subscription-activation) feature to enable users to "step-up" from one version of Windows to another, might want to exclude the Windows Store for Business, AppID 45a330b1-b1ec-4cc1-9161-9f03992aa49f from their device compliance policy.

## Related content

- [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)
- [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)
- [Device compliance policies work with Microsoft Entra ID](https://learn.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started#device-compliance-policies-work-with-azure-ad)
