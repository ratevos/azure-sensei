# Connect your DNS records at Cloudflare to Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-cloudflare  
> Microsoft doc last updated: 04/23/2026


 **[Check the Domains FAQ](../setup/domains-faq.yml)** if you don't find what you're looking for.

If Cloudflare is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Skype for Business Online, and so on.

> [!TIP]
>
> Some configuration tasks might be complex to perform. For technical support, follow these steps:
>
> 1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
> 1. At the bottom right, select **Help & Support**.
> 1. In the **Support Assistant** pane that opens, enter your question.
> 1. Review the results. If you still have questions, select **Contact support**.
>
> To learn about your options for contacting support, see [Get support for Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-support).

## Before you begin

You have two options for setting up DNS records for your domain:

- [**Use Domain Connect**](#use-domain-connect-to-verify-and-set-up-your-domain) If you haven't set up your domain with another email service provider, use the **Domain Connect** steps to automatically verify and set up your new domain to use with Microsoft 365.

    OR

- [**Use the manual steps**](#create-dns-records-with-manual-setup) Verify your domain using the manual steps below and choose when and which records to add to your domain registrar. This allows you to set up new MX (mail) records, for example, at your convenience.

## Use Domain Connect to verify and set up your domain

Follow these steps to automatically verify and set up your Cloudflare domain with Microsoft 365:

1. In the Microsoft 365 admin center, select **Settings** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">**Domains**</a>, and select the domain you want to set up.

1. Select the three dots (more actions) \> choose **Manage DNS**.

1. On the How do you want to connect your domain? page, select **Continue**.

1. On the Add DNS record page, select **Add DNS records**.

1. On the Cloudflare login page, sign in to your account, and select **Authorize**.

    This completes your domain setup for Microsoft 365.

## Create DNS records with manual setup

After you add these records at Cloudflare, your domain will be set up to work with Microsoft 365 services.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

### Change your domain's nameserver (NS) records

> [!IMPORTANT]
> You must perform this procedure at the domain registrar where you purchased and registered your domain.

When you signed up for Cloudflare, you added a domain by using the Cloudflare Setup process.

The domain that you added was purchased from Cloudflare or a separate domain registrar. To verify and create DNS records for your domain in Microsoft 365, you first need to change the nameservers at your domain registrar so that they use the Cloudflare nameservers.

To change your domain's name servers at your domain registrar's website yourself, follow these steps.

1. Find the area on the domain registrar's website where you can edit the nameservers for your domain.

2. Either create two nameserver records by using the values in the following table, or edit the existing nameserver records so that they match these values.

    |Type|Value|
    |---|---|
    |First nameserver|Use the nameserver value provided by Cloudflare.|
    |Second nameserver|Use the nameserver value provided by Cloudflare.|

    > [!TIP]
    > You should use at least two name server records. If there are any other name servers listed, you should delete them.

3. Save your changes.

> [!NOTE]
> Your nameserver record updates may take up to several hours to update across the Internet's DNS system. Then your Microsoft email and other services will be all set to work with your domain.

### Add a TXT record for verification

Before you use your domain with Microsoft, we have to make sure that you own it. Your ability to log in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain.

> [!NOTE]
> This record is used only to verify that you own your domain; it doesn't affect anything else. You can delete it later, if you like.

1. Make sure you have added a domain in the Microsoft 365 Admin Center using the steps in [Add a domain](https://learn.microsoft.com/en-us/admin/setup/add-domain#add-a-domain), and that the domain has not already been verified. You'll need to copy the **TXT value** from the **Add a record to verify ownership** page for use later in this procedure.

1. To get started, go to your domains page at Cloudflare by using [this link](https://www.cloudflare.com/a/login). You'll be prompted to log in first.

1. On the Account Home page, find the domain that you want to update, select the three dots (**...**) at the right and select **Configure DNS** from the drop-down menu.

    

1. On the DNS management page, select **+Add record**.

   

1. Select the TXT type from the drop-down list, and type or copy and paste the values from this table. You'll use the TXT value (MS=ms*XXXXXXXX*) that you copied earlier.

    |Type|Name|TTL|Content|
    |---|---|---|:----|
    |TXT|@|30 minutes|MS=ms*XXXXXXXX* <br/> **Note:** This is an example. Use your specific **Destination or Points to Address** value here, from the table. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|

1. Select **Save**.

   

   Wait a few minutes before you continue, so that the record you just created can update across the Internet.

Now that you've added the record at your domain registrar's site, you'll go back to Microsoft and search for the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. In the admin center, go to the **Settings** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">**Domains**</a>.

1. On the Domains page, select the domain that you're verifying, and select **Manage DNS**.

1. Select **Continue**.

1. On the **Verify domain** page, select **Verify**.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

### Add an MX record so email for your domain will come to Microsoft

1. To get started, go to your domains page at Cloudflare by using [this link](https://www.cloudflare.com/a/login). You'll be prompted to log in first.

1. On the Account Home page, find the domain that you want to update, select the three dots (**...**) at the right and select **Configure DNS** from the drop-down menu.

   

1. On the DNS management page, select **+Add record**.

   

1. Select the MX type from the drop-down list, and type or copy and paste the values from this table.

   |Type|Name|Mail server|TTL|Priority|
   |---|---|---|---|---|
   |MX|@|*\<domain-key\>*.mail.protection.outlook.com <br/> **Note:** Get your *\<domain-key\>* from your Microsoft 365 account. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|30 minutes|1 <br/> For more information about priority, see [What is MX priority?](../setup/domains-faq.yml) <br/>|

1. Select **Save**.

   

1. If there are any other MX records listed in the **MX Records** section, delete them by selecting **Edit**, and then select **Delete**.

   

1. In the confirmation dialog box, select **Delete** to confirm your changes.

### Add the CNAME record required for Microsoft

1. To get started, go to your domains page at Cloudflare by using [this link](https://www.cloudflare.com/a/login). You'll be prompted to log in first.

1. On the Account Home page, find the domain that you want to update, select the three dots (**...**) at the right and select **Configure DNS** from the drop-down menu.

   

1. On the **DNS management** page, select **+Add record**

   

1. Select the CNAME type from the drop-down list, and type or copy and paste the values from this table.

    |Type|Name|Target|TTL|
    |---|---|---|---|
    |CNAME|autodiscover|autodiscover.outlook.com|Auto|

1. Select **Save**.

   

### Add a TXT record for SPF to help prevent email spam

> [!IMPORTANT]
> You cannot have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, as well as delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft 365. Instead, add the required Microsoft 365 values to the current record so that you have a *single* SPF record that includes both sets of values.

1. To get started, go to your domains page at Cloudflare by using [this link](https://www.cloudflare.com/a/login). You'll be prompted to log in first.

1. On the Account Home page, find the domain that you want to update, select the three dots (**...**) at the right and select **Configure DNS** from the drop-down menu.

    

1. On the DNS management page, select **+Add record**.

   

1. Select the TXT type from the drop-down list, and type or copy and paste the values from this table.

    |Type|Name|TTL|Content|
    |---|---|---|---|
    |TXT|@|30 minutes|v=spf1 include:spf.protection.outlook.com -all <br/> **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|

1. Select **Save**.

   

## Advanced option: Skype for Business

Only select this option if your organization uses Skype for Business for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs 4 records: 2 SRV records for user-to-user communication, and 2 CNAME records to sign-in and connect users to the service.

### Add the two required SRV records

> [!IMPORTANT]
> Keep in mind that Cloudflare is responsible for making this functionality available. In case you see discrepancies between the steps below and the current Cloudflare GUI (Graphical User Interface), leverage the [Cloudflare Community](https://community.cloudflare.com/).

1. To get started, go to your domains page at Cloudflare by using [this link](https://www.cloudflare.com/a/login). You'll be prompted to log in first.

1. On the Account Home page, find the domain that you want to update, select the three dots (**...**) at the right and select **Configure DNS** from the drop-down menu.

    

1. On the DNS management page, select **+Add record**

   

1. Select the SRV type from the drop-down list, and type or copy and paste the values from this table.

    |Type|Name|Service|Protocol|TTL|Priority|Weight|Port|Target|
    |---|---|---|---|---|---|---|---|---|
    |SRV|Use your *domain_name*; for example, contoso.com|_sip|TLS|30 minutes|100|1|443|sipfed.online.lync.com|
    |SRV|Use your *domain_name*; for example, contoso.com|_sipfederationtls|TCP|30 minutes|100|1|5061|sipfed.online.lync.com|

1. Select **Save**.

   

1. Add the other SRV record by copying the values from the second row of the table.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

### Add the two required CNAME records for Skype for Business

1. To get started, go to your domains page at Cloudflare by using [this link](https://www.cloudflare.com/a/login). You'll be prompted to log in first.

1. On the Account Home page, find the domain that you want to update, select the three dots (**...**) at the right and select **Configure DNS** from the drop-down menu.

    

1. On the DNS management page, select **+Add record**

   

1. Select the CNAME type from the drop-down list, and type or copy and paste the values from this table.

    |Type|Name|Target|TTL|
    |---|---|---|---|
    |CNAME|sip|sipdir.online.lync.com <br/>|1 Hour|
    |CNAME|lyncdiscover|webdir.online.lync.com <br/>|1 Hour|

1. Select **Save**.

1. Add the other CNAME record by copying the values from the second row of the table.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs 2 CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records for Mobile Device Management

1. To get started, go to your domains page at Cloudflare by using [this link](https://www.cloudflare.com/a/login). You'll be prompted to log in first.

1. On the Account Home page, find the domain that you want to update, select the three dots (**...**) at the right and select **Configure DNS** from the drop-down menu.

    

1. On the DNS management page, select **+Add record**

   

1. Select the CNAME type from the drop-down list, and type or copy and paste the values from this table.

    |Type|Name|Target|TTL|
    |---|---|---|---|
    |CNAME|enterpriseregistration|enterpriseregistration.windows.net <br/>|1 Hour|
    |CNAME|enterpriseenrollment|enterpriseenrollment-s.manage.microsoft.com <br/>|1 Hour|

1. Select **Save**.

1. Add the other CNAME record by copying the values from the second row of the table.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).
