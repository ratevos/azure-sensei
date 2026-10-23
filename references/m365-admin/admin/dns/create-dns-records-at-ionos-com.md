# Connect your DNS records at IONOS to Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-ionos-com  
> Microsoft doc last updated: 04/23/2026


 **[Check the Domains FAQ](../setup/domains-faq.yml)** if you don't find what you're looking for.

If IONOS is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Skype for Business Online, and so on.

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

- [**Use Domain Connect**](#use-domain-connect-to-verify-and-set-up-your-domain) If you haven't set up your domain with another email service provider, use the Domain Connect steps to automatically verify and set up your new domain to use with Microsoft 365.

    OR

- [**Use the manual steps**](#create-dns-records-with-manual-setup) Verify your domain using the following manual steps and choose when and which records to add to your domain registrar. This allows you to set up new MX (mail) records, for example, at your convenience.

## Use Domain Connect to verify and set up your domain

Follow these steps to automatically verify and set up your IONOS domain with Microsoft 365:

1. In the Microsoft 365 admin center, select **Settings** > <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">**Domains**</a>, and select the domain you want to set up.

    

1. Select the three dots (more actions) >  choose **Start setup**.

    

1. On the How do you want to connect your domain? page, select **Continue**.

1. On the Add DNS records page, select **Add DNS records**.

1. On the IONOS sign-in page, sign in to your account, and select **Connect**, and **Allow**.

    

    This completes your domain setup for Microsoft 365.

## Create DNS records with manual setup

After you add these records at IONOS, your domain will be set up to work with Microsoft services.

> [!CAUTION]
> IONOS doesn't allow a domain to have both an MX record and a top-level Autodiscover CNAME record. This limits the ways in which you can configure Exchange Online for Microsoft. There's a workaround, but we recommend employing it **only** if you already have experience with creating subdomains at IONOS.
> If despite this [service limitation](../setup/domains-faq.yml) you choose to manage your own Microsoft DNS records at IONOS, follow the steps in this article to verify your domain and to set up DNS records for email, Skype for Business Online, and so on.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

### Add a TXT record for verification

Before you use your domain with Microsoft, we have to make sure that you own it. Your ability to sign in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain.

> [!NOTE]
> This record is used only to verify that you own your domain; it doesn't affect anything else. You can delete it later, if you like.

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.

1. Select **Menu**, and then select **Domains and SSL**.

   

1. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

   

1. Select **Add record**.

    

1. Select the **TXT** section.

    

1. On the Add a DNS record page, in the boxes for the new record, type or copy and paste the values from the following table.

    |Host name|Value|TTL|
    |---|---|---|
    |(Leave this field blank)|MS=ms *XXXXXXXX*  <br/> NOTE: This is an example. Use your specific **Destination or Points to Address** value here, from the table. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|1 hour|

1. Select **Save**.

    

    Wait a few minutes before you continue, so that the record you just created can update across the Internet.

Now that you've added the record at your domain registrar's site, go back to Microsoft 365 and request Microsoft 365 to look for the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. In the admin center, go to the **Settings** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">**Domains**</a>.

1. On the Domains page, select the domain that you're verifying, and select **Start setup**.

    

1. Select **Continue**.

1. On the **Verify domain** page, select **Verify**.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

### Add an MX record so email for your domain will come to Microsoft

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.

1. Select **Menu**, and then select **Domains and SSL**.

   

1. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

   

1. Select **Add record**.

    

1. Select the **MX** section.

    

1. On the Add a DNS record page, in the boxes for the new record, type or copy and paste the values from the following table.

    |Host name|Points to|Priority|TTL|
    |---|---|---|---|
    |@|*\<domain-key\>*.mail.protection.outlook.com  <br/>  NOTE: Get your \<domain-key\> from your Microsoft account. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|10  <br/> For more information about priority, see [What is MX priority?](../setup/domains-faq.yml)|1 hour|

1. Select **Save**.

    

1. If there are any MX records already listed, delete each of them by selecting the **Delete record** trash can on the **Add record** page.

    

### Add the CNAME record required for Microsoft

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.

1. Select **Menu**, and then select **Domains and SSL**.

   

1. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

   

   Now you'll create two subdomains and set an **Alias** value for each.

   (This is required because IONOS supports only one top-level CNAME record, but Microsoft requires several CNAME records.)

   First, you'll create the Autodiscover subdomain.

1. Select **Subdomains**.

   

1. Select **Add subdomain**.

   

1. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    |Add subdomain|Alias|
    |---|---|
    |autodiscover|autodiscover.outlook.com|

1. Under **Actions** for the **autodiscover** subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.

1. Select **Add record**, and then select the **CNAME** section.

1. In the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    |Add subdomain|Alias|
    |---|---|
    |autodiscover|autodiscover.outlook.com|

1. Select **Save**.

## Add a TXT record for SPF to help prevent email spam

> [!IMPORTANT]
> You can't have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, and delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a  *single*  SPF record that includes both sets of values. Need examples? Check out these [External Domain Name System records for Microsoft](https://learn.microsoft.com/en-us/microsoft-365/enterprise/external-domain-name-system-records). To validate your SPF record, you can use one of these[SPF validation tools](../setup/domains-faq.yml).

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.

1. Select **Menu**, and then select **Domains and SSL**.

   

1. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

   

1. Select **Add record**.

    

1. Select the **SPF (TXT)** section.

    

1. In the boxes for the new record, type or copy and paste the values from the following table.

    |Type|Host name|Value|TTL|
    |---|---|---|---|
    |SPF (TXT)|(Leave this field empty.)|v=spf1 include:spf.protection.outlook.com -all  <br/> **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|1 hour|

1. Select **Save**.

   

## Advanced option: Skype for Business

Only select this option if your organization uses Skype for Business for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs four records: Two SRV records for user-to-user communication, and two CNAME records to sign-in and connect users to the service.

### Add two more CNAME records

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Sign in.

1. Select **Menu**, and then select **Domains and SSL**.

   

1. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

   

   Now you'll create two subdomains and set an **Alias** value for each.

   (This is required because IONOS supports only one top-level CNAME record, but Microsoft requires several CNAME records.)

   First, you'll create the lyncdiscover subdomain.

1. Select **Subdomains**.

   

1. Select **Add subdomain**.

   

1. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    |Add subdomain|Alias|
    |---|---|
    |lyncdiscover   |webdir.online.lync.com  |

1. Under **Actions** for the **lyncdiscover** subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.

1. Select **Add record**, and then select the **CNAME** section.

1. In the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    |Create Subdomain|Alias|
    |---|---|
    |lyncdiscover|webdir.online.lync.com|

1. Create another subdomain (SIP): Select **Add subdomain**.

1. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    |Add subdomain|Alias|
    |---|---|
    |sip|sipdir.online.lync.com|

1. Under **Actions** for the subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.

1. Select **Add record**.

    

1. Select the **CNAME** section.

1. in the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    |Create Subdomain|Alias|
    |---|---|
    |sip|sipdir.online.lync.com|

1. Select the check box for the **I am aware** disclaimer, and then select **Save**.

## Add the two SRV records required for Microsoft

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Sign in.

1. Select **Menu**, and then select **Domains and SSL**.

   

1. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

   

1. Select **Add record**.

    

1. Select the **SRV** section.

    

1. In the boxes for the new record, type or copy and paste the values from the following table.

    |Type|Service|Protocol|Host name|Points to|Priority|Weight|Port|TTL|
    |---|---|---|---|---|---|---|---|---|
    |SRV|_sip|tls|(Leave this field empty.)|sipdir.online.lync.com|100|1|443|1 hour|
    |SRV|_sipfederationtls|tcp|(Leave this field empty.)|sipfed.online.lync.com|100|1|5061|1 hour|

1. Select **Save**.

    

1. Add the other SRV record.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs two CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records

> [!IMPORTANT]
> Follow the subdomain procedure that you used for the other CNAME records, and supply the values from the following table.

1. To get started, go to your domains page at IONOS by using [this link](https://login.ionos.com/). Follow the prompt to sign in.

1. Select **Menu**, and then select **Domains and SSL**.

   

1. Under **Actions** for the domain that you want to update, select the gear control, and then select **DNS**.

   

   Now you'll create two subdomains and set an **Alias** value for each.

   (This is required because IONOS supports only one top-level CNAME record, but Microsoft requires several CNAME records.)

   First, you'll create the lyncdiscover subdomain.

1. Select **Subdomains**.

   

1. Select **Add subdomain**.

   

1. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    |Add subdomain|Alias|
    |---|---|
    |enterpriseregistration|enterpriseregistration.windows.net|

1. Under **Actions** for the **enterpriseregistration** subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.

1. Select **Add record**, and then select the **CNAME** section.

1. In the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    |Add subdomain|Alias|
    |---|---|
    |enterpriseregistration|enterpriseregistration.windows.net|

1. Create another subdomain: Select **Add subdomain**.

1. In the **Add subdomain** box for the new subdomain, type or copy and paste only the **Add subdomain** value from the following table. (You'll add the **Alias** value in a later step.)

    |Add subdomain|Alias|
    |---|---|
    |enterpriseenrollment|enterpriseenrollment-s.manage.microsoft.com|

1. Under **Actions** for the **enterpriseenrollment** subdomain that you created, select the gear control, and then select **DNS** from the drop-down list.

1. Select **Add record**.

    

1. Select the **CNAME** section.

1. in the **Alias:** box, type or copy and paste only the **Alias** value from the following table.

    |Create Subdomain|Alias|
    |---|---|
    |enterpriseenrollment|enterpriseenrollment-s.manage.microsoft.com|

1. Select the check box for the **I am aware** disclaimer, and then select **Save**.
