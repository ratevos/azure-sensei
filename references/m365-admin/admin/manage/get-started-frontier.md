# Get started with the Microsoft Frontier program

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/get-started-frontier  
> Microsoft doc last updated: 04/27/2026


The Microsoft Frontier program gives organizations early access to innovative and emerging AI capabilities in Microsoft 365 before those features reach general availability (GA). By opting in to Frontier, IT administrators can evaluate new Copilot agents and AI-powered experiences, determine readiness for broader deployment across their tenant, and provide feedback about Frontier feature capabilities to Microsoft.

> [!IMPORTANT]
> Frontier is managed at the tenant level. Production tenants can safely enroll users into the Frontier program to allow your organization access to Frontier features. IT admins have explicit control which users have access to which Frontier features.  

Microsoft’s audience-based release model helps IT admins control how features are delivered to different user groups. This release model includes:

- **Frontier** (opt-in) is designed for early adopters who want pre-release access to evaluate and prepare.
- **Standard release** Users receive new features as soon as they are generally available.
- **Deferred release** is for audiences in more complex environments needing additional time to validate changes before deployment.

To learn more, see: [Configure modern release options for Microsoft 365 features](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/configure-release-options).

Access to Frontier experiences vary depending on your organization’s subscription and user roles.

Use of Microsoft Frontier requires a Microsoft 365 Copilot license.

> [!NOTE]
> Learn more about the Microsoft Frontier program, what's new, and how to try what's next in AI:  [Microsoft Frontier program](https://www.microsoft.com/microsoft-365-copilot/frontier-program). 
>
> Frontier features are preview and subject to change.

## Prerequisites

Review the following requirements and recommendations:

- Verify your admin role. You need an account that includes one of the following roles: **AI Admin**, **Security Admin**, **Office Apps Admin**.
- Verify that Microsoft 365 Copilot licenses are assigned to users who you want to access Frontier features. From the admin center, go to **Billing** > **Licenses** > **Microsoft 365 Copilot** and confirm the assignments. Users without a Microsoft 365 Copilot license aren't presented with Frontier features.
- Verify that your own admin account has a Microsoft 365 Copilot license. Some Frontier settings and agents in the admin center might not appear.

## Enroll users in Frontier

You can manage Frontier settings in the Microsoft 365 Admin Center.

To enable Frontier preview experiences:

1. Sign in to the [Microsoft 365 admin center.](https://admin.microsoft.com)   
1. Go to **Copilot** > **Settings**.
1. Select the **View all** tab.
1. In the **Search all Copilot settings** search bar, type "Frontier". 
1. Select **Copilot Frontier**.
1. Choose how Frontier access is assigned in your organization:

   - **No access** (default)
   - **All users**
   - **Specific users**

After you enable Frontier access, eligible users can access supported preview features as they're released. It might take three hours for Frontier features and agents to be available to users.

> [!NOTE]
> Some AI features in Microsoft 365 Desktop and mobile apps are currently released as a part of the Microsoft 365 Insider program. Learn more about the [Microsoft 365 Insider Program for Business](https://aka.ms/msft365insiderbusiness).

### Enable Frontier agents
Before your users can access Frontier agents, make sure that agent types are approved for use.

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), go to **Agent** > **Settings** > **Allowed agent types**.
1. Verify that **Allow apps and agents built by Microsoft** is checked. This setting allows use of Microsoft Frontier agents. 

> [!NOTE]
> You can manage access for specific agents for specific users or groups. For more information, see [Agent settings in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings).
>
> The Frontier admin control doesn't override the settings configured in the Agent section of the admin center. If an admin disabled a Frontier agent in the Agent view, that agent won't be available to users, regardless of a user’s Frontier enrollment.
>
> You can also manage the agents that show up in the Agent Store. For more information, see [Set up Agent Store in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-store).

> [!IMPORTANT]
> After the Frontier program is enabled, **Frontier agents** are available from the Agent store in Microsoft 365 Copilot. Search for "Built by Microsoft", and Frontier program agents are displayed with **(Frontier)** in the name. It might take up to three hours for Frontier agents to appear in the store. 

### Deploy agents to your users directly
You can install and pin specific agents to select users or groups directly rather than users needing to search the Agent store. This method helps users start using Frontier agents more quickly.

1. Go to **Agents** > **All agents**.
1. Select the agent you want to install.
1. In the **Users** tab, add the specific users or security groups that you want to use this agent.
   - Use an Entra ID security group to target specific users who can access Frontier agents. This approach helps you validate experiences with a small group before broad rollout. 
1. In the agent flyout, select **Install**. To help users find the agent, you can select **Pin for users**. The agent appears in the Microsoft 365 Copilot app.

### Manage AI provider large language models
Some Frontier features and agents require access to other AI provider large language models, such as Anthropic. Review the requirements and understand the implications for each large language model you want to use.

To allow access to other models, use the Microsoft 365 Admin Center to explicitly approve each model. For more information, see [Manage AI provider settings in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps#manage-the-setting-in-the-microsoft-365-admin-center).

### Configure AI-enabled Cloud PCs for Frontier

To use AI-enabled Cloud PCs during Frontier preview, complete the following steps shown in [AI-enabled Cloud PC](https://aka.ms/AICloudPCsLearn).

User accounts and Cloud PCs meet required technical specifications. All AI enablement for eligible Cloud PCs are completed by using Microsoft Intune. Cloud PCs must also be enrolled in the Windows Insider Program Beta Channel.

- [Experience next-gen productivity with Windows 365 AI-enabled Cloud PCs](https://aka.ms/AICloudPCs)  
- [AI-enabled Cloud PC](https://aka.ms/AICloudPCsLearn)
