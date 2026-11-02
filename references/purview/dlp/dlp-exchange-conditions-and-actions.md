# Data loss prevention Exchange conditions and actions reference

> Source: https://learn.microsoft.com/en-us/purview/dlp-exchange-conditions-and-actions  
> Microsoft doc last updated: 2025-10-09


Conditions in Microsoft Purview Data Loss Prevention (DLP) policies identify sensitive items that the policy is applied to. Actions define what happens as a consequence of a condition being met.

- Conditions define what to include
- Actions define what happens as a consequence of condition being met

Most conditions have one property that supports one or more values. For example, if the DLP policy is being applied to Exchange emails, the **The sender is** condition requires the sender of the message. Some conditions have two properties. For example, the **A message header includes any of these words** condition requires one property to specify the message header field, and a second property to specify the text to look for in the header field. Some conditions or exceptions don't have any properties. For example, the **Attachment is password protected** condition simply looks for attachments in messages that are password protected.

Actions typically require additional properties. For example, when the DLP policy rule redirects a message, you need to specify where the message is redirected to.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Exchange conditions for DLP policies

The tables in the following sections describe the conditions and exceptions that are available in DLP.

- Senders
- Recipients
- Message subject or body
- Attachments
- Message headers
- Message properties

### Senders

If you use the sender address as a condition the actual field where the value is looked for varies depending on the sender address location configured. By default, DLP rules use the Header address as the sender address.



At the tenant level, you can configure a sender address location to be used across all rules, unless overridden by a single rule. To set tenant DLP policy configuration to evaluate the sender address from the Envelope across all rules, you can run the following command:

```PowerShell
Set-PolicyConfig -SenderAddressLocation Envelope
```

To configure the sender address location at a DLP rule level, the parameter is *SenderAddressLocation*. The available values are:

- **Header**: Only examine senders in the message headers (for example, the **From**, **Sender**, or **Reply-To** fields). This is the default value.
- **Envelope**: Only examine senders from the message envelope (the **MAIL FROM** value that was used in the SMTP transmission, which is typically stored in the **Return-Path** field).
- **Header or envelope** (`HeaderOrEnvelope`) Examine senders in the message header and the message envelope.

| Condition or Exception in DLP | Condition/Exception parameters in Security & Compliance PowerShell | Property type | Description |
| --- | --- | --- | --- |
| Sender is | Condition: *From* Exception: *ExceptIfFrom* | *Addresses* | Messages sent by the specified mailboxes, mail users, mail contacts. |
| The sender is a member of | Condition: *FromMemberOf* Exception: *ExceptIfFromMemberOf* | *Addresses* | Messages sent by a member of the specified distribution group whether assigned or dynamic, mail-enabled security group, or Microsoft 365 group whether assigned or dynamic. |
| Sender IP address is | Condition: *SenderIPRanges* Exception: *ExceptIfSenderIPRanges* | *IPAddressRanges* | Messages where the sender's IP address matches the specified IP address, or falls within the specified IP address range. |
| Sender address contains words | Condition: *FromAddressContainsWords* Exception: *ExceptIfFromAddressContainsWords* | *Words* | Messages that contain the specified words in the sender's email address. |
| Sender address matches patterns | Condition: *FromAddressMatchesPatterns* Exception: *ExceptIfFromAddressMatchesPatterns* | *Patterns* | Messages where the sender's email address contains text patterns that match the specified regular expressions. |
| Sender domain is | Condition: *SenderDomainIs* Exception: *ExceptIfSenderDomainIs* | *DomainName* | Messages where the domain of the sender's email address matches the specified value. If you need to find sender domains that *contain* the specified domain (for example, any subdomain of a domain), use **The sender address matches pattern** (*FromAddressMatchesPatterns*) condition and specify the domain by using the syntax: `'\.domain\.com$'`. |
| Sender scope | Condition: *FromScope* Exception: *ExceptIfFromScope* | *UserScopeFrom* | Messages sent by either internal or external senders. |
| The sender's specified properties include any of these words | Condition: *SenderADAttributeContainsWords* Exception: *ExceptIfSenderADAttributeContainsWords* | First property: *ADAttribute* Second property: *Words* | Messages where the specified Microsoft Entra ID attribute of the sender contains any of the specified words. |
| The sender's specified properties match these text patterns | Condition: *SenderADAttributeMatchesPatterns* Exception: *ExceptIfSenderADAttributeMatchesPatterns* | First property: *ADAttribute* Second property: *Patterns* | Messages where the specified Microsoft Entra ID attribute of the sender contains text patterns that match the specified regular expressions. |

