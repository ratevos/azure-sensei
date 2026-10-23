# On-demand provisioning using cloud sync

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/on-demand-provision  
> Microsoft doc last updated: 04/09/2025


You can use cloud sync to test configuration changes by applying these changes to a single user. This on-demand provisioning helps you validate and verify that the changes made to the configuration were applied properly and are being correctly synchronized to Microsoft Entra ID.  This feature is only available in cloud sync and not Microsoft Entra Connect.

## Steps to use on-demand provisioning
To use on-demand provisioning, follow these steps:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Hybrid Identity Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#hybrid-identity-administrator).

1. Browse to **Entra ID** > **Entra Connect** > **Cloud sync**.

   
 4. Under **Configuration**, select your configuration.
 5. On the left, select **Provision on demand**.
 6. Enter the distinguished name of a user and select the **Provision** button.
 7. Once the process completes, a success screen appears with four green check marks. Any errors appear on the left side of the screen.

## Next steps

For more information, see [on-demand provisioning in cloud sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/how-to-on-demand-provision)
