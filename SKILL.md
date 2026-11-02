---
name: azure-sensei
description: Implementation guides for Microsoft cloud identity, security and infrastructure admin, grounded in bundled Microsoft Learn docs. Covers Entra ID (Azure AD) including Conditional Access, MFA, PIM, Identity Protection, Entra Connect and Cloud Sync, app registrations, enterprise apps, tenant restrictions; Global Secure Access; Intune; Defender XDR; Purview DLP incl. endpoint DLP on Windows/macOS and DLP PowerShell; Sentinel; Azure Key Vault; resource groups, Azure RBAC, Azure Policy; AKS; Exchange Online; the Microsoft 365 admin center; and which roles, Graph scopes and permissions any action requires. Use whenever the user asks how to configure, script, automate, troubleshoot or audit any of these, wants portal steps, PowerShell, Graph or Azure CLI for them, or asks what permissions or role they need or why they get access denied, even if they only name a feature ("CA policy", "break-glass account", "sensitivity label", "allowed upload domains", "transport rule", "node pool", "Connect-IPPSSession", "403").
---

# Microsoft cloud admin implementation guides

This skill turns official Microsoft documentation into implementation guides for an experienced administrator. The value it adds over general knowledge is that every step, cmdlet and parameter comes from a Microsoft document you actually opened, with its source URL, so the admin can trust it and check it. These products change constantly (portal menus move, cmdlets get retired, features leave preview), so recalled knowledge is often subtly out of date. Ground the guide in the references, and say so plainly when they don't cover something.

## Paths and searching

All paths in this skill (`references/…`, `PERMISSIONS.md`, `scripts/…`) are relative to **this skill's own folder**, the directory containing this SKILL.md (for example `~/.claude/skills/<skill-name>/`). Your working directory is usually the user's project, so resolve paths against the skill folder, not the current directory.

Search, don't read whole files. Several references are very large (the Graph permissions lookup is over 1 MB, some cmdlet pages over 200 KB). Use your search tool (Grep/Glob, or `grep`/`rg` in a shell) against the `INDEX.md` files and lookup tables, then open only the matching document, or only the relevant section of a long one (search for the line number first, then read that range). On Windows without a POSIX shell, use the built-in search tool or `Select-String`.

## Workflow

1. **Identify every product involved.** Many tasks span several: "require compliant devices" is Conditional Access plus Intune; "DLP for Teams and Exchange" is Purview plus Exchange; "AKS with Entra groups" is AKS plus Entra ID.
2. **Find the documents.** For each product, search its index, then open the 2–5 most relevant documents in full:
   ```bash
   # Conceptual articles first: they hold the procedure, prerequisites and warnings
   grep -i "keyword" references/<product>/INDEX.md | grep -vE "graph-api/|cli/|cmdlets/"
   # Then exact syntax
   grep -i "keyword" references/<product>/INDEX.md | grep -E "graph-api/|cli/|cmdlets/"
   grep -ril "keyword" references/<product>/ | head -20    # full text, when the index misses
   ```
   Search the two kinds separately, because API, CLI and cmdlet pages far outnumber articles and crowd them out of a single search. Try synonyms and Microsoft's own terms (for example "authentication strength", "named location", "report-only", "sensitive information type", "mail flow rule" for transport rule). Conceptual articles give the procedure and constraints; the cmdlet, CLI and Graph reference folders give exact syntax.
3. **Verify syntax before writing a script.** Open the reference page for every cmdlet, `az` command and Graph endpoint you plan to use, and use only parameters that appear there. A plausible but nonexistent parameter is the worst failure this skill can produce, because an admin will paste it into a production tenant.
4. **Check freshness.** Each reference file starts with its source URL and Microsoft's last-updated date. If web access is available and the doc is more than about six months old, involves a preview feature, or concerns portal navigation, fetch the source URL and reconcile any differences (the live page wins, and say what changed). If there's no web access, note the doc date in the guide. Cmdlet and CLI reference pages carry no date ("unknown"); that's normal and not a reason to fetch them.
5. **Work out the permissions.** Every guide states what the admin (and any script or app) needs. Read `PERMISSIONS.md` and use its lookup tables for this; it covers the separate permission layers (Entra roles, Graph scopes, Azure RBAC, Exchange and Purview role groups, Kubernetes RBAC) that one task can involve.
6. **Write the guide** in the format below.

