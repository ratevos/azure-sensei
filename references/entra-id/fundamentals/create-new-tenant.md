# Quickstart - Access and create new tenant

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/create-new-tenant  
> Microsoft doc last updated: 07/29/2026


## Overview

You can perform all of your administrative tasks using the Microsoft Entra admin center, including creating a new tenant for your organization.

In this quickstart article, you learn how to create a basic tenant for your organization.

> [!NOTE]
>Only paid customers can create a new Workforce tenant in Microsoft Entra ID. Customers using a free tenant, or a trial subscription won't be able to create additional tenants from the Microsoft Entra admin center. Customers facing this scenario who need a new tenant can sign up for a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

## Create a new tenant for your organization

After you sign in to the [Azure portal](https://portal.azure.com), you can create a new tenant for your organization. Your new tenant represents your organization and helps you to manage a specific instance of Microsoft Cloud services for your internal and external users.

> [!NOTE]
>
> - If you're unable to create a Microsoft Entra ID or Azure AD B2C tenant, review your user settings page to ensure that tenant creation isn't switched off. If it isn't enabled you must be assigned at least the [Tenant Creator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator) role.
> - This article doesn't cover creating an *external* tenant configuration for consumer-facing apps; learn more about using [Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/customers/overview-customers-ciam) for your customer identity and access management (CIAM) scenarios.
> - If you're unable to create a Governed Workforce tenant, verify that you have either an [Enterprise Agreement (EA)](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-ea-roles) or [Pay-As-You-Go](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn) subscription. Both [Microsoft Online Subscription Agreement (MOSA)](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts#microsoft-online-services-program) and [Microsoft Customer Agreement (MCA)](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts#microsoft-customer-agreement) billing accounts are supported. You also need the required Azure Resource Manager (ARM) permissions for the selected subscription through the Tenant Contributor or Subscription Owner/Creator role. To identify your billing account type, see [View your billing accounts in the Azure portal](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts).

### To create a new tenant

# [Workforce / B2C](#tab/workforce)

1. Sign in to the [Azure portal](https://portal.azure.com).

1. From the Azure portal menu, select **Microsoft Entra ID**.

1. Navigate to **Entra ID** > **Overview** > **Manage tenants**.

1. Select **Create**.

   

1. On the Basics tab, select the type of tenant you want to create, either **Microsoft Entra ID** or **Microsoft Entra ID (B2C)**.

   Choose **Microsoft Entra ID** to create a workforce tenant for your organization's users and resources. Choose **Microsoft Entra ID (B2C)** only if you need an Azure AD B2C tenant. If **Microsoft Entra ID** is unavailable, review the prerequisites in the previous note, including paid customer requirements, tenant creation settings, and the Tenant Creator role.

1. Select **Next: Configuration** to move to the Configuration tab.

1. On the Configuration tab, enter the following information:

   

   - Type your desired Organization name (for example *Contoso Organization*) into the **Organization name** box.
   - Type your desired Initial domain name (for example *Contosoorg*) into the **Initial domain name** box.
   - Select your desired Country/Region or leave the *United States* option in the **Country or region** box.

1. Select **Next: Review + Create**. Review the information you entered and if the information is correct, select **Create** in the lower left corner.

Your new tenant is created with the domain contoso.onmicrosoft.com.

# [Secure add-on tenant creation](#tab/governed-workforce)

Use the secure add-on tenant creation flow to create a new Governed Workforce tenant. This process creates the tenant and automatically establishes a [governance relationship](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/governance-relationships) with your home tenant.

### Define the default governance policy template

In order to automatically establish governance relationships with add-on tenants, you first need to define the default governance policy template.

1. Sign in to the governing tenant as an administrator.

1. Navigate to Templates.

1. Select the default policy template and configure the following options as needed:

   - **Delegated administration**: Select one or more Microsoft Entra built-in roles and assign them to a role assignable security group in the governing tenant. Members of this group can use their governing tenant credentials to sign in to the governed tenant without needing an account in the governed tenant. Each group can have multiple role assignments, and each policy template can have multiple groups defined.

   - **Multitenant application management**: Select a custom, multitenant application. The governed tenant creates a service principal with the same permissions when you establish the relationship.

### Create the tenant

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).

1. Browse to **Entra ID** > **Overview** > **Manage tenants**.

1. Select **Create**.

1. On the Basics tab, select **Governed Workforce** to access the secure add-on tenant creation feature.

1. Select **Next: Configuration** to move to the Configuration tab.

1. On the Configuration tab, enter the following information:

   - Type your desired Organization name (for example *Contoso Organization*) into the **Organization name** box.
   - Type your desired Initial domain name (for example *Contosoorg*) into the **Initial domain name** box.
   - Select your desired Country/Region or leave the *United States* option in the **Country or region** box.
   - Select your desired cloud subscription and resource group for storing the Microsoft Entra ID Free billing asset for your new tenant.

   > [!NOTE]
   > Use either an [Enterprise Agreement (EA)](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/understand-ea-roles) or [Pay-As-You-Go](https://azure.microsoft.com/pricing/offers/ms-azr-0003p?cid=msft_learn) subscription. Both [Microsoft Online Subscription Agreement (MOSA)](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts#microsoft-online-services-program) and [Microsoft Customer Agreement (MCA)](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts#microsoft-customer-agreement) billing accounts are supported. You also need the required Azure Resource Manager (ARM) permissions for the selected subscription through the Tenant Contributor or Subscription Owner/Creator role. To identify your billing account type, see [View your billing accounts in the Azure portal](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/view-all-accounts).

1. Select **Next: Review + Create**. Review the information you entered and if the information is correct, select **Create** in the lower left corner.

Your new tenant is created with the domain contoso.onmicrosoft.com. If you defined a governance policy template, a tenant governance relationship is automatically formed between your home tenant and your newly created tenant. Your billing account now shows a Microsoft Entra ID Free billing asset linked to your newly created tenant under the selected subscription and resource group.

To learn more about governance relationships and policy templates, see [Governance relationships](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/governance-relationships) and [Governance policy templates](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/governance-policy-templates).

---

## Your user account in the new tenant

By default, the user who creates a Microsoft Entra tenant is automatically assigned the [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) role.

By default, you're also listed as the [technical contact](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/change-address-contact-and-more#what-do-these-fields-mean) for the tenant. Technical contact information is something you can change in [**Properties**](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Properties).

Microsoft recommends that organizations have two cloud-only emergency access accounts permanently assigned the [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) role. These accounts are highly privileged and aren't assigned to specific individuals. The accounts are limited to emergency or "break glass" scenarios where normal accounts can't be used or all other administrators are accidentally locked out. These accounts should be created following the [emergency access account recommendations](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access).

## Clean up resources

If you're not going to continue to use this tenant, you can delete the tenant using the following steps:

- Ensure that you're signed in to the directory that you want to delete through the **Directory + subscription** filter in the Azure portal. Switch to the target directory if needed.
- Select **Microsoft Entra ID**, and then on the **Contoso - Overview** page, select **Delete directory**.

    The tenant and its associated information are deleted.

   

## Next steps

- To change or add other domain names, see [How to add a custom domain name to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/add-custom-domain).

- To add users, see [Add or delete a new user](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users).

- To add groups and members, see [Create a basic group and add members](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups).

- To learn about access management, see [Azure role-based access control (RBAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) and [Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview) to help manage your organization's application and resource access.

- Learn about Microsoft Entra ID, including [basic licensing information, terminology, and associated features](https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra).
