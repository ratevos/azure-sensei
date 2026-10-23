# Register passkeys in Authenticator on Android and iOS devices

> Source: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-register-passkey-authenticator  
> Microsoft doc last updated: 07/05/2026


This article shows how to register a passkey in Microsoft Authenticator on your iOS or Android device.

## [**iOS**](#tab/iOS)

You can register by signing in to the Authenticator app directly, by using [Security info](https://aka.ms/mysecurityinfo), or from your mobile device browser or through cross-device registration by using another device, such as a laptop. Your mobile device needs to run iOS version 17 or later.

- [Use Authenticator (iOS)](#use-authenticator-ios)
- [Use Security info (iOS)](#use-security-info-ios)
- [Use WebAuthn flow (iOS)](#use-webauthn-flow-ios)

### Use Authenticator (iOS)

You can sign in to Authenticator to create a passkey in the app and get seamless single sign-on across Microsoft native apps. **This flow is the recommended way to set up a passkey in Authenticator.** If you're signed in or already have an account in Authenticator, you still need to complete these steps to add a passkey in Authenticator.

1. Download Authenticator from the App Store, and go through the privacy screens.

1. Add your account in Authenticator on your iOS device:

   :::row:::
     :::column span="3":::

     If you installed Authenticator for the first time on your device, on the **Secure Your Digital Life** screen, tap **Add work or school account**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::
   :::row:::
     :::column span="3":::

     If you installed Authenticator on your device but you didn't add an account, tap **Add account** or the **+** button, and select **Work or school account**. Then tap **Sign in**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::
   :::row:::
     :::column span="3":::

     If you already added an account in Authenticator, tap your account, and then tap **Create a passkey**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::

1. Complete multifactor authentication (MFA).

1. If necessary, tap **Settings** and set up a screen lock.

   

1. Tap **Settings** to enable Authenticator as a passkey provider.

   

1. On your iOS 18 device, go to **Settings** > **General** > **Autofill & Passwords**. On your iOS 17 device, go to **Settings** > **Passwords** > **Password Options**.

   On both operating systems, make sure that **AutoFill Passwords and Passkeys** is turned on. Under **Autofill From**, make sure that **Authenticator** is selected.

   

1. After you return to Authenticator, tap **Done** to confirm that you added Authenticator as a passkey provider. Then you can see **Passkey** added as a sign-in method for your account. Tap **Done** again to finish.

   

   Authenticator sets up passkey, passwordless, and MFA for sign-in according to your work or school account policies. Tap your account to see information, including your new passkey.

### Use Security info (iOS)

1. On the same iOS device as the Authenticator or by using another device, such as a laptop, open a web browser and sign in with MFA to [Security info](https://mysignins.microsoft.com/security-info).

1. On **Security info**, tap **+ Add sign-in method** and select **Passkey in Microsoft Authenticator**.

   

1. If you're asked to sign in with MFA, select **Next**.

1. If necessary, download Authenticator to your iOS device. You can select [Microsoft Authenticator](https://www.microsoft.com/security/mobile-authenticator-app) and scan a QR code to install Authenticator from the iOS App Store. After you download Authenticator, tap **Next**.

   

1. You're prompted to open the Authenticator app and create your passkey there. Open Authenticator and go through the privacy screens as needed.

   

1. Add your account in Authenticator on your iOS device.

   :::row:::
     :::column span="3":::

     If you installed Authenticator for the first time on your device, on the **Secure Your Digital Life** screen, tap **Add work or school account**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::
   :::row:::
     :::column span="3":::

     If you installed Authenticator on your device before but didn't add an account, tap **Add account** or the **+** button, and select **Work or school account**. Then tap **Sign in**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::
   :::row:::
     :::column span="3":::

     If you already added an account in Authenticator, tap your account, and then tap **Create a passkey**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::

1. Complete multifactor authentication (MFA).

1. If necessary, tap **Settings** and set up a screen lock.

   

1. Tap **Settings** to enable Authenticator as a passkey provider.

1. On your iOS 18 device, go to **Settings** > **General** > **Autofill & Passwords**. On your iOS 17 device, go to **Settings** > **Passwords** > **Password Options**.

   On both operating systems, make sure that **AutoFill Passwords and Passkeys** is turned on. Under **Autofill From**, make sure that **Authenticator** is selected.

   

1. After you return to Authenticator, tap **Done** to confirm that you added Authenticator as a passkey provider. Then you can see **Passkey** added as a sign-in method for your account. Tap **Done** again to finish.

   

   Authenticator sets up passkey, passwordless, and MFA for sign-in according to your work or school account policies.  

1. Return to your browser after you finish the passkey setup in Authenticator, and select **Next**.

   

1. The wizard verifies that the passkey was created in Authenticator.

   

1. After the passkey is created, select **Done**.

   

1. On **Security info**, you can see the new passkey that was added.

   

### Use WebAuthn flow (iOS)

If you can't sign in to Authenticator to register a passkey, you can register directly from **Security info** with WebAuthn. 

> [!NOTE]
> You can't register a passkey in Authenticator this way if attestation is enabled by your administrator. 

If you sign in to **Security info** on a different device, make sure both devices have internet access and Bluetooth enabled. 

If your organization restricts Bluetooth usage, you can [permit Bluetooth pairing exclusively with passkey-enabled FIDO2 authenticators](https://learn.microsoft.com/en-us/windows/security/identity-protection/passkeys/?tabs=windows%2Cintune#passkeys-in-bluetooth-restricted-environments) to allow cross-device passkey sign-in and registration.

Your organization needs to allow connectivity to endpoints in the following table to enable cross-device registration and authentication. 
Devices must be allowed to reach these URLs without interception. 
They need to be excluded from network proxies, interception, and other enterprise systems.

Platform | URL
---------|----
Android | `cable.ua5v.com`
iOS | `cable.auth.com`<br>`app-site-association.cdn-apple.com`<br>`app-site-association.networking.apple`

1. On **Security info**, when you add a passkey in Authenticator, tap **Having trouble**.

   

1. Now, tap **create your passkey a different way**.

   

1. Select **iPhone or iPad**, and go through the rest of the flow to register a passkey on the device.

   

If a user wants to revert to the original instructions and register a passkey in Authenticator through sign-in:

1. On **Security info**, when you add a passkey in Authenticator, tap **Having trouble**.
1. Now, tap **create your passkey a different way** by signing in to Authenticator.
1. Go through the rest of the flow to register a passkey on your device.

> [!NOTE]
> If you register your passkey with the Chrome browser on macOS, allow `login.microsoft.com` to access your security key or device when prompted.

### Delete your passkey in Authenticator for iOS

To remove the passkey from Authenticator, tap the account name, and then tap **Settings** > **Delete passkey**. You also need to delete your passkey from [Security info](https://mysignins.microsoft.com/security-info).

### Troubleshoot passkey registration on iOS

In some cases when you try to register a passkey, it gets stored locally in the Authenticator app but isn't registered on the authentication server. For example, the passkey provider might not be permitted or the connection might time out. If you try to register a passkey and see an error that the passkey already exists, [delete the passkey](#delete-your-passkey-in-authenticator-for-ios) that was created locally in Authenticator and retry registration.

## [**Android**](#tab/Android)

You can register by signing in to the Authenticator app directly, by using [Security info](https://aka.ms/mysecurityinfo), or from your mobile device browser or through cross-device registration by using another device, such as a laptop. Your mobile device needs to run Android version 14 or later.

- [Use Authenticator (Android)](#use-authenticator-android)
- [Use Security info (Android)](#use-security-info-android)
- [Use WebAuthn flow (Android)](#use-webauthn-flow-android)

### Use Authenticator (Android)

You can sign in to Authenticator to create a passkey in the app and get seamless single sign-on across Microsoft native apps. **This flow is the recommended way to set up a passkey in Authenticator.** If you're signed in or already have an account in Authenticator, you still need to complete these steps to add a passkey in Authenticator.

1. Download Authenticator from Google Play, open it, and go through the privacy screens.

1. Add your account in Authenticator on your Android device:

   :::row:::
     :::column span="3":::

     If you installed Authenticator for the first time on your device, on the **Secure Your Digital Life** screen, tap **Add work or school account**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::
   :::row:::
     :::column span="3":::

     If you installed Authenticator on your device before but didn't add an account, tap **Add account** or the **+** button, and select **Work or school account**. Then tap **Sign in**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::
   :::row:::
     :::column span="3":::

     If you already added an account in Authenticator, tap your account, and then tap **Create a passkey**.

     :::column-end:::
     :::column span="1":::
     
     :::column-end:::
   :::row-end:::

1. Complete multifactor authentication (MFA).

1. If necessary, tap **Settings** and set up a screen lock.

   

1. Tap **Settings** to enable Authenticator as a passkey provider.

   > [!NOTE]
   > The steps to enable passkey providers on Android might vary based on the make and model of your device. Search for **Passkey** on your device settings, or consult your device manufacturer for guidance. If your device runs Android 14 and you can't enable Authenticator as a passkey provider, we recommend that you upgrade to Android 15.

   

   1. Open **Passwords & accounts**.

      

   1. In the **Additional providers** section, make sure that **Authenticator** is selected.

      

1. After you return to Authenticator, tap **Done** to confirm that you added Authenticator as a passkey provider. Then you can see **Passkey** added as a sign-in method for your account. Tap **Done** again to finish.

   

   Authenticator sets up passkey, passwordless, and MFA for sign-in according to your work or school account policies. Tap your account to see information, including your new passkey.

### Use Security info (Android)

1. On the same Android device as Authenticator or by using another device, such as a laptop, open a web browser and sign in with MFA to [Security info](https://mysignins.microsoft.com/security-info).

1. On **Security info**, tap **+ Add sign-in method** and select **Passkey in Microsoft Authenticator**.

   

1. If prompted, tap **Next** and sign in with MFA.

1. If necessary, download Authenticator to your Android device. You can select [Microsoft Authenticator](https://www.microsoft.com/security/mobile-authenticator-app) and scan a QR code to install Authenticator from Google Play. After you download Authenticator to your Android device, select **Next**.

   

1. You're prompted to open the Authenticator app and create your passkey there.

   

1. Open Authenticator and go through the privacy screens, as needed.

   - If you installed Authenticator for the first time on your device, on the **Secure Your Digital Life** screen, tap **Add work or school account**.

      

   - If you installed Authenticator on your device before but didn't add an account, tap **Add account** or the **+** button, and select **Work or school account**. Then tap **Sign in**.

      

   - If you already added an account in Authenticator, tap your account, and then tap **Create a passkey**.

      

1. Complete multifactor authentication (MFA).

1. If necessary, tap **Settings** and set up a screen lock.

   

1. Tap **Settings** to enable Authenticator as a passkey provider.

   > [!NOTE]
   > The steps to enable passkey providers on Android might vary based on the make and model of your device. Search for **Passkey** on your device settings, or consult your device manufacturer for guidance. If your device runs Android 14 and you can't enable Authenticator as a passkey provider, we recommend that you upgrade to Android 15.

   

   1. Open **Passwords & accounts**.

      

   1. In the **Additional providers** section, make sure that **Authenticator** is selected.

      

1. After you return to Authenticator, tap **Done** to confirm that you added Authenticator as a passkey provider. Then you can see **Passkey** added as a sign-in method for your account. Tap **Done** again to finish.

   

   Authenticator sets up passkey, passwordless, and MFA for sign-in according to your work or school account policies.

1. After you finish the passkey setup in Authenticator, return to your browser where **Security info** is open. Select **Next**.
   

1. The wizard verifies that the passkey was created in Authenticator.

1. After the passkey is created, select **Done**.

   

1. On **Security info**, you can see that the new passkey was added.

   

### Use WebAuthn flow (Android)

If you can't sign in to Authenticator to register a passkey, you can register directly from **Security info** with WebAuthn. 

> [!NOTE]
> You can't register a passkey in Authenticator this way if attestation is enabled by your administrator. 

If you sign in to **Security info** on a different device, you need Bluetooth and an internet connection. Connectivity to the following two endpoints must be allowed in your organization:

- `cable.ua5v.com`
- `cable.auth.com`

If your organization restricts Bluetooth usage, you can permit Bluetooth pairing exclusively with passkey-enabled FIDO2 authenticators to allow cross-device registration of passkeys. For more information, see [Passkeys in Bluetooth-restricted environments](https://learn.microsoft.com/en-us/windows/security/identity-protection/passkeys/?tabs=windows%2Cintune#passkeys-in-bluetooth-restricted-environments).

1. On **Security info**, when you add a passkey in Authenticator, tap **Having trouble**.

   

1. Now, tap **create your passkey a different way**.

   

1. Select **Android** and go through the rest of the flow to register a passkey on your device.

   

If a user wants to revert to the original instructions and register a passkey in Authenticator through sign-in:

1. On **Security info**, when you add a passkey in Authenticator, tap **Having trouble**.
1. Now, tap **create your passkey a different way** by signing in to Authenticator.
1. Go through the rest of the flow to register a passkey on your device.

> [!NOTE]
> If you register your passkey with the Chrome browser on macOS, allow `login.microsoft.com` to access your security key or device when prompted.

## Delete your passkey in Authenticator for Android

To remove the passkey from Authenticator, tap the account name, tap **Settings**, and then tap **Delete passkey**.

In most cases, the passkey is also deleted from [Security info](https://mysignins.microsoft.com/security-info). If not, go to **Security info** and select **Delete** to remove it.

## Troubleshoot passkey registration on Android

In some cases when you try to register a passkey, it gets stored locally in the Authenticator app but isn't registered on the authentication server. For example, the passkey provider might not be permitted, or the connection might time out. If you try to register a passkey and see an error that the passkey already exists, [delete the passkey](#delete-your-passkey-in-authenticator-for-android) that was created locally in Authenticator and retry registration.

---

## Related content

- [Sign in with passkeys in Authenticator](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-sign-in-passkey-authenticator)
- [Enable and support passkeys in Authenticator](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-enable-authenticator-passkey)
