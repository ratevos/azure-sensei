# Learn about Endpoint DLP just-in-time protection

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about-jit  
> Microsoft doc last updated: 2026-06-22


Use endpoint data loss prevention (DLP) [just-in-time (JIT)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#just-in-time-protection) protection to detect and block egress activities on monitored files while policy evaluation completes.

JIT audits and blocks these user egress activities on protected items:

- Copy to a removable media
- Copy to a network share
- Print
- Copy or move using Remote Desktop Protocol (RDP)
- Copy or move using a blocked Bluetooth app
- Copy to clipboard: JIT Audit by default
- Upload to a restricted cloud service domain

## Terms

This article uses the following terms:

- **stale classification**: A classification that isn't produced by the most current version of a DLP policy. If you update a policy after an item is evaluated and classified, the item has a stale classification until the policy re-evaluates it.
- **JIT candidate file**: Files that DLP hasn't evaluated or that have a stale classification.
- **JIT audit**: After you enable JIT, Endpoint DLP generates an event in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) for every JIT candidate file. In the JIT activity explorer event, the **JIT triggered** field has the value `true`, and the **Enforcement mode** value is `Audit`.

- **JIT block**: After you enable JIT, Endpoint DLP blocks the activity and generates an event in activity explorer for every JIT candidate file. In the JIT activity explorer event, the **JIT triggered** field has the value `true`, and the **Enforcement mode** field has the value `Block`.

Note

Endpoint DLP doesn't generate a `DLPRuleMatch` event or an alert.

- **JIT in progress notification**: When users who are in scope for JIT attempt an egress activity on a JIT candidate file, Endpoint DLP might block the egress activity and display a toast notification. This toast is called the JIT in progress toast.
- **JIT evaluation complete notification**: When Endpoint DLP finishes policy evaluation for a JIT candidate file, Endpoint DLP shows a toast notification to let the user know. This notification is called the JIT evaluation complete toast.
- **JIT event**: Endpoint DLP records and shows a JIT event in activity explorer when JIT audit or JIT block actions trigger. The event has the `JIT triggered` value set to `true`.
- **Fallback action in case of failure**: This configuration specifies the enforcement mode that DLP should apply when the policy evaluation doesn't complete. No matter which value you select, the relevant telemetry shows in activity explorer.



## How JIT protection works

JIT protection blocks the egress activity when all the following conditions are true:

- A user attempts an egress activity on an item that has never been classified or that is classified with a stale policy. A stale policy means the file was classified with a policy that has since been updated, and the file hasn't been reclassified with the updated policy.
- The user is in the scope of JIT.
- Microsoft Purview Data Loss Prevention (DLP) policies exist that block or block with override for the *egress activity*.
- The egress activity isn't to an allowed location. For example, an allowed printer, USB device, URL, or network share.
- The egress activity doesn't support JIT pause and resume.
- The DLP policy evaluation *doesn't* complete in five seconds.

### JIT workflow



