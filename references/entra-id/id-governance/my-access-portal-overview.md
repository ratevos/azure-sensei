# What is the My Access portal? - Microsoft Entra

> Source: https://learn.microsoft.com/en-us/entra/id-governance/my-access-portal-overview  
> Microsoft doc last updated: 12/10/2024


My Access is a web-based portal used by users to review or request access to resources within Microsoft Entra, and by Administrators to configure this access. Depending on who is using the My Access portal, a different set of actions can be taken.

Users access the My Access portal to:

- Request access for themselves
- Approve or deny access for themselves or direct reports
- Review access for themselves
- Review access for users
- Manage and review access for agents managed

Administrators, via the Microsoft Entra admin center, can configure:

- Access packages that users can request, or that can be assigned to agents
- Access reviews for access packages
- Access reviews for groups and applications
- The overview page

## License requirements

This feature requires Microsoft Entra ID Governance or Microsoft Entra Suite subscriptions, for your organization's users. Some capabilities, within this feature, may operate with a Microsoft Entra ID P2 subscription. For more information, see the articles of each capability for more details. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).
Using [Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) for agent identities requires one of the following license plans:

- **Microsoft 365 E7**, which includes Agent 365 and Microsoft Entra Suite, to provide governance of user and agent identities.
- **Microsoft Agent 365** license paired with at least Microsoft Entra P1 or Microsoft 365 E3.

For more information, see [Microsoft Agent 365 plans and pricing](https://www.microsoft.com/microsoft-agent-365#plans-and-pricing). For the full list of agent-specific capabilities, refer to the **Microsoft Agent 365** column in the [Microsoft Entra ID Governance licensing table](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Overview page

The Overview page shows you key tasks that need your attention such as pending requests and reviews. It's the landing page for the My Access portal.

## Discover access packages

In the My Access portal, you can view the access packages you can request by selecting **Access packages** in the left-hand menu and the **Available** tab. Find the access package you want to request access to in the list. You can search for an access package by name, description, or resources via the search bar. Once you locate the access package, select the row. You might have to answer questions and provide business justification for your request.

Select Request history in the left-hand menu to see a list of your requests and the status.

For more information, see [Request an access package - entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-access).

## Approve or deny a request

In the My Access portal, you can view your pending requests by selecting **Approvals** in the left-hand menu. Select a pending request and review the details. Based on the information provided, approve or deny the request.  

For more information, see [Approve or deny access requests - entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-request-approve).

## Review access

In the My Access portal, you can view your pending access reviews by selecting **Access reviews** in the left-hand menu. On this page, select the specific review, and make a decision based on the information provided.

Microsoft Entra ID will also send you an email with instructions shortly after the review starts. Follow the instructions in the email to complete the review.

For more information about self-reviews, see: [Review your access to resources in access reviews](https://learn.microsoft.com/en-us/entra/id-governance/self-access-review).

For more information about reviews for others, see: [Review access to groups & applications in access reviews](https://learn.microsoft.com/en-us/entra/id-governance/perform-access-review).

## Manage agents

In the My Access portal, you can view a list of agent identities that you own and sponsor. For more about managing and sponsoring agent identities, see: [Administrative relationships for agent identities (Owners, sponsors, and managers)](https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers).

You're able to manage, approve, review, and enable the agent identities. For all agent identities you own or sponsor you're also able to see general information such as level of access, and agent identities activity. For more information on managing agent identities using the My Access portal, see: [Manage Agent (Preview)](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent).

## Next step

- [What are access reviews? - Microsoft Entra](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview)