### Recipients

When an email is sent to multiple recipients and the DLP policy rules allow only some of those emails to be delivered, the email might get *bifurcated*. For example, say that your DLP policy rules allow emails to be sent to email addresses within your organization and blocks emails from being sent to external email addresses.

There are several policy conditions that cause bifurcation; that allowing an email to be sent to some users but not to others. For more information about bifurcation and the details about how bifurcation works, see the article on [Bifurcation](https://learn.microsoft.com/en-us/en-us/exchange/reference/bifurcation).

| Condition or Exception in DLP | Condition/Exception parameters in Security & Compliance PowerShell | Property type | Description | Bifurcating? |
| --- | --- | --- | --- | --- |
| Recipient is | Condition: *SentTo* Exception: *ExceptIfSentTo* | *Addresses* | Messages where one of the recipients is the specified mailbox, mail user, or mail contact in the organization. The recipients can be in the **To**, **Cc**, or **Bcc** fields of the message. | Yes |
| Recipient domain is | Condition: *RecipientDomainIs* Exception: *ExceptIfRecipientDomainIs* | *DomainName* | Messages where the domain of the recipient's email address matches the specified value. | Yes |
| Recipient address contains words | Condition: *AnyOfRecipientAddressContainsWords* Exception: *ExceptIfAnyOfRecipientAddressContainsWords* | *Words* | Messages that contain the specified words in the recipient's email address. **Note**: This condition doesn't consider messages that are sent to recipient proxy addresses. It only matches messages that are sent to the recipient's primary email address. | No |
| Recipient address matches patterns | Condition: *AnyOfRecipientAddressMatchesPatterns* Exception: *ExceptIfAnyOfRecipientAddressMatchesPatterns* | *Patterns* | Messages where a recipient's email address contains text patterns that match the specified regular expressions. **Note**: This condition doesn't consider messages that are sent to recipient proxy addresses. It only matches messages that are sent to the recipient's primary email address. | No |
| Sent to member of | Condition: *SentToMemberOf* Exception: *ExceptIfSentToMemberOf* | *Addresses* | Messages that contain recipients who are members of the specified distribution group whether assigned or dynamic, mail-enabled security group, or Microsoft 365 group whether assigned or dynamic. The group can be in the **To**, **Cc**, or **Bcc** fields of the message. | Yes |
| The recipient's specified properties include any of these words | Condition: *RecipientADAttributeContainsWords* Exception: *ExceptIfRecipientADAttributeContainsWords* | First property: *ADAttribute* Second property: *Words* | Messages where the specified Microsoft Entra ID attribute of a recipient contains any of the specified words.  Note that the **Country** attribute requires the two-letter country code value (for example, DE for Germany). | Yes |
| The recipient's specified properties match these text patterns | Condition: *RecipientADAttributeMatchesPatterns* *ExceptIfRecipientADAttributeMatchesPatterns* | First property: *ADAttribute* Second property: *Patterns* | Messages where the specified Entra ID attribute of a recipient contains text patterns that match the specified regular expressions. | Yes |
| Recipient scope/Content is shared with | Condition: *AccessScope* Exception: *ExceptIfAccessScope* | *UserScopeFrom* | Messages that are received by either internal or external recipients. | Yes |
| Unique recipient count over | Condition: *RecipientCountOver* | *Number* | Messages where the count of recipients is greater than the specified value. Groups are expanded and final recipient count is compared. | No |
| Unique recipient domain over | Condition: *DomainCountOver* | *Number* | Messages where the count of recipients' domains is greater than the specified value. | No |

Note

DLP supports only mail enabled security groups, distribution groups assigned, and dynamic, and Microsoft 365 Groups, both assigned and dynamic for sender and recipient based conditions that accept groups as input.

### Message subject or body

| Condition or Exception in DLP | Condition/Exception parameters in Security & Compliance PowerShell | Property type | Description |
| --- | --- | --- | --- |
| Subject contains words or phrases | Condition: *SubjectContainsWords* Exception: *ExceptIf SubjectContainsWords* | *Words* | Messages that have the specified words in the Subject field.  This condition has limited support for non-english multibyte characters. |
| Subject matches patterns | Condition: *SubjectMatchesPatterns* Exception: *ExceptIf SubjectMatchesPatterns* | *Patterns* | Messages where the Subject field contains text patterns that match the specified regular expressions. |
| Content contains | Condition: *ContentContainsSensitiveInformation* Exception: *ExceptIfContentContainsSensitiveInformation* | *SensitiveInformationTypes* | Messages or documents that contain sensitive information as defined by Microsoft Purview Data Loss Prevention (DLP) policies. |
| Content is not labeled | Condition: *ContentIsNotLabeled* Exception:*ExceptIfContentIsNotLabeled* | *Sensitivity Labels* | Messages where neither the email nor the attached documents contain any sensitivity labels as defined by Microsoft Purview Data Loss Prevention (DLP) policies. |
| Subject or Body matches pattern | Condition: *SubjectOrBodyMatchesPatterns* Exception: *ExceptIfSubjectOrBodyMatchesPatterns* | *Patterns* | Messages where the subject field or message body contains text patterns that match the specified regular expressions. |
| Subject or Body contains words | Condition: *SubjectOrBodyContainsWords* Exception: *ExceptIfSubjectOrBodyContainsWords* | *Words* | Messages that have the specified words in the subject field or message body.  This condition has limited support for non-english multibyte characters. |

### Attachments

| Condition or Exception in DLP | Condition/Exception parameters in Security & Compliance PowerShell | Property type | Description |
| --- | --- | --- | --- |
| Attachment is password protected | Condition: *DocumentIsPasswordProtected* Exception: *ExceptIfDocumentIsPasswordProtected* | None | Messages where an attachment is password protected (and therefore can't be scanned). Password detection works for Office documents, compressed files (.zip, .7z), and .pdf files. |
| Attachment's file extension is | Condition: *ContentExtensionMatchesWords* Exception: *ExceptIfContentExtensionMatchesWords* | *Words* | Messages where an attachment's visible or the actual file extension matches any of the specified words. To detect renamed .7z files, you must configure configure the rule to protect files with the .7zip extension. |
| Any email attachment's content could not be scanned | Condition: *DocumentIsUnsupported*Exception: *ExceptIf DocumentIsUnsupported* | N/A | Messages where an attachment isn't recognized by [Exchange Online](https://learn.microsoft.com/en-us/en-us/exchange/security-and-compliance/mail-flow-rules/inspect-message-attachments). |
| Any email attachment's content didn't complete scanning | Condition: *ProcessingLimitExceeded* Exception: *ExceptIfProcessingLimitExceeded* | N/A | Messages where the rules engine couldn't complete the scanning of the attachments. You can use this condition to create rules that work together to identify and process messages where the content couldn't be fully scanned. |
| Document scan failures | Condition: *DocumentScanFailures* | N/A | Recommend using with **Document could not be scanned** or **Document didn't complete scanning** conditions to enforce actions on granular scanning error scenarios across classification timeout, throttling or other failures. |
| Document name contains words | Condition: *DocumentNameMatchesWords* Exception: *ExceptIfDocumentNameMatchesWords* | *Words* | Messages where an attachment's file name matches any of the specified words that are delimited between the start of the name, any non-alphanumeric character that appears on the keyboard, or end of the name. |
| Document name matches patterns | Condition: *DocumentNameMatchesPatterns* Exception: *ExceptIfDocumentNameMatchesPatterns* | *Patterns* | Messages where an attachment's file name contains text patterns that match the specified regular expressions. This has been discontinued for SharePoint and OneDrive workloads. Existing rules can't be modified and new rules can't be created. Existing customers can continue to use this condition. |
| Document property is | Condition: *ContentPropertyContainsWords* Exception: *ExceptIfContentPropertyContainsWords* | *Words* | Messages with documents where an attachment's custom property matches the given value. |
| Document size equals or is greater than | Condition: *DocumentSizeOver* Exception: *ExceptIfDocumentSizeOver* | Size | Messages where any attachment is greater than or equal to the specified value. |
| Any attachment's content includes any of these words | Condition: *DocumentContainsWords* Exception: *ExceptIfDocumentContainsWords* | *Words* | Messages where an attachment contains the specified words. |
| Any attachments content matches these text patterns | Condition: *DocumentMatchesPatterns* Exception: *ExceptIfDocumentMatchesPatterns* | *Patterns* | Messages where an attachment contains text patterns that match the specified regular expressions. |

### Message Headers

| Condition or Exception in DLP | Condition/Exception parameters in Security & Compliance PowerShell | Property type | Description |
| --- | --- | --- | --- |
| Header contains words or phrases | Condition: *HeaderContainsWords* Exception: *ExceptIfHeaderContainsWords* | *Hash Table* | Messages that contain the specified header field, and the value of that header field contains the specified words. |
| Header matches patterns | Condition: *HeaderMatchesPatterns* Exception: *ExceptIfHeaderMatchesPatterns* | *Hash Table* | Messages that contain the specified header field, and the value of that header field contains the specified regular expressions. |

### Message properties

| Condition or Exception in DLP | Condition/Exception parameters in Security & Compliance PowerShell | Property type | Description |
| --- | --- | --- | --- |
| With importance | Condition: *WithImportance* Exception: *ExceptIfWithImportance* | *Importance* | Messages that are marked with the specified importance level. |
| Content character set contains words | Condition: *ContentCharacterSetContainsWords* Exception: *ExceptIfContentCharacterSetContainsWords* | *CharacterSets* | Messages that have any of the specified character set names. |
| Has sender override | Condition: *HasSenderOverride* Exception: *ExceptIfHasSenderOverride* | N/A | Messages where the sender has chosen to override a data loss prevention (DLP) policy. For more information, see [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) |
| Message type matches | Condition: *MessageTypeMatches* Exception: *ExceptIfMessageTypeMatches* | *MessageType* | Messages of the specified type. **Note**: The available message types are Automatic reply, Auto-forward, Encrypted (S/MIME), Calendaring, Permission controlled (rights management), Voicemail, Signed, Read receipt, and Approval request. |
| The message size is greater than or equal to | Condition: *MessageSizeOver* Exception: *ExceptIfMessageSizeOver* | *Size* | Messages where the total size (message plus attachments) is greater than or equal to the specified value. **Note**: Message size limits on mailboxes are evaluated before mail flow rules. A message that's too large for a mailbox will be rejected before a rule with this condition is able to act on the message. |

## Enhanced matched conditions in alerts and Activity Explorer (preview)

When an Exchange Online DLP policy matches a message, the DLP alert and the corresponding Activity Explorer event surface enhanced detail for every non-sensitive information type (SIT) condition that contributed to the match. This applies to all condition categories listed in the preceding sections: Senders, Recipients, Message subject or body, Attachments, Message headers, and Message properties. For the full list of supported conditions and detail levels, see [Enhanced matched conditions for Exchange DLP events](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer#enhanced-matched-conditions-for-exchange-dlp-events-preview).

## Actions for DLP policies

This table describes the actions that are available in DLP.

| Action in DLP | Action parameters in Security & Compliance PowerShell | Property type | Description |
| --- | --- | --- | --- |
| Restrict access or encrypt content in Microsoft 365 locations | BlockAccess | First property: *Boolean* Second property: *BlockAccessScope* | This allows you to block the access or encrypt the content to the specified users using RMS templates. |
| Set header | SetHeader | First property: *Header Name* Second property: *Header Value* | The `SetHeader` parameter specifies an action for the DLP rule that adds or modifies a header field and value in the message header. This parameter uses the syntax `"HeaderName:HeaderValue"`. You can specify multiple header name and value pairs separated by commas |
| Remove header | RemoveHeader | First property: *MessageHeaderField* Second property: *String* | The `RemoveHeader` parameter specifies an action for the DLP rule that removes a header field from the message header. This parameter uses the syntax `HeaderName` or `"HeaderName:HeaderValue`. You can specify multiple header names or header name and value pairs separated by commas |
| Redirect the message to specific users | RedirectMessageTo | *Addresses* | Redirects the message to the specified recipients. The message isn't delivered to the original recipients, and no notification is sent to the sender or the original recipients. |
| Forward the message for approval to sender's manager | Moderate | First property: *ModerateMessageByManager* Second property: *Boolean*`$true` | The *Moderate* parameter specifies an action for the DLP rule that sends the email message to a moderator (the user's manager or specified approvers). To forward the message to the user's manager for approval, use this syntax: `@{ModerateMessageByManager = $true}` |
| Forward the message for approval to specific approvers | Moderate | First property: *ModerateMessageByManager* Second property: *Boolean*`$false` Third property: *ModerateMessageByUser* Fourth property: *Addresses* | The *Moderate* parameter specifies an action for the DLP rule that sends the email message to a moderator (the user's manager or specified approvers). To forward the message to specified recipients for approval, use this syntax: `@{ModerateMessageByManager = $false; ModerateMessageByUser = @("emailaddress1","emailaddress2",..."emailaddressN")}` |
| Add recipient | AddRecipients | First property: *Field*Second property: *Addresses* | Adds one or more recipients to the **To/Cc/Bcc** field of the message. This parameter uses the syntax: `@{<AddToRecipients \<CopyTo \| BlindCopyTo\> = "emailaddress"}` |
| Add the sender's manager as recipient | AddRecipients | First property: *AddedManagerAction*Second property: *Field* | Adds the sender's manager to the message as the specified recipient type (**To**, **Cc**, **Bcc**), or redirects the message to the sender's manager without notifying the sender or the recipient. This action only works if the sender's `Manager` attribute is defined in the Microsoft Entra ID. This parameter uses the syntax: `@{AddManagerAsRecipientType = "\<To \| Cc \| Bcc\>"}` |
| Prepend subject | PrependSubject | *String* | Adds the specified text to the beginning of the **Subject** field of the message. Consider using a space or a colon (:) as the last character of the specified text to differentiate it from the original subject text.To prevent the same string from being added to messages that already contain the text in the subject (for example, replies), add the *The subject contains words* (`ExceptIfSubjectContainsWords`) exception to the rule. |
| Apply HTML disclaimer | ApplyHtmlDisclaimer | First property: *Text*Second property: *Location*Third property: *Fallback action* | Applies the specified HTML disclaimer to the required location of the message.This parameter uses the syntax: `@{Text = " " ; Location = \<Append \| Prepend\>; FallbackAction = \<Wrap \| Ignore \| Reject\>}` |
| Remove message encryption and rights protection | RemoveRMSTemplate | N/A | Removes message encryption applied on an email |
| Apply Branding to encrypted messages | ApplyBrandingTemplate | *String* | The `ApplyBrandingTemplate` parameter specifies an action for the DLP rule that applies a custom branding template for messages encrypted by Microsoft Purview Message Encryption. You identify the custom branding template by name. If the name contains spaces, enclose the name in quotation marks ("). |
| Make external recipients open mail in encrypted message portal | EnforcePortalAccess | *Boolean* | The `EnforcePortalAccess` parameter controls whether external users are required to use the encrypted message portal to view encrypted messages |
| Deliver the message to the hosted quarantine | *Quarantine* | N/A | Delivers the message to the quarantine in Microsoft 365. For more information, see [Quarantined email messages](https://learn.microsoft.com/en-us/en-us/microsoft-365/security/office-365-security/quarantine-about).DLP policies applied to external Out-of-Office (OOF) replies are not supported for this action by design; such messages will be dropped instead of being quarantined. |
| Modify Subject | ModifySubject | *PswsHashTable* | Remove text from the subject line that matches a specific pattern and replace it with different text. See the example below. You can:  - **Replace** all matches in the subject with the replacement text  - **Append** to remove all matches in the subject and inserts the replacement text at the end of the subject.  - **Prepend** to remove all matches and inserts the replacement text at the beginning of the subject. For more information, see the [ModifySubject parameter description](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancerule#-modifysubject) in the [New-DlpComplianceRule](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancerule) reference article. |
