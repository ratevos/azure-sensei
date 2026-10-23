# Permissions guide

Read this file whenever the user asks what permissions, roles, scopes or consent an action needs, why they get "access denied" / 403 / "insufficient privileges", how to delegate a task, or how to set up a service principal, managed identity or automation account. Every implementation guide also uses it to fill in its permissions section.

## Why this needs care

Microsoft has several independent permission systems, and one action often needs more than one of them. A Graph PowerShell script that creates a Conditional Access policy needs a Graph *scope* consented for the app **and** an Entra *role* on the signed-in admin. An AKS admin needs an Azure RBAC role to download the kubeconfig **and** a Kubernetes-level role to run kubectl. The most common failure is answering for one layer and missing the other, so walk through every layer that applies.

Always aim for least privilege: name the narrowest role Microsoft documents for the task, show the broader roles only as alternatives, and never default to Global Administrator or Owner.

## The permission layers

| Layer | Controls | Where to look |
|---|---|---|
| **Entra directory roles** | Entra admin center, CA, users, apps, PIM, and admin access to M365 services (Exchange Administrator, Intune Administrator, Security Administrator…) | `references/permissions/entra-tasks.md` (task → least-privileged role), `entra-roles.md` (role IDs, PRIVILEGED flag), full permissions in `references/entra-id/identity/role-based-access-control/permissions-reference.md` |
| **Microsoft Graph permissions** | Scripts, apps and automation calling Graph (Graph PowerShell, REST) | `references/permissions/graph-api-permissions.md` (per-API least-privileged scope + required Entra role), `graph-permission-catalog.md` (IDs, admin consent) |
| **Azure RBAC** | Azure resources: subscriptions, resource groups, Key Vault, AKS, Sentinel workspaces, Policy | `references/permissions/azure-roles.md`, per-role actions in `references/azure-governance/role-based-access-control/built-in-roles/<category>.md` |
| **Exchange Online RBAC** | Exchange cmdlets and EAC features (role groups, management roles, scopes) | `references/exchange-online/powershell-guides/find-exchange-cmdlet-permissions.md`; `cmdlets/Get-ManagementRole*.md`, `*RoleGroup*.md` |
| **Purview / Security & Compliance role groups** | DLP, labels, retention, eDiscovery, compliance search | `references/purview/cmdlets/*RoleGroup*.md`, `Get-ManagementRole*.md`; role group catalog is not bundled (fetch the Purview permissions page live) |
| **Kubernetes RBAC on AKS** | kubectl actions inside the cluster | `references/aks/` (search "authorization", "rbac") plus the AKS roles in `azure-roles.md` |
| **Product RBAC not bundled yet** | Intune RBAC roles and scope tags, Defender XDR unified RBAC, Sentinel content | `references/<product>/` if uploaded; otherwise live Learn. The Entra roles (Intune Administrator, Security Administrator, Security Operator…) are bundled and cover tenant-wide access |
| **M365 admin center roles** | Billing, licenses, service health, org settings at admin.cloud.microsoft | `references/m365-admin/admin/add-users/about-admin-roles.md` (these are Entra roles surfaced in the admin center) |

## Workflow

