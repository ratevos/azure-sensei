# EDR and antivirus coexistence with Global Secure Access client

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-edr-antivirus-coexistence  
> Microsoft doc last updated: 03/28/2025


Running antivirus solutions such as Microsoft Defender for Endpoint side by side with the Global Secure Access client can affect system performance. If your system experiences [high CPU usage or performance issues](https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues), exclude Global Secure Access client processes from your antivirus solution.

## Configuration overview

In your antivirus solution, configure exclusions and bypasses for all Global Secure Access client processes:

- `C:\Program Files\Global Secure Access Client\GlobalSecureAccessClientManagerService.exe`
- `C:\Program Files\Global Secure Access Client\GlobalSecureAccessEngineService.exe`
- `C:\Program Files\Global Secure Access Client\GlobalSecureAccessETLController.exe`
- `C:\Program Files\Global Secure Access Client\GlobalSecureAccessTunnelingService.exe`
- `C:\Program Files\Global Secure Access Client\TrayApp\GlobalSecureAccessClient.exe`
- `C:\Program Files\Global Secure Access Client\PolicyService\GlobalSecureAccessPolicyRetrieverService.exe`
- `C:\Program Files\Global Secure Access Client\LogsCollector\LogsCollector.exe`
- `C:\Program Files\Global Secure Access Client\AuthenticationRunner\GlobalSecureAccessAuthenticationRunner.exe`
- `C:\Program Files\Global Secure Access Client\AdvancedDiagnostics\GlobalSecureAccessClientAdvancedDiagnostics.exe`

To exclude these processes from Microsoft Defender for Endpoint, see [Configure custom exclusions for Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/configure-exclusions-microsoft-defender-antivirus).

## Next steps

-   Install the Windows client: [The Global Secure Access Client for Windows - Global Secure Access \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-install-windows-client)
-   Install the macOS client: [The Global Secure Access Client for macOS - Global Secure Access \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-install-macos-client)
-   Install the Android client: [The Global Secure Access Client for Android - Global Secure Access \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-install-android-client)
-   Install the iOS client: [The Global Secure Access Client for iOS (Preview) - Global Secure Access \| Microsoft Learn](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-install-ios-client)
