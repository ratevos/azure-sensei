# Gather the information you need to create DNS records

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records  
> Microsoft doc last updated: 04/23/2026


Check out all of our small business content on [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).

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

> [!NOTE]
> The procedures in this article assume that you have begun the process of [adding a domain](https://learn.microsoft.com/en-us/admin/setup/add-domain#add-a-domain), but have not yet verified the domain.

### Step 1: Find the TXT record value and verify

::: moniker range="o365-worldwide"

1. In the Microsoft 365 admin center, go to the **Settings** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">Domains</a> page.

::: moniker-end

::: moniker range="o365-21vianet"

1. In the admin center, go to the **Settings** > <a href="https://go.microsoft.com/fwlink/p/?linkid=2007048" target="_blank">Domains</a> page.

::: moniker-end

2. On the **Domains** page, select your domain, then select **Continue setup**. You'll go back to the domains setup wizard to see the specific value you need to add.

3. On the **Domain Verification** page, select **Add a TXT record to the domain's DNS records**, then select **Continue**.

4. Copy the **TXT value** shown. It looks like this: **MS=msXXXXXXXX**.

5. Go to [Add DNS records to connect your domain](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider), and follow the steps to add records at your DNS host's website.

6. Follow the steps for creating the TXT record (or MX record) at your DNS host, then verify the domain back in Microsoft 365.

7. Remove the TXT record (or MX record) from your DNS host once the domain is verified in Microsoft 365.

### Step 2: Find the MX record value for email and more

::: moniker range="o365-worldwide"

1. In the Microsoft 365 admin center, go to the **Settings** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">Domains</a> page.

::: moniker-end

::: moniker range="o365-21vianet"

1. In the admin center, go to the **Settings** > <a href="https://go.microsoft.com/fwlink/p/?linkid=2007048" target="_blank">Domains</a> page.

::: moniker-end

2. On the **Domains** page, select your domain.

3. Choose  **Manage DNS**, select **More Options** > **Add your own DNS** and select **Continue** to see the DNS records to add.

    You'll want to keep this information available while you make changes at your DNS host, so you can copy and paste the values.

    The groups of DNS records that are listed on the page depend on your choices listed under **Domain purpose**.

4. Go to [Add DNS records to connect your domain](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider), and follow the steps to add records at your DNS host's website.

5. Follow the steps for creating the records at your DNS host.

## Related content

- [Domains FAQ](../setup/domains-faq.yml) (article)
- [Find and fix issues after adding your domain or DNS records](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/find-and-fix-issues) (article)
- [Manage domains](https://learn.microsoft.com/en-us/admin) (link page)
