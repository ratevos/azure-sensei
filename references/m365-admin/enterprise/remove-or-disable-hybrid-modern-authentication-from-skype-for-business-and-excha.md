# Removing or disabling Hybrid Modern Authentication from Skype for Business and Exchange

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/remove-or-disable-hybrid-modern-authentication-from-skype-for-business-and-excha  
> Microsoft doc last updated: 08/13/2024


*This article applies to both Microsoft 365 Enterprise and Office 365 Enterprise.*

If you've enabled Hybrid Modern Authentication (HMA) only to find it's unsuitable for your current environment, you can disable HMA. This article explains how.

## Who is this article for?

If you've enabled Modern Authentication in Skype for Business Online or On-premises, and/or Exchange Online or On-premises and found you need to disable HMA, these steps are for you.

> [!IMPORTANT]
> See the '[Skype for Business topologies supported with Modern Authentication](https://learn.microsoft.com/en-us/skypeforbusiness/plan-your-deployment/modern-authentication/topologies-supported)' article if you're in Skype for Business Online or On-premises, have a mixed-topology HMA, and need to look at supported topologies before you begin.

## How to disable Hybrid Modern Authentication (Exchange)

1. **Exchange On-premises**: [Open the Exchange Management Shell](https://learn.microsoft.com/en-us/powershell/exchange/open-the-exchange-management-shell) and run the following commands:

   ```powershell
   Set-OrganizationConfig -OAuth2ClientProfileEnabled $false
   Set-AuthServer -Identity evoSTS -IsDefaultAuthorizationEndpoint $false
   ```

2. **Exchange Online**: [Connect to Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell). Run the following command to disable Modern Authentication:

   ```powershell
   Set-OrganizationConfig -OAuth2ClientProfileEnabled:$false
   ```

## How to disable Hybrid Modern Authentication (Skype for Business)

1. **Skype for Business On-premises**: Run the following commands in Skype for Business Management Shell:

   ```powershell
   Set-CsOAuthConfiguration -ClientAuthorizationOAuthServerIdentity ""
   ```

2. **Skype for Business Online**: [Connect to Skype for Business Online PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/manage-skype-for-business-online-with-microsoft-365-powershell). Run the following command to disable Modern Authentication:

   ```powershell
   Set-CsOAuthConfiguration -ClientAdalAuthOverride Disallowed
   ```

[Link back to the Modern Authentication overview](https://learn.microsoft.com/en-us/microsoft-365/enterprise/hybrid-modern-auth-overview).
