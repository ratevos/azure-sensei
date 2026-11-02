# Learn about DLP file quarantine for SharePoint and OneDrive

> Source: https://learn.microsoft.com/en-us/purview/dlp-spo-odb-quarantine-learn  
> Microsoft doc last updated: 2026-03-24


Note

The features described in this article are in preview. Organizations sometimes need to go beyond blocking access to sensitive files. When a file contains highly sensitive content that shouldn't exist in a particular SharePoint or OneDrive location, blocking access alone might not be enough — the file itself needs to be removed from the location entirely. Data loss prevention (DLP) file quarantine for SharePoint and OneDrive gives administrators the ability to automatically move files that match a DLP policy rule to an admin-controlled quarantine location.

## What is file quarantine?

File quarantine is a DLP policy action for SharePoint and OneDrive locations. When you configure a DLP policy with the quarantine action, files that match the policy rule are:

- Removed from the original SharePoint or OneDrive location.
- Moved to an admin-defined quarantine site in SharePoint.
- Replaced at the original location with a tombstone text file that contains an admin-configured message.

File quarantine is the most restrictive DLP action available for SharePoint and OneDrive. It removes access from everyone, including the file owner.

## When to use file quarantine

Use file quarantine when your organization needs to:

- **Isolate highly sensitive content** — For example, a file containing confidential business data, such as revenue numbers for an unannounced project, is stored in a SharePoint location where it shouldn't be. The file needs to be removed from that location and placed somewhere that only authorized administrators can access.
- **Remove access from the file owner** — In some cases, the file owner shouldn't retain access to the content. For example, the file was placed in an insecure location and the owner needs to work with an administrator to find a more secure way to store and share it.
- **Provide stronger protection than blocking alone** — Blocking prevents sharing but leaves the file in place. Quarantine removes the file entirely from the original location.

## How file quarantine works

When a file in a SharePoint or OneDrive location matches a DLP policy rule that has the quarantine action configured, the following sequence occurs:

1. **Permission removal** — All existing permissions and sharing links on the file are removed.
2. **File move** — A system account moves the file from the original location to the configured admin quarantine site. The folder structure of the original location is preserved in the quarantine site.
3. **Tombstone file creation** — A text (.txt) file with the same name as the original file replaces it at the source location. The tombstone file displays an admin-configured message and includes the relative path of the quarantined file. The full quarantine folder path isn't disclosed to the file owner.
4. **Audit and alerting** — An audit record is created that includes the quarantine file location. A DLP rule match event appears in Activity Explorer, and DLP alerts include the quarantine file location, the file owner, and the original file path.

### File identity

Each file in SharePoint and OneDrive is uniquely identified by its doc ID, not by its file name. DLP uses the doc ID to track files through the quarantine and restore process.

### Quarantine site exclusion

Once you designate a SharePoint site as the quarantine location, the contents of that site are automatically excluded from DLP rule evaluation. You don't need to manually add the quarantine site to an exclusion list. This automatic exclusion prevents conflicts where a quarantined file could match another DLP rule and create circular enforcement behavior.

### Files eligible for quarantine

The quarantine action only applies to files that are created or modified after the policy with the quarantine action is turned on. Files that existed before the policy was activated aren't evaluated for the quarantine action. This design prevents a situation where a broadly scoped policy accidentally quarantines a large number of existing files, which would be difficult to reverse because file restore is a manual process.

Important

This behavior is specific to the quarantine action. Other DLP actions, such as block, apply to all files in scope, regardless of when they were created. If your organization uses on-demand classification, files that are scanned and classified by an on-demand scan can trigger the quarantine action if the classification result matches a DLP policy rule for the first time.

Note

The quarantine action is not available as an on-demand classification action. On-demand classification only scans and classifies files — it doesn't take enforcement actions.

### Supported file types

File quarantine supports all file types that DLP supports for SharePoint and OneDrive locations.

## Tombstone files

When a file is quarantined, a tombstone text file replaces it at the original location. The tombstone file:

- Uses the original file's name with a `.txt` extension.
- Displays an admin-configured message. Administrators configure this message in DLP settings. For example, the message might instruct the file owner to contact a specific email address for assistance.
- Includes the relative path of the quarantined file within the quarantine site. The full quarantine folder path isn't provided, because the quarantine location is a confidential admin-controlled site.

The file owner can view the tombstone file to understand why their file was removed and who to contact.

## Manual file restore

There's no automated file restore for quarantined files. All file restore is a manual process. Administrators decide when and whether to restore a quarantined file.

Admins might restore files when:

- The sensitive content is determined to be harmless in context.
- The file usage is approved for valid business reasons.
- The policy match is a false positive.

To restore a quarantined file:

1. Locate the quarantined file in the quarantine site.
2. Identify the original file path by using audit logs.
3. Move the file from the quarantine site back to the original location. The quarantine site admin must have access to the original location.
4. Delete the tombstone file from the original location.

### Post-restore behavior

After a file is restored:

- **Original sharing permissions aren't restored.** The file owner or admin must reconfigure sharing permissions.
- **Only the latest file version is restored.** Previous versions aren't preserved through the quarantine and restore process.
- **The same DLP rule won't re-quarantine the restored file**, even if the file is modified or the policy rule is updated. This behavior is intentional to prevent quarantine loops. Other DLP rules continue to apply normally to the restored file.

## Known limitations

- **No automated restore** — All file restore is manual. There's no restore action available in the Microsoft Purview portal.
- **Sharing permissions not preserved** — Original sharing permissions and links aren't retained through the quarantine and restore cycle.
- A maximum of **200,000 items per tenant within a 24-hour period** may be processed for quarantine. Items exceeding this limit may be processed at a later time.
- File quarantine may not be completed for files with file path lengths greater than **350 characters**. In such cases, the tombstone file will not be created, resulting in the quarantine action not being applied.

## Relationship to other quarantine features

DLP file quarantine for SharePoint and OneDrive is separate from these related features:

- **Endpoint DLP auto-quarantine** — Applies only to files on Windows and macOS devices. It moves files to a local quarantine folder on the device. SharePoint and OneDrive file quarantine operates on cloud-hosted files.
- **Microsoft Defender for Cloud Apps file quarantine** — A similar quarantine capability that exists in Microsoft Defender for Cloud Apps (MDA). DLP file quarantine for SharePoint and OneDrive is designed for organizations that want to manage quarantine directly from Microsoft Purview.
