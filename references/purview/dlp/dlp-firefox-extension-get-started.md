# Get started with the Microsoft Purview extension for Firefox

> Source: https://learn.microsoft.com/en-us/purview/dlp-firefox-extension-get-started  
> Microsoft doc last updated: 2026-06-26


Use these procedures to roll out the Microsoft Purview extension for Firefox.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Recommended reading

To use the Microsoft Purview extension for Firefox, the device must be onboarded into endpoint DLP. Review these articles if you're new to DLP or endpoint DLP

If you're new to Microsoft Purview DLP, here's a list of the core articles you'll need as you implement DLP:

1. [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units)
2. [Learn about Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) - the article you're reading now introduces you to the data loss prevention discipline and Microsoft's implementation of DLP
3. [Plan for data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#plan-for-data-loss-prevention-dlp)- by working through this article you will:
    1. [Identify stakeholders](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#identify-stakeholders)
    2. [Describe the categories of sensitive information to protect](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#describe-the-categories-of-sensitive-information-to-protect)
    3. [Set goals and strategy](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#set-goals-and-strategy)
4. [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#data-loss-prevention-policy-reference) - this article introduces all the components of a DLP policy and how each one influences the behavior of a policy
5. [Design a DLP policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) - this article walks you through creating a policy intent statement and mapping it to a specific policy configuration.
6. [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) - This article presents some common policy intent scenarios that you'll map to configuration options, then it walks you through configuring those options.
7. [Learn about investigating data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn) - This article introduces you to the lifecycle of alerts from creation, through final remediation and policy tuning. It also introduces you to the tools you use to investigate alerts.

Additionally, you should be familiar with the information in these articles:

- [Learn about Microsoft Purview extension for Firefox](https://learn.microsoft.com/en-us/purview/dlp-firefox-extension-learn)
- [Learn about endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)
- [Onboarding tools and methods for Windows 10 devices](https://learn.microsoft.com/en-us/purview/device-onboarding-overview)
- [Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP](https://learn.microsoft.com/en-us/purview/device-onboarding-configure-proxy#configure-device-proxy-and-internet-connection-settings-for-microsoft-purview-endpoint-dlp)
- [Using Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-using)

### Licensing and subscription requirements

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

- Your organization must be licensed for Endpoint DLP
- Your devices must be running Windows 10 x64 build 1809 or later.
- The device must have Antimalware Client Version is 4.18.2202.x or later. Check your current version by opening **Windows Security** app, select the **Settings** icon, and then select **About**.

### Permissions

Data from Endpoint DLP can be viewed in [Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer). There are seven roles that grant permission to activity explorer, the account you use for accessing the data must be a member of any one of them.

- Compliance admin
- Security admin
- Compliance data admin
- Global reader
- Security reader
- Reports reader
- Global administrator

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

#### Roles and Role Groups

There are roles and role groups that you can use to fine tune your access controls.

Here's a list of applicable roles. To learn more about them, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

Here's a list of applicable role groups. To learn more about these role groups, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

### Overall installation workflow

Deploying the extension is a multi-phase process. You can choose to install on one machine at a time, or use Microsoft Intune or Group Policy for organization-wide deployments.

1. Prepare your devices.
2. Basic Setup Single Machine Selfhost
3. Deploy using Microsoft Intune
4. Deploy using Group Policy
5. Test the extension
6. Use the Alerts Management Dashboard to view Firefox DLP alerts
7. Viewing Firefox DLP data in activity explorer

### Prepare infrastructure

If you're rolling out the extension to all your monitored Windows 10 devices, you should remove Mozilla Firefox from the unallowed app and unallowed browser lists. For more information, see [Unallowed browsers](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#unallowed-browsers). If you're only rolling it out to a few devices, you can leave Firefox on the unallowed browser or unallowed app lists. The extension bypasses the restrictions of both lists for those computers where it's installed.

### Prepare your devices

1. Use the procedures in these articles to onboard your devices:
    1. [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)
    2. [Onboarding Windows 10 and Windows 11 devices](https://learn.microsoft.com/en-us/purview/device-onboarding-overview)
    3. [Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP](https://learn.microsoft.com/en-us/purview/device-onboarding-configure-proxy#configure-device-proxy-and-internet-connection-settings-for-microsoft-purview-endpoint-dlp)

### Set up a basic single-machine self-hosted deployment

The single-machine self-host installation is the recommended method.

1. Download the initial [XPI file](https://github.com/microsoft/purview/raw/main/endpointDLP/browser_extension/prod-1.1.0.212.xpi).
2. Locate the extension in your file explorer and drag the file into an open Mozilla Firefox window.
3. Confirm the installation.

### Deploy using Microsoft Intune

Use the Microsoft Intune setup method for organization-wide deployments.

#### Configure force install with Microsoft Intune

Before adding the extension to the list of force-installed extensions, it's important to ingest the Firefox ADMX. The following steps explain how to ingest the Firefox ADMX into Microsoft Intune. Before beginning these steps, please ensure you have downloaded the latest Firefox ADMX from the [Firefox GitHub](https://github.com/mozilla/policy-templates/releases).

The following steps can be followed to ingest Firefox ADMX.

1. Sign in to the [Microsoft Intune Admin Center](https://endpoint.microsoft.com).
2. Navigate to **Devices** then to **Configuration**.
3. Select **Create New Policy**.
4. Select **Windows 10** **and later** as the platform.
5. Select **Templates** and **Custom** as profile type then click **Create**.
6. Enter a descriptive name like *Firefox ADMX* and an optional description.
7. Click **Add***OMA-URI Settings* and enter the following policy information.

    Name: Descriptive name.

    Description: Optional description

    OMA-URI: `./Device/Vendor/MSFT/Policy/ConfigOperations/ADMXInstall/Firefox/Policy/FirefoxAdmx`

    Data type: `String`

    Value: Copy all of the text from the downloaded *firefox.admx* file into the *Value* field
8. Select create.

After ingesting the Firefox ADMX, follow the Microsoft Intune procedure in this section to create a configuration profile for the Microsoft Purview extension for Firefox.

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
2. Navigate to Configuration Profiles.
3. Select **Create Profile**.
4. Select **Windows 10** as the platform.
5. Select **Custom** as profile type.
6. Select the **Settings** tab.
7. Select **Add**.
8. Enter the following policy information.

    OMA-URI: `./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/ExtensionSettings` Data type: `String` Value: `<enabled/><data id="ExtensionSettings" value='{"microsoft.defender.browser_extension.native_message_host@microsoft.com":{"installation_mode": "force_installed", "install_url": "https://github.com/microsoft/purview/raw/main/endpointDLP/browser_extension/prod-1.1.0.212.xpi","updates_disabled":false}}'/>`
9. Note: It's critical that `updates_disabled` is set to `false` so that the extension can automatically update over time.
10. Select create.

### Deploy using Group Policy

If you don't want to use Microsoft Intune, you can use group policies to deploy the extension across your organization.

#### Add the Firefox extension to the force-install list

Use the following steps to add the Firefox extension to the force-install list in Group Policy.

1. In the Group Policy Management Editor, navigate to your organizational unit (OU).
2. Expand the following path **Computer/User configuration** &gt; **Policies** &gt; **Administrative templates** &gt; **Classic administrative templates** &gt; **Firefox** &gt; **Extensions**. This path may vary depending on your configuration.
3. Select **Extensions to install**.
4. Right click and select **Edit**.
5. Select **Enabled**.
6. Select **Show**.
7. Under **Value**, add the following entry: `https://github.com/microsoft/purview/raw/main/endpointDLP/browser_extension/prod-1.1.0.212.xpi`
8. Select **OK** and then **Apply**.

### Test the extension

Use the following procedures to validate that the Microsoft Purview extension for Firefox is working correctly in common DLP scenarios.

#### Test uploads to cloud services and access from blocked browsers

Use the following test to verify cloud egress blocking behavior in Firefox.

1. Create or get a sensitive item and, try to upload a file to one of your organization’s restricted service domains. The sensitive data must match one of our built-in [Sensitive Info Types](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions), or one of your organization’s sensitive information types. You should get a DLP toast notification on the device you're testing from that shows that this action isn't allowed when the file is open.

#### Testing other DLP scenarios in Firefox

Now that you’ve removed Firefox from the disallowed browsers/apps list, you can run simulations on the policy for these scenarios below to confirm the behavior meets your organization’s requirements:

- Copy data from a sensitive item to another document using the Clipboard
    - To test, open a file that is protected against copy to clipboard actions in the Firefox browser and attempt to copy data from the file.
    - Expected Result: A DLP toast notification showing that this action isn't allowed when the file is open.
- Print a document
    - To test, open a file that is protected against print actions in the Firefox browser and attempt to print the file.
    - Expected Result: A DLP toast notification showing that this action isn't allowed when the file is open.
- Copy to USB Removable Media
    - To test, try to save the file to a removable media storage.
    - Expected Result: A DLP toast notification showing that this action isn't allowed when the file is open.
- Copy to Network Share
    - To test, try to save the file to a network share.
    - Expected Result: A DLP toast notification showing that this action isn't allowed when the file is open.

### Use the Alerts Management Dashboard to view Firefox DLP alerts

Use the following steps to review Firefox DLP alerts in the Alerts dashboard.

1. Open the **Data loss prevention** page in the Microsoft Purview portal and select **Alerts**.
2. Refer to the procedures in [Get started with the data loss prevention Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) and [Investigate data loss incidents with Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender) to view alerts for your Endpoint DLP policies.

### Use Activity Explorer to view Firefox DLP data

Use Activity explorer to review and filter Firefox DLP activity data for onboarded devices.

1. Open **Activity explorer**.
2. Refer to the procedures in [Get started with Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) to access and filter all the data for your Endpoint devices.

### Known issues and limitations

Be aware of the following limitations when deploying the Microsoft Purview extension for Firefox.

1. Incognito mode isn't supported and must be disabled.
