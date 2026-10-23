# How to enable QR code authentication in Microsoft Entra ID

> Source: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-qr-code  
> Microsoft doc last updated: 06/24/2025


This topic covers how to enable the QR code authentication method in the Authentication methods policy in Microsoft Entra ID. It also covers how to manage the QR code authentication method for users, and how they can sign in with a QR code and PIN. 

Before you enable QR code authentication method, review the best practices for using security controls for work or home access for frontline workers. For more information, see [Best practices to protect frontline workers](https://learn.microsoft.com/en-us/entra/identity-platform/security-best-practices-for-frontline-workers).

## Prerequisites to enable the QR code authentication method

- An active Azure subscription.
  - If you don't have an Azure subscription, [create an account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- A Microsoft Entra tenant associated with your subscription.
  - If needed, [create a Microsoft Entra tenant][create-azure-ad-tenant] or [associate an Azure subscription with your account][associate-azure-ad-tenant].
- You need at least the [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator) role in your Microsoft Entra tenant to enable the QR code authentication method.
- Each user that's enabled in the QR code authentication method policy must be licensed, even if they don't use it. Each enabled user must have one of the following Microsoft Entra ID, EMS, Microsoft 365 licenses:
    - [Microsoft 365 F1 or F3][m365-firstline-workers-licensing]
    - [Microsoft Entra ID P1 or P2](https://www.microsoft.com/security/business/microsoft-entra-pricing)
    - [Enterprise Mobility + Security (EMS) E3 or E5][ems-licensing] or [Microsoft 365 E3 or E5][m365-licensing]
    - [Office 365 F3][o365-f3]
- Android, iOS, or iPadOS (iOS/iPadOS version 15.0 or later) shared devices. 
- Shared device mode enabled on the shared devices (optional but highly recommended). 
- A printer to print 2" x 2" QR codes. 
- To access QR code authentication on Teams, Teams app installed on the shared device would require these versions: Android version 1.0.0.2024143204 or later, and iOS version 1.0.0.77.2024132501 or later.
- [Set up the My Staff portal](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/my-staff-configure) if you plan for frontline managers to use My Staff to provision, manage, and reset QR code and PINs. 

## Enable QR code authentication method

You can enable the QR code authentication method by using the Microsoft Entra admin center or Microsoft Graph API. 

### Enable QR code authentication method in the Microsoft Entra admin center

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator).
1. Go to **Entra ID** > **Authentication methods** > **Policies**.
1. Click **QR code** > **Enable and target** > **Add target** > select a group of users who need to sign in with a QR code. 

   

1. Update default QR code settings as needed:
   - By default, the PIN length is 8 digits. The PIN length can be 8 to 20 digits. If you increase the PIN length, the new value becomes the minimum number of digits required for the PIN. For example, if you increase the PIN length to 10, a user needs to provide a 10-digit PIN during next sign-in.
   - The default lifetime of a standard QR code (provided to the users for long term use) is 365 days. The range is between 1-395 days. You can change the lifetime of a standard QR code for specific user when you add the QR code authentication method for them.

   

1. When you're done, click **Save**.

### Enable QR code authentication method in Microsoft Graph API

This example enables QR code authentication for a group, with a PIN length of 10 digits, and a Standard QR code lifetime of 395 days:

- **Request**

  ```https
  PATCH https://graph.microsoft.com/beta/policies/authenticationMethodsPolicy/authenticationMethodConfigurations/qrCodePin
  {
    "@odata.type" : "microsoft.graph.qrCodePinAuthenticationMethodConfiguration", 
    "id": "qrCodePin", 
    "state": "enabled", 
    "includeTargets": [{ 
      "targetType": "group", 
      "id": "b185b746-e7db-4fa2-bafc-69ecf18850dd", 
      }], 
    "excludeTargets": [], 
    "standardQRCodeLifetimeInDays":395,
    "pinLength": 10
  }
  ```

- **Response**

  ```https
  204 No Response
  ```

## Add QR code authentication method for a user

You can add a QR code authentication method for a user by using the Microsoft Entra admin center, My Staff, or Microsoft Graph API. At a time, only one active QR code auth method is allowed. Standard QR code is generated during 'Add authentication method'. You can add Temporary QR code, which is short-lived, if user is not carrying Standard QR code. You can delete Standard/Temporary QR code to add a new Standard/Temporary QR code. A user can have only one Standard and one Temporary QR code active at any point of time. 

### Add QR code authentication method for a user in the Microsoft Entra admin center

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator).

