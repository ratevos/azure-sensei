# Show suggested access packages for My Access in entitlement management

> Source: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-suggested-access-packages  
> Microsoft doc last updated: 1/09/2025


In My Access, Microsoft Entra ID Governance users can see a curated list of suggested access packages in My Access. This capability allows users to quickly view the most relevant access packages for them based off their peers' access packages and previous assignments without scrolling through all their available access packages.

The suggested access packages list is created by finding people related to the user (manager, direct reports, organization, team members) and recommending access packages based on what the users’ peers have. The user is also suggested access packages that were previously assigned to them.

## Settings for end users to see their suggested access packages in My Access

Follow these steps to enable suggested access packages in My Access.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Identity Governance Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#identity-governance-administrator).

1. Browse to **ID Governance** > **Entitlement management** > **Control configurations** > **My Access settings for end users**.
    
    
1. For Show insights for suggested access packages in My Access, select *Past assignments, Past assignments and peers without names*, or *Past assignments and peers with names*.
1. Select **Save**.

1. Sign in to the My Access portal at https://myaccess.microsoft.com. Select **Access packages** to see your suggested access packages.  
     

## Next steps

- [Create and manage a catalog of resources](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create)
- [Delegate access governance to access package managers](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate-managers)
- [Delegate access governance to resource owners](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate)
