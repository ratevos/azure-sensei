# Microsoft Entra Connect Health instructions data retrieval

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-health-data-retrieval  
> Microsoft doc last updated: 09/10/2026


This document describes how to use Microsoft Entra Connect to retrieve data from Microsoft Entra Connect Health.

> [!NOTE]
> This article provides steps about how to delete personal data from the device or service and can be used to support your obligations under the GDPR. For general information about GDPR, see the [GDPR section of the Microsoft Trust Center](https://www.microsoft.com/trust-center/privacy/gdpr-overview) and the [GDPR section of the Service Trust portal](https://servicetrust.microsoft.com/ViewPage/GDPRGetStarted).

## Retrieve email addresses configured for health alerts

To retrieve the email addresses for all of your users that are configured in Microsoft Entra Connect Health to receive alerts, use the following steps.

1. Open [Microsoft Entra Connect Health](https://aka.ms/aadconnecthealth).
2. Select **Sync errors**.
3. Select **Notification settings** on the command bar.
4. In the notification settings panel, review whether Global Administrators receive notifications and the addresses listed under the custom email recipients section.
 

## Retrieve all sync errors

To retrieve a list of all sync errors, use the following steps.

1. Open [Microsoft Entra Connect Health](https://aka.ms/aadconnecthealth), and then select **Sync errors**.
2. Select **Export** on the command bar. The browser downloads a CSV file that contains the recorded sync errors.

## Next Steps
* [Microsoft Entra Connect Health](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect)
* [Microsoft Entra Connect Health Agent Installation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-health-agent-install)
* [Microsoft Entra Connect Health Operations](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-health-operations)
* [Microsoft Entra Connect Health FAQ](reference-connect-health-faq.yml)
* [Microsoft Entra Connect Health Version History](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-health-version-history)
