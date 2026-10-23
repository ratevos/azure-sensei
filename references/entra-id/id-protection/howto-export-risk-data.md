# Export and use Microsoft Entra ID Protection data

> Source: https://learn.microsoft.com/en-us/entra/id-protection/howto-export-risk-data  
> Microsoft doc last updated: 09/30/2025


Microsoft Entra ID stores reports and security signals for a defined period of time. When it comes to risk information, that period might not be long enough.

| Report / Signal | Microsoft Entra ID Free | Microsoft Entra ID P1 | Microsoft Entra ID P2 |
| --- | --- | --- | --- |
| Audit logs | 7 days | 30 days | 30 days |
| Sign-ins | 7 days | 30 days | 30 days |
| Microsoft Entra multifactor authentication usage | 30 days | 30 days | 30 days |
| Risky sign-ins | 7 days | 30 days | 30 days |

This article describes the available methods for exporting risk data from Microsoft Entra ID Protection for long-term storage and analysis.

## Prerequisites

To export risk data for storage and analysis, you need:

- An Azure subscription to create a Log Analytics workspace, Azure event hub, or Azure storage account. If you don't have an Azure subscription, you can [sign up for a free trial](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- The [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) role is the least privileged role required to **configure diagnostic settings for the Microsoft Entra tenant**.

## Diagnostic settings

Organizations can choose to store or export **RiskyUsers**, **UserRiskEvents**, **RiskyServicePrincipals**, **ServicePrincipalRiskEvents**, **RiskyAgents**, and **AgentRiskEvents** data by configuring diagnostic settings in Microsoft Entra ID to export the data. You can integrate the data with a Log Analytics workspace, archive data to a storage account, stream data to an event hub, or send data to a partner solution.

The endpoint you select for exporting the logs must be set up before you can configure diagnostic settings. For a quick summary of the methods available for log storage and analysis, see [How to access activity logs in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs). 

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator).

1. Browse to **Entra ID** > **Monitoring & health** > **Diagnostic settings**.

1. Select **+ Add diagnostic setting**.

1. Enter a **Diagnostic setting name**, select the log categories that you want to stream, select a previously configured destination, and select **Save**.

[](./media/howto-export-risk-data/change-diagnostic-setting-in-portal.png#lightbox)

You might need to wait around 15 minutes for the data to start appearing in the destination you selected. For more information, see [How to configure Microsoft Entra diagnostic settings](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-configure-diagnostic-settings). 

## Log Analytics

Integrating risk data with Log Analytics provides robust data analysis and visualization capabilities. The high-level process for using Log Analytics to analyze risk data is as follows:

1. [Create a Log Analytics workspace](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/tutorial-configure-log-analytics-workspace).
1. [Configure Microsoft Entra diagnostic settings to export the data](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-configure-diagnostic-settings).
1. [Query the data in Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries).

You need to configure a Log Analytics workspace before you can export and then query the data. Once you configured a Log Analytics workspace and exported the data with diagnostic settings, go to [Microsoft Entra admin center](https://entra.microsoft.com) > **Entra ID** > **Monitoring & health** > **Log Analytics**. Then, with Log Analytics, you can query data using built-in or custom Kusto queries.

> [!IMPORTANT]
> The names you select in **diagnostic settings** are not the same as the **table names** you use in Kusto (KQL) queries.
> - **Diagnostic setting category** = what you enable for export
> - **Log Analytics table name** = what you query (usually prefixed with `AAD`)

### Diagnostic setting categories vs Log Analytics table names

Use this mapping when you enable export and when you write queries:

| Report / signal | Diagnostic setting category (enable export) | Log Analytics table name (use in queries) | Table reference |
| --- | --- | --- | --- |
| Risky users | `RiskyUsers` | `AADRiskyUsers` | [AADRiskyUsers](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aadriskyusers) |
| Risk detections (users) | `UserRiskEvents` | `AADUserRiskEvents` | [AADUserRiskEvents](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aaduserriskevents) |
| Risky workload identities | `RiskyServicePrincipals` | `AADRiskyServicePrincipals` | [AADRiskyServicePrincipals](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aadriskyserviceprincipals) |
| Workload identity detections | `ServicePrincipalRiskEvents` | `AADServicePrincipalRiskEvents` | [AADServicePrincipalRiskEvents](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aadserviceprincipalriskevents) |
| Risky agents | `RiskyAgents` | `AADRiskyAgents` | [AADRiskyAgents](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aadriskyagents) |
| Agent identity detections | `AgentRiskEvents` | `AADAgentRiskEvents` | [AADAgentRiskEvents](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aadagentriskevents) |

> [!NOTE]
> Log Analytics only has visibility into data as it is streamed. Events prior to enabling the sending of events from Microsoft Entra ID don't appear.

### Sample queries

[](./media/howto-export-risk-data/log-analytics-view-query-user-risk-events.png#lightbox)

In the previous image, the following query was run to show the most recent five risk detections triggered. 

```kusto
AADUserRiskEvents
| take 5
```

Another option is to query the AADRiskyUsers table to see all risky users.

```kusto
AADRiskyUsers
```

View the count of high risk users by day:
 
```kusto
AADUserRiskEvents
| where TimeGenerated > ago(30d)
| where RiskLevel has "high"
| summarize count() by bin (TimeGenerated, 1d)
```

View helpful investigation details, such as user agent string, for detections that are high risk and aren't remediated or dismissed:
 
```kusto
AADUserRiskEvents
| where RiskLevel has "high"
| where RiskState has "atRisk"
| mv-expand ParsedFields = parse_json(AdditionalInfo)
| where ParsedFields has "userAgent"
| extend UserAgent = ParsedFields.Value
| project TimeGenerated, UserDisplayName, Activity, RiskLevel, RiskState, RiskEventType, UserAgent,RequestId
```

Access more queries and visual insights based on AADUserRiskEvents and AADRisky Users logs in the [Impact analysis of risk-based access policies workbook](https://learn.microsoft.com/en-us/entra/id-protection/workbook-risk-based-policy-impact).

### Risk analysis

Organizations can reduce security operations center (SOC) workloads and support overhead with risk-based Conditional Access policies. Learn more in the following video, **Mastering risk analysis with Microsoft Entra ID Protection**.

   > [!VIDEO abb7d7fe-4155-4ee1-bcce-afa027d22f8d]

## Storage account

By routing logs to an Azure storage account, you can keep data for longer than the default retention period.

1. [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create).
1. [Archive Microsoft Entra logs to a storage account](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-archive-logs-to-storage-account).

## Azure Event Hubs

Azure Event Hubs can look at incoming data from sources like Microsoft Entra ID Protection and provide real-time analysis and correlation.

1. [Create an Azure event hub](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create).
1. [Stream Microsoft Entra logs to an event hub](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-stream-logs-to-event-hub).

## Microsoft Sentinel

Organizations can choose to [connect Microsoft Entra data to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors/azure-active-directory-identity-protection) for security information and event management (SIEM) and security orchestration, automation, and response (SOAR).

1. [Create a Log Analytics workspace](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/tutorial-configure-log-analytics-workspace).
1. [Configure Microsoft Entra diagnostic settings to export the data](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-configure-diagnostic-settings).
1. [Connect data sources to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/configure-data-connector).

## Related content

- [Use Microsoft Graph API to programmatically interact with risk events](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-graph-api)
- [Microsoft Entra ID Protection and the Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-graph-api)
- [Overview of Azure partner solutions for diagnostic settings](https://learn.microsoft.com/en-us/azure/partner-solutions/overview)
