# Agent Registry in Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry  
> Microsoft doc last updated: 05/01/2026


The agent registry in [Microsoft 365 admin center](https://admin.microsoft.com/) provides a centralized view of all agents available for your organization. This list helps you monitor, manage, and govern agents for your organization.

## View agent registry

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
1. In the left navigation pane, select **Agents** > **All Agents** > **Registry**.

    

## Agent types

The agent **Registry** lists all agents that are available to your organization. Agents are divided into four main types, as shown in the following table:

| Agent type | Description |
|---|---|
| **Microsoft agents** | Agents built and maintained by Microsoft. |
| **External partner-built agents** | Agents built by trusted non-Microsoft developers and published for broader or public availability. |
| **Published by your org** | Custom agents approved and published by your organization for broader use. These agents might be referred to as LOB (Line of Business) agents. |
| **Shared by creator** | Agents created and shared by individual users or developers at your organization. These agents are commonly referred to as Shared agents. |

## Agent registry summary

The agent **Registry** provides quick details about the agents your organization has available, as shown in the following table:

| Tenant-wide agent details | Description |
|---|---|
| **Total agents** | The number of agents available in your organization's tenant. |
| **Agents without owners** | The number of agents that no longer have owners at your organization. |
| **Unmanaged agents** | The number of agents created or managed outside of Agent 365, without its risk protection and observability. |

### Agent registry filters

The agent **Registry** can contain a large and diverse inventory of agents. As your organization's agent adoption increases, management of all your agents can be more involved and complex. In addition to sorting the list of agents by column, you can filter the list. Filtering this list helps you narrow the view to the agents that you want to focus on at the moment that allows you to:

- Be more efficient.
- Make focused decisions.
- Better apply your agent governance processes.

You can filter the agent list based on the following criteria:

- **Status** - You can filter the agent list based on status of the agent.
- **Publisher Type** - The publisher filter indicates who owns and distributes the agent, rather than where or how it was built. This filter is primarily used to distinguish between Microsoft agents, external partner-built agents, and internally owned agents published by your organization.
- **Channel** - The channel filter is the location where the agent is deployed. It's the surface through which members of your organization can discover and interact with the agent. Channel values include **Copilot**, **Teams**, **Outlook**, **Microsoft 365 apps**, and **SharePoint**.
- **Platform** - The platform filter indicates which platform or product was used to create the agent.
- **Data source** - The data source filter allows you to select **Embedded knowledge** and **Fine-tuned models** as data source options. **Embedded knowledge** refers to agents that include files that were uploaded by the agent maker or developer as knowledge sources. **Fine-tuned models** indicates that the agent was created using [Microsoft 365 Copilot Tuning](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-overview), allowing the agent to tune LLMs with their own organization data.

> [!TIP]
> If you don't see the agents that you expect to see in the agent registry list, check to make sure you don't have an existing filter set.
>
> Certain columns allow you to sort the agent registry list. To sort the list, select the column title.

## Agent registry actions

The agent **Registry** provides agent actions that relate specifically to your tenant's list of agents, as shown in the following table:

| Action | Description |
|---|---|
| **Refresh** | Updates the list to provide the most current view of the agent list. |
| **Export** | Exports agents to a CSV file. This action could take some time depending on the number of agents in the tenant. For more information, see [Export to Excel](#export-to-excel).  |
| **Add agent** | Provides a method to upload an agent manifest file (.zip). For more information, see [Upload custom agent](#upload-custom-agent). |
| **Manage pinned agents** | Select which agents are pinned for the user. Pinned agents are more prominently displayed in each available channel where the agent is deployed. You can change the priority of pinned agents by moving them up and down in this list. If a user has more than three pinned agents, users don't see agents with lower priority. For more information, see [Managed pinned agents](#manage-pinned-agents). |
| **Customize view** | Customize how the columns that are displayed in the agent list. For more information, see [Custom view](#customize-view). |
| **Search** | Use the search option to quickly find an agent in your agent **Registry**. |

> [!TIP]
> In addition to the above actions, you can change the view of the list from **Normal list** to **Compact list** by selecting the *list* icon next to the **Search** box.

## Agents without owners

Shared agents can become ownerless when you delete the user who created them from the organization.

To help administrators manage these scenarios, the Microsoft 365 admin center now enables you to identify and manage ownerless shared agents. The dashboard displays the total count of such agents, a one-click filter to quickly isolate them, and real-time updates that reflect user deletions. When administrators use these features, they can efficiently review and address ownership gaps by blocking or deleting affected agents.

### Key features

- **Ownerless agent count** - Administrators can view the total number of agents without a valid owner directly from the dashboard. For example, the dashboard shows 20 ownerless agents, which indicates that users who left the organization created these agents.
- **One-click filter** - Selecting the dashboard pane instantly filters the agent list to display only shared agents missing an owner. This feature allows for quick triage and action.
- **Real-time updates** - The ownerless agent count automatically updates when you hard delete a user from the organization. This feature ensures that the dashboard reflects the current state without requiring manual refreshes.

### Steps to view and manage ownerless shared agents

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
1. In the left navigation pane, select **Agents** > **All agents**.
1. Select the **Agents without owners** card.
  The **Publisher type** and **Owner** filters will be set.
1. Review the list of agents without owners and take appropriate actions for each agent, such as [blocking](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions#block-or-unblock-agents) or [deleting](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions#delete-agents) the agent.

## Export to Excel

Export the list of shared agents to an Excel file. You can set the scope of the exported list to be **All agents** or only the currently **Filtered agents**. This feature is essential for detailed analysis and reporting.

> [!NOTE]
>
> If the export process reaches one minute, the exported file includes only the data up to that point.

The exported file includes comprehensive information about each shared agent, such as:

- Name
- Status
- Channel
- Date created
- Last Modified
- Publisher
- Publisher Type
- Version
- Owner
- Description
- Platform
- Instructions

> [!TIP]
> There are over 30 different items for each agent that can be included in the exported list.

With this information, you can efficiently manage and review the shared agents within your organization, ensuring compliance and optimizing resource allocation.

## Upload custom agent

The agent **Registry** within Microsoft 365 admin center provides a method to upload a custom agent, so that you can manage those agents for your organization.

> [!NOTE]
> You can also update an existing agent in Agent Store. For more information, see [View agent details](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-details#view-agent-details).

To upload an agent, the agent must be contained in a ZIP packet file. The ZIP file contains resources, such as manifest files, configuration files, icons, branding, and embedded knowledge files.

> [!NOTE]
> Your agent ZIP file can be downloaded from Copilot Studio or from Agent Builder in Copilot.
>
> To download your agent ZIP file from Copilot Studio, select **Agents** > *the name of your agent* > **Channels**. Select the channel you use to publish, such as **Teams and Microsoft 365 Copilot**. Select **Availability options** > **Download .zip**.
>
> To download your declarative agent ZIP file from Agent Builder in Copilot, select **All agents** > *select the ellipses next to your agent* > **Edit** > *select the ellipses on the right* > **Download .zip file**.

To upload an agent as a ZIP packet file to the Microsoft 365 admin center:

1. In [Microsoft 365 admin center](https://admin.microsoft.com/), select **Agents** > **All agents** > **Add agent**.
1. Select **Choose file** to find and select the agent ZIP file.
  The ZIP file is validated.
  Then, select **Next**.
1. Verify the agent's name, icon, and host products.
1. Under **Publish**, select the users or groups who can install the agent.

    

1. Under **Deploy** (optional), select the users or groups who will have the agent pre-installed. Then, select **Next**.

    > [!NOTE]
    > You can select a small audience for testing purposes. For instance, select **Just me**, or a single test group to narrow the availability of the agent.

1. Choose to apply either an existing policy template, a custom policy, or the default policy. For more existing policy template information, see [Security templates](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings#security-templates). Agent 365 users can apply selected custom policies and protections. Default policies and protections are managed through their security platform. Check the status of each in the platform. Note policies and protections might not be enabled.
  Then, select **Next**.

    

1. Review agent permissions. Then, select **Next**.
1. Review and finished. Select **Finish deployment**.

## Manage pinned agents

As an administrator, you can choose to pin a deployed agent to the **Agents** list within Microsoft 365 Copilot. By pinning agents in Microsoft 365 Copilot, you can ensure that those agents are visible and accessible for all members of your organization, or only specific users or groups. You can choose to pin and unpin agents. Also, you can rank the list of pinned agents.

✅ **Task: Review and confirm your organization's pinned agents that are displayed in Microsoft 365 admin center.**

Microsoft 365 Copilot includes agents pinned by Microsoft, admins, and users. Microsoft pinned agents are specific agents that are pinned by default for all users. Your organization pins admin pinned agents by using the Copilot Control System in Microsoft 365 admin center. Individual users pin user pinned agents in their own Microsoft 365 Copilot Chat or Microsoft 365 Copilot experience.

To set, view, or manage pinned agents for your organization, see [Manage Pinning of Agents](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-pinning-agents).

> [!NOTE]
> After an administrator pins an agent, it might take up to six hours for end-users to see the agent pinned.

This section explains how administrators can pin, unpin, or manage agents for everyone or specific groups by using the Microsoft 365 admin center. It also covers related actions like ranking the list of pinned agents and editing the scope of pinned agents.

Pinning agents is a feature that enables administrators to preselect and pin agents for end-users by using Microsoft 365 Copilot. The administrator pins the agent to ensure that the agent automatically appears in the end user's Copilot interface without requiring any user action. The agent is now readily accessible to the user in the Copilot interface.

### Prerequisites

To pin agents so that each agent is more visible and accessible to members of your organization, there are prerequisites for your users (members of your organization). Additionally, you must have specific permissions and role.

**For end users** - Members of your organization must have access to the following:
- Microsoft 365 work account
- Access to Microsoft 365 Copilot Chat (for example, via Teams, web, or the Microsoft 365 Copilot app)
- The agent to pin must be discoverable by the member of your organization

**For administrators** - You, as the administrator, must have the following role and access:
- AI Administrator
- Access to the Microsoft 365 admin center
- (Optional) Power Platform admin center access (if you use Pay-as-you-go for agents)

### Pinned agents

### Microsoft-pinned agents

- These agents are agents that Microsoft pins by default for all users.
- Ensures essential or high-value agents, like core Copilot features, are always visible.
- End users can't unpin these agents. They're fixed in the pinned list.

### Administrator-pinned agents

- Pinned by your organization's administrator through the Microsoft 365 admin center.
- Can be pinned for:
  - **All users**.
  - **Specific groups**.
  - **Specific users**.
- End users usually can't unpin these agents. They're fixed in the pinned list.

### User-pinned agents

- Pinned by individual users in their own Microsoft 365 Copilot Chat experience.
- Users can:
  - Pin agents they frequently use.
  - Unpin them anytime.
- This list is fully under the user's control, except for Microsoft-pinned or administrator-pinned agents, which remain locked.

### Features

- Administrator-pinned agents appear by default for end-users, making them easier to discover and helping highlight new or important agents.
- Administrators can view the Microsoft-pinned agents in Microsoft 365 admin center.
- Administrators can pin up to three agents in Microsoft 365 admin center for end-users using Microsoft 365 Copilot in the organization.
- Administrators can choose to pin an agent for all users in the tenant or for specific users or groups. For example:
  - Pin **Sales Coach** agent only for the sales department.
  - Pin **HR Q&A** agent for all users.
- The end-user can't unpin the Administrator-pinned and Microsoft-pinned agents.

### Pin agents

1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
1. In the left navigation pane, select **Agents** > **All agents**.
1. In the **All agents** page, select the ellipse on the right to display a dropdown menu.
1. Select the **Manage pinned agents**.
  In the **Pinned agents** pane, you'll see agents **Pinned by your org** and agents **Pinned by Microsoft** list.
1. Select **Pin agent** to pin a new agent.
1. In the **Select an agent to pin** pane, find the agent you want to pin from the list of agents. You can search the list to find a specific agent by name. You can only pin agents that have been deployed to some or all users.

    

1. When you find the desired agent, select it and then select **Next**.
1. In the **Choose who will have this agent pinned** pane, choose the scope for the agent that you want to pin.

    - **All users the agent is deployed to** - Pin the agent for all users that the agent is deployed to in the tenant.

        >[!NOTE]
        >
        > If you don't see this option, the selected agent probably isn't deployed.

    - **Specific users or groups the agent is deployed to** - Pin for one or more groups or individual accounts.

    

1. If you select **Specific users or groups the agent is deployed to**, select the specific users or groups to pin the agent.

    

1. Select **Save**.

1. After you save the configuration, the system records which agent is pinned for the selected audience.

    

### Agents that can be pinned

You can only pin deployed agents. If the agent isn't deployed, you see a banner with a message to first deploy the agent.

If the agent is blocked, unblock the agent before you pin it.

### Rank the list of pinned agents

- The administrator has three slots reserved for the pinned agents for each user.

- The administrator can use the **Move up** and **Move down** buttons to reorder the list of pinned agents by priority to control what is shown to the user.

### Unpin an agent

From the list of pinned agents, find the agent that you want to unpin and select **Unpin**. When you remove the pin, the agent is no longer available under the **Pinned by your org** section.

### Edit the pinning scope of an agent

Select the agent and choose **Edit users** to modify the scope of users for which an agent is pinned.

### Alternate entry point for pinning

You can also pin an agent from the agent details pane. Select the pin for the user icon. The icon is only enabled if the agent is deployed.

## Customize view

The agent list provided on the **All agents** page can be customized. You can choose which columns to display.

## Microsoft Graph API for Agent Registry and Agent Details (preview)

You can also access Agent Registry data programmatically through Microsoft Graph APIs, which gives you scalable and programmatic control over agent management. By using the new Microsoft Graph API endpoints, now in preview, administrators can integrate the following tasks into existing workflows across agents in Microsoft 365:

- Automate bulk agent management.
- Streamline onboarding.
- Integrate governance.

Beyond manual UX-driven agent management, the Microsoft Graph API helps you accelerate agent management, maintain security and compliance, and ensure agents are available to the right users at the right time.

- **Get all agents in your inventory** - By using the [GET packages API](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/admin-settings/package/copilotpackages-list), administrators can retrieve a comprehensive list of all agents in their tenant to support compliance and reporting needs.

- **Get details of a particular agent in your inventory** - The [GET package details API](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/admin-settings/package/copilotpackagedetail-get) provides rich metadata and details for any agent, making it easier to audit, manage, and optimize agent management.

The API works with the **AI Admin Role**.

For more information, see [Agent and app Package Management API overview (preview)](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/admin-settings/package/overview).

## Risks column in the All agents page

The **Risks** column on the Microsoft 365 admin center **All agents** page provides a unified view of aggregated high severity risks across Microsoft security platforms such as Microsoft Entra, Microsoft Defender, and Purview. It closes a critical visibility gap for IT administrators responsible for governing AI agents.

To access the **All agents** page in the Microsoft 365 admin center and view the **Risks** column, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Agents** to expand it.

1. Under **Agents**, select [**All agents**](https://admin.cloud.microsoft/?#/agents/all).

1. In the **All agents** page, make sure **Registry** is selected.

1. The **Risks** column appears in the table in the **All agents** page.

When an administrator selects the risk count for an agent from the **Risks** column, they're taken directly to the Security tab within the agent's flyout details pane. This flyout provides a focused and actionable view of the total aggregated risk counts across all supported detection platforms for the selected agent. From this view, the administrator can further investigate risks and take mitigation actions, such as using the **Block** option to prevent the agent from operating if necessary. Additionally, the **Enabled policies and protection** sections display the default security protections applied to the agent by Microsoft Entra and Microsoft Purview.

If the agent has multiple instances associated with it, the flyout initially displays a breakdown of aggregated risks by instance. From here, the admin can proceed to view the total aggregated risk counts across all detection platforms for the selected agent.

To support further investigation, admins can select the **Review** link. The **Review** link redirects to the respective security portals where further action can be taken.

> [!NOTE]
>
> After selecting the **Review** link for Purview risks, you're taken to Purview. If you're presented with the **Welcome to the new Microsoft Purview portal!** message window, make sure to select the **Get started** button to see the relevant security alerts. If this message window is instead closed or the option **Go to classic portal** is selected instead of the **Get started** button, you might not see the relevant security alerts.

> [!IMPORTANT]
>
> - The **Risks** column only shows high severity risks flagged by the respective platforms. Zero risks is an indication that there are no high risks presently for the agent. However, there could be other types of risks, such as low or medium, in the respective security platforms.
>
> - There might be a delay of up to an hour for the risks count in the Microsoft 365 admin center when compared to what is shown in the security portals.

### Agents at risk tile

The **Agents at risk tile** on the **All agents** page displays the total number of agents in the tenant that have one or more high‑severity risks. Selecting the tile opens a pre-filtered view that shows only agents with detected risks, allowing administrators to prioritize investigation and remediation.

### Role-based access for the Review link

The following table shows what each role can access when they select the **Review** link:

| **Role** | **Can access & investigate risks in Defender** | **Can access & investigate risks in Purview**  | **Can access & investigate risks in Microsoft Entra** |
| -------- | ---------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------- |
| **[AI Admin](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator)**                                       | No | No | Partial |
| **[Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader)**                                   | No | No | No      |
| **[User Experience Success Manager](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-experience-success-manager)** | No | No | No      |
| **[Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader)**                                 | No | No | Yes     |
| **[Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator)**                   | No | No | Yes     |
| **[AI Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#ai-reader)**                                             | No | No | No      |
| **[Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader)**                                     | No | No | Yes     |

> [!IMPORTANT]
>
> To access Purview alerts, users must be assigned to one of the following **Insider Risk Management** (IRM) roles within Purview:
>
> - **Insider Risk Management Analysts**
> - **Insider Risk Management Investigators**
>
> These roles are required to sign in to Purview to view Insider Risk Management alerts. For more information, see [Assign permissions in Insider Risk Management](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions).

## Agents at risk card in the Agent 365 overview page

The **Agents at risk** card on the Microsoft 365 admin center **Overview** page provides administrators with a tenant‑level summary of agents that are identified with high‑severity risks across Microsoft security platforms including:

- Microsoft Entra.
- Microsoft Purview.
- Microsoft Defender.

To access the **Agents at risk** card in the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Agents** to expand it.

1. Under **Agents**, select [**Overview**](https://admin.cloud.microsoft/?#/agents/overview).

1. In the **Agent 365 overview** page, you can find the **Agents at risk** card under **Top actions for you**.

1. In the **Agents at risk** card, select **View agents** to be taken to the **All agents** > **Registry** page.

The **Agents at risk** card offers immediate visibility into the agents with the highest aggregated risks in the organization by surfacing the top three most at‑risk agents, enabling administrators to quickly prioritize investigation and response efforts.

Selecting **View agents** from the card takes administrators directly to the **All agents** > **Registry** page, where agents are pre‑filtered and sorted based on risk level. This filtering allows for streamlined investigation and remediation workflows without requiring manual filtering across the full agent inventory.
