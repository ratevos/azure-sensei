# Manage agent instances in Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-agent-instances  
> Microsoft doc last updated: 11/21/2025


Once an admin activates an agent, requestor can create instances of that agent. The Microsoft 365 admin center provides a centralized view for managing these instances:

- **Agent Registry** - Navigate to **Agents** > **All agents** > **Registry**. You can view agents with the **AI teammate** tag. You'll also the number of instances that have been created for the specific agent.

- **Agent Details** - Select an agent to open a flyout panel that displays the agent details. Select the **Instances** tab in the panel.

- **Instance** tab - Select the **Instances** tab to display a detailed list of all instances created under that agent. From this panel, administrators can perform the following actions:

  - **Manage individual instances** - Access and update settings for each instance.
  - **Review security and compliance status** - Ensure every instance meets organizational standards.
  - **Apply and customize licenses** - Assign licenses and configure options at the instance level.

This streamlined experience helps administrators maintain control, compliance, and flexibility across all agent instances.

## Block agent instances

You can block or unblock agent instances for the entire organization using the same controls available for any other app in the Microsoft 365 admin center. Blocking an instance stops it and any actions it's performing.

To block or unblock an agent:

1. In the [Microsoft 365 admin center](https://admin.microsoft.com/), go to **Agents** > **All Agents**.
1. Select the agent with the **AI teammate** tag from the list. The agent details panel opens.
1. Under the **Instance** tab, the **Instance list view** is displayed.
1. Select the instance to see all details of the agent instance.
1. Select an instance and choose **Block**.

To restore functionality, the administrator can **Unblock** the instance at any time.

## Delete agent instances

Administrators can delete an instance from the Microsoft 365 admin center when it's no longer needed.

1. In the left navigation pane, select **Agents** > **All agents**.
1. Select the agent with the **AI teammate** tag from the list. The agent details panel opens.
1. Under the **Instance** tab, the **Instance list view** is displayed.
1. Select the instance to see all details of the agent instance.
1. Select the instance you want to delete, then select **Delete**.
1. Confirm the deletion when prompted.
1. Notify the owner of the deletion.
1. Remove or reassign Microsoft 365 licenses tied to the instance.
1. After 30 days, all instance accounts and data are permanently deleted. Audit logs are kept.
1. Once deleted, the instance no longer appears in the list.
