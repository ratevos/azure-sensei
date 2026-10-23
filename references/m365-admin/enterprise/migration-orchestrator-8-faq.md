# Migration orchestrator FAQ

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/migration-orchestrator-8-faq  
> Microsoft doc last updated: 01/26/2026


> [!IMPORTANT]
> Tenant-to-tenant migration is currently available in preview. Features and availability may change before general availability (GA).

## Cancellation

If you start a migration and realize that you need to cancel it, you need to cancel it before the CompleteAfterDate passes. If the CompleteAfterDate is past and the mailbox is cutover, then the user data migration completes automatically with Teams chats and meetings. Once the migration completes, it's possible to move the user data back to the source.

## Moving user data back

Migration of user data back to the source tenant through the orchestrated system isn't supported in preview. If you need to move a user’s email and OneDrive back to the source tenant after completing a successful migration to the target tenant, use the standalone mailbox and OneDrive migration options. Teams meetings aren't recreated after this migration and need to be recreated manually. The original Teams chat message modifications are also not touched. If data migration for users back to the original source is a required scenario, use the Generally Available version of cross-tenant migration of mailboxes and OneDrives.

## General migration

[Learn more](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-mailbox-migration#frequently-asked-questions) about Exchange Mailbox Migration.

### Do you have any recommendations for batches?

To ensure a smooth migration process, we recommend limiting the number of mailboxes per batch to 2,000 and submitting batches at least two weeks before the cut-over date. This limit doesn't affect end users during synchronization. For guidance on migrating quantities exceeding 50,000 mailboxes, contact your account team for assistance.

If you're migrating OneDrive, there's a 4,000 limit between SharePoint and OneDrive sites that can be moved and queued to move at one time.

### Can I perform a cross-cloud tenant-to-tenant migration?

Cross-cloud tenant-to-tenant migration isn't supported. An example scenario would be moving from Office 365 Worldwide to Office 365 Government Cloud.

### Are voicemails migrated cross-tenant?

- Yes, voicemails are migrated cross-tenant.
- Received voicemails in email as attachments are available in the target mailbox.
- Received voicemails are available in Teams if you call voicemail and listen to saved messages (Voicemails received in the source tenant are available as saved messages).
- Received voicemails aren't available in the Teams client UI in target post-migration.
- The voicemail greeting also migrates to the target.

For more troubleshooting guidance, see [Resolve orchestrated migration errors](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/admin/orchestrated-migration/resolve-orchestrated-migration-errors).
