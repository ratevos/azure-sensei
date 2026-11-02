# Data loss prevention and Microsoft Teams

> Source: https://learn.microsoft.com/en-us/purview/dlp-microsoft-teams  
> Microsoft doc last updated: 2026-08-26


If your organization has Microsoft Purview Data Loss Prevention (DLP), you can define policies that help prevent people from sharing sensitive information in a Microsoft Teams channel or chat session. Here are some example scenarios:

- **Protecting sensitive information in messages**. Suppose that someone attempts to share sensitive information in a Teams chat or channel with guests (external users). If you have a DLP policy defined in your tenant to prevent this, messages with sensitive information that are sent to external users are deleted. However, your tenant must be the initiator of the chat or the thread. This happens automatically, and within seconds, according to how your DLP policy is configured.
- **Protecting sensitive information in documents**. Suppose that someone attempts to share a document with guests in a Microsoft Teams channel or chat, and the document contains sensitive information. If you have a DLP policy defined to prevent this, the document won't open for those users. Your DLP policy must include SharePoint and OneDrive in order for protection to be enforced. This is an example of DLP for SharePoint that shows up in Microsoft Teams, and therefore requires that users are licensed for Office 365 DLP (included in Office 365 E3), but doesn't require that users be licensed for Office 365 Advanced Compliance.
- **Protecting communications in Teams Shared Channels**. Shared channels are built on Microsoft Entra B2B direct connect, so each participant remains signed in to their own (home) tenant and doesn't get an identity object in the host tenant. Because DLP evaluation is driven by the sender's identity, each user's messages are evaluated against the DLP policies of their own tenant, regardless of which tenant owns the shared channel. For example, let's say there's a shared channel owned by Team A of Contoso, where Contoso has a DLP policy P1 and Fabrikam has a DLP policy P2. There are three ways to share the channel:

    - **Share with member**: You invite User1 from Contoso to join the shared channel without making them a member of Team A. User1's messages are evaluated against Contoso's DLP policies (P1), the same policies that apply to User1 elsewhere in Contoso.
    - **Share with team (internally)**: You share the channel with another team within Contoso, Team B. Messages from Team A and Team B users are evaluated against Contoso's DLP policies. If Team A and Team B are scoped to different policies, each user is still evaluated against the policies that target them.
    - **Share with team (cross tenant)**: You share the channel with a team, Team F, in Fabrikam. Contoso's DLP policies (P1) apply to messages sent by Team A (Contoso) users. Fabrikam's DLP policies (P2) apply to messages sent by Team F (Fabrikam) users. Contoso can't enforce its DLP policies on Fabrikam users' messages, and vice versa.
- **Protecting communications when chatting with external users in Microsoft Teams**.

People from different Microsoft 365 organizations who use the *external* access feature can participate in the same chat session. DLP policy enforcement in these cross-tenant conversations is based on the hosting tenant, which is the tenant that initiated the chat or thread.

For example, suppose UserA, UserB, and UserC are from Contoso, while UserX, UserY, and UserZ are from Fabrikam, and they participate in the same Teams group chat. Contoso's DLP policies apply to messages sent by Contoso users only when Contoso is the hosting tenant, such as when UserA, UserB, or UserC created the chat. In this case, Fabrikam's DLP policies aren't evaluated or enforced on messages sent by UserX, UserY, or UserZ, and Contoso's DLP policies aren't applied to those Fabrikam users.

Therefore, in a cross-tenant conversation, a user's home-tenant DLP policies don't automatically follow the user into a conversation hosted by another tenant.

