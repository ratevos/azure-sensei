# Manage inactive users using Lifecycle Workflows

> Source: https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-inactive-users  
> Microsoft doc last updated: 03/12/2026


As part of supporting users no matter where they fall in the Joiner-Mover-Leaver (JML)  model of their lifecycle within your organization, Lifecycle Workflows support automating the disabling and deleting of users once they are inactive for a set period of time. This [sign-in inactivity](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-execution-conditions#sign-in-inactivity-trigger) allows you to set a workflow to run when a user is inactive for a set number of days. This feature allows you to seamlessly maintain a secure environment by automating the removal of inactive users based on criteria you set for your organization.

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Manage inactive users using the Microsoft Entra admin center

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **workflows**.

1. On the workflow screen, select the specific workflow you want to add the inactive user task to, or create a new workflow based on a template.
    > [!NOTE]
    > To use any of the leaver tasks, you must select a leaver workflow template.
1. On the **Basics** tab, after entering a unique display name and description for the workflow,  select the **Sign-in inactivity** trigger.

1. Once you select your desired workflow template enter basic details, and then select the **Sign-in inactivity** trigger.

1.  Under the **Days of inactivity**, enter the number of days you want the trigger to run for if exceeded, and then select **Next**.
    

    > [!NOTE]
    > Sign-in inactivity is determined by the `lastSuccessfulSignInDateTime` attribute.

1. On the **Scope** page, enter the scope you want for the trigger, and then select **Next**.

1. On the **Review Tasks** page, select the task you want to run for the users who you consider to be inactive and select **Review + Create**.
    > [!NOTE]
    > Lifecycle Workflows comes with a built-in task, [Send email about user inactivity](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks#send-email-about-user-inactivity), that is directly related to helping manage inactive users.

## Next steps

- [Manage workflow versions](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks)
- [Manage workflow properties](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-properties)
