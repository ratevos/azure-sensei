# Get started with the Microsoft Purview extension for Chrome

> Source: https://learn.microsoft.com/en-us/purview/dlp-chrome-get-started  
> Microsoft doc last updated: 2026-06-26


Use these procedures to roll out the Microsoft Purview extension for Chrome.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

Note

The Microsoft Purview extension for Chrome only works on Windows devices. You don't need the extension to enforce data loss prevention on macOS devices.

## Before you begin

To use the Microsoft Purview extension for Chrome, you must onboard the device into Endpoint data loss prevention (DLP). Review these articles if you're new to DLP or Endpoint DLP:

- [Learn about the Microsoft Purview extension for Chrome](https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about)
- [Learn about Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
- [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy)
- [Learn about Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)
- [Onboarding tools and methods for Windows 10/11 devices](https://learn.microsoft.com/en-us/purview/device-onboarding-overview)
- [Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP](https://learn.microsoft.com/en-us/purview/device-onboarding-configure-proxy#configure-device-proxy-and-internet-connection-settings-for-microsoft-purview-endpoint-dlp)
- [Using Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-using)

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

- Your organization must be licensed for Endpoint DLP.
- Your devices must run Windows 10 x64 (build 1809 or later).
- The device must have Antimalware Client version 4.18.2202.x or later. Check your current version by opening the **Windows Security** app, select the **Settings** icon, and then select **About**.

### Permissions

You can view data from Endpoint DLP in [Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer). Seven roles grant permission to view and interact with the activity explorer. The account you use to access the data must be a member of at least one of these roles.

- Global administrator
- Compliance admin
- Security admin
- Compliance data admin
- Global reader
- Security reader
- Reports reader

Important

Use roles with the fewest permissions to improve security for your organization. Global Administrator is a highly privileged role that you should only use in scenarios where a lesser privileged role can't be used.

#### Roles and role groups

You can use roles and role groups to fine tune your access controls.

Here's a list of applicable roles. To learn more about them, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader

Here's a list of applicable role groups. To learn more about them, see [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

- Information Protection
- Information Protection Admins
- Information Protection Analysts
- Information Protection Investigators
- Information Protection Readers

### Overall installation workflow

Deploying the extension is a multistage process. You can install it on one machine at a time, or you can use Microsoft Intune or Group Policy for organization-wide deployments.

1. Prepare your devices.
2. Basic Setup Single Machine Selfhost
3. Deploy using Microsoft Intune
4. Deploy using Group Policy
5. Test the extension
6. Use the Alerts Management Dashboard to view Chrome DLP alerts
7. Viewing Chrome DLP data in activity explorer

### Prepare infrastructure

If you're rolling out the extension to all your monitored Windows 10/11 devices, you should remove Google Chrome from the unallowed app and unallowed browser lists. For more information, see [Unallowed browsers](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#unallowed-browsers). If you're only rolling it out to a few devices, you can leave Chrome on the unallowed browser or unallowed app lists. The extension bypasses the restrictions of both lists for those computers where it's installed.

Important

If you configure a Chrome NativeMessageBlocklist, you must configure a [NativeMessageAllowlist](https://chromeenterprise.google/policies/#NativeMessagingAllowlist) that includes the Chrome extension.

### Prepare your devices

1. Use the procedures in these articles to onboard your devices:
    1. [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)
    2. [Onboarding Windows 10 and Windows 11 devices](https://learn.microsoft.com/en-us/purview/device-onboarding-overview)
    3. [Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP](https://learn.microsoft.com/en-us/purview/device-onboarding-configure-proxy#configure-device-proxy-and-internet-connection-settings-for-microsoft-purview-endpoint-dlp)

Important

Microsoft Purview upgraded Purview Chrome extension to Manifest V3. If you already have Purview Chrome extension installed, you should see automatic upgrade on your machine to 3.0.0.239 or higher.

### Set up the extension on a single self-hosted machine

Installing the extension from the Chrome Web Store is the recommended method for a single machine.

1. Go to [Microsoft Purview Extension - Chrome Web Store (google.com)](https://chrome.google.com/webstore/detail/microsoft-compliance-exte/echcggldkblhodogklpincgchnpgcdco).
2. Install the extension by following the instructions on the Chrome Web Store page.

### Deploy using Microsoft Intune

Use the Microsoft Intune deployment method for organization-wide deployments.

#### Force-install the Chrome extension with Microsoft Intune

Using the settings catalog, follow these steps to manage Chrome extensions:

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
2. Go to **Configuration Profiles**.
3. Select **Create Profile**.
4. Select **Windows 10 and later** as the platform.
5. Select **Settings catalog** as the profile type.
6. Select **Custom** as the template name.
7. Select **Create**.
8. Enter a name and optional description on the **Basics** tab and select **Next**.
9. Select **Add settings** on the **Configuration settings** tab.
10. Select **Google** &gt; **Google Chrome** &gt; **Extensions**.
11. Select **Configure the list of force-installed apps and extensions**.
12. Change the toggle to **Enabled**.
13. Enter the following value for the extensions and app IDs and update URL: `echcggldkblhodogklpincgchnpgcdco;https://clients2.google.com/service/update2/crx`.
14. Select **Next**.
15. Add or edit scope tags on the **Scope tags** tab as needed and select **Next**.
16. Add the required deployment users, devices, and groups on the **Assignments** tab and select **Next**.
17. Add applicability rules on the **Applicability Rules** tab as required and select **Next**.
18. Select **Create**.

### Deploy by using Group Policy

If you don't want to use Microsoft Intune, you can use group policies to deploy the extension across your organization.

#### Add the Chrome extension to the ForceInstall list

Perform the following steps to add the extension to Chrome's force-install list through Group Policy:

1. In the Group Policy Management Editor, go to your OU.
2. Expand the following path: **Computer/User configuration** &gt; **Policies** &gt; **Administrative templates** &gt; **Classic administrative templates** &gt; **Google** &gt; **Google Chrome** &gt; **Extensions**. This path might vary depending on your configuration.
3. Select **Configure the list of force-installed extensions**.
4. Right-click and select **Edit**.
5. Select **Enabled**.
6. Select **Show**.
7. Under **Value**, add the following entry: `echcggldkblhodogklpincgchnpgcdco;https://clients2.google.com/service/update2/crx`
8. Select **OK** and then **Apply**.

### Test the extension

#### Test uploads to cloud services and access from unallowed browsers

Use the following test to verify that Chrome DLP blocks uploads to restricted cloud destinations:

1. Create or get a sensitive item and try to upload a file to one of your organization’s restricted service domains. The sensitive data must match one of our built-in [Sensitive Info Types](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions), or one of your organization’s sensitive information types. You should get a DLP toast notification on the device you're testing from that shows that uploading the file isn't allowed when the file is open.

#### Simulate other DLP scenarios in Chrome

Now that you removed Chrome from the disallowed browsers/apps list, you can run [simulation scenarios](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn) to confirm that the behavior meets your organization’s requirements:

- Copy data from a sensitive item to another document using the Clipboard
    - To test, open a file that is protected against copy to clipboard actions in the Chrome browser and attempt to copy data from the file.
    - Expected result: A DLP toast notification showing that copying data to the clipboard isn't allowed when the file is open.
- Print a document
    - To test, open a file that is protected against print actions in the Chrome browser and attempt to print the file.
    - Expected result: A DLP toast notification showing that printing the file isn't allowed when the file is open.
- Copy to USB Removable Media
    - To test, try to save the file to a removable media storage.
    - Expected result: A DLP toast notification showing that saving the file to removable media isn't allowed when the file is open.
- Copy to Network Share
    - To test, try to save the file to a network share.
    - Expected result: A DLP toast notification showing that saving the file to a network share isn't allowed when the file is open.

### Use the Alerts Management Dashboard to view Chrome DLP alerts

Use the following steps to view Chrome DLP alerts in the Alerts dashboard:

1. Open the **Data loss prevention** page in the Microsoft Purview portal and select **Alerts**.
2. Refer to the procedures in [Get started with the data loss prevention Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) and [Investigate data loss incidents with Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender) to view alerts for your Endpoint DLP policies.

### View Chrome DLP data in Activity Explorer

Use the following steps to view Chrome DLP activity in Activity explorer:

1. Open the Microsoft Purview portal &gt; **Information protection** &gt; **Explorers** &gt; **Activity explorer**.
2. Follow the procedures in [Get started with Activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) to access and filter all the data for your Endpoint devices.
