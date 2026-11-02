# Enable Compliant Network Check with Conditional Access

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-compliant-network  
> Microsoft doc last updated: 04/03/2026


Organizations that use Conditional Access along with Global Secure Access can prevent malicious access to Microsoft apps, third-party SaaS apps, and private line-of-business (LoB) apps by using multiple conditions to provide defense-in-depth. These conditions might include strong factor authentication, device compliance, location, and others. Enabling these conditions protects your organization against user identity compromise or token theft. Global Secure Access introduces the concept of a compliant network within Microsoft Entra ID Conditional Access. This compliant network check ensures users connect through the Global Secure Access service for their specific tenant and are compliant with security policies enforced by administrators.

By using the Global Secure Access client installed on devices or users behind configured remote networks, administrators can secure resources behind a compliant network by using advanced Conditional Access controls. This compliant network feature makes it easier for administrators to manage access policies without having to maintain a list of egress IP addresses. It also removes the requirement to hairpin traffic through your organization's VPN to maintain source IP anchoring and apply IP-based Conditional Access policies. For more information, see [What is Conditional Access?](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)

## Compliant network check enforcement
Compliant network enforcement reduces the risk of token theft and replay attacks. Microsoft Entra ID performs authentication plane enforcement at the time of user authentication. If an adversary steals a session token and attempts to replay it from a device that isn't connected to your organization's compliant network (for example, by requesting an access token with a stolen refresh token), Microsoft Entra ID immediately denies the request and blocks further access. Data plane enforcement works with services integrated with Global Secure Access that support Continuous Access Evaluation (CAE), such as Microsoft Graph. By using apps that support CAE, stolen access tokens that are replayed outside your tenant's compliant network are rejected by the application in near-real time. Without CAE, a stolen access token remains valid for its full lifetime (default is between 60 and 90 minutes).  

This compliant network check is specific to the tenant in which you configure it. For example, if you define a Conditional Access policy requiring compliant network in contoso.com, only users with Global Secure Access or with the Remote Network configuration can pass this control. A user from fabrikam.com can't pass contoso.com's compliant network policy.

The compliant network is different from [IPv4, IPv6, or geographic locations](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-assignment-network) you might configure in Microsoft Entra. Administrators don't need to review and maintain compliant network IP addresses or ranges, which strengthens the security posture and minimizes the administrative overhead. 

## Prerequisites

- Administrators who interact with **Global Secure Access** features must have one or more of the following role assignments depending on the tasks they're performing:
   - The [Global Secure Access Administrator](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference) role to manage the Global Secure Access features.
   - The [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) role to enable Global Secure Access signaling for Conditional Access, and to create and interact with Conditional Access policies and named locations.
- The product requires licensing. For details, see the licensing section of [What is Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).

### Known limitations

For detailed information about known issues and limitations, see [Known limitations for Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-current-known-limitations).

## Enable Global Secure Access signaling for Conditional Access

To enable the setting that allows the compliant network check, an administrator must take the following steps.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) with an account that has the [Global Secure Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator) and [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) roles activated.
1. Browse to **Global Secure Access** > **Settings** > **Session management** > **Adaptive access**.
1. Select the toggle to **Enable Conditional Access Signaling for Microsoft Entra ID**.

     
 
1. Browse to **Entra ID** > **Conditional Access** > **Named locations**.
   1. Confirm you have a location called **All Compliant Network locations** with location type **Network Access**. You can optionally mark this location as trusted.

> [!CAUTION]
> If your organization has active Conditional Access policies based on compliant network check, and you later disable Global Secure Access signaling in Conditional Access, you might unintentionally block targeted end users from accessing the resources. If you must disable this feature, first delete any corresponding Conditional Access policies.

## Protect your resources behind the compliant network

Use the compliant network Conditional Access policy to protect your Microsoft and third-party applications that use Microsoft Entra ID single sign-on. A typical policy blocks all network locations except compliant networks. The following example shows how to configure this policy type:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access**.
1. Select **Create new policy**.
1. Enter a name for your policy. Create a meaningful standard for the names of your policies for your organization.
1. Under **Assignments**, select **Users or workload identities**.
   1. Under **Include**, select **All users**.
   1. Under **Exclude**, select **Users and groups** and choose your organization's [emergency access or break-glass accounts](#user-exclusions).
1. Under **Target resources** > **Include**, select **All resources (formerly 'All cloud apps')**.
   1. If your organization enrolls devices into Microsoft Intune, exclude the applications **Microsoft Intune Enrollment** and **Microsoft Intune** from your Conditional Access policy to avoid a circular dependency.
1. Under **Network**:
   1. Set **Configure** to **Yes**.
   1. Under **Include**, select **Any location**.
   1. Under **Exclude**, select the **All Compliant Network locations** location.
1. Under **Access controls**:
   1. **Grant**, select **Block Access**, and select **Select**.
1. Confirm your settings and set **Enable policy** to **On**.
1. Select **Create** to enable your policy.

> [!NOTE]
> Use Global Secure Access along with Conditional Access policies that require a Compliant Network for *All Resources*.
> 
> Global Secure Access resources are automatically excluded from the Conditional Access policy when *Compliant Network* is enabled in the policy. There's no explicit resource exclusion required. These automatic exclusions are required to ensure the Global Secure Access client isn't blocked from accessing the resources it needs. The resources Global Secure Access needs are:
> * Global Secure Access Traffic Profiles 
> * Global Secure Access Policy Service (internal service)
>
> Sign-in events for authentication of excluded Global Secure Access resources appear in the Microsoft Entra ID sign-in logs as: 
> * Internet resources with Global Secure Access 
> * Microsoft apps with Global Secure Access 
> * All private resources with Global Secure Access 
> * ZTNA Policy Service

### Mobile app support

The Global Secure Access mobile app is part of the Defender app. You need to add exclusions to make sure the Defender client can access the resources it needs. To exclude Defender resources from Conditional Access policies, see [Microsoft Defender mobile app exclusion from Conditional Access policies](https://learn.microsoft.com/en-us/defender-endpoint/mobile-resources-defender-endpoint#microsoft-defender-mobile-app-exclusion-from-conditional-access-ca-policies).

For more information, see [Mobile resources for Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/mobile-resources-defender-endpoint).

### User exclusions

Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
   - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
   - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## Try your compliant network policy

1. On an end-user device with the [Global Secure Access client installed and running](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-install-windows-client), browse to [https://myapps.microsoft.com](https://myapps.microsoft.com) or any other application that uses Microsoft Entra ID single sign-on in your tenant.
1. Pause the Global Secure Access client by right-clicking the application in the Windows tray and selecting **Disable**.
1. After disabling the Global Secure Access client, access another application integrated with Microsoft Entra ID single sign-on. For example, you can try signing in to the Azure portal. Microsoft Entra ID Conditional Access blocks your access.

> [!NOTE]
> If you're already signed in to an application, access isn't interrupted. Microsoft Entra ID evaluates the Compliant Network condition. If you're already signed in, you might have an existing session with the application. In this scenario, Microsoft Entra ID reevaluates the Compliant Network check the next time sign-in is required, when your application session expires.
> 

## Next steps

[Universal Tenant Restrictions](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-universal-tenant-restrictions)
