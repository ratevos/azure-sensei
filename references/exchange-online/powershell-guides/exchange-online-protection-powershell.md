# PowerShell for the Built-in security add-on for on-premises mailboxes

> Source: https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-protection-powershell  
> Microsoft doc last updated: 12/16/2025


PowerShell is the administrative interface that enables you to manage features in [the Built-in security add-on for on-premises mailboxes](https://learn.microsoft.com/en-us/exchange/standalone-eop/standalone-eop) from the command line. For example, you can use PowerShell to configure anti-spam policies, mail flow rules (also known as transport rules) and connectors to support on-premises email protection.

> [!TIP]
> All organizations with cloud mailboxes (Microsoft 365 A3/E3/G3, Microsoft 365 Business Standard, Microsoft 365 Business Premium, etc.) use [Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell) to manage these same features for cloud email protection.

PowerShell in the Built-in security add-on for on-premises mailboxes is available in the following scenarios:

- **On-premises email environments (not just Microsoft Exchange)**: Mail from the internet passes through the Microsoft cloud organization for protection and filtering before delivery to on-premises recipients. The Microsoft cloud organization contains no cloud mailboxes.
- **Exchange Enterprise CAL with Services**: The licenses for your on-premises Exchange organization include Exchange Enterprise CAL with Services (the Built-in security add-on for on-premises mailboxes is one of the services).

The following articles provide information about using PowerShell in the Built-in security add-on for on-premises mailboxes:

- To learn about the ExchangeOnlineManagement module that's required to connect to PowerShell, see [About the Exchange Online PowerShell module](https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2).

  To learn about what's new in the Exchange Online PowerShell module, see [What's new in the Exchange Online PowerShell module](https://learn.microsoft.com/en-us/powershell/exchange/whats-new-in-the-exo-module).

- The connection instructions for PowerShell in the Built-in security add-on for on-premises mailboxes and in Exchange Online PowerShell are the same. For instructions, see [Connect to Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell).

- To learn about the structure and layout of the cmdlet reference articles, see [Exchange cmdlet syntax](https://learn.microsoft.com/en-us/powershell/exchange/exchange-cmdlet-syntax).
