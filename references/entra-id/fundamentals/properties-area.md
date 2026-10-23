# Add your organization's privacy information

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/properties-area  
> Microsoft doc last updated: 04/30/2025


## Overview

This article explains how an administrator can add privacy-related info to an organization's directory through the Microsoft Entra admin center.

Add both your global privacy contact and your organization's privacy statement, so your internal employees and external guests can review your policies. Because each business creates and tailors its own privacy statements, contact a lawyer for assistance.

> [!NOTE]
> For information about viewing or deleting personal data, please review Microsoft's guidance on the [Windows data subject requests for the GDPR](https://learn.microsoft.com/en-us/microsoft-365/compliance/gdpr-dsr-windows) site. For general information about GDPR, see the [GDPR section of the Microsoft Trust Center](https://www.microsoft.com/trust-center/privacy/gdpr-overview) and the [GDPR section of the Service Trust portal](https://servicetrust.microsoft.com/ViewPage/GDPRGetStarted).

## Add your privacy information

You can find your privacy and technical information in the **Properties** area of the Microsoft Entra admin center.

### To access the properties area and add your privacy information

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Billing Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#billing-administrator).

1. Browse to **Entra ID** > **Overview** > **Properties**.

    

1. Add your privacy info for your users:

- **Technical contact.** Type the email address for the person to contact for technical support within your organization.

- **Global privacy contact.** Type the email address for the person to contact for inquiries about personal data privacy. This person is also who Microsoft contacts if there's a data breach related to Microsoft Entra services. If there's no person listed here, Microsoft contacts your Global Administrators. For Microsoft 365 related privacy incident notifications, see [Microsoft 365 Message center FAQs](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/message-center?preserve-view=true&view=o365-worldwide#frequently-asked-questions).

- **Privacy statement URL.** Type the link to your organization's document that describes how your organization handles both internal and external guests' data privacy.

  > [!IMPORTANT]
  > If you don't include either your own privacy statement or your privacy contact, your external guests will see text in the **Review Permissions** box that says, **<_your org name_> has not provided links to their terms for you to review**. For example, a guest user will see this message when they receive an invitation to access an organization through B2B collaboration.

  

4. Select **Accept**.

## Related content

- [Microsoft Entra B2B collaboration invitation redemption](https://learn.microsoft.com/en-us/entra/external-id/redemption-experience)
- [Add or change profile information for a user in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info)
