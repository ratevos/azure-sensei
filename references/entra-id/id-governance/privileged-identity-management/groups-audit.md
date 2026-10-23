# Audit activity history for group assignments in Privileged Identity Management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-audit  
> Microsoft doc last updated: 04/23/2026


## Overview

When working with your organization's groups in Privileged Identity Management (PIM), you can view activity, activations, and audit history for Microsoft Entra group membership or ownership changes.

> [!NOTE]
> If your organization has outsourced management functions to a service provider who uses [Azure Lighthouse](https://learn.microsoft.com/en-us/azure/lighthouse/overview), role assignments authorized by that service provider won't be shown here.

Follow these steps to view the audit history for groups in Privileged Identity Management.

## View resource audit history

**Resource audit** gives you a view of all activity associated with groups in PIM.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

1. Browse to **ID Governance** > **Privileged Identity Management** > **Groups**.

1. Select the group you want to view audit history for.

1. Select **Resource audit**.

    

1. Filter the history using a predefined date or custom range.

## View my audit

**My audit** enables you to view your personal role activity for groups in PIM.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **ID Governance** > **Privileged Identity Management** > **Groups**.

1. Select the group you want to view audit history for.

1. Select **My audit**.

    

1. Filter the history using a predefined date or custom range.

## Next steps

- [Assign eligibility for a group in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-assign-member-owner)
