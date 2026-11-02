# Use the Microsoft Purview Data Loss Prevention migration assistant for Symantec and Forcepoint

> Source: https://learn.microsoft.com/en-us/purview/dlp-migration-assistant-for-symantec-use  
> Microsoft doc last updated: 2026-06-26


The [Microsoft Purview Data Loss Prevention migration assistant for Symantec and Forcepoint](https://learn.microsoft.com/en-us/purview/dlp-migration-assistant-for-symantec-learn) helps you migrate your existing Symantec or Forcepoint DLP policies to Microsoft Purview DLP. The assistant maps data identifiers, keywords, and regular expressions to Microsoft sensitive information types (SITs), and migrates rules, conditions, and actions. By the end of this procedure, your policies are active in Microsoft Purview DLP and ready for testing.

Before you start, make sure you've met these prerequisites:

- Complete the steps in the [Before you begin](https://learn.microsoft.com/en-us/purview/dlp-migration-assistant-for-symantec-get-started#before-you-begin) section.
- Export the required DLP policy files from your current DLP solution.

After a policy is migrated, you can test and fine-tune it in Microsoft Purview DLP.

## Steps for migration

Use these steps to perform a DLP policy migration:

- Step 1: Sign in to your account
- Step 2: Upload the policies that are being migrated
- Step 3: Edit policy settings
- Step 4: Review premigration feasibility report
- Step 5: Merge policies and select policy mode
- Step 6: Migration in progress
- Step 7: View the migration report
- Next steps: After policy import

## Interactive guide

Check out the [Use the Microsoft Purview DLP migration assistant interactive guide](https://mslearn.cloudguides.com/guides/Use%20the%20Microsoft%20Purview%20DLP%20migration%20assistant) for a visual walkthrough of the migration process.

## Step 1: Sign in to your account

After you install and launch the migration assistant, sign in to your account.

Important

The first time you launch the migration assistant, choose the **Run as administrator** option. Running as administrator is required because the migration assistant might need to install additional components if they aren't already available on your machine.

For all subsequent launches, you can launch the migration assistant normally and don't need to run as administrator.



To sign in to the migration assistant:

1. You're greeted with a welcome screen.
    1. Select **Get Started** and the migration assistant checks if your environment is set up correctly.
    2. Select **Next**.
2. Enter your username and select **Login**.
    - Enter your password in the browser window that opens and select **Sign in**.

        Note

        This application uses the Exchange Online PowerShell module. Basic authentication must be enabled in WinRM on the local computer. For more information, see [Prerequisites for the Exchange Online PowerShell module](https://learn.microsoft.com/en-us/en-us/powershell/exchange/exchange-online-powershell-v2#prerequisites-for-the-exchange-online-powershell-module).
3. Wait for sign-in validation. The migration assistant fetches the information required for later stages of the migration process. 
4. After you're signed in, choose **Next**.

## Step 2: Upload the policies that are being migrated

You need to upload your current DLP policy exports, which act as input for the migration assistant. The policies you upload will be migrated to the Microsoft Purview DLP platform.

1. Select which DLP solution you want to migrate policies from.
2. To upload the files, select **Browse**.
3. Select the required policy files in the File Explorer pop-up window and choose **Open**.

    1. Symantec DLP

        1. For migrating policies from Symantec DLP, you need to upload the XML files that you have exported from Symantec DLP.
        2. You can select more than one XML file to migrate multiple policies at a time. Migrate one to three policies at a time to avoid confusion during later stages of the migration process.

        Note

        Ensure that the XML files you upload are Symantec DLP policy exports only and no other kind of XML.
    2. Forcepoint DLP

        1. For migrating policies from Forcepoint DLP, you need to upload the policy backup (.bak) file from Forcepoint DLP.
4. The tool shows you a list of your selected input policy files. You can modify your selection from the policy list.
5. After you complete the selection of policy files you want to migrate, select **Next** to move to the next step.

## Step 3: Edit policy settings

After you input the policies you want to migrate, the migration assistant processes those files and maps Symantec and Forcepoint DLP policy elements to Microsoft DLP elements.

Important

There may be some items that may need your review and will be marked with 'Needs review' warning symbol.



#### Keywords, data identifiers, and regular expressions

Symantec DLP and Forcepoint DLP differ from Microsoft Purview Information Protection in how they allow users to define sensitive information that needs to be protected.

Microsoft Purview Information Protection allows users to define sensitive items that need protection as sensitive information types (SITs), or through trainable classifiers. Microsoft provides many commonly used SITs like Credit Card Number that are preconfigured. If the preconfigured SITs don't meet your needs, you can create your own custom SITs.

The most common ways Symantec and Forcepoint users specify the types of sensitive information that need protection are:

- Using out-of-box (OOB) data identifiers
- Customizing OOB data identifiers
- Defining regular expressions or keywords in DLP rules

The migration assistant handles OOB data identifiers, customized OOB data identifiers, and regular expressions or keywords in one of two ways:

- **Map to an existing OOB SIT:** For each sensitive data type that has an equivalent SIT in Microsoft DLP, the migration assistant attempts to create a 1:1 mapping. It automatically maps OOB Symantec or Forcepoint data identifiers to preconfigured Microsoft SITs, if an equivalent exists. If you want to bring the Symantec or Forcepoint data identifier over as-is, you can create a new SIT as described in the next step.
- **Migrate as a new custom SIT:** For each sensitive data type that doesn't have an equivalent SIT in Microsoft DLP, the migration assistant automatically creates a new SIT. Similarly, any regular expressions or keywords defined directly in rules are brought over as a new custom SIT.

Note

Regular expressions or keywords defined directly at the rule-level of Symantec or Forcepoint policies take on the name of the rule itself and appear in the **Source** column. If there are multiple regular expressions or keywords, they take the rule name followed by roman numerals.

Each of these items is migrated separately as a custom SIT. Migrating each regular expression or keyword as a separate custom SIT can lead to confusion. Review and rename these SITs as soon as possible.

You can't edit the name of these SITs within the migration assistant. You can edit the names of these custom SITs from the Microsoft Purview portal or via PowerShell after the policy migration is complete.

#### Inclusions, exclusions, and response rules

The current version of the migration assistant brings over policies with ‘*Generate Incident Report*’ as a default action. Also, DLP policies in Microsoft DLP automatically log events in Unified Audit Log and won't need a separate action equivalent to ‘Syslog’ in Symantec DLP.

In addition to the automatically migrated response rules (or DLP actions), you can manually add (or remove) actions to the policies after the migration assistant has successfully migrated the policies.

You can see a list of all your policies and rules along with their status. Select different policies from the left column to see details for each policy. By default, the tool displays all items that need review. You can toggle to see all items in a given policy by choosing the **Show All Items** button at the top of the Details section. 

##### Policy details

Policy Name - You can edit the name of the policy before migration.

Each policy is divided into two sections:

- Keywords, data identifiers, and regular expressions — These are migrated as sensitive information types (SITs) in Microsoft DLP.
- Rules — These are automatically mapped to different Microsoft DLP conditions. Each row in the table shows:

    - The name that the SIT will have when migrated
    - Potential issues that may affect migration
    - Type of rule as detected from the input policy
    - Status:
        - Blank/empty status — This row element is migrated without issues.
        - Needs Review — This row element might have one or more issues and might require input from you.
        - Informational — This row element might have one or more changes needed for migration but will be autoresolved.
        - Unsupported — This row element isn't supported for migration by the tool and might need to be migrated manually after the tool exits.
    - Edit button

Extend policy coverage to other Microsoft locations: - You can extend your current Symantec policies to other Microsoft locations in addition to the original scope of the policy.

For example, a Purview DLP policy that's scoped to email can be extended to SharePoint, OneDrive, Teams, and Endpoint Devices.

The migration assistant auto-creates a new policy based on the original policy with all supported rules for that given workload. One or more rules may be dropped if not supported for a given workload.

For example, the **Email subject is** condition may be dropped while extending an email (Exchange) DLP policy to OneDrive.

Some checkboxes may be disabled by default if there are no supported conditions available in extended locations.

Editing a row element — When you select a row element to edit, you're taken to an **Edit** screen with more details. If there are issues, they're reported through a yellow banner at the top of the screen. Make changes to the content in the editable sections. Those changes are incorporated at the time of migration. After you resolve the issues, the yellow banner disappears.

Use existing SITs from the tenant to automatically replace the current SIT. You can replace the current SIT (which is being edited) with another SIT from your tenant.

You can manually change any of the mappings by selecting the corresponding row in the 'Target' column. This opens a drop-down list with all the OOB SITs and any custom SITs you previously created. Select the SIT you want to map to the source item. Alternatively, you can choose **New SIT** from the drop-down. The migration assistant then brings over the source SIT as a new custom SIT.

We strongly recommend using existing SITs to replace current SITs wherever possible. Reusing existing SITs helps reduce creation of duplicate SITs and reduces the effort of optimizing multiple custom SITs of the same kind. Learn more about [sensitive information type entity definitions](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions).

Warning

Microsoft DLP platform has a threshold for up to 10 rule packages per tenant. This limit is enough for most customers, but the creation of many duplicate custom SITs may quickly lead you to hitting this threshold without the ability to create any new custom SITs.

After you've reviewed all the policies and the rules within them, select **Next**. If one or more of the policies contain at least one element with *Needs Review* status, then you’ll see a **Continue with errors** button instead of **Next**.

## Step 4: Review premigration feasibility report

The premigration feasibility report shows you how policies will be migrated. Review this report and make any necessary adjustments before starting a migration run.



Review the details and choose **Next**.

## Step 5: Merge policies and select policy mode

Each DLP policy is split into multiple rules depending on the workloads selected and support for underlying conditions and exceptions for those workloads.

The tool allows you to merge each of these rules with compatible target policies for the same workload. These target policies can be existing Microsoft Purview DLP policies you created earlier, or new policies that you're importing along with the policy you want to merge.

Merging policies together creates a single Microsoft Purview DLP policy with multiple rules. Consolidating multiple rules into a single policy allows for better management of policies.

For each DLP policy that is created, you can set it to one of three states:

- On (**Yes, turn it on right away**)
- Simulate (**Run the policy in simulation mode** and **Show policy tips**)
- Off (**No, keep it off. I'll turn it on later**)

Set the state in the migration assistant before migrating a policy:

1. Choose whether to turn on or off from the following three options:

    - Turn on policy immediately.
    - Turn on policy in simulation mode first. Remove from simulation mode later manually.
    - Keep it off. Turn it on later manually.

    We recommend bringing over the policies first in simulation mode. You can monitor the alerts that the policy generates and fine-tune the policy as required by your organization. After your policy is fine-tuned, you can turn it on.
2. Select **Start Migration** to import your policy. A new PowerShell window opens asking you to sign in again.

    After you sign in, PowerShell scripts run to create new policies in Microsoft DLP with all the data from the input policy files, and any settings you configured during the previous migration assistant steps.

    Wait until the script finishes with a Success/Failure message. Then, new SITs and policies start appearing in the Purview portal.

## Step 6: Migration in progress

In this step, the migration tool creates DLP policies in the Microsoft Purview portal.

Note

Don't close the tool window while policies are being created. Closing the tool might cause incomplete SITs and policies, which could require manual cleanup.



If an error occurs during migration, you can choose one of these actions:

- **Try Again** — Policy creation is attempted again.
- **Rollback all changes** — All SITs and policies for that session are deleted.
- **Rollback failed policies** — Only the failed SITs and policies for that session are deleted.

Important

When you choose to rollback any changes, the rollback can take two to four hours to complete. Keep the migration assistant tool window open for the entire duration for a successful rollback.



After the policies are migrated, select **Next** to view the migration report.



## Step 7: View the migration report

You can view the migration report after your policies are imported and the migration process is complete.



Each session gets its own report. A session begins at the time you launch the app and ends when you exit the app or when migration process is completed.

#### Technical report

You can select the **Save Technical Report** button to save a more detailed Excel-based report that is divided into three sheets:

- Overview
- Policy Details
- SIT Details

**Overview Sheet** — This sheet provides an overview of the migration session with the following details:

- Tenant’s name.
- Timestamp of session.
- Overall summary stats for that session.
- Input policy level details, migration status and comments/recommendations.



**Policy Details** — This sheet provides a detailed view of each migrated policy created or not created with the following information:

- Mapping of source policy and target policy(s) created.
- List of workloads each policy is applied to.
- Analysis status stating if the policy is migrated completely, partially or can't migrate.
    - For workloads other than Exchange, this would typically show as *Complete* since we create a policy with the *Content contains* condition, which is supported across all workloads.
- Migration status describing if the policy migration was a success or failure.
- Comments/recommendations with more details of that policy.



**SIT Details** — This sheet provides information about all the sensitive information types (SITs) that were migrated with the following information:

- Policy-wise mapping of Input and Output SITs created.
- Validation fixes with information about validation errors that occurred during the migration process.
- Comments about SIT automapping, and remediation steps.



## Next steps: After policy import

Visit the Purview portal and validate the policies you migrated.

#### Check sensitive information types

Use the following steps to verify and tune the migrated SITs:

1. To validate that the SITs were created, navigate to **Data Classification** &gt; **Classifiers** &gt; **Sensitive Info Types** and look for the SITs. You can also sort the list on **Publisher** and check for SITs with a publisher name of “DLP Migration Tool”.
2. Rename SITs as needed. For many SITs, you may notice there are similar names, often followed by roman numerals. To avoid confusion and duplication post-migration, you should rename these SITs. This is true for cases where your regular expressions and keywords are defined directly in rules within your input Symantec or Forcepoint DLP policies.
3. Test and fine-tune SITs as needed. You should test and fine-tune the migrated SITs. The migration assistant creates new SITs with a few standard settings, which might not be right for your tenant so look out for the following:

    1. Regular expressions: Unsupported or deleted regexes (during migration)
    2. Keywords
        1. Case sensitive versus insensitive keywords
        2. String versus word match
        3. Proximity
        4. Optional validators

#### Check DLP policies

Use the following checks to validate and finalize the migrated DLP policies:

1. **Validate the DLP policies created**

    Select **Data Loss Prevention** from the left panel and check if new policies are created.
2. **Add any missing policy elements**

    While most Symantec and Forcepoint DLP policy elements (like conditions, exclusions, or actions) are migrated, some elements from your input policy might be dropped during the migration process. Dropping some policy elements during migration is a known limitation of the migration assistant. In this scenario, manually add these elements to the policy, as they're supported by the Microsoft Purview DLP platform.
3. **Test and fine-tune the policy**

    You can test the policy and fine-tune it for the needs of your organization.
4. **Turn the policy on**

    After fine-tuning, you can turn on the policy or put it in production mode.
5. **Bring over any remaining policies**

    You can go back to bring over the next policy or next batch of policies using the migration assistant.

## Troubleshooting

If you see an error on welcome screen after selecting **Get Started**, follow these steps:

1. Confirm that you've installed all the prerequisites using the links/versions mentioned in [Before you start](https://learn.microsoft.com/en-us/purview/dlp-migration-assistant-for-symantec-get-started#before-you-begin).
2. Ensure that you've restarted the machine after installing the prerequisites.
3. Ensure that you're running the tool in *admin mode* using the **Run as administrator** option when starting the application.
4. Ensure that your PowerShell module path is set correctly using these steps:
    1. Go to **Edit system environment variables**.
    2. Add this path in the **PsModulePath** user variable: `C:\Program Files\PowerShell\7\Modules`.
    3. Move this up and keep at the top.
    4. Restart the tool in administrator mode.

If you're unable to install/uninstall due to another app/process installation, follow these steps:

1. Right click on the task bar to open Task Manager. If necessary, choose **More Details**.
2. On the **Details** tab, look for *msiexec.exe* and select **End Task**.
3. Try to install or uninstall again, or, wait until the installation is finished.

To report issues to Microsoft:

1. **Collect logs** - Find the logs generated by the migration assistant on your local machine at the following path: `C:\Users\<username>\AppData\Local\Temp\MigrationAssistantforMicrosoftPurviewDLP\Logs`.
2. **Send email** - Send us the details about your issue along with the latest logs at dlpmigrations@microsoft.com or contact your CXE / FastTrack / Microsoft partner to share your feedback and suggestions.

### Report errors and provide feedback

To report errors, raise feature requests, or share more feedback, reach out to us at dlpmigrations@microsoft.com or contact your CXE / FastTrack / Microsoft partner.

### Telemetry notice

**Data Collection**: This software might collect information about you and your use of the software, and send it to Microsoft. Microsoft might use this information to improve our products and services. If you want to turn off telemetry, you can reach out to us, and we provide you with a separate version of the tool with telemetry turned off.

There are also some features in the software that might enable you and Microsoft to collect data from users of your applications. If you use these features, you must comply with applicable law, including providing appropriate notices to users of your applications with a copy of Microsoft's privacy statement. Our privacy statement is located at [Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?LinkID=824704). You can learn more about data collection and use in the help documentation and our privacy statement. Your use of the software operates as your consent to these practices.
