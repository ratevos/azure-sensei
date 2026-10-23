#!/usr/bin/env python3
"""Build the permissions module: grep-friendly lookup tables derived from official docs.

Run after build_refs.py (it reads some of that output) and fetch_sources.sh.
Usage: python3 build_permissions.py <skill>/references
"""
import os, re, sys, glob, yaml

SRC = os.environ.get("MS_DOCS_SRC", "/tmp/src")
REFS = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/azure-sensei/references"
OUT = os.path.join(REFS, "permissions")
os.makedirs(OUT, exist_ok=True)
FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

def strip_md(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)               # icons
    s = re.sub(r"<br\s*/?>", ", ", s, flags=re.I)                # multi-value cells
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return " ".join(s.replace("*", "").split()).strip(" ,").replace(".,", ".")

def write(name, title, source, intro, lines):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n> Source: {source}  \n> Generated from official Microsoft docs by scripts/build_permissions.py\n\n{intro}\n\n")
        f.write("\n".join(lines) + "\n")
    print(f"{name:32} {len(lines):5} entries")

# 1. Graph: least-privileged permission and required Entra role per API ----------
def graph_api_permissions():
    root = os.path.join(SRC, "graph/api-reference/v1.0")
    lines = []
    for path in sorted(glob.glob(os.path.join(root, "api", "*.md"))):
        text = open(path, encoding="utf-8", errors="ignore").read()
        m = FM_RE.match(text)
        try:
            title = (yaml.safe_load(m.group(1)) or {}).get("title", "") if m else ""
        except Exception:
            title = ""
        body = text[m.end():] if m else text
        perm = re.search(r"## Permissions(.*?)\n## ", body, re.S)
        if not perm:
            continue
        sec = perm.group(1)
        inc = re.search(r"\[!INCLUDE \[permissions-table\]\(([^)]+)\)\]", sec)
        table = ""
        if inc:
            p = os.path.normpath(os.path.join(os.path.dirname(path), inc.group(1)))
            if os.path.isfile(p):
                table = open(p, encoding="utf-8").read()
        else:
            table = sec
        rows = {}
        for line in table.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2 or not line.lstrip().startswith("|"):
                continue
            key = cells[0].lower()
            if key in rows or not key.startswith(("delegated", "application")):
                continue          # keep the first table (the primary provider)
            if len(cells) >= 3:   # newer format: least | higher
                rows[key] = (cells[1], cells[2])
            else:                 # older format: one cell, least to most privileged
                perms = [x.strip() for x in cells[1].split(",") if x.strip()]
                rows[key] = (perms[0] if perms else cells[1], ", ".join(perms[1:]))
        deleg = rows.get("delegated (work or school account)")
        app = rows.get("application")
        if not deleg and not app:
            continue
        # Required Entra role for delegated calls
        role = ""
        rb = re.search(r"\[!INCLUDE \[[^\]]*\]\((\.\./includes/rbac-for-apis/[^)]+)\)\]", sec)
        if rb:
            p = os.path.normpath(os.path.join(os.path.dirname(path), rb.group(1)))
            if os.path.isfile(p):
                rt = FM_RE.sub("", open(p, encoding="utf-8").read())
                bullets = re.findall(r"^>\s*-\s*(.+)$", rt, re.M)
                role = "; ".join(strip_md(b) for b in bullets) or strip_md(rt)[:300]
        else:
            imp = re.search(r"signed-in user must[^\n]*(?:\n>[^\n]*)*", sec)
            if imp:
                role = strip_md(imp.group(0).replace(">", " "))[:400]
        http = re.search(r"## HTTP request.*?```http\s*\n(.*?)```", body, re.S)
        req = " | ".join(l.strip() for l in http.group(1).strip().splitlines()[:2]) if http else ""
        name = os.path.basename(path)[:-3]
        url = f"https://learn.microsoft.com/en-us/graph/api/{name}?view=graph-rest-1.0"
        parts = [f"- **{title}** — `{req}`"]
        if deleg:
            parts.append(f"Delegated: {deleg[0]}" + (f" (higher: {deleg[1]})" if deleg[1] else ""))
        if app:
            parts.append(f"Application: {app[0]}" + (f" (higher: {app[1]})" if app[1] else ""))
        if role:
            parts.append(f"Signed-in user also needs Entra role: {role}")
        parts.append(url)
        lines.append(" — ".join(parts))
    write("graph-api-permissions.md", "Microsoft Graph v1.0: least-privileged permissions per API",
          "https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0",
          "One line per Graph v1.0 API: the least-privileged delegated and application permission, the higher-privileged alternatives, and (where Microsoft documents it) the Entra role the signed-in user must also hold for delegated calls. `Not supported.` means that permission type can't call the API. grep by resource name, HTTP path, or permission name.",
          lines)

