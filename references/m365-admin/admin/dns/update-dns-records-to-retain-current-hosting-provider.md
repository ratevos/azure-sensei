# Update DNS records to keep your website with your current hosting provider

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/dns/update-dns-records-to-retain-current-hosting-provider  
> Microsoft doc last updated: 04/23/2026


Check out all of our small business content on [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).

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

 **If you manage your domain's Microsoft records at your DNS hosting provider**, you don't have to worry about the steps in this topic. Your website stays where it is and people can still get to it.

 **If Microsoft manages your DNS records**, to route traffic to an existing public website hosted outside of Microsoft, after you add your domain to Microsoft, do the following:

## Update DNS records in the Microsoft 365 admin center

1. In the admin center, go to the **Settings** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834818" target="_blank">Domains</a> page.

1. On the **Domains** page, select the domain and then choose **DNS Records**.

1. Select **+ Add record** and enter the following:

   - For **type** enter: **A (Address)**

   - For **Host name or Alias**, type the following: **@**

   - For **IP Address**, type the static IP address for your website where it's currently hosted (for example, 172.16.140.1).

   This must be a *static* IP address for the website, not a *dynamic* IP address. Check with site where your website is hosted to make sure you can get a static IP address for your public website.

1. Select **Save**.

In addition, you can create a CNAME record to help customers find your website.

1. Select **+ Add record** and enter the following:

   - For **type** enter: **CNAME (Alias)**

   - For **Host name or Alias**, type the following: **www**

   - For **Points to address**, type the fully qualified domain name (FQDN) for your website (for example, contoso.com).

1. Select **Save**.

Finally, do the following:

[Update your domain's NS records](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain) to point to Microsoft.

When the NS records have been updated to point to Microsoft, your domain is all set up. Email will be routed to Microsoft, and traffic to your website address will continue to go to your current website host.
