# Register a synced passkey (FIDO2)

> Source: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-register-passkey  
> Microsoft doc last updated: 07/05/2026


This article shows how users can register a synced passkey (FIDO2) by using the **Passkey** flow. A synced passkey is stored in a passkey provider (such as iCloud Keychain or Google Password Manager) and syncs across the user's devices. For an overview of synced passkeys, see [Synced passkeys in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-synced-passkeys).

> [!NOTE]
> Looking to provide passkeys (FIDO2) on behalf of users? Use our [APIs](https://aka.ms/passkeyprovision).

## Prerequisites

You need to configure a password manager on your mobile device to save a synced passkey.

- On your iOS device, you need to set **Set Up Codes In** to **Passwords** to manage synced passkeys. Open **Settings** > **General** > **AutoFill & Passwords**. For **Set Up Codes In**, select **Passwords**.
- On your Android device, open **Settings** > **Security and privacy** > **More security settings** > **Passwords, passkeys, and autofill**, and then select a provider.

## Register a passkey

To register a passkey on your device, follow these steps:

1. Open a web browser and sign in to [Security info](https://mysignins.microsoft.com/security-info).
1. Sign in with multifactor authentication (MFA).
1. Tap **+ Add sign-in method**.

    

1. Tap **Passkey**.

    

1. Tap **Next**.

    

1. On iOS, tap **Next**.

    

    On Android, tap **Continue**.

    > [!NOTE]
    > The steps to enable passkey providers on Android might vary based on the make and model of your device. Search for Passkey on your device settings, or consult your device manufacturer for guidance. If your device runs Android 14 and you can't enable Authenticator as a passkey provider, we recommend that you upgrade to Android 15.

    

1. Name your passkey and tap **Next**. 

    

1. After the passkey is created, tap **Done**. 

    

1. You can see your passkey in [Security info](https://mysignins.microsoft.com/security-info). 

    

## Related content

To register a passkey on a different type of authenticator, see:

- [Register passkeys in Microsoft Authenticator](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-register-passkey-authenticator)
- [Register a passkey with a FIDO2 security key](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-register-passkey-with-security-key)
