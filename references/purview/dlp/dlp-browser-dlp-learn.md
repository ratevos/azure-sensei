# Learn about Data Loss Prevention for Cloud Apps in Edge for Business

> Source: https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn  
> Microsoft doc last updated: 2025-07-15


Microsoft Purview Data Loss Prevention (DLP) monitoring and protection are built right into the [Microsoft Edge for Business](https://www.microsoft.com/en-us/edge/business/download?msockid=1d62cf230de86f161a9bdcf60cc56e14&amp;form=MA13FJ) browser. You don't need to onboard the device into Microsoft Purview. This integration helps you stop users from sharing sensitive information to and from cloud apps by using Edge for Business.

## Before you begin

If you're new to Microsoft Purview collection policies or Microsoft Purview DLP, familiarize yourself with the information in these articles:

- [Collection policies](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference)
- [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
- [Get started with activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer)

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## Permissions

Permissions to [create and deploy Microsoft Purview DLP policies are found here](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions).

You also need permissions for prerequisites and configurations outside of Microsoft Purview. For more information on required permissions, see Supported cloud apps.

## Managed devices

You can protect Windows 10 and Windows 11 devices that are [managed by Microsoft Intune](https://learn.microsoft.com/en-us/en-us/intune/intune-service/fundamentals/manage-devices). Users must sign in to the device using their work or school account.

On these devices, Edge for Business connects directly with Microsoft Purview and Microsoft Edge services to get policy updates and apply protections. [Microsoft Edge configuration policies](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration) block users from using protected unmanaged cloud apps in unprotected browsers. If users try to access an unmanaged app in an unprotected browser, they're blocked and must use Edge for Business.

Microsoft Purview DLP policies can [help prevent sharing via Edge for Business from managed devices to unmanaged AI apps](https://learn.microsoft.com/en-us/purview/dlp-create-policy-block-to-ai-via-edge#help-prevent-sharing-via-microsoft-edge-for-business-to-unmanaged-ai-apps-from-managed-devices), and [Microsoft Purview collection policies](https://learn.microsoft.com/en-us/en-us/purview/collection-policies-policy-reference) can be applied to interactions with unmanaged AI apps from managed devices. Policies targeting unmanaged apps on managed devices apply across all Edge browser profiles (work profile, personal profile and InPrivate).

## Unmanaged devices

Unmanaged devices aren’t connected to Intune or joined to your organization using Microsoft Entra. Users don’t sign into the device with their work or school account. Instead, they sign into their Edge for Business work profile to access organization managed apps from their unmanaged device.

Edge for Business applies DLP policies for unmanaged devices to the work profile identity. These policies don't apply when users choose a personal or InPrivate profile, except when the [work profile used to open the InPrivate window](https://support.microsoft.com/edge/browse-inprivate-in-microsoft-edge) has a policy applied. When you target policies to managed apps on unmanaged devices, you must enforce the work profile in Edge for Business. Protections for unmanaged devices [help prevent users from sharing sensitive information with cloud apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-create-policy-prevent-cloud-sharing-from-edge-biz).

## Supported cloud apps

### Microsoft Entra connected (managed) apps

Microsoft Entra connected (managed) apps are [business apps set up for Microsoft Entra single sign-on (SSO)](https://learn.microsoft.com/en-us/en-us/entra/identity/enterprise-apps/add-application-portal-setup-sso). Policies apply when users access them in Edge for Business by using work or school account credentials. Policies for managed apps in Edge for Business are supported on unmanaged devices and managed devices and policies apply only in Edge work profile.

To activate policies that apply to managed apps, you need additional permissions for [Conditional Access administration](https://learn.microsoft.com/en-us/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator) and [Microsoft Defender for Edge In-Browser protection](https://learn.microsoft.com/en-us/en-us/defender-office-365/mdo-portal-permissions#microsoft-entra-roles-in-the-microsoft-defender-portal).

### Unmanaged cloud apps

Your organization doesn't manage these apps. Users access them without signing in by using their Microsoft work or school account. You can use policies for unmanaged cloud apps in Edge for Business on Intune-managed devices and the policies apply across all Edge browser profiles (work profile, personal profile and InPrivate).

Important

Microsoft Purview browser and network data security policies don't apply to B2B guest users.

To fully activate DLP policies for unmanaged apps, additional groups and policies are required outside of Purview. This behavior is automated and triggered by the admin action in Purview. After you save your first Purview collection or DLP policy targeting unmanaged apps in Edge for Business, the [Microsoft Edge management service](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-management-service) automatically creates and manages the required configurations and policies outside of Purview. To learn more, see [Automatic activation of your Microsoft Purview DLP policy in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration).

To fully activate your Purview policies in Edge for Business, the admin needs these permissions:

- [Directory Reader](https://learn.microsoft.com/en-us/en-us/entra/identity/role-based-access-control/permissions-reference#directory-readers)
- [Microsoft Edge administration](https://learn.microsoft.com/en-us/en-us/entra/identity/role-based-access-control/permissions-reference#edge)
- [Microsoft Intune administration](https://learn.microsoft.com/en-us/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator)

Browser policies in Edge for Business support these unmanaged apps:

- Adobe Firefly
- CapCut
- ChatGPT (consumer)
- Cohere
- DeepAI
- DeepSeek
- Google Gemini
- Grok (xAI)
- Meta AI
- Microsoft Copilot 365 Chat
- Notion AI
- Otter.ai
- Perplexity AI
- QwenAI
- Qwen Chat
- Runway
- Textcortex
- Textcortex Zenochat
- You (You.com)

Note

The unmanaged cloud app features apply to the consumer versions of Microsoft 365 Copilot and ChatGPT. For more information on the enterprise versions of these apps and available Purview features see, [Learn more about Microsoft 365 Copilot Enterprise protections](https://learn.microsoft.com/en-us/en-us/copilot/microsoft-365/enterprise-data-protection) and [Use Microsoft Purview to manage data security & compliance for ChatGPT Enterprise](https://learn.microsoft.com/en-us/en-us/purview/ai-chatgpt-enterprise).

## Supported browsers

DLP policies for cloud apps in the browser work directly in Edge for Business.

### Edge for Business

These features are available in the two latest stable versions of Edge for Business, starting with version 144. For more information on Edge for Business versions, see [Microsoft Edge Releases](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-release-schedule#microsoft-edge-releases).

Important

Microsoft Purview browser data security policies don't apply to B2B guest users.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Activities you can monitor and take action on

You can audit and manage these activities on sensitive items in the browser:

| Activity | Device Type | App Type | Supported Policy Actions |
| --- | --- | --- | --- |
| Upload text | Managed | Unmanaged | allow, block, both actions audited |
| Upload file | Managed, Unmanaged | Managed, Unmanaged | allow, block, both actions audited |
| Download file | Managed, Unmanaged | Managed | allow, block, both actions audited |
| Cut/copy data | Managed, Unmanaged | Managed | allow, block, both actions audited |
| Paste data | Managed, Unmanaged | Managed | allow, block, both actions audited |
| Print data | Managed, Unmanaged | Managed | allow, block, both actions audited |
| Protected clipboard (Preview) | Managed, Unmanaged | Managed | [See Microsoft Edge Protected Clipboard (preview)](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-management-protected-clipboard) |
| Screen capture (Preview) | Managed, Unmanaged | Managed | [See Microsoft Edge Protected Clipboard (preview)](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-management-protected-clipboard) |

Some activities have limitations:

- Cut/copy data, paste data, and print data activities can only be used with the managed or unmanaged devices condition.
- Download file activity isn't supported for apps that don't follow Microsoft Edge for Business's download pipeline.

Note

Policy sync status displays N/A for DLP policies that use the built-in protections in Edge for Business. These policies use a different activation and delivery path than other DLP locations and don’t report through the same policy sync status field. Activation or configuration failures are surfaced in the Microsoft Purview portal.

## Policies for managed app interactions

DLP policies that target managed apps in the browser apply to Edge for Business in Windows 10/11 and macOS desktop devices when the user signs in to their Edge for Business work profile.

Edge for Business automatically disables developer tools and blocks the apps from opening in native clients when policies apply to managed apps (in both audit and block modes).

To activate protections in the Edge for Business work profile for managed apps:

- Onboard apps to [Conditional Access app control](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/proxy-deployment-featured-idp).
- [Import user groups from connected apps](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/user-groups). This step allows you to target Groups in your Entra Conditional Access policy and your Purview policies for managed apps in Edge for Business.
- Set up a [Microsoft Entra Conditional Access](https://learn.microsoft.com/en-us/en-us/entra/identity/conditional-access/concept-conditional-access-session) policy with custom session controls.
- Configure [Edge for Business in-browser protection](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/in-browser-protection).
- Create a [Microsoft Purview DLP policy that targets managed app interactions](https://learn.microsoft.com/en-us/purview/dlp-create-policy-prevent-cloud-sharing-from-edge-biz).
- (Optional) [Activate protected clipboard and screen capture prevention capabilities in the Microsoft Admin Portal settings for Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-management-protected-clipboard#gettingstarted).

For full implementation details, see [Help Prevent Users from Sharing Sensitive Info with Cloud Apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-create-policy-prevent-cloud-sharing-from-edge-biz).

Important

Protections might not apply in Edge for Business to managed apps included in a Microsoft Purview browser policy if the user is in scope for both a Microsoft Purview managed cloud app DLP policy *and* a Microsoft Defender session policy *or* Microsoft Purview endpoint DLP policy. You must remove or exclude the users from the Microsoft Defender and the endpoint DLP policies for the managed cloud apps in Edge for Business policy to apply.

When you add users to policies for the first time, the policy might not be applied right away if they're already signed in to the app. The policy applies after their token expires and they sign in again. You can [change the sign-in frequency](https://learn.microsoft.com/en-us/en-us/entra/identity/conditional-access/howto-conditional-access-session-lifetime) by using conditional access session controls to shorten the wait time.

Some known limitations in Conditional Access app control can impact Microsoft Purview policies that target managed apps in the browser. For more information, see [known limitations in Conditional Access app control](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/caac-known-issues).

### Accessing data from managed app interactions

You can view policy data and alerts in [Defender XDR investigations](https://learn.microsoft.com/en-us/en-us/defender-xdr/pilot-deploy-investigate-respond).

## Policies for unmanaged app interactions

DLP policies that target unmanaged apps in the browser apply to Microsoft Edge for Business on Windows 10 and Windows 11 desktop devices [managed by Microsoft Intune](https://learn.microsoft.com/en-us/en-us/intune/intune-service/fundamentals/manage-devices). For setup details, see [Help prevent sharing via Edge for Business to unmanaged AI apps from managed devices](https://learn.microsoft.com/en-us/purview/dlp-create-policy-block-to-ai-via-edge#help-prevent-sharing-via-microsoft-edge-for-business-to-unmanaged-ai-apps-from-managed-devices).

Important

Microsoft Purview inline protection in Microsoft Edge for Business for unmanaged apps doesn't support tenants that use multi-admin approval in Microsoft Intune. For more information, see [Multi-admin approval](https://learn.microsoft.com/en-us/en-us/intune/fundamentals/role-based-access-control/multi-admin-approval).

When you activate a Microsoft Purview DLP policy for unmanaged cloud apps, Purview automatically creates the required Microsoft Edge configuration policies and Microsoft Intune policies (outside of Purview) and assigns the included users.

If you configure the DLP policy to block, users in scope can't use unprotected browsers where the policy doesn't apply. This restriction doesn't affect their experience in Microsoft Edge for Business.

For more information, see [Activate your Microsoft Purview policy in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration).

Activating protections in Microsoft Edge for Business follows these phases:

- Create a [Microsoft Purview DLP policy targeting unmanaged app interactions](https://learn.microsoft.com/en-us/purview/dlp-create-policy-block-to-ai-via-edge#help-prevent-sharing-via-microsoft-edge-for-business-to-unmanaged-ai-apps-from-managed-devices).
- Microsoft Edge management service automatically creates the configuration policies that activate DLP policies in Microsoft Edge for Business. The configuration policies use [Microsoft Intune policies](https://learn.microsoft.com/en-us/en-us/deployedge/configure-edge-with-intune) to [activate your Microsoft Purview policies in Microsoft Edge for Business](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration).
- Create a [collection policy](https://learn.microsoft.com/en-us/en-us/purview/collection-policies-policy-reference) targeting unmanaged apps in the browser to identify additional sensitive data sharing that might be happening across your organization.

Important

If the [automatic behaviors](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration) fail to sync, Microsoft Purview shows an error message. Purview doesn’t enforce DLP and collection policies for unmanaged apps in Edge for Business until you resolve the error. An admin with the [required permissions](https://learn.microsoft.com/en-us/en-us/purview/dlp-browser-dlp-learn#unmanaged-cloud-apps) must resync to resolve the error. For more information, see [activate your Microsoft Purview policy in Microsoft Edge](https://learn.microsoft.com/en-us/en-us/deployedge/microsoft-edge-dlp-purview-configuration).

### Accessing data from unmanaged app interactions

You can view activities and audit log entries in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer), audit logs, and [Defender XDR investigations](https://learn.microsoft.com/en-us/en-us/defender-xdr/pilot-deploy-investigate-respond). In activity explorer, filter by enforcement plane set to browser. Data specific to AI apps is also visible in [DSPM for AI](https://learn.microsoft.com/en-us/purview/dspm-for-ai).

### Considerations for unmanaged cloud apps policies

Review this information when you configure policies that include unmanaged cloud apps, or when you troubleshoot unexpected policy behavior:

- When multiple catalog entries exist for the same app with differences in the entry name (for example, QwenAI and Qwen Chat), include all entries for the app to avoid unintended coverage gaps.
- Some unmanaged AI apps like ChatGPT, Runway and Meta AI might intermittently send content in encoded form or through dynamically generated endpoints, which can impact policy enforcement.
- Policies that target unmanaged apps can capture interactions from both the consumer and enterprise versions of an app when the app's URL is shared across instances (for example, ChatGPT consumer and ChatGPT enterprise).
- When you target an unmanaged cloud app in an Edge for Business browser policy, detection is based on the destination app's traffic, which isn't always exactly the same as the originating app.
- Inline evaluation size limits: Microsoft Purview evaluates up to 4 MB of content for uploadText, and files up to 3 MB for uploadFile.

### Default policies for unmanaged AI apps from Microsoft Data Security Posture Management for AI

[Microsoft Purview Data Security Posture Management for AI (DSPM for AI)](https://learn.microsoft.com/en-us/purview/dspm-for-ai) offers recommended policies to monitor and block supported unmanaged generative AI apps. Use [one-click policies in DSPM for AI](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) to apply them.

## Working with Microsoft Purview Endpoint data loss prevention

Endpoint DLP policies are prioritized over inline DLP policies for cloud apps in Edge for Business if the same user, context, and action are configured in both policies. For example, if you have an Endpoint DLP policy that blocks a file uploads, and you also have an inline policy for cloud apps in Edge for Business that monitors file uploads. the Endpoint DLP policy is prioritized and applied. For more information, see [Learn about Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about).
