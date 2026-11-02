# Learn about Microsoft Purview Network Data Security

> Source: https://learn.microsoft.com/en-us/purview/dlp-network-data-security-learn  
> Microsoft doc last updated: 2025-12-08


Microsoft Purview network data security helps organizations monitor, classify, and apply protections to unmanaged and untrusted cloud app traffic, including generative AI apps. Purview provides these capabilities through integrations with one or more secure access service edge (SASE) or secure browser solutions:

- **Microsoft Entra Global Secure Access**: To learn how to configure content policies that integrate with Purview, see [Create a content policy to filter network content](https://learn.microsoft.com/en-us/en-us/entra/global-secure-access/how-to-network-content-filtering).
- **Non-Microsoft SASE and secure browser solutions** (general availability or preview, depending on the integration): Find these solutions in the [Security Store in Microsoft Purview Data Loss Prevention](https://purview.microsoft.com/datalossprevention/securitystore).

Network data security utilizes the same classifiers already configured in other Microsoft Purview policies, extending discovery and protection to the network layer through [collection policies](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview) for data discovery, [data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) for protection, or both, depending on your organization's needs.

With network data security, you can identify, block, and alert on sensitive content that's shared through these interactions:

- Interactions with generative AI through browsers, apps, and add-ins, such as ChatGPT, Gemini, and Claude.
- Files uploaded to unsanctioned cloud storage providers, including Dropbox, Box, and Google Drive.
- Emails and file attachments shared with cloud email providers, such as Gmail.
- Form submissions through online form services, including Google Forms.
- Social media posts on common services like Facebook and X.

## Before you begin

If you're new to Microsoft Purview collection policies, Microsoft Purview pay-as-you-go billing models, or Microsoft Purview DLP, you should familiarize yourself with the information in these articles:

- [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview)
- [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp#learn-about-data-loss-prevention)
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models#learn-about-microsoft-purview-billing-models)
- [Get started with activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer#get-started-with-activity-explorer)

### Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

- **Network data security with Microsoft Entra Global Secure Access** requires **one** of the following license combinations:

    - Microsoft 365 E7 per-seat licenses
    - Purview E5 (or equivalent) per-seat licenses *and* Entra Internet Access (or equivalent) licenses
- **Network data security with non-Microsoft SASE and secure browser solutions** requires:

    - Purview E5 (or equivalent) per-seat licenses *and* the Microsoft Purview pay-as-you-go billing model. [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models)

Note

You must configure pay-as-you-go for your Microsoft 365 tenant to use Purview network data security with non-Microsoft SASE and secure browser solutions. For information on setting up the pay-as-you-go billing model, see [Enable Microsoft Purview pay-as-you-go features for new customers](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement#enable-microsoft-purview-pay-as-you-go-features-for-new-customers).

Pay-as-you-go is not required to be set up for integration with Microsoft Entra Global Secure Access.

## How network data security works

From a broad perspective, the Microsoft Purview network data security solution combines two components:

### Network security solution

The network data security solution integrates secure access service edge (SASE) and non-Microsoft secure browser solutions directly into Microsoft Purview. The integrated solutions monitor network traffic and send the data to Microsoft Purview for classification and policy evaluation. When you apply protections via the use of DLP policies, the communication between the integrated solution and Microsoft Purview is in real time. If you are using network data security for monitoring only via collection policies, the communication is asynchronous.

For more information on which integrations are supported, see the [Security Store in Microsoft Purview Data Loss Prevention](https://purview.microsoft.com/datalossprevention/securitystore).

Important

If you choose to integrate with non-Microsoft partners, they will be able to access and possibly store some policy configuration, including user identifiers. Their terms, conditions, and privacy policy will govern the usage and storage of this data.

### Microsoft Purview

You configure the integration between Microsoft Purview and the network security solution using the [Security Store](https://purview.microsoft.com/datalossprevention/securitystore). This integration establishes the bidirectional communication channel between the network security solution and Microsoft Purview.

Next, configure a [collection policy](https://learn.microsoft.com/en-us/purview/collection-policies-create-deploy-policy) or [data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) that defines the conditions, activities, and cloud apps that you want the network security solution to collect and send to Microsoft Purview.

- For more information on how to create a collection policy for network data security, see [Scenario 1 Detect sensitive data shared with unmanaged cloud apps via network](https://learn.microsoft.com/en-us/purview/collection-policies-create-deploy-policy#scenario-1-detect-sensitive-data-shared-with-unmanaged-cloud-apps-via-network).
- For more information on how to create a data loss prevention policy for network data security, see [Use Network Data Security to help prevent sharing sensitive information with unmanaged AI](https://learn.microsoft.com/en-us/purview/dlp-create-policy-ai-network-data-security)

Microsoft Purview shares the appropriate DLP and collection policy configuration with your integrated network security solution, and the solution sends any matching network data to Microsoft Purview for classification and policy evaluation. If you configure [content capture](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference#content-capture-for-ai-interactions) in the collection policy, the full conversation that happens between the user and the AI app is captured and sent to Microsoft Purview as well.

After the data is classified, it's available in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) and [activity explorer in Data Security Posture Management (DSPM)](https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about#how-to-use-data-security-posture-management). If a data loss prevention policy is matched, and you have configured alerts, they will be available in [DLP alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started).

After you configure the integration between Microsoft Purview and your network security solution, allow up to 24 hours for your policies to be distributed to the network security solution and for the first data to show up. Once the two services fully communicate with each other, it can take up to 30 minutes for data about a request from a client to a website or cloud app to appear in the audit log and activity explorer.

Important

Purview network data security policies don't apply to B2B guest users.

#### Supported network data security collection policy configuration

The Microsoft Purview side of the configuration is done via a collection policy. Here are the configuration options that are supported:

- **Conditions** - The conditions you can use in a network data security collection policy are the same as the conditions you can use in other Microsoft Purview policies. For example, you can use the **Content contains** &gt; **Sensitive information types** condition to classify sensitive items that are being shared with generative AI and other unmanaged cloud apps.
- **Activities** - Network data security supports four activities:

    - **Text sent to or shared with cloud or AI app**.
    - **File uploaded to or shared with cloud or AI app**.
    - **Text received from cloud or AI app**.
    - **File downloaded from cloud or AI app**.

Note

The activities supported may differ depending on integrated SASE solution. Check with your SASE solution provider for details on supported activities. Microsoft Entra Global Secure Access supports all supported activities.

- **Data sources**- These are the locations that the endpoint device is communicating with.
    - **Unmanaged cloud apps** - Network data security collection policies support all the sources that are in the Microsoft Defender for Cloud Apps Cloud app catalog which includes over 35,000 discoverable cloud apps.
    - **Adaptive app scopes** - all apps in multiple categories including generative AI, cloud storage, collaboration, social network, and webmail.

#### Supported network data security data loss prevention policy configuration

The Microsoft Purview side of the configuration is done via a data loss prevention policy. Here are the configuration options that are supported:

- **Data sources** - These are the locations that the endpoint device is communicating with.

    - **Unmanaged cloud apps** - Network data security collection policies support all the sources that are in the Microsoft Defender for Cloud Apps Cloud app catalog which includes over 35,000 discoverable cloud apps.
    - **Adaptive app scopes** - all apps in multiple categories including generative AI, cloud storage, collaboration, social network, and webmail.
- **Conditions** - The conditions you can use in a network data security collection policy are the same as the conditions you can use in other Microsoft Purview policies. For example, you can use the **Content contains** &gt; **Sensitive information types** condition to classify sensitive items that are being shared with generative AI and other unmanaged cloud apps.
- **Activities** - Network data security supports four activities:

    - **Text sent to or shared with cloud or AI app**.
    - **File uploaded to or shared with cloud or AI app**.
    - **Text received from cloud or AI app**.
    - **File downloaded from cloud or AI app**.
- **Actions** - Network data security supports **Audit only** and **Block** actions.

Note

The activities and actions supported may differ depending on integrated solution. Check with your solution provider for details on supported activities. Microsoft Entra Global Secure Access supports all supported activities and actions.

#### Default policy from Microsoft Purview Data Security Posture Management

[Microsoft Purview Data Security Posture Management (DSPM)](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview#microsoft-purview-data-security-and-compliance-protections-for-generative-ai-apps) offers recommendations to help monitor communications with generative AI apps. Select the recommendation **Extend insights into sensitive data in AI app interactions** to create a [one-click policy](https://learn.microsoft.com/en-us/purview/ai-microsoft-purview-considerations#one-click-policies-from-data-security-posture-management-for-ai) named **DSPM for AI - Detect sensitive info shared with AI via network**. After it's created, you can edit this default policy for network data security as you would any collection policy.

### Considerations for unmanaged cloud apps policies

Review this information when you configure policies that include unmanaged cloud apps, or when you troubleshoot unexpected policy behavior:

- When multiple catalog entries exist for the same app with differences in the entry name (for example, QwenAI and Qwen Chat), include all entries for the app to avoid unintended coverage gaps.
- Some unmanaged AI apps like ChatGPT, Runway and Meta AI might intermittently send content in encoded form or through dynamically generated endpoints, which can impact policy enforcement.
- Policies that target unmanaged apps can capture interactions from both the consumer and enterprise versions of an app when the app's URL is shared across instances (for example, ChatGPT consumer and ChatGPT enterprise).
- Inline evaluation size limits: Microsoft Purview evaluates up to 4 MB of content for uploadText and downloadText, and files up to 3 MB for uploadFile and downloadFile.

Note

The unmanaged cloud app features only apply to the consumer version of Microsoft Copilot. For more information on the enterprise version and available Purview features, see [Learn more about Microsoft Copilot Enterprise protections](https://learn.microsoft.com/en-us/en-us/copilot/microsoft-365/enterprise-data-protection).

#### Supported network protocols

All network data security integrations support classifying traffic sent and received from an endpoint device over HTTP and HTTPS protocols to websites, cloud apps, and generative AI services. Support for WebSocket protocol may differ depending on the integrated SASE or non-Microsoft secure browser solution. Check with your solution provider for details on supported protocols.

## Accessing network data security data

Data from network data security appear in [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer#get-started-with-activity-explorer), [Data Security Posture Management activity explorer events](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations#activity-explorer-events), and if alerts are enabled, [DLP alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started).

### Activity explorer

In [activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer#get-started-with-activity-explorer), you can filter events with **enforcement plane** set to *network*. This filter shows you activities that network data security policies generate.

## Billing model

Network data security uses the *request* as unit of measure for pay-as-you-go billing purposes when using non-Microsoft SASE and secure browser integrations. A request is each network call made from a device or browser to a website or API. This definition doesn't include the responses to the requests. For more information on pay-as-you-go billing for network data security, see [Other Microsoft Purview solutions that use pay-as-you-go pricing](https://learn.microsoft.com/en-us/purview/purview-billing-models#other-microsoft-purview-solutions-that-use-pay-as-you-go-pricing) and [Requests](https://learn.microsoft.com/en-us/purview/purview-billing-models#requests).

Here are some examples:

| Activity | Data type | Example |
| --- | --- | --- |
| Text sent to or shared with cloud or AI app | Human readable strings transmitted inline | - submitting a form with textual information - sending raw text or a prompt to a generative AI - the body of an email - sending JSON data to an API |
| File uploaded to or shared with cloud or AI app | Byte streams, including text based file, binary files, txt files, source code, documents, images, videos, .exe's, .pdf's, archive files | - Uploading a profile picture to social media - sending a document or .pdf file as an email attachment - sharing a document with generative AI - transferring a document or .zip files to a cloud storage solution |
