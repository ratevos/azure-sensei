#!/usr/bin/env python3
"""Fetch Microsoft Learn pages whose source repo isn't public (for example Purview DLP).

Learn returns a page's Markdown source when the request asks for text/markdown, so
these pages can be converted the same way build_refs.py converts repo content:
source header, images and comments removed, links made absolute. Which pages to
fetch is listed in learn_pages.txt (one TOC filter or single page per line).

Run it AFTER build_refs.py: it merges its entries into the product's INDEX.md
instead of overwriting it, and removes files for pages that left the TOC.

Usage: python3 fetch_learn.py ../references [learn_pages.txt]
"""
import os, re, sys, json, time, posixpath, urllib.request
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_refs as B  # reuses split_fm, fix_links, clean, emit

LEARN_HOST = "https://learn.microsoft.com"
ENTRY_RE = re.compile(r"^- `([^`]+)` — \*\*(.*?)\*\*(?: — (.*))?$")


def get(url, accept):
    req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "azure-sensei-docs-builder"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8")
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def toc_pages(toc_url, pattern):
    data = json.loads(get(toc_url, "application/json"))
    found = []
    def walk(items):
        for it in items:
            h = (it.get("href") or "").split("#")[0].split("?")[0]
            if h and not h.startswith(("/", "http", ".")) and re.search(pattern, h):
                found.append(h[:-3] if h.endswith(".md") else h)
            walk(it.get("children", []))
    walk(data.get("items", []))
    return sorted(set(found))


def convert(product, sub, page_url):
    md = get(page_url, "text/markdown")
    fm, body = B.split_fm(md)
    title = str(fm.get("title") or posixpath.basename(page_url)).removesuffix(" | Microsoft Learn")
    date = str(fm.get("ms.date") or "")[:10] or None
    base_path = posixpath.dirname(page_url[len(LEARN_HOST):])  # e.g. /en-us/purview
    B.DOCSET_URL[0] = LEARN_HOST + base_path

    def url_of_rel(href):
        h, _, frag = href.partition("#")
        h = h[:-3] if h.endswith(".md") else h
        full = posixpath.normpath(posixpath.join(base_path, h)) if h else page_url[len(LEARN_HOST):]
        return LEARN_HOST + full + (f"#{frag}" if frag else "")

    body = B.clean(B.fix_links(body, url_of_rel))
    body = re.sub(r"\[\s*\]\([^)]*\)", "", body)  # empty links left by lightbox images
    rel = f"{sub}/{posixpath.basename(page_url)}.md"
    B.emit(product, rel, title, page_url, date, fm.get("description"), body)
    return rel


def merge_index(product, owned_subs):
    """Rewrite INDEX.md: keep entries outside owned_subs, replace the rest with this run's."""
    path = os.path.join(B.OUT, product, "INDEX.md")
    items = {}
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            m = ENTRY_RE.match(line.rstrip("\n"))
            if m and not any(m.group(1).startswith(s + "/") for s in owned_subs):
                items[m.group(1)] = (m.group(2), m.group(3) or "")
    for rel, title, desc in B.index[product]:
        items[rel] = (title, (desc or "")[:200])
    groups = defaultdict(list)
    for rel in sorted(items):
        groups[posixpath.dirname(rel) or "."].append(rel)
    lines = [f"# {product} reference index\n",
             f"{len(items)} documents. Search this file (grep) for keywords, then open the matching path.\n"]
    for g in sorted(groups):
        lines.append(f"\n## {g}\n")
        for rel in groups[g]:
            title, desc = items[rel]
            lines.append(f"- `{rel}` — **{title}**" + (f" — {desc}" if desc else ""))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    B.OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "references"))
    cfg = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "learn_pages.txt")
    owned = defaultdict(set)    # product -> subfolders this run owns
    written = defaultdict(set)  # (product, sub) -> rel paths written
    failed = []
    for raw in open(cfg, encoding="utf-8"):
        line = raw.split("#", 1)[0].strip() if not raw.lstrip().startswith("#") else ""
        if not line:
            continue
        parts = [p.strip() for p in line.split("|", 3)]  # the regex column may contain '|'
        product, sub, url = parts[0], parts[1], parts[2]
        pattern = parts[3] if len(parts) > 3 else ""
        owned[product].add(sub)
        if url.endswith("toc.json"):
            base = url.rsplit("/", 1)[0]
            pages = [f"{base}/{p}" for p in toc_pages(url, pattern)]
        else:
            pages = [url]
        for page in pages:
            try:
                written[(product, sub)].add(convert(product, sub, page))
            except Exception as e:
                failed.append((page, str(e)[:120]))
            time.sleep(0.3)  # be polite to Learn
    for (product, sub), rels in written.items():
        folder = os.path.join(B.OUT, product, sub)
        for name in os.listdir(folder):  # drop pages that are no longer in the TOC
            if name.endswith(".md") and f"{sub}/{name}" not in rels:
                os.remove(os.path.join(folder, name))
    for product, subs in owned.items():
        merge_index(product, subs)
    for (product, sub), rels in sorted(written.items()):
        print(f"{product}/{sub:22} {len(rels):4} pages")
    for page, err in failed:
        print("FAILED", page, err)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
