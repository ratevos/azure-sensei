# Onboard Windows 10 and Windows 11 devices using Configuration Manager

> Source: https://learn.microsoft.com/en-us/purview/device-onboarding-sccm  
> Microsoft doc last updated: 2025-02-13


**Applies to:**

- [Endpoint data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)
- [Insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management)

#### Supported client operating systems

You can onboard the following operating systems using Configuration Manager:

- Windows 11
- Windows 10, version 1709 or newer

Important

When onboarding systems to Microsoft Purview for endpoint, they will also report to Defender for Endpoint, even if a different antivirus or anti-malware solution is in use. In such cases, these systems will report to Defender for Endpoint in **passive mode**, ensuring there is no interference with the existing antivirus or anti-malware solution.

### Onboarding to Microsoft Purview for Endpoint with Configuration Manager

In Configuration Manager, configure the Endpoint Protection settings as follows to ensure the client recognizes the configuration file.

- Set **Manage Endpoint protection client on the computers** to **Yes**.
- The **Install Endpoint Protection Client on Client computers** can be set to **No**.

Note

This is to allow clients to receive the configuration file from Configuration Manager. If you do not turn this on the Configuration file may not deploy on to the clients.

- Set the Microsoft Defender for Endpoint client on Windows server 2012 R2 and Windows Server 2016 to **MDE client (recommended)**.

Deploy this Client Settings configuration to the collections that are used to onboard systems.

#### Onboard devices using Configuration Manager

1. Get the configuration package .zip file (*DeviceComplianceOnboardingPackage.zip*) from [Microsoft Purview portal](https://purview.microsoft.com).
2. In the navigation pane, select **Settings** &gt; **Device Onboarding** &gt; **Onboarding**.
3. In the **Select Operating system to start onboarding process**: select **Windows 10** and then in the **Deployment method** field, select **Microsoft Endpoint Configuration Manager**.
4. Select **Download package** and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location accessible by the Configuration Manager console for deployment. Ensure the file named ***DeviceCompliance.onboarding*** is present.

#### Onboard the devices

1. In the Configuration Manager console, navigate to **Assets and Compliance** &gt; **Endpoint Protection** &gt; **Microsoft Defender for Endpoint Policies**.

    Note

    Microsoft Purview and Microsoft Defender for Endpoint use the same method to connect to Microsoft cloud security environments.
2. Select **Create Microsoft Defender for Endpoint Policy** to open the policy wizard.
3. Select **I accept these license terms and automatic updates of both Agents**. Then type the **Name** and **Description** for the Microsoft Defender for Endpoint policy and select **Onboarding**.
4. Select **Browse** and browse to the configuration file you extracted from the downloaded .zip file.

    Note

    You do not need the Workspace key and Workspace ID for Windows 10 and 11.

    Select **Next**.
5. Specify the file samples that are collected and shared from managed devices for analysis.

    - **None**
    - **All file types**
6. Review the summary and complete the wizard.
7. Right-click on the policy you created, select **Deploy**, and then choose a collection to which you want to deploy the Microsoft Defender for Endpoint policy.

## Monitor

1. In the Configuration Manager console, navigate **Monitoring** &gt; **Deployments** and then select the deployment you created for the **Defender for Endpoint policy** deployment.
2. Click on **View Status** to review the information. Under **Compliant** you can see the status of the onboarded systems. Systems that have not yet been onboarded may appear under the **Unknown** tab.

Note

This process may take some time, and the system might need to reboot for the changes to take effect.

## Offboard devices using Configuration Manager

For security reasons, the package used to Offboard devices will expire 30 days after the date it was downloaded. Expired offboarding packages sent to a device will be rejected. When downloading an offboarding package, you'll be notified of the packages expiry date and it will also be included in the package name.

Note

Onboarding and offboarding policies must not be deployed on the same device at the same time, otherwise this causes unpredictable collisions.

#### Offboard devices using Microsoft Configuration Manager current branch

If you use Microsoft Configuration Manager current branch, see [Create an offboarding configuration file](https://learn.microsoft.com/en-us/en-us/mem/configmgr/protect/deploy-use/defender-advanced-threat-protection#create-an-offboarding-configuration-file).

#### Create an offboarding configuration file

1. Sign in to the [Microsoft Purview console](https://Purview.microsoft.com).
2. Select **Settings**, then select **Device onboarding** and then select **Offboarding** under the onboarding heading.
3. Select **Windows 10** for the operating system and **Microsoft Endpoint Configuration Manager** for the deployment method.

    - Using the **Windows 10** option ensures that all devices in the collection are off boarded, and the MMA is uninstalled when needed.
4. Download the compressed archive (.zip) file and extract the contents. Offboarding files are valid for 30 days.
5. In the Configuration Manager console, navigate to **Assets and Compliance** &gt; **Endpoint Protection** &gt; **Microsoft Defender For Endpoint Policies** and select **Create Microsoft Defender for Endpoint Policy**. The policy wizard opens.
6. Type the **Name** and **Description** for the Microsoft Defender for Endpoint policy and select **Offboarding**.
7. **Browse** to the configuration file you extracted from the downloaded .zip file.
8. Review the summary and complete the wizard.
9. Select Deploy to target the Microsoft Defender for Endpoint policy to clients you wish to offboard from Purview.

Important

The Microsoft Purview for Endpoint configuration files contains sensitive information which should be kept secure.

Tip

If you're not an E5 customer, use the 90-day Microsoft Purview Suite trial to explore how additional Purview capabilities can help your organization manage data security and compliance needs. Start now at the **[Microsoft Purview trials hub](https://purview.microsoft.com/home/trials?sku=ComplianceE5&amp;ref=DocsRef)**. Learn details about **[signing up and trial terms](https://learn.microsoft.com/en-us/en-us/purview/compliance-easy-trials)**.

## Monitor device configuration

With Microsoft Configuration Manager current branch, use the built-in Microsoft Defender for Endpoint dashboard in the Configuration Manager console. For more information, see [Microsoft Defender Advanced Threat Protection - Monitor](https://learn.microsoft.com/en-us/en-us/configmgr/protect/deploy-use/windows-defender-advanced-threat-protection#monitor).

### Check that the devices are compliant with the Endpoint data loss prevention service

You can set a compliance rule for configuration item in Configuration Manager to monitor your deployment.

Note

This procedure and registry entry applies to Endpoint DLP and Defender for Endpoint.

This rule should be a *non-remediating* compliance rule configuration item that monitors the value of a registry key on targeted devices.

Monitor the following registry key entry:

```console
Path: "HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status"
Name: "OnboardingState"
Value: "1"
```

For more information, see [Plan for and configure compliance settings](https://learn.microsoft.com/en-us/en-us/mem/configmgr/compliance/plan-design/plan-for-and-configure-compliance-settings).
