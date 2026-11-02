# Learn about the Microsoft Purview Data Loss Prevention migration assistant for Symantec and Forcepoint

> Source: https://learn.microsoft.com/en-us/purview/dlp-migration-assistant-for-symantec-learn  
> Microsoft doc last updated: 2025-01-28


This article helps you to learn about the Microsoft Purview Data Loss Prevention migration assistant for Symantec and Forcepoint.

The migration assistant is a Windows-based desktop application for migrating your Symantec and Forcepoint data loss prevention (DLP) policies to Microsoft Purview Data Loss Prevention. This article takes you through the five-step migration process. The migration assistant accepts Symantec DLP policy XML exports and Forcepoint DLP policy backup, performs mapping, and creates equivalent DLP policies through PowerShell scripts. You can use the migration assistant to create DLP policies in [**Run the policy in simulation mode**](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn). Policies in simulation mode won't affect your live data or impact your existing business processes.

## What can the migration assistant help with?

The migration assistant helps with some of the tasks involved in a DLP migration project:

- In a manual migration scenario, you need to perform a feasibility analysis between the source and target DLP platforms, map the features, migrate policies manually, and test and tweak DLP policies. With the migration assistant, your migrated DLP policies can be up and running within minutes of starting the migration assistant process.
- With migration assistant, you can quickly scale up your migration project. You can start by moving a single policy manually to multiple policies at the same time.
- The migration assistant automatically identifies sensitive information types (SITs) or Data Identifiers in source policies and creates custom SITs in your Microsoft tenant. It also moves all of your custom regular expressions and keywords in a few clicks.
- The migration assistant detects which conditions, exclusions, and actions are currently used in source policies and automatically creates new rules with the same conditions and actions.
- The migration assistant provides you with a detailed migration report that includes the migration status and recommendations at the policy level.
- The migration assistant ensures that your DLP policy migration project is private and takes place within the boundaries of your organization.

## How does the migration assistant for Symantec and Forcepoint work?

Here's how the migration process works:



Each time the migration assistant runs, it performs the following steps:

- **Input:** The migration assistant ingests one or more Symantec DLP policy XML files or Forcepoint DLP policy backup (.bak) file.
- **Analyze:** The migration assistant interprets the files and identifies Symantec and Forcepoint DLP policy constructs.
- **Rationalize:** The migration assistant maps the identified Symantec and Forcepoint DLP policy constructs to Microsoft DLP capabilities. It performs validations for Microsoft DLP platform limitations.
- **Migrate:** The migration assistant runs PowerShell scripts for the DLP scenarios identified and supported by the Microsoft Purview DLP platform.
- **Report:** The migration assistant reports which policies were migrated successfully, which were partially migration, and which ones couldn't be migrated. It also provides recommendations to improve future migrations.

## Understand mapping of Symantec and Forcepoint DLP elements to Microsoft Purview DLP elements

The migration assistant translates different policy elements from Symantec DLP to Microsoft Purview DLP.

### Symantec DLP supported versions

The migration assistant supports migrating DLP policies from Symantec versions 15.0 through 16.0, maintenance packs included.

### Forcepoint DLP supported versions

The migration assistant supports migrating DLP policies from Forcepoint versions 8.0 through 10.0.

### Supported Workloads

The migration assistant migrates policies into these workloads:

| **Workload** | **Migration assistant support** |
| --- | --- |
| Exchange | Yes |
| SharePoint | Yes |
| OneDrive | Yes |
| Teams chat and channel messages | Yes |
| Endpoint devices | Yes |

Tip

You can use the migration assistant to extend your policy to more workloads than the ones detected in the input Symantec or Forcepoint DLP policy.

### Classification Elements

Here's how the migration assistant maps Symantec and Forcepoint elements to Purview DLP elements.

| **Symantec Classification Element** | **Microsoft Purview DLP Classification Element** |
| --- | --- |
| Regular Expression | Create a new custom sensitive information type (SIT) with the regular expression. |
| Keyword | Create a new custom SIT with a keyword list or keyword dictionary. |
| Keyword Pair | Create a new custom SIT with first keyword list as primary element & second keyword list as a supporting element with 300 char proximity. |
| Data Identifier | Map to a preconfigured SIT if an equivalent is available, else create a new custom SIT. |

Here are the mapping details of optional validators for sensitive information types (also known as Data Identifiers in Symantec DLP) that the migration assistant uses while translating Symantec DLP policies:

| **Symantec Optional Validators** | **Microsoft Purview DLP Optional Validators** |
| --- | --- |
| Exclude exact match | Exclude specific matches |
| Exact Match Data Identifier Check | N/A |
| Exclude beginning characters | Starts or doesn't start with characters |
| Exclude ending characters | Ends or doesn't end with characters |
| Exclude prefix | Include or Exclude prefixes |
| Exclude suffix | Include or Exclude prefixes |
| Number Delimiter | N/A |
| Require beginning characters | Starts or doesn't start with characters |
| Exact Match | N/A |
| Duplicate digits | Exclude duplicate characters |
| Require ending characters | Ends or doesn't end with characters |
| Find keywords | Available as both primary & supporting elements |

