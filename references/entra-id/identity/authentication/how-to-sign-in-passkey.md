# Sign in with a synced passkey (FIDO2)

> Source: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-sign-in-passkey  
> Microsoft doc last updated: 07/05/2026


This article describes how to sign in to your work or school account with a synced passkey.

Your passkey can be synced to the same device where you want to sign in, or it can be synced to another device.

- [Use a passkey from the same device](#use-a-passkey-from-the-same-device)
- [Use a passkey from another device](#use-a-passkey-from-another-device)

## Use a passkey from the same device

1. Select **Sign in** for a Microsoft application or website such as the [Azure portal](https://ms.portal.azure.com/).

1. If you most recently used a passkey to sign in, you're automatically prompted to sign in with a passkey. Choose your account.

    

    Otherwise, you can enter your username and select **Next** to sign in.

    

1. Complete multifactor authentication (MFA).

1. You're signed in with your work or school account.

## Use a passkey from another device

1. Select **Sign in** for a Microsoft application or website such as the [Azure portal](https://ms.portal.azure.com/).

1. In Microsoft Edge, right-click where you enter your name, select **Use passkey from another device** > **Use a phone, tablet or security key**.

    

    In Google Chrome, select where you enter your name, then select **Use passkey from another device**.

    

    You can also click **Sign in**, select **Sign-in options** > **Face, fingerprint, PIN or security key**.

    

1. Select **iPhone, iPad, or Android device**. The other sign-in options that are shown vary depending on your account and device.

    

1. The device where you want to sign in shows a QR code. Scan the QR code with the other device that has your passkey.

    

1. On iOS, select **Sign in with passkey**. On Android, select **Use passkey to sign in**.

1. Bluetooth and an internet connection are required for this step and must be enabled on both devices. The device where you want to sign in shows this screen:

    

1. Complete multifactor authentication (MFA).

1. You're signed in with the synced passkey for your work or school account.

## Known issues

Review the following known issues to avoid problems with synced passkey sign-in.

### Bluetooth must be enabled on both devices for cross-device authentication

If you're signing in by using a different mobile device, Bluetooth must be enabled on the device you're trying to sign in on and the mobile device with the passkey.

Some organizations restrict Bluetooth usage, which includes the use of passkeys. In such cases, organizations can allow passkeys by permitting Bluetooth pairing exclusively with passkey-enabled FIDO2 authenticators. For more information, see [Passkeys in Bluetooth-restricted environments](https://learn.microsoft.com/en-us/windows/security/identity-protection/passkeys/?tabs=intune#passkeys-in-bluetooth-restricted-environments).

### Orphaned passkey

An orphaned passkey occurs when a passkey remains on a user's device but is no longer registered with Microsoft Entra ID. This typically happens if the passkey was deleted from a user's Security info or removed due to policy changes, but the local credential wasn't cleaned up.

If you're blocked from sign-in by an orphaned passkey:

1. Remove the orphaned passkey from the device or passkey provider.
1. Re-register a new passkey after cleanup.

## Related content

- [Register a synced passkey (FIDO2)](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-register-passkey)
- [Synced passkeys in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-synced-passkeys)
- [Support for passkey (FIDO2) authentication with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-fido2-compatibility)