# 2. Graph permission catalog: ID, consent, description -------------------------
def graph_permission_catalog():
    path = os.path.join(SRC, "graph/concepts/permissions-reference.md")
    text = open(path, encoding="utf-8", errors="ignore").read()
    lines = []
    for m in re.finditer(r"^### (\S+)\s*\n(.*?)(?=^### |\Z)", text, re.S | re.M):
        name, block = m.group(1), m.group(2)
        rows = {r[0].strip(): (r[1].strip(), r[2].strip()) for r in re.findall(r"^\|([^|\n]+)\|([^|\n]*)\|([^|\n]*)\|", block, re.M)}
        ids, desc, consent = rows.get("Identifier"), rows.get("Description"), rows.get("AdminConsentRequired")
        if not ids:
            continue
        name = name.strip()
        lines.append(f"- **{name}** — App ID: {ids[0]} · Delegated ID: {ids[1]} · Admin consent: app {consent[0] if consent else '?'}, delegated {consent[1] if consent else '?'}"
                     + (f" — {strip_md(desc[1] if desc[1] not in ('', '-') else desc[0])[:240]}" if desc else ""))
    write("graph-permission-catalog.md", "Microsoft Graph permissions catalog",
          "https://learn.microsoft.com/en-us/graph/permissions-reference",
          "Every Microsoft Graph permission with its application and delegated IDs (needed for app manifests and app-role assignments), whether admin consent is required, and what it allows. `-` means the permission doesn't exist in that form.",
          lines)

# 3. Entra built-in roles: template ID and privileged flag ----------------------
def entra_roles():
    path = os.path.join(SRC, "entra-docs/docs/identity/role-based-access-control/permissions-reference.md")
    text = open(path, encoding="utf-8").read()
    allroles = re.search(r"## All roles(.*?)\n## ", text, re.S).group(1)
    lines = []
    for name, anchor, desc, rid in re.findall(r"^>?\s*\|\s*\[([^\]]+)\]\(#([^)]+)\)\s*\|(.*?)\|\s*([0-9a-f-]{36})\s*\|", allroles, re.M):
        priv = "PRIVILEGED · " if "privileged-roles-permissions" in desc else ""
        lines.append(f"- **{name}** — `{rid}` — {priv}{strip_md(desc)[:260]} — https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#{anchor}")
    write("entra-roles.md", "Microsoft Entra built-in roles",
          "https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference",
          "Every Entra built-in role with its role template ID (use it in Conditional Access `includeRoles`, PIM and Graph role assignments) and Microsoft's PRIVILEGED flag. Full permission lists per role: references/entra-id/identity/role-based-access-control/permissions-reference.md.",
          lines)

# 4. Entra least-privileged role by task ----------------------------------------
def entra_tasks():
    path = os.path.join(SRC, "entra-docs/docs/identity/role-based-access-control/delegate-by-task.md")
    text = open(path, encoding="utf-8").read()
    lines = []
    for sec in re.split(r"^## ", text, flags=re.M)[1:]:
        area = sec.splitlines()[0].replace("least privileged roles", "").strip()
        for task, least, extra in re.findall(r"^>?\s*\|([^|\n]+)\|([^|\n]*)\|([^|\n]*)\|", sec, re.M):
            task, least, extra = strip_md(task), strip_md(least), strip_md(extra)
            if task.lower() in ("task", "") or set(task) <= set("-: "):
                continue
            lines.append(f"- [{area}] {task} → **{least}**" + (f" (also: {extra})" if extra else ""))
    write("entra-tasks.md", "Microsoft Entra: least-privileged role by task",
          "https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-by-task",
          "Microsoft's own mapping of Entra admin tasks to the least-privileged built-in role. Format: [Area] Task → **least-privileged role** (also: other roles that can do it).",
          lines)

# 5. Azure built-in roles --------------------------------------------------------
def azure_roles():
    path = os.path.join(SRC, "azure-docs/articles/role-based-access-control/built-in-roles.md")
    text = open(path, encoding="utf-8").read()
    lines, cat = [], ""
    for line in text.splitlines():
        h = re.match(r"^## (.+)", line)
        if h:
            cat = h.group(1).strip()
            continue
        m = re.match(r"^>?\s*\|\s*(?:<a name='[^']*'></a>)?\[([^\]]+)\]\(([^)]+)\)\s*\|(.*?)\|\s*([0-9a-f-]{36})\s*\|", line)
        if m:
            name, link, desc, rid = m.groups()
            if not link.startswith("http"):
                link = "https://learn.microsoft.com/en-us/azure/role-based-access-control/" + link.lstrip("./").replace(".md", "")
            lines.append(f"- [{cat}] **{name}** — `{rid}` — {strip_md(desc)[:260]} — {link}")
    write("azure-roles.md", "Azure built-in roles (Azure RBAC)",
          "https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles",
          "Every Azure built-in role with category, role definition ID and description. Exact Actions/DataActions per role: references/azure-governance/role-based-access-control/built-in-roles/<category>.md. Key Vault, Sentinel, AKS, Policy and Monitor roles are all here.",
          lines)

if __name__ == "__main__":
    graph_api_permissions()
    graph_permission_catalog()
    entra_roles()
    entra_tasks()
    azure_roles()
