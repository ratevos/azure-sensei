# Sign-up logs in Microsoft Entra External ID

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ups  
> Microsoft doc last updated: 06/30/2025


**Applies to**:  External tenants ([learn more](https://learn.microsoft.com/en-us/entra/external-id/tenant-configurations))

Microsoft Entra External ID logs all self-service sign-up events, including both successful sign-ups and failed attempts. The logs include information that helps organizations optimize their sign-up processes, enhance the user experience, and improve overall customer engagement. This article explains how to access and use the sign-up logs.

The sign-up logs provided by Microsoft Entra External ID are a powerful type of [activity log](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health) that you can analyze. In addition to the External ID sign-up logs, three other activity logs are also available to help monitor the health of your external tenant:

- **[Sign-ins](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins)** – Information about sign-ins and how your resources are used by your users.
- **[Audit](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs)** – Information about changes applied to your tenant, such as users and group management or updates applied to your tenant’s resources.
- **[Provisioning](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-provisioning-logs)** – Activities performed by a provisioning service, such as the creation of a group in ServiceNow or a user imported from Workday.

## What can you do with sign-up logs?

You can use the sign-up logs to find the following information:

- The percentage of sign-up attempts that result in account creation.
- The stage in the sign-up process with the highest drop-off rate.
- How drop-off rates compare between social sign-ups and local account sign-ups.

You can also describe the activity associated with a sign-up request by identifying the following details:

- Who performed the sign-up
- When the user performed the sign-up
- How the user signed up (for example, local account or social identity provider)
- What app they accessed to sign up
- Whether the sign-up was successful
- Where an unsuccessful sign-up failed in the sign-up flow
- Whether the user who tried to sign up already had an account  

## Next steps

[Access activity logs using Microsoft Graph](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-analyze-activity-logs-with-microsoft-graph) and query the activity logs for [sign-up activity](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-analyze-activity-logs-with-microsoft-graph#sample-sign-up-queries-preview).
