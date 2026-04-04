#!/usr/bin/env python3
"""
lint.py — Check wiki/ for structural issues.

Checks performed:
  1. Orphan pages — wiki pages not linked from any other page or index.md
  2. Broken [[links]] — links pointing to non-existent pages
  3. Empty sections — section headings with no content below them
  4. Missing frontmatter — pages without required YAML fields
  5. Unresolved [UNVERIFIED] on stable pages — stable pages should not have unverified claims

Usage:
    python agent/lint.py             # full report
    python agent/lint.py --strict    # exit 1 if any issues found (for CI)
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_DIR = ROOT / "wiki"
REQUIRED_FRONTMATTER = ["title", "type", "status", "sources"]


def find_wiki_pages() -> list[Path]:
    pages = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        if path.name == "AGENTS.md":
            continue
        pages.append(path)
    return pages


def extract_links(text: str) -> list[str]:
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def page_exists(name: str, all_pages: dict[str, Path]) -> bool:
    return name in all_pages


def build_page_map(pages: list[Path]) -> dict[str, Path]:
    """Map page stem → path."""
    return {p.stem: p for p in pages}


def extract_frontmatter(text: str) -> dict[str, str]:
    fields = {}
    in_fm = False
    for line in text.splitlines():
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                continue
            else:
                break
        if in_fm and ":" in line:
            key, _, val = line.partition(":")
            fields[key.strip()] = val.strip()
    return fields


def check_empty_sections(text: str) -> list[str]:
    """Return list of section headings that have no content (only whitespace or next heading)."""
    lines = text.splitlines()
    empty = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^#{2,6} ", line):  # skip H1 — it's just the page title
            heading = line.strip()
            # Check next non-empty lines
            j = i + 1
            has_content = False
            while j < len(lines):
                next_line = lines[j].strip()
                if not next_line:
                    j += 1
                    continue
                if next_line.startswith("<!--") or next_line.startswith("#"):
                    break
                has_content = True
                break
            if not has_content:
                empty.append(heading)
        i += 1
    return empty


def main():
    parser = argparse.ArgumentParser(description="Wiki linter")
    parser.add_argument("--strict", action="store_true", help="Exit 1 if issues found")
    args = parser.parse_args()

    pages = find_wiki_pages()
    page_map = build_page_map(pages)
    issues = []

    # Build reverse link map: page_stem → set of pages that link to it
    incoming_links: dict[str, set[str]] = {p.stem: set() for p in pages}
    all_outgoing: dict[str, list[str]] = {}

    for page in pages:
        text = page.read_text()
        links = extract_links(text)
        all_outgoing[page.stem] = links
        for link in links:
            if link not in incoming_links:
                incoming_links[link] = set()
            incoming_links[link].add(page.stem)

    print("# Wiki Lint Report\n")

    # --- Check 1: Broken links ---
    broken = []
    for page in pages:
        for link in all_outgoing.get(page.stem, []):
            if link not in page_map:
                broken.append((page.stem, link))

    if broken:
        print(f"## Broken [[links]] ({len(broken)})\n")
        for src, link in broken:
            print(f"  {src} → [[{link}]] (no page found)")
        print()
        issues.extend(broken)
    else:
        print("## Broken [[links]]: none\n")

    # --- Check 2: Orphan pages ---
    # index.md and AGENTS.md are exempt; a page is orphaned if nothing links to it
    orphans = []
    exempt = {"index", "AGENTS"}
    for page in pages:
        if page.stem in exempt:
            continue
        if not incoming_links.get(page.stem):
            orphans.append(page)

    if orphans:
        print(f"## Orphan Pages ({len(orphans)})\n")
        for page in orphans:
            print(f"  {page.relative_to(ROOT)} — not linked from any page")
        print()
        issues.extend(orphans)
    else:
        print("## Orphan Pages: none\n")

    # --- Check 3: Missing frontmatter ---
    fm_issues = []
    for page in pages:
        if page.stem in ("index",):
            continue
        text = page.read_text()
        fm = extract_frontmatter(text)
        missing_fields = [f for f in REQUIRED_FRONTMATTER if f not in fm]
        if missing_fields:
            fm_issues.append((page, missing_fields))

    if fm_issues:
        print(f"## Missing Frontmatter Fields ({len(fm_issues)} pages)\n")
        for page, fields in fm_issues:
            print(f"  {page.relative_to(ROOT)} — missing: {', '.join(fields)}")
        print()
        issues.extend(fm_issues)
    else:
        print("## Missing Frontmatter: none\n")

    # --- Check 4: [UNVERIFIED] in stable pages ---
    unverified_stable = []
    for page in pages:
        text = page.read_text()
        fm = extract_frontmatter(text)
        if fm.get("status") == "stable" and "[UNVERIFIED]" in text:
            count = text.count("[UNVERIFIED]")
            unverified_stable.append((page, count))

    if unverified_stable:
        print(f"## [UNVERIFIED] Claims in Stable Pages ({len(unverified_stable)} pages)\n")
        for page, count in unverified_stable:
            print(f"  {page.relative_to(ROOT)} — {count} unverified claim(s)")
        print()
        issues.extend(unverified_stable)
    else:
        print("## [UNVERIFIED] in Stable Pages: none\n")

    # --- Check 5: Empty sections ---
    empty_section_issues = []
    for page in pages:
        text = page.read_text()
        empty = check_empty_sections(text)
        # Filter out known template sections (from schema files, stubs)
        real_empty = [h for h in empty if "FILL IN" not in text[text.find(h):text.find(h)+200]]
        if real_empty:
            empty_section_issues.append((page, real_empty))

    if empty_section_issues:
        print(f"## Empty Sections ({sum(len(s) for _, s in empty_section_issues)} total)\n")
        for page, sections in empty_section_issues:
            for s in sections:
                print(f"  {page.relative_to(ROOT)} — {s}")
        print()
        issues.extend(empty_section_issues)
    else:
        print("## Empty Sections: none\n")

    # --- Summary ---
    total_issues = len(broken) + len(orphans) + len(fm_issues) + len(unverified_stable) + len(empty_section_issues)
    print(f"---\n")
    print(f"**Total issue groups: {total_issues}**")
    if total_issues == 0:
        print("Wiki is clean.")
    else:
        print("Run `python agent/distill.py` on relevant output reports to address these issues.")

    if args.strict and total_issues > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
