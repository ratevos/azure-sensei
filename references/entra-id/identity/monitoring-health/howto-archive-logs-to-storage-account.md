# How to archive activity logs to a storage account

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-archive-logs-to-storage-account  
> Microsoft doc last updated: 11/08/2024


If you need to store Microsoft Entra activity logs for longer than the [default retention period](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-reports-data-retention), you can archive your logs to a storage account. We recommend that you use a general storage account and not a Blob storage account. For storage pricing information, see the [Azure Storage pricing calculator](https://azure.microsoft.com/pricing/calculator/?service=storage).

## Prerequisites

To use this feature, you need:

* An Azure subscription. If you don't have an Azure subscription, you can [sign up for a free trial](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
* An Azure storage account you have `ListKeys` permissions for. Learn how to [create a storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create).
* A user who's a [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator) for the Microsoft Entra tenant.

## Archive logs to an Azure storage account

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator).

1. Browse to **Entra ID** > **Monitoring & health** > **Diagnostic settings**. You can also select **Export Settings** from either the **Audit Logs** or **Sign-ins** page.

1. Select **+ Add diagnostic setting** to create a new integration or select **Edit setting** for an existing integration.

1. Enter a **Diagnostic setting name**. If you're editing an existing integration, you can't change the name.

1. Select the log categories that you want to stream.

6. Under **Destination Details** select the **Archive to a storage account** check box.

7. Select the appropriate **Subscription** and **Storage account** from the menus.

    

  > [!NOTE]
  > The Diagnostic settings storage retention feature has been deprecated. If you're editing a diagnostic setting created when the retention option was available, those fields are still visible. For details on this change, see [**Migrate from diagnostic settings storage retention to Azure Storage lifecycle management**](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/migrate-to-azure-storage-lifecycle-policy).
 
8. Select **Save** to save the setting.

9. Close the window to return to the diagnostic settings page.

## Related content

* [Manually download activity logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-download-logs)
* [Integrate activity logs with Azure Monitor logs](howto-integrate-activity-logs-with-azure-monitor-logs.yml)
* [Stream logs to an event hub](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-stream-logs-to-event-hub)
