# Block legacy authentication with Conditional Access

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication  
> Microsoft doc last updated: 03/24/2026


## Overview

Microsoft recommends that organizations block authentication requests using legacy protocols that don't support multifactor authentication. Based on Microsoft's analysis more than 97 percent of credential stuffing attacks use legacy authentication and more than 99 percent of password spray attacks use legacy authentication protocols. These attacks would stop with basic authentication disabled or blocked.

Customers without licenses that include Conditional Access can make use of [security defaults](https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults) to block legacy authentication.

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Template deployment

Organizations can deploy this policy by following the steps outlined below or by using the [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

## Create a Conditional Access policy

The following steps help create a Conditional Access policy to block legacy authentication requests. This policy is put in to [Report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting) to start so administrators can determine the impact they have on existing users. When administrators are comfortable that the policy applies as they intend, they can switch to **On** or stage the deployment by adding specific groups and excluding others.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Give your policy a name. Create a meaningful standard for the names of your policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose any accounts that must maintain the ability to use legacy authentication. Microsoft recommends you exclude at least one account to prevent yourself from being locked out due to misconfiguration.
1. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Conditions** > **Client apps**, set **Configure** to **Yes**.
   1. Check only the boxes **Exchange ActiveSync clients** and **Other clients**.
   1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Block access**.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

> [!NOTE]
> Conditional Access policies are enforced after first-factor authentication is completed. Conditional Access isn't intended to be an organization's first line of defense for scenarios like denial-of-service (DoS) attacks, but it can use signals from these events to determine access.

## Identify legacy authentication use

To understand if your users have client apps that use legacy authentication, administrators can check for indicators in the sign-in logs with the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).
1. Browse to **Entra ID** > **Monitoring & health** > **Sign-in logs**.
1. Add the **Client App** column if it isn't shown by selecting **Columns** > **Client App**.
1. Select **Add filters** > **Client App** > choose all of the legacy authentication protocols and select **Apply**.
1. Also perform these steps on the **User sign-ins (non-interactive)** tab.

Filtering shows you sign-in attempts made by legacy authentication protocols. Clicking on each individual sign-in attempt shows you more details. The **Client App** field under the **Basic Info** tab indicates which legacy authentication protocol was used. These logs indicate users who are using clients that depend on legacy authentication.

Additionally, to help triage legacy authentication within your tenant use the [Sign-ins using legacy authentication workbook](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/workbook-legacy-authentication).

## Related content

- [Deprecation of Basic authentication in Exchange Online](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online)
- [How to set up a multifunction device or application to send email using Microsoft 365](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365)
- [How modern authentication works for Office client apps](https://learn.microsoft.com/en-us/microsoft-365/enterprise/modern-auth-for-office-2013-and-2016)
- [Connect to Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell)
