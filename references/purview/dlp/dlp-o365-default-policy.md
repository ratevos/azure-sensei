# Learn about the default Office 365 DLP policy

> Source: https://learn.microsoft.com/en-us/purview/dlp-o365-default-policy  
> Microsoft doc last updated: 2026-03-10


To help you protect sensitive data in Microsoft Office 365 apps, Microsoft created a default Microsoft Purview data loss prevention (DLP) policy called **Default Office 365 DLP policy**.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## What does the default policy do?

This default policy looks for items with the sensitive information type [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) It's configured like this.

- Admin units: **Full directory**
- Choose where to apply the policy:
    - **Exchange email** &gt; **All groups**
    - **SharePoint sites** &gt; **All sites**
    - **OneDrive accounts** &gt; **All users and groups**
- Conditions:
    - **Content is shared from Microsoft 365** &gt; **with people outside my organization** AND
    - **Content contains** &gt; **Credit card number**
- User Notifications:
    - **On**
    - **Notify these people** &gt; **The person who sent, shared, or modified the content** and **Owner of the SharePoint site or OneDrive account** and **Owner of the SharePoint or OneDrive content**.
    - **Attach matching email message to the notification (applies only to Exchange)**
    - With customized policy tip text.
- Policy mode: **Turn the policy on immediately**

Administrator can view the activities and edit the policies details by logging into the Microsoft Purview portal.

Admins can view this policy in the Microsoft Purview portal. Navigate to **Data Loss prevention** &gt; **Policies**.

## Edit or delete the default policy

To [edit the default policy for better performance or to delete it](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy), just use an account with **DLP Compliance Management** permissions. For more information, see, [Permissions](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions).
