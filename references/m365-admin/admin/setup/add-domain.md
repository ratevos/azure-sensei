# Add a custom domain to Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain  
> Microsoft doc last updated: 04/23/2026


Microsoft recommends using a custom domain name for your organization. A custom domain improves brand recognition, email deliverability, and user trust. Many organizations also add multiple domains to support alternate company names or common variations.

This article explains how to add a custom domain to Microsoft 365 and configure the DNS records required by Microsoft 365 services. You can complete this process automatically by using [**Domain Connect**](#domain-connect) (recommended) or manually if your registrar doesn't support **Domain Connect**.

## Domain Connect

When you add a custom domain, Microsoft 365 supports registrars that are [**Domain Connect**](https://www.domainconnect.org/) enabled. By using **Domain Connect**, Microsoft 365 automatically handles the following tasks:

- Confirming domain ownership.
- Adding DNS records required for Microsoft 365 services.

If a registrar doesn't support **Domain Connect**, you need to manually confirm domain ownership and add DNS records. Sign in to your registrar and manually add the appropriate DNS records.

To find your registrar, see [Find your domain registrar](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/find-your-domain-registrar). Once you determine your registrar, consult with the registrar to see if they support **Domain Connect**.

Microsoft 365 services start working after you complete these tasks. Examples of Microsoft 365 services include:

- Email through Microsoft 365.
- Microsoft Teams.

For examples of registrars that support **Domain Connect**, see [Domain Connect registrars integrating with Microsoft 365](#domain-connect-registrars-integrated-with-microsoft-365).

## Before you begin

Before adding a custom domain to Microsoft 365, make sure the following requirements are met:

- To add, modify, or remove domains, you **must** be a **Domain Name Administrator** of a [business or enterprise plan](https://products.office.com/business/office). Because these changes affect the whole tenant, *customized administrators* or *regular users* can't make these changes.

- If you're using Microsoft 365 for email, add users and set up mailboxes in Microsoft 365 for all email users on your domain. Add users after adding the custom domain but before adding an MX record for Microsoft 365. Adding users before setting up the MX record ensures that email continues to work without interruption as the email moves from the previous email provider to Microsoft 365.

- Determine if your registrar supports [**Domain Connect**](#domain-connect).

## Watch: Add a custom domain to Microsoft 365

Check out this video and others on our [YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198213).

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=23594aee-6bbd-45d0-8e89-f00fc78ca495]

## Add a domain

> [!IMPORTANT]
> We recommend that your organization use a custom domain for sending, as it can enhance your email's appearance, improve its reputation and avoid limits designed to prevent misuse.

To add a custom domain to Microsoft 365, select the tab based on your registrar's support for [**Domain Connect**](#domain-connect):

- **Domain Connect** - Registrar supports Domain Connect and DNS records are added automatically.
- **Manual** - Registrar doesn't support Domain Connect and DNS records need to be added manually.

>[!NOTE]
>
> If your registrar supports **Domain Connect** but you prefer to manually verify domain ownership and manually add DNS records needed by Microsoft 365 services, select the **Manual** tab. If you decide to manually add DNS records, make sure you're familiar with how to properly add DNS records at your registrar. Incorrect DNS records can cause email and service outages.

### [ **Domain Connect**](#tab/domain-connect)

To add a custom domain to Microsoft 365 by using [**Domain Connect**](#domain-connect), follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. In the Microsoft 365 admin center, you can start the process of adding a custom domain to Microsoft 365 in two different ways:

    - First time adding a custom domain to Microsoft 365:

      1. From the left navigation bar, select **… Show all**, and then select [**Setup**](https://go.microsoft.com/fwlink/p/?linkid=2075721).

      1. In the **Setup** page, under **Sign-in and security**, select **Get your custom domain set up**.

      1. In the **Get your custom domain set up** page, select **Get Started**.

    - Add a custom domain, add extra custom domains, or continue setting up a domain:

      1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

      1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

      1. In the **Domains** page, select **+ Add domain**.

1. In the **Domain name** textbox of the **Add a domain** page, enter the new domain name that you want to add, and then select **Use this domain**.

1. In the **Verify you own your domain** page, make sure the name of the displayed registrar is correct and then select **Verify**. If your domain is registered at a different registrar than what is displayed, select **choose a different domain host**. After selecting the proper registrar, select **Verify**.

1. A new window from your registrar opens. Sign in to the registrar and then authorize to add the TXT DNS record.

    > [!NOTE]
    >
    > To make the new window from the registrar appear, make sure of one of the following two items:
    >
    > - Pop-up blockers are disabled.
        > - The registrar's URL is added to the pop-up blocker's allow list. For more information on allowing pop-ups when using Microsoft Edge, see [Block pop-ups in Microsoft Edge](https://support.microsoft.com/microsoft-edge/1d8ba4f8-f385-9a0b-e944-aa47339b6bb5).

1. After you add the TXT DNS record and verify domain ownership, you're returned to the Microsoft 365 admin center window.

1. In the **How do you want to connect your domain** page, select **Continue**.

1. In the **Add DNS records** page, select the Microsoft 365 services that you want DNS records added for, and then select **Add DNS records**. Make sure to also expand **Advanced options** to view additional Microsoft 365 services that might need DNS records.

1. A new window from your registrar opens showing the DNS records that are going to be added. Verify that the DNS records are correct, and then authorize the DNS records to be added.

1. After you add the DNS records, you're returned to the Microsoft 365 admin center window.

1. The **Domain setup is complete** page displays. Select **Done** to complete adding your custom domain and DNS records to Microsoft 365.

### [ **Manual**](#tab/manual)

If a registrar doesn't support [**Domain Connect**](#domain-connect), manually perform the following tasks:

- Verify domain ownership by using DNS records or a verification file uploaded to your website.
- Manually add DNS records for Microsoft 365 services.

To add a custom domain to Microsoft 365 by manually verifying domain ownership and manually adding DNS records, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. In the Microsoft 365 admin center, you can start the process of adding a custom domain to Microsoft 365 in two different ways:

    - First time adding a custom domain to Microsoft 365:

      1. From the left navigation bar, select **… Show all**, and then select [**Setup**](https://go.microsoft.com/fwlink/p/?linkid=2075721).

      1. In the **Setup** page, under **Sign-in and security**, select **Get your custom domain set up**.

      1. In the **Get your custom domain set up** page, select **Get Started**.

    - Add a custom domain, add extra custom domains, or continue setting up a domain:

      1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

      1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

      1. In the **Domains** page, select **+ Add domain**.

1. In the **Domain name** textbox of the **Add a domain** page, enter the new domain name that you want to add, and then select **Use this domain**.

1. In the **Verify you own your domain** page, select one of the following options to verify domain ownership:

   - **Add a TXT record to the domain's DNS records** - Uses a TXT record manually added to the domain's DNS at the registrar to verify domain ownership. It can take up to 10 minutes to verify domain ownership after adding the TXT record. Some registrars might require additional time up to 48 hours.

   - **If you can't add a TXT record, add an MX record to the domain's DNS records** - Uses an MX record manually added to the domain's DNS at the registrar to verify domain ownership. It can take up to 10 minutes to verify domain ownership after adding the MX record. Some registrars might require additional time up to 48 hours.

   - **Add a text file to the domain's website** - Uses a file download from this wizard and then uploaded to the domain's website top-level folder to verify domain ownership. The path to the file should look similar to the following example:

        `http://mydomain.com/ms39978200.txt`

        Microsoft confirms you own the domain by finding the file on your website.

1. After you select an option, select **Continue**.

1. Instructions specific to the selected option appear:

   - The **Add a record to verify ownership** page appears if you select one of the first two options. The page contains instructions on what DNS records to add at your registrar to verify domain ownership. For detailed instructions on adding DNS records at your registrar, refer to the registrar's documentation and instructions.

        > [!WARNING]
        >
        > If you use the option **If you can't add a TXT record, add an MX record to the domain's DNS records**, make sure to set the **Priority** field of the MX record to a high value so that it doesn't break email with your current email provider.

   - If you select the **Add a text file to the domain's website** option, instructions appear on the **Verify you own this domain** page that explains how to add a file to your website to verify domain ownership. For detailed instructions on adding files to your website, refer to the web hosting provider's documentation and instructions.

1. Once you complete the selected option, select **Verify**. Domain ownership verification occurs.

1. Once domain ownership verification completes, the **How do you want to connect your domain** appears. Select **Continue**.

    > [!NOTE]
    >
    > If you select **More options** instead of **Continue**, select **Add your own DNS records**, and then select **Continue**.

1. The **Add DNS records** page contains instructions on what DNS records you need to add at your registrar. Select the Microsoft 365 services that you need DNS records for and then expand each DNS record type for detailed information on the format of the DNS record. Make sure to also expand **Advanced options** to view additional Microsoft 365 services that might need DNS records.

1. In a separate browser window or tab, sign in to your registrar and then manually add the required DNS records from the previous step. For detailed instructions on adding DNS records at your registrar, refer to the registrar's documentation and instructions.

    > [!TIP]
    >
    > The name for managing DNS settings at your registrar varies from registrar to registrar. It might have one of the following names instead:
    >
    > - **Zone File Settings**.
    > - **Manage Domains**.
    > - **Domain Manager**.
    > - **DNS Manager**.

1. Once you add the DNS records at the registrar, switch back to the web browser window or tab with the Microsoft 365 admin center, and then select **Continue**.

1. The **Domain setup is complete** page displays. Select **Done** to complete adding your custom domain and DNS records to Microsoft 365.

---

## What happens to my email and website?

After you finish setting up a custom domain, the MX record for your domain is updated to point to Microsoft 365. All email for your domain starts coming to Microsoft 365.

> [!IMPORTANT]
>
> As described in the [Before you begin](#before-you-begin) section, make sure you add users and set up mailboxes in Microsoft 365 for everyone who gets email on your domain before adding an MX record. Adding users before setting up the MX record ensures that when email moves from the previous email provider to Microsoft 365, users continue to receive their emails.

If you have a website that you use with your business, it keeps working where it is. The Domain Connect setup steps don't affect your website.

## Add or edit DNS records

If Microsoft 365 hosts the domain instead of a non-Microsoft registrar, use the following steps to add DNS records for items such as a website or non-Microsoft services. If a non-Microsoft registrar hosts the domain, consult the registrar's documentation and instructions on how to add DNS records.

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, select a domain.

1. In the page that displays your custom domain, select **DNS records**.

1. Select **+ Add records**.

    > [!NOTE]
    >
    > If **+ Add records** isn't available, a non-Microsoft registrar hosts the domain. The page displays the registrar next to **To manage DNS records for *domain*, go to your DNS hosting provider:**. Consult the non-Microsoft registrar's documentation and instructions on how to add DNS records.

1. In the **Add a custom DNS record** pane that opens, select the type of DNS record to add (A, CNAME, MX, TXT, SRV, and so on), and then fill out the related fields for the selected type of DNS record. Once you fill out all of the fields, select **Save** to create the DNS record.

1. The newly created record should appear under **Custom records**.

## Domain Connect registrars integrated with Microsoft 365

The following registrars support [**Domain Connect**](#domain-connect) integration with Microsoft 365:

- [**Aruba.it**](https://www.aruba.it/).
- [**Cloudflare**](https://www.cloudflare.com/).
- [**EuroDNS**](https://www.eurodns.com/).
- [**GoDaddy (_Media Temple_)**](https://www.godaddy.com/).
- [**IONOS**](https://www.1and1.com/).
- [**Plesk**](https://www.plesk.com/).
- [**WordPress.com**](https://wordpress.com/).
- **SecureServer** or **WildWestDomains** (**GoDaddy** resellers using **SecureServer DNS** hosting)
  - Examples:
    - [**DomainsPricedRight**](https://www.domainspricedright.com/products/domain-registration)
    - [**DomainRightNow**](https://www.domainrightnow.com/)

## Add an onmicrosoft.com domain

To add an onmicrosoft.com domain, see [Add or replace your onmicrosoft.com fallback domain in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-or-replace-your-onmicrosoftcom-domain).

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

- [Domains FAQ](domains-faq.yml).
- [What is a domain?](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/what-is-a-domain).
- [Domain Connect](https://www.domainconnect.org/).
- [Connect your domain by adding DNS records](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider).
- [Buy a domain name in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/buy-a-domain-name).
- [Change nameservers to set up Microsoft 365 with any registrar](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/change-nameservers-at-any-domain-registrar).
- [Add or replace your onmicrosoft.com fallback domain in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-or-replace-your-onmicrosoftcom-domain).
- [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).
- [Microsoft 365 small business help](https://go.microsoft.com/fwlink/?linkid=2197659).
