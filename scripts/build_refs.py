#!/usr/bin/env python3
"""Convert Microsoft docs repo content into clean skill reference files.

Each output file starts with a source header (title, Learn URL, ms.date) and has
[!INCLUDE] fragments inlined, images removed and relative links made absolute.
Each product folder gets an INDEX.md listing every article with its description.
Re-run any time to refresh from upstream.
"""
import os, re, sys, glob, yaml, posixpath
from collections import defaultdict

SRC = os.environ.get("MS_DOCS_SRC", "/tmp/src")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/azure-sensei/references"
LEARN = "https://learn.microsoft.com/en-us"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
INC_RE = re.compile(r"\[!INCLUDE\s*\[[^\]]*\]\(([^)]+)\)\]", re.I)
IMG_RE = re.compile(r":::image[^\n]*?:::(?:.*?:::image-end:::)?|!\[[^\]]*\]\([^)]*\)", re.S)
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)(\s+\"[^\"]*\")?\)")

def split_fm(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    return fm, text[m.end():]

def inline_includes(body, path, depth=0, to_url=None):
    def rep(m):
        ref = m.group(1).strip()
        cands = []
        if ref.startswith("~/"):
            # "~" is the docset root; try the repo root and its usual docset folders
            repo = path[len(SRC) + 1:].split("/")[0]
            for root in ("", "docs", "articles", "microsoft-365"):
                cands.append(os.path.normpath(os.path.join(SRC, repo, root, ref[2:])))
        else:
            cands.append(os.path.normpath(os.path.join(os.path.dirname(path), ref)))
        target = next((c for c in cands if os.path.isfile(c)), None)
        if depth > 2 or not target:
            UNRESOLVED[ref.split("/")[1] if ref.startswith("~/") else "relative"] += 1
            if not ref.startswith("~/"): MISSING_REL[os.path.relpath(cands[0], SRC).split("/includes/")[0]] += 1
            return ""
        _, inc = split_fm(open(target, encoding="utf-8", errors="ignore").read())
        inc = inline_includes(inc, target, depth + 1, to_url)
        if to_url:
            # Links in an include are relative to the include file, not the article using it.
            repo_rel = os.path.relpath(target, SRC).split("/", 1)[1]
            def relink(lm):
                href = lm.group(2)
                h, _, frag = href.partition("#")
                if not h.endswith(".md") or h.startswith(("http", "/", "~")):
                    return lm.group(0)
                t = posixpath.normpath(posixpath.join(posixpath.dirname(repo_rel), h))
                return f"[{lm.group(1)}]({to_url(t)}" + (f"#{frag}" if frag else "") + ")"
            inc = LINK_RE.sub(relink, inc)
        return inc.strip()
    return INC_RE.sub(rep, body)

def fix_links(body, url_of_rel):
    def rep(m):
        text, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            if href.startswith("/"):
                href = "https://learn.microsoft.com" + href
            return f"[{text}]({href})"
        if href.startswith("/"):
            return f"[{text}](https://learn.microsoft.com/en-us{href})"
        if href.startswith("~/"):
            h, _, frag = href[2:].partition("#")
            h = h[:-3] if h.endswith(".md") else h
            return f"[{text}]({DOCSET_URL[0]}/{h}" + (f"#{frag}" if frag else "") + ")"
        return f"[{text}]({url_of_rel(href)})"
    body = LINK_RE.sub(rep, body)
    # Reference-style definitions: [label]: path
    def refdef(m):
        fake = LINK_RE.match(f"[x]({m.group(2)})")
        return m.group(1) + (rep(fake)[4:-1] if fake else m.group(2))
    return re.sub(r"^(\s*\[[^\]]+\]:\s*)(\S+)", refdef, body, flags=re.M)

def clean(body):
    body = COMMENT_RE.sub("", body)
    body = IMG_RE.sub("", body)
    body = re.sub(r"^>\s*\[!div[^\]]*\]\s*$", "", body, flags=re.M)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip() + "\n"

index = defaultdict(list)
UNRESOLVED = defaultdict(int)
MISSING_REL = defaultdict(int)   # product -> [(relpath, title, desc)]

def emit(product, relout, title, url, date, desc, body):
    dest = os.path.join(OUT, product, relout)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    head = f"# {title}\n\n> Source: {url}  \n> Microsoft doc last updated: {date or 'unknown'}\n\n"
    body = re.sub(r"^#\s+.*\n", "", body, count=1)  # drop duplicate H1
    with open(dest, "w", encoding="utf-8") as f:
        f.write(head + body)
    index[product].append((relout, title, (desc or "").replace("\n", " ").strip()))

DOCSET_URL = [LEARN]
GRAPH_KEEP = re.compile(r"^(conditionalaccess|.*namedlocation|authenticationstrength|authenticationcombination|unifiedrole|rbacapplication|privilegedaccessgroup|riskyuser|authenticationmethodspolicy)")
# Big lookup tables / changelogs that add size but rarely help an implementation guide.
# Their live Learn URLs are listed in SKILL.md instead.
NOISE = ("whats-new-archive", "licensing-service-plan-reference", "role-based-access-control/permissions/",
         "policy/samples/guest-configuration-baseline", "policy/samples/built-in-", "policy/samples/index",
         "azure-services-resource-providers", "resource-name-rules", "move-support-resources",
         "tag-support", "region-move-support", "/release-notes")
SKIP_DIRS = ("/includes/", "/media/", "/breadcrumb/", "/archive/", "/zone-pivots/")

def conceptual(repo_root, sub, product, url_base, strip_prefix, out_prefix=""):
    """url_base: Learn URL that strip_prefix maps onto."""
    root = os.path.join(SRC, repo_root)
    DOCSET_URL[0] = url_base
    for path in glob.glob(os.path.join(root, sub, "**/*.md"), recursive=True):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        if any(n in rel for n in NOISE):
            continue
        if any(s in "/" + rel for s in SKIP_DIRS) or rel.lower().endswith(("toc.md", "readme.md")):
            continue
        fm, body = split_fm(open(path, encoding="utf-8", errors="ignore").read())
        if not fm.get("title"):
            continue
        tail = rel[len(strip_prefix):] if rel.startswith(strip_prefix) else rel
        url = f"{url_base}/{tail[:-3]}"
        def url_of_rel(href, rel=rel):
            h, _, frag = href.partition("#")
            if h.endswith(".md"):
                target = posixpath.normpath(posixpath.join(posixpath.dirname(rel), h))
                t = target[len(strip_prefix):] if target.startswith(strip_prefix) else target
                return f"{url_base}/{t[:-3]}" + (f"#{frag}" if frag else "")
            return href
        to_url = lambda t: f"{url_base}/{(t[len(strip_prefix):] if t.startswith(strip_prefix) else t)[:-3]}"
        body = clean(fix_links(inline_includes(body, path, to_url=to_url), url_of_rel))
        emit(product, out_prefix + tail, fm.get("title"), url, fm.get("ms.date"), fm.get("description"), body)

def exchange_cmdlets():
    root = os.path.join(SRC, "office-docs-powershell/exchange/exchange-ps/ExchangePowerShell")
    for path in glob.glob(os.path.join(root, "*.md")):
        fm, body = split_fm(open(path, encoding="utf-8", errors="ignore").read())
        app = str(fm.get("applicable", ""))
        name = os.path.basename(path)[:-3]
        url = fm.get("online version") or f"https://learn.microsoft.com/powershell/module/exchangepowershell/{name.lower()}"
        body = clean(fix_links(body, lambda h: h))
        syn = re.search(r"## SYNOPSIS\s*\n(.*?)\n## ", body, re.S)
        desc = " ".join(syn.group(1).split())[:220] if syn else ""
        targets = []
        if "Exchange Online" in app:
            targets.append("exchange-online")
        if "Security & Compliance" in app:
            targets.append("purview")
        for p in targets:
            emit(p, f"cmdlets/{name}.md", name, url, fm.get("ms.date"), desc, body)

def cli_reference():
    root = os.path.join(SRC, "azure-docs-cli/docs-ref-autogen/Latest-version/latest")
    product_for = lambda g: ("aks" if g.startswith("aks") else "key-vault" if g.startswith("keyvault")
                             else "entra-id" if g.startswith(("ad", "identity")) else "azure-governance")
    for path in glob.glob(os.path.join(root, "**/*.yml"), recursive=True):
        rel = os.path.relpath(path, root)[:-4].replace(os.sep, "/")
        try:
            d = yaml.safe_load(open(path, encoding="utf-8"))
        except Exception:
            continue
        group = d.get("name") or "az " + rel.replace("/", " ")
        out = [f"{(d.get('summary') or '').strip()}\n"]
        if d.get("importantNote"):
            out.append(f"> {d['importantNote'].strip()}\n")
        subgroups = [c.get("name", c) if isinstance(c, dict) else c for c in d.get("commands") or []]
        if subgroups:
            out.append("Subgroups and commands: " + ", ".join(f"`{c}`" for c in subgroups) + "\n")
        def param_line(p):
            vals = p.get("parameterValueGroup")
            extra = f" Allowed: {vals}." if vals else ""
            dflt = p.get("defaultValue")
            extra += f" Default: {dflt}." if dflt not in (None, "") else ""
            summ = " ".join((p.get("summary") or "").split())[:300]
            return f"- `{p.get('name')}` — {summ}{extra}"
        for c in d.get("directCommands") or []:
            src = c.get("sourceType", "Core")
            status = c.get("status", "GA")
            tags = [t for t in (status if status != "GA" else "", "extension: aks-preview etc." if src == "Extension" else "") if t]
            out.append(f"## {c.get('name')}" + (f"  ({'; '.join(tags)})" if tags else "") + "\n")
            out.append((c.get("summary") or "").strip() + "\n")
            req = c.get("requiredParameters") or []
            if req:
                out.append("**Required parameters**\n")
                out += [param_line(p) for p in req]
                out.append("")
            opt = c.get("optionalParameters") or []
            if opt:
                out.append("**Optional parameters**\n")
                out += [param_line(p) for p in opt]
                out.append("")
            for ex in (c.get("examples") or []):
                out.append(f"*{(ex.get('summary') or '').strip()}*\n```azurecli\n{(ex.get('syntax') or '').strip()}\n```\n")
        url = f"https://learn.microsoft.com/en-us/cli/azure/{rel}"
        emit(product_for(rel), f"cli/{rel}.md", group, url, None, d.get("summary", ""), "\n".join(out))

def graph_reference():
    root = os.path.join(SRC, "graph/api-reference/v1.0")
    for path in glob.glob(os.path.join(root, "**/*.md"), recursive=True):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        if "/includes/" in "/" + rel:
            continue
        fm, body = split_fm(open(path, encoding="utf-8", errors="ignore").read())
        name = posixpath.basename(rel)[:-3]
        # Full pages only for the identity/CA APIs; every other API is covered by
        # references/permissions/graph-api-permissions.md (build_permissions.py).
        if not GRAPH_KEEP.match(name.lower()):
            continue
        kind = "resources/" if rel.startswith("resources/") else ""
        url = f"https://learn.microsoft.com/en-us/graph/api/{kind}{name}?view=graph-rest-1.0"
        low = name.lower()
        product = "conditional-access" if any(k in low for k in ("conditionalaccess", "namedlocation", "authenticationstrength", "authenticationcombination")) else "entra-id"
        body = re.sub(r"^# \[(C#|Go|Java|JavaScript|PHP|Python|CLI)\]\(#tab/\w+\)\n.*?(?=^# \[|^---\s*$)", "",
                      body, flags=re.S | re.M)
        body = re.sub(r"^\[!INCLUDE \[sdk-documentation\][^\n]*\n", "", body, flags=re.M)
        body = clean(fix_links(inline_includes(body, path), lambda h: h))
        emit(product, f"graph-api/{rel}", fm.get("title", name), url, fm.get("ms.date"), fm.get("description"), body)

def write_indexes():
    for product, items in index.items():
        groups = defaultdict(list)
        for rel, title, desc in sorted(items):
            groups[posixpath.dirname(rel) or "."].append((rel, title, desc))
        lines = [f"# {product} reference index\n",
                 f"{len(items)} documents. Search this file (grep) for keywords, then open the matching path.\n"]
        for g in sorted(groups):
            lines.append(f"\n## {g}\n")
            for rel, title, desc in groups[g]:
                lines.append(f"- `{rel}` — **{title}**" + (f" — {desc[:200]}" if desc else ""))
        with open(os.path.join(OUT, product, "INDEX.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    E = f"{LEARN}/entra"
    conceptual("entra-docs", "docs/identity/conditional-access", "conditional-access", E, "docs/", "")
    for sub in ["docs/identity/authentication", "docs/id-governance", "docs/id-protection", "docs/identity/hybrid",
                "docs/identity/enterprise-apps", "docs/identity/role-based-access-control",
                "docs/identity/monitoring-health", "docs/identity/users", "docs/fundamentals"]:
        conceptual("entra-docs", sub, "entra-id", E, "docs/")
    conceptual("azure-aks-docs", "articles/aks", "aks", f"{LEARN}/azure/aks", "articles/aks/")
    for sub in ["articles/azure-resource-manager/management", "articles/role-based-access-control",
                "articles/governance/policy", "articles/governance/management-groups"]:
        conceptual("azure-docs", sub, "azure-governance", f"{LEARN}/azure", "articles/")
    conceptual("office-docs-powershell", "exchange/docs-conceptual", "exchange-online",
               "https://learn.microsoft.com/en-us/powershell/exchange", "exchange/docs-conceptual/", "powershell-guides/")
    for sub in ["microsoft-365/admin", "microsoft-365/enterprise", "microsoft-365/baseline-security-mode", "microsoft-365/security"]:
        conceptual("microsoft-365-docs", sub, "m365-admin", f"{LEARN}/microsoft-365", "microsoft-365/")
    exchange_cmdlets()
    cli_reference()
    graph_reference()
    write_indexes()
    for p, items in sorted(index.items()):
        print(f"{p:20} {len(items):5} docs")
    print("unresolved includes:", dict(UNRESOLVED))
    for k,v in sorted(MISSING_REL.items(), key=lambda x:-x[1])[:12]: print(f"  {v:5} {k}")
