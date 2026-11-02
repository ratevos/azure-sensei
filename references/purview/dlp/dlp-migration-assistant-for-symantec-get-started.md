# Get started with the Microsoft Purview Data Loss Prevention migration assistant for Symantec and Forcepoint

> Source: https://learn.microsoft.com/en-us/purview/dlp-migration-assistant-for-symantec-get-started  
> Microsoft doc last updated: 2026-06-22


This article walks you through the prerequisites and installation of the [Microsoft Purview Data Loss Prevention migration assistant](https://learn.microsoft.com/en-us/purview/dlp-migration-assistant-for-symantec-learn).

## Before you begin

If you're using the Microsoft Purview Data Loss Prevention migration assistant for the first time, ensure the following prerequisites are met:

Tip

If the application won't launch after completing all the steps in this article, refer to [Troubleshoot the DLP migration assistant](https://learn.microsoft.com/en-us/purview/dlp-migration-assistant-for-symantec-use#troubleshooting).

### 1. Have an appropriate Microsoft 365 subscription

You'll need the appropriate DLP licensing for the locations that the migrated policies are scoped to. Check the [DLP licensing requirements](https://aka.ms/dlplicensing).

### 2. Have appropriate user role and privileges

You need to have either the *Global Administrator or Compliance Administrator* role to be able to use the migration assistant.

Important

Microsoft recommends that you use roles with the fewest permissions. This helps improve security for your organization. Global Administrator is a highly privileged role that should only be used in scenarios where a lesser privileged role can't be used.

### 3. Check your Operating System

You can only install and run the migration assistant on these operating systems:

- Windows 11,10,8.1,7
- Windows Vista
- Windows Server 2008+
- Windows Server 2003 (excluding IA-64)

### 4. Install PowerShell

You must have PowerShell v7.2.6 or higher installed on the host machine. [Download Powershell-7.2.6-win-x64.msi core on your machine](https://github.com/PowerShell/PowerShell/releases/download/v7.2.6/PowerShell-7.2.6-win-x64.msi).

### 5. Install .NET

You must have .NET desktop runtime v6.0.13 or higher installed on the host machine. [Download .NET 6.0 Desktop Runtime (v6.0.13) - Windows x64 Installer (microsoft.com)](https://dotnet.microsoft.com/download/dotnet/thank-you/runtime-desktop-6.0.13-windows-x64-installer?cid=getdotnetcore).

### Export DLP policies

Before you begin the migration process, you need to export your DLP policies from your current DLP solution.

#### Symantec DLP

You need to export your Symantec DLP policies as XML files from Symantec DLP. Export the policies using the [Symantec DLP policy export procedures](https://go.microsoft.com/fwlink/?linkid=2221525).

#### Forcepoint DLP

You need to export your Forcepoint DLP policies using the backup capability from Forcepoint DLP. Export the policy backup using the [Forcepoint DLP policy backup procedures](https://go.microsoft.com/fwlink/?linkid=2272783).

## Installation steps

Follow these steps to install the Microsoft Purview Data Loss Prevention migration assistant for Symantec:

1. Download and launch the **[Microsoft Purview Data Loss Prevention migration assistant](https://aka.ms/DLPMigrationAssistant)** file.
2. The following dialog box will open. Select **Next**.
3. Review the End-User License Agreement.
4. After reviewing, accept the License Agreement and select **Next**.
5. Select the location where you want to install the migration assistant and select **Next**.
6. Once installer is ready, select **Install** to begin installation.
7. Wait while the migration assistant is being installed.
8. Once migration assistant is installed, select **Finish** and close the dialog box.
