# Download workflow history reports

> Source: https://learn.microsoft.com/en-us/entra/id-governance/download-workflow-history  
> Microsoft doc last updated: 03/12/2026


The Lifecycle Workflows history feature allows you to view details about the actions of a workflow such as when it runs, processes a task, or processes a user. From the Microsoft Entra admin center, you're able to filter this information up to 30 days from when the action was taken. To store this information for a longer period of time, you can save the history as a CSV report. This article walks you through how you can download these reports.

## Download the history report of a workflow by using the Microsoft Entra admin center

To download the history report of a workflow by using the Microsoft Entra admin center, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. Select the workflow you want to download the history of.

1. On the workflow overview screen, select **Workflow history** under the **Activity** bar on the left.

1. The Workflow history screen shows the history of a workflow from the view of Users, runs, and Tasks. For more information on workflow history, see [Lifecycle Workflows history](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-history).
    
1. On the workflow history page that you want to download a report of, the applied filters are included in your report. When these selected filters match what you want in your report, select **Download**.
    
1. On the download pane, you see the type of report you're downloading at the top, and it's also present in the default name of the CSV report.
   
    
1. Select **Download**.
 
> [!NOTE]
> You can download up to 100,000 records in a report. If you want to download more, use the [Lifecycle Workflow reporting API](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-lifecycleworkflows-reporting-overview).

## Next steps

- [Check the status of a workflow](https://learn.microsoft.com/en-us/entra/id-governance/check-status-workflow)
- [Lifecycle Workflows history](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-history)
