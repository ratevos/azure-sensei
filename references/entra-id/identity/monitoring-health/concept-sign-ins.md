# Sign-in logs in Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins  
> Microsoft doc last updated: 11/07/2025


Microsoft Entra logs all sign-ins into a Microsoft Entra tenant, which includes your internal apps and resources. As an IT administrator, you need to know what the sign-in log details mean, so that you can interpret the log values correctly.

Reviewing sign-in errors and patterns provides valuable insight into how your users access applications and services. The sign-in logs provided by Microsoft Entra ID are a powerful type of [activity log](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health) that you can analyze. This article describes several key aspects of the sign-in logs.

Three other activity logs are also available to help monitor the health of your tenant:

- **[Audit](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs)** – Information about changes applied to your tenant, such as users and group management or updates applied to your tenant’s resources.
- **[Sign-ups (preview)](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ups)** - For [external tenants](https://learn.microsoft.com/en-us/entra/external-id/tenant-configurations) only, information about all self-service sign-up attempts, including successful sign-ups and failed attempts.
- **[Provisioning](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-provisioning-logs)** – Activities performed by a provisioning service, such as the creation of a group in ServiceNow or a user imported from Workday.

## What can you do with sign-in logs?

You can use the sign-in logs to answer questions such as:

- How many users signed into a particular application this week?
- How many failed sign-in attempts occurred in the last 24 hours?
- Are users signing in from specific browsers or operating systems?
- Which of my Azure resources were accessed by managed identities and service principals?

You can also describe the activity associated with a sign-in request by identifying the following details:

- **Who** – The identity (User) performing the sign-in.
- **How** – The client (Application) used for the sign-in.  
- **What** – The target (Resource) accessed by the identity.

> [!NOTE]
> Entries in the sign-in logs are system generated and can't be changed or deleted.

## How do you access the sign-in logs?

There are several ways to access the logs, depending on your needs. For more information, see [How to access activity logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-access-activity-logs).

To view the sign-in logs from the Microsoft Entra admin center:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).
1. Browse to **Entra ID** > **Monitoring & health** > **Sign-in logs**.

To more effectively use the sign-in logs in the Microsoft Entra admin center, adjust the filters to only view a specific set of logs. For more information, see [Filter sign-in logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-customize-filter-logs).

## What are the types of sign-in logs?

There are four types of logs in the sign-in logs preview:

- [Interactive user sign-ins](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-interactive-sign-ins)
- [Non-interactive user sign-ins](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-noninteractive-sign-ins)
- [Service principal sign-ins](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-service-principal-sign-ins)
- [Managed identity sign-ins](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-managed-identity-sign-ins)

The legacy sign-in logs experience only includes interactive user sign-ins.

### Agent logs

Agent activity logs are a new log type in our audit and sign-in logs to help you monitor agent related activities. IT administrators can view and manage agent activity directly in the Microsoft Entra admin center and using the Microsoft Graph API. For more information, see [Microsoft Entra Agent ID logs](https://learn.microsoft.com/en-us/entra/agent-id/identity-professional/sign-in-audit-logs-agents).

## Sign-in data used by other services

Sign-in data is used by several services in Azure and Microsoft Entra to monitor risky sign-ins, provide insight into application usage, and more. 

### Microsoft Entra ID Protection
<a name='azure-ad-identity-protection'></a>

Sign-in log data visualization that relates to risky sign-ins is available in the **Microsoft Entra ID Protection** overview, which uses the following data:

- Risky users
- Risky user sign-ins
- Risky workload identities

For more information about the Microsoft Entra ID Protection tools, see the [Microsoft Entra ID Protection overview](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection).

### Microsoft Entra Usage and insights
<a name='azure-ad-usage-and-insights'></a>

To view application-specific sign-in data, browse to **Microsoft Entra ID** > **Monitoring & health** > **Usage & insights**. These reports provide a closer look at sign-ins for Microsoft Entra application activity and AD FS application activity. For more information, see [Microsoft Entra Usage & insights](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-usage-insights-report).

There are several reports available in **Usage & insights**. Some of these reports are in preview.

- Microsoft Entra application activity (preview)
- AD FS application activity
- Authentication methods activity
- Service principal sign-in activity
- Application credential activity

### Microsoft 365 activity logs

You can view Microsoft 365 activity logs from the [Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/admin-overview/admin-center-overview). Microsoft 365 activity and Microsoft Entra activity logs share a significant number of directory resources. Only the Microsoft 365 admin center provides a full view of the Microsoft 365 activity logs.

You can access the Microsoft 365 activity logs programmatically by using the [Office 365 Management APIs](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-apis-overview).
