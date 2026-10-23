# Change your email address to use your custom domain

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/email/change-email-address  
> Microsoft doc last updated: 04/23/2025


Check out [Microsoft 365 small business help](https://go.microsoft.com/fwlink/?linkid=2197659) on YouTube.

 **[Check the Domains FAQ](../setup/domains-faq.yml)** if you don't find what you're looking for. 
  
::: moniker range="o365-worldwide"

Your initial email address in Microsoft 365 includes .onmicrosoft.com, like tom@fourthcoffee.onmicrosoft.com. You can change it to a friendlier address like tom@fourthcoffee.com. You'll need your own domain name, like fourthcoffee.com first. If you already have one, great! If not, you can learn how to [buy one from a domain registrar](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/buy-a-domain-name).

::: moniker-end

::: moniker range="o365-21vianet"

Your initial email address in Microsoft 365 operated by 21Vianet includes partner.onmschina.cn, like tom@fourthcoffee.partner.onmschina.cn. You can change it to a friendlier address like tom@fourthcoffee.cn. You'll need your own domain name, like fourthcoffee.cn first. If you already have one, great! If not, you can learn how to [buy one from a domain registrar](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/buy-a-domain-name).

::: moniker-end

When you change your domain's email to come to Microsoft 365, by updating your domain's MX record during setup, ALL email sent to that domain will start coming to Microsoft 365. Make sure you've added users and created mailboxes in Microsoft 365 for everyone who has email on your domain BEFORE you change the MX record. Don't want to move email for everyone on your domain to Microsoft 365? You can take steps to [pilot Microsoft 365 with just a few email addresses instead](https://learn.microsoft.com/en-us/microsoft-365/admin/misc/pilot-microsoft-365-from-my-custom-domain).
  
## Set up business email with a new domain

Check out this video and others on our [YouTube channel](https://go.microsoft.com/fwlink/p/?linkid=2198215).

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=e06209e9-487f-4f5c-be79-d658aca544be]

Buy a new domain name for your email address and set up the email addresses with Microsoft 365.

1. Buy a new domain name for your email address by providing your contact information for the new domain name, choosing your payment method, and then placing your order.
1. Change the first part of the address (before the @ sign) or leave it as is. 
1. Sign out of Microsoft 365, and then sign back in with your new email address. Your employee email addresses are updated with the new domain. 

## Set up business email with an existing domain

> [!VIDEO https://learn-video.azurefd.net/vod/player?id=8ea6055b-328d-4ce9-a1ac-fa515cd16b7d]

Use a domain name you already own whether you're using it for a website address or an email address at another provider.

1. Sign into the website that hosts your domain. Click a button to verify automatically or update the domain manually. 
1. Customize the email address or leave it as is.
1. Sign out of Microsoft 365, and then sign back in with your new email address. Your employee email addresses are updated with the new domain.

## Change your email address to use your custom domain using the Microsoft 365 admin center

You must be a global admin to perform these steps.

> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

::: moniker range="o365-worldwide"

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>.

::: moniker-end

::: moniker range="o365-21vianet"

1. Go to the admin center at <a href="https://go.microsoft.com/fwlink/p/?linkid=850627" target="_blank"> https://portal.partner.microsoftonline.cn</a>.

::: moniker-end

2. Go to the **Settings** > **Domains** page.

3. On the **Domains** page, select **Add domain**.

4. Follow the steps to confirm that you own your domain. You'll be guided to get everything set up correctly with your domain in Microsoft 365.

5. Go to **Users** > **Active users**.

6. Select a user to edit their username and change it to the domain you just added.

> [!NOTE]
> If you are not using an Exchange license, you cannot use the domain to send or receive emails from the Microsoft 365 tenant.
  
## Related content

[Buy a custom domain using Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/buy-a-domain-name) (article)\
[Manage domains](https://learn.microsoft.com/en-us/admin) (link page)\
[Domains FAQ](../setup/domains-faq.yml) (article)
