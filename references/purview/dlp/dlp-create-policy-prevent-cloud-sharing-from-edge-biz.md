# Help prevent users from sharing sensitive information with cloud apps in Microsoft Edge for Business

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-policy-prevent-cloud-sharing-from-edge-biz  
> Microsoft doc last updated: 2026-06-26


Use this procedure to create a Microsoft Purview data loss prevention (DLP) policy that blocks users from exfiltrating sensitive information from business-managed apps (such as ServiceNow and Workday) in Microsoft Edge for Business. This procedure follows the policy design process described in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy). Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Use the managed-app browser DLP policy scenario to block users from exfiltrating sensitive information from business-managed apps such as ServiceNow and Workday through Microsoft Edge.

**Prerequisites:**

- Onboard the apps to Microsoft Entra Conditional Access with session controls applied.
- Block access to the protected apps outside the Edge work profile.

**When the policy applies:**

This policy takes effect when users access the protected apps in Edge for Business and sign in with their work or school account for both the Edge work profile and the app. Edge for Business applies DLP policies for unmanaged devices only to the work profile. These policies don’t apply to personal or InPrivate profiles unless the [work profile that opens the InPrivate](https://learn.microsoft.com/en-us/en-us/edge/browse-inprivate-in-microsoft-edge) window has a policy applied. To target managed apps on unmanaged devices, enforce the work profile in Edge for Business.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important as policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

The following policy-creation procedure uses a hypothetical distribution group named *External*. For more information on DLP protections applying in the browser, see [browser data security resources](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn).

Important

Read [Learn about Data Loss Prevention for Cloud Apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) before you start this procedure. It provides important information about the prerequisites and assumptions for this scenario.

Setting up a policy to protect data sharing with Microsoft Entra-managed apps in the browser follows these phases:

1. Onboard apps to [Conditional Access app control](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/proxy-deployment-featured-idp).
2. [Import user groups from connected apps](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/user-groups). Importing user groups is necessary for you to target groups in your Entra Conditional Access policy and your Purview policies for managed apps in Edge for Business.
3. Create a [Microsoft Entra Conditional Access policy](https://learn.microsoft.com/en-us/en-us/entra/identity/conditional-access/concept-conditional-access-session) that’s configured with custom session controls enabled and using the client apps condition for browser.
4. Enable [Edge for Business in-browser protection](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/in-browser-protection), configured to enforce Edge work profile sign in for business apps on all devices.
5. Create a Microsoft Purview DLP policy targeting user interactions with managed apps.
6. (optional) Activate Protected Clipboard and Screen Capture prevention capabilities in the Microsoft Admin Portal settings for Microsoft Edge. See the [Get started with Protected Clipboard for Microsoft Edge for Business](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-management-protected-clipboard#gettingstarted) instructions.
7. Review outcomes of Microsoft Purview policy in Microsoft Defender.

Important

The user and the app must both be in scope for all the prerequisite protections for the policy to apply to the user in Edge.

## Policy intent statement and mapping

*We need to allow users to access resources in business apps from their BYOD and personal devices, but block them from downloading the data to those devices. Contractors and vendor employees use these types of devices to collaborate for their work activities. When they attempt to download files containing sensitive information, like customer banking information, the action should be blocked. We also have to meet alerting requirements. Lastly, we want this to take effect as soon as possible.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| We need to allow users to access resources in business apps like Workday from their BYOD and personal devices, but block them from downloading the data to their devices … | - Choose where to apply the policy: **Enterprise apps and Devices**-Administrative scope: **Full directory**- Where to apply the policy: **Managed apps &gt; Workday** |
| Contractors and vendor employees use these types of devices to collaborate for their work activities.... | - scope alongside apps" **specific users and groups, Include users and groups** &gt; **External** |
| When they attempt to download files containing sensitive information, like customer banking information, the action should be blocked. | What to monitor: - use the **custom policy template**- Conditions for a match: **Content contains Sensitive info types** &gt; **ABA Routing Number**, **Australia Bank Account Number**, **Canada Bank Account Number**, **International Bank Account Number (IBAN)**, **Israel Bank Account Number**, **Japan Bank Account Number**, **New Zealand bank account number**, **SWIFT Code**, **U.S Bank Account Number**- Action: **Restrict browser and network activities** &gt; \*\*File download \*\* &gt; **Block**. |
| We also have to meet alerting requirements. Our security team must have a way to investigate and take actions against the policy match outcomes. | - Incident reports: **Send an alert to admins when a rule match occurs** is on by default |
| ...Lastly, we want this to take effect as soon as possible.... | Policy mode: \*\*on \*\* |

## Steps to set up prerequisites

Complete the following steps to set up the prerequisites before you create the DLP policy:

1. Onboard apps to Conditional Access app control. For more information, please see [Onboard non-Microsoft IdP catalog apps for Conditional Access app control](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/proxy-deployment-featured-idp) and [Onboard non-Microsoft IdP custom apps for Conditional Access app control](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/proxy-deployment-any-app-idp).
2. Import user groups. Sign into the Microsoft Defender XDR, select **Settings &gt; Cloud Apps &gt; System &gt; User groups &gt; + Import.** For more information, please see [Import user groups from connected apps](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/user-groups).
3. Sign into the [Microsoft Entra admin center.](https://entra.microsoft.com/)
4. Create a new [Conditional Access policy that targets cloud apps with session controls and using the and using the client apps condition for browser.](https://learn.microsoft.com/en-us/en-us/entra/identity/conditional-access/concept-conditional-access-session).

    1. **Custom policy** must be selected in the session controls dropdown.
    2. **Browser** must be selected in **Conditions &gt; Client Apps**
5. In the Microsoft Defender portal at https://security.microsoft.com), go to System &gt; Settings &gt; Cloud apps &gt; Conditional Access App Control section &gt; Edge for Business protection. Or, to go directly to the Edge for Business protection page, use https://security.microsoft.com/cloudapps/settings?tabid=edgeIntegration.
6. Configure in-browser protection for Edge on, selecting **Allow access only from Edge** and **All devices**

Important

To include groups in policies targeting managed cloud apps, you must first [import user groups from connected apps](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/user-groups).

## Steps to create the policy

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Data loss prevention** &gt; **Policies** &gt; **+ Create policy**.
3. Select **Enterprise apps and Devices**.
4. Select **Custom** from the **Categories** list and then **Custom policy** from the **Regulations** list.
5. Choose **Next**.
6. Provide a policy name and give a description. You can use the policy intent statement here.
7. Select **Next**.
8. Accept the default **Full directory** on the **Assign admin units** page.
9. Choose **Next**.
10. Select **Managed cloud apps**
11. Select **Specific users and groups**.
12. Choose **+ Include** and then **Include groups**.
13. Select **External**.
14. Choose **Done** and then choose **Next**.
15. Select **+ Include managed apps**.
16. Select **Workday**
17. Choose **Done**
18. On the **Define policy settings** page, the **Create or customize advanced DLP rules** option should already be selected.
19. Choose **Next**.
20. On the **Customize advanced DLP rules** page, select **+ Create rule**.
21. Name the rule and give a description.
22. Select **Add condition**and use these values:
    1. Select **Content contains**.
    2. Select **Add** &gt; **Sensitive information types** &gt; **Sensitive info types** &gt; **ABA Routing Number**, **Australia Bank Account Number**, **Canada Bank Account Number**, **International Bank Account Number (IBAN)**, **Israel Bank Account Number**, **Japan Bank Account Number**, **New Zealand bank account number**, **SWIFT Code**, **U.S Bank Account Number**.
23. Choose **Add**.
24. Under **Actions**, add an action with these values:
    1. **Restrict browser and network activities**
    2. **File download** &gt; **Block**
25. Under **Incident reports** select: 2. The toggle for **Send an alert to admins when a rule match occurs** defaults to **On**.
26. Choose **Save** and then choose **Next**.
27. On the **Policy mode** page, choose **On**.
28. Choose **Next** and then choose **Submit**.
29. Choose **Done**.

Important

The DLP policy won't be applied in Edge until all requirements are met.

## Steps to activate Microsoft Edge for Business Protected Clipboard and Screen Capture protections (optional)

See the [Get started with Protected Clipboard for Microsoft Edge for Business](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-management-protected-clipboard#gettingstarted) instructions.

## Steps to review outcomes of a Microsoft Purview policy in Microsoft Defender

See [Investigate and respond in Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/pilot-deploy-investigate-respond) for instructions on how to review and act on policy match outcomes.
