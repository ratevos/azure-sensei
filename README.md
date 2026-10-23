# Azure Sensei

**Your Microsoft tenant's sensei: implementation guides and least-privilege permissions, built on Microsoft's official documentation.**

An [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) for Claude that turns Microsoft Learn documentation into ready-to-run implementation guides: portal steps and PowerShell / Microsoft Graph / Azure CLI side by side, verification, rollback, and the exact roles and permissions each task needs, with every step citing its Microsoft source.

> **Unofficial community project.** Not affiliated with, endorsed by, or supported by Microsoft. Microsoft, Azure, Microsoft Entra, Intune, Microsoft Defender, Microsoft Purview, Microsoft Sentinel and Exchange are trademarks of the Microsoft group of companies.

## Why

Admins lose hours to the same problems: portal menus that moved, retired PowerShell modules, cmdlet parameters that don't exist, and permissions spread across half a dozen separate systems. General-purpose AI answers often sound right and are subtly out of date.

This skill bundles about **4,000 official Microsoft documents** (converted from Microsoft's public docs repositories) and instructs Claude to:

- **Answer from the docs, not from memory.** Every guide cites the Microsoft Learn pages it used, with each page's last-updated date.
- **Verify every cmdlet, flag and Graph property** against the reference before putting it in a script.
- **Check freshness.** Older or preview-feature docs are re-checked against the live Learn page when web access is available.
- **Default to safe rollout.** Conditional Access in report-only mode, DLP in simulation mode, break-glass exclusions, PIM-eligible roles.
- **Work out permissions across every layer** an action touches.

## What it covers

| Area | Bundled official documentation |
|---|---|
| **Conditional Access** | All Entra CA articles; Graph API for policies, named locations, authentication strengths, with Graph PowerShell examples |
| **Microsoft Entra ID** | Authentication methods, PIM, ID Protection, Entra Connect & Cloud Sync, enterprise apps, roles, users, monitoring, governance |
| **Exchange Online** | Every Exchange Online PowerShell cmdlet; connection and app-only auth guides |
| **Microsoft Purview** | Every Security & Compliance PowerShell cmdlet: DLP, sensitivity labels, retention, eDiscovery |
| **Microsoft 365 admin center** | Admin center tasks, enterprise deployment, baseline security |
| **Azure governance** | Resource groups, ARM, locks, tags, management groups, Azure RBAC, Azure Policy, plus `az` CLI reference |
| **AKS** | AKS documentation plus the full `az aks` CLI reference |
| **Key Vault** | `az keyvault` CLI reference |
| **Permissions (all of the above)** | See below |

**Not bundled yet:** Intune, Defender XDR, Sentinel, and Key Vault / Purview / Exchange admin center conceptual docs. Microsoft doesn't publish these in public repositories. For these the skill falls back to live Microsoft Learn pages and says so in the guide.

## The permissions module

Ask "what role do I need to…", "which Graph scope for…", or "why am I getting 403?" and the skill checks every layer involved, since one task often needs more than one:

- **Entra directory roles:** Microsoft's own task → least-privileged role mapping (212 tasks), plus all built-in roles with template IDs and the PRIVILEGED flag
- **Microsoft Graph:** least-privileged delegated and application scope for about 3,900 APIs, the higher-privileged alternatives, and the Entra role the signed-in user also needs; plus every permission's IDs and admin-consent requirement
- **Azure RBAC:** about 500 built-in roles with IDs, including data-plane roles (Key Vault, Storage)
- **Exchange Online and Security & Compliance** role discovery, and **Kubernetes RBAC** on AKS

Each answer includes the commands to check what you currently hold.

## Example prompts

- *Create a Conditional Access policy requiring phishing-resistant MFA for all admin roles. Roll it out safely.*
- *Write a script that creates a DLP policy for Exchange, SharePoint and OneDrive detecting credit card numbers. Start in test mode.*
- *Deploy an AKS cluster with Entra ID auth, Azure RBAC, an admin group, and local accounts disabled.*
- *Our nightly app registration creates users and reads sign-in logs. Which Graph permissions should it get?*
- *I'm Security Administrator and New-MgIdentityConditionalAccessPolicy returns 403. Why?*

## Installation

### Claude Code (recommended)

Claude Code works directly in your terminal, which is where this skill shines. Claude searches the bundled references itself and, with your approval at each step, can do the implementation work too: check your PowerShell modules, confirm which tenant you're connected to, look up real values (existing policies, group and account IDs) with read-only commands, write the script into your project, and run it once you say yes.

Install it as a personal skill, available in every project:

```bash
git clone https://github.com/ratevos/azure-sensei.git ~/.claude/skills/azure-sensei
```

Or as a project skill, shared with your team through the repository:

```bash
git clone https://github.com/ratevos/azure-sensei.git .claude/skills/azure-sensei
```

Start `claude` and ask *"What skills are available?"*, or type `/` to see it in the menu. Claude uses it automatically when a request matches, or you can call it directly with `/azure-sensei`.

**How it behaves in Claude Code:** it does read-only discovery freely, but shows exactly what it will change, and in which tenant, and waits for your explicit yes before modifying anything. It uses report-only, simulation and `-WhatIf` modes where they exist. Use a test tenant when you can.

### Claude Desktop and claude.ai

Download `azure-sensei.skill` from the [Releases](../../releases) page and add it under Skills in Claude's settings. Skills require code execution to be enabled. Claude reads the references and writes the guides and scripts for you to run yourself, but it can't execute commands against your tenant.

## Keeping the docs current

Microsoft updates its documentation constantly. To rebuild the references from Microsoft's public repositories (requires `git` and Python 3 with PyYAML):

```bash
cd ~/.claude/skills/azure-sensei/scripts
./fetch_sources.sh                          # sparse-clones the official docs repos into /tmp/src
python3 build_refs.py ../references         # converts docs into reference files and indexes
python3 build_permissions.py ../references  # regenerates the permissions lookup tables
```

Set `MS_DOCS_SRC` to clone somewhere other than `/tmp/src`. The `references/intune`, `defender-xdr` and `sentinel` folders are for documentation you add yourself and aren't touched by the rebuild, so back them up first if you've filled them in.

## Repository layout

```
SKILL.md          Instructions Claude follows: routing, verification, guide format, agent-mode safety
PERMISSIONS.md    Permissions workflow across Entra, Graph, Azure RBAC, Exchange, Purview, AKS
references/       Converted Microsoft docs, one folder per product, each with an INDEX.md
  permissions/    Generated lookup tables (roles, Graph scopes, Azure roles)
scripts/          fetch_sources.sh, build_refs.py, build_permissions.py
evals/            Test prompts used to check the skill's behaviour
```

## Disclaimer

Guides are generated from Microsoft's documentation, but they're still guides. Review every script before running it, test in a non-production tenant when possible, and confirm that licensing and roles match your environment. You are responsible for changes made to your tenant.

## License

This project's own files (SKILL.md, PERMISSIONS.md, scripts, evals) are MIT licensed; see [LICENSE](LICENSE).

## Attribution

The content in `references/` is derived from Microsoft's documentation and remains under its original licenses. See [NOTICE.md](NOTICE.md).
