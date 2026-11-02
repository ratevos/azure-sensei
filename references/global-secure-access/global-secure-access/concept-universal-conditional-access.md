# Learn about Universal Conditional Access Through Global Secure Access

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/concept-universal-conditional-access  
> Microsoft doc last updated: 03/12/2026


## Overview

In addition to sending traffic to Global Secure Access, administrators can use Conditional Access policies to secure traffic profiles. They can mix and match controls as needed like requiring multifactor authentication, requiring a compliant device, or defining an acceptable sign-in risk. Applying these controls to network traffic not just cloud applications allows for universal Conditional Access.

Conditional Access on traffic profiles provides administrators with enormous control over their security posture. Administrators can enforce [Zero Trust principles](https://learn.microsoft.com/en-us/security/zero-trust/) using policy to manage access to the network. Using traffic profiles allows consistent application of policy. For example, applications that don't support modern authentication can now be protected behind a traffic profile.

This functionality allows administrators to consistently enforce Conditional Access policy based on [traffic profiles](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding), not just applications or actions. Administrators can target specific traffic profiles - the Microsoft traffic profile, private resources, and internet access with these policies. Users can access these configured endpoints or traffic profiles only when they satisfy the configured Conditional Access policies. 

## Prerequisites

* Administrators who interact with **Global Secure Access** features must have one or more of the following role assignments depending on the tasks they're performing.
   * The [Global Secure Access Administrator role](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference) role to manage the Global Secure Access features.
   * The [Conditional Access Administrator](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#conditional-access-administrator) to create and interact with Conditional Access policies.
* The product requires licensing. For details, see the licensing section of [What is Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).

### Known tunnel authorization limitations

Both the Microsoft and Internet access forwarding profiles use Microsoft Entra ID Conditional Access policies to authorize access to their tunnels in the Global Secure Access Client. This means that you can Grant or Block access to the Microsoft traffic and Internet access forwarding profiles in Conditional Access. In some cases when authorization to a tunnel isn't granted, the recovery path to regain access to resources requires accessing destinations on either the Microsoft traffic or Internet access forwarding profile, locking a user out from accessing anything on their machine.

One example is if you block access to the Internet access target resource on noncompliant devices, you leave Microsoft Entra Internet Access users unable to bring their devices back to compliance. The way to mitigate this issue is bypassing [Network endpoints for Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/fundamentals/intune-endpoints) and any other destinations accessed in [Custom compliance discovery scripts for Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/protect/compliance-custom-script). You can perform this operation as part of custom bypass in the [Internet access forwarding profile](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding).

### Other known limitations

For detailed information about known issues and limitations, see [Known limitations for Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-current-known-limitations).

## Conditional Access policies

With Conditional Access, you can enable access controls and security policies for the network traffic acquired by Microsoft Entra Internet Access and Microsoft Entra Private Access. 

- Create a policy that targets all [Microsoft traffic](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-microsoft-profile).
- Apply Conditional Access policies to your [Private Access apps](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-private-access-apps), such as Quick Access.
- Enable [Global Secure Access source IP restoration](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-source-ip-restoration) so the source IP address is visible in the appropriate logs and reports.

## Internet Access flow diagram

The following example demonstrates how Microsoft Entra Internet Access works when you apply Universal Conditional Access policies to network traffic.

> [!NOTE]
> Microsoft's Security Service Edge solution comprises three tunnels: Microsoft traffic, Internet Access, and Private Access. Universal Conditional Access applies to the Internet Access and Microsoft traffic tunnels. There isn't support to target the Private Access tunnel. You must individually target Private Access Enterprise Applications.

The following flow diagram illustrates Universal Conditional Access targeting internet resources and Microsoft apps with Global Secure Access.

|Step|Description|
|-----|-----|
|1|The Global Secure Access client attempts to connect to Microsoft's Security Service Edge solution.|
|2|The client redirects to Microsoft Entra ID for authentication and authorization.|
|3|The user and the device authenticate. Authentication happens seamlessly when the user has a valid Primary Refresh Token.|
|4|After the user and device authenticate, Universal Conditional Access policy enforcement occurs. Universal Conditional Access policies target the established Microsoft and internet tunnels between the Global Secure Access client and Microsoft Security Service Edge.|
|5|Microsoft Entra ID issues the access token for the Global Secure Access client.|
|6|The Global Secure Access client presents the access token to Microsoft Security Service Edge. The token validates.|
|7|Tunnels establish between the Global Secure Access client and Microsoft Security Service Edge.|
|8|Traffic starts being acquired and tunneled to the destination via the Microsoft and Internet Access tunnels.|

> [!NOTE]
> Target Microsoft apps with Global Secure Access to protect the connection between the Microsoft Security Service Edge and the Global Secure Access client. To ensure that users can't bypass the Microsoft Security Service Edge service, create a Conditional Access policy that requires compliant network for your Microsoft 365 Enterprise applications.

## User experience

When users sign in to a machine with the Global Secure Access Client installed, configured, and running for the first time they're prompted to sign in. When users attempt to access a resource protected by a policy. Like the previous example, the policy is enforced and they're prompted to sign in if they haven't already. Looking at the system tray icon for the Global Secure Access Client you see a red circle indicating it's signed out or not running.

When a user signs in the Global Secure Access Client has a green circle that you're signed in, and the client is running.

## Next steps

- [Enable source IP restoration](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-source-ip-restoration)
- [Create a Conditional Access policy for Microsoft traffic](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-microsoft-profile)
- [Create a Conditional Access policy for Private Access apps](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-private-access-apps)