1. Go to **Users**, select a user, and click **Authentication methods**.

1. Click **Add authentication method** and choose **QR code**.

   

1. Modify the expiration date for the user if needed. Set **Activation time** to now or later. Provide or generate a temporary PIN. The custom PIN can be specified only when you add the QR code authentication method. A PIN is autogenerated during reset events. When ready, click **Add** to add the QR code authentication method for the user.

   

1. Save the PIN, and click **Download image** to download and print the QR code. The QR code image download has the smallest optimal print size. If you reduce the size of the QR code, it may impact QR code scan performance.

   You can't regenerate the same QR code because it has a unique secret. If the QR code can't work for some reason, delete it. Create a new QR code for the user.

   

1. After you add the QR code authentication method, it appears as a usable authentication method for the user.

   

### Add the QR code authentication method for a user in My Staff

1. Sign in to the My Staff portal as a frontline manager. Select an administrative unit and a frontline worker.

   

   

1. Click **Manage QR code authentication method**.

   

1. Click **Add QR code method**.

   

1. Specify the expiration and activation date, and click **Add** to generate a QR code and PIN for the user.

   

1. Save the PIN, download or print the QR code, and then click **Done**. The QR code image download has the smallest optimum print size. If you reduce the size, the QR code is hard to scan. You can't regenerate the same QR code because it has a unique secret. If the QR code can't work for some reason, delete it. Create a new QR code for the user.

   

### Add QR code authentication method for a user in Microsoft Graph API

This example adds QR code authentication method for a user: 

- **Request**

  ```https
  HTTP PUT/users/{id | userPrincipalName}/authentication/qrCodePinMethod
  
  
  {
    "standardQRCode": {
      "expireDateTime": "2024-12-30T12:00:00Z",
      "startDateTime": "2024-10-30T12:00:00Z"
    },
    "pin": {
      "code": "<PIN>"
    }
  }
  ```

- **Response**

  ```https
  HTTP/1.1 201 Created
  Location: /beta/users/aaaaaaaa-bbbb-cccc-1111-222222222222/authentication/qrCodePinMethod`
  Content-type: application/json

  {
    "standardQRCode": {
      "id": "BBBBBBBB-1C1C-2D2D-3E3E-444444444444"
      "expireDateTime": "2024-12-30T12:00:00Z",
      "startDateTime": "2024-10-30T12:00:00Z"
      "createdDateTime": "2024-10-30T12:00:00Z",
      "lastUsedDateTime": null,
       "image":
          {
    "binaryValue": "<binaryImageData>",
           "version": 1,
           "errorCorrectionLevel": "H".
           "rawContent": <binary data encoded in QR>        
    }
      },
    "temporaryQRCode": null,
    "pin": {
      "code": "<PIN>",
      "isForcePinChangeRequired": true,
      "createdDateTime": "2024-10-30T12:00:00Z",
      "updatedDateTime": null
    }  
  }
  ```

This example confirms whether QR code authentication method is added for the user:

- **Request**

  ```https
  GET https://graph.microsoft.com/beta/users/flokreg@contoso.com/authentication/qrCodePinMethod`
  ```

- **Response**

  ```https
  HTTP/1.1 200 OK
  Content-type: application/json
  
  {
    "id": "<id>",
    "standardQRCode": {
      "id": "BBBBBBBB-1C1C-2D2D-3E3E-444444444444"
      "image": null,
      "expireDateTime": "2024-12-30T12:00:00Z",
      "startDateTime": "2024-10-30T12:00:00Z"
      "createdDateTime": "2024-10-30T12:00:00Z",
      "lastUsedDateTime": "2024-12-30T12:00:00Z"
    },
    "temporaryQRCode": {
      "id": "CCCCCCCC-2D2D-3E3E-4F4F-555555555555"
      "image": null,
      "expireDateTime": "2024-12-30T12:00:00Z",
      "startDateTime": "2024-10-30T12:00:00Z"
      "createdDateTime": "2024-10-30T12:00:00Z",
      "lastUsedDateTime": "2024-12-30T12:00:00Z"
    },
    "pin": {
      "code": null,
      "isForcePinChangeRequired": false,
      "createdDateTime": "2024-10-30T12:00:00Z",
      "updatedDateTime": "2024-11-30T12:00:00Z"
    }
  }

## Edit the QR code authentication method for a user

You can edit QR code authentication method for a user by using the Microsoft Entra admin center, My Staff, or Microsoft Graph API. 