1. A user attempts an egress activity on an onboarded device for one or more JIT candidate items.
2. If the activity involves an app on the excluded app list, an excluded file path location, or an excluded file extension, the process ends.
3. The evaluation ends and the activity isn't blocked by JIT. No notification message is shown to the user and no JIT audit event is logged.
4. DLP confirms that the user is in scope for JIT. If yes, evaluation continues. If not, the process ends at step 5.
5. JIT doesn't block the activity. No notification is shown, and a JIT audit event is logged.
6. DLP checks if any DLP rule defines **Block** or **Block with override** actions for the attempted activity. If yes, evaluation continues. If not, the process ends with the behavior noted in step 5.
7. JIT doesn't block the activity. No notification is shown, and a JIT audit event is logged.
8. DLP checks if the activity is to an allowed printer group, USB group, network share, or URL. If yes, JIT doesn't block the activity and policy evaluation ends.
9. JIT evaluation is triggered.
10. JIT checks to see if the activity supports JIT pause and resume.
11. If yes, evaluation continues.
12. For all the activities that complete policy evaluation within three seconds, the policy action is applied.
13. For **audit** action, the activity resumes, there's no message shown to the user and a JIT audit event is logged in the audit log.
14. For **block** action, the activity is blocked. A blocked activity message is shown to the user and a JIT audit event is logged in the audit log.
15. User sees policy message with **Review files** button or **Take action** button. Policy evaluation ends.
16. For **block with override** action, the activity is blocked, the block with override message is shown to the user so they can override the block as needed, and both JIT audit event and the block with override event are logged in the audit log.
17. For all the items that didn't complete DLP policy evaluation within three seconds OR don't support resume, JIT evaluation allows two more seconds.
18. For all activities that complete DLP policy evaluation within the allotted two seconds, the policy action is applied.
19. For **audit** policy action, the activity is blocked because the activity doesn't support resume and a JIT block event is logged in the audit log.
20. User sees the policy evaluation complete message and is told to retry. Policy evaluation ends.
21. For **block** policy action, the activity is blocked, a blocked activity message is shown, and a JIT block event is logged in the audit log and evaluation ends.
22. For **block with override** policy action, the activity is blocked, the block with override message is shown so the user can override the block as needed, and both JIT block event and block with override event are logged in the audit log and evaluation ends.
23. For all the items that didn't complete DLP policy evaluation within the total five seconds, the activity is blocked, the **Just-in-time in progress** message is shown to the user. A JIT block event is logged in the audit log.
24. The JIT in progress allows 30 more seconds for the policy evaluation to complete while the activity is blocked.
25. If the DLP policy evaluation completes within these 30 seconds, the user is shown the **Just-in-time evaluation complete** message and the user is asked to retry the activity again.
26. If DLP policy evaluation doesn't complete within the 30 seconds, the JIT fallback action is applied.
27. The **JIT policy evaluation complete** message is shown to the user and evaluation ends. The user is prompted to try the activity again.

## User experience of just-in-time protection

This section describes the user experience with antimalware client version **4.18.25080 or later**.

### Resume support for each activity

If the policy evaluation finishes within 3 seconds, Endpoint DLP automatically resumes these activities:

- Copy to a removable media
- Copy to a network share

If the policy evaluation takes longer than 3 seconds, you need to repeat the activity after the JIT policy evaluation complete notification appears.

Repeat these activities after Endpoint DLP completes the policy evaluation:

- Print
- Copy or move using Remote Desktop Protocol (RDP)
- Copy or move using unallowed Bluetooth app
- Copy to clipboard: JIT Audit by default

### Perform an activity on a single file

When a user performs an activity on a single file, Endpoint DLP takes the JIT audit action when:

- the user isn't in the JIT Scope setting
- there's no **Block** or **Block with override** for the activity
- the activity is to an allowed printer, removable media, network share, or website
- the policy evaluation for the file completes within 5 seconds for activities that support JIT resume, or completes within seconds for activities that don't support JIT resume.

Endpoint DLP blocks the activity with a notification (no alert) and applies JIT block only when the policy evaluation takes more than 5 seconds.

### Perform an activity on multiple files

When a user performs an activity on multiple files simultaneously, Endpoint DLP takes the JIT audit action when:

- the user isn't in the JIT Scope setting
- there's no **Block** or **Block with override** for the performed activity
- the activity is to an allowed printer, or to an allowed removable media, or to an allowed network share

For JIT candidate files, Endpoint DLP triggers policy evaluation, consolidates notifications for files that finish within 5 seconds for activities that support resume, and automatically resumes the activity. If the activity doesn't support resume, Endpoint DLP triggers policy evaluation and consolidates notifications for files that finish within 2 seconds. In both cases, Endpoint DLP doesn't raise a JIT in progress toast. It only shows the final policy verdict in the consolidated toast.
