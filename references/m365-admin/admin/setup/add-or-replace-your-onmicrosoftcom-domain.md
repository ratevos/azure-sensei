# Add or replace a onmicrosoft.com fallback domain

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-or-replace-your-onmicrosoftcom-domain  
> Microsoft doc last updated: 04/23/2026


When you sign up for Microsoft 365, Microsoft provides an *onmicrosoft.com* domain. The *onmicrosoft.com* domain is your **fallback domain**. Microsoft provides the fallback domain in case you don't own a domain or don't want to connect a domain to Microsoft 365. An example of a fallback domain is:

> [!IMPORTANT]
> To prevent misuse and help improve deliverability of customer email, we recommend that onmicrosoft.com domains should only be used for testing purposes, not sending regular email.
>
> Starting **October 15, 2025**, we are introducing limits that might restrict your Microsoft 365 environment from sending to more than 100 external recipients per 24 hours, see: [Limiting Onmicrosoft Domain Usage for Sending Emails](https://techcommunity.microsoft.com/blog/exchange/limiting-onmicrosoft-domain-usage-for-sending-emails/4446167).

When you sign up for Microsoft 365, Microsoft provides an *onmicrosoft.com* domain - your **fallback domain** - in case you don't own a domain, or don't want to connect it to Microsoft 365 (for example, tailspintoys.onmicrosoft.com). Your fallback domain is used by default in:

Use your fallback domain by default in:

- Usernames and email addresses.
- Microsoft 365 teams and groups email aliases.
- Automatic domain dependency moves.

The fallback domain serves as a default email routing address for your Microsoft 365 environment. When you set up a user with a mailbox, email routes to the fallback domain. If you use a custom domain, for example, `tailspintoys.com`, and you delete that custom domain from your Microsoft 365 environment, the fallback domain ensures that your user's email is successfully routed.

You can change your fallback domain in the Microsoft 365 admin center. Common reasons customers change their fallback domain include:

- They didn't know the company name to use when they first signed up for Microsoft 365. Now that they know the company name, they want their users to have sign in account names that are appropriate.

- They want to change how their SharePoint URLs look when they create a new site. SharePoint URLs in your Microsoft 365 environment are created based on your fallback domain name. If you didn't use the correct company name when you first signed up, your SharePoint URLs for your sites continue to use that name when you create new SharePoint sites.

While you can add more onmicrosoft.com domains, you can use only one onmicrosoft.com domain as your fallback domain. The steps in this article describe how to:

- Create a new onmicrosoft.com domain.
- Assign it as your fallback domain.

> [!WARNING]
>
> You're limited to a total of five onmicrosoft.com domains in your Microsoft 365 environment. Once created, onmicrosoft.com domains can't be deleted.

## Before you begin

To add, modify, or remove domains, you must be a **Domain Name Administrator** of a [business or enterprise plan](https://products.office.com/business/office). These changes affect the whole tenant. *Custom admin roles* or *regular users* can't make these changes.

## Add a new onmicrosoft.com domain

To add a new onmicrosoft.com domain, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, select your onmicrosoft.com default domain.

    

1. On the domain properties page, in the **About this domain** section, select **Add onmicrosoft domain**.

    

1. In the **Add onmicrosoft domain** page, in the **Domain name** box, type the name for your new onmicrosoft.com domain.

    

    > [!IMPORTANT]
    >
    > Make sure to verify the spelling and accuracy of the domain name you entered. You're limited to five onmicrosoft.com domains, and currently you can't delete them once you create them.

1. Select **Add domain**. When you add the domain successfully, you see a message stating that it was successfully added.

    

## Make your new onmicrosoft.com domain your fallback domain

> [!TIP]
>
> Before changing your fallback domain to a new onmicrosoft.com domain, consider changing your onmicrosoft.com SharePoint domain. Creating another onmicrosoft.com domain and using it as your fallback domain doesn't rename SharePoint in Microsoft 365. Your existing SharePoint and OneDrive URLs stay the same.
>
> You can change your.onmicrosoft.com SharePoint domain through the PowerShell steps provided in [SharePoint domain rename preview](https://learn.microsoft.com/en-us/sharepoint/change-your-sharepoint-domain-name).

After you create your new onmicrosoft.com domain, change your fallback domain:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, select the new onmicrosoft.com domain that you created.

    

1. On the domain's property page, select **Make fallback domain**.

    

1. A message displays on the page stating that your fallback domain changed to the new domain.

    

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
- [Buy a domain name in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/buy-a-domain-name).
- [Connect your domain by adding DNS records](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/create-dns-records-at-any-dns-hosting-provider).
- [Change nameservers to set up Microsoft 365 with any domain registrar](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/change-nameservers-at-any-domain-registrar).
- [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).
