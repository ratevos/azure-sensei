# Agent overview in Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview  
> Microsoft doc last updated: 04/21/2026


Agents are powerful AI companions that can handle a range of interactions and tasks. An agent can resolve issues that require complex conversations and autonomously determine the best action to take based on its instructions and context. It coordinates language models, along with instructions, context, knowledge sources, articles, tools, inputs, and triggers to accomplish goals that members of your organization need to accomplish. Your organization can use agents in multiple languages across websites, mobile apps, Facebook, Microsoft Teams, and any other supported channel.

Agent governance involves using policies, settings, and admin actions to control how agents at your organization are accessed, published, deployed, and managed across your organization. When you apply an agent governance approach to managing agents, you ensure agents and the data they use remain secure and compliant.

By using governance across your agent lifecycle, you help ensure agent adoption is consistent and safe. Governance ensures agents onboard intentionally, operate within guardrails, and are managed consistently from build through retirement.

Organizations face significant challenges related to agent governance, including the following:
- How to apply consistent governance policies across all agents, regardless of how or where they’re built.
- How to balance developer freedom and experimentation with centralized oversight.
- How to identify and retire low value or ownerless agents before they create risk or cost.

By managing agents within Microsoft 365 admin center, organizations can establish these guardrails for agents and people, onboard agents with IT oversight, and govern agent access to resources and data, thereby meeting the challenges that organization face. In addition, organizations track their governance approach with built-in compliance and data retention details.

The following capabilities help your organization confidently manage and govern your agent's ecosystem:

- **Bring agents under control from day one** - Onboard and approve agents through one IT controlled flow, applying policy templates to every agent for governance and compliance.
- **Control what agents can access and do** - Enforce least privilege access by controlling which users, data, and tools agents can use and limit access to only the resources and other agents they need.
- **Automate ongoing agent governance** - Leverage rules-based agent management to automatically enforce lifecycle policies, such as flagging ownerless agents, or blocking risky agents.
- **Be audit-ready from the start** - Strengthen visibility into how your agents are being used and how they're performing, helping you ensure they operate securely, comply with policies, and run reliably across your organization.
- **Reduce compliance and safety risks** - Establish data safety and compliance controls to detect, retain, and investigate unethical agent interactions.

