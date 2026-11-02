# Protect enterprise generative AI apps with prompt injection protection

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-ai-prompt-injection-protection  
> Microsoft doc last updated: 08/28/2026


Prompt injection attacks pose a significant risk for generative AI apps. Bad actors craft malicious input to make a large language model (LLM) ignore instructions, expose sensitive data, perform unintended actions, or generate harmful content.

AI Gateway, part of Microsoft's Security Service Edge (SSE) solution, safeguards generative AI applications, agents, and language models. The Prompt Injection Protection capability provides real-time protection against malicious prompt injection attacks, a top risk for LLMs. By enforcing guardrails at the network level, Prompt Injection Protection ensures consistent security across all generative AI applications without the need for code changes.

Prompt Injection Protection:
- Blocks adversarial prompts and jailbreak attempts before they reach AI models.
- Prevents unauthorized actions and sensitive data exfiltration.
- Works across any device, browser, or application for uniform enforcement.

## High-level architecture

## Prerequisites

To complete the steps in this process, you must have the following prerequisites in place:
- A valid [Microsoft Entra Internet Access license](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access#licensing-overview). If needed, you can [purchase licenses or get trial licenses](https://aka.ms/azureadlicense).
- One or more devices or virtual machines running Windows that are either Microsoft Entra joined or hybrid joined to your organization's Microsoft Entra ID.
- To configure Global Secure Access settings, you need the [Global Secure Access Administrator role](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-role-based-permissions#global-secure-access-administrator).
- To configure Conditional Access policies, you need the [Conditional Access Administrator role](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-role-based-permissions#conditional-access-administrator).

## Initial configuration

To configure Prompt Injection Protection for your organization, complete the following steps:
1. [Enable the Internet Access traffic forwarding profile](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-internet-access-profile#enable-the-internet-access-traffic-forwarding-profile) and configure the appropriate user assignments.
1. Configure TLS inspection with either a [Microsoft-managed certificate](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-transport-layer-security-settings-managed-certificate) or [your own certificate](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-transport-layer-security-settings), and then configure [TLS inspection policies](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-transport-layer-security).
1. Install and configure the Global Secure Access client on user devices. Follow the steps in [Install the Global Secure Access client for Microsoft Windows](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-install-windows-client).
    > [!IMPORTANT]
    > Before you continue, test and ensure your client’s internet traffic is routed through the Global Secure Access service.

## Create a new prompt policy to scan prompts

To create new prompt policies for Prompt Injection Protection:
1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a [Global Secure Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator).
1. Browse to **Global Secure Access** > **Secure** > **Prompt policies**.
1. Select **Create policy**.
1. On the **Basics** tab, enter a **Name** and **Description** for the policy.
1. Select **Next**.
1. On the **Rules** tab, select **Add rule**.
1. On the **Prompt rule** page:
    1. Enter or select a **Rule Name**, **Description**, **Priority**, and **Status**.
    1. Set **Action** to **Block** to block malicious prompts.
    
1. Select **+ Conversation scheme** to choose the target LLMs for your enterprise generative AI.
1. From the **Type** menu, select the language model that matches your app. 
1. If the language model isn't on the list:
    1. Select **Custom**.
    1. Enter the **URL** of the service endpoint where the prompts are sent.
    1. Enter the **JSON path** for the prompt location in the request body.
1. Select **Add** to add the Conversation scheme. You can add multiple schemes.
1. Select **Next**.
1. To create the prompt policy, select **Create**.

## Link the prompt policy to your security profile

After you create the Prompt Injection Protection prompt policy, link it to a new or existing security profile.
1. Browse to **Global Secure Access** > **Secure** > **Security profiles**.
1. Select or create the security profile you want to link the prompt policy to.
1. Select the **Link policies** tab.
1. Select **+ Link a policy** > **Existing prompt policy**.
1. Select the Prompt Injection Protection prompt policy you created earlier.
1. To link the Prompt Injection Protection prompt policy, select **Add**.

## Create a Conditional Access policy

To create a Conditional Access policy:
1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#conditional-access-administrator).
1. Browse to **Entra ID** > **Conditional Access**.
1. Select **Create new policy**.
1. Enter a name for your policy.
1. Select **Users** to specify the users or groups that the policy applies to.
1. Set the **Target resources** to **All internet resources with Global Secure Access**.
1. Configure the **Network**, **Conditions**, and **Grant** settings as needed.
1. For **Session**, select **Use Global Secure Access Security Profile** and choose the security profile you created earlier.
1. Select **Create** to create the Conditional Access policy.

For more information, see [Create a Conditional Access policy targeting Global Secure Access internet traffic](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-microsoft-profile#create-a-conditional-access-policy-targeting-global-secure-access-internet-traffic).

## Generative AI models
The following sections list more details about the AI models that work with Prompt Injection Protection.

### Top supported generative AI models
Prompt Injection Protection is preconfigured with custom extractors for the following models: ChatGPT, Claude, Cohere, Deepseek, Gemini, Grok, Meta AI, Mistral, Perplexity, Pi, and Qwen.

### Custom model support
You can protect any custom JSON-based LLM or GenAI app by configuring a custom type model with a URL and JSON path.

### Rate limits
- The system applies rate limits when scanning requests for specified conversation schemes.
- When the system reaches the rate limit, it blocks subsequent requests.
- To optimize the performance for custom LLMs, specify the exact URL and JSON path for each scheme.

## Known limitations

- Prompt Injection Protection currently supports only text prompts. It doesn't support files.
- Prompt Injection Protection supports only JSON-based generative AI apps.
- Prompt Injection Protection supports prompts up to 64,000 characters. Anything longer is truncated.

## Related content

- [Global Secure Access traffic forwarding profiles](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding)
- [Create content policies for network content filtering](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-network-content-filtering)
- [Apply Conditional Access policies to Global Secure Access traffic](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-target-resource-microsoft-profile)
- [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)
