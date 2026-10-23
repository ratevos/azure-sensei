# Microsoft Entra Connect: Features in preview

> Source: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-preview  
> Microsoft doc last updated: 04/09/2025

This topic describes how to use features currently in preview.

<a name='azure-ad-connect-sync-v2-endpoint-api'></a>

## Microsoft Entra Connect Sync V2 endpoint API

We've deployed a new endpoint (API) for Microsoft Entra Connect that improves the synchronization service operations performance for Microsoft Entra ID. By utilizing the new V2 endpoint, you'll experience noticeable performance gains on export and import to Microsoft Entra ID. This new endpoint also supports syncing groups with up to 250k members. Using this endpoint also allows you to write back Microsoft 365 unified groups, with no maximum membership limit, to your on-premises Active Directory, when group writeback is enabled. For more information, see [Microsoft Entra Connect Sync V2 endpoint API](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-endpoint-api-v2).

## User writeback
> [!IMPORTANT]
> The user writeback preview feature was removed in the August 2015 update to Microsoft Entra Connect. If you have enabled it, then you should disable this feature.
>
>

## Next steps
Continue your [Custom installation of Microsoft Entra Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom).

Learn more about [Integrating your on-premises identities with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/hybrid/whatis-hybrid-identity).
