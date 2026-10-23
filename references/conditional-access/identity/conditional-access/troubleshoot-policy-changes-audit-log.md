# Troubleshoot Conditional Access policy changes

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-policy-changes-audit-log  
> Microsoft doc last updated: 03/24/2026


## Overview

The Microsoft Entra audit log is a valuable source of information when troubleshooting why and how Conditional Access policy changes happened in your environment.

Audit log data is kept for 30 days by default, which might not be enough for every organization. Organizations can store data longer by changing diagnostic settings in Microsoft Entra ID to:

- Send data to a Log Analytics workspace
- Archive data to a storage account
- Stream data to Event Hubs
- Send data to a partner solution

Find these options under **Entra ID** > **Monitoring & health** > **Diagnostic settings** > **Edit setting**. If you don't have a diagnostic setting, see [Create diagnostic settings to send platform logs and metrics to different destinations](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings) for instructions to create one.

## Use the audit log

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).
1. Browse to **Entra ID** > **Monitoring & health** > **Audit logs**.
1. Select the **Date** range to query.
1. From the **Service** filter, select **Conditional Access** and select the **Apply** button.

   By default, the audit logs display all activities. Use the **Activity** filter to narrow down the activities. For a full list of the audit log activities for Conditional Access, see the [Audit log activities](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-audit-activities#conditional-access).

1. Select a row to view the details. The **Modified Properties** tab lists the modified JSON values for the selected audit activity.

## Use Log Analytics

Log Analytics lets organizations query data using built-in queries or custom-created Kusto queries. For more information, see [Get started with log queries in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries).

After enabling it, find Log Analytics in **Entra ID** > **Monitoring & health** > **Log Analytics**. The table most relevant to Conditional Access administrators is **AuditLogs**.

```kusto
AuditLogs 
| where OperationName == "Update Conditional Access policy"
```

Find changes under **TargetResources** > **modifiedProperties**.

## Reading the values

The old and new values from the audit log and Log Analytics are in JSON format. Compare the two values to identify changes to the policy.

Old policy example:

```json
{
    "conditions": {
        "applications": {
            "applicationFilter": null,
            "excludeApplications": [
            ],
            "includeApplications": [
                "797f4846-ba00-4fd7-ba43-dac1f8f63013"
            ],
            "includeAuthenticationContextClassReferences": [
            ],
            "includeUserActions": [
            ]
        },
        "clientAppTypes": [
            "browser",
            "mobileAppsAndDesktopClients"
        ],
        "servicePrincipalRiskLevels": [
        ],
        "signInRiskLevels": [
        ],
        "userRiskLevels": [
        ],
        "users": {
            "excludeGroups": [
                "eedad040-3722-4bcb-bde5-bc7c857f4983"
            ],
            "excludeRoles": [
            ],
            "excludeUsers": [
            ],
            "includeGroups": [
            ],
            "includeRoles": [
            ],
            "includeUsers": [
                "All"
            ]
        }
    },
    "displayName": "Common Policy - Require MFA for Azure management",
    "grantControls": {
        "builtInControls": [
            "mfa"
        ],
        "customAuthenticationFactors": [
        ],
        "operator": "OR",
        "termsOfUse": [
            "a0d3eb5b-6cbe-472b-a960-0baacbd02b51"
        ]
    },
    "id": "334e26e9-9622-4e0a-a424-102ed4b185b3",
    "modifiedDateTime": "2021-08-09T17:52:40.781994+00:00",
    "state": "enabled"
}

```

Updated policy example:

```json
{
    "conditions": {
        "applications": {
            "applicationFilter": null,
            "excludeApplications": [
            ],
            "includeApplications": [
                "797f4846-ba00-4fd7-ba43-dac1f8f63013"
            ],
            "includeAuthenticationContextClassReferences": [
            ],
            "includeUserActions": [
            ]
        },
        "clientAppTypes": [
            "browser",
            "mobileAppsAndDesktopClients"
        ],
        "servicePrincipalRiskLevels": [
        ],
        "signInRiskLevels": [
        ],
        "userRiskLevels": [
        ],
        "users": {
            "excludeGroups": [
                "eedad040-3722-4bcb-bde5-bc7c857f4983"
            ],
            "excludeRoles": [
            ],
            "excludeUsers": [
            ],
            "includeGroups": [
            ],
            "includeRoles": [
            ],
            "includeUsers": [
                "All"
            ]
        }
    },
    "displayName": "Common Policy - Require MFA for Azure management",
    "grantControls": {
        "builtInControls": [
            "mfa"
        ],
        "customAuthenticationFactors": [
        ],
        "operator": "OR",
        "termsOfUse": [
        ]
    },
    "id": "334e26e9-9622-4e0a-a424-102ed4b185b3",
    "modifiedDateTime": "2021-08-09T17:52:54.9739405+00:00",
    "state": "enabled"
}

```

In the previous example, the updated policy doesn't include terms of use in the grant controls.

## Related content

- [What is Microsoft Entra monitoring?](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- Learn how to [install and use the log analytics views for Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-view-designer-conversion-overview).
