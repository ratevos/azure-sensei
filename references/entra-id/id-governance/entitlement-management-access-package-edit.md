# Hide or delete access package in entitlement management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-edit  
> Microsoft doc last updated: 07/15/2024


When you create access packages, they're discoverable by default. This means that if a policy allows a user to request the access package, they'll automatically see the access package listed in their My Access portal. However, you can change the **Hidden** setting so that the access package isn't listed in the user's My Access portal. A user will only see the access packages from a given tenant in their My Access portal. Users can either use the organization/tenant switcher which is located on the top right of the My Access portal or a My Access portal link which includes a tenant hint. For more information, see [Share link to request an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-settings).

This article describes how to hide or delete an access package.

## Change the Hidden setting

Follow these steps to change the **Hidden** setting for an access package.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).
    > [!TIP]
    > Other least privilege roles that can complete this task include the Catalog owner and Access Package manager.
1. Browse to **ID Governance** > **Entitlement management** > **Access package**.

1. On the Access packages page, open an access package.

1. On the Overview page, select **Edit**.

1. Set the **Hidden** setting.

    If set to **No**, the access package is listed in the user's My Access portal.

    If set to **Yes**, the access package won't be listed in the user's My Access portal. The only way a user can view the access package is if they have the direct **My Access portal link** to the access package. For more information, see [Share link to request an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-settings).

## Delete an access package

An access package can only be deleted if it has no active user assignments. Follow these steps to delete an access package.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).
     > [!TIP]
     > Other least privilege roles that can complete this task include the Catalog owner and Access Package manager.
1. Browse to **ID Governance** > **Entitlement management** > **Access package**.

1. On the Access packages page, open the access package.

1. In the left menu, select **Assignments** and remove access for all users.

1. In the left menu, select **Overview** and then select **Delete**.

1. In the delete message that appears, select **Yes**.

## Next steps

- [View, add, and remove assignments for an access package](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-assignments)
- [View reports and logs](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-reports)
