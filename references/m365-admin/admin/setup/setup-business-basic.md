# Set up Microsoft 365 Business Basic

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/setup-business-basic  
> Microsoft doc last updated: 04/27/2026


For more small business content, see [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).

## Activate your Microsoft 365 Business Basic subscription

Use these steps to confirm your subscription is active and ready for users.

> [!NOTE]
> If you bought a nonprofit offer, sign in to the [Nonprofit Hub](https://nonprofit.microsoft.com/) to claim or activate your nonprofit offer. Then return to the Microsoft 365 admin center to verify that the subscription appears under **Billing** > **Your products**. If the nonprofit offer still doesn't appear, use the [Microsoft nonprofit support Contact Us form](https://nonprofit.microsoft.com/contactus).

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. In the admin center, go to **Billing** > **Your products**.

1. Verify that **Microsoft 365 Business Basic** shows **Active**.

1. Go to **Users** > **Active users**, and assign available Business Basic licenses to your users.

1. In the admin center Home page, select **Dashboard view**, and then select **Go to guided setup** to complete domain, email, and app setup.

## Add an existing domain to your Microsoft 365 Business Basic subscription

When you purchase Microsoft 365 Business Basic, you can use a domain you own or buy one during the sign-up process.

- If you purchase a new domain during sign-up, your domain is all set up and you can move to [Add users and assign licenses](#add-users-and-assign-licenses).

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. In the admin center Home page, select **Dashboard view**, and then select **Go to guided setup** to start the wizard.

1. In the **Add domain** step, enter the domain name you want to use (like contoso.com).

    > [!IMPORTANT]
    > If you purchase a domain during sign-up, you don't see the **Add a domain** step. Instead, go to [Add users](#add-users-and-assign-licenses).

1. Follow the steps in the wizard to [Add DNS records to connect your domain](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider) that verifies you own the domain. If you know your domain host, see also [Add a domain to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain).

    If your hosting provider is GoDaddy or another host that is enabled with [domain connect](https://learn.microsoft.com/en-us/office365/admin/get-help-with-domains/domain-connect), the process is easy and you're automatically asked to sign in and let Microsoft authenticate on your behalf.

    
   
## Add users and assign licenses

You can add users in the wizard, but you can also [add users later](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users) in the admin center.

Any users you add in the wizard automatically get assigned a Microsoft 365 Business Basic license.

1. If your Microsoft 365 Business Basic subscription has existing users (for example, if you used Microsoft Entra Connect), you get an option to assign licenses to them now. Go ahead and add licenses to them as well.

1. After you add the users, you also get an option to share credentials with the new users you added. You can choose to print them out, email them, or download them.

## Connect your domain

> [!NOTE]
> If you choose to use the .onmicrosoft domain, or use Microsoft Entra Connect to set up users, you don't see this step.
  
To set up services, you have to update some records at your DNS host or domain registrar.
  
1. The setup wizard typically detects your registrar and gives you a link to step-by-step instructions for updating your NS records at the registrar website. If it doesn't, [Change nameservers to set up Microsoft 365 with any domain registrar](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/change-nameservers-at-any-domain-registrar).

    - If you have existing DNS records, for example an existing website, but your DNS host is enabled for [domain connect](https://learn.microsoft.com/en-us/office365/admin/get-help-with-domains/domain-connect), choose **Add records for me**. On the **Choose your online services** page, accept all the defaults, and choose **Next**. Choose **Authorize** on your DNS host's page.
    - If you have existing DNS records with other DNS hosts (not enabled for domain connect), you need to manage your own DNS records to make sure the existing services stay connected. See [domain basics](https://learn.microsoft.com/en-us/office365/admin/get-help-with-domains/dns-basics) for more info.

1. Follow the steps in the wizard and email and other services are set up for you.

    When the signup process is complete, you're directed to the admin center, where you can add users, and assign licenses. After you complete the initial setup, you can use the **Setup** page in the admin center to continue setting up and configuring the services that come with your subscriptions.

    For more information about the setup wizard and the admin center **Setup** page, see [Difference between the setup wizard and the Setup page](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/o365-setup-wizard-and-setup-page).

## Watch: Set up business email with a new domain

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=e06209e9-487f-4f5c-be79-d658aca544be]

## Steps: Set up business email with a new domain

1. From the **How you'll sign in** page on the Microsoft 365 Business Standard sign up, choose **Create a new business email account (advanced)**.

1. Follow the steps to buy a new domain and enter the domain name you want to use (like contoso.com). After you complete buying your domain, you can [add users and licenses](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users) and install your Microsoft 365 productivity apps in the admin center.

## Finish setting up

Follow the steps in this section to set up Outlook, Teams, OneDrive, and your website.

### Step: Set up Outlook for email

1. On the Windows Start menu, search for Outlook, and select it.

    (If you're using a Mac, open Outlook from the toolbar or locate it using the Finder.)

    On the Welcome page, select **Next**.

1. Choose **File** \> **Info** \> **Add Account**.

1. Enter your Microsoft email address and select **Connect**.

## Watch: Set up Outlook for email

> [!VIDEO e30573c6-b0d5-4007-8ff6-8c9dfd4e39fe]
  
More at [Set up Outlook for email](https://support.microsoft.com/office/f5bf0cd1-e1f3-4b0d-a022-ecab17efe86f).
  
### Import email

If you used Outlook with another email account, you can import your previous email, calendar, and contacts into your new Microsoft account.
  
1. **Export your old email**

    In Outlook, select **File** \> **Open & Export** \> **Import/Export**.

    Select **Export to a File** and then follow the steps to export your Outlook Data File (.pst) and any subfolders.

1. **Import your old email**

    In Outlook, select **File** \> **Open & Export** \> **Import/Export**.

    Select **Import from another program or file** and follow the steps to import the backup file you created when you exported your old email.

## Watch: Import and redirect email

> [!VIDEO 9efe5ae1-1dec-4f2c-8ea5-fef10843388e]
  
More at [Import email with Outlook](https://support.microsoft.com/office/6a3771d4-4c1d-4a25-92a6-0b8e476335de).

You can also use <a href="https://go.microsoft.com/fwlink/p/?linkid=2059104" target="_blank">Exchange admin center</a> to import everyone's email. For more information, see [migrate multiple email accounts](https://learn.microsoft.com/en-us/Exchange/mailbox-migration/mailbox-migration).

## Set up Microsoft Teams and OneDrive

Select the OneDrive cloud icon from your taskbar and follow the steps to move your files to your new OneDrive folder. To set up Microsoft Teams select **Next**.

1. Open Microsoft Teams, select your profile icon, and then **Add work or school account**. To add your new account to Teams, follow the steps that appear after selecting **Add work or school account**.

## Use a public website

Microsoft 365 doesn't include a public website for your business. If you want to set one up, consider using a Microsoft partner, such as GoDaddy or WIX.
  
1. From the admin center, go to **Resources**, and then select **Public website**.

1. Select **Learn more** under one of the options, and then sign up with a website partner and use their tools to set up and design your site.

## Watch: Create your business website

> [!VIDEO d89ace24-5e06-4858-81bf-512300be5d78]

## Invite users to join your subscription and organization

Once you set up your organization, you can invite other users to join your Microsoft 365 business subscription. They get access to all the features of the subscription.

[Invite users to my subscription](https://learn.microsoft.com/en-us/microsoft-365/admin/simplified-signup/admin-invite-business-standard)

To join your organization and subscription, see the following articles:

- [Accept an email invitation](https://learn.microsoft.com/en-us/microsoft-365/admin/simplified-signup/user-invite-business-standard)

- [Accept an email invitation using an Outlook, Yahoo, Gmail, or other account (User)](https://learn.microsoft.com/en-us/microsoft-365/admin/simplified-signup/user-invite-msa-nodomain-join)

## Related topics

[Migrate data to my Microsoft 365 Business Standard subscription](https://learn.microsoft.com/en-us/microsoft-365/admin/simplified-signup/migrate-data-business-standard)
