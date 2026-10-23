# Update your MX records to transition to the global Exchange Online service

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/transition-to-global-exchange-online  
> Microsoft doc last updated: 02/13/2026


The following steps describe how to transition from Microsoft Cloud Germany Exchange Online to the global Exchange Online service:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select [**Domains**](https://go.microsoft.com/fwlink/p/?linkid=834818).

1. In the **Domains** page, the status for each domain is shown under the **Status** column. If your organization's domains point to Microsoft Cloud Germany Exchange Online, the domain's MX records need to be updated.

1. Select the affected domain, and then select **DNS errors detected** to view the details.

1. The page that opens has instructions showing how to fix the MX record. If your domain's registrar uses [Domain Connect](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/add-domain#domain-connect-registrars-integrated-with-microsoft-365), you can select **Fix my records** at the top. Otherwise you can follow the link in the wizard for step-by-step instructions for your registrar.