### Edit the QR code authentication method for a user in the Microsoft Entra admin center

- Navigate to the usable authentication methods for a user, and click **Edit** to edit the properties of the QR code authentication method.

  

- Change the expiration time for the standard QR code, and click **Save**. After you make edits, click **Done**.

  

- Delete a standard QR code. You might want to delete the standard QR code if it's reported as expired, compromised, or stolen. 
  
  

  After you delete the standard QR code, click the add symbol (**+**) to add a new standard QR code for the user. 
  The deleted QR code is no longer valid for login. 
  
  You need to print and distribute the new QR code to the user. 
  The user can continue to use their existing PIN. 

  

- Reset a PIN. If you need to reset a user PIN, generate a temporary one and distribute it to the user. The user will be required to change the temporary PIN at the next sign-in. Click the pencil icon after the masked PIN. Click **Generate new PIN** to create a new temporary PIN. Click **OK** to confirm that the user is forced to change the temporary PIN when they next sign in. Copy the temporary PIN and share it with the user. 

  

- Add or delete a temporary QR code. A temporary QR code reduces admin overhead of provisioning and deprovisioning the QR code on a badge if a user didn't bring their badge to work. It also reduces the stress of retaining the QR code after their shift. A temporary QR code has a lifetime of 1-12 hours and can be activated instantly or later. 
To deprovision the QR code, you can delete the temporary QR code or let it expire as it's unusable after expiry.

  

  

### Edit the QR code authentication method for a user in My Staff

- To edit the expiration date for a standard QR code, click **Edit**. Edit the expiration date and save the changes.

  

- To delete a standard QR code, click **Delete**, and confirm the action.

  

- To add a new standard QR code, click **Add new** next to the standard QR code.

  

  Select the activation time and expiration date for the QR code, and click **Add**. 

  

  Download or print the QR code, and click **Done**.

  

- To add a temporary QR code, click **Add new** next to the temporary QR code. Specify the **Lifetime in hours** and the **Activation date**, and click **Add**.

  

  Download or print the QR code, and click **Done**.

  

- To reset a PIN, click **Reset PIN**. 

  

  Click **Copy PIN** to copy the PIN to your clipboard.

  

### Edit the QR code authentication method for a user in Microsoft Graph API

This example shows how to delete the standard QR code for a user if they lose their badge, and create a new standard QR code. The user isn't required to change their PIN.

Delete a standard QR code:

- **Request**

  ```https
  DELETE https://graph.microsoft.com/beta/users/flokreg@contoso.com/authentication/qrCodePinMethod/standardQRCode`
  ```

- **Response**

  ```https
  HTTP/1.1 204 No Content
  ```

Create a standard QR code:

- **Request**

  ```https
  HTTP PATCH/users/{id | userPrincipalName}/authentication/qrCodePinMethod/standardQRCode`
  
  
  {
      "startDateTime": "2024-10-30T12:00:00Z",
      "expireDateTime": "2024-12-30T12:00:00Z"
  }
  ```

- **Response**

  ```https
  HTTP/1.1 201 Created
  Location: /beta/users/aaaaaaaa-bbbb-cccc-1111-222222222222/authentication/qrCodePinMethod/standardQRCode`
  Content-type: application/json

  {
      "id": "BBBBBBBB-1C1C-2D2D-3E3E-444444444444"
      "expireDateTime": "2024-12-30T12:00:00Z",
      "startDateTime": "2024-10-30T12:00:00Z"
      "createdDateTime": "2024-10-30T12:00:00Z",
      "lastUsedDateTime": null,
       "image":
          {
    "binaryValue": "<binaryImageData>",
           "version": 1,
           "errorCorrectionLevel": "H".
           "rawContent": <binary data encoded in QR>        
    }
    }
  
Get a standard QR code:

- **Request**

  ```https
  GET https://graph.microsoft.com/beta/users/{id|UPN}/authentication/qrCodePinMethod/standardQRCode`
  ```

- **Response**

  ```https
  HTTP/1.1 200 OK
  Content-type: application/json

  {
      "id": "BBBBBBBB-1C1C-2D2D-3E3E-444444444444",
      "image": null,
      "expireDateTime": "2024-12-30T12:00:00Z",
      "startDateTime": "2024-10-30T12:00:00Z"
      "createdDateTime": "2024-10-30T12:00:00Z",
      "lastUsedDateTime": "2024-12-30T12:00:00Z"
  }

This example shows how to create a temporary QR code for a user. The user can use the existing PIN. This operation returns an error if a temporary QR code already exists for the user, or if the **expireDateTime** is more than 12 hours past the **startDateTime**. 

