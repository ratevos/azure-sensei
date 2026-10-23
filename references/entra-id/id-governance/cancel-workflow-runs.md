# Cancel workflow runs using Lifecycle Workflows

> Source: https://learn.microsoft.com/en-us/entra/id-governance/cancel-workflow-runs  
> Microsoft doc last updated: 07/27/2026


Lifecycle Workflows allows administrators to cancel in-progress or queued workflow runs to prevent or mitigate the widespread impact of automation errors and misconfigurations.

When you cancel a workflow run, keep the following behavior in mind:

- **In-progress runs**: Canceling an in-progress workflow run cancels any tasks that haven't been processed yet. Tasks that already completed aren't affected.
- **Queued runs**: Queued workflows are runs where execution hasn't started yet. Canceling a queued run cancels the upcoming execution of all tasks for that run.
- **No rollback**: Previously completed changes aren't reversed. Only execution of upcoming changes is halted.
- **Single run selection**: Currently, you can only select a single run to cancel at a time.
- **Run-level cancellation only**: You can't cancel specific tasks or specific users within a run. Cancellation applies to the entire run.

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Cancel a workflow run in the Microsoft Entra admin center

To cancel a workflow run:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. Select the workflow that contains the run you want to cancel.

1. On the workflow page, select **Workflow History**.

    

1. Select the **Runs** tab.

1. Select a run that has a status of **In progress** or **Queued**.

    > [!NOTE]
    > The **Cancel** button is only enabled after you select a run that has a status of **In progress** or **Queued**. The **Cancel** button isn't available on the **Users** or **Tasks** tabs because only runs can be canceled.

1. Select **Cancel**.

## Related content

- [Lifecycle Workflows history](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-history)
- [Reprocess workflow runs using Lifecycle Workflows](https://learn.microsoft.com/en-us/entra/id-governance/reprocess-workflow)
- [Check the status of a workflow](https://learn.microsoft.com/en-us/entra/id-governance/check-status-workflow)
