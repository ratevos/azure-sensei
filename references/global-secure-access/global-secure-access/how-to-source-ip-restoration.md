# Enable Source IP Restoration with Global Secure Access

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-source-ip-restoration  
> Microsoft doc last updated: 04/03/2026

When you use cloud-based network proxy and SSE solutions, they abstract the original source IP of the user from the service that the user connects to. Instead, the service detects the user's IP address as the egress address of the cloud-based network proxy. While this abstraction helps with privacy-related concerns in consumer scenarios, not having the original source IP information makes it difficult to achieve enterprise security goals. For example, without an actual client egress IP address, you can't apply Microsoft Entra ID Conditional Access policies based on your organization's well-known IP addresses, and audit logs don't reflect accurate location information.

Source IP restoration is part of the Adaptive Access feature of Microsoft Entra Internet Access for Microsoft Services. Source IP restoration detects and securely communicates the original egress IP address of the end user to Microsoft Entra ID and Microsoft Graph, bringing the following benefits to your organization:

- You can continue to enforce IP-based location policies in [Microsoft Entra ID Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview).
- It improves the accuracy of risk detection in [Microsoft Entra ID Protection risk detections](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks).
- It elevates your threat detection and response by recording accurate source IP in [Microsoft Entra sign-in logs](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-all-sign-ins) and in [Microsoft Entra audit logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs).

## Prerequisites

- Administrators who configure source IP restoration settings must have one of the following role assignments:
   - The [Global Secure Access Administrator role](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference)
   - The [Global Administrator role](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference)
- The product requires Microsoft Entra ID P1 licenses. For details, see the licensing section of [What is Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).
- You must enable the [Microsoft Traffic Profile](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-microsoft-traffic-profile) to use source IP restoration.

### Known limitations

For detailed information about known issues and limitations, see [Known limitations for Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-current-known-limitations).

<a name="enable-global-secure-access-signaling-for-conditional-access"></a>
## Enable Global Secure Access signaling for Microsoft Entra ID and Microsoft Graph

> [!NOTE]
> Source IP restoration is now enabled by default for new tenants. If you enabled Global Secure Access features in your tenant before June 2025, you might need to explicitly enable source IP restoration.

To enable the required setting to allow source IP restoration, an administrator must take the following steps.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a [Global Secure Access Administrator](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#global-secure-access-administrator).
1. Browse to **Global Secure Access** > **Settings** > **Session management** > **Adaptive Access**.
1. Select the toggle to **Enable Conditional Access Signaling for Microsoft Entra ID**.

By using this functionality, Microsoft Entra ID and Microsoft Graph receive the public egress source IP address of the user.

> [!CAUTION]
> If you create Conditional Access policies based on IP location checks, and you disable Global Secure Access signaling, you might unintentionally block targeted end users from accessing the resources. If you must disable this feature, first delete any corresponding Conditional Access policies.

## Sign-in log behavior

To see source IP restoration in action, administrators can take the following steps.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Security Reader](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#security-reader).
1. Browse to **Entra ID** > **Users** > select one of your test users > **Sign-in logs**.
1. When you enable source IP restoration, you see IP addresses that include the user's actual IP address.
   - When you disable source IP restoration, you can't see the user's actual IP address.

Sign-in log data might take some time to appear. This delay is normal because the data undergoes some processing before it appears.

## Related content

- [Enable compliant network check with Conditional Access](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-compliant-network)
- [Microsoft Traffic Profile](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-microsoft-traffic-profile)
