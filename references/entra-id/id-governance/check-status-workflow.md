# Check status of a Lifecycle workflow

> Source: https://learn.microsoft.com/en-us/entra/id-governance/check-status-workflow  
> Microsoft doc last updated: 03/12/2026


When a workflow is created, it's important to check its status and run history to make sure it ran properly for the users it processed both by schedule and by on-demand. To get information about the status of workflows, Lifecycle Workflows allows you to check run and user processing history. This history also gives you summaries to see how often a workflow has run, and who it ran successfully for. You're also able to check the status of both the workflow, and its tasks. Checking the status of workflows and their tasks allows you to troubleshoot potential problems that could come up during their execution.

## Run workflow history using the Microsoft Entra admin center

You're able to retrieve run information of a workflow using Lifecycle Workflows. To check the runs of a workflow using the Microsoft Entra admin center, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. Select the workflow whose run history you want to check. 

1. On the workflow overview screen, select **Workflow history**.

1. On the history page, select the **Runs** button.  

1. Here you see a summary of workflow runs.
    
1. The runs summary cards include the total number of processed runs, the number of successful runs, the number of failed runs, and the total number of failed tasks.   

## User workflow history using the Microsoft Entra admin center

To get further information than just the runs summary for a workflow, you're also able to get information about users processed by a workflow. To check the status of users a workflow has processed using the Microsoft Entra admin center, follow these steps:
 
1. In the left menu, select **Lifecycle Workflows**.

1. Select **Workflows**.

1. Select the workflow you want to see user processing information for. 

1. On the workflow overview screen, select **Workflow history**.
    
1. On the workflow history page, you're presented with a summary of every user processed by the workflow along with counts of successful and failed users and tasks.
    
1. By selecting total tasks for a user, you can see which tasks successfully completed, or are currently in progress.
    
1. By selecting failed tasks, you're able to see which tasks failed for a specific user.
    
1. By selecting unprocessed tasks, you're able to see which tasks are unprocessed.
    

## User workflow history using Microsoft Graph

### List user processing results using Microsoft Graph

To view a status list of users processed by a workflow, which are UserProcessingResults, you'd make the following API call:

To view a list of user processing results using API via Microsoft Graph, see: [List userProcessingResults](https://learn.microsoft.com/en-us/graph/api/identitygovernance-workflow-list-userprocessingresults)

### User processing results using Microsoft Graph

To view a summary of user processing results via API using Microsoft Graph, see: [userProcessingResult: summary](https://learn.microsoft.com/en-us/graph/api/identitygovernance-userprocessingresult-summary)

## Run workflow history via Microsoft Graph

### List runs using Microsoft Graph

To view runs of a workflow via API using Microsoft Graph, see: [runs](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-run)

### Get a summary of runs using Microsoft Graph

To view run summary via API using Microsoft Graph, see: [run summary of a lifecycle workflow](https://learn.microsoft.com/en-us/graph/api/identitygovernance-run-summary)

### List user and task processing results of a given run using Microsoft Graph

To get user processing result for a run of a lifecycle workflow via API using Microsoft Graph, see: [Get userProcessingResult (for a run of a lifecycle workflow)](https://learn.microsoft.com/en-us/graph/api/identitygovernance-userprocessingresult-get)

To list task processing results for a user processing result via API using Microsoft Graph, see: [List taskProcessingResults (for a userProcessingResult)](https://learn.microsoft.com/en-us/graph/api/identitygovernance-userprocessingresult-list-taskprocessingresults)

> [!NOTE]
> A workflow must have activity in the past 7 days to get **userProcessingResults ID**. If there isn't any activity in that time-frame, the **userProcessingResults** call returns no value.

## Next steps

- [Manage workflow versions](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks)
- [Download workflow history reports](https://learn.microsoft.com/en-us/entra/id-governance/download-workflow-history)
