# Transfer data manually between Microsoft 365 accounts

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/transfer-data-manually  
> Microsoft doc last updated: 04/23/2026


This article explains how to transfer data manually between two Microsoft 365 accounts when the Switch plans wizard isn't available. The manual process in this article requires careful planning and coordination to minimize downtime and data loss. Transferring data between two Microsoft 365 accounts where the Switch plans wizard isn't available isn't automated. It's a manual, complicated, and time-consuming process. Additionally, the process in this article isn't supported. However, this article helps you get started.

Use this guide in the following scenarios:

- You need to change to a plan in a different service family.
- Your company name changed and you want to use different domain names. As part of this change, you decided to create a new subscription instead of trying to migrate your new domains to your existing subscription.
- You need to combine multiple subscriptions into one new subscription.

The instructions in this article are only applicable in these scenarios. Don't use the instructions for other scenarios, for example, when the Switch plans wizard is available. When the Switch plans wizard is available, use it to transfer data between two Microsoft 365 accounts instead of the manual method. For example:

- [Changing your subscription plan](https://learn.microsoft.com/en-us/microsoft-365/commerce/subscriptions/switch-to-a-different-plan) and can use the Switch plans wizard.
- Transferring to a new subscription plan in the same subscription family even when the Switch plans wizard doesn't work.

> [!CAUTION]
>
> Be aware of the following implications of the process described in this article if you're moving your custom domain from your current subscription to a new subscription:
>
> - **There might be some downtime while you perform the process**: Services such as email, Teams, and public websites hosted on Microsoft 365 don't work while the transfer is in progress.
>
> - **User accounts don't automatically transfer to your new subscription**: You need to recreate user accounts in the new subscription. Users receive new usernames and passwords. After users receive their new credentials, they need to set up Outlook with their new credentials.

## Overview of the manual transfer process

The manual transfer process consists of purchasing a new subscription, preparing domains and users, transferring data, and retiring the old subscription. The following steps provide an overview of the manual process to transfer data between two Microsoft 365 accounts:

### 1. Purchase the Microsoft 365 plan you want to transfer to

When you sign up, specify the company name to use in the initial domain names. For example:

- *yourcompany*.onmicrosoft.com.
- *yourcompany*-public.sharepoint.com.
- *yourcompany*.sharepoint.com.

Microsoft 365 requires unique initial `.onmicrosoft.com` domain names across subscriptions. For this reason, make sure to use a different *yourcompany* name than what you're using in your existing subscriptions.

> [!NOTE]
>
> It typically takes a minimum of several months after canceling a subscription to release the initial domain names that use  *yourcompany*  from our systems. Even if you plan to save all your data from your old Microsoft 365 subscription and cancel that subscription, the old  *yourcompany*  value isn't immediately available for use in a new subscription.

### 2. Add new custom domain names and users in your new subscription when using new domain names

If you're using new domain names in your new subscription, perform the following actions in your new subscription:

1. Add the new custom domain names in your new subscription.

1. Add the necessary DNS records for your new custom domains. For example:

   - MX record for email.
   - CNAME records for Teams.
   - CNAME record for your public website.

1. Create new users with your new custom domain names.

For more information, see [Add a custom domain to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain).

### 3. If you're moving a custom domain from an old subscription to a new subscription, remove your custom domain from your old subscription

Follow the steps in the article [Remove a domain from Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/remove-a-domain) to remove the domain name from your old Microsoft 365 subscription. This step is necessary because you can't add your custom domain to your new subscription until you remove the custom domain from the old subscription.

If Microsoft 365 is hosting your DNS, this step also removes DNS records for the domain, including MX, CNAME, and other records. If your DNS is hosted at a non-Microsoft DNS hosting provider, you don't need to remove your DNS records. However, you might need to modify some of the DNS records.

Your Microsoft 365 services such as email, Teams, and your public website stop working during this step:

- If Microsoft 365 is hosting your DNS, your Microsoft 365 services stop working when you remove the DNS records from your old subscription. Services resume after you complete the following steps:

  - Add your custom domain to your new subscription.
  - Add back the DNS records to your new subscription.
  - Set up your users for email.

- If a non-Microsoft DNS hosting provider is hosting your DNS, your Microsoft 365 services stop working when you remove your custom domain from your old subscription. Services resume after you complete the following steps:

  - Add your custom domain to your new subscription.
  - Set up your users for email.
  - Modify DNS records if necessary. Most DNS records probably remain the same between your old subscription and your new subscription. Check your Microsoft 365 admin center to see if any DNS records need to be changed or updated.

For more information, see [Remove a domain from Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/remove-a-domain).

### 4. Set up your custom domain and users for your new subscription

Set up your new subscription:

1. Add your custom domain to your new subscription.

1. Add or modify DNS records:

   - If Microsoft 365 is hosting your DNS, create the required DNS records for your custom domain.
   - If a non-Microsoft DNS hosting provider is hosting your DNS, modify or update any DNS records as needed. Most DNS records probably remain the same between your old subscription and your new subscription. Check your Microsoft 365 admin center to see if any DNS records need to be changed or updated.

1. Create your users on your custom domain.

### 5. Transfer data from your old subscription to your new subscription

Using two browser sessions, sign in to both your old subscription and your new subscription at the same time. Using separate sessions prevents sign-in conflicts between tenants. For the two browser sessions, use one of the following methods:

- Two different browsers. For example, Microsoft Edge and Google Chrome.
- Two different profiles in the same browser. For example, two different [profiles in Microsoft Edge](https://www.microsoft.com/edge/features/profiles).
- A normal session and a private session in the same browser. For example, an [InPrivate window in Microsoft Edge](https://www.microsoft.com/edge/features/inPrivate).

After you open two browser sessions, you can manually transfer data for the following services:

- [Manually transfer administrative settings between subscriptions](#manually-transfer-administrative-settings-between-subscriptions).
- [Manually transfer a SharePoint team site structure and data](#manually-transfer-a-sharepoint-team-site-structure-and-data).
- [Manually transfer a public website between subscriptions](#manually-transfer-a-public-website-between-subscriptions).
- [Manually transfer users' data between subscriptions](#manually-transfer-users-data-between-subscriptions).

### 6. Cancel the old subscription

   Verify that your new subscription is working and all data is transferred to your new account. Once you confirm everything is working, [contact customer support](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-support) to cancel your old subscription.

## Manually transfer administrative settings between subscriptions

To transfer administrative settings between subscriptions, manually configure the settings in your new subscription to match the settings in your old subscription. The following sections list the admin centers and settings you need to review and configure in your new subscription to match your old subscription.

### General Microsoft 365 subscription settings

To view and copy general settings for your subscriptions, follow these steps in each browser session:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Select each of the categories under **Settings**, such as **Domains**, **Org Settings**, and so on.

1. Review each category and configure equivalent settings in the new subscription.

### Exchange, SharePoint, and Teams admin settings

To view and copy Exchange settings for your subscriptions, follow these steps in each browser session:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Admin centers**, select the appropriate admin center. For example:

    - **Exchange**.

        > [!TIP]
        >
        > You can also go directly to the **Exchange admin center** by signing in to the [Exchange admin center](https://admin.exchange.microsoft.com/).

    - **SharePoint**.

    - **Teams**.

1. In the selected admin center, review each category and its settings. When needed, configure equivalent settings in the new subscription.

## Manually transfer a public website between subscriptions

If you have a public website hosted on Microsoft 365, you need to save it and recreate it on your new subscription. If your public website isn't hosted on Microsoft 365, you don't need to save it and recreate it. However, if needed, make sure you update any [DNS settings](#4-set-up-your-custom-domain-and-users-for-your-new-subscription) for the website appropriately.

> [!NOTE]
>
> The Public site migration app can't transfer data to a different subscription.

## Manually transfer a SharePoint team site structure and data

To transfer SharePoint team site data:

- Save the old site as a template and import the template into the new site. For more information, see [Apply and customize SharePoint site templates](https://support.microsoft.com/office/39382463-0e45-4d1b-be27-0e96aeec8398).

- To transfer documents:

    1. Manually recreate your hierarchy on the new site.
    1. Open both SharePoint team sites at the same time.
    1. Open both document libraries with Windows Explorer.
    1. Copy and paste the documents from the old site to the new site.

- To transfer list data, save a list template, and then use the saved template to recreate the list on the new site. For more information, see [Manage list templates](https://support.microsoft.com/office/c3884ad1-bc49-44b8-b3d6-3bc6a01eb393).

- To save a document library or list content from a SharePoint environment to file shares or to a local computer, see [Information about manual migration of SharePoint Online content](https://learn.microsoft.com/en-us/sharepoint/troubleshoot/migration-tool/content-manual-migration).

## Manually transfer users' data between subscriptions

### Email

Ask users to move their email, contacts, tasks, and calendar information after you set up their user account and they sign in. To reduce disruption, communicate these steps in advance to users. For more information, see [Find and transfer Outlook data files from one computer to another](https://support.microsoft.com/office/0996ece3-57c6-49bc-977b-0d1892e2aacc).

Users can continue to access their old email by using:

- Their **onmicrosoft.com** email address, such as `sue@contoso.onmicrosoft.com`.
- If changing domains, their email address associated with the domain in the old subscription.

### OneDrive data

Ask users to copy and sync their OneDrive content from the old subscription to their computer and then add it back to their account on the new subscription. To reduce disruption, communicate these steps in advance to users. For more information, see [Sync SharePoint files with the OneDrive sync client](https://support.microsoft.com/office/59b1de2b-519e-4d3a-8f45-51647cf291cd).

### OneNote

Ask users to:

- [Back up OneNote](https://support.microsoft.com/office/f58b34b0-611d-435e-87fa-7942a1767af4).
- [Restore notes from a backup](https://support.microsoft.com/office/5daf9cb0-6769-4998-a5de-f044fdd0d831) to their new account.
