# Get started with Endpoint DLP Just-in-time protection

> Source: https://learn.microsoft.com/en-us/purview/endpoint-dlp-get-started-jit  
> Microsoft doc last updated: 2026-06-26


Use endpoint data loss prevention (DLP) [just-in-time (JIT)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#just-in-time-protection) protection to detect and block egress activities on monitored files while policy evaluation completes.

## Applies to

JIT protection for Endpoint DLP supports these devices:

- Windows 10
- Windows 11
- macOS (the three most recent versions)

## Best practice for deploying Just-in-time protection

Note

Allow at least an hour for JIT setting updates, including disabling JIT, to be pushed to client devices.

### Step 1: Prepare your environment

Before you can deploy just-in-time protection, you must first deploy antimalware Client version 4.18.23080 or later. The [just-in-time protection end user experience](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about-jit#user-experience-of-just-in-time-protection) is improved in version 4.18.25080 or later.

Tip

To maximize user productivity, configure and deploy your Endpoint DLP policies to your devices before enabling just-in-time protection. This approach prevents unnecessary blocking of user activity during policy evaluation.



Note

For machines with an outdated version of the antimalware client, disable just-in-time protection by installing one of the following KBs:

- Windows 10 - [KB5032278](https://support.microsoft.com/en-us/topic/november-30-2023-kb5032278-os-build-19045-3758-preview-0ae14f06-577e-4eb3-8fcb-c722f3f9dc29)
- Windows 11 - [KB5032288](https://support.microsoft.com/en-us/topic/december-4-2023-kb5032288-os-builds-22621-2792-and-22631-2792-preview-538fbe4a-e9de-4312-85cd-d870444341d0)

1. To find out which devices have the necessary antimalware client, go to **Security portal** &gt; **Investigation & response** &gt; **Advanced hunting**, and run this query.

```kusto
`DeviceRegistryEvents`
| where InitiatingProcessVersionInfoInternalFileName == "MsMpEng.exe" and Timestamp >= ago(60d)
| summarize arg_max(Timestamp, *) by DeviceId
| distinct DeviceName, DeviceId, vTimeStamp = Timestamp, AntiMalwareClientVersion = InitiatingProcessVersionInfoProductVersion
| extend Meet_Minimum_JIT_Version = strcmp(AntiMalwareClientVersion, "4.18.23080") // whether the device has required minimum JIT version
| extend Meet_Latest_JIT_Version = strcmp(AntiMalwareClientVersion, "4.18.25080") // whether the device has latest JIT improvement
| project DeviceId, Meet_Latest_JIT_Version, Meet_Minimum_JIT_Version, AntiMalwareClientVersion
| summarize dcount(DeviceId) by AntiMalwareClientVersion // distribution of AntiMalwareClientVersion
// | summarize dcount(DeviceId) by Meet_Minimum_JIT_Version //how many devices meet minimum JIT version
// | summarize dcount(DeviceId) by Meet_Latest_JIT_Version //how many devices meet latst JIT improvements
| order by dcount_DeviceId desc
```

Here's an example of the output of the query.



You can also go to **Data Loss Prevention** &gt; **Diagnostics page**, and select **Endpoint DLP not working** card to check whether a specific device meets JIT prerequisite.



### Step 2: Deploy JIT protection

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data Loss Prevention** &gt; **Just-in-time protection**.
3. Under **Choose which locations to monitor**, select the checkbox next to **Devices**.
4. Under **Fallback action in case of failure**, select **Allow users to complete actions**. This option lets the user action complete if the classification fails.

Caution

Don't choose the **Block users from completing actions** option until you fully understand the impact of this feature.

Selecting **Allow users to complete actions** or **Block users from completing actions** doesn't change whether *JIT Block* is triggered. Blocking by JIT is applied if the user is in scope. The **Allow users to complete actions** or **Block users from completing actions** setting controls Endpoint DLP enforcement when classification fails.

If you select **Allow users to complete actions**, Endpoint DLP allows the egress activity when classification fails. If you select **Block users to complete actions**, Endpoint DLP blocks the egress activity when classification fails.

### Step 3: Estimate the number of JIT protection events for your deployment

Validate the JIT protection scope and fallback action settings after each rollout stage until the number of events is stable. Make sure you understand the possible size of the user group you want to enforce the policy on, based on the following telemetry calculations.

Estimate the impact of deploying JIT protection by performing the following calculation based on the events in activity explorer:

- N = The number of unique machines firing JIT events.
- S = The total number of machines within the scope of your deployment.

`N/S` yields the percentage of machines that might experience a JIT protection block event.

With this information, you should know how many machines will be affected by implementing the JIT Block mode when you expand the scope, and how many possible support tickets you may see. Then, you can decide whether or not to expand the scope.

### Step 4: Fine-tune JIT protection through other Additional settings

In addition to the **Fallback action in case of failure** setting, you can also use the following settings to fine-tune JIT protection:

- **Control copying to clipboard**: Turn on this setting to prevent users from copying content to the clipboard while JIT protection is evaluating the file.

Note

Turning on **Control copying to clipboard** might impact user's productivity. Be sure to test the impact on productivity before turning on this setting.

- **App exclusions for Windows**: You can exclude maximum 50 apps here from JIT protection on Windows devices.
- **App exclusions for Mac**: You can exclude maximum 50 apps here from JIT protection on Mac devices.
- **File extensions exclusions**: Files with extensions you add here aren't evaluated by JIT protection.
- **File path exclusions for Windows**: Files in these locations aren't evaluated by JIT protection.
- **File path exclusions for Mac**: Files in these locations aren't evaluated by JIT protection.

If you want to change the scope of JIT protection after tuning all these settings, return to **Settings** &gt; **Data Loss Prevention** &gt; **Just-in-time protection** in the Microsoft Purview portal and update the monitored locations.

#### Exclusions for Just-in-time protection

**File path exclusion** settings in JIT are different from **File path exclusions for Windows** setting found via **Data loss prevention** &gt; **Settings** &gt; **Endpoint settings** &gt; **File path exclusions for Windows**.

- **File path exclusions** in JIT only excludes specific file paths from JIT protection. In all other cases, Microsoft Purview still applies Endpoint DLP classification and protection for files in those folders.
- **File path exclusions for Windows** setting prevents Purview from applying Endpoint DLP classification and protection for files under the specified folders.
- **File extension exclusions**: Files with these extensions aren't evaluated by JIT protection.

### Step 5: Deploy JIT protection in 'Block users from completing actions' for the 'Fallback action in case of failure' setting

The **Block users from completing actions** option for **Fallback action in case of failure** controls the enforcement mode that DLP applies when classification fails. This setting doesn't control JIT Block or JIT Audit for JIT candidate files. JIT Block or JIT Audit is controlled by how the policy is scoped. No matter which value you select here, the relevant telemetry displays in activity explorer.
