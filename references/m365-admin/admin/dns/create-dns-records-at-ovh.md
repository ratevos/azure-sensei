# Connect your DNS records at OVH to Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-ovh  
> Microsoft doc last updated: 04/23/2026


[Check the Domains FAQ](../setup/domains-faq.yml) if you don't find what you're looking for.

If OVH is your DNS hosting provider, follow the steps in this article to verify your domain and set up DNS records for email, Skype for Business Online, and so on.

After you add these records at OVH, your domain will be set up to work with Microsoft services.

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

1. To get started, go to your domains page in OVH by using [this link](https://www.ovh.com/manager/). You'll be prompted to log in.

    

1. On the dashboard landing page, under **View all my activity**, select the name of the domain that you want edit.

1. Select **DNS zone**.

    

1. Select **Add an entry**.

    

1. Select **TXT**

    

1. In the boxes for the new record, type or copy and paste the values from the following table. To assign a TTL value, choose **Custom** from the drop-down list, and then type the value in the text box.

   |Record type|Sub-domain|TTL|Value|
   |---|---|---|---|
   |TXT|(leave blank)|3600 (seconds)|MS=msxxxxxxxx  <br/> **Note:** This is an example. Use your specific **Destination or Points to Address** value here, from the table.  [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|

1. Select **Next**.

1. Select **Confirm**.

    

1. Wait a few minutes before you continue, so that the record you just created can update across the Internet.

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

1. To get started, go to your domains page in OVH by using [this link](https://www.ovh.com/manager/). You'll be prompted to log in.

    

1. On the dashboard landing page, under **View all my activity**, select the name of the domain that you want edit.

1. Select **DNS zone**.

    

1. Select **Add an entry**.

    

1. Select **MX**.

    

1. In the boxes for the new record, type or copy and paste the values from the following table. To assign a TTL value, choose **Custom** from the drop-down list, and then type the value in the text box.

    > [!NOTE]
    > By default OVH uses relative notation for the target, which adds the domain name to the end of the target record. To use absolute notation instead, add a dot to the target record as shown in the table below.

   |Sub-domain|TTL|Priority|Target|
   |---|---|---|---|
   |(leave blank)|3600 (seconds)|0  <br/> For more information about priority, see [What is MX priority?](../setup/domains-faq.yml)|\<domain-key\>.mail.protection.outlook.com.  <br/> **Note:** Get your *\<domain-key\>* from your Microsoft account. [How do I find this?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records)|

    

1. Select **Next**.

    

1. Select **Confirm**.

    

1. Delete any other MX records in the list on the **DNS zone** page. Select each record and, in the **Actions** column, select the trash-can **Delete** icon.

    

1. Select **Confirm**.

## Add the CNAME record required for Microsoft

1. To get started, go to your domains page in OVH by using [this link](https://www.ovh.com/manager/). You'll be prompted to log in.

    

1. On the dashboard landing page, under **View all my activity**, select the name of the domain that you want edit.

1. Select **DNS zone**.

    

1. Select **Add an entry**.

    

1. Select **CNAME**.

    

1. In the boxes for the new record, type or copy and paste the values from the first row of the following table. To assign a TTL value, choose **Custom** from the drop-down list, and then type the value in the text box.

   |Sub-domain|TTL|Target|
   |---|---|---|
   |autodiscover|3600 (seconds)|autodiscover.outlook.com.|

    

1. Select **Next**.

    

1. Select **Confirm**.

## Add a TXT record for SPF to help prevent email spam

> [!IMPORTANT]
> You cannot have more than one TXT record for SPF for a domain. If your domain has more than one SPF record, you'll get email errors, as well as delivery and spam classification issues. If you already have an SPF record for your domain, don't create a new one for Microsoft. Instead, add the required Microsoft values to the current record so that you have a  *single*  SPF record that includes both sets of values.

1. To get started, go to your domains page in OVH by using [this link](https://www.ovh.com/manager/). You'll be prompted to log in.

    

1. On the dashboard landing page, under **View all my activity**, select the name of the domain that you want edit.

1. Select **DNS zone**.

    

1. Select **Add an entry**.

    

1. Select **TXT**.

1. In the boxes for the new record, type or copy and paste the following values. To assign a TTL value, choose **Custom** from the drop-down list, and then type the value in the text box.

   |Sub-domain|TTL|Value|
   |---|---|---|
   |(leave blank)|3600 (seconds)|v=spf1 include:spf.protection.outlook.com -all  <br/**Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|

    

1. Select **Next**.

    

1. Select **Confirm**.

    

## Advanced option: Skype for Business

Only select this option if your organization uses Skype for Business for online communication services like chat, conference calls, and video calls, in addition to Microsoft Teams. Skype needs 4 records: 2 SRV records for user-to-user communication, and 2 CNAME records to sign-in and connect users to the service.

### Add the two required SRV records

1. To get started, go to your domains page in OVH by using [this link](https://www.ovh.com/manager/). You'll be prompted to log in.

    

1. On the dashboard landing page, under **View all my activity**, select the name of the domain that you want edit.

1. Select **DNS zone**.

    

1. Select **Add an entry**.

    

1. Select **SRV**.

1. In the boxes for the new record, type or copy and paste the following values. To assign a TTL value, choose **Custom** from the drop-down list, and then type the value in the text box.

   |Sub-domain|TTL (Seconds)|Priority|Weight|Port|Target|
   |---|---|---|---|---|---|
   |_sip._tls|3600 (s.)|100|1|443|sipdir.online.lync.com. **This value MUST end with a period (.)**><br> **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|
   |_sipfederationtls._tcp|3600 (s.)|100|1|5061|sipfed.online.lync.com. **This value MUST end with a period (.)**<br> **Note:** We recommend copying and pasting this entry, so that all of the spacing stays correct.|

1. To add the other SRV record, select **Add another record**, create a record using the values from the next row in the table, and then select **Create records**.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

### Add the two required CNAME records for Skype for Business

1. To get started, go to your domains page in OVH by using [this link](https://www.ovh.com/manager/). You'll be prompted to log in.

    

1. On the dashboard landing page, under **View all my activity**, select the name of the domain that you want edit.

1. Select **DNS zone**.

    

1. Select **Add an entry**.

    

1. Select **CNAME**.

    

1. In the boxes for the new record, type or copy and paste the values from the first row of the following table. To assign a TTL value, choose **Custom** from the drop-down list, and then type the value in the text box.

   |Sub-domain|TTL|Target|
   |---|---|---|
   |sip|3600 (s.)|sipdir.online.lync.com.  <br/> **This value MUST end with a period (.)**|
   |lyncdiscover|3600 (s.)|webdir.online.lync.com.  <br/> **This value MUST end with a period (.)**|

1. Select **Next**.

    

1. Select **Confirm**.

1. Add the other CNAME record.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Advanced option: Intune and Mobile Device Management for Microsoft 365

This service helps you secure and remotely manage mobile devices that connect to your domain. Mobile Device Management needs two CNAME records so that users can enroll devices to the service.

### Add the two required CNAME records for Mobile Device Management

1. To get started, go to your domains page in OVH by using [this link](https://www.ovh.com/manager/). You'll be prompted to log in.

    

1. On the dashboard landing page, under **View all my activity**, select the name of the domain that you want edit.

1. Select **DNS zone**.

    

1. Select **Add an entry**.

    

1. Select **CNAME**.

    

1. In the boxes for the new record, type or copy and paste the values from the first row of the following table. To assign a TTL value, choose **Custom** from the drop-down list, and then type the value in the text box.

   |Sub-domain|TTL|Target|
   |---|---|---|
   |enterpriseregistration  <br/>|3600 (s.)|enterpriseregistration.windows.net.  <br/> **This value MUST end with a period (.)**|
   |enterpriseenrollment|3600 (s.)|enterpriseenrollment-s.manage.microsoft.com.  <br/> **This value MUST end with a period (.)**|

1. Select **Next**.

    

1. Select **Confirm**.

1. Add the other CNAME record.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).
