#!/usr/bin/env python3
"""
distill.py — Extract reusable knowledge from an output/ report and surface it for wiki updates.

This script does NOT write wiki pages directly (that requires LLM judgment).
Instead it:
  1. Parses an output/ report to find referenced wiki pages
  2. Identifies [[links]] that point to non-existent pages (stub candidates)
  3. Lists [UNVERIFIED] claims in matched pages
  4. Prints a distillation plan for an LLM agent to act on

The LLM agent reads this plan and then writes/updates wiki pages accordingly.

Usage:
    python agent/distill.py output/flash-attention-report.md
    python agent/distill.py output/flash-attention-report.md --plan-only
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_DIR = ROOT / "wiki"
OUTPUT_DIR = ROOT / "output"


def extract_links(text: str) -> list[str]:
    """Extract all [[PageName]] links from text."""
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def extract_unverified(text: str) -> list[tuple[int, str]]:
    """Find lines containing [UNVERIFIED]."""
    results = []
    for i, line in enumerate(text.splitlines(), 1):
        if "[UNVERIFIED]" in line:
            results.append((i, line.strip()))
    return results


def wiki_page_exists(name: str) -> Path | None:
    """Check if a wiki page exists. Returns path if found, None otherwise."""
    for subdir in (WIKI_DIR / "concepts", WIKI_DIR / "topics", WIKI_DIR / "summaries"):
        candidate = subdir / f"{name}.md"
        if candidate.exists():
            return candidate
    candidate = WIKI_DIR / f"{name}.md"
    if candidate.exists():
        return candidate
    return None


def find_mentioned_pages(report_text: str) -> list[str]:
    """Return page names mentioned in the report via [[links]]."""
    return list(dict.fromkeys(extract_links(report_text)))  # deduplicated, order preserved


def main():
    parser = argparse.ArgumentParser(description="Distillation planner for output/ reports")
    parser.add_argument("report", help="Path to output/ report file")
    parser.add_argument("--plan-only", action="store_true",
                        help="Only print the distillation plan, do not modify anything")
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        report_path = ROOT / args.report
    if not report_path.exists():
        print(f"Error: report not found: {args.report}", file=sys.stderr)
        sys.exit(1)

    report_text = report_path.read_text()
    rel_report = report_path.relative_to(ROOT) if report_path.is_relative_to(ROOT) else report_path

    print(f"# Distillation Plan")
    print(f"Source report: {rel_report}")
    print()

    # 1. Pages mentioned in the report
    mentioned = find_mentioned_pages(report_text)
    existing = [(name, wiki_page_exists(name)) for name in mentioned]
    missing = [(name, path) for name, path in existing if path is None]
    found = [(name, path) for name, path in existing if path is not None]

    print(f"## Pages Referenced in Report: {len(mentioned)}")
    for name, path in found:
        print(f"  EXISTS   [[{name}]] → {path.relative_to(ROOT)}")
    for name, _ in missing:
        print(f"  MISSING  [[{name}]] → no wiki page found")
    print()

    # 2. Stub candidates
    if missing:
        print(f"## Stub Candidates ({len(missing)} missing pages)")
        print("These [[links]] appear in the report but have no wiki page.")
        print("An LLM agent should create concept or topic pages for each.\n")
        for name, _ in missing:
            # Guess type by checking if it appears in concept vs topic pages
            print(f"  → Create: wiki/concepts/{name}.md  (or wiki/topics/{name}.md if broad)")
            print(f"    Template: schemas/concept.md")
            print(f"    Stub command: python agent/compile.py --stub <source-file>")
        print()

    # 3. Unverified claims in found pages
    unverified_total = []
    for name, path in found:
        if path is None:
            continue
        text = path.read_text()
        claims = extract_unverified(text)
        if claims:
            unverified_total.append((name, path, claims))

    if unverified_total:
        print(f"## [UNVERIFIED] Claims to Resolve ({sum(len(c) for _, _, c in unverified_total)} total)")
        for name, path, claims in unverified_total:
            print(f"\n  [[{name}]] ({path.relative_to(ROOT)}):")
            for lineno, line in claims:
                print(f"    Line {lineno}: {line[:120]}")
        print()

    # 4. Action summary
    print("## Suggested Actions for LLM Agent")
    print()
    if missing:
        print(f"1. Create {len(missing)} missing wiki pages:")
        for name, _ in missing:
            print(f"   - wiki/concepts/{name}.md  using schemas/concept.md")
    if unverified_total:
        n = sum(len(c) for _, _, c in unverified_total)
        print(f"2. Resolve {n} [UNVERIFIED] claims across {len(unverified_total)} pages")
    print(f"3. Update wiki/index.md if new pages are created")
    print(f"4. After wiki updates: git add wiki/ && git commit -m 'distill: <topic>'")
    print()
    print("Run `python agent/lint.py` after making changes to check for orphans and broken links.")


if __name__ == "__main__":
    main()
