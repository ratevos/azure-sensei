# Manage Multiple Tenants in the Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/multi-tenant/manage  
> Microsoft doc last updated: 01/06/2026


[Multitenant management](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/overview) in the Microsoft 365 admin center offers a unified approach that allows partner administrators to manage all their tenants in a single location. This streamlined solution helps partners with [delegated administrator](https://learn.microsoft.com/en-us/entra/identity/users/directory-delegated-administration-primer) roles efficiently manage multiple Microsoft 365 tenants. If you're a partner managing multiple tenants, you can:

- Move quickly between tenants you manage
- Assess service health, products, and billing across multiple tenants
- On the **All tenants** page, quickly see the health of all your tenants' services, any open service requests, your products and billing, and the number of users in that tenant

## Before you begin

You must have the [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) role assigned to perform this task.

> [!IMPORTANT]
> Global Administrator is a highly privileged role. Limit its use to emergency scenarios when you can't use another role. For more information, see [About admin roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Move between tenants

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage), select a tenant name.

   

1. Using the **Tenant switcher**, you can move quickly between tenants you manage.

   

## View the All tenants page

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage), in the navigation pane, select **All tenants**.

2. On the **All tenants** page, take one or more of the following steps:

   - Assess service health
   - Review license usage
   - Search for or select the tenant you want to manage
   - Pin your most often visited tenant to the top of the list.

If you mark a tenant as a favorite, the list automatically expands the tenant. Then you can immediately view the status details.

## View service health for all tenants

The service health view shows you if any incidents or advisories are affecting the tenants. It also tells you how many of your managed tenants are affected.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage), in the multitenant view, select **Service Health**.

1. On the **Service health** page aggregated view, you can also see the total number of incidents, the total number of advisories affecting any of the managed tenants, and the number of services with active incidents. You can also see if any incidents and advisories affect your tenants.

   - You can use the filter option to view issues by issue type or by service.
   - You can review issues under **All services** or **All issues** tabs.

   

1. Select an incident on the **All services** or **All issues** tab to get more information about any incident on the **Overview** tab. Select the **Tenants affected** tab to get a list of the affected tenants.

   

   You can export the list of affected tenants to CSV format so that admins can share it with support teams.

## View a single tenant in the Microsoft 365 admin center

You can return to the Microsoft 365 admin center for any of the tenants from the **All tenants** page.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/?#/homepage), in the navigation pane, select **All tenants**.

2. Select the tenant name for which you want to view the Microsoft 365 admin center. 

   The admin center opens for that tenant.

## Related content

- [Overview of Microsoft 365 Lighthouse](https://learn.microsoft.com/en-us/microsoft-365/lighthouse/m365-lighthouse-overview)

- [Multitenant organization capabilities in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/overview)

- [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference)

- [What is Partner Center?](https://learn.microsoft.com/en-us/partner-center/enroll/overview)

- [Add and manage multiple tenants in your Partner Center account](https://learn.microsoft.com/en-us/partner-center/account-settings/multi-tenant-account)
