# Microsoft Entra Connect: Pass-through Authentication - Current limitations

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta-current-limitations  
> Microsoft doc last updated: 04/09/2025


## Supported scenarios

The following scenarios are supported:

- User sign-ins to web browser-based applications.
- User sign-ins to legacy Office client applications and Office applications that support [modern authentication](https://www.microsoft.com/en-us/microsoft-365/blog/2015/11/19/updated-office-365-modern-authentication-public-preview): Office 2013 and 2016 versions.
- User sign-ins to legacy protocol applications such as PowerShell version 1.0 and others.
- Microsoft Entra joins for Windows 10 and later devices.
- Hybrid Microsoft Entra joins for Windows 10 and later devices. 

## Unsupported scenarios

The following scenarios *aren't* supported:

- Detection of users with [leaked credentials](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection).
- Microsoft Entra Domain Services needs Password Hash Synchronization to be enabled on the tenant. Therefore tenants that use Pass-through Authentication *only* don't work for scenarios that need Microsoft Entra Domain Services.
- Pass-through Authentication isn't integrated with [Microsoft Entra Connect Health](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect).
- Signing in to Microsoft Entra joined (AADJ) devices with a temporary or expired password isn't supported for Pass-through authentication users. The error "the sign-in method you're trying to use isn't allowed" will appear. These users must sign in to a browser to update their temporary password.

> [!IMPORTANT]
> As a workaround for unsupported scenarios *only* (except Microsoft Entra Connect Health integration), enable Password Hash Synchronization on the [Optional features](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom#optional-features) page in the Microsoft Entra Connect wizard.
> 
> [!NOTE]
> Enabling Password Hash Synchronization gives you the option to failover authentication if your on-premises infrastructure is disrupted. This failover from Pass-through Authentication to Password Hash Synchronization isn't automatic. You'll need to switch the sign-in method manually using Microsoft Entra Connect. If the server running Microsoft Entra Connect goes down, you'll require help from Microsoft Support to turn off Pass-through Authentication.

## Next steps
- [Quick start](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta-quick-start): Get up and running with Microsoft Entra pass-through authentication.
- [Migrate your apps to Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/migration-resources): Resources to help you migrate application access and authentication to Microsoft Entra ID.
- [Smart Lockout](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-password-smart-lockout): Learn how to configure the Smart Lockout capability on your tenant to protect user accounts.
- [Technical deep dive](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta-how-it-works): Understand how the Pass-through Authentication feature works.
- [Frequently asked questions](how-to-connect-pta-faq.yml): Find answers to frequently asked questions about the Pass-through Authentication feature.
- [Troubleshoot](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication): Learn how to resolve common problems with the Pass-through Authentication feature.
- [Security deep dive](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta-security-deep-dive): Get deep technical information on the Pass-through Authentication feature.
- [Microsoft Entra hybrid join](https://learn.microsoft.com/en-us/entra/identity/devices/how-to-hybrid-join): Configure Microsoft Entra hybrid join capability on your tenant for SSO across your cloud and on-premises resources.
- [Microsoft Entra seamless SSO](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sso): Learn more about this complementary feature.
- [UserVoice](https://feedback.azure.com/d365community/forum/22920db1-ad25-ec11-b6e6-000d3a4f0789): Use the Microsoft Entra Forum to file new feature requests.
