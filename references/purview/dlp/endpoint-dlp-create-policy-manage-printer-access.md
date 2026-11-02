# Create policy to manage printer access using authorization groups

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-manage-printer-access  
> Microsoft doc last updated: 2026-06-26


This scenario demonstrates how to use **authorization groups** in Microsoft Purview DLP to enforce a default block on sensitive data actions while allowing controlled exceptions. In this example, printing of documents classified as legal content is restricted across all devices, except for a defined set of approved **legal department printers**.

Combining **device-level print restrictions** with a printer allowlist enables organizations to protect sensitive information while still supporting legitimate business workflows. This scenario also illustrates how authorization groups can be reused for other scenarios, such as removable storage devices or network shares.

This scenario is for an unrestricted admin creating a full directory policy.

The procedures in this article require that you already have devices onboarded and reporting into Activity explorer. If you haven't onboarded devices yet, see [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started).

Authorization groups are mostly used as allowlists. You assigned policy actions to the group that are different than the global policy actions. In this scenario, we go through defining a printer group and then configuring a policy with block actions for all print activities except for the printers in the group. The procedures for defining a printer group and configuring policy exceptions are essentially the same for **Removeable storage device groups**, and **Network share groups**.

In this scenario, we define a group of printers that the legal department uses for printing contracts. Printing contracts to any other printers is blocked.

## Prerequisites and assumptions

This article uses the DLP policy design process described in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

This scenario uses the *Confidential* sensitivity label, so it requires you to create and publish sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)

This procedure uses a hypothetical distribution group *Human Resources* and a distribution group for the security team at Contoso.com.

The policy-creation procedure in this article uses alerts, see: [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)

## Policy intent statement and mapping

*We, Contoso, want to prevent users from printing sensitive legal content to unauthorized printers while still allowing approved business workflows for the legal department. In this scenario, documents that match the **Legal Affairs** trainable classifier should be protected from being printed broadly across the organization, but users in Legal must be able to print those documents to a defined set of approved printers.*

*To achieve this, we will create a policy that applies print restrictions on devices for content classified as legal in nature. Printing will be blocked by default, but an **authorization group** of approved printers will be configured as an exception and allowed. This enables a strong default-protect posture while supporting legitimate business needs through a controlled allowlist model.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to protect sensitive legal documents from being printed to unauthorized printers…” | - Administrative scope: Full directory- Where to monitor: Devices only- Policy scope: All users/devices covered by the policy |
| “We want to identify documents that contain legal-sensitive content…” | - Condition: **Content contains** = Trainable classifiers, **Legal Affairs** |
| “We want to restrict printing of that sensitive content across endpoint devices…” | - Action: **Audit or restrict activities on devices**- Activity type: **File activities on all apps**- Restriction model: **Apply restrictions to specific activity** |
| “We want printing to be blocked by default unless explicitly allowed…” | - Activity restriction: **Print = Block** |
| “We want approved legal department printers to be exempt from the default block…” | - Endpoint settings: Create a **Printer group** named **Legal printers**- Group members can be defined by friendly printer name, USB product/vendor ID, IP range, print-to-file, Universal Print, corporate printer, or print to local |
| “We want different policy behavior for approved printers than the global policy action…” | - Authorization group behavior: **Choose different print restrictions**- Printer group restriction: Add **Legal printers**- Group-specific action: **Allow** |
| “We want approved printing activity to remain visible for audit purposes without creating unnecessary alerts…” | - Allow action behavior: Allowed print activity is recorded in the audit log- No alert or user notification is generated for the allowlisted printer action |
| “We want to test the policy safely before enforcement…” | - Policy mode: **Run the policy in simulation mode**- User experience: **Show policy tips while in simulation mode** |
| “We want to use this same design pattern for other authorized destinations in the future…” | - Reusable authorization group model: Same approach applies to **Removable storage device groups** and **Network share groups** |

## Steps to create policy

### Create and use printer groups

Perform the following steps to create a printer group for approved legal printers:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Settings** (gear in the upper left hand corner) &gt; **Data Loss Prevention** &gt; **Endpoint settings** &gt; **Printer groups**.
2. Select **Create printer group** and enter a **Group a name**. In this scenario, we use `Legal printers`.
3. Select **Add printer** and provide a name. You can define printers by:

    1. Friendly printer name
    2. USB product ID
    3. USB vendor ID
    4. IP range
    5. Print to file
    6. Universal print deployed on a printer
    7. Corporate printer
    8. Print to local
4. Select **Close**.

### Configure policy printing actions

Perform the following steps to configure the DLP policy's printing actions and assign the printer group exception:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Navigate to **Data loss prevention** &gt; **Policies**.
3. Select **Create policy**.
4. **Data stored in connected sources**.
5. Select the **Custom** from the **Categories** then **Custom policy** template from **Regulations**.
6. Give your new policy a **Name** and **Description**.
7. Accept the default **Full directory** under **Admin units**.
8. Scope the location to only the **Devices** location.
9. Create a rule with the following values:

    1. Add a **Condition**: **Content contains** = **Trainable classifiers**, **Legal Affairs**
    2. **Actions** = **Audit or restrict activities on devices**
    3. Then pick **File activities on all apps**
    4. The select **Apply restrictions to specific activity**
    5. Select **Print** = **Block**
10. Select **Choose different print restrictions**
11. Under **Printer group restrictions**, select **Add group** and select **Legal printers**.
12. Set **Action** = **Allow**.

    Tip

    The **Allow** action wil record and audit event to the audit log, but not generate an alert or notification.
13. Select **Save** and then **Next**.
14. Accept the default **Run the policy in simulation mode** value and choose **Show policy tips while in simulaiton mode**. Choose **Next**.
15. Review your settings and choose **Submit**.
16. The new DLP policy appears in the **Data loss prevention** &gt; **Policies** list.
