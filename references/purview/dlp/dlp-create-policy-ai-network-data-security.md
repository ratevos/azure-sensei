# Use Network Data Security to help prevent sharing sensitive information with unmanaged AI

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-policy-ai-network-data-security  
> Microsoft doc last updated: 2026-06-26


Note

Some features used in this scenario are in preview.

This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) to show you how to create a Microsoft Purview data loss prevention (DLP) policy that helps prevent sharing sensitive information with unmanaged AI apps through network data security using an integrated SASE solution, such as Microsoft Entra Global Secure Access, or non-Microsoft secure browser solution. Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy this DLP policy scenario is as important as policy design. [Create and deploy a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

Important

Before you start this procedure, read [Learn about Microsoft Purview Network Data Security](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn). It provides important information about the prerequisites and assumptions for this scenario, including [considerations for unmanaged apps policies](https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn#considerations-for-unmanaged-cloud-apps-policies).

Before you begin, make sure the following prerequisites and assumptions are met:

- You have an supported SASE or secure enterprise browser integration. For more information on which integrations are supported, see the [Security Store in Microsoft Purview Data Loss Prevention](https://purview.microsoft.com/datalossprevention/securitystore).
- If you're using Microsoft Entra Global Secure Access
    - The device must be Entra ID joined.
    - You must configure a [Transport Layer Security inspection policy](https://learn.microsoft.com/en-us/en-us/entra/global-secure-access/how-to-transport-layer-security)
    - You must configure a [content policy in Microsoft Entra GSA Internet Access](https://learn.microsoft.com/en-us/en-us/entra/global-secure-access/how-to-network-content-filtering).
- If you are using a non-Microsoft SASE or secure enterprise browser provider
    - Ensure you've configured Purview pay-as-you-go billing. For more information, see [Enable Microsoft Purview pay-as-you-go features for new customers](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement#enable-microsoft-purview-pay-as-you-go-features-for-new-customers).
    - Ensure you've completed the integration steps outlined in your provider's documentation.
- This procedure uses hypothetical distribution groups, one named *Finance Team*, and another group for the *Security Team*. You have to create these groups in your environment or substitute your own groups.

## Policy intent statement and mapping

*We want to embrace responsible AI use within our organization while protecting customer and organizational sensitive data from intentional or accidental exposure. Because the Finance department regularly handles highly sensitive information, we need to create a policy that blocks Finance users from sharing sensitive content with any unsanctioned generative AI application. Since many of our users have flexibility in which browser they choose to use, as well as the ability to use locally installed AI apps and Office add-ins, we need to ensure broad endpoint coverage through network data security protection. Given the sensitivity of the Finance department’s access to data, we need to prevent financial data, personally identifiable information (PII), or confidential documents from being shared through text prompts or uploaded files. Then, to ensure efficient and quick incident management, we must generate alerts and ensure our security team is notified via email any time a block occurs. Lastly, we want this policy to take effect immediately to begin protecting company data as soon as possible.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| Because the Finance department regularly handles highly sensitive information, we need to create a policy that blocks Finance users from sharing sensitive content with any unsanctioned generative AI application. | Choose cloud apps to apply the policy: - Select **+ Add cloud apps**- Select the **Adaptive app scopes** tab- Choose **All unmanaged AI apps** and select **Add**- Select **Edit scope**- Select **Include only specific**- Choose the **Finance department** group |
| Since many of our users have flexibility in which browser they choose to use, as well as the ability to use locally installed AI apps and Office add-ins, we need to ensure broad endpoint coverage through network data security protection. | Choose where to enforce the policy:- Enable **Network and non-Microsoft secure browsers** |
| Given the sensitivity of the Finance department’s access to data, we need to prevent financial data, personally identifiable information (PII), or confidential documents... | Customize advanced DLP rules:- Select **+ Create rule**- Select **+ Add condition** and choose **Content contains**- Select **Add** and chooose **Sensitive info types**- Select **ABA Routing Number**, **U.S. Bank Account Number**, **Credit Card Number**, **U.S. Social Security Number (SSN)** and select **Add**- Select **Add** and choose **Sensitivity labels**- Choose **Confidential** and select **Add**- Ensure the **Group operator** is set to **Any of these** |
| ...from being shared through text prompts or uploaded files. | Actions:- Select **+ Add an action** and choose **Restrict browser and network activities**- Select **Text sent to or shared with cloud or AI apps** and **File uploaded to or shared with cloud or AI apps**- Select **Block** for both |
| Then, to ensure efficient and quick incident management, we must generate alerts and ensure our security team is notified via email any time a block occurs. | Incident reports:- Set the severity level to **High**-Ensure **Send an alert to admins when a rule match occurs** is **On**- Select **+ Add or remove users** and choose the **SecurityOps distribution group**- Ensure **Send alert every time an activity matches the rule** is selected, and then **Save** the rule |
| Lastly, we want this policy to take effect immediately to begin protecting company data as soon as possible. | Policy mode:- Select **Turn the policy on immediately** |

### Configure SASE provider integration

Important

You must have a Secure Access Service Edge (SASE) or non-Microsoft secure browser provider integrated with Purview to begin discovering and protecting content shared over the network.

To integrate your provider with Purview, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open the **Data Loss Prevention** solution and select **Security Store** from the left navigation bar.
3. Select **Get solution** for the provider you're using.
4. Complete the setup steps provided by your integrated SASE or secure browser provider.

### Steps to create policy

To create the DLP policy, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Data loss prevention** &gt; **Policies** &gt; **+ Create policy**.
3. Select **Inline web traffic**.
4. Select **Custom** from the **Categories** list and then select **Custom policy** from the **Regulations** list.
5. Choose **Next**.
6. Enter a policy name and provide an optional description. You can use the policy intent statement here.
7. Choose **Next**.
8. Select **+ Add cloud apps**.
9. Select the **Adaptive app scopes** tab, then choose **All unmanaged AI apps** and select **Add (1)**.
10. Select **Edit scope** on **All unmanaged AI apps**.
11. Select the **Include only specific** option on the **Add or edit the scope for All Unmanaged AI Apps**.
12. Select **+ Add inclusions**.
13. Select **Specific users and groups**.
14. Search for and select the **Finance department** group, then select **Add**.
15. Select **Save and close**.
16. Choose **Next**.
17. On the **Choose where to enforce the policy** page, ensure **Network and non-Microsoft secure browsers** is **On**, then select **Next**.

Note

If using a non-Microsoft SASE or secure enterprise browser integration, you must have pay-as-you-go configured. [Learn more about pay-as-you-go billing](https://learn.microsoft.com/en-us/purview/purview-billing-models).

1. On the **Define policy settings** page, ensure **Create or customize advanced DLP rules** is selected and select **Next**.
2. On the **Customize advanced DLP rules** page, select **+ Create rule**.
3. Give the rule a unique **name** and optional description.
4. Under **Conditions**
    1. Select **+ Add condition** then choose **Content contains**.
    2. Select **Add** and choose **Sensitive info types**.
    3. Choose **ABA Routing Number**, **U.S. Bank Account Number**, **Credit Card Number**, **U.S. Social Security Number (SSN)** and select **Add**.
    4. Select **Add** and choose **Sensitivity labels**
    5. Choose **Confidential** and select **Add**.
    6. Ensure the **Group operator** is set to **Any of these** for the **Content contains group**.
5. Under **Actions**
    1. Select **+ Add an action** and choose **Restrict browser and network activities**.
    2. Select **Text sent to or shared with cloud or AI apps** and **File uploaded to or shared with cloud or AI apps**.
    3. Select **Block** for both.
6. Under **Incident reports**
    1. Set the **Severity level in admin alerts and reports** to **High**
    2. Ensure **Send an alert to admins when a rule match occurs** is **On**
    3. Select **+ Add or remove users** and choose the **SecurityOps distribution group**
    4. Ensure **Send alert every time an activity matches the rule** is selected
7. Select **Save**.
8. Review the rule configuration, ensure it's status is **On**, and select **Next**.
9. On the **Policy mode** page choose **Turn the policy on immediately** and then select **Next**.
10. Review the policy information then select **Submit** to create the policy.
