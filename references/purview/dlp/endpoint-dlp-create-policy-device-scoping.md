# Create a DLP Policy Using Device Scoping

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-device-scoping  
> Microsoft doc last updated: 2026-06-26


This scenario shows how to scope a Microsoft Purview Endpoint DLP policy to specific device groups. For example, you can enforce a policy only when Finance users access data from Windows devices while excluding macOS devices. Device groups are commonly defined using dynamic device groups in Microsoft Entra ID.

This scenario is for an unrestricted admin creating a full directory policy.

This scenario requires that you already have devices onboarded and reporting into activity explorer. If you haven't onboarded devices yet, see [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started).

## Prerequisites and assumptions

This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important as policy design. [Deploy a DLP policy](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

You've created a dynamic device group.

## Policy intent statement and mapping

*An organization wants to enforce a DLP policy that blocks copying sensitive items with credit card data to USB devices when Finance users access data from Windows devices, and does not apply when the same users work from macOS devices.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “An organization wants to enforce a DLP policy that blocks copying sensitive items with credit card data to USB devices..." | - Administrative scope: Full directory- Where to monitor: Devices only- Policy scope: All users/Finance Windows Devices group |
| “when Finance users access data from Windows devices…” | - Condition: **Content contains** = **Credit Card Number** |
| “…and does not apply when the same users work from macOS devices…” | - Action: **Audit or restrict activities on devices**- Activity type: **File activities on all apps**- Restriction model: **Apply restrictions to specific activity**- **Copy to a removable USB device** = **Block** |

## Create a device group

If you're unfamiliar with dynamic device groups, see:

- [Create or update a dynamic membership group in Microsoft Entra ID](https://learn.microsoft.com/en-us/en-us/entra/identity/users/groups-create-rule)
- [Manage rules for dynamic membership groups in Microsoft Entra ID](https://learn.microsoft.com/en-us/en-us/entra/identity/users/groups-dynamic-membership).

To create the device group for this scenario:

1. Create a new dynamic device group named **Finance Windows Device** for the Windows devices that the finance team uses.

## Create a policy scoped to the dynamic device group

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **policies**.
2. Select **Create policy**.
3. Select **Enterprise applications & devices**.
4. Select the **Custom** from the **Categories** then **Custom policy** template from **Regulations**. Select **Next**.
5. Give your new policy a **Name** and **Description**.
6. Accept the default **Full directory** under **Admin units**.
7. Scope the location to only the **Devices** location.
8. Select **Edit** on the **Devices** location.
9. Accept the default **All users, groups, and adaptive scopes**
10. Select **Specific devices and device groups** and add the **Finance Windows Device** that you created.
11. Create a rule with the following values:

    - **Condition**: **Content contains** = **Sensitive Info types** = **Credit Card Number**
    - **Action**: **Audit or restrict activities on devices** &gt; **File activities for all apps** &gt; **Apply restrictions to specific activity** &gt; **Copy to a removable USB device** = **Block**.
12. Select **Save** and then **Next**.
13. Accept the default **Run the policy in simulation mode** value and choose **Show policy tips while in simulation mode**. Choose **Next**.
14. Review your settings and choose **Submit**.

The new DLP policy appears in the policy list.
