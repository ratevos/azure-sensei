# Help prevent sharing via Microsoft Edge for Business to unmanaged AI apps from managed devices

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-policy-block-to-ai-via-edge  
> Microsoft doc last updated: 2026-06-26


This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview data loss prevention (DLP) policy that helps prevent sharing sensitive information from organization managed devices to unmanaged AI apps in Microsoft Edge for Business. Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Use this scenario to use the Edge for Business browser as the control point to block the sharing of sensitive information to unmanaged AI apps. The policy that's created here applies across all Edge browser profiles (work profile, personal profile and InPrivate) on Windows devices that are [managed by Microsoft Intune](https://learn.microsoft.com/en-us/en-us/intune/intune-service/fundamentals/manage-devices).

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important as policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

This procedure uses hypothetical distribution groups, one named *Finance Team*, and another group for the *Security Team*.

Important

Before you start this procedure, read [Learn about Data Loss Prevention for Cloud Apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn). It provides important information about the prerequisites and assumptions for this scenario, including [considerations for unmanaged apps policies](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn#considerations-for-unmanaged-cloud-apps-policies).

Implementing DLP policies for unmanaged apps in the browser follows these phases:

1. Create a DLP policy targeting unmanaged apps in the browser (the procedure in this article) in the Microsoft Purview Data Loss Prevention portal.
2. The creation of the DLP policy triggers the Microsoft Edge management service to automatically create the Microsoft Edge configuration policies required to activate DLP policies in Edge for Business. The configuration policies use [Microsoft Intune policies](https://learn.microsoft.com/en-us/en-us/deployedge/configure-edge-with-intune) to fully [activate your Microsoft Purview policies in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration).
3. (optional) Create a [collection policy](https://learn.microsoft.com/en-us/en-us/purview/collection-policies-policy-reference) that targets unmanaged apps in the browser to identify other sensitive data sharing across your organization.

Important

Activating a Purview DLP policy for unmanaged cloud apps automatically adds included users to the required Microsoft Edge configuration policies. When the Purview DLP policy is set to block, included users are blocked from using unprotected browsers where the policy doesn’t apply. The experience in Edge for Business isn’t impacted. For more information see: [activate your Microsoft Purview policy in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration).

## Licensing requirements

[!INCLUDE Microsoft Purview licensing]

## Policy intent statement and mapping

*We need to block members of the finance team from sharing sensitive information to unmanaged AI apps in Edge for Business. Other teams don't have access to this highly sensitive information, so the block only needs to apply to this team. When their prompts contain information like bank account, routing, or the SWIFT (Society for Worldwide Interbank Financial Telecommunication) numbers of our international customers, the sharing is blocked. We also have to meet alerting requirements. We want to notify our security team with an email every time there's a match to the policy. Lastly, we want the policy to take effect as soon as possible after testing, and we need to be able to see related activity within the system.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| We need to block members of the finance team from sharing sensitive information to unmanaged AI apps via Edge… | - Choose where to apply the policy: **Edge for Business**-Administrative scope: **Full directory**- Where to apply the policy: **Adaptive app scopes &gt; All unmanaged AI apps** |
| Other teams don’t have access to this information, so the block only needs to apply to this team... | - scope for each app" **specific users and groups, Include users and groups** &gt; **Finance Team** |
| When their text prompts contain information like bank account, routing or the SWIFT numbers of our international customers, the sharing should be blocked. | What to monitor: - use the **custom policy template**- Conditions for a match: **Content contains Sensitive info types** &gt; **ABA Routing Number**, **Australia Bank Account Number**, **Canada Bank Account Number**, **International Bank Account Number (IBAN)**, **Israel Bank Account Number**, **Japan Bank Account Number**, **New Zealand bank account number**, **SWIFT Code**, **U.S Bank Account Number**- Action: **Restrict browser and network activities** &gt; **Text upload** &gt; **Block** and **File upload &gt; Block** |
| We also have to meet alerting requirements. We want to notify our security team with an email every time there’s a match to the policy. | - Incident reports: **Send an alert to admins when a rule match occurs**- Send email alerts to these people (optional): add the **Security team**- Send an alert every time an activity matches the rule: **selected**- Use email incident reports to notify you when a policy match occurs: **On**- Send notifications to these people: add individual admins as desired - You can also include the following information in the report: **select all options** |
| ...Lastly, we want the policy to take effect as soon as possible after testing and need to be able to see related activity within the system.... | Policy mode: **on in simulation** |

### Create the policy for unmanaged AI apps

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Data loss prevention** &gt; **Policies** &gt; **+ Create policy**.
3. Select **Inline web traffic**.
4. Select **Custom** from the **Categories** list and then select **Custom policy** from the **Regulations** list.
5. Choose **Next**.
6. Enter a policy name and provide a description. You can use the policy intent statement here.

Important

You can't rename policies.

1. Choose **Next**.
2. Select **+ Add cloud apps &gt; Adaptive app scopes**
    1. Select **All unmanaged AI apps &gt; Add.** Unmanaged apps in the Generative AI category are included in this scope.

Important

Not all unmanaged AI apps are supported in Edge for Business. Adaptive app scopes apply only to the supported unmanaged AI apps in Edge for Business. For more information, see [Supported apps for browser DLP](https://learn.microsoft.com/en-us/en-us/purview/dlp-browser-dlp-learn).

1. Select **Edit** **scope**
2. Select **Include only specific**
3. Choose **+ Add inclusions**
4. Select **Finance Team**
5. Select **Add** and then select **Save and Close** and then select **Next**.
6. On the **Choose where to enforce the policy** step, select **Edge for Business.**
7. On the **Define policy settings** page, the **Create or customize advanced DLP rules** option should already be selected.
8. Choose **Next**.
9. On the **Customize advanced DLP rules** page, select **+ Create rule**.
10. Enter a name and description for the rule.
11. Select **Add condition** and use these values:

    1. Select **Content contains**.
    2. Select **Add** &gt; **Sensitive information types** &gt; **Sensitive info types** &gt; **ABA Routing Number**, **Australia Bank Account Number**, **Canada Bank Account Number**, **International Bank Account Number (IBAN)**, **Israel Bank Account Number**, **Japan Bank Account Number**, **New Zealand bank account number**, **SWIFT Code**, **U.S Bank Account Number**.
12. Select **Add**.
13. Under **Actions**, add an action with these values:

    1. **Restrict browser and network activities**
    2. **Text sent to or shared with cloud or AI apps** &gt; **Block**
    3. **File uploaded to or shared with cloud or AI app &gt; Block**
14. Under **Incident reports** select:

    1. Set **Use this severity level in admin alerts and reports** to **Low**.
    2. Set the toggle for **Send an alert to admins when a rule match occurs** to **On**.
    3. Under **Send email alerts to these people (optional)**, select **+ Add or remove users** and then add the email address of the security team.
15. Select **Save** and then select **Next**.
16. On the **Policy mode** page, select **Run the policy in simulation mode**.
17. Select **Next** and then select **Submit**.
18. Select **Done**.
19. The Microsoft Edge management service automatically creates the required configuration policies and required [Microsoft Intune policies](https://learn.microsoft.com/en-us/en-us/deployedge/configure-edge-with-intune) to [activate your Microsoft Purview policies in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration). Additional permissions are required for [Microsoft Intune administration](https://learn.microsoft.com/en-us/en-us/entra/identity/role-based-access-control/permissions-reference) and [Microsoft Edge administration](https://learn.microsoft.com/en-us/en-us/entra/identity/role-based-access-control/permissions-reference) for this step.

Important

If the [automatic Purview DLP configuration sync in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration) fails, Microsoft Purview shows an error message. Purview doesn’t enforce DLP and collection policies for unmanaged apps in Edge for Business until you resolve the error. An admin with the [required permissions for unmanaged cloud apps](https://learn.microsoft.com/en-us/en-us/purview/dlp-browser-dlp-learn#unmanaged-cloud-apps) must resync to resolve the error. For more information, see [activate your Microsoft Purview policy in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration).

Note

When the action of the policy is configured to **Block**, users are blocked at the device level from opening Firefox and other browsers. They are also blocked from opening Chrome if [Microsoft Purview extension for Chrome](https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about) isn't installed or is out of date. In Chrome with Microsoft Purview extension, access to a dynamic set of generative AI apps is blocked. For more information, see: [Activate your Microsoft Purview policies in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration)

## Steps to review outcomes of the policy in Microsoft Purview activity explorer

See [Activity explorer overview](https://learn.microsoft.com/en-us/en-us/purview/data-classification-activity-explorer) for instructions on how to monitor and view activities in the Activity explorer tool.

## Steps to review outcomes of Microsoft Purview policy in Microsoft Defender

See [Investigate and respond in Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/pilot-deploy-investigate-respond) for instructions on how to investigate and respond using Microsoft Defender.
