# Create policy to manage file activities by implementing network exceptions

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-file-activities-using-network-exceptions  
> Microsoft doc last updated: 2026-06-26


This scenario shows how to use **network-based conditions** in Microsoft Purview DLP to apply different protections based on where users access sensitive data. By defining VPN connections and configuring **network exceptions**, the policy adjusts actions—such as auditing or blocking clipboard activity—based on network context, enabling more precise control for hybrid work environments without uniformly restricting user activity.

This scenario is for an unrestricted admin creating a full directory policy.

## Prerequisites and assumptions

This scenario requires that you already have devices onboarded and reporting into Activity explorer. If you haven't onboarded devices yet, see [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started).

In this scenario, we define a list of VPNs that hybrid workers use for accessing organization resources.

This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview Data Loss Prevention (DLP) policy. Work through these scenarios in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

This scenario uses the *Confidential* sensitivity label, so it requires you to create and publish sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)

This procedure uses a hypothetical distribution group *Human Resources* and a distribution group for the security team at Contoso.com.

This procedure uses alerts, see: [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started)

## Policy intent statement and mapping

*We, Contoso, want to control how sensitive legal content is handled based on the network context in which users are operating. In particular, we want to apply different levels of restriction depending on whether users are connected through trusted corporate networks or VPN connections used by hybrid workers.*

*To achieve this, we will define known VPN connections and use them in **network exception rules** within a DLP policy. This allows us to enforce stricter controls—such as blocking clipboard activity with override—when users are connected through specific VPNs, while maintaining less restrictive (audit-only) behavior in other contexts. This approach enables contextual data protection that adapts to how and where users access sensitive data.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| “We want to apply different data protection controls depending on the network users are connected from…” | - Administrative scope: Full directory- Where to monitor: Devices only- Policy scope: All users/devices or targeted users |
| “We want to identify VPN connections used by hybrid workers…” | - Endpoint settings: Configure **VPN settings** using Server address or Network address- Data gathered via PowerShell commands (Get-VpnConnection, Get-NetConnectionProfile) |
| “We want to detect sensitive legal content handled on endpoints…” | - Condition: **Content contains** = Trainable classifiers, **Legal Affairs** |
| “We want to control specific user activities involving sensitive content…” | - Action: **Audit or restrict activities on devices**- Activity type: **File activities on all apps**- Specific activity: **Copy to clipboard** (extendable to others like print or USB copy) |
| “We want less restrictive monitoring under normal conditions…” | - Default activity action: **Audit only** for copy to clipboard |
| “We want stricter controls when users are connected through defined VPN networks…” | - Network exception: Select **VPN** and set action to **Block with override**- Priority: VPN must be set as top priority in network exception configuration |
| “We want to support user productivity while maintaining accountability…” | - Override capability: Users can proceed with justification when blocked under VPN conditions |
| “We want to ensure correct precedence of network-based rules…” | - Configuration behavior: VPN rules take precedence over Corporate network settings when ordered correctly- Caution: ‘Apply to all activities’ can overwrite other activity-specific configurations |
| “We want to safely test the policy behavior before full enforcement…” | - Policy mode: **Run in simulation mode**- User experience: **Show policy tips while in simulation mode** |
| “We want to validate policy behavior through monitoring and testing…” | - Monitoring: Use **Activity explorer** to review policy matches- Testing: Perform clipboard copy action under different network conditions (VPN vs non-VPN) |

## Steps to create policy

The following procedures walk you through defining VPN settings, verifying corporate network connectivity, and creating the DLP policy with network-based controls.

### Create and use a Network exception

Network exceptions enable you to configure Allow, Audit only, Block with override, and Block actions to file activities based on the network from which users access sensitive files. You can select from the [VPN settings](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#vpn-settings) list you've defined and use the **Corporate network** option. The actions can be applied individually or collectively to these user activities:

- Copy to clipboard
- Copy to a USB removable device
- Copy to a network share
- Print
- Copy or move using unallowed Bluetooth app
- Copy or move using RDP

#### Get the Server address or Network address

Use the following steps to retrieve the Server address or Network address values needed to define a VPN entry in the endpoint DLP settings.

1. On a DLP monitored Windows device, open a **Windows PowerShell** window as an administrator.
2. Run this cmdlet:

    ```powershell
    Get-VpnConnection
    ```
3. Running this cmdlet returns multiple fields and values.
4. Find the **ServerAddress** field and record that value. You use this when you create a VPN entry in the VPN list.
5. Find the **Name** field and record that value. The **Name** field maps to the **Network address** field when you create a VPN entry in the VPN list.

#### Determin if the device is connected through a Corporate network

Use the following steps to verify whether the device is currently connected through a corporate network.

1. On a DLP monitored Windows device, open a **Windows PowerShell** window as an administrator.
2. Run this cmdlet:

    ```powershell
    Get-NetConnectionProfile
    ```
3. If the **NetworkCategory** field is **DomainAuthenticated**, then the device is connected to a corporate network. If its anything else, the device's connection is not through a corporate network.

#### Add a VPN

After you collect the server or network address, use the following steps to add the VPN to the Endpoint DLP settings.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Settings** &gt; **Data Loss Prevention** &gt; **Endpoint settings** &gt; **VPN settings**.
3. Select **Add or edit VPN addresses**.
4. Provide either the **Server address** or **Network address** value that you recorded in the Get the Server address or Network address procedure.
5. Select **Save**.
6. Close the item.

#### Configure policy actions

Use the following steps to create the DLP policy and configure its network-based controls for file activities.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open **Data Loss Prevention** &gt; **Policies**.
3. Select **Create policy**
4. On the **Choose what to protect** page, select **Data stored in connected sources**.
5. Select **Custom** from the **Categories** list, then select the **Custom policy** template from **Regulations**.
6. Name your new policy and provide a description.
7. Select **Full directory** under **Admin units**.
8. Scope the location to **Devices** only.
9. Create a rule where:

    1. **Content contains** = **Trainable classifiers**, **Legal Affairs**
    2. **Actions** = **Audit or restrict activities on devices**
    3. Then pick **File activities on all apps**
    4. The select **Apply restrictions to specific activity**
    5. Select the actions that you want to configure **Network exceptions** for.
10. Select **Copy to clipboard** and the **Audit only** action
11. Select **Choose different copy to clipboard restrictions**.
12. Select **VPN** and set the action to **Block with override**.

    Important

    When you want to control the activities of a user when they're connected through a VPN *you must* select the VPN and make the VPN the top priority in the **Network exceptions** configuration. Otherwise, if the **Corporate network** option is selected, then that action defined for the **Corporate network** entry will be enforced.

Caution

The **Apply to all activities** option will copy the network exceptions that are defined here and apply them to all the other configured specific activities, like **Print**, and **Copy to a network share**. ***This will overwrite the network exceptions on the other activities The last saved configuration wins.***
13. **Save**.
14. Accept the default **Run the policy in simulation mode** value and choose **Show policy tips while in simulation mode**. Choose **Next**.
15. Review your settings and choose **Submit** and then **Done**.
16. The new DLP policy appears in the policy list.