If the question is only about permissions ("what role do I need to…", "which Graph scope…", "why do I get 403…"), go straight to `PERMISSIONS.md` and answer in its format instead of writing a full guide.

## Where the documents are

| Product | Folder | Contents |
|---|---|---|
| Conditional Access | `references/conditional-access/` | All Entra Conditional Access articles; Graph API reference for policies, named locations and authentication strengths, with Graph PowerShell examples |
| Entra ID | `references/entra-id/` | Authentication methods, PIM, ID Protection, hybrid (Connect, Cloud Sync), enterprise apps, Entra roles, users, monitoring, governance, fundamentals; `external-id/` tenant restrictions v2 (company-only sign-in, blocking personal Microsoft accounts and other tenants); Graph reference for roles, auth methods policy, risky users; `az ad` CLI |
| Global Secure Access | `references/global-secure-access/` | Entra Internet/Private Access: clients (Windows, macOS), traffic profiles, universal tenant restrictions, web content filtering, network content filtering with inline Purview DLP for any app's HTTP/S traffic |
| Exchange Online | `references/exchange-online/` | `powershell-guides/` (connecting, app-only auth, EXO V3 module); `cmdlets/` with every cmdlet available in Exchange Online |
| Purview | `references/purview/` | `dlp/` every DLP article: policy design and reference, endpoint DLP (settings, activities, Windows/macOS support), Chrome/Firefox extensions, network data security, label conditions, simulation; `device-onboarding/` Windows and macOS onboarding (Intune, JAMF, any MDM); `cmdlets/` every Security & Compliance PowerShell cmdlet: DLP, sensitivity labels, retention, compliance search, eDiscovery |
| M365 admin center | `references/m365-admin/` | admin center tasks, enterprise deployment, baseline security mode, security guidance |
| Azure governance | `references/azure-governance/` | resource groups, ARM, locks, tags, management groups, Azure RBAC, Azure Policy; `az group`, `az role`, `az policy`, `az lock`, `az tag` CLI |
| AKS | `references/aks/` | AKS articles; `az aks` CLI reference |
| Key Vault | `references/key-vault/` | `az keyvault` CLI reference (conceptual docs: uploaded material when present) |
| Permissions (all products) | `references/permissions/` | Generated lookups: Entra task → least-privileged role, Entra role IDs, Graph per-API least-privileged scopes and required roles (~2,900 APIs), Graph permission IDs and consent, Azure built-in roles. Workflow in `PERMISSIONS.md` |
| Intune, Defender XDR, Sentinel | `references/<product>/` if present | Not in Microsoft's public repos; add them with `scripts/fetch_learn.py` (see "Adding documentation") or from user-supplied documentation |

Every folder has an `INDEX.md`. If a product has no folder, or the folder lacks the scenario, use web search restricted to learn.microsoft.com when available and cite those pages. Otherwise, write from general knowledge only with a clear warning at the top that the guide is not grounded in documentation and must be checked.

