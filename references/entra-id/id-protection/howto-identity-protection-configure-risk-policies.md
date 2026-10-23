# Risk policies - Microsoft Entra ID Protection

> Source: https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies  
> Microsoft doc last updated: 10/30/2025


There are two types of [risk policies](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies) in Microsoft Entra Conditional Access you can set up. You can use these policies to automate the response to risks allowing users to self-remediate when risk is detected:

- [User risk policy](#user-risk-policy-in-conditional-access)
- [Sign-in risk policy](#sign-in-risk-policy-in-conditional-access)

> [!WARNING]
> Don't combine sign-in risk and user risk conditions in the same Conditional Access policy. Create separate policies for each risk condition.

## Prerequisites

- The Microsoft Entra ID P2 or Microsoft Entra Suite license is required for full access to Microsoft Entra ID Protection features.
    - For a detailed list of capabilities for each license tier, see [What is Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection).
- The [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) role is the least privileged role required to **create or edit Conditional Access policies**.

## Choosing acceptable risk levels

Organizations must decide the level of risk they want to require access control on, while balancing security posture and user productivity.

Choosing to apply access control on a **High** risk level reduces the number of times a policy is triggered and minimizes friction for users. However, it excludes **Low** and **Medium** risks from the policy, which might not block an attacker from exploiting a compromised identity. Selecting **Medium** and/or **Low** risk levels usually introduces more user interrupts.

Configured trusted [network locations](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-assignment-network#trusted-locations) are used by Microsoft Entra ID Protection in some risk detections to reduce false positives.

### Risk remediation

Organizations can choose to block access when risk is detected. Blocking sometimes stops legitimate users from doing what they need to. A better solution is to configure [user](#user-risk-policy-in-conditional-access) and [sign-in](#sign-in-risk-policy-in-conditional-access) risk-based Conditional Access policies that [allow users to self-remediate](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock#end-user-self-remediation).

> [!WARNING]
> Users must register for Microsoft Entra multifactor authentication before they face a situation requiring remediation. For hybrid users that are synced from on-premises, password writeback must be enabled. Users not registered are blocked and require administrator intervention.
> 
> Password change (I know my password and want to change it to something new) outside of the risky user policy remediation flow doesn't meet the requirement for secure password change.

### Microsoft recommendations

Microsoft recommends the following risk policy configurations to protect your organization:

### User risk policy

Organizations should select **Require risk remediation** when user risk level is **High**. For passwordless users, Microsoft Entra revokes the user's sessions so they must reauthenticate. For users with passwords, they're prompted to complete a secure password change after a successful Microsoft Entra multifactor authentication.

When **Require risk remediation** is selected, two settings are automatically applied:
- **Require authentication strength** is automatically selected as a grant control.
- **Sign-in frequency - Every time** is automatically applied as a session control.

### Sign-in risk policy

Require Microsoft Entra multifactor authentication when sign-in risk level is **Medium** or **High**. This configuration allows users to prove it's them by using one of their registered authentication methods, remediating the sign-in risk.

We also recommend including the [sign-in frequency session control](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-session-lifetime#require-reauthentication-every-time) to require reauthentication for risky sign-ins. A successful "strong authentication" usually via multifactor authentication or passwordless authentication, is the only way to self-remediate sign-in risk, regardless of the risk level.

## Enable policies

Organizations can choose to deploy risk-based policies in Conditional Access using the following steps or use [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

Before organizations enable these policies, they should take action to [investigate](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk) and [remediate](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock) any active risks.

### Policy exclusions

Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

### User risk policy in Conditional Access

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access**.
1. Select **New policy**.
1. Give your policy a name. We recommend that organizations create a meaningful standard for the names of their policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
   1. Select **Done**.
1. Under **Target resources** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Conditions** > **User risk**, set **Configure** to **Yes**. 
   1. Under **Configure user risk levels needed for policy to be enforced**, select **High**. [This guidance is based on Microsoft recommendations and might be different for each organization](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies#choosing-acceptable-risk-levels)
   1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require risk remediation**. The **Require authentication strength** grant control is automatically selected. Choose the strength appropriate for your organization.
   1. Select **Select**.
1. Under **Session**, **Sign-in frequency - Every time** is automatically applied as a session control and is mandatory.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to create your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

### Sign-in risk policy in Conditional Access

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access**.
1. Select **New policy**.
1. Give your policy a name. We recommend that organizations create a meaningful standard for the names of their policies.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts. 
   1. Select **Done**.
1. Under **Cloud apps or actions** > **Include**, select **All resources (formerly 'All cloud apps')**.
1. Under **Conditions** > **Sign-in risk**, set **Configure** to **Yes**. 
   1. Under **Select the sign-in risk level this policy will apply to**, select **High** and **Medium**. [This guidance is based on Microsoft recommendations and might be different for each organization](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies#choosing-acceptable-risk-levels)
   1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Grant access**.
   1. Select **Require authentication strength**, then select the built-in **Multifactor authentication** authentication strength from the list.
   1. Select **Select**.
1. Under **Session**.
   1. Select **Sign-in frequency**.
   1. Ensure **Every time** is selected.
   1. Select **Select**.
1. Confirm your settings and set **Enable policy** to **Report-only**.
1. Select **Create** to create to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

### Passwordless scenarios

For organizations that adopt [passwordless authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-passwordless-deployment) make the following changes: 

#### Update your passwordless sign-in risk policy

1. Under **Users**:
   1. **Include**, select **Users and groups** and target your passwordless users.
   1. Under **Exclude**, select **Users and groups** and choose your organization's emergency access or break-glass accounts.
   1. Select **Done**.
1. Under **Cloud apps or actions** > **Include**, select **All resources** (formerly 'All cloud apps').
1. Under **Conditions** > **Sign-in risk**, set **Configure** to **Yes**.
    1. Under **Select the sign-in risk level this policy will apply to**, select **High** and **Medium**. For more information on risk levels, see [Choosing acceptable risk levels](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies#choosing-acceptable-risk-levels).
    1. Select **Done**.
1. Under **Access controls** > **Grant**, select **Grant access**.
    1. Select **Require authentication strength**, then select the built-in **Passwordless MFA** or **Phishing-resistant MFA** based on which method the targeted users have.
    1. Select **Select**.
1. Under **Session**:
    1. Select **Sign-in frequency**.
    1. Ensure **Every time** is selected.
    1. Select **Select**.

## Migrate risk policies to Conditional Access

If you have legacy risk policies enabled in Microsoft Entra ID Protection, you should plan to migrate them to Conditional Access:

> [!WARNING]
> The legacy risk policies configured in Microsoft Entra ID Protection will be retired on **October 1, 2026**.

### Migrate to Conditional Access

1. **Create equivalent** [user risk-based](#user-risk-policy-in-conditional-access) and [sign-in risk-based](#sign-in-risk-policy-in-conditional-access) policies in Conditional Access in report-only mode. You can create a policy with the previous steps or using [Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common) based on Microsoft's recommendations and your organizational requirements.
   1. After administrators confirm the settings using [report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-insights-reporting), they can move the **Enable policy** toggle from **Report-only** to **On**.
1. **Disable** the old risk policies in ID Protection.
   1. Browse to **ID Protection** > **Dashboard** > Select the **User risk** or **Sign-in risk** policy.
   1. Set **Enforce policy** to **Disabled**.
1. Create other risk policies if needed in [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common).

#### Help and support for migrating risk policies

If you need help migrating your risk policies to Conditional Access, please submit a support request in the Microsoft Entra admin center.

1. Go to **New support request** in the Microsoft Entra admin center.
1. Describe your issue: **Migrate legacy ID Protection policy**.
1. Select **Microsoft Entra Sign-in and Multifactor Authentication** > **Next**.
1. Select **Configuring new or existing policy settings** > **Next**.
1. Close the solution page.
1. Select **Create a support request**.
1. Use the following selections to get your request to the right team:
    1. Issue type: **Technical**.
    1. Service type: **Microsoft Entra Sign-in and Multifactor Authentication**.
    1. Summary: **Migrate legacy ID Protection policy**.
    1. Problem type: **Identity Protection**.
    1. Problem subtype: **Configure risk policies**.
1. Select **Next** and navigate to the **Additional details** tab to fill out your details.
1. Fill out the required details and submit your request.

## Related content

- [Enable Microsoft Entra multifactor authentication registration policy](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-mfa-policy)
- [What is risk](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks)
- [Investigate risk detections](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk)
- [Simulate risk detections](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-simulate-risk)
