# Disable access to Exchange Web Services

> Source: https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-access-exchange-web-services  
> Microsoft doc last updated: 03/25/2026


Exchange Web Services (EWS) provides cross platform API access to sensitive Exchange Online data such as emails, calendar items, and contacts. If EWS is not restricted, apps or scripts can programmatically access this data, increasing the risk of unauthorized exposure. Blocking EWS across your organization helps prevent attackers from using it to exfiltrate data, send phishing messages, or spoof identities.

If you have enabled this setting but need to revert to the default behavior (allow users to access EWS), you can turn this setting off directly in the Microsoft 365 admin center.

## Why this setting matters

EWS has historically been used by legacy applications and custom integrations. However, it also represents a common attack vector because it allows broad programmatic access to mailbox data. Compromised accounts or malicious apps can use EWS to read mail, access contacts, send messages, or perform automated actions without user interaction. Enforcing this setting significantly reduces your risk by preventing unauthorized or outdated apps from reaching sensitive Exchange data. You can still allow exceptions for specific users or workloads using Exchange Online PowerShell.

You can also generate a CSV report to identify which apps are making EWS requests, how frequently they access EWS, and the extent of your organization’s dependency on EWS.

> [!NOTE]
> Usage data is collected and aggregated weekly, not daily.

For a list of Microsoft first-party client application IDs, see [Commonly used Microsoft first-party services and portal apps](https://learn.microsoft.com/en-us/power-platform/admin/apps-to-allow). For Microsoft applications, Microsoft updates those periodically to remove EWS dependencies. We recommend that you keep your client applications up-to-date. If you still can't find the Application ID, check your Enterprise Applications in Entra ID. For more information, see [Quickstart: View enterprise applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/view-applications-portal).

For more information, see [Control access to EWS in Exchange](https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-control-access-to-ews-in-exchange).
