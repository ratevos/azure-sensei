# Send Email Notifications and Show Policy Tips for DLP Policies

> Source: https://learn.microsoft.com/en-us/purview/dlp-use-notifications-and-policy-tips  
> Microsoft doc last updated: 2026-06-22


You can use a Microsoft Purview Data Loss Prevention (DLP) policy to identify, monitor, and protect sensitive information across Microsoft 365. You want people who work with sensitive information to stay compliant with your DLP policies without being blocked from getting their work done. This is where email notifications and policy tips can help.



When you create a DLP policy, you can configure the user notifications to:

- Send an email notification to the people you choose that describes the issue.
- Display a policy tip for content that conflicts with the DLP policy:

    - For Outlook on the web and Outlook 2013 and later, the policy tip appears at the top of a message above the recipients while the message is being composed.
    - For documents in a OneDrive account or SharePoint site, the policy tip shows as a warning icon that appears on the item. To view more information, you can select an item and then choose **Information** in the upper-right corner of the page to open the details pane.
    - For Excel, PowerPoint, and Word documents that are stored on a OneDrive site or SharePoint site that's in scope of a DLP policy, the policy tip appears on the Message Bar and the Backstage view (**File** menu &gt; **Info**).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

Note

Notification emails are sent unprotected.

## Options for configuring email notifications

For each rule in a DLP policy, you can:

- Send the notification to the people you choose. These people can include the owner of the content, the person who last modified the content, the owner of the site where the content is stored, or a specific user.
- Customize the text that's included in the notification by using HTML or tokens. For more information, see Custom email notifications.

Note

- You can send email notifications only to individual recipients, not to groups or distribution lists.
- Only new content triggers an email notification. Editing existing content triggers policy tips, but not email notifications.
- External senders receive only a templatized notification without full details to prevent any unintended loss of information about the policy configuration.



### Default email notification

Notifications have a **Subject** line that begins with the action taken, such as `Notification`, `Message Blocked` for email, or `Access Blocked` for documents. If the notification is about a document, the notification message body includes a link. That link takes you to the site where the document's stored and opens the policy tip for the document, where you can resolve any issues. If the notification is about a message, the notification includes as an attachment the message that matches a DLP policy.



By default, notifications display text similar to the following for an item on a site. You configure the notification text separately for each rule, so the text that's displayed differs depending on which rule is matched.

| If the DLP policy rule does this... | Then the default notification for SharePoint or OneDrive documents says this... | Then the default notification for Outlook messages says this... |
| --- | --- | --- |
| Sends a notification but doesn't allow override | This item conflicts with a policy in your organization. | Your email message conflicts with a policy in your organization. |
| Blocks access, sends a notification, and allows override | This item conflicts with a policy in your organization. If you don't resolve this conflict, access to this file might be blocked. | Your email message conflicts with a policy in your organization. The message wasn't delivered to all recipients. |
| Blocks access and sends a notification | This item conflicts with a policy in your organization. Access to this item is blocked for everyone except its owner, last modifier, and the primary site admin. | Your email message conflicts with a policy in your organization. The message wasn't delivered to all recipients. |

### Custom email notifications

You can create a custom email notification template for end user email notifications for each rule. Then send it instead of sending the default email notification. This option is available for policies scoped to the Exchange, SharePoint, and OneDrive locations.



Select **Preview and edit notification email** to create a customized template when you edit or create a rule in a policy.

The custom email notification supports HTML and customization of these fields:

- Sender display name: Define a custom value that suits your organization's needs. There's a 70 character limit. Setting this value doesn't change the sender's email address.
- Email subject: Define a custom value to make the email subject more meaningful to your end users. There's a 256 character limit.
- Email body: Define a custom value that has greater meaning to your users. There's a 5120 character limit. You can use HTML or markdown to include images, formatting, and other branding in the notification. Custom definition for the email body supports the use of inline styling. If you add actions that users can take to email, only markdown can be used to format the email body.

Note

If you configure a sender email alias in Exchange Admin Center mailboxes, it overwrites the **sender display name** that you configure here.

You can also use the following tokens to help customize the body of the email. Tokens are variables that get replaced by specific information when the notification is sent. For example, the %%ContentURL%% token is replaced by the URL of the document on the SharePoint site or OneDrive site.