1. **Name the action precisely** and identify how it will be done: portal, PowerShell as a signed-in admin (delegated), or unattended automation (application permissions, managed identity, service principal). The answer differs.
2. **List every layer** from the table that the action touches.
3. **Look up each layer** in the files above (paths are relative to the skill folder; search them, don't open the large tables in full):
   ```bash
   cd references/permissions
   grep -i "conditional access" entra-tasks.md                 # who can do the task
   grep -i "conditionalAccess/policies\`" graph-api-permissions.md   # scope + role for the API
   grep -i "key vault" azure-roles.md                           # Azure roles
   ```
   For Graph, search by HTTP path or resource name (about 30 pages, such as change-notification subscriptions, have per-resource permissions and aren't in the lookup: fetch those live); the `—` separated line gives delegated scope, application scope, higher alternatives, and the Entra role the signed-in user also needs. If a Graph line shows no role requirement, check `entra-tasks.md` for the task rather than assuming none is needed.
   For Exchange and Security & Compliance cmdlets, the reference pages only link to a permissions article; use the documented discovery method in `find-exchange-cmdlet-permissions.md` (`Get-ManagementRoleEntry` and `Get-ManagementRoleAssignment`), and give the user the commands to run in their tenant.
4. **Prefer just-in-time access:** for Entra roles and Azure roles, recommend PIM eligible assignments. For automation, prefer a managed identity over a client secret, and application permissions scoped as narrowly as the API allows.
5. **Show how to verify** what the person currently holds (commands below).

## Answer format

For a permissions question, answer with a compact block per layer, then the verify commands:

```markdown
## Permissions for: <action>

**Entra role (signed-in admin):** <least-privileged role> · alternatives: <roles> · PRIVILEGED: yes/no
**Graph scopes (if scripting):** delegated `<scope>` · application `<scope>` · admin consent: yes/no
**Azure RBAC:** <role> at scope `<narrowest scope>`
**Exchange / Purview role group:** <role group or management role>
**In-cluster (AKS):** <role> at `<cluster or namespace>`

Recommended: <PIM eligible assignment / managed identity / etc.>

### Check what you have
<commands for the relevant layers>

### Sources
- <doc> — <date>
```

Drop layers that don't apply. In a full implementation guide, the same content goes in the header line (**Least-privileged role**) and, when scripting is involved, a short "Permissions" paragraph under "Before you start" listing the Graph scopes for `Connect-MgGraph` or the role groups for `Connect-IPPSSession`.

## Checking current permissions

Use these patterns (all documented in the bundled references; open the relevant page to confirm parameters before giving them):

- **Entra roles of a user:** `GET https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments?$filter=principalId eq '<object-id>'` (run with `Invoke-MgGraphRequest`), or in PowerShell list a role's holders with `Get-MgRoleManagementDirectoryRoleAssignment -Filter "roleDefinitionId eq '<role-id>'"`. Roles inherited through role-assignable groups appear only in the **beta** `transitiveRoleAssignments` endpoint. PIM-eligible roles appear only once activated. Source: `entra-id/identity/role-based-access-control/view-assignments.md`.
- **Graph scopes in the current session:** `(Get-MgContext).Scopes`.
- **Azure RBAC:** `az role assignment list --assignee <upn-or-object-id> --all -o table` (CLI reference in `azure-governance/cli/role/assignment.md`).
- **Exchange Online:** `Get-ManagementRoleEntry -Identity "*\<Cmdlet>"` to find which roles grant a cmdlet, then `Get-ManagementRoleAssignment -Role <role> -Delegating $false` to see who holds them (`exchange-online/powershell-guides/find-exchange-cmdlet-permissions.md`).
- **Security & Compliance:** `Get-RoleGroup` and `Get-RoleGroupMember -Identity <role-group>` after `Connect-IPPSSession`.
- **AKS in-cluster:** `kubectl auth can-i <verb> <resource> [-n <namespace>]`.

## Common traps to mention when relevant

- **Delegated Graph calls need both** the consented scope and an Entra role; app-only calls need only the application permission (plus admin consent), which makes them powerful, so scope them tightly.
- **Conditional Access via Graph** has a documented known issue requiring consent to extra permissions (`Application.Read.All`).
- **Directory-role-targeted CA and admin-unit-scoped roles:** CA doesn't enforce on AU-scoped or custom role assignments.
- **Azure RBAC propagation** can take up to several minutes (AKS documents up to five), so a fresh assignment that fails immediately may just need time.
- **Key Vault:** data-plane roles (Key Vault Secrets User, etc.) work only when the vault uses the Azure RBAC permission model, not access policies.
- **Owner/Contributor don't grant data-plane access** (Key Vault secret values, blob data) under the RBAC model: those need DataActions roles such as Key Vault Secrets User or Storage Blob Data Reader. Microsoft's worked example is in `azure-governance/role-based-access-control/role-definitions.md`.
