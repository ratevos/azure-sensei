# Conditional Access Templates: Simplify Security

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common  
> Microsoft doc last updated: 03/24/2026


## Overview

Conditional Access templates provide a convenient method to deploy new policies aligned with Microsoft recommendations. These templates are designed to provide maximum protection aligned with commonly used policies across various customer types and locations. 

## Template categories

Conditional Access policy templates are organized into the following categories:

# [Secure foundation](#tab/secure-foundation)

Microsoft recommends these policies as the base for all organizations. Deploy these policies as a group.

- [Require multifactor authentication for admins](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-admin)
- [Securing security info registration](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-security-info-registration)
- [Block legacy authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication)
- [Require multifactor authentication for admins accessing Microsoft admin portals](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-admin-portals)
- [Require multifactor authentication for all users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-mfa-strength)
- [Require multifactor authentication for Azure management](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-azure-mgmt)
- [Require compliant or Microsoft Entra hybrid joined device or multifactor authentication for all users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-all-users-compliant-hybrid-or-mfa)
- [Require compliant device](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-compliance)

# [Zero Trust](#tab/zero-trust)

These policies help support a [Zero Trust architecture](https://learn.microsoft.com/en-us/security/zero-trust/deploy/identity).

- [Require multifactor authentication for admins](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-admin)
- [Securing security info registration](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-security-info-registration)
- [Block legacy authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication)
- [Require multifactor authentication for all users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-mfa-strength)
- [Require multifactor authentication for guest access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-guest)
- [Require multifactor authentication for Azure management](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-azure-mgmt)
- [Require multifactor authentication for risky sign-ins](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-sign-in) **Requires Microsoft Entra ID P2**
- [Require password change for high-risk users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-user) **Requires Microsoft Entra ID P2**
- [Block access for unknown or unsupported device platform](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-unknown-unsupported)
- [No persistent browser session](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-persistent-browser)
- [Require approved client apps or app protection policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-compliance)
- [Require compliant or Microsoft Entra hybrid joined device or multifactor authentication for all users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-all-users-compliant-hybrid-or-mfa)
- [Require multifactor authentication for admins accessing Microsoft admin portals](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-admin-portals)
- [Block access for users with insider risk](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-insider-block) **Requires Microsoft Purview**

# [Remote work](#tab/remote-work)

These policies help secure organizations with remote workers.

- [Securing security info registration](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-security-info-registration)
- [Block legacy authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication)
- [Require multifactor authentication for all users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-mfa-strength)
- [Require multifactor authentication for guest access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-guest)
- [Require multifactor authentication for risky sign-ins](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-sign-in) **Requires Microsoft Entra ID P2**
- [Require password change for high-risk users](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-user) **Requires Microsoft Entra ID P2**
- [Require compliant or Microsoft Entra hybrid joined device for administrators](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-admin-device-compliand-hybrid)
- [Block access for unknown or unsupported device platform](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-unknown-unsupported)
- [No persistent browser session](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-persistent-browser)
- [Require compliant device](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-compliance)
- [Require approved client apps or app protection policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-compliance)
- [Use application enforced restrictions for unmanaged devices](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-app-enforced-restrictions)

# [Protect administrator](#tab/protect-administrator)

These policies are for highly privileged administrators in your environment, where compromise might cause the most damage.

- [Require multifactor authentication for admins](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-admin)
- [Block legacy authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-legacy-authentication)
- [Require multifactor authentication for Azure management](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-old-require-mfa-azure-mgmt)
- [Require compliant or Microsoft Entra hybrid joined device for administrators](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-admin-device-compliand-hybrid)
- [Require compliant device](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-compliance)
- [Require phishing-resistant multifactor authentication for administrators](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa)

# [Emerging threats](#tab/emerging-threats)

Policies in this category provide new ways to protect against compromise.

- [Require phishing-resistant multifactor authentication for administrators](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa)

# [AI Agents](#tab/ai-agents)

Policies in this category provide ways to control agents in your environment.

- [Block high-risk agent identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-agent-block-high-risk)
- [Configure policy for autonomous agent access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-autonomous-agents)
- [Configure policy for on-behalf-of agent access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-on-behalf-of-agents)

---

Find these templates in the [Microsoft Entra admin center](https://entra.microsoft.com) > **Entra ID** > **Conditional Access** > **Create new policy from templates**. Select **Show more** to view all policy templates in each category.

> [!IMPORTANT]
> Conditional Access template policies targeting users exclude only the user creating the policy from the template. If your organization needs to [exclude other accounts](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access), modify the policy after it's created. You can find these policies in the [Microsoft Entra admin center](https://entra.microsoft.com) > **Entra ID** > **Conditional Access** > **Policies**. Select a policy to open the editor and modify the excluded users and groups to select accounts you want to exclude.

By default, each policy is created in [report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only). Test and monitor usage to ensure the intended result before turning on each policy.

Organizations can select individual policy templates and:

- View a summary of the policy settings.
- Edit, to customize based on organizational needs.
- Export the JSON definition for use in programmatic workflows.
   - These JSON definitions can be edited and then imported on the main Conditional Access policies page using the **Upload policy file** option.

## Other common policies

- [Require multifactor authentication for device registration](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-device-registration)
- [Block access by location](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-by-location)
- [Block access except specific apps](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-example)

## User exclusions
Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Migrate from classic policies

Classic Conditional Access policies are deprecated and stopped enforcing controls after July 10, 2024. They depend on the retired Azure AD Graph service and can't protect your resources. If your tenant still has classic policies, migrate their settings to modern Conditional Access policies.

> [!WARNING]
> After you disable a classic policy, you can't re-enable it. Document the policy's settings before you disable it.

To migrate a classic policy:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access** > **Classic policies**.
1. Select a classic policy and document its configuration settings.
1. Recreate the settings by using a template or custom policy described earlier in this article. Test the new policy in [report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) before you turn it on.
1. Return to the classic policy and select **Disable**.

The [What If tool](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) indicates whether classic policies still exist in your environment.

## Next steps

- [Simulate sign in behavior using the Conditional Access What If tool.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool)
- [Use report-only mode for Conditional Access to determine the results of new policy decisions.](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only)
