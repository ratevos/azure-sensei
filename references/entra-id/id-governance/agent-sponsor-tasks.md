# Agent identity sponsor tasks in Lifecycle Workflows

> Source: https://learn.microsoft.com/en-us/entra/id-governance/agent-sponsor-tasks  
> Microsoft doc last updated: 10/25/2025


Governing agent identities sponsors is a critical aspect of maintaining lifecycle governance and access control in your organization. Agent identity sponsors are responsible for overseeing the lifecycle and access decisions of agent identities. Keeping sponsor information up to date helps with effective governance and compliance. For an overview of agent identity governance including access packages and sponsor responsibilities, see [Governing Agent Identities](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview).

Lifecycle Workflows currently contain the following tasks that involve the governing of sponsors of agent identities:

- [Send email to manager about sponsorship changes](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks#send-email-to-manager-about-sponsorship-changes)
- [Send email to cosponsors about sponsor changes](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks#send-email-to-co-sponsors-about-sponsor-changes)
- [Transfer agent identity sponsorships to manager](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks#transfer-agent-identity-sponsorships-to-manager)

These tasks ensure continuity of sponsorship when an agent's sponsor changes roles or leaves the organization. All three tasks are classified as **mover and leaver** tasks and are available only under mover or leaver workflow templates.

This article explains how to configure Lifecycle Workflows to streamline agent identity sponsor governance.

## License Requirements

Using [Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) for agent identities requires one of the following license plans:

- **Microsoft 365 E7**, which includes Agent 365 and Microsoft Entra Suite, to provide governance of user and agent identities.
- **Microsoft Agent 365** license paired with at least Microsoft Entra P1 or Microsoft 365 E3.

For more information, see [Microsoft Agent 365 plans and pricing](https://www.microsoft.com/microsoft-agent-365#plans-and-pricing). For the full list of agent-specific capabilities, refer to the **Microsoft Agent 365** column in the [Microsoft Entra ID Governance licensing table](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Create a sponsor workflow using the Microsoft Entra Admin Center

To create a workflow that notifies the manager or cosponsors of an existing agent identity sponsor's move, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Lifecycle Workflows Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#lifecycle-workflows-administrator).

1. Browse to **ID Governance** > **Lifecycle workflows** > **workflows**.

1. On the workflow screen, select the specific mover or leaver workflow template you want to add the sponsorship email tasks to, or create a new workflow based on a template.
    > [!NOTE]
    > The **Send email to manager about sponsorship changes**, **Send email to co-sponsors about sponsor changes**, and **Transfer agent identity sponsorships to manager** are mover and leaver tasks, and are only available as selectable tasks under workflow templates of the same category.
1. On the **Basics** tab, after entering a unique display name and description for the workflow,  select your trigger and select **Next**.

1. On the **Configure scope** screen, select the scope of the workflow and select **Next**.

1. On the **Tasks** page, select which sponsor related tasks you want to include and select **Next**.
    
1. Review the created workflow, and then select **Create**. 

## Related content

- [Manage agent identities in your organization](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-organization) - See how sponsor governance fits into overall agent management.
- [Governing Agent Identities](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview) - Overview of agent identity governance including access packages and sponsor responsibilities.
- [Write concepts](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-tasks)
- [Manage workflow properties](https://learn.microsoft.com/en-us/entra/id-governance/manage-workflow-properties)
