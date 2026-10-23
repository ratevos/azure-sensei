# Delete a lifecycle workflow

> Source: https://learn.microsoft.com/en-us/entra/id-governance/delete-lifecycle-workflow  
> Microsoft doc last updated: 03/12/2026


You can remove workflows that you no longer need. Deleting these workflows helps keep your lifecycle strategy up to date.

When a workflow is deleted, it enters a soft-delete state. During this period, you can still view it in the list of deleted workflows and restore it if needed. A workflow is permanently removed 30 days after it enters a soft-delete state. If you don't want to wait 30 days for a workflow to be permanently deleted, you can manually delete it.

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Delete a workflow by using the Microsoft Entra admin center

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. On the **Workflows** page, select the workflow that you want to delete. Then select **Delete**.

    

1. Confirm that you want to delete the workflow by selecting the **Delete** button.

    

## View deleted workflows in the Microsoft Entra admin center

After you delete workflows, you can view them on the **Deleted workflows** page.

1. On the left pane, select **Deleted workflows**.

1. On the **Deleted workflows** page, check the list of deleted workflows. Each workflow has a description, the date of deletion, and a permanent delete date. By default, the permanent delete date for a workflow is 30 days after it was originally deleted.

    

1. To restore a deleted workflow, select it and then select **Restore workflow**.

   To permanently delete a workflow immediately, select it and then select **Delete permanently**.

## Delete a workflow by using Microsoft Graph

To delete a workflow by using an API via Microsoft Graph, see [Delete a lifecycle workflow](https://learn.microsoft.com/en-us/graph/api/identitygovernance-workflow-delete?view=graph-rest-beta&preserve-view=true).

## View deleted workflows by using Microsoft Graph

To view a list of deleted workflows by using an API via Microsoft Graph, see [List deleted workflows](https://learn.microsoft.com/en-us/graph/api/identitygovernance-lifecycleworkflowscontainer-list-deleteditems).

## Permanently delete a workflow by using Microsoft Graph

To permanently delete a workflow by using an API via Microsoft Graph, see [Permanently delete a deleted workflow](https://learn.microsoft.com/en-us/graph/api/identitygovernance-deleteditemcontainer-delete).

## Restore a deleted workflow by using Microsoft Graph

To restore a deleted workflow by using an API via Microsoft Graph, see [Restore a deleted workflow](https://learn.microsoft.com/en-us/graph/api/identitygovernance-workflow-restore).

> [!NOTE]
> You can't restore permanently deleted workflows.

## Next steps

- [What are lifecycle workflows?](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows)
- [Manage lifecycle workflow versions](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks)
