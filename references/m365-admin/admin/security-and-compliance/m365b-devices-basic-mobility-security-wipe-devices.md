# Wipe devices in Basic Mobility and Security

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-wipe-devices  
> Microsoft doc last updated: 08/14/2025


Mobile devices can store sensitive organizational information and provide access to your organization's Microsoft 365 resources. Admins can remotely remove company data from devices that are [enrolled in Basic Mobility and Security](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-enroll-devices). The following actions are available:

- **Factory reset**: Delete all data on the device, including all installed apps, photos, and personal information. This action returns the device to factory default settings. Typically, you use this action on company owned devices. For example:
  - Lost or stolen devices.
  - Reassigned devices before you reassign them.
- **Remove company data**: Remove only organization data from the device. Personal data, photos, and apps aren't affected. Typically, you use this action on personal devices when a user leaves the company. Removing company data has the following effects based on the device platform:
  - Policy settings applied by Basic Mobility and Security are no longer enforced; users can change the device settings. Applies to:
    - iOS/iPadOS
    - Android
  - Email profiles created by Basic Mobility and Security are removed and cached email is deleted. Applies to:
    - iOS/iPadOS

    > [!TIP]
    > The **Require managing email profile** (_RequireEmailProfile_) setting is required in the applicable policy to remove company data.

- **Delete**: Remove the device from management by Basic Mobility and Security. The result is equivalent to **Remove company data**.

Regardless of your selection, the request is immediately sent to the device:

- The device is marked as not compliant in Microsoft Entra ID.
- The device is removed from the list of managed devices on the **Fully managed** tab of the **Active devices** page in the Microsoft 365 admin center.

## What do you need to know before you begin?

- You open the **Active devices** page for Basic Mobility and Security at <https://admin.microsoft.com/Adminportal/Home?#/IntuneDevices/?isMifo=true>.

- You need to be assigned permissions before you can do the procedures in this article. You have the following options:
  - [Microsoft Entra permissions](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal): Membership in the **Global Administrator**<sup>\*</sup> or **Cloud Device Administrator** roles gives users the required permissions _and_ permissions for other features in Microsoft 365.

    > [!IMPORTANT]
    > <sup>\*</sup> Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.

- You can't use a delegated admin account to manage Basic Mobility and Security. For more information about delegated administration, see [Partners: Offer delegated administration](https://support.microsoft.com/office/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e).

- Questions? See the [Basic Mobility and Security FAQ](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview#basic-mobility-and-security-faq).

## Wipe a device

1. On the **Overview** tab of the Basic Mobility and Security page at <https://compliance.microsoft.com/basicmobilityandsecurity>, select **Manage devices**. Or, to go directly to the **Active devices** page, use <https://admin.microsoft.com/Adminportal/Home?#/IntuneDevices/?isMifo=true>.

   Devices on the **Fully managed** tab are enrolled in Basic Mobility and Security.

2. On the **Fully managed** tab of the **Active devices** page, do one of the following steps to select the device or devices you want to wipe:
   - Select the check box next to the **Device name** column of one or more devices.
   - Clicking anywhere in the row other than the check box next to the **Device name** column to open the details flyout.
   - Select **⋮** in the **Device name** column.

3. Select one of the following actions:
   -  **Remove company data**: Delete only Microsoft 365 organization information. Read the information in the confirmation dialog that opens, and then select **Remove data**.
   -  **Factory reset**: Wipe the device and return it to factory settings. Read the information in the confirmation dialog that opens, and then select **Factory Reset**.
   -  **Delete**: Equivalent to **Remove data**. Read the information in the confirmation dialog that opens, and then select **Delete**.

> [!TIP]
> You can configure device security policies in Basic Mobility and Security to automatically factory reset devices after a specified number of unsuccessful device password attempts (the **Number of sign-in failures before device is wiped** setting). For more information, see [Access requirement settings in Basic Mobility and Security](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview#access-requirement-settings) and [Configure policies in Basic Mobility and Security](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-policies-configure).
