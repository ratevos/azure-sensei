# Select the domain to use for email from Microsoft 365 products

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/email/select-domain-to-use-for-email-from-microsoft-365-products  
> Microsoft doc last updated: 03/04/2024


**In this article**:

- [Configure the "Send email notifications from your domain" setting](#configure-the-send-email-notifications-from-your-domain-setting)
- [Supported Products](#supported-products)
- [Excluded Scenarios](#excluded-scenarios)

Emails sent out to users as they interact with each other and across various products within Microsoft 365 are designed to provide insights and information about their organization. These emails are typically sent out between users based on those interactions, which means that they're often sent from the user’s email address. Those emails remain unchanged and continue to work as they do today.

There are several scenarios where emails are sent from a “no-reply” system-based product account. For example, batched comments, news, digests, and system notification emails are currently sent from a no-reply product address. These include addresses such _no-reply@sharepointonline.com_, _no-reply@planner.com_, _no-reply@project.com_.

The default option is that users receive no-reply emails sent by Microsoft on behalf of your organization. Your users receive these emails as [EXTERNAL] notifications. You can now use a custom domain as the sender of these notifications. Using this feature means that emails are sent from your own Exchange Online instance and they become internal communication. For example, **no-reply@sharepointonline.com [External]** could become **no-reply@contoso.com**, if **Contoso.com** is the selected domain.

> [!NOTE]
> Only domains registered within your tenant can be used and ownership must be verified through the existing add domains process within Microsoft 365. Use the following steps and note the Domain Name System (DNS) records required when configuring a domain for sending email.

<a name="configsetting"></a>
## Configure the "Send email notifications from your domain" setting

The setting is available via the Microsoft 365 Admin Center **Settings** menu item. Select **Settings**, select **Org settings**, and then select the **Organization profile** tab as illustrated. 

> [!NOTE]
> - This setting is an opt-in setting that allows the Microsoft 365 system administrators to select a verified domain within the tenant, meaning that the domain is validated for ownership.
> - The recommendation is to use a domain that has the appropriate DNS records to facilitate email validation, like SPF, DKIM, DMARC, and MX as this then complies with the [RFC compliance](https://www.ietf.org/rfc/rfc2142.txt) for sending and receiving email. For more information, see [Learn more about Exchange Online Email Routing](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/mail-flow-best-practices).
> - Ensure you comply with all privacy, compliance, and security requirements and policies within your organization. 

**To configure the "Send email notifications from your domain" setting:**

1. In the Microsoft 365 admin center, in the navigation pane select **Settings**.
2. Select **Org settings**.
3. On the **Org settings** page, select **Organization profile**.
4. On the **Organization profile** page, select **Send email notifications from your domain**.
5. In the **Send email notifications from your domain** page, select **Use a custom send-from domain address**.
6. The **Domains** menu, select the domain that you want to use for your email replies. The domains listed in the menu includes verified complete and incomplete domains as Microsoft 365 allows DNS settings to be configured and managed outside of the tenant. Your System or Exchange administrator must ensure that they follow and meet all DNS and domain requirements. 
7. For **Custom username**, administrators can optionally configure the no-reply prefix. They could then create a matching email address in Exchange, if they would like to monitor responses from users.
8. Select **Save**. Changes take a few minutes to complete.

> [!NOTE]
> If you make a mistake or would like to roll back the change, deselect the **Use a custom send-from domain address** checkbox and then select **Save**. The setting will revert to the original configuration.

<a name="supportedproducts"></a>
## Supported products

Note that the following products currently support this feature: 
- SharePoint Online
- OneDrive for Business
- Office
- Stream
- Planner
- Project
- Viva Connections
- Viva Glint
- Viva Pulse
- Viva Topics
- Viva Amplify
- Teams

> [!NOTE]
> The supported products list is updated as each product migrates to support the setting and no action is required as these products onboard to the centralized setting. 

<a name="excludedscenarios"></a>
## Excluded Scenarios
One Time Passcodes (OTP) generated from sharing within OneDrive and SharePoint Online will continue to use _no-reply@notify.microsoft.com_. These are secure emails generated by Microsoft and utilize this trusted sender address to ensure delivery of these emails.
