# Connect your domain by adding DNS records

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider  
> Microsoft doc last updated: 04/23/2026


If you purchased a domain from a non-Microsoft registrar, you can connect it to Microsoft 365 by updating the DNS records at your registrar. After you add DNS records at your registrar, your domain stays registered with the registrar that you purchased the domain from. However, Microsoft 365 can use the domain for its various services such as your domain email addresses.

> [!NOTE]
>
> A registrar is also known as a DNS hosting provider.

If you don't add a custom domain to Microsoft 365, your organization can instead use the **onmicrosoft.com** domain for email addresses until a custom domain is added. It's important to add your custom domain before you add users so you don't have to set up users twice.

If you want to change the email domain of existing user accounts, follow the steps described in [Change your email address to use your custom domain using the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/email/change-email-address#change-your-email-address-to-use-your-custom-domain-using-the-microsoft-365-admin-center).

For more information on domains, see [Domains FAQ](../setup/domains-faq.yml).

## Registrars and Domain Connect

Before you connect your domain to Microsoft 365 by adding DNS records, you need to determine the registrar that hosts your domain. Additionally, you need to determine if your registrar supports [**Domain Connect**](https://www.domainconnect.org/). **Domain Connect** allows Microsoft 365 to automatically perform the following tasks:

- Confirm domain ownership.
- Add DNS records required for Microsoft 365 services.

If a registrar doesn't support **Domain Connect**, you need to manually confirm domain ownership and add DNS records by signing in to your registrar and manually adding the appropriate DNS records.

To find your registrar, see [Find your domain registrar](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/find-your-domain-registrar). Once you determine your registrar, consult with the registrar to see if they support **Domain Connect**.

For instructions on how to manually add DNS records at specific registrars, see the following articles:

- [Connect your DNS records at IONOS to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-ionos-com).
- [Connect your DNS records at 123-reg.co.uk to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-123-reg-co-uk).
- [Connect your DNS records at Amazon Web Services (AWS) to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-aws).
- [Connect your DNS records at Cloudflare to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-cloudflare).
- [Connect your DNS records at GoDaddy to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-godaddy).
- [Connect your DNS records at Namecheap to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-namecheap).
- [Connect your DNS records at Network Solutions to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-network-solutions).
- [Connect your DNS records at OVH to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-ovh).
- [Connect your DNS records at web.com to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-web-com).
- [Connect your DNS records at Wix to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-at-wix).
- [Create DNS records for Microsoft using Windows-based DNS](https://learn.microsoft.com/en-us/microsoft-365/admin/dns/create-dns-records-using-windows-based-dns).

## Step 1: Add a domain and verify domain ownership

First, add a custom domain to Microsoft 365 and verify domain ownership. For detailed instructions on how to add a custom domain to Microsoft 365, see [Add a domain to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain#add-a-domain).

## Step 2: Connect to Microsoft services by adding DNS records

When you add a custom domain as part of [Step 1: Add a domain and verify domain ownership](#step-1-add-a-domain-and-verify-domain-ownership), the wizard prompts you to add DNS entries for Microsoft 365 services, including email. However, if you skip adding DNS entries when adding the custom domain, you can add them later.

The following sections describe how to add the various DNS records for some of the Microsoft 365 services.

### Add an MX record and DNS records for email (Outlook, Exchange Online)

> [!IMPORTANT]
>
> Before you begin, add users and set up mailboxes in Microsoft 365 for all email users on your domain. Add users before updating an MX record for Microsoft 365 to ensure that email continues to work without interruption as the email moves from the previous email provider to Microsoft 365.
>
> When you update your domain's MX record, all new email for anyone who uses your domain is sent to Microsoft 365. Any existing email stays at your previous email host, unless you decide to [migrate email and contacts to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/migrate-email-and-contacts-admin).

To add the DNS records needed for Microsoft 365 email services, select the tab based on your registrar's support for **Domain Connect**:

- **Domain Connect** - Registrar supports Domain Connect and DNS records are added automatically.
- **Manual** - Registrar doesn't support Domain Connect and DNS records need to be added manually.

#### [ **Domain Connect**](#tab/domain-connect)

To add an MX record and other supporting email DNS records for use with email in Microsoft 365 (Outlook, Exchange Online), follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, select a domain.

1. In the page that displays your custom domain, select **DNS records**, and then select **Manage DNS**.

1. The **How do you want to connect your domain?** wizard starts. Select **Continue**.

1. In the **Add DNS records** page, make sure **Exchange and Exchange Online Protection** is selected.

1. For additional email spam protection, select **Advanced options**, and then select **DomainKeys Identified Mail (DKIM)**. DKIM DNS records are optional. For more information about **DKIM**, see [Help prevent email spam (Outlook, Exchange Online) by adding appropriate DNS records](#help-prevent-email-spam-outlook-exchange-online-by-adding-appropriate-dns-records) in this article.

1. Once the desired email services are selected, select **Add DNS records**.

1. A new window from your registrar opens showing the DNS records that are going to be added, including the MX record. Verify that the DNS records are correct, and then authorize the DNS records to be added.

    > [!IMPORTANT]
    >
    > If an MX record already exists for the previous email provider, take one of the following two actions to ensure that email starts getting delivered to Microsoft 365:
    >
    > - Remove any existing MX records pointing to a previous email provider.
    > - Set the MX record priority for the previous email provider to a lower priority than the MX record for Microsoft 365.
    >
    > Depending on the registrar, the registrar might offer to automatically delete the existing MX record via **Domain Connect**. If you don't want the existing MX record to be automatically deleted, add the required email DNS records manually at your registrar. Select the **Manual** tab instead to add MX records manually.

1. After you add DNS records at the registrar, the browser returns you to the Microsoft 365 admin center.

1. The **Domain setup is complete** page displays. Select **Done** to complete adding DNS records to Microsoft 365.

#### [ **Manual**](#tab/manual)

To add an MX record and other supporting email DNS records for use with email in Microsoft 365 (Outlook, Exchange Online), follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, select a domain.

1. In the page that displays your custom domain, select **DNS records**, and then select **Manage DNS**.

1. The **How do you want to connect your domain?** wizard starts. Select **Continue**.

1. In the **Add DNS records** page, make sure **Exchange and Exchange Online Protection** is selected.

1. For additional email spam protection, select **Advanced options**, and then select **DomainKeys Identified Mail (DKIM)**. DKIM DNS records are optional. For more information about **DKIM**, see [Help prevent email spam (Outlook, Exchange Online) by adding appropriate DNS records](#help-prevent-email-spam-outlook-exchange-online-by-adding-appropriate-dns-records) in this article.

1. Select the **>** next to **MX Records**, **CNAME Records**, and **TXT Records** to expand them. If you also selected **DomainKeys Identified Mail (DKIM)**, make sure to also expand **CNAME Records** under **DomainKeys Identified Mail (DKIM)**. The DNS records that you need to add at your registrar are displayed under each DNS record type.

1. In a separate browser window or tab, sign in to your registrar and then manually add the required DNS records shown in the previous step. For detailed instructions on adding DNS records at your registrar, refer to the registrar's documentation and instructions.

    > [!TIP]
    >
    > The name for managing DNS settings at your registrar varies from registrar to registrar. It might have one of the following names instead:
    >
    > - **Zone File Settings**.
    > - **Manage Domains**.
    > - **Domain Manager**.
    > - **DNS Manager**.

    The following DNS records need to be added for Microsoft 365 email services:

    - **MX record** - This DNS record is required and specifies where email for the domain should go.

      | **DNS record field**            | **Value**                                            |
      | ------------------------------- | ---------------------------------------------------- |
      | *Type*                          | **MX**                                               |
      | *Host Name* or *Alias*          | **@**                                                |
      | *Points to address* or *Target* | Copy the MX record value displayed in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
      | *Priority*                      | Set to the highest value available, typically **0**. |
      | *TTL*                           | **3600** (1 hour)                                    |

      > [!NOTE]
      >
      > Exchange Online only supports TTL values less than 6 hours (21,600 seconds).

    - **Autodiscover CNAME record** - This DNS record is optional but highly recommended. It allows automatic configuration of a user's email in products that support it, for example Microsoft Outlook.

      | **DNS record field**            | **Value**         |
      | ------------------------------- | ----------------- |
      | *Type*                          | **CNAME (Alias)** |
      | *Host Name* or *Alias*          | **autodiscover**  |
      | *Points to address* or *Target* | Copy the autodiscover CNAME record value displayed in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
      | *TTL*                           | **3600** (1 hour) |

    - **SPF TXT record** - This record is optional but highly recommended. The SPF TXT record helps prevent email spam. For more information on SPF TXT records, see [Help prevent email spam (Outlook, Exchange Online) by adding appropriate DNS records](#help-prevent-email-spam-outlook-exchange-online-by-adding-appropriate-dns-records) in this article.

      | **DNS record field**                | **Value**                                          |
      | ----------------------------------- | -------------------------------------------------- |
      | *Type*                              | **TXT (Text)**                                     |
      | *Host Name*, *TXT Name*, or *Alias* | **@**                                              |
      | *TXT value*                         | **v=spf1 include:spf.protection.outlook.com -all** |
      | *TTL*                               | **3600** (1 hour)                                  |

      > [!IMPORTANT]
      >
      > If an SPF record already exists for the domain, don't create a new one for Microsoft 365. Don't delete the existing value already in the SPF TXT record for the previous email provider. Instead, add the required Microsoft 365 SPF TXT value to the current SPF TXT record. When complete, there should be a *single* SPF TXT record that includes the values for both the previous email provider and Microsoft 365.

    - **DomainKeys Identified Mail (DKIM) CNAME records** - This record is optional. The DKIM record helps prevent email spam. For more information on DKIM records, see [Help prevent email spam (Outlook, Exchange Online) by adding appropriate DNS records](#help-prevent-email-spam-outlook-exchange-online-by-adding-appropriate-dns-records) in this article.

      | **DNS record field**            | **Value**                |
      | ------------------------------- | ------------------------ |
      | *Type*                          | **CNAME (Alias)**        |
      | *Host Name* or *Alias*          | **selector1._domainkey** |
      | *Points to address* or *Target* | Copy the first value displayed under **DomainKeys Identified Mail (DKIM)** in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
      | *TTL*                           | **3600** (1 hour)        |

      | **DNS record field**            | **Value**                |
      | ------------------------------- | ------------------------ |
      | *Type*                          | **CNAME (Alias)**        |
      | *Host Name* or *Alias*          | **selector2._domainkey** |
      | *Points to address* or *Target* | Copy the second value displayed under **DomainKeys Identified Mail (DKIM)** in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
      | *TTL*                           | **3600** (1 hour)        |

1. If MX records already exist for the previous email provider, take one of the following two actions to ensure that email starts getting delivered to Microsoft 365:

   - Remove any existing MX records that point to a previous email provider.
   - Set the MX record priority for the previous email provider to a lower priority than the MX record for Microsoft 365. In MX records, lower numbers indicate higher priority. For example, priority **0** is higher than priority **10**.

1. Once you add the DNS records manually at the registrar, switch back to the Microsoft 365 admin center web browser window or tab, and then select **Continue**.

1. Microsoft 365 verifies that you added the DNS records for email correctly. Once verification completes successfully, the **Domain setup is complete** page displays. Select **Done** to complete adding the email DNS records for Microsoft 365 email services.

---

### Add CNAME and SRV records to connect other Microsoft 365 services (Microsoft Teams, Exchange Online, Microsoft Intune)

Select the tab based on your registrar's support for **Domain Connect**:

- **Domain Connect** - Registrar supports Domain Connect and DNS records are added automatically.
- **Manual** - Registrar doesn't support Domain Connect and DNS records need to be added manually.

#### [ **Domain Connect**](#tab/domain-connect)

To add CNAME and SRV records required by Microsoft 365 services such as Microsoft Teams, Exchange Online, or Microsoft Intune:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, select a domain.

1. In the page that displays your custom domain, select **DNS records**, and then select **Manage DNS**.

1. The **How do you want to connect your domain?** wizard starts. Select **Continue**.

1. In the **Add DNS records** page, select **Advanced options**. **Advanced options** displays all additional available Microsoft 365 services.

1. Select the Microsoft 365 services that need DNS records added, and then select **Add DNS records**. For example:

   - For Microsoft Intune, select **Intune and Mobile Device Management for Microsoft 365**.
   - To add DKIM records to reduce email spam, select **DomainKeys Identified Mail (DKIM)**.

1. A new window from your registrar opens showing the DNS records that are going to be added. Verify that the DNS records are correct, and then authorize the DNS records to be added.

1. Once the DNS records are added, you're returned to the Microsoft 365 admin center window.

1. The **Domain setup is complete** page displays. Select **Done** to complete adding the CNAME and SRV records to Microsoft 365.

#### [ **Manual**](#tab/manual)

To add CNAME and SRV records required by Microsoft 365 services such as Microsoft Teams, Exchange Online, or Microsoft Intune:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, select a domain.

1. In the page that displays your custom domain, select **DNS records**, and then select **Manage DNS**.

1. The **How do you want to connect your domain?** wizard starts. Select **Continue**.

1. In the **Add DNS records** page, select **Advanced options**. **Advanced options** displays all additional available Microsoft 365 services.

1. Select the Microsoft 365 services that need DNS records added. For example, for Microsoft Intune, make sure to select **Intune and Mobile Device Management for Microsoft 365**.

1. For each Microsoft 365 service, select the **>** next to either **CNAME Records** or **SRV Records** to expand it. The CNAME records or SRV records that you need to add at your registrar are displayed.

1. In a separate browser window or tab, sign in to your registrar and then manually add the required DNS records shown in the previous step. For detailed instructions on adding DNS records at your registrar, refer to the registrar's documentation and instructions.

    > [!TIP]
    >
    > The name for managing DNS settings at your registrar varies from registrar to registrar. It might have one of the following names instead:
    >
    > - **Zone File Settings**.
    > - **Manage Domains**.
    > - **Domain Manager**.
    > - **DNS Manager**.

1. Once you add the CNAME and SRV records at the registrar, switch back to the Microsoft 365 admin center web browser window or tab, and then select **Continue**.

1. Microsoft 365 verifies that you added the CNAME and SRV records correctly. When verification succeeds, the **Domain setup is complete** page displays. Select **Done** to finish adding the CNAME and SRV records for Microsoft 365 services.

Examples of CNAME and SRV DNS records:

- **CNAME record**

    | **DNS record field**            | **Value**                |
    | ------------------------------- | ------------------------ |
    | *Type*                          | **CNAME (Alias)**        |
    | *Host Name* or *Alias*          | Copy the value displayed in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
    | *Points to address* or *Target* | Copy the value displayed in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
    | *TTL*                           | **3600** (1 hour)        |

    For example, to add the required CNAME records for Microsoft Intune, add the following CNAME records:

    | **DNS record field**            | **Value**                               |
    | ------------------------------- | --------------------------------------- |
    | *Type*                          | **CNAME (Alias)**                       |
    | *Host Name* or *Alias*          | **enterpriseregistration**              |
    | *Points to address* or *Target* | **enterpriseregistration.windows.net.** |
    | *TTL*                           | **3600** (1 hour)                       |

    | **DNS record field**            | **Value**                                        |
    | ------------------------------- | ------------------------------------------------ |
    | *Type*                          | **CNAME (Alias)**                                |
    | *Host Name* or *Alias*          | **enterpriseenrollment**                         |
    | *Points to address* or *Target* | **enterpriseenrollment-s.manage.microsoft.com.** |
    | *TTL*                           | **3600** (1 hour)                                |

- **SRV record**

    | **DNS record field**   | **Value**                                                                                                         |
    | ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
    | *Type*                 | **SRV (Service)**                                                                                                 |
    | *Host Name* or *Alias* | **@**                                                                                                             |
    | *Service*              | Copy the value displayed in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
    | *Protocol*             | Copy the value displayed in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
    | *Target*               | Copy the value displayed in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
    | *Priority*             | **100**                                                                                                           |
    | *Weight*               | **1**                                                                                                             |
    | *Port*                 | Copy the value displayed in the Microsoft 365 admin center **Add DNS records** page and paste it into this field. |
    | *TTL*                  | **3600** (1 hour)                                                                                                 |

  For example, to add the required SRV record for Microsoft Teams in Microsoft 365, add the following SRV record:

    | **DNS record field**   | **Value**                  |
    | ---------------------- | -------------------------- |
    | *Type*                 | **SRV (Service)**          |
    | *Host Name* or *Alias* | **@**                      |
    | *Service*              | **_sipfederationtls**      |
    | *Protocol*             | **TCP**                    |
    | *Target*               | **sipfed.online.lync.com** |
    | *Priority*             | **100**                    |
    | *Weight*               | **1**                      |
    | *Port*                 | **5061**                   |
    | *TTL*                  | **3600** (1 hour)          |

    > [!NOTE]
    >
    > Some registrars might restrict what you can add to an SRV record. For more information, including workarounds, see [SRV record field restrictions and workarounds](#srv-record-field-restrictions-and-workarounds) in this article.

---

### Help prevent email spam (Outlook, Exchange Online) by adding appropriate DNS records

Sender Policy Framework, better known as SPF, helps prevent email spam. SPF is designed to help prevent spoofing. Activate SPF on a domain by adding a TXT record to the domain's DNS. To set up an SPF TXT record for use with Microsoft 365 email services, see [Add an MX record and DNS records for email (Outlook, Exchange Online)](#add-an-mx-record-and-dns-records-for-email-outlook-exchange-online) in this article.

Although SPF is designed to help prevent spoofing, some spoofing techniques bypass SPF. To protect against these threats, after setting up the SPF record, also set up DomainKeys Identified Mail (DKIM) and Domain-based Message Authentication, Reporting, and Conformance (DMARC) for Microsoft 365. For more information on DKIM and DMARC, see the following two articles:

- [Use DKIM to validate outbound email sent from your domain in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dkim-configure).
- [Use DMARC to validate email in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication-dmarc-configure).

To set up DKIM for use with Microsoft 365 email services, see [Add an MX record and DNS records for email (Outlook, Exchange Online)](#add-an-mx-record-and-dns-records-for-email-outlook-exchange-online) in this article.

### SRV record field restrictions and workarounds

Some registrars restrict field values within SRV records. The following sections describe some of those restrictions and their workarounds.

#### Host Name/Alias can't be set to @

If your registrar doesn't allow setting this field to **@**, leave it blank. Use this approach *only* when your registrar has separate fields for **Service** and **Protocol**. If your registrar doesn't have separate fields for **Service** and **Protocol**, see [Service and Protocol fields aren't available](#service-and-protocol-fields-arent-available) in this article.

#### Service and Protocol fields aren't available

If your registrar doesn't provide separate **Service** and **Protocol** fields for SRV records, you must specify the **Service** and **Protocol** values in the record's **Host Name**/**Alias** field. To add these values, create a single string, separating the values with a dot. For example, for the following values:

| **DNS record field**   | **Value**                  |
| ---------------------- | -------------------------- |
| *Type*                 | **SRV (Service)**          |
| *Host Name* or *Alias* | **@**                      |
| *Service*              | **_sipfederationtls**      |
| *Protocol*             | **TCP**                    |
| *Target*               | **sipfed.online.lync.com** |
| *Priority*             | **100**                    |
| *Weight*               | **1**                      |
| *Port*                 | **5061**                   |
| *TTL*                  | **3600** (1 hour)          |

enter the following value in the **Host Name**/**Alias** field instead of **@**:

| **DNS record field**   | **Value**                  |
| ---------------------- | -------------------------- |
| *Type*                 | **SRV (Service)**          |
| *Host Name* or *Alias* | **_sipfederationtls._tcp** |
| *Target*               | **sipfed.online.lync.com** |
| *Priority*             | **100**                    |
| *Weight*               | **1**                      |
| *Port*                 | **5061**                   |
| *TTL*                  | **3600** (1 hour)          |

#### Priority, Weight, and Port fields aren't available

If your registrar doesn't provide the **Priority**, **Weight**, and **Port**  fields for SRV records, you must specify them in the SRV record's **Target** field. To add these values, create a single string, separating the values with spaces. The values must be included in this order:

  1. Priority.
  1. Weight.
  1. Port.
  1. Target.

For example, for the following values:

| **DNS record field**   | **Value**                  |
| ---------------------- | -------------------------- |
| *Type*                 | **SRV (Service)**          |
| *Host Name* or *Alias* | **@**                      |
| *Service*              | **_sipfederationtls**      |
| *Protocol*             | **TCP**                    |
| *Target*               | **sipfed.online.lync.com** |
| *Priority*             | **100**                    |
| *Weight*               | **1**                      |
| *Port*                 | **5061**                   |
| *TTL*                  | **3600** (1 hour)          |

enter the following value in the **Target** field:

| **DNS record field**   | **Value**                             |
| ---------------------- | ------------------------------------- |
| *Type*                 | **SRV (Service)**                     |
| *Host Name* or *Alias* | **@**                                 |
| *Service*              | **_sipfederationtls**                 |
| *Protocol*             | **TCP**                               |
| *Target*               | **100 1 5061 sipfed.online.lync.com** |
| *TTL*                  | **3600** (1 hour)                     |

> [!WARNING]
>
> - Some registrars require that the string entered into the **Target** field end with a dot (**.**). For example:
>
>    | **DNS record field**   | **Value**                              |
>    | ---------------------- | -------------------------------------- |
>    | *Type*                 | **SRV (Service)**                      |
>    | *Host Name* or *Alias* | **@**                                  |
>    | *Service*              | **_sipfederationtls**                  |
>    | *Protocol*             | **TCP**                                |
>    | *Target*               | **100 1 5061 sipfed.online.lync.com.** |
>    | *TTL*                  | **3600** (1 hour)                      |
>
>     Check with your registrar to verify if ending with a dot (**.**) is required.
>
> - Depending on your registrar, the **Target** field might have a different name such as:
>
>   - **Content**.
>   - **IP Address**.
>   - **Target Host**.
>   - **Value**.

## Support

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

## Related content

- [Help and learning for small business](https://go.microsoft.com/fwlink/?linkid=2224585).
- [Domains FAQ](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/domains-faq).
- [Add a domain to Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain).
- [Change nameservers to set up Microsoft 365 with any domain registrar](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/change-nameservers-at-any-domain-registrar).
- [Find and fix issues after adding your domain or DNS records](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/find-and-fix-issues) (article).
- [Manage domains](https://learn.microsoft.com/en-us/admin) (link page).
