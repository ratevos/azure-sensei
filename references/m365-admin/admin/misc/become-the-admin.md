# Perform an internal admin takeover

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/become-the-admin  
> Microsoft doc last updated: 04/22/2026


 **[Check the Domains FAQ](../setup/domains-faq.yml)** if you don't find what you're looking for.

If you're an administrator and you want to take over an unmanaged account that was created by a self-service user sign-up process, you can perform an internal administrator takeover by following the steps in this article.

> [!NOTE]
> A self-service sign up for any cloud service that uses Microsoft Entra ID adds the user to an unmanaged or "shadow" Microsoft Entra directory and creates an unmanaged account. An unmanaged account is a directory without a global administrator. To determine whether an account is managed or unmanaged, see [Determining Tenant Type](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-gdpr-dsr-guide-systemlogs#determining-tenant-type).
  
## Before you begin

When a user signs up for Microsoft 365 services by using an email address, the process automatically creates an account for them. If an admin wants to manage the users on the account or purchase other Microsoft 365 services, they must become an admin on the account by following these steps to perform an admin takeover.

## Step 1: Verify your email address

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

If self-service is enabled in your account, users can subscribe to free services such as Power BI, on their own. These services are specifically for use in cases where a self-service user subscription created the unmanaged account you want to take over as admin. In Step 1, you create a user account for the domain you want to remove by using Power BI to launch the admin takeover wizard so you can become the admin for the unmanaged domain account.

1. To sign up for Power BI, go to the [Power BI site](https://powerbi.com) and select **Start Free** > **Start free trial** (in Share with Power BI Pro box). 

1. Sign up with a user account that uses the domain name of your organization (like `powerbiadmin@contoso.com`). If your account is already in use, sign in by using your current password.

1. Check your email for the **verification code** and enter the code to validate your email address.

## Step 2: Create a new account for admin access

1. When you enter the verification code, you're taken to a page where you can create a new account.

1. Fill in the user name and password fields with the account that you want to use, and then complete the steps to create the account.

## Step 3: Verify domain ownership and become the admin

1. After you complete Step 2, select the admin center icon in the left navigation pane. Alternatively, go to a browser and type in `https://admin.cloud.microsoft`.

   You're redirected to the admin takeover wizard.

1. Select **Next** and verify that you own the domain you want to take over by adding a TXT record to your domain registrar.

   The wizard gives you the TXT record to add, and provides a link to your registrar's website, and a link to step-by-step instructions.

1. On the **You're now the admin** page, select **Go to the admin center**.

   You have the admin privileges required to manage the account in the admin center. For example, you can manage account users and groups, purchase new subscriptions and make user assignments, and manage the account domains.

   If you want to remove your domain from this account so you can add it to another account, see [Remove a domain from another account](https://learn.microsoft.com/en-us/microsoft-365/admin/misc/remove-a-domain-from-another-account).
  
## Related content

- [YouTube: Three steps to do an IT Admin Takeover for Power BI and Microsoft 365](https://www.youtube.com/watch?v=xt5EsrQBZZk) 

- [Admin takeover in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/users-groups-roles/domains-admin-takeover)

- [Using self-service sign up in your organization](https://learn.microsoft.com/en-us/microsoft-365/admin/misc/self-service-sign-up) 

- [Understanding the Power BI service administrator role](https://learn.microsoft.com/en-us/power-bi/service-admin-role)
