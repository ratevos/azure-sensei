# Connect your DNS records at web.com to Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-web-com  
> Microsoft doc last updated: 04/23/2026


 **[Check the Domains FAQ](../setup/domains-faq.yml)** if you don't find what you're looking for.

If web.com is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Skype for Business Online, and so on.

After you add these records at web.com, your domain will be set up to work with Microsoft services.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

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

## Change your domain's nameserver (NS) records

> [!IMPORTANT]
> You must perform this procedure at the domain registrar where you purchased and registered your domain.

When you signed up for web.com, you added a domain by using the web.com **Setup** process.

To verify and create DNS records for your domain in Microsoft, you first need to change the nameservers at your domain registrar so that they use the web.com nameservers.

To change your domain's name servers at your domain registrar's website yourself, follow these steps.

1. Find the area on the domain registrar's website where you can edit the nameservers for your domain.

2. Either create two nameserver records by using the values in the following table, or edit the existing nameserver records so that they match these values.

    |Type|Value|
    |---|---|
    |First nameserver|Use the nameserver value provided by web.com.|
    |Second nameserver|Use the nameserver value provided by web.com.|

    > [!TIP]
    > You should use at least two name server records. If there are any other name servers listed, you should delete them.

3. Save your changes.

> [!NOTE]
> Your nameserver record updates may take up to several hours to update across the Internet's DNS system. Then your Microsoft email and other services will be all set to work with your domain.

## Add a TXT record for verification

Before you use your domain with Microsoft, we have to make sure that you own it. Your ability to log in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain.

> [!NOTE]
> This record is used only to verify that you own your domain; it doesn't affect anything else. You can delete it later, if you like.

