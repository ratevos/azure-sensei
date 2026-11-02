# Data loss prevention policy tip reference for Outlook for Android, iOS, and macOS

> Source: https://learn.microsoft.com/en-us/purview/dlp-outlook-mobile-policy-tip-ref  
> Microsoft doc last updated: 2026-03-26


Outlook for Android, iOS, and macOS now supports data loss prevention (DLP) policy tips with commonly used predicates and exceptions, advanced classifiers, and override capabilities.

## Licensing requirements

## Policy tips supported in Outlook for Android, iOS, and macOS

## Enable Policy Tips UI to Appear

Policy Tip UI is turned off by default in Outlook for Android, iOS, and macOS to allow for administrators to test and perform user training prior to deployment.

To enable Policy Tip UI to appear in Outlook for Android, iOS, and macOS, you must enable the policy listed in the following section in the Microsoft 365 Apps Admin Center. To access this policy setting, go to the [Microsoft 365 Admin Center](https://admin.cloud.microsoft/), expand "All Admin Centers" to find the "Microsoft 365 app" admin center.

You can access this policy under **Customization** and **Policy Management**. You can target policies to individuals or groups, so you can test and deploy policy tip UI as needed through your organization.

| Policy Name | Value |
| --- | --- |
| Enable Purview Data Loss Prevention (DLP) policy tips in Outlook | (default) **Disabled** policy tips aren't shown **Enabled** policy tips are shown |

## Supported conditions and actions

For details on actions that support policy tips, see [Exchange actions support policy tips](https://learn.microsoft.com/en-us/en-us/purview/dlp-ol365-win32-policy-tips).

## Supported SITs

For details on sensitive information types that support policy tips for Microsoft 365 users, see [Sensitive information types](https://learn.microsoft.com/en-us/en-us/purview/dlp-ol365-win32-policy-tips).

## Supported custom SITs

All custom SITs are supported.

## Supported EDM SITs

All EDM SITs are supported.

## Supported sensitivity labels

All sensitivity labels are supported.

## Supported retention labels

All retention labels are supported.

## Supported trainable classifiers

All trainable classifiers are supported.

## Actions and information types that support policy tips

All actions and information types for email communications are supported.

For details on creating and using all policy tip types, see [DLP Policy Reference](https://learn.microsoft.com/en-us/en-us/purview/dlp-policy-reference).

## Oversharing dialog for Outlook for Android and iOS

The oversharing dialog is available in DLP for Outlook for Android and iOS users when used with the necessary licenses and configuration. When you enable this feature in a DLP rule, it displays popups for warning, override, or block actions to end users who are sharing labeled or sensitive emails in Outlook for Android and iOS.

### Default oversharing dialog

This dialog uses the exact same text as the policy tip (default or custom) and, when applicable, a noncustomizable set of justification options to override the policy.

### Customized oversharing dialog

You can choose to tailor your oversharing dialog with a customized title, body, and dynamic variables like %%MatchedRecipientsList%%, and justification options. For more information, see [Customized Oversharing Dialog](https://learn.microsoft.com/en-us/en-us/purview/dlp-policy-reference-new-outlook).

## Wait on send dialog support for oversharing

Outlook for Android and iOS doesn't yet support *DLP Wait‑to‑Send, which is* centrally managed [Exchange Online mailbox settings](https://learn.microsoft.com/en-us/en-us/powershell/module/exchangepowershell/set-organizationconfig). For future announcements, see the Microsoft 365 Roadmap, [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=Outlook%2CAndroid%2CiOS%2CMobile).

For Exchange mailbox parameters, see [Set-OrganizationConfig (ExchangePowerShell) | Microsoft Learn](https://learn.microsoft.com/en-us/en-us/powershell/module/exchangepowershell/set-organizationconfig).
