# Manage unsponsored guests using Lifecycle Workflows (Preview)

> Source: https://learn.microsoft.com/en-us/entra/id-governance/how-to-lifecycle-workflow-unsponsored-guest-removal  
> Microsoft doc last updated: 07/31/2026


Unsponsored guests—guest users without a valid sponsor assigned—represent a security and compliance risk in your organization. Lifecycle Workflows help you automate the management and removal of unsponsored guests. Microsoft Entra ID Governance includes a built-in **Unsponsored guest cleanup (Preview)** workflow template that automates the detection and management of unsponsored guests.

This article walks you through managing unsponsored guests using the **Unsponsored guest cleanup (Preview)** workflow template.

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

> [!IMPORTANT]
> This functionality is subject to the guest billing model. For details, see [Microsoft Entra ID Governance licensing for guest users](https://learn.microsoft.com/en-us/entra/id-governance/microsoft-entra-id-governance-licensing-for-guest-users).

## Manage unsponsored guests using the Microsoft Entra admin center

To create a workflow for managing unsponsored guests:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. On the workflow screen, select **Create new workflow**.

1. On the template selection screen, find and select the **Unsponsored guest cleanup (Preview)** workflow template.

    > [!NOTE]
    > This template is specifically designed for leaver workflows.

1. Enter basic details for your workflow:
   - **Display name**: A descriptive name for your workflow
   - **Description**: Information about the workflow's purpose

1. Configure the workflow execution conditions. The trigger type is set to **Guest sponsor status (Preview)** by the template and can't be changed.

    

    > [!NOTE]
    > The **Number of sponsors** condition is set to **Equal to 0** and is not currently configurable. This workflow targets users with no sponsors assigned.

1. Configure the workflow tasks based on your organization's requirements.

1. Select **Review + Create** to finalize and enable the workflow.

## Add email notifications for unsponsored guest removal (optional)

The **Unsponsored guest cleanup (Preview)** template includes the **Delete User Account** task by default. You can optionally add the **Send email about unsponsored guest removal (Preview)** task to notify specified recipients when unsponsored guests are being removed from your organization.

> [!NOTE]
> For detailed information about adding and configuring the email task, including recipient options, email customization, and dynamic attributes, see [Lifecycle Workflow tasks and definitions - Send email about unsponsored guest removal (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks#send-email-about-unsponsored-guest-removal-preview).

## Next steps

- [Lifecycle Workflow tasks and definitions](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks)
- [Check status of a workflow](https://learn.microsoft.com/en-us/entra/id-governance/check-status-workflow)
- [Customize workflow schedule](https://learn.microsoft.com/en-us/entra/id-governance/customize-workflow-schedule)
- [Customize emails sent out by workflow tasks](https://learn.microsoft.com/en-us/entra/id-governance/customize-workflow-email)
