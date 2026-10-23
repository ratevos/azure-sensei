# Approve activation requests for group members and owners

> Source: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-approval-workflow  
> Microsoft doc last updated: 04/23/2026


## Overview

With Privileged Identity Management (PIM) and Microsoft Entra ID, you can configure activation of group membership and ownership to require approval. You can also choose users or groups from your Microsoft Entra organization as delegated approvers.

Select two or more approvers for each group. Delegated approvers have 24 hours to approve requests. If a request isn't approved within 24 hours, the eligible user must resubmit a new request. The 24-hour approval time window isn't configurable.

Follow the steps in this article to approve or deny requests for group membership or ownership.

## View pending requests

As a delegated approver, you receive an email notification when an Azure resource role request is pending your approval. You can view pending requests in Privileged Identity Management.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a user who has been set as an approver.

1. Browse to **ID Governance** > **Privileged Identity Management** > **Approve requests** > **Groups**.

1. In the **Requests for role activations** section, you see a list of requests pending your approval.

    

## Approve requests

> [!NOTE]
> Approvers can't approve their own role activation requests. Additionally, service principals aren't allowed to approve requests.

1. Find and select the request that you want to approve and select **Approve**.

1. In the **Justification** box, enter the business justification.

1. Select **Confirm**. Your approval generates an Azure notification.

    

## Deny requests

1. Find and select the request that you want to deny and select **Deny**.

1. In the **Justification** box, enter the business justification.

1. Select **Confirm**. Your denial generates an Azure notification.

## Workflow notifications

Here's some information about workflow notifications:

- Approvers receive notifications by email when a request for a group assignment is pending their review. Email notifications include a direct link to the request, where the approver can approve or deny.
- Requests are resolved by the first approver who approves or denies.
- When an approver responds to the request, all approvers are notified of the action.

> [!NOTE]
> An administrator who believes that an approved user shouldn't be active can remove the active group assignment in Privileged Identity Management. Resource administrators aren't notified of pending requests unless they're an approver. But they can view and cancel pending requests for all users by viewing pending requests in Privileged Identity Management.

## Troubleshoot

Here's a troubleshooting tip.

### Permissions aren't granted after you activate a role

When you activate a role in Privileged Identity Management, the activation might not instantly propagate to all portals that require the privileged role. Sometimes, even if the change is propagated, web caching in a portal might result in the change not taking effect immediately.

If your activation is delayed:

1. Sign out of the Microsoft Entra admin center and then sign back in.
1. In Privileged Identity Management, verify that you're listed as the member of the role.

## Next steps

[Configure PIM for Groups settings](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-role-settings)
