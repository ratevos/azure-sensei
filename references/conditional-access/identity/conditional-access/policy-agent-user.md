# Secure agent users with Microsoft Entra Conditional Access

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-agent-user  
> Microsoft doc last updated: 07/31/2026


Use Conditional Access to protect an agent that accesses resources through its own [agent user account](https://learn.microsoft.com/en-us/entra/agent-id/agent-users), instead of (or in addition to) an agent identity.This access pattern supports agents that need a mailbox, access to chat, or the ability to participate in collaborative workflows as a team member.

In this access pattern, the access token's subject is the agent's user account. Conditional Access policies therefore target the agent's user account, not its agent identity.

Before you start, review the licensing, role, agent-user, device, and network requirements.

## Prerequisites

- One of the following license plans:
	- Microsoft 365 E7, which includes Agent 365 and Microsoft Entra Suite, to provide governance of user and agent identities.
	- Microsoft Agent 365 license paired with at least Microsoft Entra P1 or Microsoft 365 E3.
- At least the [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) role.
- An [agent user account](https://learn.microsoft.com/en-us/entra/agent-id/agent-users) linked to an agent identity.
- For device compliance, an agent that runs on an Intune-managed [Windows 365 Cloud PC for Agents](https://learn.microsoft.com/en-us/windows-365/agents/introduction-windows-365-for-agents).
- For compliant network policies, an agent that runs on an Intune-managed Windows 365 Cloud PC for Agents with [Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access) client installed.

> [!IMPORTANT]
> Agent user targeting is in Preview. Policies that target all users don't include agent user accounts. Group-based inclusion and exclusion also aren't supported for agent user accounts. Target "all agent users," select individual agent users, or use custom security attributes.

A policy that targets an agent identity doesn't apply to the agent's user account. If the agent also uses its own agent identity, create a separate policy for that access pattern. For more information, see [Secure autonomous agents with Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-autonomous-agents).

## Creating policies for agent users

Conditional Access extends policy enforcement to these user-like autonomous agents. Administrators can:

- Target all agent users or select specific agent users
- Apply policies using custom security attributes
- Apply agent risk conditions to block risky agents
- Use the agent execution environments condition to scope policies to agents running on endpoints
- Enforce device compliance for agents running on managed endpoints (Windows 365 Cloud PCs)
- Enforce compliant network locations for agents running on managed endpoints (Windows 365 Cloud PCs) with a Global Secure Access client

To create a Conditional Access policy for agent users, use the following settings:

- **Assignments**: In an agent access flow, the access token is issued to the agent users (the token subject), so you assign the policy to agents or their agent identity blueprint.
- **Target resources**: Select the resources the agent needs to access.
- **Conditions**: Configure whether you want the policy to apply when the agent is at a particular risk level. For example, a restrictive policy for agents that are high-risk. For more information, see [ID Protection for agents](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents).
- **Access control**: Because this agent accesses resources with its own identity, there's no remediation and the only available option is blocking access.

## Block risky agent user accounts

Create a policy that blocks agent user accounts when [Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents) detects medium or high agent risk. Agent risk is in Preview.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
2. Browse to **Entra ID** > **Conditional Access** > **Policies**.
3. Select **New policy**.
4. Enter a name for the policy.
5. Under **Assignments**, select **Users, agents or workload identities**.
6. Under **What does this policy apply to?**, select **Agents**.
	1. Under **Include**, select **All agent users (Preview)**.
7. Under **Target resources** > **Include**, select **All resources (formerly 'All cloud apps')**.
8. Under **Conditions** > **Agent risk (Preview)**, set **Configure** to **Yes**.
	1. Select **Medium** and **High**.
9. Under **Access controls** > **Grant**, select **Block**, and then select **Select**.
10. Set **Enable policy** to **Report-only**.
11. Select **Create**. 

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

## Require a compliant device

Some agent users are computer-using agents. These agents operate a desktop environment to complete tasks, similar to how a human user interacts with applications. 
Use this policy for an agent that runs on a managed endpoint, such as a Windows 365 Cloud PC for Agents. The **Agent execution environments (Preview)** condition limits the policy to agent user sessions that start from endpoints. Agents that don't run on a device are excluded from evaluation.

Note that not all agents run on endpoints. Agents running directly in Microsoft infrastructure don't have an associated device. Policies scoped with this condition don't apply to those cloud-native agents, which prevents unintended blocking.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
2. Browse to **Entra ID** > **Conditional Access** > **Policies**.
3. Select **New policy**.
4. Enter a name for the policy.
5. Under **Assignments**, select **Users, agents or workload identities**.
	1. Under **What does this policy apply to?**, select **Agents**.
		1. Under **Include**, select **All agent users (Preview)**.
6. Under **Target resources** > **Include**, select **All resources (formerly 'All cloud apps')**.
7. Under **Conditions** > **Agent execution environments (Preview)**, set **Configure** to **Yes**.
	1. Under **Include**, select **Agent user sessions initiated from endpoints**.
8. Under **Access controls** > **Grant**, select **Grant access**.
	1. Select **Require device to be marked as compliant**, and then select **Select**.
9. Set **Enable policy** to **Report-only**.
10. Select **Create**.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

> [!NOTE]
> An agent can technically run on any machine. Device compliance requires Intune enrollment, which today is only supported on Windows 365 Cloud PCs for Agents. Without the **Agent execution environments** condition scoping this policy, agents running in cloud infrastructure are blocked with no path to compliance.

## Require a compliant network

Use this policy to require agents running on endpoints to connect through a compliant network using [Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access). The client provides the network location signal that Conditional Access evaluates. This applies to agents that run on a managed endpoint, such as a Windows 365 Cloud PC for Agents.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a Conditional Access Administrator.
1. Browse to **Entra ID** > **Conditional Access** > **Policies**.
1. Select **New policy**.
1. Enter a name for the policy.
1. Under **Assignments**, select **Users, agents or workload identities**.
	1. Under **What does this policy apply to?**, select **Agents**.
	2. Under **Include**, select **All agent users (Preview)**.
2. Under **Target resources** > **Include**, select **All resources (formerly 'All cloud apps')**.
3. Under **Conditions** > **Agent execution environments (Preview)**, set **Configure** to **Yes**.
	1. Under **Include**, select **Agent user sessions initiated from endpoints**.
4. Under **Access controls** > **Grant**, select **Grant access**.
	1. Select **Require compliant network**, and then select **Select**.
5. Set **Enable policy** to **Report-only**.
6. Select **Create**.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

> [!NOTE]
> Use the **Agent execution environments (Preview)** condition to scope this policy to endpoint-based sessions only. Without this condition, cloud-native agents without a Global Secure Access client are blocked with no path to compliance.

## Related content

- [Conditional Access for agents](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id)
- [Target agent identities in Conditional Access policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-target-agent-identities)
- [Secure autonomous agents with Microsoft Entra Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-autonomous-agents)
- [Security for AI with Microsoft Entra agent identity](https://learn.microsoft.com/en-us/entra/agent-id/security-for-ai-overview)
- [Microsoft Entra ID Protection and agents](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents)
