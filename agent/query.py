#!/usr/bin/env python3
"""
query.py — Search wiki/ for a keyword or phrase and write a markdown report to output/.

This is a simple keyword search across all wiki pages. For semantic search,
an LLM agent should call this to get candidate pages, then synthesize the answer.

Usage:
    python agent/query.py "flash attention"
    python agent/query.py "memory bandwidth" --type concept
    python agent/query.py "HBM" --output output/my-report.md

Output:
    Writes a markdown report to output/<query-slug>-report.md (or --output path).
    Prints the output path to stdout.
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
WIKI_DIR = ROOT / "wiki"
OUTPUT_DIR = ROOT / "output"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")


def find_wiki_pages(page_type: str | None = None) -> list[Path]:
    pages = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        if path.name in ("AGENTS.md", "index.md"):
            continue
        if page_type:
            # Check frontmatter type field
            text = path.read_text()
            if f"type: {page_type}" not in text:
                continue
        pages.append(path)
    return pages


def search_page(path: Path, query: str) -> list[tuple[int, str]]:
    """Return list of (line_number, line_text) matches for query in path."""
    matches = []
    terms = query.lower().split()
    for i, line in enumerate(path.read_text().splitlines(), 1):
        line_lower = line.lower()
        if all(term in line_lower for term in terms):
            matches.append((i, line.strip()))
    return matches


def extract_frontmatter_field(text: str, field: str) -> str:
    """Extract a single-line frontmatter field value."""
    for line in text.splitlines():
        if line.startswith(field + ":"):
            return line.split(":", 1)[1].strip()
    return ""


def build_report(query: str, results: list[tuple[Path, list[tuple[int, str]]]]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Query Report: {query}",
        f"",
        f"**Query**: `{query}`  ",
        f"**Generated**: {now}  ",
        f"**Pages searched**: {len(find_wiki_pages())}  ",
        f"**Pages with matches**: {len(results)}",
        f"",
        "---",
        "",
    ]

    if not results:
        lines += [
            "## No Results Found",
            "",
            f"No wiki pages contain all terms: `{query}`",
            "",
            "Suggestions:",
            "- Try fewer or broader terms",
            "- Check if the concept has been compiled yet (`python agent/compile.py`)",
            "- Search raw/ directly: `grep -ri '<term>' raw/`",
        ]
        return "\n".join(lines)

    lines += [f"## Results ({len(results)} pages)\n"]

    for path, matches in results:
        text = path.read_text()
        title = extract_frontmatter_field(text, "title") or path.stem
        page_type = extract_frontmatter_field(text, "type")
        status = extract_frontmatter_field(text, "status")
        rel = path.relative_to(ROOT)

        lines += [
            f"### [[{path.stem}]]",
            f"",
            f"**File**: `{rel}`  ",
            f"**Type**: {page_type}  **Status**: {status}",
            f"",
            f"**Matching lines** ({len(matches)} hits):",
            "",
        ]
        for lineno, text_line in matches[:10]:  # cap at 10 matches per page
            lines.append(f"- Line {lineno}: `{text_line[:120]}`")
        if len(matches) > 10:
            lines.append(f"- ... and {len(matches) - 10} more matches")
        lines.append("")

    lines += [
        "---",
        "",
        "## Distillation Prompt",
        "",
        "After reviewing these results, if new reusable knowledge was found, run:",
        "```bash",
        f"python agent/distill.py output/<this-report-filename>",
        "```",
        "to extract insights back into wiki/.",
    ]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search wiki/ and write a query report")
    parser.add_argument("query", help="Search query (all terms must match)")
    parser.add_argument("--type", choices=["concept", "topic", "summary"],
                        help="Restrict search to a specific page type")
    parser.add_argument("--output", metavar="PATH", help="Output file path (default: auto-named)")
    args = parser.parse_args()

    query = args.query
    pages = find_wiki_pages(page_type=args.type)

    if not pages:
        print("No wiki pages found. Run `python agent/compile.py` first.", file=sys.stderr)
        sys.exit(1)

    results = []
    for page in pages:
        matches = search_page(page, query)
        if matches:
            results.append((page, matches))

    # Sort by match count descending
    results.sort(key=lambda x: len(x[1]), reverse=True)

    report = build_report(query, results)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if args.output:
        out_path = Path(args.output)
    else:
        out_path = OUTPUT_DIR / f"{slugify(query)}-report.md"

    out_path.write_text(report)
    print(f"Report written to: {out_path.relative_to(ROOT)}")
    print(f"Pages matched: {len(results)} / {len(pages)}")


if __name__ == "__main__":
    main()
