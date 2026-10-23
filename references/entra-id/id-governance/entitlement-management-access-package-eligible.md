# Assign eligible group membership and ownership in access packages via Privileged Identity Management for Groups

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-eligible  
> Microsoft doc last updated: 11/04/2025


As an access package manager, you can assign which role you want to provide a user for a group within an access package. By [managing groups with Privileged Identity Management(PIM)](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/groups-discover-groups), you're able to enhance security by designating that group access happens just-in-time. This article describes how to enable PIM for a group, adding the group to an access package, and verifying eligible assignments are available.

## Prerequisites

Using this feature requires Microsoft Entra ID Governance or Microsoft Entra Suite licenses. To find the right license for your requirements, see [Microsoft Entra ID Governance licensing fundamentals](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals).

## Create a group

This section walks you through creating the group that you enable to be managed by PIM. If you've already created the group you want to be managed by PIM, skip to [Enable management of group with PIM](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-eligible#enable-management-of-group-with-pim).

To create a group, you'd do the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [User Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator).

1. Browse to **Entra ID** > **Groups** > **All groups**.

1. Select **New group**.

1. Give the group a name and description and then complete the other required options:
   - **Group Type:** Security
   - **Membership type:** Select *Assigned*.
   
1. Select **Create**.

## Enable management of group with PIM

To enable PIM management for the group, you'd do the following steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

1. Browse to **ID Governance** > **Privileged Identity Management** > **Groups**.

1. Select **Discover groups** and select a group that you want to bring under management with PIM.

1. Select **Manage groups** and **OK**.

1. Select **Groups** to return to the list of groups enabled in PIM for Groups, and notice the group you added is now on the list.
    

> [!IMPORTANT]
> Once a group is managed, it can't be taken out of management. This prevents another resource administrator from removing PIM settings. If a group is deleted from Microsoft Entra ID, it can take up to 24 hours for the group to be removed from the **PIM for Groups** option.

## Add the resource to an access package

Once the resource is managed by PIM, eligible roles can be added as its role assignment in an access package. To verify this, do the following:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).
    > [!TIP]
    > Other least privileged roles that can complete this task include the Catalog owner and the Access package manager.
1. Browse to **ID Governance** > **Entitlement management** > **Access package**.

1. On the **Access packages** page, open the access package you want to add resource roles to.

1. In the left menu, select **Resource roles**.

1. Select **Add resource roles** to open the Add resource roles to access package page.

1. On the resource roles page, select **Groups and Teams**.

1. Select the group you want to add, and under roles verify that you can assign both active and eligible roles. After choosing the role, select **Next**.
    
1. When you're finished filling in required **Requests** information, go to **Lifecycle**.

1. Verify the Access Package expiration period doesn't exceed the **Expire eligible assignments after** setting in the PIM managed group.

> [!NOTE]
> If an Access Package expiration period exceeds the "*Expire eligible assignments after*" policy setting in the PIM managed group, it can cause discrepancies between Entitlement Management and Privileged Identity Management, leading to identities losing access while EM shows they're still assigned. For more information, see: [Using groups managed by Privileged Identity Management with access packages reference](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-pim-reference).

## Next steps

- [Review access of access packages](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-reviews-review-access)
- [Change resource roles for an access package in entitlement management](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-resources)
