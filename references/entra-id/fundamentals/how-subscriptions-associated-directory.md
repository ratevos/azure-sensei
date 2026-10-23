# Add an existing Azure subscription to your tenant

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/how-subscriptions-associated-directory  
> Microsoft doc last updated: 06/19/2026


## Overview

All Azure subscriptions have a trust relationship with a Microsoft Entra tenant. Subscriptions rely on this tenant (directory) to authenticate and authorize security principals and devices. When a subscription expires, the trusted instance remains, but the security principals lose access to Azure resources. Subscriptions can only trust a single directory while one Microsoft Entra tenant might be trusted by multiple subscriptions.

Think of the subscription as the scope where Azure resources and Azure role assignments are managed, and the tenant as the directory that contains the identities used to sign in and receive access. Azure roles control access to Azure resources in the subscription. Microsoft Entra roles control access to directory resources, such as users, groups, and domains. Changing a subscription's directory changes which tenant supplies identities for Azure role-based access control (Azure RBAC), but it doesn't make the subscription owner a Global Administrator in the tenant.

By default, the user who creates a Microsoft Entra tenant is automatically assigned the [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) role. However, when an owner of a subscription joins their subscription to an existing tenant, the owner isn't assigned to the Global Administrator role.

While users might only have a single authentication *home* directory, users might participate as guests in multiple directories. You can see both the home and guest directories for each user in Microsoft Entra ID.

> [!IMPORTANT]
> When a subscription is associated with a different directory, users who have roles assigned using [Azure role-based access control](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) lose their access. Classic subscription administrators, including Service Administrator and Co-Administrators, also lose access.
>
> Moving your Azure Kubernetes Service (AKS) cluster to a different subscription, or moving the cluster-owning subscription to a new tenant, causes the cluster to lose functionality due to lost role assignments and service principal's rights. For more information about AKS, see [Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/).

## Prerequisites

Before you can associate or add your subscription, do the following steps:
- Review the following list of changes that will occur after you associate or add your subscription, and how you might be affected:    
    - Users assigned roles using Azure RBAC lose their access.
    - Service Administrator and Co-Administrators will lose access.
    - If you have any key vaults, they'll be inaccessible, and you'll have to fix them after association.
    - If you have any managed identities for resources such as Virtual Machines or Logic Apps, you must re-enable or recreate them after the association.
    - If you have a registered Azure Stack, you'll have to re-register it after association.
  
  For more information, see [Transfer an Azure subscription to a different Microsoft Entra directory](https://learn.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription).

- Sign in using an account that:
    - Has an [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) role assignment for the subscription. For information about how to assign the Owner role, see [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).
    - Exists in both the current directory and in the new directory. The current directory is associated with the subscription. You associate the new directory with the subscription. For more information about getting access to another directory, see [Add Microsoft Entra B2B collaboration users in the Azure portal](https://learn.microsoft.com/en-us/entra/external-ID/add-users-administrator.yml).
    - Make sure that you're not using an Azure Cloud Service Providers (CSP) subscription (MS-AZR-0145P, MS-AZR-0146P, MS-AZR-159P), a Microsoft Internal subscription (MS-AZR-0015P), or a Microsoft Azure for Students Starter subscription (MS-AZR-0144P).

## Associate a subscription to a directory

To associate an existing subscription with your Microsoft Entra ID, follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com) with the [Owner](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) role assignment for the subscription.

1. Browse to **Subscriptions**.

1. Select the name of the subscription you want to use.

1. Select **Change directory**.

    

1. Review any warnings that appear, and then select **Change**.

    

    After the directory is changed for the subscription, you'll get a success message.

1. Select **Switch directories** on the subscription page to go to your new directory.

    

    It can take several hours for everything to show up properly. If it seems to be taking too long, check the **Global subscription filter**. Make sure the moved subscription isn't hidden. You might need to sign out of the Azure portal and sign back in to see the new directory.

Changing the subscription directory is a service-level operation, so it doesn't affect subscription billing ownership. To delete the original directory, you must transfer the subscription billing ownership to a new Account Admin. To learn more about transferring billing ownership, see [Transfer ownership of an Azure subscription to another account](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/billing-subscription-transfer).

## Post-association steps

After you associate a subscription with a different directory, you might need to do the following tasks to resume operations:

1. Reassign Azure roles in the new directory for users, groups, or service principals that need access to Azure resources. Role assignments from the previous directory aren't transferred.

1. If you have any key vaults, you must change the key vault tenant ID. For more information, see [Change a key vault tenant ID after a subscription move](https://learn.microsoft.com/en-us/azure/key-vault/general/move-subscription).

1. If you used system-assigned Managed Identities for resources, you must re-enable these identities. If you used user-assigned Managed Identities, you must re-create these identities. After re-enabling or recreating the Managed Identities, you must re-establish the permissions assigned to those identities. For more information, see [What are managed identities for Azure resources?](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

1. If you've registered an Azure Stack using this subscription, you must re-register. For more information, see [Register Azure Stack Hub with Azure](https://learn.microsoft.com/en-us/azure-stack/operator/azure-stack-registration).

For more information, see [Transfer an Azure subscription to a different Microsoft Entra directory](https://learn.microsoft.com/en-us/azure/role-based-access-control/transfer-subscription).

## Related content

- [Create a new tenant in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/create-new-tenant)
- [Azure roles, Microsoft Entra roles, and classic subscription administrator roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles)
- [Assign administrator and non-administrator roles to users with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-subscriptions-associated-directory)
