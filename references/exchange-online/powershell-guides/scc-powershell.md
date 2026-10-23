# Security & Compliance PowerShell

> Source: https://learn.microsoft.com/en-us/powershell/exchange/scc-powershell  
> Microsoft doc last updated: 9/1/2023


Security & Compliance PowerShell is the administrative interface that enables you to manage compliance and some security features of your Microsoft 365 organization from the command line (mostly Microsoft Purview risk and compliance features that were formerly part of Microsoft 365 compliance). For example, you can use Security & Compliance PowerShell to perform Compliance Searches. The following articles provide information about using Security & Compliance PowerShell:

- To learn about the ExchangeOnlineManagement module that's required to connect to Security & Compliance PowerShell, see [About the Exchange Online PowerShell module](https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2).

  > [!TIP]
  > Version 3.0.0 and later (2022) is known as the Exchange Online PowerShell V3 module (abbreviated as the EXO V3 module). Version 2.0.5 and earlier (2021) was known as the Exchange Online PowerShell V2 module (abbreviated as the EXO V2 module).

  To learn about what's new in the Exchange Online PowerShell module, see [What's new in the Exchange Online PowerShell module](https://learn.microsoft.com/en-us/powershell/exchange/whats-new-in-the-exo-module).

- To connect to Security & Compliance PowerShell, see [Connect to Security & Compliance PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-scc-powershell). The connection instructions are different from Exchange Online PowerShell.

  To connect to Security & Compliance PowerShell for unattended scripts, see [App-only authentication for unattended scripts in the Exchange Online PowerShell module](https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2).

- To learn about the structure and layout of the cmdlet reference articles in Security & Compliance PowerShell, see [Exchange cmdlet syntax](https://learn.microsoft.com/en-us/powershell/exchange/exchange-cmdlet-syntax).

Security & Compliance PowerShell contains the following types of cmdlets:

- Cmdlets that correspond to features available only in Purview compliance and the Microsoft Purview compliance portal. Most cmdlets in Security & Compliance PowerShell fall into this category.
- Basic cmdlets that are also available in Exchange Online PowerShell (for example, [Get-User](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/get-user), and [Get-RoleGroup](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/get-rolegroup)).
- A few cmdlets that correspond to default protections for cloud mailboxes and protections in Microsoft Defender for Office 365 in the Microsoft Defender portal (for example, [Set-SecOpsOverridePolicy](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/set-secopsoverridepolicy)).

  Cmdlets for most built-in security features for all cloud mailboxes and Defender for Office 365 security features (for example, [anti-spam policies](https://learn.microsoft.com/en-us/defender-office-365/anti-spam-protection-about)) are available only in [Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell).

Check the **Applies to** value in the cmdlet references article to verify the PowerShell environment where the cmdlet actually resides.
