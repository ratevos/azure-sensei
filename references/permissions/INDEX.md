# permissions reference index

Lookup tables generated from official Microsoft docs (scripts/build_permissions.py). Read PERMISSIONS.md at the skill root for the workflow. Each file is one entry per line, built to be searched with grep.

- `entra-tasks.md` — **Entra: least-privileged role by task** — Microsoft's task → role mapping across Entra areas (CA, apps, users, groups, PIM, governance, devices, monitoring…)
- `entra-roles.md` — **Entra built-in roles** — role template IDs, PRIVILEGED flag, description
- `graph-api-permissions.md` — **Graph v1.0 per-API permissions** — least-privileged delegated/application scope, higher alternatives, required Entra role for delegated calls, for ~2,900 APIs
- `graph-permission-catalog.md` — **Graph permissions catalog** — every permission's app and delegated IDs, admin consent requirement, description
- `azure-roles.md` — **Azure built-in roles** — category, role definition ID, description for ~500 roles (Key Vault, AKS, Sentinel, Policy, Monitor…)

Related material elsewhere: Exchange RBAC discovery (`exchange-online/powershell-guides/find-exchange-cmdlet-permissions.md`), Security & Compliance role group cmdlets (`purview/cmdlets/*RoleGroup*`), M365 admin roles (`m365-admin/admin/add-users/about-admin-roles.md`), Azure RBAC concepts (`azure-governance/role-based-access-control/`).
