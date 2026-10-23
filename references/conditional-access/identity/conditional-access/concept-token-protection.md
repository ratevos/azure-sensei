# How Token Protection Enhances Conditional Access Policies

> Source: https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection  
> Microsoft doc last updated: 08/14/2026


## Overview

Token Protection is a Conditional Access session control that attempts to reduce token replay attacks by ensuring only device bound sign-in session tokens, like [Primary Refresh Tokens (PRTs)](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token), are accepted by Microsoft Entra ID when applications request access to protected resources.  

When a user registers a supported device with Microsoft Entra, a PRT is issued and cryptographically bound to that device. This binding ensures that even if a threat actor steals the token, it can't be used from another device. With Token Protection enforced, Microsoft Entra validates that only these bound sign-in session tokens are used by supported applications. 

> [!NOTE]
> Use Token Protection as part of a broader defense-in-depth strategy against token theft. For more information, see [Protecting tokens in Microsoft Entra](https://learn.microsoft.com/en-us/entra/identity/devices/protecting-tokens-microsoft-entra-id). 

## Platform availability

| Platform | Native applications | Browser-based applications |
|----------|---------------------|----------------------------|
| Windows | Generally Available | Preview for supported web apps that access Azure Resource Manager |
| iOS / iPadOS | Generally Available | Not supported |
| macOS | Generally Available | Preview for supported web apps that access Azure Resource Manager |

> [!NOTE]
> Browser-based application support is currently limited to selected web apps, browsers, and device configurations that access Azure Resource Manager. For requirements and the list of supported applications, see [Token Protection deployment guide - Web apps](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-web-apps).

## Supported resources

For native applications, Token Protection policy can be enforced on the following cloud resources:
- Exchange Online
- SharePoint Online
- Microsoft Teams

On Windows, enforcement is also supported for:
- Azure Virtual Desktop
- Windows 365

For browser-based applications in preview, enforcement is supported for Azure Resource Manager, configured in Conditional Access as the **Windows Azure Service Management API** resource. Only selected web applications that access Azure Resource Manager are supported. For details, see [Token Protection deployment guide - Web apps](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-web-apps).

### Supported devices

**Windows**:
- Windows 10 or newer devices that are Microsoft Entra joined, Microsoft Entra hybrid joined, or Microsoft Entra registered. See the known limitations section in the appropriate deployment guide for unsupported device types.  
- Windows Server 2019 or newer that are hybrid Microsoft Entra joined.
- For detailed steps on how to register your device, see [Register your personal device on your work or school network](https://support.microsoft.com/account-billing/register-your-personal-device-on-your-work-or-school-network-8803dd61-a613-45e3-ae6c-bd1ab25bf8a8).
- Browser-based application support (Preview) has additional operating system, browser, extension, and configuration requirements. See [Token Protection deployment guide - Web apps](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-web-apps).

**Apple (Preview)**:
- macOS 14.0 or later. Requires the Microsoft Enterprise single sign-on (SSO) plug-in. Alternatively, you can also use Platform SSO. Only MDM-managed devices are supported.
- iOS / iPadOS 16.0 or later. Requires the Microsoft Enterprise SSO plug-in. Only MDM-managed devices are supported.
- For detailed steps on how to set up, see [Enabling Microsoft Enterprise SSO plug-in](https://learn.microsoft.com/en-us/entra/identity-platform/apple-sso-plugin) and configuring [Platform SSO for macOS](https://learn.microsoft.com/en-us/intune/intune-service/configuration/platform-sso-macos).
- Browser-based application support (Preview) on macOS has additional browser, extension, and configuration requirements. See [Token Protection deployment guide - Web apps](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-web-apps).

## Deployment

To minimize the likelihood of user disruption due to app or device incompatibility, follow these recommendations: 

- Start with a pilot group of users and expand over time. 
- Create a Conditional Access policy in [report-only mode](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) before enforcing token protection. 
- Capture both interactive and non-interactive sign-in logs. 
- Analyze these logs long enough to cover normal application use.
- Add known, reliable users to an enforcement policy. 

This process helps assess your users' client and app compatibility for token protection enforcement. 

### Deployment guides

Select the guide for your target platform:

- **Windows**: [Token Protection deployment guide - Windows](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-windows)
- **iOS, iPadOS, and macOS**: [Token Protection deployment guide - Apple](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-apple)
- **Web apps that access Azure Resource Manager (Preview)**: [Token Protection deployment guide - Web apps](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-web-apps)

## Related content 

[What is a Primary Refresh Token?](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token)
