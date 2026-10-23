# About shared mailboxes in Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/email/about-shared-mailboxes  
> Microsoft doc last updated: 03/13/2026


This article explains what shared mailboxes are, when to use them, licensing considerations, limitations, and common troubleshooting scenarios.

Use shared mailboxes when multiple people need access to the same mailbox, such as for:

- Company information addresses.
- Support email addresses.
- Reception or front-desk mailboxes.
- Any other mailboxes shared by multiple people.

Users with the appropriate permissions can send as or send on behalf of a shared mailbox. Shared mailboxes are useful for help and support mailboxes because users can send emails from **Contoso Support** or **Building 7 Reception**.

## Before creating a shared mailbox

Know the following items before [creating a shared mailbox](https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-a-shared-mailbox):

### Licensing and mailbox storage limits

- **Licensing**: A shared mailbox can store up to 50 GB of data without assigning a license to it.

    > [!WARNING]
    >
    > When a shared mailbox reaches the mailbox storage limit, you can receive email for some time, but you can't send new email. After some time, the shared mailbox stops receiving email and senders to the mailbox receive a non-delivery receipt. For more information, see [Exchange Online Limits](https://learn.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits#StorageLimits).

- **Scenarios requiring additional licenses**: The following scenarios require additional licenses:

  - **Shared mailbox with more than 50 GB**: Shared mailboxes are limited to 50 GB. To increase the size limit to 100 GB, the shared mailbox must be assigned an **Exchange Online Plan 2** license.

  - **Shared mailbox with in-place archiving**: To increase the size of the archive mailbox, an **Exchange Online Plan 2** license or an **Exchange Online Plan 1** license with an **Exchange Online Archiving** add-on license is required. Assigning either one of these licenses also lets you enable auto-expanding archiving for additional archive storage capacity.

  - **Shared mailbox placed on litigation hold**: To place a shared mailbox on litigation hold, the shared mailbox must have an **Exchange Online Plan 2** license or an **Exchange Online Plan 1** license with an **Exchange Online Archiving** add-on license.

  - **Advanced features**: To apply advanced features such as Microsoft Defender for Office 365, Microsoft Purview eDiscovery (Premium), or retention policies, licenses might be required. For more information, see [Microsoft 365 licensing guidance for security & compliance](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance).

    For step-by-step instructions on how to assign licenses, see [Assign licenses to users](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users).

- **Subscription requirements**: To create a shared mailbox, you need to subscribe to a Microsoft 365 for business plan that includes email (the Exchange Online service). The Microsoft 365 Apps for business subscription doesn't include email. Microsoft 365 Business Standard does include email.

- **License requirements to access a shared mailbox**: To access a shared mailbox, a user must have a licensed Exchange Online mailbox, but the shared mailbox doesn't require a separate license. Delegate access must be done through the delegate's own mailbox.

### Access and permissions

- **User permissions**:  To use the shared mailbox, assign permissions to users through a membership. Only people inside your organization can use a shared mailbox.

- **External users**: You can't give people outside your business, such as people with a Gmail account, access to your shared mailbox. If you want to give people outside your business access to your shared mailbox, consider creating a group for Outlook instead. To learn more, see [Create a Microsoft 365 group in the admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/create-groups).

- **Signing in**: A shared mailbox isn't intended for direct sign-in by using its associated user account. Always block sign-in for the shared mailbox account and keep it blocked.

- **Admin roles**: Users with Exchange admin roles can create shared mailboxes.

- **Shared mailbox password**: Every shared mailbox has a corresponding user account with a system-generated password that isn't known or intended for use. Don't use the account to sign in to the shared mailbox.

### Client support and usage

- **Use with Outlook for Android and Outlook for iOS App**: In addition to using Outlook on the web from your browser to access shared mailboxes, you can also use the Outlook for iOS app or the Outlook for Android app. To learn more, see [Add a shared mailbox to Outlook mobile](https://support.microsoft.com/office/f866242c-81b2-472e-8776-6c49c5473c9f). Another option is to create a group for your shared mailbox. To learn more, see [Compare Groups](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups).

- **Too many users**: A shared mailbox supports a maximum of 25 users. If too many users access the mailbox at the same time, they might experience connection failures or duplicated messages. If you need more users, use a Microsoft 365 group instead.

- **Message deletion**: You can't prevent users from deleting messages in a shared mailbox. To restrict deletion, [create a Microsoft 365 group](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/create-groups) instead of a shared mailbox. A Microsoft 365 group in Outlook provides shared access to email and a calendar, but it uses a different model than a shared mailbox. For a comparison of the two, see [Compare groups](https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups). To learn more about groups, see [Learn about Microsoft 365 groups](https://support.microsoft.com/office/b565caa1-5c40-40ef-9915-60fdb2d97fa2).

### Security and compliance considerations

- **Encryption**: Email sent from a shared mailbox can't be encrypted because the mailbox doesn't have its own security context (username and password). As a result, it can't be assigned an encryption key. If members encrypt messages using their own keys, other members might not be able to read those messages.

- **Litigation hold**: Shared mailboxes require additional licensing to support litigation hold. For more information, see [Licensing and mailbox storage limits](#licensing-and-mailbox-storage-limits).

### Mailbox management

- **Mailbox conversion**: You can convert user mailboxes to shared mailboxes. See [Convert a user mailbox to a shared mailbox](https://learn.microsoft.com/en-us/microsoft-365/admin/email/convert-user-mailbox-to-shared-mailbox).

- **Mailboxes created before July 2018**: All unlicensed shared mailboxes created before July 2018 have a size of 100 GB. For more information, see [Correcting Shared Mailbox provisioning and sizing](https://techcommunity.microsoft.com/t5/exchange-team-blog/correcting-shared-mailbox-provisioning-and-sizing/ba-p/607991).

## Troubleshoot shared mailbox problems

This section describes common problems you might encounter when creating or using shared mailboxes and how to resolve them.

### Error when creating shared mailboxes

If you're trying to give the shared mailbox a name that's already in use, you see the following error message:

**The proxy address "smtp:<shared mailbox name\>" is already being used by the proxy addresses or LegacyExchangeDN of "\<name>". Please choose another proxy address**

For example, to create two shared mailboxes named `info@domain1` and `info@domain2`, perform one of the following two tasks:

- Use Exchange Online PowerShell. For instructions, see [Create Shared Mailboxes with Same Alias at Different Domains](https://blog.quadrotech-it.com/blog/create-shared-mailboxes-with-same-alias-at-different-domains-in-office-365/).

- Name the second shared mailbox something different from the start to get around the error. Then in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), rename the shared mailbox to what you want it to be.

### Send permissions error when you use a shared mailbox

If you create a shared mailbox and then try to send a message from it, you might get the following error message:

**This message could not be sent. You do not have the permission to send the message on behalf of the specified user.**

This message appears when Microsoft 365 is experiencing a replication latency problem. It goes away in about an hour, when the information about your new shared mailbox (or added user) is replicated across all data centers. Wait an hour and then try again to send a message.

## Related content

- [Create a shared mailbox](https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-a-shared-mailbox).
- [Configure a shared mailbox](https://learn.microsoft.com/en-us/microsoft-365/admin/email/configure-a-shared-mailbox).
- [Convert a user mailbox to a shared mailbox](https://learn.microsoft.com/en-us/microsoft-365/admin/email/convert-user-mailbox-to-shared-mailbox).
