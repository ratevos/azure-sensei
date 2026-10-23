# Identity protection risk analysis workbook

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/workbook-risk-analysis  
> Microsoft doc last updated: 11/04/2024


Microsoft Entra ID Protection detects, remediates, and prevents compromised identities. As an IT administrator, you want to understand risk trends in your organizations and opportunities for better policy configuration. With the Identity Protection Risky Analysis Workbook, you can answer common questions about your Identity Protection implementation.

This article provides you with an overview of the **Identity Protection Risk Analysis** workbook.

## Prerequisites

To use Azure Workbooks for Microsoft Entra ID, you need:

- A Microsoft Entra tenant with a [Premium P1 license](https://learn.microsoft.com/en-us/entra/fundamentals/get-started-premium)
- A Log Analytics workspace *and* access to that workspace
- The appropriate roles for Azure Monitor *and* Microsoft Entra ID

### Log Analytics workspace

You must create a [Log Analytics workspace](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace) *before* you can use Microsoft Entra Workbooks. several factors determine access to Log Analytics workspaces. You need the right roles for the workspace *and* the resources sending the data.

For more information, see [Manage access to Log Analytics workspaces](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access).

### Azure Monitor roles

Azure Monitor provides [two built-in roles](https://learn.microsoft.com/en-us/azure/azure-monitor/roles-permissions-security#monitoring-reader) for viewing monitoring data and editing monitoring settings. Azure role-based access control (RBAC) also provides two Log Analytics built-in roles that grant similar access.

- **View**:
  - Monitoring Reader
  - Log Analytics Reader

- **View and modify settings**:
  - Monitoring Contributor
  - Log Analytics Contributor

### Microsoft Entra roles
<a name='azure-ad-roles'></a>

Read only access allows you to view Microsoft Entra ID log data inside a workbook, query data from Log Analytics, or read logs in the Microsoft Entra admin center. Update access adds the ability to create and edit diagnostic settings to send Microsoft Entra data to a Log Analytics workspace.

- **Read**:
  - Reports Reader
  - Security Reader
  - Global Reader

- **Update**:
  - Security Administrator

For more information on Microsoft Entra built-in roles, see [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference).

For more information on the Log Analytics RBAC roles, see [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#log-analytics-contributor).

## Description

As an IT administrator, you need to understand trends in identity risks and gaps in your policy implementations, to ensure you're best protecting your organizations from identity compromise. The identity protection risk analysis workbook helps you analyze the state of risk in your organization.

**This workbook:**

- Provides visualizations of where in the world risk is being detected.
- Allows you to understand the trends in real time vs. offline risk detections.
- Provides insight into how effective you are at responding to risky users.

## How to access the workbook

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) using the appropriate combination of roles.

1. Browse to **Entra ID** > **Monitoring & health** > **Workbooks**.

1. Select the **Identity Protection Risk Analysis** workbook from the **Usage** section.

## Workbook sections

This workbook has five sections:

- Heatmap of risk detections
- Offline vs real-time risk detections
- Risk detection trends
- Risky users
- Summary

## Filters

This workbook supports setting a time range filter.

There are more filters in the risk detection trends and risky users sections. 

Risk Detection Trends:

- Detection timing type (real-time or offline)
- Risk level (low, medium, high, or none)

Risky Users:

- Risk detail (which indicates what changed a user’s risk level)
- Risk level (low, medium, high, or none)

## Best practices

- **[Enable risky sign-in policies](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies#sign-in-risk-based-conditional-access-policy)** - To prompt for multifactor authentication (MFA) on medium risk or higher. Enabling the policy reduces the proportion of active real-time risk detections by allowing legitimate users to self-remediate the risk detections with MFA.

- **[Enable a risky user policy](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies#user-risk-policy-in-conditional-access)** - To enable users to securely remediate their accounts when they're considered high risk. Enabling the policy reduces the number of active at-risk users in your organization by returning the user’s credentials to a safe state.

- To learn more about identity protection, see [What is identity protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection). 

- For more information about Microsoft Entra workbooks, see [How to use Microsoft Entra workbooks](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-workbooks).

## Related content

- [How to use the identity workbooks](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-workbooks)
- [What is Microsoft Entra ID Protection?](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection)
- [What are risk detections?](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks)
