# Learn about Global Secure Access Alerts

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/concept-alerts  
> Microsoft doc last updated: 12/08/2025

Global Secure Access alerts provide real-time notifications about potential security issues and operational concerns within your organization's network. Alerts include details about severity, related MITRE techniques, provider information, and related entities.

Alerts provide visibility into activities, threats, and entities of interest such as users, devices, and applications. Alerts offer operational insights to resolve deployment and health issues. They also deliver security insights from detections and related activities, strengthening your overall security posture. 

The Global Secure Access alert structure aligns with the [Microsoft Sentinel security alert schema](https://learn.microsoft.com/en-us/azure/sentinel/security-alert-schema), enabling a smooth integration with [Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender).

With alerts, Global Secure Access admins can:
- View statistics on alert types and severity.
- Investigate alerts and related data by using filters and linked information.
- Export alerts for use with security information and event management (SIEM) tools or other solutions.

## Types of alerts
Global Secure Access includes the following alert types:

### Token/Device Inconsistency alert
You see this alert when the same access token is used on more than one device.

### Increased External Tenant Activity alert
You see this alert when there's an unusual rise in activity with external tenants. This alert looks at a 14-day sliding window, with access to tenants other than the home tenant.

###	Unhealthy Remote Network alert
You see this alert when there are deficiencies in remote network availability. This alert checks hourly for remote network health events like BGPDisconnect or TunnelDisconnect.

### Netskope alerts
The Netskope alerts include:
- **Threat Protection**: You see this alert when Netskope detects malware or suspicious content in traffic.
- **Data Loss Prevention** (DLP): You see this alert when sensitive data matches a DLP profile during inspection.
- **Fallback**: You see this alert when Netskope can't fully process traffic due to technical limitations like file size limits, scan timeouts, or unsupported file types.

> [!IMPORTANT]
> Netskope alerts require the Netskope Advanced Threat Protection (ATP) and DLP modules in Global Secure Access. For more information, see [Netskope's Advanced Threat Protection and Data Loss Prevention](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-netskope-integration).

## View alerts
To view Global Secure Access alerts: 
1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a [Global Secure Access Administrator](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#global-secure-access-administrator).
1. Browse to **Global Secure Access** > **Monitor** > **Alerts**.

You can filter and sort alerts based on severity, date, and type to quickly identify and respond to potential security issues.

You can also view the **Alerts** widget in the [Global Secure Access dashboard](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-dashboard) for a summary of recent alerts.

## Related content
- [Global Secure Access dashboard](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-dashboard)
