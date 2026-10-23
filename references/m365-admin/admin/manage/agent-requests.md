# Agent requests in Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-requests  
> Microsoft doc last updated: 04/07/2026


When a member of your organization publishes an agent to your tenant, the agent requires administrator approval before becoming available tenant-wide. Administrators can review the agent's details, such as the description, owner, data, and tools, and then publish or reject it. On publishing, administrators can also scope its audience to specific users or groups, or everyone, ensuring a controlled rollout.

The **Requests** list of agents provides a view of agents that require your review and action. Members of your organization can request specific agents that need your review before an agent can be made available. For example, agents that have been created by members of your organization using Copilot Studio or Foundry or Microsoft 365 Agents Toolkit can be submitted for admin approval. When an agent is submitted for admin approval, all metadata about an agent’s definition is provided in Microsoft 365 admin center. From the **Requests** list, you can select the agent to see the details about the agent to better understand the agent’s capabilities, data sources, and custom actions before allowing the agent to be published to your organization.

## Agent registry filters

The agent **Requests** view can contain a large list of agents that need your approval. You can filter the agent **Requests** list based on the following criteria:
- **State** - The state of the request, such as **Pending activate**, **Pending review**, or **Pending update**.
- **Channel** - The channel filter is the location where the agent will be deployed. It's the surface through which members of your organization can discover and interact with the agent. Channel values include **Teams**, **Copilot**, **Office**, **Outlook**, **Word**, **Excel**, or **PowerPoint**.

> [!TIP]
> If you don't see the agents that you expect to see in the agent registry list, check to make sure you don't have an existing filter set.

The streamlined approval workflow makes it faster and easier for administrators to review, approve, and manage custom agents in the Microsoft 365 admin center. 

There are three kinds of requests that show up under the **Requests** tab:

- Pending review
- Pending update
- Pending activate

## Actions for requested agents

There are two primary actions that you can select for an agent that has been requested:
- **Publish to store** - When you're ready to publish a requested agent, you can select this action to start the agent publishing wizard. The wizard allows you to select users, protection policies, and any required permissions.
- **Reject submission** - After you've reviewed a requested agent's details, you can select this action if you don't want to make the agent available to your organization.

## Requested agents pending review

When an agent is submitted for admin approval, all metadata about an agent’s definition is provided in Microsoft 365 admin center. Select the available tab to confirm the agent’s capabilities, data sources, and custom actions before allowing the agent to be published to your organization.

Use the following steps to view pending agent requests and act on those requests:

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
1. Select **Agents** > **All agents** > **Requests**.
1. Select the requested agent and view the agent’s details.<br>
  Confirm the capabilities, data sources, security and permissions, and custom actions that the agent can invoke.
1. When you're ready, select **Publish to store** within the agent details pane to view the agent publishing wizard.
  The publishing wizard steps you through the process of selecting users, applying a policy template, and accepting permissions.
1. Select the users or groups that can install the agent. Publishing makes the agent available for installation to the selected audience.
1. (Optional) Select the users or groups who will have the agent preinstalled. 
1. Select **Next** to view template options.
1. Choose a policy template that applies to the agent.
1. Select to apply either an existing template, the default template, or a custom template.
1. Select **Next** to review permissions. 
1. In the **Review permissions** step, view the permissions requested by the agent and grant admin consent if appropriate. Permissions allow the agent to access relevant data or perform actions on behalf of users. For more information, see [Agent permissions](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-details#agent-permissions).
1. Select **Next** to complete the process.
1. Once you have reviewed the agent details, select **Publish**.

For more information about publishing requested agents, see [Publish agents](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions).

## Requested agents pending update

When developers publish an update to an existing agent, the update appears in the **Pending approval** list with the status **Update pending**. Until the update is approved, the previous version of the agent remains available to users.

Use the following steps to view pending agent requests and act on those requests:

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
1. Select **Agents** > **All agents** > **Requests**.
1. Select the agent with the state of **Pending update** and view the agent’s details.
1. When ready, select **Update in store**.

## Requested agents pending activate

When a member of your organization requests to activate an agent so that they can create agent instances, the process requires your approval before they can create instances. Administrators can review the agent's details, such as the description, owner, data, and tools, and then approve the request and activate or reject it. When an administrator activates an agent, they can also scope its audience, such as specific users, groups, or everyone, ensuring a controlled rollout.

The Microsoft 365 admin center activation process for agents ensures governance, security, and quality of custom applications.

For more information about activating requested agents, see [Activate agents](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions).

## Reject agents

As an alternative, within the **Requests** list, you can select the ellipses to the right of the agent name, then **Reject submission** when you don't want to publish the agent.

For more information about rejecting requested agents, see [Reject agents](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions).
