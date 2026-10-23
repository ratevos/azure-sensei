# Check Workflow Insights

> Source: https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-insights  
> Microsoft doc last updated: 03/12/2026


With Workflow Insights, you're able to get a quick view of workflow execution within your environment. With Workflow Insights, you can view information such as:

- Numerical summaries of all successful workflows, users processed, and successful tasks that ran in your environment.
- The top workflows of the past time-span that you define from either 7, 14, or 30 days.
- The top tasks of the past time-span that you define from either 7, 14, or 30 days.
- Number of workflows by categories of the past time-span that you define from either 7, 14, or 30 days.

For more information, see: [Workflow Insights](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-insights).

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Check Workflow Insights using the Microsoft Entra admin center

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Overview**. 

1. On the overview page, select **Workflow Insights**.

1. On the Workflow Insights page, you're able to view workflow information across your environment.

1. When you find the information you want to look further into, you can select the **filter** option and choose which time frame you want to view information from.

1. Along with being able to filter on a time period, for top workflows and tasks, you're also able to filter based on activity.

   

1. With the activity filter, you can choose to see the top processed workflows or tasks by choosing **Total Processed**, only those which were **Successful**, or only the ones that **Failed**.

1. Under **Workflow Runs by Category** you can filter workflows by category. You can filter to see the percentage of workflows **Total Processed**, **Successful** workflows by category, or **Failed** workflows by category.

   

## Next step

> [Manage workflow versions](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks)