Some very large lookup tables were left out of the bundle on purpose. Fetch them live when needed: the [licensing service plan reference](https://learn.microsoft.com/en-us/entra/identity/users/licensing-service-plan-reference), [Azure resource provider operations](https://learn.microsoft.com/en-us/azure/role-based-access-control/permissions/compute), and the Azure Policy built-in definition lists.

## Admin portals

Use current portal names and URLs, and the navigation path exactly as the source document gives it.

- Microsoft Entra admin center: `entra.microsoft.com`
- Microsoft 365 admin center: `admin.cloud.microsoft` (admin.microsoft.com redirects there)
- Exchange admin center: `admin.exchange.microsoft.com`
- Microsoft Purview portal: `purview.microsoft.com`
- Microsoft Defender portal: `security.microsoft.com` (Defender XDR, and Sentinel in the unified SecOps experience)
- Intune admin center: `intune.microsoft.com`
- Azure portal: `portal.azure.com`

## Scripting conventions

These reflect current Microsoft guidance; prefer them unless a document in the references says otherwise.

- **Entra and Conditional Access:** Microsoft Graph PowerShell (`Connect-MgGraph -Scopes ...` with the least-privileged scopes the endpoint's reference page lists) or Graph REST. The AzureAD and MSOnline modules are retired; never use them, and if the user's script does, point that out and translate it.
- **Exchange Online:** `Connect-ExchangeOnline` (ExchangeOnlineManagement module, REST-based V3).
- **Purview DLP, labels, retention:** `Connect-IPPSSession` from the same module. DLP policies and rules are separate objects (`New-DlpCompliancePolicy`, then `New-DlpComplianceRule -Policy`).
- **Azure:** Azure CLI (`az`) or Az PowerShell; give both only when the user asks. Bicep or Terraform only on request.
- Make scripts safe to rerun: check whether the object exists before creating it, and use `-WhatIf` where the cmdlet supports it.
- Use placeholders (`<tenant-id>`, `<group-object-id>`) instead of invented values, and list them once at the top of the script.

## Safety defaults that belong in every relevant guide

- **Conditional Access:** create policies in report-only mode (`state = "enabledForReportingButNotEnforced"`), check sign-in logs and the What If tool, then enable. Exclude emergency access (break-glass) accounts from every policy. Warn when a policy could lock out admins (for example "All users" + "All resources" + block).
- **DLP:** start in simulation mode (test mode) and review matches before enforcing.
- **Privileged roles:** recommend PIM eligible assignments over permanent ones, and least-privileged roles (name the specific role the doc lists, such as Conditional Access Administrator, not Global Administrator).
- **Azure:** apply resource locks and policy assignments at the narrowest sensible scope; call out anything that affects a whole subscription or management group.

## Data-movement requests: say which layer can actually enforce it

Requests like "only let labelled files go to approved destinations", "company OneDrive but not personal", or "developer tools may only upload to our repos" usually span several products, and some parts can't be enforced by DLP at all. Before writing the guide, map each part of the request to the control that enforces it and say plainly which parts no Microsoft control covers. Verify the points below in the bundled pages before relying on them (they reflect the docs as of the last rebuild):

- **Endpoint DLP destination controls are browser-only.** Service domains and Sensitive service domain groups apply to uploads from Microsoft Edge, and from Chrome/Firefox with the Purview extension (`purview/dlp/dlp-configure-endpoint-settings.md`, "Service domains"). For non-browser apps (IDEs, `git`, CLIs, sync clients) the endpoint control is Restricted apps, which acts when the app *opens* a protected file, not on where it sends it. Microsoft doesn't state "not supported for non-browser apps" outright; quote the scoping sentences and say the conclusion is an inference.
- **Non-browser network uploads** need network data security: Global Secure Access network content filtering with "Scan with Purview" (`global-secure-access/global-secure-access/how-to-network-content-filtering.md`) or a SASE integration (`purview/dlp/dlp-network-data-security-learn.md`). Point out its documented limits (fail-open, size cap, files encoded inside JSON may not be inspected) and licensing.
- **Browser extension by OS:** the Purview extension for Chrome works only on Windows and isn't needed on macOS (`purview/dlp/dlp-chrome-get-started.md`); macOS supports Edge, Safari, Chrome and Firefox natively (`purview/device-onboarding/device-onboarding-macos-overview.md`). Check the macOS column of the support table in `purview/dlp/endpoint-dlp-learn-about.md` for preview features.
- **Domain syntax:** `*.` only as a prefix (no `highwaybaas.*.com`); the Service domains list takes host names only, while sensitive service domain groups accept paths (`contoso.com/path/`). Enumerate real hosts instead of inventing wildcards.
- **Personal vs company account on the same domain** (OneDrive, Azure DevOps, SaaS AI tools) can't be told apart by DLP domain lists. For Microsoft services use tenant restrictions v2 (`entra-id/external-id/tenant-restrictions-v2.md`) and the OneDrive sync-client tenant allow-list; for non-Microsoft services, say that the vendor's own org controls are needed and that they're outside this skill's references.
- **Sensitivity-label conditions** only match items that can carry labels; check `purview/dlp/dlp-sensitivity-label-as-condition.md` before promising coverage for code files or other formats.
- **Endpoint DLP settings in PowerShell:** the `Set-PolicyConfig -EndpointDlpGlobalSettings` examples in the cmdlet reference are malformed and `-SiteGroups` is undocumented. Give portal steps for endpoint settings and groups; for rules, configure once in the portal and read back the exact `EndpointDlpRestrictions` setting names with `Get-DlpComplianceRule` before scripting.

## When you can run commands (agent mode)

In Claude Code or any environment where you can execute commands, go beyond writing the guide: inspect the environment, tailor the script to the real tenant, and carry it out with the user. Admin changes hit production identity and security systems, so follow this order.

1. **Check tooling.** Confirm what's installed before relying on it: `pwsh` and the needed modules (`Microsoft.Graph.*`, `ExchangeOnlineManagement`, `Az`), `az`, `kubectl`/`kubelogin`. Offer the install command from the references if something is missing.
2. **Confirm the target.** After connecting, show which tenant, subscription and account you're on (`Get-MgContext`, `Get-ConnectionInformation`, `az account show`) and have the user confirm it's the intended one before anything else. Prefer a test or dev tenant when the user has one.
3. **Check permissions first.** Use `PERMISSIONS.md` to work out what's needed, then run its read-only check commands so a missing role or scope surfaces now, not halfway through a change.
4. **Discover before you write.** Run read-only commands to fill in real values instead of placeholders: existing policies with the same name, break-glass account object IDs, group IDs, existing DLP policies, resource IDs. Reading is safe; do it freely.
5. **Write scripts to files** in the user's project (for example `scripts/ca-admins-phishing-resistant.ps1`), so there's a reviewable, rerunnable record of what was done.
6. **Ask before every change.** Show exactly what will be created, changed or deleted, and in which tenant, then wait for an explicit yes before running anything that modifies the tenant or Azure resources. Use the safe states from "Safety defaults": report-only, simulation/test mode, `-WhatIf`. Never disable security controls, remove break-glass exclusions, or delete objects without a separate explicit confirmation.
7. **Verify and report.** Run the guide's verification steps, show the results, and tell the user how to roll back.

Never paste secrets, client secrets or tokens into scripts or files; use interactive sign-in, managed identities or certificate credentials, as the references describe.

## Guide format

The reader is an experienced administrator. Skip basics, explain only what's non-obvious, and keep prose tight. Use this structure, dropping sections that don't apply:

```markdown
# <Task>

**Applies to:** <products> · **Licensing:** <exact SKUs/plans required, e.g. Entra ID P1> · **Least-privileged role:** <role(s), per layer when several apply>

## Before you start
Prerequisites, dependencies, and decisions to make first (design choices, things that can't be undone, known limitations and preview status). Include a **Permissions** line for anything beyond the header role: Graph scopes for `Connect-MgGraph`, role groups for `Connect-IPPSSession`, Azure RBAC role and scope, in-cluster roles.

## Configure in the portal
Numbered steps, starting with the sign-in URL and role, using the navigation path from the docs.

## Configure with PowerShell / Graph / CLI
Module install and connect lines, then a complete script equivalent to the portal steps.

## Verify
How to confirm it works (logs, reports, What If, Get- commands, test sign-ins).

## Roll back
How to disable or remove it safely.

## Sources
- [Doc title](source URL) — Microsoft doc date
```

Give portal and script versions side by side for each configuration task, because experienced admins usually prototype in the portal and then automate. If a task genuinely has no portal option (or no scripting option), say so in that section instead of omitting it silently.

When the user asks a narrow question (one cmdlet's syntax, what a setting does, whether a feature needs P2), answer it directly and briefly, with the source link, rather than producing a full guide.

## Adding documentation

When the user supplies new documentation (PDFs, saved pages, Markdown), convert it into `references/<product>/` as one Markdown file per article with the same header (`# Title`, `> Source: <Learn URL>`, `> Microsoft doc last updated: <date>`), then regenerate that folder's `INDEX.md`. `scripts/build_refs.py` and then `scripts/build_permissions.py` rebuild everything from Microsoft's public GitHub repos; `scripts/fetch_sources.sh` clones those repos first.

For Learn docsets with no public repo (Purview DLP today; Intune, Defender XDR or Sentinel if the user wants them), add a line to `scripts/learn_pages.txt` (a docset's `toc.json` plus a page-name regex, or a single page URL) and run `scripts/fetch_learn.py <skill>/references` **after** `build_refs.py`. It asks Learn for each page's Markdown source, writes files with the standard header and merges them into the product's `INDEX.md`.
