# Find your domain registrar and DNS hosting provider

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/find-your-domain-registrar  
> Microsoft doc last updated: 04/23/2026


Your domain registrar and DNS hosting provider are often the same company, but they can be different. The registrar manages your domain registration, while the DNS hosting provider manages the DNS records that route traffic for your domain.

## Use the ICANN Lookup tool

Use the ICANN Lookup tool to find your domain registrar and DNS hosting provider. The Internet Corporation for Assigned Names and Numbers (ICANN) provides this free lookup page where you can view registration and nameserver details for any domain name.

> [!NOTE]
>
> The ICANN website is a non-Microsoft site. Microsoft doesn't control the information provided on the ICANN site. The information provided on the ICANN website might be inaccurate or out of date. Additionally, ICANN might change their website and tools so that the steps in this article are no longer valid. Microsoft isn't responsible for the accuracy or reliability of the information provided on the ICANN website.

To find your domain registrar and DNS hosting provider at the ICANN site, follow these steps:

1. Go to the [ICANN Lookup](https://lookup.icann.org/) page.

    Once at the ICANN Lookup page, use the **Registration data lookup tool** to find your domain registrar and identify the nameservers that host your DNS.

1. In the **Lookup** text box, enter your domain name and then select **Lookup**. For example, *contoso.com*.

1. The **Registrar Information** section of the results page lists the registrar for your domain.

1. In the **Domain Information** section of the results page, look for **Nameservers:**. The domain name shown in the nameserver entries (NS records) indicates which provider hosts your DNS records.

    If you need more details about the DNS hosting provider, perform a second lookup using one of the nameservers:

    1. Copy the domain name of one of the nameservers (NS) in the list. For example, if a nameserver is *ns1.contoso.com*, copy only the root domain name (*contoso.com*).

    1. Paste the copied domain name into the **Lookup** text box at the top of the page and then select **Lookup**.

    1. Information about the DNS hosting provider is listed in the **Contact Information** section of the results page. Additional information about the DNS hosting provider might also be listed in other sections of the results page.

## Get support

 **[Check the Domains FAQ](../setup/domains-faq.yml)** if you don't find what you're looking for.

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

- [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).
