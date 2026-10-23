# Discover Azure resources to manage in PIM

> Source: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-discover-resources  
> Microsoft doc last updated: 04/23/2026


## Overview

You can use Privileged Identity Management (PIM) in Microsoft Entra ID, to improve the protection of your Azure resources. This helps:

- Organizations that already use Privileged Identity Management to protect Microsoft Entra roles
- Management group and subscription owners who are trying to secure production resources

When you first set up Privileged Identity Management for Azure resources, you need to discover and select the resources you want to protect with Privileged Identity Management. When you discover resources through Privileged Identity Management, PIM creates the PIM service principal (MS-PIM) assigned as User Access Administrator on the resource. There's no limit to the number of resources that you can manage with Privileged Identity Management. However, start with your most critical production resources.

>[!NOTE]
>PIM can now automatically manage Azure resources in a tenant with no onboarding required. The updated user experience uses the latest PIM ARM API, allowing for improved performance and granularity in choosing the correct scope you want to manage. The new experience is the default when you navigate to **Azure resources** in PIM. The steps in this article describe the legacy experience. To switch between the new and legacy experiences, use the banner link at the top of the Azure resources page.

## Required permissions

You can view and manage the management groups or subscriptions to which you have Microsoft.Authorization/roleAssignments/write permissions, such as User Access Administrator or Owner roles. If you aren't a subscription owner, but are a Global Administrator and don't see any Azure subscriptions or management groups to manage, then you can [elevate access to manage your resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin).

## Discover resources

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator).

1.  Browse to **ID Governance** > **Privileged Identity Management** > **Azure resources**.

    If it is your first time using Privileged Identity Management for Azure resources, you see a **Discover resources** page.

    

    If another administrator in your organization is already managing Azure resources in Privileged Identity Management, you see a list of the resources that are currently being managed.

    

1. Select **Discover resources** to launch the discovery experience.

    

1. On the **Discovery** page, use **Resource state filter** and **Select resource type** to filter the management groups or subscriptions you have write permission to. It's probably easiest to start with **All** initially.

   You can search for and select management group or subscription resources to manage in Privileged Identity Management. When you manage a management group or a subscription in Privileged Identity Management, you can also manage its child resources.

   > [!Note]
   > When you add a new child Azure resource to a PIM-managed management group, you can bring the child resource under management by searching for it in PIM.

1. Select any unmanaged resources that you want to manage.

1. Select **Manage resource** to start managing the selected resources. The PIM service principal (MS-PIM) is assigned as User Access Administrator on the resource.

    > [!NOTE]
    > Once a management group or subscription is managed, it can't be unmanaged. This prevents another resource administrator from removing Privileged Identity Management settings.
     
    

1. If you see a message to confirm the onboarding of the selected resource for management, select **Yes**. PIM will then be configured to manage all the new and existing child objects under the resource.

    

## Next steps

- [Configure Azure resource role settings in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-configure-role-settings)
- [Assign Azure resource roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles)
