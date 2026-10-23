# Manage users synchronized from Active Directory Domain Services with workflows

> Source: https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-on-premises  
> Microsoft doc last updated: 03/12/2026


Workflows created by Lifecycle workflows can be used to manage the lifecycle of users synchronized from Active Directory Domain Services (AD DS). Synced AD DS support allows you to use workflow tasks to enable, disable, and delete synchronized users. In this article, you're walked through the steps of enabling a user account task to be run for users synchronized from AD DS.

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

While most Lifecycle workflow tasks can manage users synchronized from Active Directory Domain Services without any extra configuration, certain tasks such as enabling, disabling, and deleting tasks require some extra configuration. For more information on setting these prerequisites, see:  [User account tasks](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-on-premises#user-account-tasks).

## Configure a user account task to manage users synchronized from Active Directory Domain Services using the Microsoft Entra admin center

Account related tasks within workflows can be quickly edited to apply to users synchronized from Active Directory Domain Services. To edit a task in such a way using the Microsoft Entra admin center, do the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **Workflows**.

1. Select the workflow you want to edit the task within.

1. On the workflow screen, select **Tasks**.

1. On the Tasks screen, either select an existing task you want to run for users synchronized from Active Directory Domain Services, or create a new one by selecting **Add task**.

1. On the individual task screen, enable the checkbox that corresponds to running for a synchronized Active Directory Domain Services user. The following image shows it being enabled for a delete user account task.
    
1. Select **Save**.

## Edit a user account task to be compatible with users synchronized from Active Directory Domain Services using Microsoft Graph

To manage user tasks to be compatible with users synchronized from Active Directory Domain Services via API using Microsoft Graph, see: [Configure the arguments for built-in Lifecycle Workflow tasks](https://learn.microsoft.com/en-us/graph/identitygovernance-lifecycleworkflows-task-arguments).

## Next steps

- [Check status of a workflow](https://learn.microsoft.com/en-us/entra/id-governance/check-status-workflow)
- [Customize workflow schedule](https://learn.microsoft.com/en-us/entra/id-governance/customize-workflow-schedule)
