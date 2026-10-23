# Connect your DNS records at 123-reg.co.uk to Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-123-reg-co-uk  
> Microsoft doc last updated: 04/23/2026


 **[Check the Domains FAQ](../setup/domains-faq.yml)** if you don't find what you're looking for.

If 123-reg.co.uk is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Skype for Business Online, and so on.

After you add these records at 123-reg.co.uk, your domain will be set up to work with Microsoft services.

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

## Add a TXT record for verification

Before you use your domain with Microsoft, we have to make sure that you own it. Your ability to log in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain.

> [!NOTE]
> This record is used only to verify that you own your domain; it doesn't affect anything else. You can delete it later, if you like.

1. To get started, go to your domains page at 123-reg.co.uk and follow the prompt to log in.

2. Select **Domains**, and on the Domain name overview page, select the name of the domain that you want to verify or go to Control panel.

   

3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

   

4. On the Manage your DNS page, select the **Advanced DNS** tab.

   

5. In the **Type** box for the new record choose **TXT/SPF** from the drop-down list, and then type or copy and paste the other values from the following table.

    |Hostname|Type|Destination TXT/SPF|
    |---|---|---|
    |@|TXT/SPF|MS=ms*XXXXXXXX* <br/> **Note:** This is an example. Use your specific **Destination or Points to Address** value here, from the table. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|

   

6. Select **Add**.

   

   Wait a few minutes before you continue, so that the record you just created can update across the Internet.

Now that you've added the record at your domain registrar's site, you'll go back to Microsoft and request a search for the record. When Microsoft finds the correct TXT record, your domain is verified.

To verify the record in Microsoft 365:

1. In the admin center, go to the **Settings** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">**Domains**</a>.

1. On the Domains page, select the domain that you're verifying, and select **Start setup**.

    

1. Select **Continue**.

1. On the **Verify domain** page, select **Verify**.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Add an MX record so email for your domain will come to Microsoft

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.

2. On the Domain name overview page, select the name of the domain that you want to edit.

   

3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

   

4. On the Manage your DNS page, select the **Advanced DNS** tab.

   

5. In the **Type** box for the new record choose **MX** from the drop-down list, and then type or copy and paste the other values from the following table.

    |Hostname|Type|Priority|Destination MX|
    |---|---|---|---|
    |@|MX|1 <br/> For more information about priority, see [What is MX priority?](../setup/domains-faq.yml)|*\<domain-key\>*.mail.protection.outlook.com. <br/> **This value MUST end with a period (.)** <br/> **Note:** Get your \<domain-key\> from your Microsoft account. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|

   

6. Select **Add**.

   

7. If there are any other MX records, remove each one by selecting the **Delete (trash can)** icon for that record.

   

## Add the CNAME record required for Microsoft

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.

2. On the Domain name overview page, select the name of the domain that you want to edit.

   

3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

   

4. On the Manage your DNS page, select the **Advanced DNS** tab.

   

5. Add the CNAME record.

    In the **Type** box for the new record choose **CNAME** from the drop-down list, and then type or copy and paste the other values from the following table.

    |Hostname|Type|Destination CNAME|
    |---|---|---|
    |autodiscover|CNAME|autodiscover.outlook.com. <br/> **This value MUST end with a period (.)**|

   

6. Select **Add**.

   

## Add a TXT record for SPF to help prevent email spam

> [!IMPORTANT]
> You cannot have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, as well as delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a *single* SPF record that includes both sets of values. Need examples? Check out these [External Domain Name System records for Microsoft](https://learn.microsoft.com/en-us/microsoft-365/enterprise/external-domain-name-system-records). To validate your SPF record, you can use one of these [SPF validation tools](../setup/domains-faq.yml).

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.

2. On the Domain name overview page, select the name of the domain that you want to edit.

   

3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

   

4. On the Manage your DNS page, select the **Advanced DNS** tab.

   

5. In the **Type** box for the new record choose **TXT/SPF** from the drop-down list, and then type or copy and paste the other values from the following table.

    |Hostname|Type|Destination TXT/SPF|
    |---|---|---|
    |@|TXT/SPF|v=spf1 include:spf.protection.outlook.com -all <br/> **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|

   

6. Select **Add**.

## Advanced option: Skype for Business

Only select this option if your organization uses Skype for Business for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs 4 records: 2 SRV records for user-to-user communication, and 2 CNAME records to sign-in and connect users to the service.

### Add the two required SRV records

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.

2. On the Domain name overview page, select the name of the domain that you want to edit.

   

3. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

   

4. On the Manage your DNS page, select the **Advanced DNS** tab.

   

5. Add the first of the two SRV records:

   In the **Type** box for the new record choose **SRV** from the drop-down list, and then type or copy and paste the other values from the following table.

    |Hostname|Type|Priority|TTL|Destination SRV|
    |---|---|---|---|---|
    |_sip._tls|SRV|100|3600|1 443 sipdir.online.lync.com. **This value MUST end with a period (.)** <br/> **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|
    |_sipfederationtls._tcp|SRV|100|3600|1 5061 sipfed.online.lync.com. **This value MUST end with a period (.)** <br/> **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|

   

6. Select **Add**.

   

7. Add the other SRV record.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

### Add the two required CNAME records for Skype for Business

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.

1. On the Domain name overview page, select the name of the domain that you want to edit.

   

1. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

   

1. On the Manage your DNS page, select the **Advanced DNS** tab.

   

1. Add the first CNAME record.

    In the **Type** box for the new record choose **CNAME** from the drop-down list, and then type or copy and paste the other values from the following table.

    |Hostname|Type|Destination CNAME|
    |---|---|---|
    |sip|CNAME|sipdir.online.lync.com. <br/> **This value MUST end with a period (.)**|
    |lyncdiscover|CNAME|webdir.online.lync.com. <br/> **This value MUST end with a period (.)**|

   

1. Select **Add**.

   

1. Add the other CNAME record.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs two CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records for Mobile Device Management

1. To get started, go to your domains page at 123-reg.co.uk. You'll be prompted to log in first.

1. On the Domain name overview page, select the name of the domain that you want to edit.

   

1. On the Manage domain page, under **Advanced domain settings**, choose **Manage DNS**.

   

1. On the Manage your DNS page, select the **Advanced DNS** tab.

   

1. Add the first CNAME record.

    In the **Type** box for the new record choose **CNAME** from the drop-down list, and then type or copy and paste the other values from the following table.

   |Hostname|Type|Destination CNAME|
   |---|---|---|
   |enterpriseregistration|CNAME|enterpriseregistration.windows.net. <br/> **This value MUST end with a period (.)**|
   |enterpriseenrollment|CNAME|enterpriseenrollment.manage.microsoft.com. <br/> **This value MUST end with a period (.)**|

   

1. Select **Add**.

   

1. Add the other CNAME record.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).