| Token | Description | Available for Exchange | Available for SharePoint | Available for OneDrive |
| --- | --- | --- | --- | --- |
| %%MatchedConditions%% | The conditions that the content matched. Use this token to inform people of possible issues with the content. | Yes | Yes | Yes |
| %%ContentURL%% | The URL of the document on the SharePoint site or OneDrive site. | No | Yes | Yes |
| %%AppliedActions%% | The actions applied to the content. This token is populated only when the action - **Restrict access or encrypt the content in Microsoft 365 locations** is selected in the DLP rule configuration | Yes | Yes | Yes |
| %%BlockedMessageInfo%% | The details of the message that was blocked. Use this token to inform people of the details of the message that was blocked. This token is populated only when the action - **Restrict access or encrypt the content in Microsoft 365 locations** is selected in the DLP rule configuration | Yes | No | No |
| %%ContentId%% | The unique identifier of the message. | Yes | No | No |
| %%TimestampForIncidentOccurrence%% | Timestamp in UTC of when the DLP policy conditions were matched. | Yes | Yes | Yes |
| %%MatchedConditionsAndValues%% | The matched DLP condition and values. This token doesn’t cover the *content contains sensitive info* condition. For matched SITs and redacted values, see %%MatchedSITAndSurroundingcontext%% | Yes | Yes | Yes |
| %%Filename%% | For SharePoint and OneDrive matches, this token shows the document name. For Exchange, it shows the email attachment name. | Yes | Yes | Yes |
| %%PolicyName%% | The matched DLP policy name. | Yes | Yes | Yes |
| %%PolicyRule%% | The matched DLP rule name. | Yes | Yes | Yes |
| %%Workload%% | The workload name where the match occurred. | Yes | Yes | Yes |
| %%MatchedSITAndSurroundingcontext%% | The matched SITs and the redacted values. | Yes | Yes | Yes |
| %%UserEmail%% | The email address of the end user associated with the matched content. | Yes | Yes | Yes |
| %%SiteAdmin%% | For SharePoint sites, this token shows the email address of the site administrator. | No | Yes | No |
| %%EmailSubject%% | For Exchange, this token shows the email subject. | Yes | No | No |
| %%EmailRecipients%% | For Exchange, this token shows the list of email recipients. | Yes | No | No |
| %%FileOwner%% | For SharePoint and OneDrive matches, this token shows the name of file owner. | No | Yes | Yes |

Note

Use the HTML &lt;div&gt; tag to style the tokens. For example, &lt;div\ "style="color:blue; font-size: 12px;"&gt; %%MatchedConditions%% &lt;/div&gt; renders the token in font size 12 px and font color blue.



## Actionable email notifications for OneDrive and SharePoint workloads

Note

Actionable email notifications for OneDrive and SharePoint workloads are in preview.

Admins can add controls to customized email notifications. These controls enable users to fix the issue that caused the DLP policy match or otherwise remediate issues on OneDrive folders or SharePoint sites directly from the email. This streamlines the remediation process. The controls are:

- **Stop sharing file**: Removes any sharing access and links on the file.
- **Delete file**: Deletes the file.
- **Apply sensitivity or retention label on the file**: Opens the OneDrive or SharePoint folder or site where the file is located so the user can apply the sensitivity or the retention label.
- **Override the policy**: Requires the end user to add business justification and overrides the policy.
- **Report false positive**: Requires the end user to enter the justification and notifies the admin via audit log.
- **Report unable to take action**: Requires the end user to enter the justification and notifies the admin via audit log.

To make these options available to your users in notification emails, select them when you configure the email notification.

Note

Only markdown mode can be used to format the email body if you add actions to the email.

Actions details in unified audit logs:

- Delete, Stop share, Apply label: Record types = **SharepointFileOperation**
- Override, Report false positive, Report unable to take action: Activities - operation names = **DLPInfo**, Record types = **ComplianceDLPSharePoint**

## Options for configuring policy tips

For each rule in a DLP policy, you can configure policy tips to:

- Notify the person that the content conflicts with a DLP policy, so they can take action to resolve the conflict. You can use the default text (see the tables below) or enter custom text about your organization's specific policies.
- Allow the person to override the DLP policy. Optionally, you can:

    - Require the person to enter a business justification for overriding the policy. This information is logged and you can view it in the DLP reports in the **Reports** section of the portal.
    - Allow the person to report a false positive and override the DLP policy. This information is also logged for reporting, so that you can use false positives to fine tune your rules.



For example, say you have a DLP policy applied to OneDrive sites that detects personal data, and this policy has three rules:

