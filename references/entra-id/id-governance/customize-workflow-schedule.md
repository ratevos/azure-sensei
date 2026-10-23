# Customize a workflow schedule

> Source: https://learn.microsoft.com/en-us/entra/id-governance/customize-workflow-schedule  
> Microsoft doc last updated: 03/12/2026


When you create workflows by using lifecycle workflows, you can fully customize them to match the schedule that fits your organization's needs. By default, workflows are scheduled to run every 3 hours. But you can set the interval to be as frequent as 1 hour or as infrequent as 24 hours.

## Customize the schedule of workflows by using the Microsoft Entra admin center

Workflows that you create within lifecycle workflows follow the same schedule that you define on the **Workflow settings** pane. To adjust the schedule, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows**.

1. On the **Lifecycle workflows** overview page, select **Workflow settings**.

1. On the **Workflow settings** pane, set the schedule of workflows as an interval of 1 to 24.

   
1. Select **Save**.

## Customize the schedule of workflows by using Microsoft Graph

To schedule workflow settings by using the Microsoft Graph API, see [`lifecycleManagementSettings` resource type](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-lifecyclemanagementsettings).

## Next steps

- [Manage workflow properties](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-properties)
- [Delete lifecycle workflows](https://learn.microsoft.com/en-us/entra/id-governance/delete-lifecycle-workflow)
