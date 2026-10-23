# Get started with the Microsoft Release Communications MCP Server

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/mrc-mcp  
> Microsoft doc last updated: 04/15/2026


This article introduces the Microsoft Release Communications (MRC) Model Context Protocol (MCP) Server, explains how it works, and outlines how to start using it in your environment.

The MRC MCP Server provides a unified, programmatic way for MCP-compatible AI clients to access trusted and up-to-date information that powers **[Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)** and **[Azure Updates](https://azure.microsoft.com/updates)**.

MRC MCP Server is a remote **[MCP](https://modelcontextprotocol.io/docs/getting-started/intro)** server that uses streamable HTTP transport, which allows users to search, filter and retrieve the latest feature release information using natural language in AI clients.

Instead of requiring developers to understand schemas and query APIs, this tool lets anyone ask questions in plain language to get precise, structured answers.

## Use cases

With MRC MCP, you can do the following actions:

- Enhance **AI clients** such as Visual Studio Code (VS Code), Visual Studio, GitHub Copilot CLI, Claude Code, and other MCP‑compatible clients.
- Enable IT admins, engineers, and technical users to query release and roadmap information directly from their AI client without relying on the websites.

## Requirements

Although the MRC MCP Server is publicly available and free to use, users are subject to the [Microsoft API Terms of Use](https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use). Read and understand the API Terms of Use before using the MRC MCP Server and before including the output in any production environment.

There's no authentication required to access the MRC MCP Server. Users can use their preferred MCP client or agentic development environment, such as VS Code, Visual Studio, and more.

There's no licensing required to use the MRC MCP server.

## MCP Endpoint

To connect with MRC MCP Server, use a compatible AI client with the endpoint pointing to the following URL:

```HTML
https://www.microsoft.com/releasecommunications/mcp
```

> [!NOTE]
> This endpoint provides programmatic access for MCP clients over Streamable HTTP. It doesn't support direct access from a web browser and might return a 405 Method Not Allowed error if accessed manually.

## Installation guide

Although VS Code is a common client for MCP Server, MCP is an open protocol that's also supported by many clients including agents in Copilot Studio, in Foundry, and many other agentic IDEs. For some other MCP‑compatible clients, the configuration steps are similar and involve adding the MCP server endpoint to a client‑specific configuration file or settings.

The high-level process includes the following steps:

1. Configure your AI client.
2. Use the MCP server.

### Standard configuration

The following **standard configuration** works in most clients:

```json
{
  "servers": {
    "MRC-MCP-Server": {
      "type": "http",
      "url": "https://www.microsoft.com/releasecommunications/mcp"
    }
  }
}
```

### Configure your Editor

For detailed instructions on how to configure the MRC MCP Server in specific clients, see the following guides:

| Client | Installation / Configuration | MCP Guide |
| ---------------------- | ----------------------------------------------- | ------------------------------------- |
| **VS Code** | 1. Open `mcp.json` at **User level** (applies to every VS Code session) or **Workspace level** (`.vscode/mcp.json` in your project folder).<br/>The user-level file is located in the VS Code user settings directory:<br/>  - **Windows:** `%APPDATA%\Code\User\mcp.json`<br/>  - **macOS:** `~/Library/Application Support/Code/User/mcp.json`<br/>  - **Linux:** `~/.config/Code/User/mcp.json`<br/>2. Add the [standard configuration](#standard-configuration) MCP server entry.<br/>3. Query release data using your AI client. | [VS Code MCP configuration guide](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) |
| **Visual Studio** | 1. Create `.mcp.json` at solution or user level<br/>2. Add the [standard configuration](#standard-configuration) MCP server entry.<br/>3. Query release data using your AI client. | [Visual Studio MCP configuration guide](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers) |
| **GitHub Copilot CLI** | 1. Run `/mcp add` in interactive mode, opens a configuration form.<br/> 2. Enter a server name and select **HTTP** as the server type. No authentication is required.<br/> 3. Press **Ctrl+S** to save (server is available immediately). <br/> **or** <br/> edit `~/.copilot/mcp-config.json`.<br/> | [Copilot CLI MCP guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers) |
| **Claude Desktop** | Follow **Add custom connector** instructions in official guide. | [Claude Desktop MCP guide](https://modelcontextprotocol.io/docs/develop/connect-remote-servers#connecting-to-a-remote-mcp-server) |
| **Claude Code** | Run `claude mcp add --transport http mrc-mcp https://www.microsoft.com/releasecommunications/mcp` <br /> **or** <br/> edit `~/.claude/mcp.json`<br /> | [Claude Code MCP guide](https://code.claude.com/docs/en/mcp) |
| **Cursor** | 1. Open Cursor MCP settings.<br/>2. Edit the MCP server configuration to `mcp.json`. | [Cursor MCP guide](https://cursor.com/docs/mcp). |
| **Codex** | Run `codex mcp add mrc-mcp --url https://www.microsoft.com/releasecommunications/mcp`. | [Codex MCP documentation](https://github.com/openai/codex/blob/main/codex-rs/config.md#mcp_servers) |

## Available Tools

The MCP server exposes four tools:

| Tool | Description |
| --- | --- |
| **`get_recent_azure_updates`** | Retrieves Azure update posts from Microsoft Release Communications with optional filtering and search capabilities. Returns up to 50 updates per request with truncated descriptions. Supports OData filtering by products, product categories, tags (Features, Retirements, Security, etc.), status, availability dates, and publication dates. Includes text search on titles and pagination |
| **`get_azure_update_by_id`** | Retrieves a specific Azure update post by its unique identifier. Returns full details of products, tags, and availability dates. Use the unique Azure Updates ID to get more information about a specific post. |
| **`get_recent_roadmaps`** | Retrieves Microsoft 365 roadmap posts from Microsoft Release Communications with optional filtering and search capabilities. Returns up to 50 roadmap items per request with truncated descriptions. Supports OData filtering by products, platforms, release rings, cloud instances, status, availability dates, and publication dates. Includes text search on titles and pagination. |
| **`get_roadmap_by_id`** | Retrieves a specific Microsoft 365 roadmap post by its unique identifier. Returns full details of products and availability dates. Use the unique Microsoft 365 roadmap ID to get more information about a specific post. |

> [!TIP]
> The list tools (`get_recent_azure_updates`, `get_recent_roadmaps`) return truncated descriptions to fit within AI context windows.

## Use the MCP Server

To use the MRC MCP Server after installation, do the following steps:

1. Open a chat window in VS Code with GitHub Copilot or your AI client.
2. Ask a question related to Microsoft 365 Roadmap or Azure Updates.
3. Allow the client to use MCP server tools when prompted.
4. Review the response.

### Example queries

Here are sample natural‑language queries that demonstrate how users can retrieve product release information across Microsoft 365 Roadmap and Azure Updates:

**Microsoft 365 Roadmap**

- As per Microsoft 365 Roadmap, which Microsoft Teams product features are releasing in June?
- Which Outlook product features on the Microsoft 365 Roadmap were updated last week?
- What's the status of Feature ID 526798?
- List all Excel features launching on Mac that are releasing in March.
- Create an email for my Compliance team to review the Microsoft Purview features that are currently rolling out on Microsoft 365 Roadmap.
- What's planned for mobile-only apps in OneNote?

**Azure Updates**

- Which Azure features became Generally Available this quarter?
- Show all Azure retirements scheduled for this year.
- What are the latest Azure AI services updates?
- Which Azure Databricks features were released in February?
- List all Azure features that are retiring in next three months.

## Limitations

The MRC MCP server contains publicly available documentation, which is available on [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) and [Azure Updates](https://azure.microsoft.com/updates).
The underlying product release information refreshes daily.

## Troubleshooting

### MCP tools aren't being invoked

In some cases, even tool-friendly models might not call MCP tools by default. You can improve tool usage by providing **system-level instructions** (if supported by your AI client) that explicitly encourage use of the Release Communications MCP Server tools.

#### System instructions prompt example

When an AI tool doesn't use the MCP tool when expected, configure specific system-level instructions for the tool, similar to the following text:

```markdown
You have access to MCP tools provided by the Release Communications MCP Server:
- `get_recent_roadmaps`
- `get_roadmap_by_id`
- `get_recent_azure_updates`
- `get_azure_update_by_id`

When handling questions about Microsoft 365 Roadmap features or Azure service updates, use these tools to retrieve the most current and authoritative release information
before responding. When handling questions about Microsoft 365 product roadmap timelines, upcoming feature releases, Azure service updates, or release status for specific products (Teams, Outlook, SharePoint, Excel, etc).
```

Here are some general best practices:

- Be explicit in your prompt (for example, mention *Azure Updates* or *Microsoft 365 Roadmap*). If the prompt is too generic or doesn't clearly relate to release or roadmap data, then your AI client might not invoke MCP tools.
- Use a **system-level instruction** (if supported by your AI client) to encourage tool usage.
- Confirm that the MCP server is correctly configured and enabled in your client

### Customize MCP tool selection

#### VS Code and Visual Studio

VS Code and Visual Studio support **explicit MCP tool selection** in Copilot Agent mode. You can improve accuracy by selecting only relevant tools, such as Azure Update tools.

1. Open Chat.
2. Select **Agent** mode.
3. Select **Configure Tools**.
4. Select or deselect MCP tools before running the prompt.

**Related documentation**

- [Use tools with agents in VS Code](https://code.visualstudio.com/docs/copilot/agents/agent-tools)
- [Configure MCP servers in VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [Use MCP servers in Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/mcp-servers)

#### Claude Desktop, Claude Code, Cursor, Codex, GitHub Copilot

These clients don't expose explicit tool selection UI. Instead, do the actions:

- Use system instructions to guide tool usage.
- Avoid mixing Azure and Microsoft 365 topics in one prompt.

**Related documentation**

- [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers#connecting-to-a-remote-mcp-server)
- [MCP tools specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)

## Related articles

[Modern change management for Microsoft 365 - Overview](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/plan-for-change-management)

[Configure modern release options for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/configure-release-options)

[What's new in Message center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/message-center-updates)