1. First rule: If fewer than five instances of this sensitive information are detected in a document, and the document is shared with people inside the organization, the **Send a notification** action displays a policy tip. For policy tips, no override options are necessary because this rule is simply notifying people and not blocking access.
2. Second rule: If more than five instances of this sensitive information are detected in a document, and the document is shared with people inside the organization, the **Block access to content** action restricts the permissions for the file, and the **Send a notification** action allows people to override the actions in this rule by providing a business justification. Your organization's business sometimes requires internal people to share personal data, and you don't want your DLP policy to block this work.
3. Third rule: If more than five instances of this sensitive information are detected in a document, and the document is shared with people outside the organization, the **Block access to content** action restricts the permissions for the file, and the **Send a notification** action doesn't allow people to override the actions in this rule because the information is shared externally. Under no circumstances should people in your organization be allowed to share personal data outside the organization.

### User override support

The override option is per rule, and it overrides all of the actions in the rule.

Content can match several rules in a DLP policy or several different DLP policies, but only the policy tip from the most restrictive rule that has the highest priority is shown. This includes policies that are in simulation mode. This setup prevents people from seeing a cascade of policy tips.

For example, if a document matches three rules in a DLP policy, and the rules have these configurations, rule LMN is applied and the policy tip from rule LMN is shown to the user.

| Rule name | Rule priority | Rule action | Rule action applied |
| --- | --- | --- | --- |
| ABC | 1 | Send notification | No |
| LMN | 2 | Block access and send notification | Yes |
| XYZ | 3 | Block | No |

If the policy tips in the most restrictive rule allow people to override the rule, then overriding this rule also overrides any other rules that the content matched.

If you set the NotifyAllowOverride action to WithoutJustification or WithJustification or FalsePositives, make sure BlockAccess is set to true and BlockAccessScope has appropriate value. Otherwise, the policy tip comes up but the user doesn't find an option to override the email with justification.

To see overrides in policy tips in Outlook on the web, the policy must be set to the *Turn it on* state. The policy action must also be configured to block with override.

#### Availability of override

The following table shows when override is available for each notification and block-action combination.

| Notification Rule | Notify/Block action | Override available | Require Justification |
| --- | --- | --- | --- |
| Notify only | Notify | No | No |
| Notify + AllowOverride | Notify | No | No |
| Notify + AllowOverride + False positive | Notify | No | No |
| Notify + AllowOverride + With justification | Notify | No | No |
| Notify + AllowOverride + False positive + Without justification | Notify | No | No |
| Notify + AllowOverride + False positive + With justification | Notify | No | No |
| Notify + Block | Block | No | No |
| Notify + Block + AllowOverride | Block | Yes | No |
| Notify + Block + AllowOverride + False positive | Block | Yes | No |
| Notify + Block + AllowOverride + With justification | Block | Yes | Yes |
| Notify + Block + AllowOverride + False positive + Without justification | Block | Yes | No |
| Notify + Block + AllowOverride + False positive + With justification | Block | Yes | Yes |

## Policy tips on OneDrive sites and SharePoint sites

When a document on a OneDrive site or SharePoint site matches a rule in a DLP policy that uses policy tips, special icons appear on the document:

1. If the rule sends a notification about the file, the warning icon appears.
2. If the rule blocks access to the document, the blocked icon appears.

    

To take action on a document, select an item, choose **Information** in the upper-right corner of the page to open the details pane, then select **View policy tip**.

The policy tip lists the issues with the content. If the policy tips are configured with these options, you can choose **Resolve**, then **Override** the policy tip or **Report** a false positive.





DLP policies sync to sites and content is evaluated against them periodically and asynchronously, so there might be a short delay between the time you create the DLP policy and the time you begin to see policy tips. There might be a similar delay from when you resolve or override a policy tip to when the icon on the document on the site goes away.

### Default text for policy tips on sites

By default, policy tips display text similar to the following for an item on a site. The notification text is configured separately for each rule, so the text that displays differs depending on which rule is matched.

| If the DLP policy rule does this... | Then the default policy tip says this... |
| --- | --- |
| Sends a notification but doesn't allow override | This item conflicts with a policy in your organization. |
| Blocks access, sends a notification, and allows override | This item conflicts with a policy in your organization. If you don't resolve this conflict, access to this file might be blocked. |
| Blocks access and sends a notification | This item conflicts with a policy in your organization. Access to this item is blocked for everyone except its owner, last modifier, and the primary site admin. |

