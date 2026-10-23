# Understand Shadow AI in Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-shadow-ai  
> Microsoft doc last updated: 05/01/2026


> [!IMPORTANT]
>
> This feature is part of [Frontier preview program](https://www.microsoft.com/microsoft-365-copilot/frontier-program). Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities might change over time.

The Shadow AI page in the Microsoft 365 admin center helps IT administrators discover, monitor, and govern unmanaged AI agents used within their organization.

This preview capability provides a dedicated view for detecting and governing unapproved local AI agents such as OpenClaw, and enables administrators to take governance actions to maintain security and compliance.

> [!NOTE]
>
> Shadow AI is currently in public preview. Features, supported agents, and behaviors might change before general availability.

## Prerequisites

To use Shadow AI detection and governance, you need:

- Microsoft 365 E3 license to view Shadow AI Agents.

- At least one of the following roles:

  - [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator).
  - [AI Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator).
  - [Global Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader).
  - [Security Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader).
  - [Security Operator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator).
  - [Reports Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).
  - [User Experience Success Manager](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-experience-success-manager).
  - [Intune Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator).

- [Microsoft Intune](https://learn.microsoft.com/en-us/intune/fundamentals/what-is-intune) enrollment for managed Windows devices.
- Opt in to the [Frontier preview experience](https://www.microsoft.com/microsoft-365-copilot/frontier-program) in the Microsoft 365 admin center.

## What is Shadow AI?

Shadow AI refers to AI-powered tools and agents used by users without IT awareness or approval. While these tools might improve productivity, unmanaged usage can introduce risks related to:

- Data leakage.
- Compliance violations.
- Security vulnerabilities.
- Lack of auditability and governance.

Common examples of Shadow AI tools include:

- Unauthorized AI coding assistants. For example, OpenClaw.
- Local agents, MCP servers, and Agentic CLIs.
- Browser extensions with AI capabilities.

The Shadow AI experience helps administrators identify and manage these risks without disrupting legitimate business workflows.

## Available features

During public preview, the Shadow AI experience allows admins to detect and block the following Shadow AI agent:

| Agent    | Detection | Blocking  |
| -------- | --------- | --------- |
| OpenClaw | Available | Available |

> [!NOTE]
>
> Shadow AI detection and blocking currently apply only to managed Windows devices enrolled with Microsoft Intune.

## Access the Shadow AI (Frontier) agent

The **Shadow AI (Frontier)** page in the Microsoft 365 admin center is a dedicated experience separate from the **All agents** page. It focuses exclusively on unmanaged AI agents that require detection and governance.

To access the **Shadow AI (Frontier)** page in the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Agents** to expand it.

1. Under **Agents**, select **Shadow AI (Frontier)**

1. The **Shadow AI (Frontier)** page displays a list of known Shadow AI agents that can be detected in your environment.

### View Shadow AI agent details

1. To view Shadow AI agent details, such as OpenClaw details, select the Shadow AI agent from the list of agents in the **Shadow AI (Frontier)** page.

1. The details pane opens for the selected Shadow AI agent. Make sure **Details** is selected. From **Details** you can view information regarding the type of agent. For example:

   - When it was last scanned.
   - If there are any Microsoft Intune security policies currently applied.

### Enable detection for a Shadow AI agent

To proactively configure detection for a Shadow AI agent before broad adoption, follow these steps:

1. In the Shadow AI agent details pane, select **Security policies**.

1. Under **Security policies**, select **Continuously detect managed devices**.

1. Select **Apply policies** to confirm.

### View detected devices for a Shadow AI agent

Once detection is enabled for a Shadow AI agent, you can view detected devices in the Shadow AI agent details pane by following these steps:

1. In the Shadow AI agent details pane, select the **Detected devices** tab.

1. A list and count of detected devices is displayed.

    > [!NOTE]
    >
    > The detected devices list and count are only populated if a detection policy is applied. After the detection policy is initially enabled, it might take some time for devices to sync with Microsoft Intune and for the detected devices to populate in the list.

1. In **Detected devices**, you can search for a specific device name. You can also see the following device data:

   - **Device name**: Name of the device.
   - **Device type**: Type of device (Desktop, Virtual Machine, Server, Laptop, etc.)
   - **Operating system**: Operating system installed on the device.
   - **Last Intune scan**: The last time Microsoft Intune scanned the device.

### Blocking a Shadow AI agent

After detection is enabled and the Shadow AI agent is identified in your environment, you can block it to prevent execution on managed devices. When a Shadow AI agent is blocked, such as OpenClaw, it blocks common ways of running it by creating a new Microsoft Intune policy that automatically propagates to all managed Windows devices enrolled in Intune.

To view the policy details, search for the policy name **A365 - Block OpenClaw** in the article [Assign policies in Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-configuration/assign-device-profile). Depending on how Intune is configured in your organization, this Intune policy update could take anywhere from 15 minutes up to 8 hours to apply. Full policy details, including when Intune policy applies, can be found in Intune. Lastly, policies can also be edited in Intune to add additional controls.

To block a Shadow AI agent, follow these steps:

1. In the Shadow AI agent details pane, select **Security policies**.

1. Under **Security policies**, select **Block AI agents from *\<Shadow AI agent name>***. For example, select **Block AI agents from OpenClaw**.
