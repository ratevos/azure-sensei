# Getting a mailbox not found error in Outlook on the web

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/mailbox-not-found-error  
> Microsoft doc last updated: 03/18/2025


If you're using Outlook on the web and you get a  **Mailbox couldn't be found for**  error, the account that you used to connect to Outlook on the web doesn't have an Exchange Online license and therefore, no mailbox is associated with the account.

## Assign a license to your account

Your admin can assign a license to your account by following these steps:

1. Go to the <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">Microsoft 365 admin center</a>. In the left nav pane, in the **Users**  section, select **Active users**, and then select the user who is seeing the error.
1. In the user page that opens, go to the  **Licenses and Apps**  section, select the appropriate  **Location**  value, and assign a license that contains Exchange Online (expand **Apps** to see its details).
1. When you're finished, click  **Save changes**.

## Related content

[Add another email alias for a user](https://learn.microsoft.com/en-us/microsoft-365/admin/email/add-another-email-alias-for-a-user) (article)\
[Configure email forwarding in Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/email/configure-email-forwarding) (article)\
[Create a shared mailbox](https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-a-shared-mailbox) (article)
