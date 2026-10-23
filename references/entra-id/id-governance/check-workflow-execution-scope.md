# Check execution user scope of a workflow - Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/id-governance/check-workflow-execution-scope  
> Microsoft doc last updated: 03/12/2026


Workflow scheduling will automatically process the workflow for users meeting the workflow's execution conditions. This article walks you through the steps to check the users who fall into the execution scope of a workflow. For more information about execution conditions, see: [workflow basics](https://learn.microsoft.com/en-us/entra/id-governance/understanding-lifecycle-workflows#workflow-basics).

## Check execution user scope of a workflow using the Microsoft Entra admin center

To check the users who fall under the execution scope of a workflow, you'd follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. From the list of workflows, select the workflow you want to check the execution scope of.

1. On the workflow overview page, select **Execution conditions**.

1. On the Execution conditions page, select the **Execution User Scope** tab.

1. On this page, you're presented with a list of users who currently meet the scope for execution for the workflow regardless of whether they have already been processed by the workflow.
    

> [!NOTE]
> The workflow engine currently has a retroactive window that allows workflows to run for users who previously met the conditions for the workflow. For more information on this window, see: [Lifecycle workflow catch-up window](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-execution-conditions#lifecycle-workflow-catch-up-window).

## Check execution user scope of a workflow using Microsoft Graph

To check execution user scope of a workflow using API via Microsoft Graph, see: [List executionScope](https://learn.microsoft.com/en-us/graph/api/workflow-list-executionscope).

## Next steps

- [Manage workflow properties](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-properties)
- [Delete Lifecycle Workflows](https://learn.microsoft.com/en-us/entra/id-governance/delete-lifecycle-workflow)
