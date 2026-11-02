# View Generative AI Insights logs in Global Secure Access (preview)

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-generative-ai-insights-logs  
> Microsoft doc last updated: 06/04/2026


The Generative AI Insights logs page in Microsoft Entra Global Secure Access is the unified surface for Generative AI activity flowing through Internet Access. From a single page, you can review GenAI prompt requests sent to supported applications, Model Context Protocol (MCP) traffic between AI agents and remote MCP servers, and the user, destination, and transaction behind each event. This article walks through accessing the page, filtering events, inspecting per-event details, and exporting results.

For background on what Generative AI Insights captures and how it works, see [Generative AI Insights in Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-generative-ai-insights).

> [!IMPORTANT]
> Generative AI Insights logging is currently in preview. For more information, see the [Microsoft Entra preview terms](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

## Prerequisites

- A Microsoft Entra tenant with a Global Secure Access license. For details, see the licensing section of [What is Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access).
- One of the following roles: [Global Secure Access Administrator](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-role-based-permissions#global-secure-access-administrator) or [Global Secure Access Log Reader](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-role-based-permissions#global-secure-access-log-reader).
- Internet Access traffic forwarding enabled for the users or devices you want to monitor.
- For prompt logging and for MCP logging on end-user devices, [TLS inspection](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-transport-layer-security) must be enabled. TLS inspection isn't required for MCP traffic from Microsoft Copilot Studio agents when the [Global Secure Access integration with Copilot Studio](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-secure-web-ai-gateway-agents) is enabled.

## Open the Generative AI Insights logs page

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Global Secure Access Log Reader](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-role-based-permissions#global-secure-access-log-reader).
1. Browse to **Global Secure Access** > **Monitor** > **Generative AI Insights**.

The page displays a list of GenAI prompt and MCP events captured from your tenant, with the most recent events at the top.

## Filter events

Use the filter controls at the top of the page to narrow the view.

- **Activity**. Switch between event types. Select **Prompt** to see only GenAI prompt requests, or **MCP** to see only Model Context Protocol traffic.
- **Sub-activity**. Filter by a specific operation. For prompts, the GenAI application or interaction type. For MCP, the protocol method, such as `initialize`, `tools/list`, `tools/call`, `prompts/list`, or `prompts/get`.
- **Destination URL**. Filter by a specific GenAI service or MCP server URL to focus on activity for one destination.
- **User**. Filter by user principal name to see all GenAI prompts and MCP operations from a specific user.

You can combine filters to scope the view, for example **Activity = MCP** plus a specific destination URL to review every operation against one MCP server.

## Column reference

The Generative AI Insights logs page surfaces the following columns. The same fields are available when you stream events to Log Analytics or Microsoft Sentinel.

| Column | Description |
|---|---|
| **Create date time** | Timestamp when the event was recorded. |
| **Activity** | The traffic type — **Prompt** or **MCP**. |
| **Sub-activity** | The specific operation, such as a GenAI application name or an MCP protocol method. |
| **Content** | The payload, such as the prompt body or MCP request or response. Stored up to 65 KB per event. |
| **Destination URL** | The URL of the GenAI service or remote MCP server. The destination URL is the reliable identifier for an MCP server. |
| **Event ID** | A unique identifier for the event. For MCP, the request and response for the same operation share the same event ID. |
| **Event Type** | For MCP, indicates whether the entry is a **Request** or a **Response**. |
| **MCP Client Name** | The name reported by the MCP client. Might be missing if the client doesn't include it in the payload. |
| **MCP Server Name** | The name reported by the MCP server. Might be missing if the server doesn't include it in the payload. |
| **Session ID** | The session identifier. Multiple events can share the same session. |
| **Transaction ID** | The related Global Secure Access traffic log transaction. Use it to correlate Generative AI Insights events with [traffic logs](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-traffic-logs). |
| **User Principal Name** | The user or identity whose traffic was inspected. |

## View event details

Select any row to open the details pane for that event.

The details pane shows:

- The full **Content** of the prompt or MCP payload, including the prompt body, MCP request arguments, or MCP response payload.
- Correlation IDs — **Event ID**, **Session ID**, and **Transaction ID** — that you can use to match a request with its response and to pivot to the corresponding [traffic log](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-traffic-logs) entry.
- For MCP `initialize` responses, the server-reported tools and capabilities.

## Export logs

To export the current view for offline analysis or sharing:

1. Apply the filters you want.
1. Select **Export**.
1. Save the resulting file.

You can export up to 100,000 records per export.

For long-term retention and detection, stream Generative AI Insights events to Microsoft Sentinel or Azure Monitor Log Analytics by using the `NetworkAccessGenerativeAIInsights` diagnostic settings category. For configuration steps, see [Microsoft Sentinel integration](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-sentinel-integration).

## Discover shadow MCP servers

Because MCP detection uses deep packet inspection rather than a cloud app catalog, the Generative AI Insights logs page surfaces previously unknown, private, and shadow MCP servers.

To review discovered MCP servers:

1. Open the **Generative AI Insights** logs page.
1. Set **Activity** to **MCP**.
1. Review unique values in the **Destination URL** column to identify MCP servers in use.
1. Select an `initialize` response event for a server to view the tools and capabilities it advertises.
1. To block traffic to a risky MCP server, use [URL filtering](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-web-content-filtering) to deny access to that server's URL.

For a deeper walkthrough of MCP-specific operations, see [View MCP traffic logs](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-model-context-protocol-logging).

## Troubleshoot

| Issue | Likely cause and fix |
|---|---|
| The page is empty. | Verify that traffic forwarding is enabled, that users have generated GenAI or MCP traffic, and that [TLS inspection](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-transport-layer-security) is enabled for end-user devices. |
| No prompt events appear, but users access supported GenAI apps. | Prompt logging requires TLS inspection. Confirm that the destination isn't excluded from your TLS inspection policy. |
| MCP events show no MCP client name or server name. | The name isn't guaranteed to be present in every payload. Use **Destination URL** as the reliable MCP server identifier. |
| Local MCP server activity is missing. | MCP logging captures traffic only to **remote** MCP servers. Local MCP servers don't have a network footprint that Global Secure Access can inspect. |

## Next steps

- [Generative AI Insights in Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-generative-ai-insights)
- [View MCP traffic logs](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-model-context-protocol-logging)
- [View network traffic logs](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-view-traffic-logs)
- [Microsoft Sentinel integration](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-sentinel-integration)
