# Governance and Lifecycle actions for agents available in Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions  
> Microsoft doc last updated: 05/01/2026


The Microsoft 365 admin center provides governance and lifecycle management capabilities for agents through the [Agent Registry](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry). These capabilities enable administrators to manage agent visibility, access, distribution, and retirement across the tenant.

## Agent actions

> [!NOTE]
>
> Microsoft 365 for government Community Cloud High (GCCH) and Government Community Cloud Moderate (GCCM) environments support publishing agents to the organization.

| Agent actions | Description |
|---|---|
| **[Install](#install-agents) and [uninstall](#uninstall-agents)** | Install an agent for users so it's ready to use without manual installation by end users. Admin can uninstall a previously installed agent. |
| **[Block and unblock](#block-or-unblock-agents)** | Restrict access to an agent across the organization, preventing any user from using it. |
| **[Delete](#delete-agents)** | Delete agents and any associated files. When you delete an agent, it permanently removes the agent from the inventory and deletes all associated files. |
| **[Assign a new owner](#assign-new-owner-to-an-agent)** | Assign a new owner to agents that are ownerless or active. |
| **[Publish to store](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests#actions-for-requested-agents)** | Make a requested agent available to members of your organization by publishing the agent to Agent Store. For more information, see [Actions for requested agents](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests#actions-for-requested-agents). |
| **[Reject submission](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests#actions-for-requested-agents)** | Prevent a requested agent from becoming available to members of your organization. For more information, see [Actions for requested agents](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests#actions-for-requested-agents). |

> [!NOTE]
>
> For information about actions related to the agent registry list, such as **Export to Excel**, **Upload custom agent**, and **Manage pinned agents**, see [Agent registry in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry).

### Install agents

You can install agents across the whole organization or for specific users or groups by using the same controls that work for any other app in the Microsoft 365 admin center.

To install an agent via the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Agents** to expand it.

1. Under **Agents**, select **All agents**.

1. In the **All agents** page, make sure **Registry** is selected. Select the **Status** filter and then select **Available**.

1. From the list of agents, select an agent that isn't already installed.

1. In the agent details pane that opens, immediately under the agent's name, select **Install**.

1. In the **Deploy agent to selected users** pane, decide whether to install the agent to all users or to specific users or groups, and then select **Next**.

    

1. In the **Review permissions** pane, review the requested permissions for the agent. If the permissions are acceptable, select **Grant admin consent**. For more information, see [Agent permissions](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-details#agent-permissions).

1. In the **Permissions requested** window, select **Accept** to grant the permissions to the agent, and then select **Next**.

1. In the **Review & finish** pane, select **Finish deployment**.

Installing an agent affects its availability and functionality in Copilot and in the other host products, such as Outlook, Teams, or Microsoft 365.

### Uninstall agents

You can uninstall first-party or external agents across the whole organization or for specific users or groups by using the same controls that work for any other agent in the Microsoft 365 admin center.

To uninstall an agent via the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Agents** to expand it.

1. Under **Agents**, select **All agents**.

1. In the **All agents** page, make sure **Registry** is selected. Select the **Status** filter and then select **Available**.

1. Select an installed agent from the list of agents.

1. In the agent details pane that opens, immediately under the agent's name, select **Uninstall**.

    > [!NOTE]
    >
    > If you don't see the Uninstall option, the selected agent might not be installed.

1. In the **Remove agent** pane, select the **Remove agent** option, and then select the **Uninstall Agent** button.

Uninstalling an agent affects its availability and functionality in Copilot and in the other host products, such as Microsoft Outlook, Microsoft Teams, or other Microsoft 365 applications.

## Block or unblock agents

Block or unblock agents for the entire organization by using the same controls that work for any other app in the Microsoft 365 admin center.

To block or unblock an agent, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Agents** to expand it.

1. Under **Agents**, select **All agents**.

1. In the **All agents** page, select an agent from the list of agents.

1. In the agent details pane that opens, immediately under the agent's name, select **Block** or **Unblock**.

1. In the **Block agent** or **Unblock agent** pane that opens, select either **Block agent** or **Unblock agent**, and then select **Save**.

    

Blocking or unblocking an agent that you created by using Microsoft 365 Copilot Agent Builder and Microsoft 365 Copilot Studio affects its availability and functionality in Microsoft 365 Copilot. It also affects availability and functionality in other host products, such as Microsoft Outlook, Microsoft Teams, or other Microsoft 365 applications. However, blocking an agent that you created by using SharePoint or Microsoft Foundry only impacts its availability in Microsoft 365 Copilot Chat.

> [!NOTE]
>
> For the [Researcher](https://support.microsoft.com/topic/e63ab760-f3de-4c47-ae87-dad601b0e9c4) and [Analyst](https://support.microsoft.com/topic/ff505b9c-a06c-4be9-b855-69d89b1d25d2) agents, the **Edit users** panel is disabled. To manage their availability, block the agent for the entire tenant by using the **Block** action in the Microsoft 365 admin center.

## Delete agents

You can delete agents created using Microsoft 365 Copilot Agent Builder directly from the Microsoft 365 admin center. Delete permanently removes the agent and its data from the tenant.

To delete an Agent Builder agent, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Agents** to expand it.

1. Under **Agents**, select **All agents**.

1. In the **All agents** page, from the list of agents find the Agent Builder agent that you want to delete.

    > [!TIP]
    >
    > To quickly find Agent Builder agents, use the **Platform** filter in the **All agents** page and then select **Agent Builder in Microsoft 365 Copilot**.

1. Next to the Agent Builder agent you want to delete, select the vertical ellipses (**⁝**) and then select **Delete**.

When you delete an agent, the following actions occur:

1. Microsoft 365 removes the agent from the inventory.
1. All associated files are deleted.
1. The underlying SharePoint Embedded container is deleted.

This deletion process is irreversible. Once you delete an agent, it might take up to 24 hours for the deletion to reach all users who had access to the agent. During this time, users might still see the agent listed, but they can't interact with it.

## Assign new owner to an agent

IT administrators can reassign ownership for agents that are ownerless or active.

> [!IMPORTANT]
>
> Reassigning ownership of shared agents is only supported for Agent Builder and Copilot Studio agents.

To reassign ownership of a shared agent, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Agents** to expand it.

1. Under **Agents**, select **All agents**.

1. In the **All agents** page, from the list of agents select an Agent Builder or Copilot Studio agent that you want to reassign.

    > [!TIP]
    >
    > To quickly find Agent Builder or Copilot Studio agents, use the **Platform** filter in the **All agents** page and then select either **Agent Builder in Microsoft 365 Copilot** or **Copilot Studio**.

1. In the agent details pane, immediately under the agent name, select **Assign new owner**.

1. In the **Assign a new owner** pane, enter a new owner from your organization, and then select **Assign**.

The following changes occur after owner reassignment:

- The new owner gets full edit and delete permissions, plus access to any files the previous owner uploaded.
- The previous owner loses all access, including read rights.
