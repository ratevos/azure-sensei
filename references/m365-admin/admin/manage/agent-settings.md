# Agent settings in Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings  
> Microsoft doc last updated: 04/09/2026


The **Agent** settings page in [Microsoft 365 admin center](https://admin.microsoft.com/) provides centralized controls for managing AI agents across your organization. These settings help administrators enforce security, compliance, and governance standards while enabling flexibility for collaboration and productivity.

## Overview

The **Agent settings** page includes the following configuration options:

- **Agent management rules** - Set and run rules to manage or perform actions on agents.
- **Allowed agent types** - Specify which categories of AI agents are permitted for use within the organization.
- **Security templates** - Create preset policies, rules, and allow lists for new AI agents to ensure consistency and compliance.
- **Sharing** - Manage who can share AI agents within your organization and define the methods they can use to share them.
- **User access** - Control which users or groups can interact with AI agents, aligning access with organizational roles and permissions.

These settings allow you to customize agent behavior, control access, and maintain compliance with enterprise standards.

## Agent management rules

Agent Management Rules in the Microsoft 365 Admin Center (MAC) enable tenant administrators to apply governance and lifecycle controls across AI agents at scale using bulk administrative actions. 

Rather than requiring you to manually review and take action on agents individually, Agent Management Rules allow you to:

- Identify agents that meet defined conditions
- Review impacted agents prior to run
- Apply governance actions across affected agents in bulk

This experience helps organizations maintain compliance, ownership accountability, and deployment consistency across agents while keeping administrators in the control loop. 

### Supported Rule‑Based Bulk Actions

Agent Management Rules currently support the following governance scenarios:

- Install Microsoft agents
- Reassign ownerless agents created with Agent Builder to manager

#### Install Microsoft agents

Microsoft first‑party (1P) agents are consistently among the most installed and widely used agents. However, administrators currently lack a scalable way to install these agents proactively across their tenant.

Using the Install Microsoft (1P) Agents rule, you can do the following:

- Identify Microsoft‑published agents within the tenant
- Review eligible agents prior to installation
- Install selected agents for all users through a single bulk action
- Microsoft agents appear as installed and are readily available for end-users in the organization  

#### Reassign ownerless agents created with Agent Builder to manager

Agents may become ownerless when their original creator leaves the organization. Administrators must currently identify and transfer ownership manually, which can result in lifecycle governance gaps.

> [!NOTE]
> This rule is only supported when the agent is created using Microsoft 365 Copilot Agent Builder.

Using the Reassign Ownerless Agents rule, you can do the following:

- Identify agents that no longer have a valid owner
- Review ownerless agents prior to reassignment
- Transfer ownership using a bulk reassignment action to the manager of the previous owner based on Microsoft Entra ID hierarchy

## Allowed agent types

**Allowed agent types** allows control of which types of agents users can view and install from the agent catalog. You can select from the following options:

- **Allow apps and agents built by Microsoft** - Enables users to install agents created by Microsoft.

- **Allow apps and agents built by your organization** - Enables users to install custom agents developed within your tenant.

- **Allow apps and agents built by external publishers** - Enables users to install non-Microsoft agents built by external developers.

> [!TIP]
>
> - If you disable an option, agents of that type don't appear for users in the Agent store.
> - Agents built by Microsoft are visible to users even if the setting is disabled. Users aren't able to install those agents.

## Agent templates

To enhance governance and security for agents, you can apply a template that includes predefined security policies.

For more information about templates, see [Agent templates](https://learn.microsoft.com/en-us/microsoft-agent-365/overview).

## Sharing

**Sharing** allows defining who can share agents within your organization and how sharing works.

Options include:

- **Allow all users to share with anyone in the organization** - All users can share their agents with others in your tenant.

- **No users can share with anyone in the organization** - Sharing is disabled at the org level, but users can still share directly with specific individuals.

- **Allow specific groups of users to share with anyone in the organization** - Restrict broad sharing permissions to designated groups.

Only agents built with **Agent Builder** are governed by sharing control.

## User access

**User access** allows control of how members of your organization access and install agents.

> [!NOTE]
>
> As the administrator, you should use discretion when managing individual agent's distribution and costs.

To manage access to Copilot agents, follow these steps:

1. Open the [Microsoft 365 admin center](https://admin.microsoft.com/) in your browser.

1. Select **Agents** > **Settings** > **User access** to manage your organization's agents.

1. Select who can access agents within your organization.

    The setting has three options:

    - **All users** - This option is the default. It means that all users in the organization can access agents, subject to the existing app policies and user assignments.

    - **No users** - This option means that no users in the organization can access agents.

    - **Specific users/groups** - This option lets you select specific users or groups in your organization to have access to agents. While some users in your organization might have permission to install and use agents from the **Agent Registry** list, only the users or groups you select in this setting can use agents.

    > [!IMPORTANT]
    >
    > Data processed by non-Microsoft services isn't subject to Microsoft agreements. Review the terms provided by non-Microsoft agent publishers to make sure that you're familiar the agent's data handling and privacy practices. In addition, consult your internal policies before allowing access.

    

1. Select **Save** to update your Copilot agent settings for your tenant.
