# Connect DNS records at Namecheap to Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-namecheap  
> Microsoft doc last updated: 04/23/2026


If Namecheap hosts your domain's DNS, follow the steps in this article to verify domain ownership and manually add the DNS records required for Microsoft 365 services such as email, Microsoft Teams, and device management. After you add these records at Namecheap, your domain is ready to work with Microsoft 365.

This article covers the creation of the following DNS records at Namecheap:

| **Service**                                                                                                                  | **DNS record types** |
| ---------------------------------------------------------------------------------------------------------------------------- |--------------------- |
| [**Domain verification**](create-dns-records-at-namecheap.md?&tabs=domain-verify#add-microsoft-365-dns-records-at-namecheap) | TXT                  |
| [**Email**](create-dns-records-at-namecheap.md?&tabs=email#add-microsoft-365-dns-records-at-namecheap)                       | MX, CNAME (Autodiscover), TXT (SPF) |
| [**Microsoft Teams**](create-dns-records-at-namecheap.md?&tabs=teams#add-microsoft-365-dns-records-at-namecheap)             | SRV (2), CNAME (2)   |
| [**Microsoft Intune/MDM**](create-dns-records-at-namecheap.md?&tabs=intune-mdm#add-microsoft-365-dns-records-at-namecheap)   | CNAME (2)            |

> [!NOTE]
>
> Namecheap is a non-Microsoft site. Microsoft doesn't control the Namecheap site. Additionally, Namecheap might change their website and tools so that the steps in this article are no longer valid. For support with Namecheap's site and tools, contact Namecheap support.

## Before you begin

- You must own a domain registered with Namecheap.
- You must add the domain in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). If the domain isn't added in the Microsoft 365 admin center, follow the steps in [Add a domain](https://learn.microsoft.com/en-us/admin/setup/add-domain#add-a-domain) to add your domain before you start adding DNS records at Namecheap.

> [!NOTE]
>
> When creating or updating DNS records, it typically takes about 15 minutes for DNS changes to take effect. However, it can occasionally take longer for a DNS record change to update across the Internet's DNS system. If you're having trouble with mail flow or other issues after adding DNS records, see [Find and fix issues after adding your domain or DNS records](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/find-and-fix-issues).

## Sign in to Namecheap to manage your domain's DNS records

To add DNS records at Namecheap, sign in to your Namecheap account and then go to the page where you can manage your domain's DNS records. Follow these steps to get there:

1. Sign in to your Namecheap domains page by going to the Namecheap [Log in to your account](https://www.namecheap.com/myaccount/login.aspx?ReturnUrl=%2f) page.

     

1. On the landing page, under **Account**, choose **Domain List** from the drop-down list.

     

1. On the **Domain List** page, select the domain that you want to edit, and then select **Manage**.

     

1. Select **Advanced DNS**.

     

## Add Microsoft 365 DNS records at Namecheap

To add required DNS records at Namecheap for Microsoft 365 services, select the tab based on which DNS records you need to add:

- [**Domain Verification**](create-dns-records-at-namecheap.md?&tabs=domain-verify#add-microsoft-365-dns-records-at-namecheap).
- [**Email**](create-dns-records-at-namecheap.md?&tabs=email#add-microsoft-365-dns-records-at-namecheap).
- [**Microsoft Teams**](create-dns-records-at-namecheap.md?&tabs=teams#add-microsoft-365-dns-records-at-namecheap).
- [**Microsoft Intune/Mobile Device Management for Microsoft 365**](create-dns-records-at-namecheap.md?&tabs=intune-mdm#add-microsoft-365-dns-records-at-namecheap).

### [ **Domain Verify**](#tab/domain-verify)

#### Add a TXT record for domain ownership verification

Before you can use your domain with Microsoft 365, you need to prove you own the domain. Your ability to sign in to your account at your domain registrar and create the DNS record proves to Microsoft that you own the domain. This process involves creating a TXT record at your domain registrar with a specific value that Microsoft can look for. When Microsoft finds the record with the correct value, your domain is verified. The TXT record is used only to verify that you own your domain. It doesn't affect anything else and can be deleted once domain verification is complete.

> [!NOTE]
>
> The procedures in this section assume that the process of [adding a domain](https://learn.microsoft.com/en-us/admin/setup/add-domain#add-a-domain) is started, but that domain ownership isn't verified yet.

To add the TXT record for domain verification at Namecheap, follow these steps:

1. Get the **TXT** value specific for your domain from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). For help on finding the value of your TXT record in the Microsoft 365 admin center, see [Gather the information you need to create DNS records](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records#step-1-find-the-txt-record-value-and-verify).

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in [Sign in to Namecheap to manage your domain's DNS records](#sign-in-to-namecheap-to-manage-your-domains-dns-records) to get there.

1. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

     

1. In the **Type** drop-down, select **TXT Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

     

1. In the boxes for the new record, enter the values from the following table:

    | **Type** | **Host** | **Value**              | **TTL** |
    | -------- | -------- | ---------------------- | ------- |
    | TXT      | @        | *MS=msXXXXXXXX*        | 30 min  |

    - Use the TXT value you gathered earlier from the Microsoft 365 admin center. The value *MS=msXXXXXXXX* shown in the table is only an example.
    - Choose the **TTL** value from the drop-down list.

     

1. Select the **Save Changes** ✅ check mark icon or select the **Save All Changes** button located just below the record you added.

     

1. Wait a few minutes for the TXT record to propagate before continuing.

Now that the TXT record is added at your domain registrar's site, go back to the Microsoft 365 admin center and complete the domain ownership verification process. When Microsoft 365 finds the correct TXT record, your domain is verified.

To verify the record in the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, select the ellipsis **⋮** next to the domain that you're verifying, and then select **Start setup**.

    

1. In the **Verify you own your domain** page, make sure **Add a TXT record to the domain's DNS records** is selected, and then select **Continue**.

1. On the **Add a record to verify domain ownership** page, select **Verify**.

1. After you verify domain ownership, the **How do you want to connect your domain?** page appears. The rest of the wizard walks you through adding additional DNS records to connect your domain to Microsoft 365 services. For more information, see the following article or the following sections in this article:

    - [Connect to Microsoft services by adding DNS records](../../admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider.md?&tabs=manual#step-2-connect-to-microsoft-services-by-adding-dns-records).
    - [Add an MX record to enable email delivery to Microsoft 365](create-dns-records-at-namecheap.md?&tabs=email#add-an-mx-record-to-enable-email-delivery-to-microsoft-365).
    - [Add a CNAME record so email accounts are automatically set up in Outlook and other email clients](create-dns-records-at-namecheap.md?&tabs=email#add-a-cname-record-so-email-accounts-are-automatically-set-up-in-outlook-and-other-email-clients).
    - [Add an SPF TXT record to help prevent email spam](create-dns-records-at-namecheap.md?&tabs=email#add-an-spf-txt-record-to-help-prevent-email-spam).
    - [DNS records for Microsoft Teams](create-dns-records-at-namecheap.md?&tabs=teams#dns-records-for-microsoft-teams).
    - [DNS records for Microsoft Intune and Mobile Device Management for Microsoft 365](create-dns-records-at-namecheap.md?&tabs=intune-mdm#dns-records-for-microsoft-intune-and-mobile-device-management-for-microsoft-365).

### [ **Email**](#tab/email)

#### DNS records for Microsoft 365 email

Microsoft 365 email requires three types of DNS records:

- An [MX](#add-an-mx-record-to-enable-email-delivery-to-microsoft-365) record for email delivery.
- A [CNAME](#add-a-cname-record-so-email-accounts-are-automatically-set-up-in-outlook-and-other-email-clients) record for email account discovery.
- A [TXT](#add-an-spf-txt-record-to-help-prevent-email-spam) record for SPF email spam protection.

To add each of these types of records at Namecheap, follow the steps in the following sections.

##### Add an MX record to enable email delivery to Microsoft 365

To add the MX record for email at Namecheap, follow these steps:

1. Get the **MX** value specific for your domain from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). For help on finding the value of your MX record in the Microsoft 365 admin center, see [Gather the information you need to create DNS records](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records#step-2-find-the-mx-record-value-for-email-and-more).

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in [Sign in to Namecheap to manage your domain's DNS records](#sign-in-to-namecheap-to-manage-your-domains-dns-records) to get there.

1. In the **MAIL SETTINGS** section, select **Custom MX** from the **Email Forwarding** drop-down list. You might have to scroll down the drop-down list to find it.

     

1. Select **ADD NEW RECORD**.

     

1. In the boxes for the new record, enter the values from the following table:

    | **Type**  | **Host** | **Value**                                  | **Priority** | **TTL** |
    | --------- | -------- | ------------------------------------------ | ------------ | ------- |
    | MX Record | @        | \<domain-key>.mail.protection.outlook.com. | 0            | 30 min  |

    - Use the MX value you gathered earlier from the Microsoft 365 admin center.
    - The value shown in the table is only an example.
    - The **Priority** box is the unnamed box to the right of the **Value** box. For more information about priority, see [What is MX priority?](../setup/domains-faq.yml)
    - Choose the **TTL** value from the drop-down list.

     

1. Select the **Save Changes** ✅ check mark icon.

     

1. If there are any other MX records, use the following two-step process to remove each of them:

    1. First, select **Delete** (trash can) for the record that you want to remove.

        

    1. Second, select **Yes** to confirm the deletion.

         

    Remove all MX records except for the one that you added earlier in this procedure.

##### Add a CNAME record so email accounts are automatically set up in Outlook and other email clients

To add a CNAME record for email account discovery at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in [Sign in to Namecheap to manage your domain's DNS records](#sign-in-to-namecheap-to-manage-your-domains-dns-records) to get there.

1. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

     

1. In the **Type** drop-down, select **CNAME Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

     

1. In the empty boxes for the new record, select **CNAME** for the **Record Type**, and then enter the values from the following table:

    | **Type** | **Host**     | **Value**                 | **TTL**   |
    | -------- | ------------ | ------------------------- | --------- |
    | CNAME    | autodiscover | autodiscover.outlook.com. | Automatic |

    > [!IMPORTANT]
    >
    > Make sure the **Value** *autodiscover.outlook.com.* ends with a period (.).

     

1. Select the **Save Changes** ✅ check mark icon.

     

##### Add an SPF TXT record to help prevent email spam

> [!IMPORTANT]
>
> If your domain already has an SPF record, don't create a new one for Microsoft 365. Instead, add the required Microsoft 365 values to the existing record so that you have a *single* SPF record that includes both sets of values.

To add an SPF TXT record for email spam protection at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in [Sign in to Namecheap to manage your domain's DNS records](#sign-in-to-namecheap-to-manage-your-domains-dns-records) to get there.

1. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

     

1. In the **Type** drop-down, select **TXT Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

     

1. In the boxes for the new record, enter the values from the following table:

    | **Type** | **Host** | **Value**                                      | **TTL** |
    | -------- | -------- | ---------------------------------------------- | ------- |
    | TXT      | @        | v=spf1 include:spf.protection.outlook.com -all | 30 min  |

     - Choose the **TTL** value from the drop-down list.
     - Use copy and paste for this entry so that all of the spacing remains correct.

    

1. Select the **Save Changes** ✅ check mark icon.

     

### [ **Teams**](#tab/teams)

#### DNS records for Microsoft Teams

Microsoft Teams needs four records:

- Two [SRV](#add-the-two-required-srv-records-for-microsoft-teams) records for user-to-user communication.
- Two [CNAME](#add-the-two-required-cname-records-for-microsoft-teams) records to sign in and connect users to the service.

Only add these DNS records if your organization uses Microsoft Teams.

##### Add the two required SRV records for Microsoft Teams

To add SRV records for Microsoft Teams at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in [Sign in to Namecheap to manage your domain's DNS records](#sign-in-to-namecheap-to-manage-your-domains-dns-records) to get there.

1. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

     

1. In the **Type** drop-down, select **SRV Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

     

1. In the empty boxes for the new records, enter the values from the following table:

    | **Service**       | **Protocol** | **Priority** | **Weight** | **Port** | **Target**              | **TTL**   |
    | ----------------- | ------------ | ------------ | ---------- | -------- | ----------------------- | --------- |
    | _sip              | _tls         | 100          | 1          | 443      | sipdir.online.lync.com. | Automatic |
    | _sipfederationtls | _tcp         | 100          | 1          | 5061     | sipfed.online.lync.com. | Automatic |

    > [!IMPORTANT]
    >
    > Make sure both **Target** fields *sipdir.online.lync.com.* and *sipfed.online.lync.com.* end with a period (.).

     

1. Select the **Save Changes** ✅ check mark icon.

     

1. Add the other SRV record by choosing the values from the second row of the table.

##### Add the two required CNAME records for Microsoft Teams

To add CNAME records for Microsoft Teams at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in [Sign in to Namecheap to manage your domain's DNS records](#sign-in-to-namecheap-to-manage-your-domains-dns-records) to get there.

1. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

     

1. In the **Type** drop-down, select **CNAME**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

     

1. In the empty boxes for the new records, enter the values from the following table:

    | **Type**  | **Host**     | **Value**               | **TTL**   |
    | --------- | ------------ | ----------------------- | --------- |
    | CNAME     | sip          | sipdir.online.lync.com. | Automatic |
    | CNAME     | lyncdiscover | webdir.online.lync.com. | Automatic |

    > [!IMPORTANT]
    >
    > Make sure both **Value** fields *sipdir.online.lync.com.* and *webdir.online.lync.com.* end with a period (.).

     

1. Select the **Save Changes** ✅ check mark icon.

     

1. Add the other CNAME record by choosing the values from the second row of the table.

### [ **Intune/MDM**](#tab/intune-mdm)

#### DNS records for Microsoft Intune and Mobile Device Management for Microsoft 365

Microsoft Intune and Mobile Device Management for Microsoft 365 help you secure and remotely manage devices that connect to your domain. Mobile Device Management for Microsoft 365 needs two CNAME records so that users can enroll devices to the service. Only add these records if your organization uses Microsoft Intune or Mobile Device Management for Microsoft 365.

##### Add the two required CNAME records for Microsoft Intune and Mobile Device Management for Microsoft 365

To add CNAME records for Microsoft Intune and Mobile Device Management for Microsoft 365 at Namecheap, follow these steps:

1. If you're not already signed in to the Namecheap **Advanced DNS** page for your domain, follow the steps in [Sign in to Namecheap to manage your domain's DNS records](#sign-in-to-namecheap-to-manage-your-domains-dns-records) to get there.

1. In the **HOST RECORDS** section, select **ADD NEW RECORD**.

     

1. In the **Type** drop-down, select **CNAME Record**. The **Type** drop-down automatically appears when you select **ADD NEW RECORD**.

     

1. In the empty boxes for the new records, enter the values from the first row in the following table.

    | **Type**  | **Host**               | **Value**                                    | **TTL**  |
    | --------- | ---------------------- | -------------------------------------------- |---------- |
    | CNAME     | enterpriseregistration | enterpriseregistration.windows.net.          | Automatic |
    | CNAME     | enterpriseenrollment   | enterpriseenrollment-s.manage.microsoft.com. | Automatic |

    > [!IMPORTANT]
    >
    > Make sure both **Value** fields *enterpriseregistration.windows.net.* and *enterpriseenrollment-s.manage.microsoft.com.* end with a period (.).

     

1. Select the **Save Changes** ✅ check mark icon.

     

1. Add the other CNAME record by choosing the values from the second row of the table.

---

## Support

If you don't find what you're looking for, check the [**Domains FAQ**](../setup/domains-faq.yml).

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