- **Request**

  ```https
  HTTP PATCH/users/{id | userPrincipalName}/authentication/qrCodePinMethod/temporaryQRCode`
  
  
  {
      "startDateTime": "2024-10-30T12:00:00Z",
      "expireDateTime": "2024-10-30T22:00:00Z"
  }
  ```

- **Response**

  ```https
  HTTP/1.1 201 Created
  Location: /beta/users/aaaaaaaa-bbbb-cccc-1111-222222222222/authentication/qrCodePinMethod/temporaryQRCode`
  Content-type: application/json

  {
      "id": "EEEEEEEE-4F$F-5A5A-6B6B-777777777777"
      "expireDateTime": "2024-10-30T22:00:00Z",
      "startDateTime": "2024-10-30T12:00:00Z"
      "createdDateTime": "2024-10-30T12:00:00Z",
      "lastUsedDateTime": null,
       "image":
          {
    "binaryValue": "<binaryImageData>",
           "version": 1,
           "errorCorrectionLevel": "H".
           "rawContent": <binary data encoded in QR>        
    }
    }

Get a temporary QR code:

- **Request**

  ```https
  GET https://graph.microsoft.com/beta/users/{id|UPN}/authentication/qrCodePinMethod/temporaryQRCode`
  ```

- **Response**

  ```https
  HTTP/1.1 200 OK
  Content-type: application/json

  {
      "id": "EEEEEEEE-4F$F-5A5A-6B6B-777777777777",
      "image": null,
      "expireDateTime": "2024-10-30T22:00:00Z",
      "startDateTime": "2024-10-30T12:00:00Z"
      "createdDateTime": "2024-10-30T12:00:00Z",
      "lastUsedDateTime": "2024-10-30T20:00:00Z"
  }

This example shows how to delete a temporary QR code for a user.  

