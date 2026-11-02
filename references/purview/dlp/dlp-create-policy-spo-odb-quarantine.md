# Create a DLP policy to quarantine files in SharePoint and OneDrive

> Source: https://learn.microsoft.com/en-us/purview/dlp-create-policy-spo-odb-quarantine  
> Microsoft doc last updated: 2026-10-21


Note

The features described in this article are in preview. This article uses the process you learned in [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) to show you how to create a Microsoft Purview data loss prevention (DLP) policy that automatically quarantines files containing sensitive information in SharePoint and OneDrive. Work through this scenario in your test environment to familiarize yourself with the quarantine action and policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users. How you deploy a policy is as important as policy design. [This article](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

Before you start, make sure you've completed the following:

### Create a quarantine site in SharePoint

The quarantine destination must be a SharePoint site in your tenant. You can't use a subsite or a OneDrive location. If you select a subsite, quarantined files are moved to the site that contains the subsite instead. You can use any SharePoint site template.

When you set up your quarantine site:

- **Restrict access.** Make sure the site is accessible only by the administrators who manage quarantine operations. Don't share it with information workers or general users.
- **Don't use a site that contains active business content.** Create a dedicated site for quarantine purposes.
- **Manage the lifecycle.** Administrators are responsible for access control and lifecycle management of the quarantine site.

Tip

If your organization uses on-demand classification, it's recommended that you exclude the quarantine site from on-demand classification scans. While scanning the quarantine site doesn't compromise security, excluding it avoids unnecessary processing.

### Configure quarantine settings in Microsoft Purview

Before you can select the quarantine action in a DLP policy, you must configure the quarantine folder path and tombstone file message in DLP settings.

Important

You can't select the quarantine action in a DLP policy until you complete this configuration. The policy creation wizard prompts you to configure these settings first if they aren't already set.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Go to **Data loss prevention** &gt; **Settings**.
3. Select **File quarantine**.
4. Under **Quarantine folder path**, select a SharePoint site from the list of available sites.

    Note

    The site list is automatically populated from your tenant's SharePoint sites. You can't manually enter a path. If you recently created a new SharePoint site, it might take time for the site to appear in the list. If the site you need isn't listed, wait and check back later.
5. Under **Replacement file message**, provide the text content for the tombstone file that replaces each quarantined file. For example:

    *"This file has been moved to a secure quarantine location because it matched a data loss prevention policy. Contact your compliance administrator at compliance@contoso.com for assistance."*
6. Save your settings.

Important

You can't select the quarantine action in a DLP policy until you complete this configuration. The policy creation wizard prompts you to configure these settings first if they aren't already set.

### Sensitivity label requirements

This scenario uses the *Highly Confidential* sensitivity label. To learn more, see:

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)

### Alert configuration

This procedure uses alerts. See [Get started with the data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started).

## Policy intent statement and mapping

*We need to quarantine files in SharePoint and OneDrive that contain financial data classified as "Highly Confidential," so that the files are removed from their original location and placed in a secure admin-controlled quarantine site. We want a tombstone file left in the original location to notify the file owner. We want the compliance admin alerted whenever a file is quarantined.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| "We need to quarantine files in SharePoint and OneDrive..." | - **Where to monitor:** SharePoint sites, OneDrive accounts- **Administrative scope:** Full directory- **Action:** Restrict access or encrypt the content in Microsoft 365 locations &gt; **Block everyone and move file to quarantine location** |
| "...that contain financial data classified as 'Highly Confidential'..." | - **What to monitor:** Use the **Custom template**- **Conditions for match:** Add the sensitive info types that apply to the financial data your organization needs to protect (for example, *Credit Card Number*, *U.S. Bank Account Number*).- **Additional condition:** Content contains &gt; Sensitivity labels &gt; *Highly Confidential* |
| "We want the compliance admin alerted whenever a file is quarantined." | - **Incident reports:** Send an alert to admins when a rule match occurs: **On**- Send alert every time an activity matches the rule: **selected**- Severity level: **High** |
| "We want a tombstone file left in the original location to notify the file owner." | - Tombstone file content is configured in **DLP Settings** &gt; **File quarantine** (not in the policy itself). Verify that the tombstone message is configured before you create this policy. |

## Steps to create the policy

Important

For this policy creation procedure, accept the default include and exclude values and leave the policy turned off. Change these values when you deploy the policy.

### Create the policy

Perform the following steps to create the DLP policy in the Microsoft Purview portal.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open the **Data loss prevention** solution and go to **Policies**.
3. Select **Create policy**.
4. Select **Enterprise applications & devices**.
5. Select **Custom** from the **Categories** list.
6. Select **Custom policy** from the **Regulations** list.
7. Select **Next**.
8. Enter a name and description for the policy. You can use the policy intent statement here.

    Important

    Policies can't be renamed.
9. Select **Next**.
10. Accept the **Full directory** default under **Admin units**.
11. Select **Next**.
12. Choose where to apply the policy. Select only the following locations:

    - **SharePoint sites**
    - **OneDrive accounts**
13. Select **Next**.
14. On the **Define policy settings** page, make sure the **Create or customize advanced DLP rules** option is selected.
15. Select **Next**.
16. Select **+ Create rule**. Name the rule and provide a description.
17. Under **Conditions**, select **Add condition** &gt; **Content contains** &gt; **Add** &gt; **Sensitive info types**.
18. Select the sensitive info types that apply to the financial data you want to protect (for example, *Credit Card Number*, *U.S. Bank Account Number*).
19. Select **Add**.
20. Optionally, add a sensitivity label condition:

    1. Under the **Content contains** section, select **Add group**.
    2. Leave the Boolean operator set to **AND**.
    3. Select **Add condition** &gt; **Content contains** &gt; **Add** &gt; **Sensitivity labels**.
    4. Select the **Highly Confidential** sensitivity label.
    5. Select **Add**.
21. Under **Actions**, select **Add an action** &gt; **Restrict access or encrypt the content in Microsoft 365 locations**.
22. Select **Block everyone and move file to quarantine location**.

    Note

    If quarantine settings aren't configured, you're prompted to configure them. Select the link to open the **File quarantine** settings page in a new tab, complete the configuration, and then return to the policy creation wizard.
23. Under **User notifications**, set the toggle to **On** if you want to notify users through policy tips.
24. Under **Incident reports**, set **Use this severity level in admin alerts and reports** to **High**.
25. Make sure the **Send an alert to admins when a rule match occurs** toggle is set to **On**.
26. Select **Send alert every time an activity matches the rule**.
27. Select **Save**.
28. Review the rule, then select **Next**.
29. Select the **Run the policy in simulation mode** radio button.

    Tip

    Simulation mode is supported for the quarantine action. Use simulation mode to evaluate the impact of the policy before you turn it on. Review the policy matches in Activity Explorer and the DLP alerts dashboard to verify that the policy targets the files you expect.
30. Select **Next**.
31. Review the policy, then select **Submit**.
32. Select **Done**.

## Validate the policy

After the policy is deployed, validate the following:

| Scenario | Expected result |
| --- | --- |
| A file matching the policy is uploaded to a SharePoint site in scope. | The file is moved to the quarantine site. A tombstone file appears at the original location. A DLP alert is generated. |
| Check the tombstone file at the original location. | The tombstone file displays the admin-configured message and the relative path of the quarantined file. |
| Review the DLP alert. | The alert shows the file owner, original file path, and quarantine file location. |
| Review Activity Explorer. | A DLP rule match event appears with quarantine file location details. |
