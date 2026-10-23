# Configure ID Protection-based approvals for access package requests in Entitlement Management (Preview)

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-configure-id-protection-approvals  
> Microsoft doc last updated: 11/04/2025


Making sure risky users don’t gain access to sensitive resources is an important part of securing your environment. You can further secure the entitlement management request process by integrating [Microsoft Entra ID Protection (IDP)](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) signals into the access package approval workflow in Microsoft Entra ID Governance entitlement management. With ID protection, entitlement management automatically adds a new first approval stage when a user flagged as risky requests access to an access package. This feature ensures that users identified as potentially compromised or at risk are reviewed by authorized security or compliance approvers before access requests are routed for standard approval routing. This article describes how to further secure your entitlement request process with ID Protection.

## License requirements

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Prerequisites

To use ID-protection with Entitlement management, you must first [deploy ID protection](https://learn.microsoft.com/en-us/entra/id-protection/how-to-deploy-identity-protection).

## How risk-based approvals work

> [!NOTE]
> If the customer has enabled both the IDP and IRM options, the access package request will first route to the IDP approver, then to the IRM approver, and finally to the access package policy approvers.

When a user requests access to an access package through the **My Access** portal:
1.	**Risk evaluation**: Entitlement Management queries Microsoft Entra ID Protection for the user’s current userRiskLevel 

1.	**Configuration check**: If the user’s risk level matches one of the administrator-selected thresholds (for example, Medium or High), Entitlement Management automatically adds an additional risk-based approval stage before the standard approval process.

1.	**Automatic approver assignment**:
    - The request is routed to users assigned the Security Administrator role in Microsoft Entra ID.

1.	**Security  review**: The assigned approvers review the user’s risk details and decide whether to approve or deny this stage of the request approval routing.
    - If approved, the request continues through the rest of the regular access package approval steps.
    - If denied, the request is closed, recorded in the audit logs, and no further approval routing takes place.

1.	**Audit logging**: All actions (approval and denial) and outcomes are captured in [Entitlement Management logs](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logs-and-reporting) for reporting and compliance visibility.

## Configure ID protection-based approvals for an access package using the Microsoft Entra admin center

To configure ID protection-based approvals for an access package in the Microsoft Entra admin center, you'd do the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).
    
1. Browse to **ID Governance** > **Entitlement management** > **Control configurations**.

1. On the control configurations screen, you're able to see the options  
    

1. On the card **Risk-based approval (Preview)**, select **View settings**.

1. On the risk-based approval page, next to **Require approval for users with ID protection risk (Preview)**, select **Customize**. (See the separate article if you also want to configure [insider risk management-based approvals](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-configure-insider-risk-management-approvals).)
     

1. You can set the ID protection user risk level and then select **Save**.  
    

## Reviewing a risky user's request

To review the pending request from a risky user, the approver must have the [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) role.

When a risky user submits a request for an access package, administrators are able to see their pending status via the requests page within the access package:

A user set as an approver, or fallback approver, for risky users can view the request and approve or deny via the my access portal:

> [!NOTE]
> Approvers have a maximum of 14 days to take action. If they don't take action within that time frame, requests are automatically denied.

## Next step

- [Configure Insider risk management-based approvals for access package requests in Entitlement Management (Preview)](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-configure-insider-risk-management-approvals)