For more information on using Microsoft Teams to chat with people external to your organization, see [Manage external meetings and chat with people and organizations using Microsoft identities](https://learn.microsoft.com/en-us/en-us/microsoftteams/trusted-organizations-external-meetings-chat)

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## DLP Licensing for Microsoft Teams

[Data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) capabilities include Microsoft Teams chat and channel messages, **including private channel messages** for:

- Office 365 E5/A5/G5
- Microsoft 365 E5/A5/G5
- Microsoft 365 E5/A5/G5 Information Protection and Governance
- Microsoft 365 E5/A5/G5/F5 Compliance and F5 Security & Compliance

Office 365 and Microsoft 365 E3 include DLP protection for SharePoint, OneDrive, and Exchange. This also includes files that are shared through Teams because Teams uses SharePoint and OneDrive to share files.

Support for DLP protection in Teams Chat requires an E5 license.

Important

For information on licensing, see [Microsoft 365, Office 365, Enterprise Mobility + Security, and Windows 11 Subscriptions for Enterprises](https://aka.ms/M365EnterprisePlans).

## Scope of DLP protection

DLP protection is applied differently to Teams entities and is described in the table that follows.

| Policy scope | Teams Entities | DLP Protection |
| --- | --- | --- |
| Individual user accounts | 1:1/n chats | Yes |
| Individual user accounts | Standard, private and shared channel messages | No |
| Security groups/distribution group/non-mail-enabled security group | 1:1/n chats | Yes |
| Security groups/distribution group/non-mail enabled security group | Standard, private and shared channel messages | Yes |
| Microsoft 365 groups | 1:1/n chats | Yes |
| Microsoft 365 groups | Standard, private and shared channel messages | Yes |

## Policy tips help educate users

Similar to how DLP policy tips work in [Exchange, Outlook, SharePoint, OneDrive, and on Windows Devices](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp), policy tips in Teams appear when an action triggers with a DLP policy. Here's an example of a policy tip:



Here, the sender attempted to share a social security number in a Microsoft Teams channel. The **What can I do?** Link opens a dialog box that provides options for the sender to resolve the issue. Notice that the sender can opt to override the policy or notify an admin to review and resolve the issue.



You can choose to allow users in your organization to override a DLP policy. When you configure your DLP policies, you can use the default policy tips, or customize policy tips for your organization.

Returning to our example, when a sender has shares a social security number in a Teams channel, here's what the recipient sees:



DLP protections are applied to the actual messages in the chat or channel thread. Message information is also shown in the short preview in Activity notifications that are created from chat or channel message. When there's a match to a DLP policy, the corresponding preview is hidden, and a "Preview Unavailable" message is shown instead of the blocked preview. An Activity entry is also generated for the sender if the message sent matched a DLP policy. Flagged and blocked messages, activities are created stating "Your message has been blocked".

DLP for Microsoft Teams does not send user notification emails like DLP for Exchange, SharePoint, and OneDrive. Instead, users only receive message flags as notifications.

### To customize policy tips

To perform this task, you must be assigned a role that has permissions to edit DLP policies. To learn more, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt;**Data loss prevention** &gt; **Policies**.
2. Select a policy, and then choose **Edit policy** (the pencil icon).
3. Navigate through the tool until you come to the **Customize advanced DLP rules** screen.
4. Either create a new rule, or edit an existing rule for the policy.
5. Scroll down to **User notifications** and set the **Use notifications to inform your users and help educate them on the proper use of sensitive info** toggle to **On**.
6. Under **Microsoft 365 services**, select **Notify users in Office 365 service with a policy tip**.
7. Under **Policy tips**, select **Customize the policy tip text**.
8. Specify the text you want to use for the policy tip.
9. If the policy tip applies to user activities in Microsoft Exchange and you want a dialog box to display the tip before an email is sent, select **Show the policy tip as a dialog for the end user before send**.
10. Choose **Save** and then **Next**.
11. On the **Policy mode** page, check the box next to **Show policy tips while in simulation mode** if desired.
12. Choose **Next**, choose **Submit**, and then choose **Done**.

## Add Microsoft Teams as a location to existing DLP policies

To perform this task, you must be assigned a role that has permissions to edit DLP policies. To learn more, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions)

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Data loss prevention** &gt; **Policies**.
2. Select a policy, and then choose **Edit policy** (the pencil icon).
3. Navigate through the tool until you arrive at the **Choose locations to apply the policy** page.
4. Select **Teams chat and channel messages**.
5. Choose **Next** and work your way through to the end of the process.
6. Choose **Submit**.

Allow approximately one hour for your changes to work their way through your data center and sync to user accounts.

## Define a new DLP policy for Microsoft Teams

For information about how to create and implement a new DLP policy, see [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#create-and-deploy-data-loss-prevention-policies).

## Prevent external access to sensitive documents

You can ensure that documents are protected until DLP scans and marks them as safe to share by [marking new files as sensitive by default](https://learn.microsoft.com/en-us/en-us/sharepoint/sensitive-by-default).

### Recommended DLP policy structure

- **Conditions**
- **Content contains any of these sensitive information types**: [Select all that apply]
- **Content is shared from Microsoft 365** &gt; **with people outside my organization**
- **Actions**

    - **Add an action**
    - **Restrict access or encrypt the content in Microsoft 365 locations** &gt; **Block only people outside your organization**



- **Use notifications to inform your users and help educate them on the proper use of sensitive info** &gt; **Notify users in Office 365 with a policy tip**
- **Notify these people** [Select all that apply]
- **Policy tips** [Select all that apply]



Note

The sender address for incident reports is *no-reply@teams.mail.microsoft.com*.
