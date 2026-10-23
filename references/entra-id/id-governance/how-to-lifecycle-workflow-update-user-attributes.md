# Update user attributes with Lifecycle Workflows

> Source: https://learn.microsoft.com/en-us/entra/id-governance/how-to-lifecycle-workflow-update-user-attributes  
> Microsoft doc last updated: 05/01/2026


Lifecycle Workflows allow you to automate the updating of user attributes as part of joiner, mover, and leaver scenarios. The **Update user attributes** task enables you to set or clear attribute values for users in your organization when lifecycle events occur, such as a department change or an employee leaving.

This article walks you through configuring a workflow with the Update user attributes task using the Microsoft Entra admin center and Microsoft Graph.

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Supported attributes

The Update user attributes task supports the following attribute types:

- Built-in user attributes for cloud-managed users (for example, `department`, `jobTitle`, `employeeLeaveDateTime`)
- On-premises extension attributes for cloud-managed users (for example, `extensionAttribute1` through `extensionAttribute15`)
- Directory extension attributes for cloud-managed users and users synced from on-premises AD

> [!NOTE]
> Custom security attributes are not supported with this task.

> [!NOTE]
> For datetime attributes, you can specify either a specific date or use `system.now`. When set to `system.now`, the attribute will be set to the date when the task is processed.

## Limitations

Before configuring this task, be aware of the following limitations:

- **Up to 10 attributes** can be updated per task instance.
- For **users synced from on-premises AD**, this task supports **directory extension attributes only**.

## Configure the Update user attributes task using the Microsoft Entra admin center

To add the Update user attributes task to a workflow using the Microsoft Entra admin center, complete the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. Select an existing workflow or create a new workflow where you want to add the task.

1. On the workflow screen, select **Tasks**.

1. Select **Add task**, and then select **Update user attributes** from the list of available tasks.

    

1. Configure the attribute updates:
    - Select the attributes you want to update or clear.
    - Provide the new values for each attribute, or leave the value empty to clear an attribute.

    

1. Select **Save** to add the task to the workflow.

> [!NOTE]
> You can configure up to 10 attribute updates within a single task instance.

## Next steps

- [Lifecycle Workflow tasks and definitions](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks)
- [Manage workflow versions](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks)
- [Check status of a workflow](https://learn.microsoft.com/en-us/entra/id-governance/check-status-workflow)
- [Customize workflow schedule](https://learn.microsoft.com/en-us/entra/id-governance/customize-workflow-schedule)
