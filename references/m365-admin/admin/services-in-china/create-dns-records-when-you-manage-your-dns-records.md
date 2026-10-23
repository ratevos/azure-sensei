# Create DNS records for Microsoft 365 when you manage your DNS records

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/services-in-china/create-dns-records-when-you-manage-your-dns-records  
> Microsoft doc last updated: 04/23/2026


For detailed instructions about how to create DNS records for Microsoft 365 operated by 21Vianet, including the MX record required for mail routing, see [Create DNS records at any DNS hosting provider for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider).

More options and some things to be aware of:

-  If you don't know the DNS hosting provider or domain registrar for your domain, see [Find your domain registrar or DNS hosting provider](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/find-your-domain-registrar). For descriptions of what the DNS records do, see [DNS basics](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/dns-basics).

-  Some DNS hosting providers don't let you create all the required record types, which causes [Service limitations when your hosting provider doesn't support SRV, CNAME, TXT, or redirection](https://support.microsoft.com/office/dfbb03e3-08c1-4c4e-b2f0-891665b29b77). If your provider doesn't support SRV, TXT, or CNAME records, we recommend that you [transfer your domain](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/buy-a-domain-name) to a [provider that supports all required record types](https://support.microsoft.com/office/dfbb03e3-08c1-4c4e-b2f0-891665b29b77).

- To see which DNS records are required and find the values to use for each record, including the MX record for email, see [Gather the information you need to create Office 365 DNS records](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records). For descriptions of what the DNS records do, see [DNS basics](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/dns-basics).