- **Request**

  ```https
  DELETE https://graph.microsoft.com/beta/users/flokreg@contoso.com/authentication/qrCodePinMethod/temporaryQRCode`
  ```

- **Response**

  ```https
  HTTP/1.1 204 No Content
  ```

This example shows how to reset the PIN a QR code authentication method:

- **Request**

  ```https
  PATCH https://graph.microsoft.com/beta/users/flokreg@contoso.com/authentication/qrCodePinMethod/pin`
  ```

- **Response**

  ```https
  {
    "code": <PIN>,
    "forceChangePinNextSignIn": true,
    "createdDateTime": "2024-10-30T12:00:00Z",
    "updatedDateTime": null
  }
  ```

This example shows how to force a user to change their PIN for a QR code authentication method:

- **Request**

  ```https
  PATCH https://graph.microsoft.com/beta/users/flokreg@contoso.com/authentication/qrCodePinMethod/updatePin`

  {
    "currentPin": "<Old PIN>",
    "newPin": "<New PIN>"
  }
  ```

- **Response**

  ```https
  HTTP/1.1 204 No Content
  ```

## Delete the QR code authentication method for a user

You can delete the QR code authentication method for a user by using the Microsoft Entra admin center, My Staff, or Microsoft Graph API. 

### Delete the QR code authentication method for a user in the Microsoft Entra admin center

If a QR code authentication method is deleted for a user, they can no longer sign in by using that authentication method. 

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Authentication Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-administrator).

1. Go to **Users**, select a user, and click **Authentication methods**.
1. Under **Usable authentication methods**, click the ellipsis on the right side of the QR code, and click **Delete**.

   

### Delete the QR code authentication method for a user in My Staff

1. To delete the QR code auth method itself, click **Delete QR code method**.

   

1. Click **Delete** to confirm the action.

   

### Delete the QR code authentication method for a user in Microsoft Graph API

This example shows how to delete a standard QR code for a user.  

- **Request**

  ```https
  DELETE https://graph.microsoft.com/beta/users/flokreg@contoso.com/authentication/qrCodePinMethod/standardQRCode`
  ```

- **Response**

  ```https
  HTTP/1.1 204 No Content
  ```

## Sign in to Microsoft Teams or Managed Home Screen (MHS) with QR code

Microsoft Teams and Managed Home Screen (MHS) have an optimized QR code sign-in experience. An Authentication Policy Administrator needs to configure Intune or another mobile device management (MDM) solution to enable the QR code authentication method for mobile devices. 

### Enable sign-in with a QR code in Teams or MHS
When configuring with Intune, assign Microsoft Authenticator as a required app for all devices you want to add QR code authentication for.

| Platform | MDM app config key    | Value | Configuration location |
|----------|-----------------------|-------|------------------------|
| iOS      | preferred_auth_config | qrpin | Device management profile, which configures a single sign-on (SSO) extension |
| Android  | preferred_auth_config | qrpin | Microsoft Authenticator |

> [!Note] 
> MHS is only available on Android devices.

### QR code authentication Teams sign-in experience 

Users need to [download Teams](https://aka.ms/teamsmobiledownload). The following table lists the minimum Teams version for mobile operating systems. For more information about Teams versions, see [Version update history for the new and classic Microsoft Teams app](https://learn.microsoft.com/en-us/officeupdates/teams-app-versioning).

|   Mobile OS    |  Release date   |           Teams version            |
|----------------|-----------------|------------------------------------|
| iOS and iPadOS | July 21, 2024   | 6.13.1 (1.0.0.77.2024132501)       |
| Android        | August 08, 2024 | 1416/1.0.0.2024143204 (2024143204) |

Users can follow these steps to sign in with a QR code in Teams:

1. Click **Scan QR code** in Microsoft Teams.
1. Scan the QR code. Give consent if you're asked for camera permission.
1. Enter your PIN.
1. You're now signed in to the app.

   

1. When you sign in with a temporary PIN, you need to change it. 

   

## QR code authentication web sign-in experience (login.microsoftonline.com)

1. Click **More sign-in options** > **Sign in to an organization** > **Sign in with QR code**.
1. Allow the camera when prompted > scan the QR code > enter your PIN > you're successfully signed in.

   

## Add security with QR code authentication using Conditional Access policies

Restrict the QR code authentication method to only frontline workers, compliant, and shared devices. This section covers how to create policies that restrict QR code authentication method to only frontline workers and shared devices.

### Restrict QR code authentication to frontline workers  

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least an [Authentication Policy Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#authentication-policy-administrator).
1. Browse to **Entra ID** > **Authentication methods** > **QR code** > **Enable and target**.
1. Click **Add target** > select a group that only includes frontline workers, such as **Frontline workers** in the following screenshot. This group selection restricts enablement of the QR code authentication method only to frontline workers added to the **Frontline workers** group. 

   

### Restrict QR code authentication to shared devices 

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator). 
1. Click **Conditional Access** > **Authentication strengths** > **New authentication strength**.

   

1. Create a custom authentication strength Conditional Access policy. Select authentication **QR code**.  

1. Create a Conditional Access policy that requires shared devices be marked as compliant with policies from Intune or another MDM solution. This policy makes sure that frontline workers can access only specific resources from a compliant, shared device that they signed into with a QR code.
   
   1. Under **Users or workload identities** > **Include** > select **Users and groups**, and choose your **Frontline workers** frontline worker group. 
   1. Under **Target resources** > **Include** > select specific resources that frontline workers can access.
   1. Under **Conditions**, click **Filter for devices**, set **Configure** to **Yes**.
   1. Click **Include filtered devices from policy**.
   1. For **Property**, select **ProfileType**.
   1. For **Operator**, select **Equals**.
   1. For **Value**, select **Shared**.  

      
   
   1. Under **Access controls** > **Grant** > select **Require device to be marked as compliant**, and click **Select**.  
   1. Click **Create**.

## Related content

- [Authentication methods in Microsoft Entra ID - QR code authentication method](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-qr-code)
- [Manage your users with My Staff](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/my-staff-configure)
- [What authentication and verification methods are available in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/authentication/overview-authentication)

[create-azure-ad-tenant]: https://learn.microsoft.com/en-us/entra/fundamentals/sign-up-organization
[associate-azure-ad-tenant]: https://learn.microsoft.com/en-us/entra/fundamentals/how-subscriptions-associated-directory

[m365-firstline-workers-licensing]: https://www.microsoft.com/licensing/news/m365-firstline-workers
[azuread-licensing]: https://azure.microsoft.com/pricing/details/active-directory/
[ems-licensing]: https://www.microsoft.com/microsoft-365/enterprise-mobility-security/compare-plans-and-pricing
[m365-licensing]: https://www.microsoft.com/microsoft-365/compare-microsoft-365-enterprise-plans
[o365-f1]: https://www.microsoft.com/microsoft-365/business/office-365-f1?market=af
[o365-f3]: https://www.microsoft.com/microsoft-365/business/office-365-f3?activetab=pivot%3aoverviewtab
