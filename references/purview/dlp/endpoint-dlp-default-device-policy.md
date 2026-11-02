# Learn about the default DLP policy for devices

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-default-device-policy  
> Microsoft doc last updated: 2026-03-11


To help you protect sensitive data on endpoint devices, Microsoft provides a default Microsoft Purview data loss prevention (DLP) policy called **Default policy for devices**.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## What does the default policy do?

This default policy looks for items with the sensitive information type [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) It's configured like this.

- Admin units: **Full directory**
- Choose where to apply the policy: **Devices** &gt; **All users, groups, devices, device groups**
    - **SharePoint sites** &gt; **All sites**
    - **OneDrive accounts** &gt; **All users and groups**
- Conditions:
    - **Content contains** &gt; **Credit card number**
- Action:
    - **Audit or restrict activities on devices**
        - **Upload to a restricted cloud service domain or access from an unallowed browser** &gt; **Audit only**
        - **Copy to clipboard** &gt; **Audit only**
        - **Copy to a removable USB device** &gt; **Audit only**
        - **Copy to a network share** &gt; **Audit only**
        - **Print** &gt; **Audit only**
        - **Copy or move using unallowed Bluetooth app** &gt; **Audit only**
        - **Copy or move using RDP** &gt; **Audit only**
    - **App access restrictions** &gt; **Access by restricted apps** &gt; **Audit only**
- Policy mode: **Turn the policy on immediately**

Administrator can view the activities and edit the policies details by logging into the Microsoft Purview portal.

Admins can view this policy in the Microsoft Purview portal. Navigate to **Data Loss prevention** &gt; **Policies**.

## Edit or delete the default policy

To [edit the default policy for better performance or to delete it](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy), just use an account with **DLP Compliance Management** permissions. For more information, see, [Permissions](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions).
