# Organizational messages in Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/organizational-messages-microsoft-365  
> Microsoft doc last updated: 03/13/2026


By using organizational messages in the Microsoft 365 admin center, you can connect with your organization through customized, in-product messages. Use organizational messages to streamline communication with users across Microsoft products. These messages enhance in-product experiences and support remote and hybrid work scenarios by sharing:

- Educational content.
- Information about Microsoft 365 service or license availability.
- Updates on organizational activities.

## Organizational messages capabilities

You can centrally manage organizational messages in the Microsoft 365 admin center. In the Microsoft 365 admin center, you can perform the following actions from a single, central location:

- Create messages from scratch.
- Use or edit pre-made template messages from Microsoft.
- Send messages to Windows 11 and Microsoft 365 app locations. For example, Windows Spotlight, Windows Notification Center, Windows Taskbar, and Microsoft Teams notifications.
- Save draft messages.
- Reject or Approve customized messages.
- Add images or icons to messages.
- Specify custom destination URLs.
- Configure delivery schedules and parameters for messages, including urgent messages configuration.
- Assign targeting via Microsoft Entra user groups and advanced targeting options, such as [Group Level Aggregate-based targeting](https://learn.microsoft.com/en-us/microsoft-365/admin/adoption/group-level-aggregates).
- Manage messages created in Microsoft 365 admin center and other portals, including [Usage reports](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-organizational-messages).
- Review message performance with time series data.

## New organizational messages capabilities in public preview: email messages and action segments

Organizational Messages now include two new capabilities available in public preview:

- **Email Messages**: Admins can now deliver pre‑made, template-based messages by email, extending existing surfaces like Windows Spotlight, the taskbar, Notification Center, and Microsoft Teams. For the initial public preview, eight pre-made email templates are available:

  - Two welcome messages for **Welcome to Copilot** and **Welcome to Copilot Chat**.
  - Six templates from the **Great M365 Copilot Journey** that highlight features and best practices to help drive Copilot onboarding and adoption.

    Email functionality during the public preview is limited to the eight provided English-only pre-made templates. The email templates aren't customizable. Message analytics aren't yet available for email.

- **Action Segments**: Admins can now target organizational messages based on usage behaviors. For the public preview, two predefined action segments are available for Copilot usage:

  - Inactive Copilot users: all users with a Microsoft 365 Copilot license that have not used Copilot in the prior 28 days.

  - Inactive Copilot users in Teams: all users with a Microsoft 365 Copilot license that have not used Copilot in Teams in the prior 30 days.

    You can't use **Action Segments** together with email messages during the public preview. **Action Segments** are available for the existing surfaces of Windows Spotlight, Taskbar, Notification Center, and Microsoft Teams notifications.

As we roll out the public preview for these features, we're excited to see how these features enhance communication and help drive Copilot adoption within your organization. We're committed to continuously improving these capabilities based on your feedback and usage.

## Requirements

Before working with organizational messages, make sure the following requirements are met:

- **Tenant policies** - To use organizational messages, configure the appropriate tenant policies. For more information on what policies are required, see the [Set tenant policies](#set-tenant-policies) section in this article.

- **Authors** - Assign the [Organizational Messages Writer](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#organizational-messages-writer) role in the Microsoft 365 admin center to anyone in your organization who wants to create messages.

- **Approvers** - Assign the [Organizational Messages Approver](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#organizational-messages-approver) admin role in the Microsoft 365 admin center to anyone in your organization who is a designated responsible party for approving customized messages.

- **Message recipients** - Recipients must have access to the Microsoft products the messages are configured for delivery. However, end users aren't required to have any Microsoft Entra roles to receive organizational messages. For example, any message configured to be delivered to a Windows channel, like Windows Spotlight, requires that recipients use Windows 11 Enterprise.

- **Devices** - Only Microsoft Entra ID joined devices are supported. Microsoft Entra (AD) hybrid joined devices aren't supported.

- **Firewall** - To ensure users can communicate with organizational messages, open the following endpoints:

  - `fd.api.orgmsg.microsoft.com`
  - `ris.prod.api.personalization.ideas.microsoft.com`

### Organizational messages advanced features requirements

Advanced features are experiences in organizational messages that are restricted to certain tenants. The currently available advanced features for organizational messages are:

- Fully customized message creation.
- Advanced targeting by group level aggregates, including Department, Location, Company, and Usage.

Admins and users can access these advanced features for organizational messages when the tenant has at least one of the following licenses:

- Microsoft 365 E3 or Microsoft 365 E5 license.
- Office 365 E3 or Office 365 E5 license.
- Windows Enterprise E3 or E5 license.

## Organizational messages experiences in the Microsoft 365 admin center

Familiarize yourself with these three experiences within the organizational messages centralized experience:

- **Manage messages** - A centralized workspace where you and your team can view and manage organizational messages created across supported portals. This area includes usage reports and access to the Copilot advanced deployment guide within the Microsoft 365 admin center. From **Manage messages**, your team can perform the following actions on messages:

  - Filter based on message status, location, objective, or message name.
  - Review existing message details such as language and targeting.
  - Understand aggregate performance data per message.
  - Cancel, delete, approve, and copy messages.
  - Run approval workflows.

- **Create a message** - A guided creation experience where authors can write fully customized or template-based messages.

- **Review activity** - A reporting view that enables administrators to monitor delivery and performance metrics for organizational messages, including messages that are currently being delivered or were delivered in the past.

### Access organizational messages experiences

To access the organizational messages experiences, you need the [Organizational Messages Writer](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#organizational-messages-writer) Microsoft Entra role. After you get that role, you can access the organizational messages centralized experience in the Microsoft 365 admin center by following these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.

1. Under **Reports**, select [**Organizational messages**](https://admin.cloud.microsoft/?#/organizationalmessages).

1. In the **Organizational messages** page, you can access the three experiences:

    - **Manage messages**.
    - **Create a message**.
    - **Review activity**.

### Create a new message

If you have the [Organizational Messages Writer](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#organizational-messages-writer) Microsoft Entra role, you can create a new organizational message. To create a new message, follow these steps:

1. If you're not at the **Organizational messages** page of the Microsoft 365 admin center, follow the steps in [Access organizational messages experiences](#access-organizational-messages-experiences) to get there.

1. Under the **Top actions** section of the **Organizational messages** page, select **Create a message**.

1. In the **Create a message** wizard, step through the wizard to create a new message. The wizard includes the following steps:

   - **Objective**: Select the nature or purpose of your new message.

   - **Location**: Indicate which in-product channel the message should be sent.

   - **Template**: Choose the format of the message. You can either use a pre-made message from Microsoft or create your own. For more information, see the section [Choose a pre-made message or custom message](#choose-a-pre-made-message-or-custom-message) in this article.

   - **Customize**: Add customization to the message including full text and custom URLs.

   - **Recipients**: Set the groups within your organization that should receive the message. You can also target by Companies, Departments, Locations, and Usage if the tenant is enabled for advanced features. For more information, see the section [Advanced targeting with Companies, Departments, Locations, and Usage](#advanced-targeting-with-companies-departments-locations-and-usage) in this article.

     > [!NOTE]
     >
     > The available targeting options depend on the message location you select. For example, Windows channels support recipient selection via Microsoft Entra groups and advanced targeting options based on Group Level Aggregates, while Teams notification channels only support recipient selection via Microsoft Entra groups.

   - **Schedule**: Configure the start date, end date, and frequency when the message is sent to users. If the user doesn't select the message when the message is displayed, or dismisses the message by selecting **X**, then the message reappears to the user based on the specified frequency. If the user does select the message, the message doesn't reappear again for a year as long as it isn't expired.

   - **Finish**: Review the message before scheduling or sending for approval by your organization's approvers.

Throughout the **Create a message** wizard, you can select **Save and close** to save the message as a draft and come back to it later. Once saved, a draft message has the status of **Draft**. You can see draft messages in the **Manage messages** section of the **Organizational messages** page. For information on how to continue editing a draft message, see the section [Modify a draft message](#modify-a-draft-message) in this article.

#### Choose a pre-made message or custom message

Two primary forms of message creation are enabled in this experience:

- **Pre-made messages** - Pre-made messages, also known as template-based messages, are a method of selecting and customizing content that Microsoft partially creates for general purpose use. For example, Microsoft might provide various generic messages that your team can pick. You can then customize the message by adding your logo and URL.

- **Create your own messages** - Create your own messages, also known as fully customized creation messages, is an open-ended format of entering in content for messages. This customization allows your team to make messages that include your company name or other specifics that are unique to your company, group, or team. For example, an author can select **Create your own** and type all of the words of the message themselves.

    > [!NOTE]
    >
    > The **Create your own** option is enabled if your organization has the required licenses as described in the [Organizational messages advanced features requirements](#organizational-messages-advanced-features-requirements) section in this article.

#### Advanced targeting with Companies, Departments, Locations, and Usage

If your tenant has the appropriate licenses as described in the [Organizational messages advanced features requirements](#organizational-messages-advanced-features-requirements) section, at the **Recipients** step and **Select message recipients** page of the **Create a message** wizard, the following options are available for a **Target audience** :

- **Companies**.
- **Departments**.
- **Locations**.
- **Usage**.

The advanced targeting options of **Companies**, **Departments**, **Locations**, and **Usage** in the **Recipients** step of the **Create a message** wizard are made possible by the group-level aggregates settings associated with **Adoption Score**. For more information, see [Group Level Aggregates in Adoption Score](https://learn.microsoft.com/en-us/microsoft-365/admin/adoption/group-level-aggregates).

To enable advanced targeting of organizational messages, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

1. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.

1. Under **Settings**, select **Org settings**.

1. In the **Org settings** page, make sure **Services** is selected and then select **Adoption Score**.

1. In the **Adoption Score** pane, make sure **Insight calculations and display** is selected.

1. Under **Group data filtering**, select **Turn on group-level insights** and then select **Save**.

1. Under **Group data filtering**, select **Manage group-level filtering**.

1. In the **Manage group-level filtering** pane, select the **Organizational attributes** checkbox, and then **Turn on selected filters**

### Modify a draft message

If you have the [Organizational Messages Writer](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#organizational-messages-writer) Microsoft Entra role, you can edit or complete a saved draft message. To edit or complete a draft message, follow these steps:

1. If you're not at the **Organizational messages** page of the Microsoft 365 admin center, follow the steps in [Access organizational messages experiences](#access-organizational-messages-experiences) to get there.

1. Under the **Top actions** section of the **Organizational messages** page, next to **Filter** select **Status**, and then select **Draft**.

1. Select the message you want to edit.

1. In the **Message details** pane, select **Modify**.

1. In the **Create a message** wizard, step through the wizard to edit or complete the draft message.

### Approve or reject a pending message

Selecting a pre-made message doesn't require any approval before the message can be delivered to end users. However, approvers must approve custom messages before the system delivers them to users. Approvers can't approve or reject a message that they created.

**Rejecting** a message marks the message state as **Rejected**. The author can review the message and resubmit it after making the requested changes. For more information, see the section [Withdraw a rejected message](#withdraw-a-rejected-message) in this article.

If approvers don't approve or reject a message by the set **End date** of the message, the system automatically rejects the message. This policy ensures the minimum duration of delivery of messages as expected by authors.

If you have the [Organizational Messages Approver](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#organizational-messages-approver) Microsoft Entra role, you can review messages that are in the **Pending approval** state. You can then either approve or reject the messages. To approve or reject a **Pending approval** message, follow these steps:

1. If you're not at the **Organizational messages** page of the Microsoft 365 admin center, follow the steps in [Access organizational messages experiences](#access-organizational-messages-experiences) to get there.

1. Under the **Top actions** section of the **Organizational messages** page, next to **Filter** select **Status** and then select **Pending approval**.

1. Select the message you want to review.

1. In the **Message details** pane, review the message details:

    - To approve the message, select **Approve**. You can also optionally add a comment before approving the message.
    - To reject the message, add a comment in the text field, and then select **Reject**. You must enter a comment before rejecting the message.

### Withdraw a rejected message

When approvers reject a message, the message state changes to **Rejected**. However, if you have the [Organizational Messages Writer](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#organizational-messages-writer) Microsoft Entra role, you can withdraw a rejected message. By withdrawing a rejected message, you can modify the message to address the approver's concerns before resubmitting it for approval. When you withdraw a rejected message, its status changes from **Rejected** to **Draft**. To withdraw a rejected message, follow these steps:

1. If you're not at the **Organizational messages** page of the Microsoft 365 admin center, follow the steps in [Access organizational messages experiences](#access-organizational-messages-experiences) to get there.

1. Under the **Top actions** section of the **Organizational messages** page, next to **Filter** select **Status** and then select **Rejected**.

1. Next to the rejected message that you want to withdraw, select the ellipses **⋮** menu, and then select **Withdraw**. The state of the rejected message changes to **Draft**.

1. Select the **Draft** message you just withdrew.

1. In the **Message details** pane, select **Modify**.

1. The **Create a message** wizard opens where you can edit the message. When you finish editing, resubmit the message for approval.

### Copy an existing organizational message

1. If you're not at the **Organizational messages** page of the Microsoft 365 admin center, follow the steps in [Access organizational messages experiences](#access-organizational-messages-experiences) to get there.

1. Under the **Manage messages** section of the **Organizational messages** page, next to the message that you want to copy, select the ellipses **⋮** menu, and then select **Copy**.

1. The **Create a message** wizard opens with elements from the previous message.

1. Step through the **Create a message** wizard and make any necessary edits.

> [!NOTE]
>
> - As long as the **Location** of the copied message remains the same, images from the copied message are automatically copied to the new message. However, you can override that image by uploading a new image.
>
> - Pre-made messages aren't available for all selections in the **Objective** step. However, all objectives have the **Create your own messages** format available for full customization authoring.

### Urgent delivery

For some time-sensitive communications, admins and other communicators might need to send a message quickly. Admins might need to quickly broadcast an event to some users so they can be informed. For example:

- An event is occurring on a corporate campus.
- A service outage begins.

To support communications in such events, organizational messages include an urgent delivery feature. The message creation experience for an urgent message is similar to the flow for creating other messages with these exceptions:

- The only locations available are Windows 11 Taskbar and Notifications area.
- Only Microsoft Entra group targeting is supported.
- At the *Schedule** step of the **Create a message** wizard, **Start date**, **End date**, and **Frequency** configurations aren't available since urgent messages are sent as soon as possible and only once.

To create an urgent message, follow these steps:

1. If you're not at the **Organizational messages** page of the Microsoft 365 admin center, follow the steps in [Access organizational messages experiences](#access-organizational-messages-experiences) to get there.

1. Under the **Top actions** section of the **Organizational messages** page, select **Send urgent message**.

    

1. In the **Create a message** wizard, step through the wizard to create a new urgent message.

### Delayed delivery of organizational messages

Organizational messages deliver messages to end users within the time windows that admins configure through the Microsoft 365 admin center. However, system or user device conditions might prevent messages from being delivered as expected. For example, urgent messages don't reach devices that are disconnected from the internet. In these situations, Microsoft 365 continues trying to deliver messages when possible. If a device is offline while an urgent message is being delivered, the system caches the message for up to 24 hours. Windows attempts to show the message to the user again once the device is back online.

> [!NOTE]
>
> To support tenant-based targeting, the organizational messages system might take up to 24 to 48 hours to initialize for tenants where a message wasn't scheduled in the past 30 days.

## Review activity

In the **Organizational messages** page of the Microsoft 365 admin center, the table under the **Manage messages** section includes basic aggregate insights data for your messages. For example:

- **Total messages seen**.
- **Total clicks**.
- **Clickthrough rate**.

However, the **Review activity** experience provides additional advanced insights. In the **Review activity** experience, you can review insights data for your messages by using the following capabilities:

- Filtering on time range, status, and other aspects.
- Graphing of selected date range.
- Data export to CSV.

To access the **Review activity** experience, follow these steps:

1. If you're not at the **Organizational messages** page of the Microsoft 365 admin center, follow the steps in [Access organizational messages experiences](#access-organizational-messages-experiences) to get there.

1. Under the **Top actions** section of the **Organizational messages** page, select **Review activity**.

1. The **Review activity** page opens where you can review insights data for your messages including:

    - Three time-series data charts showing daily changes in the total **Messages seen**. Total **Messages seen** is also known as impressions.
    - Total **Clicks**.
    - **Clickthrough rate** for your messages.

### Export organizational message performance data

You can export message data to a CSV file if you want to work with your tenant's message performance data. To export message performance data to CSV, follow these steps:

1. If you're not already signed in to the Microsoft 365 admin center and navigated to the **Review activity** page, follow the steps in [Review activity](#review-activity) to get there.

1. In the **Review message activity** page, next to **Filters:**, set the filters as desired. For example, set the time range for the data you're interested in retrieving.

1. Select **Export to CSV** and then save the CSV file locally.

## Set tenant policies

Set tenant policies only if you need to deliver messages to Windows surfaces such as Windows Spotlight, Windows Notification Center, and Windows Taskbar. You don't need to set tenant policies for sending messages to Teams Teaching notifications or to Email.

Certain policies can block the delivery of organizational messages. For example, policies in [Microsoft Intune](https://intune.microsoft.com). This section describes both how to set policies to allow organizational messages and how to verify that there are no policies that block organizational messages.

### Create a policy that allows organizational messages in Microsoft Intune

To enable organizational messages through a policy in Microsoft Intune, follow these steps:

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com/).

1. In the **Home** screen, select **Devices** in the left pane.

1. In the **Devices | Overview** screen, expand **Manage devices**, and then select **Configuration**.

1. In the **Devices | Configuration** screen:

   1. At the top, make sure **Policies** is selected.

   1. Select the **+ Create** drop down menu and then select **New Policy**.

1. In the **Create a profile** pane:

   1. Under **Platform**, select **Windows 10 and later**.

   1. Under **Profile type**, select **Settings catalog**.

   1. Select **Create**.

1. The **Create profile** wizard opens. In the **Basics** page, enter a name and description for the new policy, such as **Organizational Messages Policy**, and then select **Next**.

1. In the **Configuration settings** page, select **+ Add settings**.

1. In the **Settings picker** pane:

   1. Under **Browse by category**, select **Experience** from the list of categories.

   1. When the **Settings name** section appears:

      1. Select the following two settings:

        - **Enable delivery of organizational messages (User)**
        - **Disable Cloud Optimized Content**.

      1. Expand **Allow Windows Spotlight (User)** and then select the following settings under **Allow Windows Spotlight (User)**:

         - **Allow Windows Spotlight on Action Center (User)**.
         - **Allow Windows Tips**.
         - **Configure Windows Spotlight on Lock Screen (User)**.

   1. Close the **Settings picker** pane by selecting the **X** in the top right corner.

1. In the **Configuration settings** page:

   1. Set all of the following settings to **Allow**:

      - **Enable delivery of organizational messages (User)**.
      - **Allow Windows Spotlight (User)**.
      - **Allow Windows Spotlight on Action Center (User)**.
      - **Allow Windows Tips**.

   1. Make sure **Disable Cloud Optimized Content** is set to **Disabled**.

   1. Make sure **Configure Windows Spotlight on Lock Screen (User)** is set to one of the following settings:

      - **Windows spotlight enabled.**
      - **Windows spotlight is always enabled, the user cannot disable it**.

   1. Select **Next**.

1. In the **Scope tags** page, select the **Next** button.

    > [!NOTE]
    >
    > **Scope tags** are optional. If you need to specify a custom scope tag, add it on this page. For more information about scope tags, see [Use role-based access control and scope tags for distributed IT](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/scope-tags).

1. In the **Assignments** page, select the groups that should be targeted by this policy and then select **Next**. Include any users or devices that might receive organizational messages.

1. In the **Review + create** page, review the policy settings to make sure they're correct, and then select **Create**.

>[!NOTE]
>
> If you recently onboarded your tenant to Microsoft Entra ID, it can take 36 to 64 hours before you can use the organizational messages features.

### Verify no device restriction policies block organizational messages in Microsoft Intune

After creating a policy in Microsoft Intune to allow organizational messages, verify that no device restriction policies block any of the following settings:

- **Windows Spotlight**.
- **Windows Spotlight on lock screen**.
- **Windows Tips**.
- **Windows Spotlight in action center**.
- **Windows Spotlight personalization**.

To check if any policies block these settings, follow these steps:

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com/).

1. In the **Home** screen, select **Devices** in the left pane.

1. In the **Devices | Overview** screen, expand **Manage devices**, and then select **Configuration**.

1. In the **Devices | Configuration** screen, select **Add filters**.

1. In the **Add filters** dropdown menu, select **Policy type**, select **Device restrictions**, and then select **Apply**.

1. All policies of the type **Device restrictions** appear under **Policy name**.

1. Select each of the **Device restrictions** policies. For each policy, make sure that **Windows Spotlight** isn't listed under **Configuration settings**.

1. If **Windows Spotlight** appears under **Configuration settings**, expand **Windows Spotlight** and ensure that none of the following settings are set to **Block**:

   - **Windows Spotlight**.
   - **Windows Spotlight on lock screen**.
   - **Windows Tips**.
   - **Windows Spotlight in action center**.
   - **Windows Spotlight personalization**.

1. If any of these settings are set to **Block**, select **Edit** next to **Configuration settings**.

1. In the **Device restrictions** page, expand **Windows Spotlight**. You might need to scroll down the list to find **Windows Spotlight**.

1. Change any of the following policies from **Block** to **Not configured**:

   - **Windows Spotlight**.
   - **Windows Spotlight on lock screen**.
   - **Windows Tips**.
   - **Windows Spotlight in action center**.
   - **Windows Spotlight personalization**.

1. Select **Review + save** and then select **Save**.

## Frequently asked questions about organizational messages (FAQ)

For frequently asked questions about organizational messages, see [Organizational Messages in Microsoft 365 FAQ](organizational-messages-microsoft-365-faq.yml).