1. To get started, go to your domains page at web.com by using [this link](https://checkout.web.com/manage-it/index.jsp). Log in first.

1. On the landing page, select **Domain Names**.

1. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    

1. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.

    

1. On the Manage Advanced DNS Records page, select **+ ADD RECORD**.

    

1. Under **Type**, select **TXT** from the drop-down list.

    

1. Select, or copy and paste, the values from the following table.

    |Refers|TXT value|TTL|
    |---|---|:----|
    |@|MS=ms*XXXXXXXX* <br/> **Note:** This is an example. Use your specific **Destination or Points to Address** value here, from the table. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|1 Hour|

1. Select **ADD**.

    Wait a few minutes before you verify your new TXT record, so that the record you just created can update across the Internet.

Now that you've added the record at your domain registrar's site, you'll go back to Microsoft and request the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. In the admin center, go to the **Settings** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">**Domains**</a>.

1. On the Domains page, select the domain that you're verifying, and select **Start setup**.

    

1. Select **Continue**.

1. On the **Verify domain** page, select **Verify**.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Add an MX record so email for your domain will come to Microsoft

1. To get started, go to your domains page at web.com by using [this link](https://checkout.web.com/manage-it/index.jsp). Log in first.

1. On the landing page, select **Domain Names**.

1. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    

1. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.

    

1. On the Manage Advanced DNS Records page, select **+ ADD RECORD**.

    

1. Under **Type**, select **MX** from the drop-down list.

1. Select, or copy and paste, the values from the following table.

    |Refers to|Mail server|Priority|TTL|
    |---|---|---|---|
    |@|*\<domain-key\>*.mail.protection.outlook.com <br/> **Note:** Get your *\<domain-key\>* from the Microsoft admin center. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|For more information about priority, see [What is MX priority?](../setup/domains-faq.yml) <br/> 1|1 Hour|

1. Select **ADD**.

    

1. If there are any other MX records, delete all of them by selecting the edit tool, and then **Delete** for each record.

    

## Add the CNAME record required for Microsoft

1. To get started, go to your domains page at web.com by using [this link](https://checkout.web.com/manage-it/index.jsp). Log in first.

1. On the landing page, select **Domain Names**.

1. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    

1. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.

    

1. On the Manage Advanced DNS Records page, select **+ ADD RECORD**.

    

1. Under **Type**, select **CNAME** from the drop-down list.

    

1. Select, or copy and paste, the values from the following table.

    |Refers to|Host name|Alias to|TTL|
    |---|---|---|---|
    |Other Host|autodiscover|autodiscover.outlook.com|1 Hour|

    

1. Select **ADD**.

## Add a TXT record for SPF to help prevent email spam

> [!IMPORTANT]
> You cannot have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, as well as delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a *single* SPF record that includes both sets of values.

1. To get started, go to your domains page at web.com by using [this link](https://checkout.web.com/manage-it/index.jsp). Log in first.

1. On the landing page, select **Domain Names**.

1. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    

1. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.

    

1. On the Manage Advanced DNS Records page, select **+ ADD RECORD**.

    

1. Under **Type**, select **TXT** from the drop-down list.

    

1. Select, or copy and paste, the values from the following table.

    |Refers to|TXT value|TTL|
    |---|---|---|
    |@|v=spf1 include:spf.protection.outlook.com -all <br/> **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|1 Hour|

1. Select **ADD**.

## Advanced option: Skype for Business

Only select this option if your organization uses Skype for Business for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs 4 records: 2 SRV records for user-to-user communication, and 2 CNAME records to sign-in and connect users to the service.

### Add the two required SRV records

1. To get started, go to your domains page at web.com by using [this link](https://checkout.web.com/manage-it/index.jsp). Log in first.

1. On the landing page, select **Domain Names**.

1. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    

1. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.

    

1. On the Manage Advanced DNS Records page, select **+ ADD RECORD**.

    

1. Under **Type**, select **SRV** from the drop-down list.

    

1. Select, or copy and paste, the values from the following table.

    |Type|Service|Protocol|Weight|Port|Target|Priority|TTL|
    |---|---|---|---|---|---|---|---|
    |SRV|_sip|TLS|100|443|sipdir.online.lync.com <br/> **This value CANNOT end with a period (.)**|1|1 Hour|
    |SRV|_sipfederationtls|TCP|100|5061|sipfed.online.lync.com <br/> **This value CANNOT end with a period (.)**|1|1 Hour|

    

1. Select **ADD**.

1. Add the other SRV record by copying the values from the second row of the table.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

### Add the two required CNAME records for Skype for Business

1. To get started, go to your domains page at web.com by using [this link](https://checkout.web.com/manage-it/index.jsp). Log in first.

1. On the landing page, select **Domain Names**.

1. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    

1. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.

1. On the Manage Advanced DNS Records page, select **+ ADD RECORD**.

    

1. Under **Type**, select **CNAME** from the drop-down list.

    

1. Select, or copy and paste, the values from the following table.

    |Type|Refers to|Host Name|Alias to|TTL|
    |---|---|---|---|---|
    |CNAME|Other Host|sip|sipdir.online.lync.com <br/> **This value CANNOT end with a period (.)**|1 Hour|
    |CNAME|Other Host|lyncdiscover|webdir.online.lync.com <br/> **This value CANNOT end with a period (.)**|1 Hour|

    

1. Select **ADD**.

1. Add the other CNAME record by copying the values from the second row of the table.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs 2 CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records for Mobile Device Management

1. To get started, go to your domains page at web.com by using [this link](https://checkout.web.com/manage-it/index.jsp). Log in first.

1. On the landing page, select **Domain Names**.

1. Under **Actions**, select the three dots, and then select **Manage** in the drop-down list.

    

1. Scroll down to select **Advanced Tools**, and next to **Advanced DNS Records**, select **MANAGE**.

    You might have to select **Continue** to get to the Manage Advanced DNS Records page.

    

1. On the Manage Advanced DNS Records page, select **+ ADD RECORD**.

    

1. Under **Type**, select **CNAME** from the drop-down list.

    

1. Select, or copy and paste, the values from the following table.

    |Type|Refers to|Host Name|Alias to|TTL|
    |---|---|---|---|---|
    |CNAME|Other Host|enterpriseregistration|enterpriseregistration.windows.net <br/> **This value CANNOT end with a period (.)**|1 Hour|
    |CNAME|Other Host|enterpriseenrollment|enterpriseenrollment-s.manage.microsoft.com <br/> **This value CANNOT end with a period (.)**|1 Hour|

    

1. Select **ADD**.

1. Add the other CNAME record by copying the values from the second row of the table.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).
