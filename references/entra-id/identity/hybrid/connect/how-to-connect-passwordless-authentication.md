# Sign in to Microsoft Entra Connect Sync by using passwordless authentication

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-passwordless-authentication  
> Microsoft doc last updated: 06/15/2026


Passwordless authentication for Microsoft Entra Connect Sync lets administrators sign in with secure, modern credentials (such as FIDO2 security keys, passkeys, or Windows Hello) instead of typing a password.

This article shows you how to enable passwordless authentication methods in Microsoft Entra ID, register a credential, turn on passwordless sign-in for Microsoft Entra Connect Sync, and verify that you can sign in without a password. You can choose from the following passwordless methods:

- **FIDO2 security keys**: Insert a USB or NFC key (for example, a YubiKey), enter a PIN, and tap the key.
- **Passkeys**: Use a platform-stored credential (for example, an iCloud Keychain or Android passkey) through the system browser or a device prompt.

## Prerequisites

- A Microsoft Entra account with the **Hybrid Administrator** or **Global Administrator** role.
- A FIDO2 security key, such as a YubiKey.
- Windows Server 2022 or later.

## Enable passwordless authentication methods in Microsoft Entra ID

Before you can register a passwordless credential, enable the passkey or FIDO2 authentication method for your account in Microsoft Entra ID.

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
1. Browse to **Entra ID** > **Authentication methods** > **Policies**.
1. Select **Passkey (FIDO2)**.
1. Set the method to **Enabled**, and target **All users** or a specific group that contains your administrator account.

   

## Register a passwordless credential

After the authentication method is enabled, register the credential that you want to use to sign in. You can register a passkey, a security key, or both.

### Register a passkey

Register a passkey that's stored on your device or password manager:

1. Go to [Security info](https://mysignins.microsoft.com/security-info) and sign in with your administrator account.
1. Select **Add sign-in method**.
1. Select **Passkey**.
1. Follow the prompts to create the passkey with your device, such as Windows Hello, Face ID, Touch ID, or a synced password manager.

After registration finishes, the new passkey appears under your registered sign-in methods.

### Register a security key

Register your FIDO2 security key, such as a YubiKey:

1. Go to [Security info](https://mysignins.microsoft.com/security-info) and sign in with your administrator account.
1. Select **Add sign-in method**.
1. Select **Security key**.
1. Select **USB device**.
1. Insert your YubiKey, and then touch it when it blinks.
1. Set a PIN if you're prompted, and then touch the key again to finish registration.

## Turn on passwordless authentication for Microsoft Entra Connect Sync

To make passwordless sign-in available in the installation wizard, install Microsoft Entra Connect Sync and set a registry key.

1. Install Microsoft Entra Connect Sync. For installation steps, see [Get started with Microsoft Entra Connect Sync by using express settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-express).
1. On the server, open PowerShell and run the following command to enable passwordless authentication:

   ```powershell
   # Enable passwordless authentication
   New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Azure AD Connect" -Name "EnablePasswordlessAuth" -Value 1 -PropertyType DWORD -Force
   ```

## Sign in to Microsoft Entra Connect Sync without a password

After passwordless authentication is enabled, use your passkey or security key to sign in when you run the installer.

1. Run the Microsoft Entra Connect Sync installer. When you're prompted to sign in to Microsoft Entra ID, select **Sign-in options**.

   

1. Select **Face, fingerprint, PIN or security key**, and then complete the prompt with the passkey or security key that you registered.

   

When sign-in succeeds, you're signed in to Microsoft Entra Connect Sync without entering a password. The same steps apply whether you sign in with a passkey or a security key.

## Disable passwordless authentication

To turn off passwordless authentication and return to signing in with a username and password, set the registry value to `0`.

1. On the server, open PowerShell and run the following command to disable passwordless authentication:

   ```powershell
   # Disable passwordless authentication
   Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Azure AD Connect" -Name "EnablePasswordlessAuth" -Value 0
   ```

1. Run the Microsoft Entra Connect Sync installer again. The passwordless sign-in option is no longer available, and you can sign in with your username and password.

## Related content

- [Get started with Microsoft Entra Connect Sync by using express settings](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-express)
- [Choose the right authentication method for your Microsoft Entra hybrid identity solution](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn)
