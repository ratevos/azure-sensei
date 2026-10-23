# Create a lifecycle workflow - Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/id-governance/create-lifecycle-workflow  
> Microsoft doc last updated: 08/21/2026


Lifecycle workflows allow for tasks associated with the lifecycle process to be run automatically for users as they move through their lifecycle in your organization. Workflows consist of:

- **Tasks**: Actions taken when a workflow is triggered.
- **Execution conditions**: The who and when of a workflow. These conditions define which users this workflow should run against, and when (trigger) the workflow should run.

In the Microsoft Entra admin center, you can create and customize workflows for common scenarios by using built-in templates or by cloning an existing workflow. To build a workflow from scratch without using a template or an existing workflow, use Microsoft Graph.

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Create a lifecycle workflow by cloning an existing workflow in the Microsoft Entra admin center

You can use an existing workflow as the starting point for a new workflow. The clone option is available only in the Microsoft Entra admin center.

To start cloning from the workflow list:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. Select the workflow that you want to clone, and then select **Clone**.

    

You can also start cloning from the workflow creation experience:

1. Browse to **ID Governance** > **Lifecycle workflows** > **Create workflow**.

1. On the **Choose a workflow** page, find the **Clone an existing workflow** card, and then select **Browse workflows**.

    

1. Select the workflow that you want to clone.

After you select a workflow to clone, the **Review + create** tab opens directly. Review the workflow settings, and then select **Create** to create the workflow without making changes.

To customize the workflow before you create it, select the other tabs and update the workflow details or configuration. When you're finished, return to the **Review + create** tab and select **Create**.

## Create a lifecycle workflow by using a template in the Microsoft Entra admin center

If you're using the Microsoft Entra admin center to create a workflow, you can customize existing templates to meet your organization's needs. These templates include one for common pre-hire scenarios.

To create a workflow based on a template:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Create a workflow**.

1. On the **Choose a workflow** page, select the workflow template that you want to use.

    
1. On the **Basics** tab, enter a unique display name, description, and [administrative scope](https://learn.microsoft.com/en-us/entra/id-governance/manage-delegate-workflow) for the workflow, and then select **Next**.

    

1. On the **Configure scope** tab, select the trigger type and execution conditions to be used for this workflow. For more information on what you can configure, see [Execution conditions](https://learn.microsoft.com/en-us/entra/id-governance/understanding-lifecycle-workflows#execution-conditions).

1. Under **Rule**, enter values for **Property**, **Operator**, and **Value**. The following screenshot gives an example of a rule being set up for a sales department. For a full list of user properties that lifecycle workflows support, see [Supported user properties and query parameters](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-rulebasedsubjectset?view=graph-rest-beta&preserve-view=true#supported-user-properties-and-query-parameters).

    

1. To view your rule syntax, select the **View rule syntax** button. You can copy and paste multiple user property rules on the panel that appears. For more information on which properties you can include, see [User properties](https://learn.microsoft.com/en-us/graph/aad-advanced-queries?tabs=http#user-properties). When you finish adding rules, select **Next**.

    

1. On the **Review tasks** tab, you can add a task to the template by selecting **Add task**. To enable an existing task on the list, select **Enable**. To disable a task, select **Disable**. To remove a task from the template, select **Remove**.

    When you're finished with tasks for your workflow, select **Next: Review and create**.

    

1. On the **Review and create** tab, review the workflow's settings. You can also choose whether or not to enable the schedule for the workflow. Select **Create** to create the workflow.

    

> [!IMPORTANT]
> By default, a newly created workflow is disabled to allow for the testing of it first on smaller audiences. For more information about testing workflows before rolling them out to many users, see [Run an on-demand workflow](https://learn.microsoft.com/en-us/entra/id-governance/on-demand-workflow).

## Create a lifecycle workflow by using Microsoft Graph

To create a lifecycle workflow by using the Microsoft Graph API, see [Create workflow](https://learn.microsoft.com/en-us/graph/api/identitygovernance-lifecycleworkflowscontainer-post-workflows).

## Next steps

- [Manage a workflow's properties](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-properties)
- [Manage workflow versions](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks)