### Regular Expressions – Potential validation issues to be aware of

When you upload your rule package XML file, the system validates the XML and checks for known bad patterns and obvious performance issues. Here are known issues that the validation process checks a regular expression for.

- Can't begin or end with alternator "|", which matches everything because it's considered an empty match.
    - For example, "|a" or "b|" won't pass validation.
- Can't begin or end with a ".{0,m}" pattern, which has no functional purpose and only impairs performance.
    - For example, ".{0,50}ASDF" or "ASDF.{0,50}" won't pass validation.
- Can't have ".{0,m}" or ".{1,m}" in groups, and can't have ".\*" or ".+" in groups.
    - For example, "(.{0,50000})" won't pass validation.
- Can't have any character with "{0,m}" or "{1,m}" repeaters in groups.
    - For example, "(a\*)" won't pass validation.
- Can't begin or end with ".{1,m}"; instead, use just "."
    - For example, ".{1,m}asdf" won't pass validation; instead, use just ".asdf".
- Can't have an unbounded repeater (such as "\*" or "+") on a group.
    - For example, "(xx)\*" and "(xx)+" won't pass validation.

### Condition and Exception Mapping

Here's how the migration assistant maps Symantec and Forcepoint, condition and exception elements for various workloads to Microsoft Purview DLP conditions.

#### Exchange Workload

| **Condition/Exception in Symantec** | **Condition in Microsoft Purview DLP** |
| --- | --- |
| Content Matches Regular Expression | Content contains SIT |
| Content Matches Keyword | Content contains SIT |
| Content Matches Data Identifier | Content contains SIT |
| Content Matches Classification | Not supported |
| File Properties- File name<br>- File type | One or more of the following:- Document name is<br>- File extension is |
| Message Attachment or File Type Match | One or more of the following:- Attachment is password protected<br>- Attachment's file extension is |
| Message Attachment or File Size Match | Document size equals or is greater than |
| Message Attachment or File Name Match | One or more of the following:- Document name contains words or phrases<br>- Document name matches patterns |
| Message/Email Properties and Attributes | One or more of the following:- Email subject contains |
| Sender/User Matches Pattern | One or more of the following:- Sender is<br>- Sender is a member of<br>- Sender domain is<br>- Sender address contains words<br>- Sender address matches patterns<br>- Sender IP address is |
| Recipient Matches Pattern | One or more of the following:- Recipient is a member of<br>- Recipient domain is<br>- Recipient is<br>- Recipient address contains words<br>- Recipient address matches patterns |
| Sender/User based on a Directory Server Group | Not supported |
| Recipient based on a Directory Server Group | Not supported |
| Content Matches Exact Data from an Exact Data Profile (EDM) | Not supported |
| Content Matches Document Signature from an Indexed Document Profile (IDM) | Not supported |
| Detect using Vector Machine Learning profile (VML) | Not supported |
| Protocol Monitoring- SMTP protocol | Exchange (EXO) DLP policy |

#### Endpoint Devices, SharePoint Online, OneDrive, and other workloads

| **Condition/Exception in Symantec** | **Condition in Microsoft Purview DLP** |
| --- | --- |
| Content Matches Regular Expression | Content contains SIT |
| Content Matches Keyword | Content contains SIT |
| Content Matches Data Identifier | Content contains SIT |
| Message Attachment or File Type Match | Document’s file extension is |
| Protocol Monitoring- HTTP<br>- HTTPS<br>- FTP | Cross-workload DLP policy(s) |
| Protocol Monitoring: Endpoint Device Type- CD/DVD<br>- Removable storage<br>- Copy to network share<br>- Printer/Fax<br>- Clipboard<br>- Cloud storage<br>- Application File Access<br>- SEP Intensive Protection | One or more of the following (Devices):- Copy to USB removable media<br>- Copy to network share<br>- Copy to clipboard<br>- Print<br>- Upload to cloud service domains or access by browsers that aren't allowed |

### Response Rules

Here's how the migration assistant maps Symantec and Forcepoint response rules to Microsoft Purview DLP actions.

| **Symantec Response Rule** | **Microsoft Purview DLP Action** |
| --- | --- |
| Generate DLP Incident | Generate Alert |
| Logging (Syslog) | Audit logs |
| Network Prevent: Modify SMTP Message- Modify email subject<br>- Modify header | One or more of the following:- Prepend subject<br>- Set headers |
| Network Prevent: Block SMTP Message- Bounce message to sender<br>- Redirect message to this address | One or more of the following:- Block / Restrict access<br>- Send user notification<br>- Redirect message to |
| Send Email Notification | Send User Notification |
| Endpoint Prevent- Notify<br>- Notify with Cancel<br>- Block | One or more of the following (Endpoint Devices)- Notify<br>- Block<br>- Audit |
| User Cancel | One or more of the following:- Block / Restrict access<br>- User Overrides |