The Agent workload within [Microsoft 365 admin center](https://admin.microsoft.com/) allows you to view a summary of agents that you manage, deploy, and monitor at your organization. It provides usage and insights that help monitor agent adoption and governance. The Agent workload serves as the grounding control plane for all agents managed at your organization.

The Agent workload will help you accomplish the following tasks:
- Discover and review the agents that exist in your organization's tenant
- Understand who published and owns each agent
- Control availability and access to each agent
- Apply agent governance and policy decisions consistently across channels

> [!NOTE]
> The Microsoft Frontier program gives organizations early access to innovative and emerging AI capabilities in Microsoft 365 before those features reach general availability (GA). Frontier previews are subject to the existing preview terms of your customer agreements. For more information, see [Get started with the Microsoft Frontier program](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/get-started-frontier).

## View the Agent overview

You can access and view the **Agent overview** using the following steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. Select **Agents** > **Overview**.
   The **Agent overview** pane is displayed.

> [!IMPORTANT]
> Certain features are available within Microsoft 365 admin center based on services licensed in your subscription. Based on your subscription, you may see Agent 365 branding and additional agent related features and details. To view your licensed subscriptions in the [Microsoft 365 admin center](https://admin.cloud.microsoft/), select **Billing** > **Licenses** > **Subscriptions**.

## Agent overview summary

Administrators use the Agent overview to identify and act on critical governance tasks required to maintain compliance, mitigate risk, and ensure agents are properly managed across the organization. These actions are surfaced through actionable insights in the dashboard and provide direct pathways to resolve governance gaps.

Using the **Agent overview**, you can view key agent details for your tenant, including the following items:

- A snapshot of agent activity and actionable insights for the last 30 days
- Track agent usage trends
- Identify risks and governance gaps
- Critical actions for administrators to review, such as:
  - Approve pending requests
  - Manage agents without owners
- Total agents in your organization
- Enable visibility and control across all agents in your tenant
 
> [!TIP]
> A tenant is an instance of Microsoft Entra ID. Your subscription to Copilot or Agent 365 is hosted by a Microsoft Entra tenant. For more information about creating and understanding tenants, see [Set up a new Microsoft Entra tenant](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant) in the Microsoft Entra documentation.

To ensure consistent interpretation across metrics and insights in the Agent overview, the following definitions clarify what is included in agent counts and reporting on the **Overview** dashboard:
- **Definition of an agent**
  An agent is defined as an AI-powered entity that can perform tasks or interactions autonomously or semi-autonomously using instructions, context, knowledge sources, and tools to accomplish user or organizational goals.
- **Supported agent types and platforms**
  The Agent Overview includes agents built across supported Microsoft and connected platforms. This includes agents created using platforms surfaced in the ecosystem such as Copilot Studio and other Microsoft-supported creation tools, as well as applicable non-Microsoft agents detected through connected platforms. Specific platforms supported include: Microsoft Copilot Studio, SharePoint, Agent Builder, AI Foundry, Agents Toolkit, other Microsoft agentic types (such as Researcher), and non-Microsoft agentic platforms (such as Manus or Genspark).

  > [!NOTE]
  > The Agent Overview doesn't show all agent platforms in use, only the top 5 most used, to fit on the card. To see all agent platforms and associated agents, go to the **Registry** tab.
  
- **Draft agent visibility**
  Agent counts and metrics primarily reflect agents that are discoverable within the tenant through governance and registry systems. Visibility of draft or unpublished agents may vary based on platform integration and governance state. 

  > [!NOTE]
  > Currently, you can only view draft agents from Copilot Studio. Support for draft agents from other platforms, such Agent Builder, Foundry, and SharePoint, aren't currently available.

- **System and Microsoft-built agents**
  Agent inventory includes Microsoft-built, partner-built, and custom (line-of-business) agents to provide a comprehensive view of the total agent footprint in the organization. 
- **Platforms surfaced in Copilot Studio and ecosystem**
  Agent creation platforms represented in the overview include Microsoft-native tools (such as Copilot Studio, Agent Builder, and others) along with any external or third-party platforms detected and integrated into the agent registry. 
- **Data consistency across sources (Registry vs. analytics systems)**
  Metrics in the Agent overview are derived from multiple underlying systems (such as the Agent Registry and usage analytics pipelines). Minor variances may occur due to differences in ingestion timing, update frequency, and system-specific processing. These variances are expected and don't impact overall directional insights.

View access to the agent **Overview** doesn't grant permission to install, modify, or manage agents. Administrative actions continue to be governed by role-based access controls aligned with agent installation and consent workflows. For more information about roles and permissions, see [Agent management roles and permissions in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-roles-perms).

## Types of agents

Agents that can be managed in Microsoft 365 admin center vary depending on the agent type and platform. An agent's type and platform is based on the tools and methods used to create the agent.

The following table describes each type of agent:

| Type of agent | Description |
|---|---|
| **MCS DA** | A Microsoft Copilot Studio Declarative Agent (MCS DA) is created primarily using written instructions within Copilot Studio. These agents can be published based on channel and approved by the administrator within Microsoft 365 admin center. |
| **MCS CEA** | A Microsoft Copilot Studio Custom Engine Agent (MCS CEA) is designed using more precise settings and capabilities using Copilot Studio. The agents can be published based on channel and approved by the administrator within Microsoft 365 admin center. |
| **MCS BP** | A business process (BP) agent, created with Microsoft Copilot Studio, is a sequence of tasks, decisions, and interactions often implemented to use automation. |
| **Foundry LOB** | A Foundry LOB agent is create using Microsoft Foundry. This is a Line-of-Business (LOB) agent that has been created in-house (within your organization) for a specific business scenario.  |
| **Foundry non-LOB** | A Foundry non-LOB agent is created using Microsoft Foundry, however it isn't tied to a specific business workflow. |
| **Foundry hosted** | A Foundry hosted agent is created, stored, and run inside the Foundry platform. |
| **Agent Builder** | An Agent Builder agent is a declarative agent that has been created using Agent Builder within Copilot. |
| **SharePoint** | A SharePoint agent is a declarative agent that has been created using SharePoint. This type of agent typically uses organizational knowledge hosted on SharePoint. |
| **Agent Toolkit** | An Agent Toolkit agent has been created using Microsoft 365 Agents Toolkit. The toolkit provides tooling for building, testing, and managing agents across Microsoft 365. |
| **Agent instance** | An agent that has been extended using the Microsoft Agent 365 SDK is an agent instance. Once extended, an agent instance has Entra-backed agent identity, enhanced notification capabilities, extended observability, covered MCP tooling, and an IT-approved template system. |

For more information about agent types, see [Data & tools by agent type](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-details#data--tools-by-agent-type).

## Agent card details

### Hero metrics for agent impact

Hero metrics provide a high-level summary of the most critical indicators of agent scale and engagement.

- **Agent registry** - The total count of all agents available in your organization's catalog, including Microsoft-built, partner-built, and custom "line-of-business" agents. In both registry and usage, we refer to these types of agents as "Built by your organization". This Agent registry reflects the breadth of agents deployed across your tenant. In the **Agent overview**, you can select **Explore All agents** > **Registry** to view your inventory in detail.
- **Active users** - The number of unique users who interacted with at least one agent up to the last 30 days by sending a prompt to an agent and receiving a response from that agent. These conversational interactions can occur in Microsoft experiences, such as Teams and Microsoft Copilot, as well as non-Microsoft channels. For Microsoft Copilot Studio agents, an active user is counted when a user sends a prompt to the agent. In most cases, prompts and responses have a one-to-one relationship. However, there are limited scenarios where a user may send a prompt but not receive a response. This difference is expected to have a minimal impact in practice. This definition will evolve in the future as we continue to improve how usage is measured.
  - This metric begins when your organization activates Agent 365 licenses. It may reflect fewer than 30 days of data immediately after activation. As activity accumulates, the metric will progressively reflect a fuller 30-day view.
  - Data collection starts at license activation. For related information, see [Microsoft 365 Copilot Agents usage report - Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-agents-new).
- **Agent run-time** - Total hours worked by agents during the last 30 days, calculated from when a user request begins to when it is completed, and aggregated across all agent activities, such as executing tool calls and preparing responses.
  - This metric begins when your organization activates Agent 365 licenses, so it will reflect fewer than 30 days of data immediately after activation. As activity accumulates, the metric will progressively reflect a fuller 30-day view.
- **Registry sync** - The external connected platforms that were scanned. You can connect to external platforms to find and monitor agents used in your organization. Your use of external non-Microsoft products is subject to the third-party service provider's terms of use. You're responsible for complying with each provider's terms of use.

## Top actions for you

Governance actions help administrators enforce policy, maintain accountability, and manage the agent lifecycle across the tenant. These actions are driven by signals such as pending approvals, ownership gaps, and identified risks.

Common governance actions include: 
- **Review and approve pending agent requests** - Identify agents awaiting administrative approval and take action to allow or restrict deployment. Selecting **Manage requests** navigates to **Requests** view (**All agents** > **Requests**).
- **Assign ownership to agents without owners** - Ensure all agents have a designated owner responsible for lifecycle management, compliance, and ongoing maintenance.
- **Investigate and remediate agents at risk** - Review agents flagged for potential security or compliance issues and take corrective action by selecting to manage agent risks in the Agent Registry.
- **Review agents with exceptions** - Identify agents experiencing errors or issues in operation and investigate underlying problems through detailed views.

These governance actions are surfaced through the following key views:
- Pending Requests for agents
- Agents without owners
- Agents at risk
- Agents with exceptions

Selecting any of these options navigates to filtered views within the Agent Registry, where administrators can take corrective action.

> [!IMPORTANT]
> Important governance actions such as approving agent requests or assigning ownership can only be performed by users in the **AI Administrator** or **Global Administrator** roles. Other roles can monitor governance gaps but can't take administrative action.

View actionable governance cards that display urgent tasks for you (the administrator) to maintain compliance. These cards help you quickly identify and resolve governance gaps.

- **Pending Requests for Agents** - See the total number of agent requests awaiting admin approvals. The card lists three pending requests, prioritized by newest first. To take immediate action, select **Manage requests**. This selection navigates to the **Agent Registry** > **Requests** tab. This tab lists all pending agent requests submitted by users within your organization.
- **Agents at risk** - View the total number of agents with security risks. These are aggregated high severity risks across Microsoft security platforms such as Microsoft Entra, Microsoft Defender, and Microsoft Purview. It closes a critical visibility gap for IT administrators responsible for governing AI agents. Select **Manage agent risks** to view agents filter by risk in the **Agent Registry**.
- **Agents without owners** - View the total number of agents without an assigned owner and still pending owner assignment. Select **Assign Owner** to view a list of agents filtered by **Agents without owners**.
- **Agent with exceptions** - View the total number of agents with errors in their conversations. Select **View details** to view a list of agents filtered by agents with errors.
  - This metric begins when your organization activates Agent 365 licenses. It will reflect fewer than 30 days of data immediately after activation. As activity accumulates, the metric will progressively reflect a fuller 30-day view.
 
## Agent analytics

Get detailed insights into how agents are distributed and used. This information helps administrators understand if a specific platform is being used, and if an agent is spiking in usage, to assure it’s compliant and managed, so as to mitigate risk.

- **Agents by creators** - View a breakdown of all agents in your inventory by their source of publisher type, such as who created and shared the agent. There are three categories:
  - **Your organization** - Agents that your organization created and published. These agents can be shared by the creator or used only by the creator. This group also contains counts for "your users", which are agents created by members of your organization. These agents can be shared by those members of your organization, or used only by them.
  - **Third Party** - Agents created by external partners.
  - **Microsoft** - Agent created by Microsoft.
- **Top platforms used to build agents** - See which creation platforms are most used for building agents. The following MSFT platforms are covered in Agent 365 (A365):
  - Microsoft 365 Copilot Agent Builder (including Teams and Copilot Studio Legacy Agents)
  - Copilot Studio
  - Agents Toolkit
  - SharePoint
  - Microsoft Foundry - **NOTE**: Currently, analytics only support Microsoft Foundry V2 agents.
  - Other - **NOTE**: **Other** is used to indicate an unknown platform. **Other** also includes Microsoft, External, and LOB agents when the metadata field for **Platforms** is blank for those agents.
  - Non-Microsoft platforms will also display in this card if there are non-Microsoft agents in your registry.

  > [!NOTE]
  > New agent platforms will be regularly be added, thus this list will continue to grow.

- **Active users over time** - View a trend chart that shows daily active user engagement with agents over the last 30 days. This chart reveals usage momentum and helps you spot spikes or declines.
  - This metric begins when your organization activates Agent 365 licenses, so it will reflect fewer than 30 days of data immediately after activation. As activity accumulates, the metric will progressively reflect a fuller 30-day view.
- **Trending agents by active users** - You can view the agents with the most active users in your organization over the last 30 days.
  - This metric begins when your organization activates Agent 365 licenses, so it will reflect fewer than 30 days of data immediately after activation. As activity accumulates, the metric will progressively reflect a fuller 30-day view.