### Custom text for policy tips on sites

You can customize the text for policy tips separately from the email notification. Unlike custom text for email notifications (described in Custom email notifications), custom text for policy tips doesn't accept HTML or tokens. Instead, custom text for policy tips is plain text only with a 256-character limit.

## Policy tips in Outlook on the web and Outlook 2013 and later

When you compose a new email in Outlook on the web and Outlook 2013 and later, you see a policy tip if you add content that matches a rule in a DLP policy, and that rule uses policy tips. The policy tip appears at the top of the message, above the recipients, while the message is being composed.



Policy tips work whether the sensitive information appears in the message body, subject line, or even a message attachment as shown here.



If the policy tips are configured to allow override, you can choose **Show Details** &gt; **Override** &gt; enter a business justification or report a false positive &gt; **Override**.





When you add sensitive information to an email, there might be latency between when you add the sensitive information and when the policy tip appears. When emails are encrypted with Microsoft Purview Message Encryption and the policy used to detect them uses the detected encryption condition, policy tips don't appear.

### Policy tips in the Exchange admin center vs. the Microsoft Purview portal

Policy tips can work either with DLP policies and mail flow rules created in the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104), or with DLP policies, but not both. This limitation exists because these policies are stored in different locations, but policy tips can draw only from a single location.

If you configure policy tips in the Exchange admin center, any policy tips that you configure in the Purview portal don't appear to users in Outlook on the web and Outlook 2013 and later until you turn off the tips in the Exchange admin center. This behavior ensures that your current Exchange mail flow rules (also known as transport rules) continue to work until you choose to switch over to the Purview portal.

While policy tips can draw only from a single location, email notifications are always sent, even if you're using DLP policies in both the Purview portal and the Exchange admin center.

### Default text for policy tips in email

By default, policy tips display text similar to the following text for email.

| If the DLP policy rule does this... | Then the default policy tip says this... |
| --- | --- |
| Sends a notification but doesn't allow override | Your email conflicts with a policy in your organization. |
| Blocks access, sends a notification, and allows override | Your email conflicts with a policy in your organization. |
| Blocks access and sends a notification | Your email conflicts with a policy in your organization. |

## Policy tips in Excel, PowerPoint, and Word

When people work with sensitive content in the desktop versions of Excel, PowerPoint, and Word, policy tips notify them that the content conflicts with a DLP policy. This feature requires that:

- The Office document is stored on a OneDrive site or SharePoint site.
- The site is included in a DLP policy that's configured to use policy tips.

Office desktop programs automatically sync DLP policies directly from Microsoft 365, and then scan your documents to ensure that they don't conflict with your DLP policies.

Depending on how you configure the policy tips in the DLP policy, people can choose to ignore the policy tip, override the policy with or without a business justification, or report a false positive.

Policy tips appear on the Message Bar.



Policy tips also appear in the Backstage view (on the **File** tab).



If you configure policy tips in the DLP policy with these options, you can choose **Resolve** to **Override** a policy tip or **Report** a false positive.



In each of these Office desktop programs, people can choose to turn off policy tips. If turned off, policy tips that are simple notifications don't appear on the Message Bar or Backstage view (on the **File** tab). However, policy tips about blocking and overriding still appear, and the user still receives the email notification. In addition, turning off policy tips doesn't exempt the document from any DLP policies that you applied to it.

### Default text for policy tips in Excel 2016, PowerPoint 2016, and Word 2016

By default, policy tips display text similar to the following text on the Message Bar and Backstage view of an open document. You configure the notification text separately for each rule, so the text that displays differs depending on which rule is matched.

| If the DLP policy rule does this... | Then the default policy tip says this... |
| --- | --- |
| Sends a notification but doesn't allow override | This file conflicts with a policy in your organization. Go to the **File** menu for more information. |
| Blocks access, sends a notification, and allows override | This file conflicts with a policy in your organization. If you don't resolve this conflict, access to this file might be blocked. Go to the **File** menu for more information. |
| Blocks access and sends a notification | This file conflicts with a policy in your organization. If you don't resolve this conflict, access to this file might be blocked. Go to the **File** menu for more information. |

### Custom text for policy tips in Excel, PowerPoint, and Word

You can customize the text for policy tips separately from the email notification. Unlike custom text for email notifications (described in Custom email notifications), custom text for policy tips doesn't accept HTML or tokens. Instead, custom text for policy tips is plain text only with a 256-character limit.
